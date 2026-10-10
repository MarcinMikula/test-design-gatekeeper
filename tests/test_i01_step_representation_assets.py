"""Check step-representation fixtures independently of TDG product behavior.

Expected content/order comes from the accepted W02-B recipes. The mutations in
the witness checks are in-memory contrasts; original fixture files are untouched.
"""

import hashlib
import json
from pathlib import Path

import pytest


FIXTURES = Path(__file__).parent / "fixtures/i01"
MANIFEST = json.loads((FIXTURES / "step-representation/manifest.json").read_bytes())
CASES = MANIFEST["cases"]
POINTER = "/content/test_cases/0/steps"
NARRATIVE = (
    "1. Enter age 30.\n"
    "   Expected: The age field displays 30.\n"
    "2. Submit the registration form.\n"
    "   Expected: Registration is accepted."
)
ENTER = {"action": "Enter age 30.", "expected_result": "The age field displays 30."}
SUBMIT = {"action": "Submit the registration form.", "expected_result": "Registration is accepted."}
EXPECTED = [NARRATIVE, [ENTER, SUBMIT],
            [{"number": "02", **ENTER}, {"number": "02", **ENTER}, {"number": "01", **SUBMIT}]]


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
def test_exact_source_bytes_and_independent_measurements(case):
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
    assert len(raw) < 1_048_576 and depth < 32 and nodes < 20_000 and text < 65_536
    assert case["measurements"]["tc_entries"] == case["measurements"]["basis_entries"] == 1


@pytest.mark.parametrize("case, expected", list(zip(CASES, EXPECTED, strict=True)),
                         ids=[f"TC-I01-022.{i:02}" for i in range(1, 4)])
def test_only_steps_changes_and_its_raw_span_matches_the_fixed_recipe(case, expected):
    raw = (FIXTURES / case["file"]).read_bytes()
    base_raw = (FIXTURES / "base-01.json").read_bytes()
    prefix, suffix = b'        "steps": ', b',\n        "test_data": '
    assert raw.count(prefix) == raw.count(suffix) == 1
    assert base_raw.count(prefix) == base_raw.count(suffix) == 1
    start, end = raw.index(prefix) + len(prefix), raw.index(suffix)
    base_start, base_end = base_raw.index(prefix) + len(prefix), base_raw.index(suffix)
    assert raw[:start] == base_raw[:base_start] and raw[end:] == base_raw[base_end:]
    assert case["source"] == {
        "pointer": POINTER,
        "representation": "narrative_text" if isinstance(expected, str) else "array",
        "value_span": {"start_byte": start, "end_byte": end},
    }
    assert _decode(raw[start:end]) == expected == case["expected_steps"]
    doc, base_doc = _decode(raw), _decode(base_raw)
    item, base_item = doc["content"]["test_cases"][0], base_doc["content"]["test_cases"][0]
    assert type(item["steps"]) is type(expected)
    assert item.pop("steps") == expected
    base_item.pop("steps")
    assert "expected_result" not in item and doc == base_doc


def test_narrative_retains_lines_and_expectations_as_one_text_value():
    case = CASES[0]
    value = _item(case)["steps"]
    assert type(value) is str and value == NARRATIVE
    assert value.count("\n") == 3 and value.count("   Expected: ") == 2
    assert value.splitlines() == [
        "1. Enter age 30.", "   Expected: The age field displays 30.",
        "2. Submit the registration form.", "   Expected: Registration is accepted.",
    ]
    assert case["structured_step_count"] is None
    assert case["nested_expected_result_pointers"] == []
    raw = (FIXTURES / case["file"]).read_bytes()
    span = case["source"]["value_span"]
    assert raw[span["start_byte"]:span["end_byte"]].count(b"\\n") == 3


@pytest.mark.parametrize("case", CASES[1:], ids=lambda c: c["id"])
def test_structured_occurrences_keep_order_and_distinct_expectation_locations(case):
    steps = _item(case)["steps"]
    expected = EXPECTED[1 if case["id"].endswith(".02") else 2]
    assert type(steps) is list and steps == expected
    assert len(steps) == case["structured_step_count"]
    pointers = case["nested_expected_result_pointers"]
    assert pointers == [f"{POINTER}/{i}/expected_result" for i in range(len(steps))]
    assert len(set(pointers)) == len(steps)
    for index, step in enumerate(steps):
        assert step["expected_result"] == expected[index]["expected_result"]
    assert list(reversed(steps)) != expected
    assert "expected_result" not in _item(case)


def test_repeated_steps_and_supplied_numbers_distinguish_lossy_witnesses():
    case = CASES[2]
    steps = _item(case)["steps"]
    assert steps[0] == steps[1] and steps[1] != steps[2] and len(steps) == 3
    assert [step["number"] for step in steps] == ["02", "02", "01"] == case["supplied_array_numbers"]
    assert all(type(step["number"]) is str for step in steps)
    deduplicated = []
    for step in steps:
        if step not in deduplicated:
            deduplicated.append(step)
    assert len(deduplicated) == 2 and deduplicated != steps
    assert sorted(steps, key=lambda step: step["number"]) != steps
    renumbered = [{**step, "number": f"{i:02}"} for i, step in enumerate(steps, 1)]
    assert renumbered != steps


def test_manifest_matches_the_accepted_variants_levels_and_capture_oracle():
    ids = [f"TC-I01-022.{i:02}" for i in range(1, 4)]
    assert [case["id"] for case in CASES] == ids
    assert {path.name for path in (FIXTURES / "step-representation").glob("TC-*.json")} == {
        f"{case_id}.json" for case_id in ids
    }
    for case in CASES:
        assert case["file"] == f"step-representation/{case['id']}.json"
    assert [case["structured_step_count"] for case in CASES] == [None, 2, 3]
    assert [case["supplied_array_numbers"] for case in CASES] == [None, None, ["02", "02", "01"]]
    assert MANIFEST["levels"] == ["U", "I"] and MANIFEST["evidence"] == ["E1", "E2"]
    assert MANIFEST["oracles"] == ["OR-I01-FID-002"]
    assert MANIFEST["conditions"] == ["TCND-I01-01", "TCND-I01-06"]
    assert MANIFEST["expected_full_capture"] == {
        "outcome": "CAPTURED", "new_package_version": True,
        "minimum": "NOT_EVALUATED", "minimum_reason": "MINIMUM_CHECK_NOT_ENABLED_IN_I01",
        "review_performed": False, "source_bytes_unchanged": True,
        "original_representation_order_and_occurrences_preserved": True,
        "numbering_and_nested_expectations_preserved": True,
        "top_level_tc_expected_result_remains_absent": True,
        "no_invented_actions": True,
    }
