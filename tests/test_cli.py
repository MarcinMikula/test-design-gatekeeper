"""Foundational CLI safety checks; partial TCND-I01-14/15 evidence only."""

import json
from pathlib import Path
import subprocess
import sys
import tomllib

import pytest

from tdg import __version__
from tdg.cli import main


def test_manifest_reports_only_implemented_cli_and_no_processing(capsys, monkeypatch):
    monkeypatch.setattr("tdg.windows_workspace.supported_host", lambda: False)
    assert main(["capabilities"]) == 0
    result = json.loads(capsys.readouterr().out)
    assert result["enabled_commands"] == ["version", "capabilities"]
    assert result["package_processing_enabled"] is False
    assert result["target_platform_verification"] == "W01_WINDOWS_TRIAL_PASSED_2026-09-28"
    assert result["implementation_stage"] == "W01_VERIFIED_CLOSURE_PENDING"
    assert set(result["disabled_commands"]) == {"init", "import", "receipt", "package"}
    assert {"core_minimum_check", "model_invocation", "sealed_processing", "tc_repair_or_approval"} <= set(
        result["disabled_capabilities"]
    )


@pytest.mark.parametrize("command", ["import", "receipt", "package"])
def test_disabled_commands_do_not_open_source_or_store(command, tmp_path, monkeypatch, capsys):
    source = tmp_path / "do-not-read.json"
    source.write_text("synthetic fixture; must remain unopened", encoding="utf-8")
    data_dir = tmp_path / "must-not-be-created"

    def forbidden_open(*args, **kwargs):
        pytest.fail("Disabled command attempted to open a path")

    monkeypatch.setattr("builtins.open", forbidden_open)
    monkeypatch.setattr("io.open", forbidden_open)
    monkeypatch.setattr("os.open", forbidden_open)
    monkeypatch.setattr("sqlite3.connect", forbidden_open)
    monkeypatch.setattr("os.mkdir", forbidden_open)
    code = main([command, "--input", str(source), "--data-dir", str(data_dir)])
    captured = capsys.readouterr()
    assert code == 3
    assert captured.out == ""
    assert captured.err == "CAPABILITY_NOT_ENABLED: see tdg capabilities.\n"
    assert not data_dir.exists()


def test_init_refuses_unsupported_host_before_creating_data(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr("tdg.windows_workspace.supported_host", lambda: False)
    target = tmp_path / "lab"
    assert main(["init", "--data-dir", str(target), "--profile", "laboratory", "--actor-ref", "qa"]) == 3
    assert capsys.readouterr().err == "WINDOWS_X64_PYTHON313_REQUIRED\n"
    assert not target.exists()


def test_sealed_profile_is_refused_before_host_or_path_access(monkeypatch, capsys):
    def unexpected_host_probe():
        pytest.fail("Profile should be refused first")
    monkeypatch.setattr("tdg.windows_workspace.supported_host", unexpected_host_probe)
    assert main(["init", "--profile", "sealed", "--actor-ref", "qa"]) == 3
    assert capsys.readouterr().err == "LABORATORY_PROFILE_REQUIRED\n"


@pytest.mark.parametrize("arguments", [["\x1b[2Jsecret"], ["version", "--secret=\x1b[2J"], []])
def test_invalid_arguments_do_not_echo_untrusted_values(arguments, capsys):
    with pytest.raises(SystemExit) as stopped:
        main(arguments)
    assert stopped.value.code == 2
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == "INVALID_ARGUMENTS: use tdg --help.\n"


def test_both_installed_entry_points_work_outside_repo_without_data_writes(tmp_path):
    console = Path(sys.executable).parent / ("tdg.exe" if sys.platform == "win32" else "tdg")
    outputs = []
    for command in ([sys.executable, "-m", "tdg", "version"], [str(console), "version"]):
        completed = subprocess.run(command, cwd=tmp_path, capture_output=True, text=True, timeout=10)
        assert completed.returncode == 0, completed.stderr
        assert completed.stderr == ""
        outputs.append(json.loads(completed.stdout))
    assert outputs[0] == outputs[1]
    assert outputs[0]["tdg"] == __version__
    assert outputs[0]["python"].startswith("3.13.")
    assert list(tmp_path.iterdir()) == []


def test_build_metadata_and_runtime_version_agree():
    project = Path(__file__).resolve().parents[1] / "pyproject.toml"
    with project.open("rb") as stream:
        metadata = tomllib.load(stream)
    assert metadata["project"]["version"] == __version__
