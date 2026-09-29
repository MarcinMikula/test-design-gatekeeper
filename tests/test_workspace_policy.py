"""Pure admission rules; no assertion that mocks prove Windows kernel behavior."""

from pathlib import PureWindowsPath

import pytest

from tdg.windows_workspace import WorkspacePolicyError, select_workspace_path

APPDATA = r"C:\Users\qa\AppData\Local"
WORKSPACE_ID = "7d97d04d-954a-4173-97b3-42822a8dc62f"


def test_default_path_uses_managed_root_and_generated_workspace_identity():
    base, target = select_workspace_path(APPDATA, None, workspace_id=WORKSPACE_ID, sync_roots=[])
    assert base == PureWindowsPath(APPDATA) / "TDG" / "lab"
    assert target == base / WORKSPACE_ID


@pytest.mark.parametrize("requested", [
    r"\\server\share\lab",
    r"\\?\C:\Users\qa\AppData\Local\TDG\lab\workspace",
    r"C:relative",
    r"relative\workspace",
    r"C:\Users\qa\AppData\Local\TDG\lab\..\escape",
    r"C:\Users\qa\AppData\Local\TDG\lab\workspace.",
    r"C:\Users\qa\AppData\Local\TDG\lab\workspace ",
    r"C:\Users\qa\AppData\Local\TDG\lab\file:stream",
    r"C:\Users\qa\AppData\Local\TDG\lab\NUL.txt",
    r"C:\Users\qa\AppData\Local\TDG\lab\COM1",
    r"C:\Users\qa\AppData\Local\TDG\lab\COM¹",
    r"D:\arbitrary-root\workspace",
    r"C:\Users\qa\AppData\Local\TDG\lab\nested\workspace",
    r"C:\Users\qa\AppData\Local\TDG\lab\.git",
    "https://example.invalid/input",
])
def test_unsupported_path_refuses_before_filesystem_access(requested):
    with pytest.raises(WorkspacePolicyError):
        select_workspace_path(APPDATA, requested, workspace_id=WORKSPACE_ID, sync_roots=[])


def test_explicit_managed_child_is_allowed_case_insensitively():
    requested = r"c:\USERS\QA\APPDATA\LOCAL\tdg\LAB\qa-session"
    _, target = select_workspace_path(APPDATA, requested, workspace_id=WORKSPACE_ID, sync_roots=[])
    assert target == PureWindowsPath(requested)


def test_sync_root_containing_managed_workspace_is_refused():
    with pytest.raises(WorkspacePolicyError, match="^SYNCHRONIZED_DATA_PATH_REFUSED$"):
        select_workspace_path(APPDATA, None, workspace_id=WORKSPACE_ID,
                              sync_roots=[r"c:\users\qa\AppData"])


def test_similar_prefix_is_not_treated_as_same_sync_directory():
    _, target = select_workspace_path(APPDATA, None, workspace_id=WORKSPACE_ID,
                                      sync_roots=[r"C:\Users\qa\AppData\Local-other"])
    assert target.name == WORKSPACE_ID
