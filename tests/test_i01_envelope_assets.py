"""Check W02-C envelope data/oracles without exercising a TDG validator.

Mutations and expected partitions follow the accepted inventory independently
of the authoring script and of any future product implementation.
"""

import hashlib
import json
from decimal import Decimal
from pathlib import Path

import pytest


FIXTURES = Path(__file__).parent / "fixtures" / "i01"
MANIFEST = json.loads((FIXTURES / "envelope" / "manifest.json").read_bytes())
CASES = MANIFEST["cases"]
MARKER = "W02C_UNKNOWN_MARKER_012"
MISSING = {
    "TC-I01-011.01": "document_type",
    "TC-I01-011.02": "contract_version",
    "TC-I01-011.03": "content",
}
WRONG_TYPES = {
    "TC-I01-013.01": ("document_type", None),
    "TC-I01-013.02": ("document_type", 1),
    "TC-I01-013.03": ("contract_version", None),
    "TC-I01-013.04": ("contract_version", Decimal("1.0")),
    "TC-I01-013.05": ("content", None),
    "TC-I01-013.06": ("content", []),
    "TC-I01-013.07": ("content", "synthetic content"),
}
UNSUPPORTED = {
    "TC-I01-014.01": ("document_type", "review_export"),
    "TC-I01-014.02": ("document_type", "review_package_snapshot"),
    "TC-I01-014.03": ("document_type", "unknown-kind"),
    "TC-I01-014.04": ("contract_version", "999.0"),
}
ACCEPTED_ENVELOPES = {"TC-I01-012.02", "TC-I01-015"}


def _unique_members(pairs):
    result = {}
    for key, value in pairs:
        assert key not in result, f"Duplicate fixture member: {key!r}"
        result[key] = value
    return result


def _no_nonfinite(token):
    raise AssertionError(f"Non-JSON numeric token in envelope fixture: {token}")


def _decode(raw):
    assert not raw.startswith(b"\xef\xbb\xbf")
    numbers = []

    def number(token, converter):
        numbers.append(token)
        return converter(token)

    result = json.loads(
        raw.decode("utf-8", errors="strict"),
        object_pairs_hook=_unique_members,
        parse_int=lambda token: number(token, int),
        parse_float=lambda token: number(token, Decimal),
        parse_constant=_no_nonfinite,
    )
    assert all(len(token) < 128 for token in numbers)
    return result


def _tree_measurements(value, parent_depth=0):
    """Count containers/scalars once; member names contribute only text size."""
    if isinstance(value, (dict, list)):
        depth = parent_depth + 1
        max_depth, nodes, text_bytes = depth, 1, 0
        if isinstance(value, dict):
            text_bytes = max((len(key.encode("utf-8")) for key in value), default=0)
            children = value.values()
        else:
            assert len(value) <= 1  # All fixture arrays are well below item bounds.
            children = value
        for child in children:
            child_depth, child_nodes, child_text = _tree_measurements(child, depth)
            max_depth = max(max_depth, child_depth)
            nodes += child_nodes
            text_bytes = max(text_bytes, child_text)
        return max_depth, nodes, text_bytes
    return parent_depth, 1, len(value.encode("utf-8")) if isinstance(value, str) else 0


@pytest.mark.parametrize("case", CASES, ids=lambda case: case["id"])
def test_envelope_fixture_bytes_and_unrelated_limits(case):
    raw = (FIXTURES / case["file"]).read_bytes()
    depth, nodes, text_bytes = _tree_measurements(_decode(raw))
    assert case["measurements"] == {
        "byte_length": len(raw),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "container_depth": depth,
        "value_nodes": nodes,
        "max_decoded_text_bytes": text_bytes,
    }
    assert len(raw) < 1_048_576
    assert depth < 32
    assert nodes < 20_000
    assert text_bytes < 65_536


@pytest.mark.parametrize("case", CASES, ids=lambda case: case["id"])
def test_envelope_fixture_has_only_the_declared_mutation(case):
    base = _decode((FIXTURES / "base-01.json").read_bytes())
    document = _decode((FIXTURES / case["file"]).read_bytes())
    case_id = case["id"]
    if case_id in MISSING:
        field = MISSING[case_id]
        assert field not in document
        document[field] = base[field]
        assert document == base
    elif case_id in {"TC-I01-012.01", "TC-I01-012.02"}:
        target = document if case_id.endswith(".01") else document["content"]
        assert target.pop("synthetic_marker") == MARKER
        assert document == base
    elif case_id in WRONG_TYPES or case_id in UNSUPPORTED:
        field, value = (WRONG_TYPES | UNSUPPORTED)[case_id]
        assert type(document[field]) is type(value)
        assert document[field] == value
        document[field] = base[field]
        assert document == base
    elif case_id == "TC-I01-013.08":
        assert type(document) is list and document == [base]
    elif case_id == "TC-I01-013.09":
        assert type(document) is str and document == "synthetic scalar"
    elif case_id == "TC-I01-015":
        assert type(document["content"]) is dict and document["content"] == {}
        document["content"] = base["content"]
        assert document == base
    else:
        pytest.fail(f"No independent mutation check for {case_id}")


def test_manifest_keeps_inventory_order_levels_and_expected_outcomes():
    expected_ids = [
        *(f"TC-I01-011.{i:02}" for i in range(1, 4)),
        *(f"TC-I01-012.{i:02}" for i in range(1, 3)),
        *(f"TC-I01-013.{i:02}" for i in range(1, 10)),
        *(f"TC-I01-014.{i:02}" for i in range(1, 5)),
        "TC-I01-015",
    ]
    assert [case["id"] for case in CASES] == expected_ids
    assert len({case["file"] for case in CASES}) == 19
    assert {path.name for path in (FIXTURES / "envelope").glob("TC-*.json")} == {
        f"{case_id}.json" for case_id in expected_ids
    }
    for case in CASES:
        case_id = case["id"]
        assert case["file"] == f"envelope/{case_id}.json"
        accepted = case_id in ACCEPTED_ENVELOPES
        levels = ["U", "I"] if case_id.startswith("TC-I01-012.") else ["U", "C"]
        if case_id == "TC-I01-015":
            levels = ["U", "I", "C"]
        assert case["levels"] == levels
        expected = {
            "component": {"envelope_permits_next_stage": accepted},
            "full_capture": {
                "outcome": "CAPTURED" if accepted else "REJECTED",
                "new_package_version": accepted,
                "minimum": "NOT_EVALUATED",
                "review_performed": False,
            },
        }
        if "C" in levels:
            expected["cli"] = {"exit_code_on_successful_result_delivery": 0 if accepted else 2}
        assert case["expected"] == expected


def test_positive_cases_preserve_unknown_content_and_missing_dimensions():
    assert MANIFEST["base_fixture"] == "base-01.json"
    assert MANIFEST["additional_capture_observations"] == {
        "TC-I01-012.02": {
            "preserved_pointer": "/content/synthetic_marker",
            "raw_value": MARKER,
            "mapping_state_visible": True,
        },
        "TC-I01-015": {
            "absent_content_dimensions": ["scope", "basis_elements", "test_cases"],
            "minimum_reason": "MINIMUM_CHECK_NOT_ENABLED_IN_I01",
        },
    }
