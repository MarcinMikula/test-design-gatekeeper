"""Laboratory checks for the age BVA example and the RA-06 evidence boundary."""

import hashlib
import json
from pathlib import Path
import subprocess
import sys

import pytest

from tdg.cli import main


BASE = Path(__file__).parent / "fixtures" / "i01" / "base-01.json"
COMMAND = [
    "lab-age-bva", "--classification", "synthetic", "--actor-ref", "lab-qa",
    "--basis-id", "BR-AGE-01", "--confirmed-interval", "18", "120",
]


def run_lab(package, directory, *, installed=False):
    executable = Path(sys.executable).with_name("tdg.exe" if sys.platform == "win32" else "tdg")
    entry_point = [str(executable)] if installed else [sys.executable, "-m", "tdg"]
    data = package if isinstance(package, bytes) else json.dumps(package).encode("utf-8")
    return subprocess.run(
        [*entry_point, *COMMAND], input=data, capture_output=True, cwd=directory, timeout=10,
    )


def test_reports_missing_boundary_ages_with_source_locations(tmp_path):
    original = BASE.read_bytes()
    completed = run_lab(original, tmp_path, installed=True)
    assert completed.returncode == 0, completed.stderr
    assert completed.stderr == b""
    result = json.loads(completed.stdout)
    assert result["outcome"] == "ASSESSED"
    assert result["input_sha256"] == hashlib.sha256(original).hexdigest()
    assert result["basis_id"] == "BR-AGE-01"
    assert result["basis_locator"] == "/content/basis_elements/0/text"
    assert result["operator_interpretation"] == {"actor_ref": "lab-qa", "inclusive_age_interval": [18, 120]}
    assert result["target_ages"] == [17, 18, 120, 121]
    assert result["missing_ages"] == [17, 18, 120, 121]
    assert result["case_age_inputs"] == [
        {"case_id": "TC-CREATE-01", "age": 30, "locator": "/content/test_cases/0/test_data/age"},
    ]
    assert list(tmp_path.iterdir()) == []


def test_recognizes_a_complete_set_of_linked_boundary_ages(tmp_path):
    package = json.loads(BASE.read_bytes())
    original = package["content"]["test_cases"][0]
    package["content"]["test_cases"] = [
        {
            **original, "source_id": f"TC-AGE-{index}", "title": f"Register a customer aged {age}",
            "test_data": {"age": age},
            "steps": [{"action": f"Submit the registration form for a customer aged {age}."}],
        }
        for index, age in enumerate([17, 18, 120, 121, 121])
    ]
    completed = run_lab(package, tmp_path)
    assert completed.returncode == 0, completed.stderr
    result = json.loads(completed.stdout)
    assert result["outcome"] == "ASSESSED"
    assert result["missing_ages"] == []
    assert [item["age"] for item in result["case_age_inputs"]] == [17, 18, 120, 121, 121]


def test_excludes_inputs_explicitly_linked_to_a_different_rule(tmp_path):
    package = json.loads(BASE.read_bytes())
    content = package["content"]
    content["basis_elements"].append({"source_id": "BR-OTHER", "text": "A separate synthetic rule."})
    content["test_cases"].append({"basis_refs": ["BR-OTHER"], "test_data": {"age": 17}})
    completed = run_lab(package, tmp_path)
    assert completed.returncode == 0, completed.stderr
    result = json.loads(completed.stdout)
    assert result["outcome"] == "ASSESSED"
    assert result["excluded_cases"] == ["/content/test_cases/1"]
    assert result["missing_ages"] == [17, 18, 120, 121]


def test_withholds_assessment_for_an_unbound_test_source(tmp_path):
    package = json.loads(BASE.read_bytes())
    package["content"]["tc_sources"] = [{"binding_ref": "unsubmitted-cases"}]
    completed = run_lab(package, tmp_path)
    assert completed.returncode == 0, completed.stderr
    result = json.loads(completed.stdout)
    assert result["outcome"] == "UNGRADABLE"
    assert result["reason"] == "UNRESOLVED_SOURCE_BINDINGS"
    assert result["unresolved_locations"] == ["/content/tc_sources"]
    assert "missing_ages" not in result


@pytest.mark.parametrize("duplicate", [False, True], ids=["missing", "ambiguous"])
def test_withholds_gap_when_the_selected_rule_cannot_be_resolved(tmp_path, duplicate):
    package = json.loads(BASE.read_bytes())
    basis = package["content"]["basis_elements"]
    package["content"]["basis_elements"] = [*basis, *basis] if duplicate else []
    completed = run_lab(package, tmp_path)
    assert completed.returncode == 0, completed.stderr
    result = json.loads(completed.stdout)
    assert result["outcome"] == "UNGRADABLE"
    assert result["reason"] == ("BASIS_AMBIGUOUS" if duplicate else "BASIS_NOT_SUPPLIED")
    assert "missing_ages" not in result


@pytest.mark.parametrize("age", [True, "17", 17.0])
def test_withholds_gap_when_a_linked_age_is_unresolved(tmp_path, age):
    package = json.loads(BASE.read_bytes())
    original = package["content"]["test_cases"][0]
    package["content"]["test_cases"].append({**original, "test_data": {"age": age}})
    completed = run_lab(package, tmp_path)
    assert completed.returncode == 0, completed.stderr
    result = json.loads(completed.stdout)
    assert result["outcome"] == "UNGRADABLE"
    assert result["reason"] == "AGE_EVIDENCE_UNRESOLVED"
    assert result["unresolved_locations"] == ["/content/test_cases/1/test_data/age"]
    assert [item["age"] for item in result["case_age_inputs"]] == [30]
    assert "missing_ages" not in result


@pytest.mark.parametrize("data, error", [
    (b'{"content": {}, "content": {}}', b"INVALID_LAB_PACKAGE_JSON"),
    (b'{"age": NaN}', b"INVALID_LAB_PACKAGE_JSON"),
    (b'{"age": "\xff"}', b"INVALID_LAB_PACKAGE_JSON"),
    (b'{}', b"INVALID_LAB_PACKAGE_ENVELOPE"),
    (b" " * (64 * 1024 + 1), b"LAB_PACKAGE_TOO_LARGE"),
])
def test_rejects_unsupported_input_with_a_safe_diagnostic(tmp_path, data, error):
    completed = run_lab(data, tmp_path)
    assert completed.returncode == 2
    assert completed.stdout == b""
    assert completed.stderr.strip() == error


def test_refuses_non_synthetic_classification_before_reading_input(monkeypatch, capsys):
    class UnreadableInput:
        @property
        def buffer(self):
            pytest.fail("Laboratory input was accessed before admission")

    monkeypatch.setattr(sys, "stdin", UnreadableInput())
    arguments = ["confidential" if value == "synthetic" else value for value in COMMAND]
    assert main(arguments) == 3
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == "SYNTHETIC_CLASSIFICATION_REQUIRED\n"
