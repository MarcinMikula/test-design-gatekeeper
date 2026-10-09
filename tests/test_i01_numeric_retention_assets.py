"""Check exact numeric/text fixture observations, not TDG capture behavior.

The stdlib decoder exposes numeric lexemes as tagged test values; it never
converts them through float. Fractions below witness numeric differences only.
Neither representation is a proposed TDG implementation or a product oracle
derived from TDG output.
"""

import hashlib
import json
import re
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

import pytest


FIXTURES = Path(__file__).parent / "fixtures/i01"
MANIFEST = json.loads((FIXTURES / "numeric-retention/manifest.json").read_bytes())
CASES = MANIFEST["cases"]
POINTER = "/content/test_cases/0/test_data/n"
DIGITS = "1" + "0" * 128
EXPECTED = [
    ("TC-I01-019.01", "9007199254740993", "number"),
    ("TC-I01-019.02", "0.1000000000000000000001", "number"),
    ("TC-I01-019.03", "-0", "number"),
    ("TC-I01-020", '"' + DIGITS + '"', "string"),
]


@dataclass(frozen=True)
class NumberLexeme:
    text: str


def _unique_members(pairs):
    result = {}
    for name, value in pairs:
        assert name not in result, f"Duplicate fixture member: {name!r}"
        result[name] = value
    return result


def _nonfinite(token):
    raise AssertionError(f"Non-JSON fixture number: {token!r}")


def _decode(raw):
    assert not raw.startswith(b"\xef\xbb\xbf")
    return json.loads(raw.decode("utf-8", errors="strict"),
                      object_pairs_hook=_unique_members,
                      parse_int=NumberLexeme, parse_float=NumberLexeme,
                      parse_constant=_nonfinite)


def _measure(value, parent_depth=0):
    if isinstance(value, (dict, list)):
        depth = parent_depth + 1
        max_depth, nodes, text_bytes = depth, 1, 0
        if isinstance(value, dict):
            text_bytes = max((len(k.encode("utf-8")) for k in value), default=0)
            children = value.values()
        else:
            children = value
        for child in children:
            child_depth, child_nodes, child_text = _measure(child, depth)
            max_depth = max(max_depth, child_depth)
            nodes += child_nodes
            text_bytes = max(text_bytes, child_text)
        return max_depth, nodes, text_bytes
    # A numeric lexeme is a number, not a decoded JSON text value.
    return parent_depth, 1, len(value.encode("utf-8")) if isinstance(value, str) else 0


@pytest.mark.parametrize("case", CASES, ids=lambda c: c["id"])
def test_exact_bytes_and_independent_resource_measurements(case):
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
    assert len(raw) < 1_048_576 and depth < 32 and nodes < 20_000
    assert text < 65_536
    assert case["measurements"]["tc_entries"] == case["measurements"]["basis_entries"] == 1


@pytest.mark.parametrize("case, recipe", list(zip(CASES, EXPECTED, strict=True)),
                         ids=[entry[0] for entry in EXPECTED])
def test_exact_lexeme_location_and_isolated_mutation(case, recipe):
    case_id, lexeme, kind = recipe
    assert case["id"] == case_id
    raw = (FIXTURES / case["file"]).read_bytes()
    # Only these four small, deliberately fixed n members are recognized here.
    matches = list(re.finditer(rb',\n +"n": (?P<value>[^\r\n]+)(?=\n)', raw))
    assert len(matches) == 1
    match = matches[0]
    assert match.group("value") == lexeme.encode("ascii")
    assert case["source"] == {
        "kind": kind, "pointer": POINTER, "raw_lexeme": lexeme,
        "start_byte": match.start("value"), "end_byte": match.end("value"),
    }
    assert raw[case["source"]["start_byte"]:case["source"]["end_byte"]] == lexeme.encode("ascii")
    base = (FIXTURES / "base-01.json").read_bytes()
    assert raw[:match.start()] + raw[match.end():] == base
    doc = _decode(raw)
    supplied = doc["content"]["test_cases"][0]["test_data"].pop("n")
    assert supplied == (NumberLexeme(lexeme) if kind == "number" else DIGITS)
    assert doc == _decode(base)


@pytest.mark.parametrize("case", CASES[:3], ids=lambda c: c["id"])
def test_number_is_in_bound_and_lexically_distinct_from_lossy_witness(case):
    raw = (FIXTURES / case["file"]).read_bytes()
    lexeme = case["source"]["raw_lexeme"]
    assert len(lexeme) <= 128
    witnesses = {
        "TC-I01-019.01": ("9007199254740992", Fraction(9007199254740993)),
        "TC-I01-019.02": ("0.1", Fraction(10**21 + 1, 10**22)),
        "TC-I01-019.03": ("0", Fraction(0)),
    }
    changed, exact_value = witnesses[case["id"]]
    assert Fraction(lexeme) == exact_value
    start, end = case["source"]["start_byte"], case["source"]["end_byte"]
    counterpart = raw[:start] + changed.encode("ascii") + raw[end:]
    assert counterpart != raw
    assert hashlib.sha256(counterpart).hexdigest() != case["measurements"]["sha256"]
    changed_value = _decode(counterpart)["content"]["test_cases"][0]["test_data"]["n"]
    assert changed_value == NumberLexeme(changed)
    if case["id"] == "TC-I01-019.03":
        # Numeric equality is insufficient to establish source-lexeme fidelity.
        assert Fraction(changed) == exact_value
        assert counterpart == (FIXTURES / "syntax/control-number-zero.json").read_bytes()
    else:
        assert Fraction(changed) != exact_value


def test_129_digit_string_differs_from_numeric_limit_probe_only_by_quotes():
    case = CASES[3]
    raw = (FIXTURES / case["file"]).read_bytes()
    value = _decode(raw)["content"]["test_cases"][0]["test_data"]["n"]
    assert type(value) is str and value == DIGITS
    assert len(value.encode("utf-8")) == 129 < 65_536
    start, end = case["source"]["start_byte"], case["source"]["end_byte"]
    assert raw[start:end] == b'"' + DIGITS.encode("ascii") + b'"'
    unquoted = raw[:start] + raw[start + 1:end - 1] + raw[end:]
    assert unquoted == (FIXTURES / "numeric-token/TC-I01-018.03.json").read_bytes()
    number = _decode(unquoted)["content"]["test_cases"][0]["test_data"]["n"]
    assert number == NumberLexeme(DIGITS) and len(number.text) > 128


def test_manifest_covers_the_accepted_variants_levels_and_oracles():
    assert [c["id"] for c in CASES] == [recipe[0] for recipe in EXPECTED]
    assert {p.name for p in (FIXTURES / "numeric-retention").glob("TC-*.json")} == {
        f"{recipe[0]}.json" for recipe in EXPECTED
    }
    for case, (_, _, kind) in zip(CASES, EXPECTED, strict=True):
        number = kind == "number"
        assert case["file"] == f"numeric-retention/{case['id']}.json"
        assert case["levels"] == ["U", "I"] and case["evidence"] == ["E1", "E2"]
        assert case["oracles"] == (["OR-I01-SYN-005"] if number else ["OR-I01-FID-003", "OR-I01-SYN-004"])
        assert case["conditions"] == ["TCND-I01-05", "TCND-I01-06"] + ([] if number else ["TCND-I01-10"])
        assert case["expected_component"] == {
            "numeric_token_limit_applies_to_n": number,
            "within_numeric_token_limit": True if number else None,
            "decoded_text": None if number else DIGITS,
            "projection_policy": "exact_or_explicit_limitation_with_source_reference" if number else "preserve_string_without_numeric_conversion",
            "source_lexeme_and_locator_retained": True,
            "false_numeric_limit_violation": False,
        }
    assert MANIFEST["expected_full_capture"] == {
        "outcome": "CAPTURED", "new_package_version": True,
        "minimum": "NOT_EVALUATED", "minimum_reason": "MINIMUM_CHECK_NOT_ENABLED_IN_I01",
        "review_performed": False, "source_bytes_unchanged": True,
        "source_reference_resolves_to_retained_artifact": True,
    }
