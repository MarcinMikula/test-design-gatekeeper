"""Verify the W02-C corpus, not TDG's unimplemented import behavior.

No TDG parser, projection or policy is used as the fixture oracle. JSON decoding
is deliberately limited to these four small, integer-only synthetic inputs.
"""

import hashlib
import json
import re
from pathlib import Path

import pytest


FIXTURES = Path(__file__).parent / "fixtures" / "i01"
MANIFEST = json.loads((FIXTURES / "numeric-token" / "manifest.json").read_bytes())
CASES = MANIFEST["cases"]
INPUTS = [MANIFEST["base"], *CASES]


def _unique_members(pairs):
    result = {}
    for key, value in pairs:
        assert key not in result, f"Duplicate fixture member: {key!r}"
        result[key] = value
    return result


def _unexpected_number(token):
    raise AssertionError(f"This integer-only fixture recipe has token {token!r}")


def _decode(raw):
    assert not raw.startswith(b"\xef\xbb\xbf")
    return json.loads(
        raw.decode("utf-8", errors="strict"),
        object_pairs_hook=_unique_members,
        parse_float=_unexpected_number,
        parse_constant=_unexpected_number,
    )


def _tree_measurements(value, parent_depth=0):
    """Root container depth 1; count values, excluding object member names."""
    if isinstance(value, (dict, list)):
        depth = parent_depth + 1
        max_depth, nodes, max_text = depth, 1, 0
        if isinstance(value, dict):
            max_text = max((len(key.encode("utf-8")) for key in value), default=0)
            children = value.values()
        else:
            children = value
        for child in children:
            child_depth, child_nodes, child_text = _tree_measurements(child, depth)
            max_depth = max(max_depth, child_depth)
            nodes += child_nodes
            max_text = max(max_text, child_text)
        return max_depth, nodes, max_text
    return parent_depth, 1, len(value.encode("utf-8")) if isinstance(value, str) else 0


@pytest.mark.parametrize("entry", INPUTS, ids=lambda entry: entry["id"])
def test_fixture_bytes_and_measurements(entry):
    raw = (FIXTURES / entry["file"]).read_bytes()
    document = _decode(raw)
    depth, nodes, text_bytes = _tree_measurements(document)
    measured = {
        "byte_length": len(raw),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "container_depth": depth,
        "value_nodes": nodes,
        "max_decoded_text_bytes": text_bytes,
        "tc_entries": len(document["content"]["test_cases"]),
        "basis_entries": len(document["content"]["basis_elements"]),
    }
    assert measured == entry["measurements"]
    assert set(document) == {"document_type", "contract_version", "content"}
    assert document["document_type"] == "review_package_input"
    assert document["contract_version"] == "1.0"
    assert isinstance(document["content"], dict)
    # These accepted bounds are independent test-basis values, not TDG imports.
    assert len(raw) < 1_048_576
    assert depth < 32
    assert nodes < 20_000
    assert text_bytes < 65_536
    assert measured["tc_entries"] == measured["basis_entries"] == 1


def test_base_matches_the_accepted_recipe():
    content = _decode((FIXTURES / MANIFEST["base"]["file"]).read_bytes())["content"]
    assert "customer-registration" in content["scope"]["description"]
    assert content["basis_elements"][0]["source_id"] == "BR-AGE-01"
    assert content["basis_elements"][0]["text"] == (
        "For this synthetic scenario, the supplied age is an integer. Values from "
        "18 through 120 inclusive are accepted; values outside this interval are rejected."
    )
    case = content["test_cases"][0]
    assert case["source_id"] == "TC-CREATE-01"
    assert case["origin"] == "HUMAN_AUTHORED"
    assert case["basis_refs"] == ["BR-AGE-01"]
    assert isinstance(case["preconditions"], str) and case["preconditions"].strip()
    assert case["test_data"] == {"age": 30}
    assert case["steps"] == [{
        "action": "Submit the registration form for a customer aged 30.",
        "expected_result": "Registration is accepted.",
    }]


@pytest.mark.parametrize("entry", CASES, ids=lambda entry: entry["id"])
def test_each_numeric_variant_changes_only_the_intended_token(entry):
    raw = (FIXTURES / entry["file"]).read_bytes()
    base_raw = (FIXTURES / MANIFEST["base"]["file"]).read_bytes()
    matches = list(re.finditer(rb',\n +"n": (?P<number>[0-9]+)(?=\n)', raw))
    assert len(matches) == 1
    match = matches[0]
    token = match.group("number")
    length = entry["token"]["length"]
    assert token == b"1" + b"0" * (length - 1)
    assert (match.start("number"), match.end("number")) == (
        entry["token"]["start_byte"], entry["token"]["end_byte"]
    )
    assert raw[:match.start()] + raw[match.end():] == base_raw
    decoded = _decode(raw)
    value = decoded["content"]["test_cases"][0]["test_data"].pop("n")
    assert type(value) is int and value == int(token)
    assert decoded == _decode(base_raw)


def test_oracles_follow_the_accepted_numeric_decision():
    assert MANIFEST["governing_decision"] == "SAD04-I01-NUM-001"
    assert MANIFEST["source_pointer"] == "/content/test_cases/0/test_data/n"
    assert [entry["id"] for entry in CASES] == [
        "TC-I01-018.01", "TC-I01-018.02", "TC-I01-018.03"
    ]
    assert [entry["token"]["length"] for entry in CASES] == [127, 128, 129]
    for entry, within_limit, outcome, code in zip(
        CASES, [True, True, False], ["CAPTURED", "CAPTURED", "REJECTED"], [0, 0, 2],
        strict=True,
    ):
        assert entry["expected"] == {
            "component": {"within_numeric_token_limit": within_limit},
            "full_capture": {
                "outcome": outcome,
                "new_package_version": within_limit,
                "minimum": "NOT_EVALUATED",
                "review_performed": False,
            },
            "cli": {"exit_code_on_successful_result_delivery": code},
        }
