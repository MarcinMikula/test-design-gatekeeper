"""Inspect negative fixture bytes and valid controls, not TDG behavior.

Raw sources are never rewritten by these checks. In-memory counterparts only
establish that the deliberately introduced defect is isolated.
"""

import hashlib
import json
from pathlib import Path

import pytest


FIXTURES = Path(__file__).parent / "fixtures" / "i01"
MANIFEST = json.loads((FIXTURES / "syntax" / "manifest.json").read_bytes())
CASES = MANIFEST["cases"]
CONTROLS = {entry["id"]: entry for entry in MANIFEST["controls"]}


class ObjectPairs(list):
    """A JSON object whose decoded names and duplicate occurrences survive."""


class NonJSONNumber(ValueError):
    pass


def _no_nonfinite(token):
    raise NonJSONNumber(token)


def _unique_members(pairs):
    result = {}
    for key, value in pairs:
        assert key not in result, f"Duplicate control member: {key!r}"
        result[key] = value
    return result


def _decode_control(raw):
    assert not raw.startswith(b"\xef\xbb\xbf")

    def integer(token):
        assert len(token) < 128
        return int(token)

    return json.loads(
        raw.decode("utf-8", errors="strict"),
        object_pairs_hook=_unique_members,
        parse_int=integer,
        parse_constant=_no_nonfinite,
    )


def _measure_control(value, parent_depth=0):
    if isinstance(value, (dict, list)):
        depth = parent_depth + 1
        max_depth, nodes, text = depth, 1, 0
        if isinstance(value, dict):
            text = max((len(key.encode("utf-8")) for key in value), default=0)
            children = value.values()
        else:
            assert len(value) <= 1
            children = value
        for child in children:
            child_depth, child_nodes, child_text = _measure_control(child, depth)
            max_depth = max(max_depth, child_depth)
            nodes += child_nodes
            text = max(text, child_text)
        return max_depth, nodes, text
    return parent_depth, 1, len(value.encode("utf-8")) if isinstance(value, str) else 0


def _duplicates(value, pointer=""):
    found = []
    if isinstance(value, ObjectPairs):
        counts = {}
        for name, _ in value:
            counts[name] = counts.get(name, 0) + 1
        found.extend((pointer, name, count) for name, count in counts.items() if count > 1)
        for name, child in value:
            escaped = name.replace("~", "~0").replace("/", "~1")
            found.extend(_duplicates(child, pointer + "/" + escaped))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            found.extend(_duplicates(child, pointer + "/" + str(index)))
    return found


@pytest.mark.parametrize("entry", [*CONTROLS.values(), *CASES], ids=lambda e: e["id"])
def test_exact_raw_bytes(entry):
    raw = (FIXTURES / entry["file"]).read_bytes()
    assert entry["raw"] == {
        "byte_length": len(raw), "sha256": hashlib.sha256(raw).hexdigest()
    }
    assert len(raw) < 4096  # Even the whole source is far below intake/text bounds.


@pytest.mark.parametrize("entry", list(CONTROLS.values()), ids=lambda e: e["id"])
def test_valid_controls_and_their_measurements(entry):
    document = _decode_control((FIXTURES / entry["file"]).read_bytes())
    depth, nodes, text = _measure_control(document)
    assert entry["measurements"] == {
        "container_depth": depth, "value_nodes": nodes, "max_decoded_text_bytes": text
    }
    assert depth < 32 and nodes < 20_000 and text < 65_536
    base = _decode_control((FIXTURES / "base-01.json").read_bytes())
    data = document["content"]["test_cases"][0]["test_data"]
    if entry["id"] == "CTRL-SYN-NAME":
        assert data.pop("a") == "first"
    elif entry["id"] == "CTRL-SYN-NUMBER":
        assert type(data["n"]) is int and data.pop("n") == 0
    else:
        assert entry["id"] == "BASE-01"
    assert document == base


@pytest.mark.parametrize("case", CASES, ids=lambda c: c["id"])
def test_only_the_intended_mutation_separates_negative_and_control(case):
    raw = (FIXTURES / case["file"]).read_bytes()
    control = (FIXTURES / CONTROLS[case["control_id"]]["file"]).read_bytes()
    case_id = case["id"]
    if case_id == "TC-I01-016.01":
        member = b'  "document_type": "review_package_input",\n'
        assert raw.count(member) == 2
        second = raw.index(member, raw.index(member) + len(member))
        restored = raw[:second] + raw[second + len(member):]
    elif case_id in {"TC-I01-016.02", "TC-I01-016.03"}:
        extra = (
            b'        "title": "Second supplied title",\n'
            if case_id.endswith(".02") else b',\n          "\\u0061": "second"'
        )
        assert raw.count(extra) == 1
        restored = raw.replace(extra, b"", 1)
    elif case_id == "TC-I01-017.01":
        assert raw[:3] == b"\xef\xbb\xbf"
        restored = raw[3:]
    elif case_id == "TC-I01-017.02":
        offset = case["defect"]["byte_offset"]
        assert raw.count(b"\xff") == 1 and raw[offset:offset + 1] == b"\xff"
        assert control[offset:offset + 1] == b"R"
        restored = raw[:offset] + b"R" + raw[offset + 1:]
    elif case_id == "TC-I01-017.03":
        comment = b"  // W02C_COMMENT\n"
        assert raw.startswith(b"{\n" + comment)
        restored = raw[:2] + raw[2 + len(comment):]
    elif case_id == "TC-I01-017.04":
        assert raw.endswith(b"},\n}\n")
        restored = raw[:-4] + raw[-3:]
    else:
        tokens = {"TC-I01-017.05": b"NaN", "TC-I01-017.06": b"Infinity",
                  "TC-I01-017.07": b"-Infinity"}
        assert case_id in tokens
        member = b'"n": ' + tokens[case_id]
        assert raw.count(member) == 1
        restored = raw.replace(member, b'"n": 0', 1)
    assert restored == control
    _decode_control(restored)


@pytest.mark.parametrize("case", CASES[:3], ids=lambda c: c["id"])
def test_duplicate_detection_observation_preserves_decoded_occurrences(case):
    raw = (FIXTURES / case["file"]).read_bytes()
    pairs = json.loads(raw.decode("utf-8"), object_pairs_hook=ObjectPairs,
                       parse_constant=_no_nonfinite)
    defect = case["defect"]
    assert _duplicates(pairs) == [
        (defect["object_pointer"], defect["decoded_name"], defect["occurrences"])
    ]
    if case["id"] == "TC-I01-016.03":
        assert b'"a": "first"' in raw and b'"\\u0061": "second"' in raw
    control = (FIXTURES / CONTROLS[case["control_id"]]["file"]).read_bytes()
    assert _duplicates(json.loads(control, object_pairs_hook=ObjectPairs)) == []


@pytest.mark.parametrize("case", CASES[3:], ids=lambda c: c["id"])
def test_encoding_and_syntax_observations_distinguish_the_intended_cause(case):
    raw = (FIXTURES / case["file"]).read_bytes()
    kind = case["defect"]["kind"]
    if kind == "invalid_utf8":
        with pytest.raises(UnicodeDecodeError) as error:
            raw.decode("utf-8", errors="strict")
        assert error.value.start == case["defect"]["byte_offset"]
    elif kind == "leading_utf8_bom":
        assert raw.decode("utf-8").startswith("\ufeff")
        with pytest.raises(json.JSONDecodeError):
            json.loads(raw.decode("utf-8"))
    elif kind in {"comment", "trailing_comma"}:
        with pytest.raises(json.JSONDecodeError):
            json.loads(raw.decode("utf-8"))
    else:
        assert kind == "nonfinite_token"
        with pytest.raises(NonJSONNumber) as error:
            json.loads(raw.decode("utf-8"), parse_constant=_no_nonfinite)
        assert error.value.args == (case["defect"]["token"],)


def test_manifest_matches_the_accepted_variants_and_common_oracle():
    ids = [*(f"TC-I01-016.{i:02}" for i in range(1, 4)),
           *(f"TC-I01-017.{i:02}" for i in range(1, 8))]
    assert [case["id"] for case in CASES] == ids
    assert set(CONTROLS) == {"BASE-01", "CTRL-SYN-NAME", "CTRL-SYN-NUMBER"}
    assert {path.name for path in (FIXTURES / "syntax").glob("TC-*.json")} == {
        f"{case_id}.json" for case_id in ids
    }
    expected_defects = [
        {"kind": "duplicate_member", "object_pointer": "", "decoded_name": "document_type", "occurrences": 2},
        {"kind": "duplicate_member", "object_pointer": "/content/test_cases/0", "decoded_name": "title", "occurrences": 2},
        {"kind": "duplicate_member", "object_pointer": "/content/test_cases/0/test_data", "decoded_name": "a", "occurrences": 2},
        {"kind": "leading_utf8_bom"},
        {"kind": "invalid_utf8", "byte_offset": (FIXTURES / "base-01.json").read_bytes().index(b"Register a customer aged 30"), "invalid_byte_hex": "ff"},
        {"kind": "comment"}, {"kind": "trailing_comma"},
        *({"kind": "nonfinite_token", "source_pointer": "/content/test_cases/0/test_data/n", "token": token}
          for token in ["NaN", "Infinity", "-Infinity"]),
    ]
    for case, defect in zip(CASES, expected_defects, strict=True):
        assert case["file"] == f"syntax/{case['id']}.json"
        assert case["control_id"] in CONTROLS
        assert case["levels"] == ["U", "C"]
        assert case["defect"] == defect
    assert MANIFEST["expected_for_every_negative_case"] == {
        "component": {"native_syntax_profile_accepted": False, "observe_intended_cause": True},
        "full_capture": {"outcome": "REJECTED", "new_package_version": False,
                         "minimum": "NOT_EVALUATED", "review_performed": False},
        "cli": {"exit_code_on_successful_result_delivery": 2},
    }
