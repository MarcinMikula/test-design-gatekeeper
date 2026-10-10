"""Check duplicate-key data/locations, not TDG-generated identities or links.

Candidate observations enumerate supplied array positions. They do not resolve
product links, assign UUIDs or use TDG output as the expected result.
"""

import copy
import hashlib
import json
from pathlib import Path

import pytest


FIXTURES = Path(__file__).parent / "fixtures/i01"
MANIFEST = json.loads((FIXTURES / "source-id-collisions/manifest.json").read_bytes())
CASES = MANIFEST["cases"]
RECIPES = {
    "TC-I01-023.01": ("test_cases", "TC-CREATE-01", 2, 1),
    "TC-I01-023.02": ("basis_elements", "BR-AGE-01", 1, 2),
}


def _unique_members(pairs):
    result = {}
    for name, value in pairs:
        assert name not in result, f"Duplicate object member: {name!r}"
        result[name] = value
    return result


def _unexpected_number(token):
    raise AssertionError(f"Unexpected non-integer fixture token: {token!r}")


def _decode(raw):
    assert not raw.startswith(b"\xef\xbb\xbf")
    return json.loads(raw.decode("utf-8", errors="strict"),
                      object_pairs_hook=_unique_members,
                      parse_float=_unexpected_number, parse_constant=_unexpected_number)


def _measure(value, parent_depth=0):
    if isinstance(value, (dict, list)):
        depth = parent_depth + 1
        max_depth, nodes, text = depth, 1, 0
        if isinstance(value, dict):
            text = max((len(key.encode("utf-8")) for key in value), default=0)
            children = value.values()
        else:
            children = value
        for child in children:
            child_depth, child_nodes, child_text = _measure(child, depth)
            max_depth = max(max_depth, child_depth)
            nodes += child_nodes
            text = max(text, child_text)
        return max_depth, nodes, text
    return parent_depth, 1, len(value.encode("utf-8")) if isinstance(value, str) else 0


def _source_candidates(doc):
    """Small corpus observer: retain all matching positions, never pick one."""
    content = doc["content"]
    return [{
        "source_pointer": f"/content/test_cases/{tc_index}/basis_refs/{ref_index}",
        "supplied_value": ref,
        "candidate_source_pointers": [f"/content/basis_elements/{index}"
                                      for index, basis in enumerate(content["basis_elements"])
                                      if basis["source_id"] == ref],
    } for tc_index, tc in enumerate(content["test_cases"])
      for ref_index, ref in enumerate(tc["basis_refs"])]


@pytest.mark.parametrize("case", CASES, ids=lambda c: c["id"])
def test_exact_source_bytes_valid_json_and_resource_measurements(case):
    raw = (FIXTURES / case["file"]).read_bytes()
    doc = _decode(raw)  # Duplicate values across objects are valid JSON here.
    depth, nodes, text = _measure(doc)
    assert case["measurements"] == {
        "byte_length": len(raw), "sha256": hashlib.sha256(raw).hexdigest(),
        "container_depth": depth, "value_nodes": nodes,
        "max_decoded_text_bytes": text,
        "tc_entries": len(doc["content"]["test_cases"]),
        "basis_entries": len(doc["content"]["basis_elements"]),
    }
    assert set(doc) == {"document_type", "contract_version", "content"}
    assert doc["document_type"] == "review_package_input" and doc["contract_version"] == "1.0"
    assert len(raw) < 1_048_576 and depth < 32 and nodes < 20_000 and text < 65_536
    assert case["measurements"]["tc_entries"] < 200 and case["measurements"]["basis_entries"] < 200


@pytest.mark.parametrize("case", CASES, ids=lambda c: c["id"])
def test_two_identical_items_keep_separate_positions_and_only_one_is_added(case):
    collection, source_id, tc_count, basis_count = RECIPES[case["id"]]
    raw = (FIXTURES / case["file"]).read_bytes()
    base_raw = (FIXTURES / "base-01.json").read_bytes()
    doc, base = _decode(raw), _decode(base_raw)
    items = doc["content"][collection]
    assert case["duplicated_collection"] == collection and case["supplied_source_id"] == source_id
    assert len(items) == 2 and items[0] == items[1] == base["content"][collection][0]
    assert [item["source_id"] for item in items] == [source_id, source_id]
    assert case["item_pointers"] == [f"/content/{collection}/0", f"/content/{collection}/1"]
    assert (len(doc["content"]["test_cases"]), len(doc["content"]["basis_elements"])) == (tc_count, basis_count)
    first, second = case["item_byte_spans"]
    a, b = first["start_byte"], first["end_byte"]
    c, d = second["start_byte"], second["end_byte"]
    assert 0 <= a < b < c < d < len(raw) and raw[b:c] == b",\n"
    assert raw[:a] == base_raw[:a] and raw[:a].endswith(f'    "{collection}": [\n'.encode())
    assert raw[a:b] == raw[c:d] and _decode(raw[a:b]) == items[0]
    assert raw[:b] + raw[d:] == base_raw
    items.pop(1)
    assert doc == base


@pytest.mark.parametrize("case", CASES, ids=lambda c: c["id"])
def test_reference_candidates_distinguish_tc_collision_from_basis_ambiguity(case):
    _, _, tc_count, basis_count = RECIPES[case["id"]]
    doc = _decode((FIXTURES / case["file"]).read_bytes())
    expected = [{
        "source_pointer": f"/content/test_cases/{i}/basis_refs/0",
        "supplied_value": "BR-AGE-01",
        "candidate_source_pointers": [f"/content/basis_elements/{j}" for j in range(basis_count)],
    } for i in range(tc_count)]
    assert _source_candidates(doc) == expected
    assert case["reference_observations"] == [{
        **observation, "must_remain_ambiguous": basis_count == 2,
        "unique_target_if_resolved": "/content/basis_elements/0" if basis_count == 1 else None,
    } for observation in expected]


@pytest.mark.parametrize("case", CASES, ids=lambda c: c["id"])
def test_unique_key_witness_changes_only_the_second_supplied_id(case):
    collection, source_id, tc_count, _ = RECIPES[case["id"]]
    doc = _decode((FIXTURES / case["file"]).read_bytes())
    witness = copy.deepcopy(doc)
    replacement = "TC-CREATE-02" if collection == "test_cases" else "BR-AGE-02"
    witness["content"][collection][1]["source_id"] = replacement
    assert [item["source_id"] for item in witness["content"][collection]] == [source_id, replacement]
    candidates = _source_candidates(witness)
    assert len(candidates) == tc_count
    assert all(item["candidate_source_pointers"] == ["/content/basis_elements/0"] for item in candidates)
    witness["content"][collection][1]["source_id"] = source_id
    assert witness == doc


@pytest.mark.parametrize("case", CASES, ids=lambda c: c["id"])
def test_key_indexing_witness_would_erase_an_item_and_its_evidence(case):
    collection = case["duplicated_collection"]
    doc = _decode((FIXTURES / case["file"]).read_bytes())
    original_items = doc["content"][collection]
    lossy_by_key = {item["source_id"]: item for item in original_items}
    assert len(lossy_by_key) == 1 < len(original_items) == 2
    witness = copy.deepcopy(doc)
    witness["content"][collection] = list(lossy_by_key.values())
    assert witness != doc and _source_candidates(witness) != _source_candidates(doc)
    if collection == "basis_elements":
        assert len(_source_candidates(doc)[0]["candidate_source_pointers"]) == 2
        assert len(_source_candidates(witness)[0]["candidate_source_pointers"]) == 1


def test_manifest_matches_accepted_variants_levels_and_relational_oracles():
    assert [case["id"] for case in CASES] == list(RECIPES)
    assert {p.name for p in (FIXTURES / "source-id-collisions").glob("TC-*.json")} == {
        f"{case_id}.json" for case_id in RECIPES
    }
    for case in CASES:
        assert case["file"] == f"source-id-collisions/{case['id']}.json"
    assert MANIFEST["levels"] == ["U", "I"] and MANIFEST["evidence"] == ["E1", "E2"]
    assert MANIFEST["oracles"] == ["OR-I01-FID-007"] and MANIFEST["conditions"] == ["TCND-I01-06"]
    assert MANIFEST["expected_component"] == {
        "all_source_occurrences_preserved": True, "source_id_collision_visible": True,
        "no_source_id_repair_or_key_based_merge": True, "no_arbitrary_target_selection": True,
    }
    assert MANIFEST["expected_full_capture"] == {
        "outcome": "CAPTURED", "new_package_version": True,
        "minimum": "NOT_EVALUATED", "minimum_reason": "MINIMUM_CHECK_NOT_ENABLED_IN_I01",
        "review_performed": False, "source_bytes_unchanged": True,
        "duplicated_items_have_distinct_generated_internal_ids": True,
        "item_id_to_source_location_binding_survives_reopen": True,
    }
