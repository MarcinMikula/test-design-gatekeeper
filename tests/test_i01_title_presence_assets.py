"""Inspect the accepted seven title recipes, not a TDG presence classifier.

Expected presence states are fixed from W02-B / RA-09 before any TDG output.
These checks distinguish supplied values and absence; they do not implement
the future product's classification or prove durable capture.
"""

import hashlib
import json
import re
from pathlib import Path

import pytest


FIXTURES = Path(__file__).parent / "fixtures/i01"
MANIFEST = json.loads((FIXTURES / "title-presence/manifest.json").read_bytes())
CASES = MANIFEST["cases"]
MISSING = object()
RECIPES = {
    "TC-I01-021.01": (None, MISSING, "ABSENT"),
    "TC-I01-021.02": ("null", None, "NULL"),
    "TC-I01-021.03": ('""', "", "EMPTY"),
    "TC-I01-021.04": ('" \\t\\r\\n "', " \t\r\n ", "WHITESPACE_ONLY"),
    "TC-I01-021.05": ('"Register a customer aged 30"', "Register a customer aged 30", "VALUE"),
    "TC-I01-021.06": ("0", 0, "TYPE_MISMATCH"),
    "TC-I01-021.07": ("[]", [], "TYPE_MISMATCH"),
}


def _unique_members(pairs):
    result = {}
    for name, value in pairs:
        assert name not in result, f"Duplicate fixture member: {name!r}"
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


def _item(case):
    return _decode((FIXTURES / case["file"]).read_bytes())["content"]["test_cases"][0]


@pytest.mark.parametrize("case", CASES, ids=lambda c: c["id"])
def test_exact_bytes_envelope_and_resource_measurements(case):
    raw = (FIXTURES / case["file"]).read_bytes()
    doc = _decode(raw)
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
    assert case["measurements"]["tc_entries"] == case["measurements"]["basis_entries"] == 1


@pytest.mark.parametrize("case", CASES, ids=lambda c: c["id"])
def test_only_title_changes_with_exact_source_value_or_visible_absence(case):
    lexeme, expected_value, expected_presence = RECIPES[case["id"]]
    raw = (FIXTURES / case["file"]).read_bytes()
    base_raw = (FIXTURES / "base-01.json").read_bytes()
    pattern = rb'^        "title": (?P<value>[^\r\n]+),\n'
    base_matches = list(re.finditer(pattern, base_raw, flags=re.MULTILINE))
    assert len(base_matches) == 1
    base_match = base_matches[0]
    without_title = base_raw[:base_match.start()] + base_raw[base_match.end():]
    matches = list(re.finditer(pattern, raw, flags=re.MULTILINE))
    doc = _decode(raw)
    item = doc["content"]["test_cases"][0]
    if expected_value is MISSING:
        assert not matches and "title" not in item and raw == without_title
        assert case["source"] == {"member_present": False, "raw_lexeme": None, "value_span": None}
    else:
        assert len(matches) == 1 and "title" in item
        match = matches[0]
        assert match.group("value") == lexeme.encode("ascii")
        assert raw[:match.start()] + raw[match.end():] == without_title
        assert type(item["title"]) is type(expected_value)
        assert item.pop("title") == expected_value
        assert case["source"] == {
            "member_present": True, "raw_lexeme": lexeme,
            "value_span": {"start_byte": match.start("value"), "end_byte": match.end("value")},
        }
    assert case["expected_presence"] == expected_presence
    assert doc == _decode(without_title)


def test_absence_and_explicit_null_have_different_source_evidence():
    absent, supplied_null = CASES[:2]
    assert "title" not in _item(absent)
    assert "title" in _item(supplied_null) and _item(supplied_null)["title"] is None
    assert absent["source"]["value_span"] is None
    span = supplied_null["source"]["value_span"]
    raw = (FIXTURES / supplied_null["file"]).read_bytes()
    assert raw[span["start_byte"]:span["end_byte"]] == b"null"
    assert [absent["expected_presence"], supplied_null["expected_presence"]] == ["ABSENT", "NULL"]


def test_falsy_values_do_not_imply_one_presence_state():
    selected = [CASES[i] for i in (1, 2, 5, 6)]
    values = [_item(case)["title"] for case in selected]
    assert [type(value) for value in values] == [type(None), str, int, list]
    assert values == [None, "", 0, []] and all(not value for value in values)
    assert [case["expected_presence"] for case in selected] == [
        "NULL", "EMPTY", "TYPE_MISMATCH", "TYPE_MISMATCH"
    ]


def test_whitespace_is_nonempty_and_its_characters_are_preserved():
    case = CASES[3]
    value = _item(case)["title"]
    assert type(value) is str and [ord(char) for char in value] == [32, 9, 13, 10, 32]
    assert value and value.isspace() and value != _item(CASES[2])["title"]
    raw = (FIXTURES / case["file"]).read_bytes()
    span = case["source"]["value_span"]
    assert raw[span["start_byte"]:span["end_byte"]] == b'" \\t\\r\\n "'


def test_value_variant_reuses_the_existing_control_bytes():
    assert CASES[4]["expected_presence"] == "VALUE"
    assert (FIXTURES / CASES[4]["file"]).read_bytes() == (FIXTURES / "base-01.json").read_bytes()


def test_manifest_matches_accepted_variants_levels_and_capture_oracle():
    assert [case["id"] for case in CASES] == list(RECIPES)
    assert {path.name for path in (FIXTURES / "title-presence").glob("TC-*.json")} == {
        f"{case_id}.json" for case_id in RECIPES
    }
    for case in CASES:
        assert case["file"] == f"title-presence/{case['id']}.json"
    assert MANIFEST["target_field_pointer"] == "/content/test_cases/0/title"
    assert MANIFEST["containing_item_pointer"] == "/content/test_cases/0"
    assert MANIFEST["levels"] == ["U", "I"] and MANIFEST["evidence"] == ["E1", "E2"]
    assert MANIFEST["oracles"] == ["OR-I01-FID-001", "OR-I01-FID-004"]
    assert MANIFEST["conditions"] == ["TCND-I01-06"]
    assert MANIFEST["expected_full_capture"] == {
        "outcome": "CAPTURED", "new_package_version": True,
        "minimum": "NOT_EVALUATED", "minimum_reason": "MINIMUM_CHECK_NOT_ENABLED_IN_I01",
        "review_performed": False, "source_bytes_unchanged": True,
        "deficiency_preserved_without_filling_or_coercion": True,
    }
