"""Real Windows checks. Skips are outstanding evidence, never passes."""

import subprocess
import sys

import pytest

from tdg import storage
from tdg.windows_workspace import _WindowsAPI, initialize_workspace, supported_host

pytestmark = pytest.mark.skipif(not supported_host(), reason="Requires real Windows x64 / CPython 3.13")


def test_windows_init_roundtrip_and_no_overwrite(tmp_path, monkeypatch):
    monkeypatch.setenv("LOCALAPPDATA", str(tmp_path))
    metadata, target = initialize_workspace(requested=None, actor_ref="qa-lab", profile="laboratory")
    assert target == tmp_path / "TDG" / "lab" / metadata.workspace_id
    assert storage.read_workspace_metadata(target) == metadata
    before = (target / storage.STORE_NAME).read_bytes()
    with pytest.raises(storage.StoreExistsError):
        initialize_workspace(requested=str(target), actor_ref="qa-other", profile="laboratory")
    assert (target / storage.STORE_NAME).read_bytes() == before


def test_windows_mutex_blocks_a_second_process(tmp_path):
    code = """
import sys
from pathlib import Path
from tdg.windows_workspace import _WindowsAPI, WorkspaceBusyError
try:
    with _WindowsAPI().writer(Path(sys.argv[1])):
        raise SystemExit(91)
except WorkspaceBusyError:
    raise SystemExit(0)
"""
    with _WindowsAPI().writer(tmp_path / "workspace"):
        completed = subprocess.run([sys.executable, "-c", code, str(tmp_path / "workspace")],
                                   capture_output=True, text=True, timeout=12)
    assert completed.returncode == 0, completed.stderr


def test_windows_directory_cannot_be_renamed_while_held(tmp_path):
    folder = tmp_path / "guarded"
    folder.mkdir()
    with _WindowsAPI().hold_directory(folder):
        with pytest.raises(OSError):
            folder.rename(tmp_path / "redirected")
    assert folder.is_dir()


def test_windows_reparse_directory_is_refused(tmp_path):
    from tdg.windows_workspace import WorkspacePolicyError

    source = tmp_path / "junction"
    destination = tmp_path / "destination"
    destination.mkdir()
    assert not any(char in str(source) + str(destination) for char in '%!&|<>^"\r\n'), "Unsafe cmd.exe fixture path"
    # mklink /J does not require developer-mode symlink privileges. cmd.exe is
    # used only for this test fixture, never by the TDG processing path.
    completed = subprocess.run(["cmd.exe", "/d", "/c", "mklink", "/J", str(source), str(destination)],
                               capture_output=True, text=True, timeout=10)
    assert completed.returncode == 0, "Windows junction fixture could not be created"
    try:
        with pytest.raises(WorkspacePolicyError, match="^REDIRECTED_OR_OFFLINE_DATA_PATH_REFUSED$"):
            with _WindowsAPI().hold_directory(source):
                pytest.fail("Junction was admitted")
    finally:
        source.rmdir()  # Removes the junction only; destination belongs to tmp_path.
