"""Windows-only workspace admission and one-writer guard for empty-store init.

This initial build admits only direct children of LOCALAPPDATA/TDG/lab.
No input payload is inspected here. These are laboratory controls, not sealed
deployment qualification or an authenticated permission system.
"""

from contextlib import ExitStack, contextmanager
import ctypes
from ctypes import wintypes
import hashlib
import os
from pathlib import Path, PureWindowsPath
import platform
import re
import sys
from uuid import uuid4


class WorkspacePolicyError(Exception):
    pass


class WorkspaceOperationError(Exception):
    pass


class WorkspaceBusyError(Exception):
    pass


def supported_host() -> bool:
    return (
        sys.platform == "win32"
        and platform.machine().upper() in {"AMD64", "X86_64"}
        and platform.python_implementation() == "CPython"
        and sys.version_info[:2] == (3, 13)
        and sys.maxsize > 2**32
    )


def _normal_local_path(value: str) -> PureWindowsPath:
    """Reject network/device/relative/alias forms before opening any directory."""
    normalized = value.replace("/", "\\")
    if not re.match(r"^[A-Za-z]:\\", normalized):
        raise WorkspacePolicyError("LOCAL_ABSOLUTE_DATA_PATH_REQUIRED")
    parts = normalized[3:].split("\\")
    if any(
        not part
        or part in {".", ".."}
        or part.endswith((".", " "))
        or any(ord(char) < 32 or char in '<>:"|?*' for char in part)
        or re.match(r"^(CON|PRN|AUX|NUL|COM[1-9¹²³]|LPT[1-9¹²³])(?:\.|$)", part, re.IGNORECASE)
        for part in parts
    ):
        raise WorkspacePolicyError("UNSUPPORTED_DATA_PATH")
    return PureWindowsPath(normalized)


def select_workspace_path(
    local_appdata: str, requested: str | None, *, workspace_id: str, sync_roots: list[str]
) -> tuple[PureWindowsPath, PureWindowsPath]:
    """Pure policy decision, independently testable without Windows APIs."""
    base = _normal_local_path(local_appdata) / "TDG" / "lab"
    target = _normal_local_path(requested) if requested is not None else base / workspace_id
    if target.parent != base:
        raise WorkspacePolicyError("CUSTOM_DATA_ROOT_NOT_ENABLED")
    if target.name.casefold() == ".git":
        raise WorkspacePolicyError("REPOSITORY_DATA_PATH_REFUSED")
    for item in sync_roots:
        root = _normal_local_path(item)
        if target.is_relative_to(root):
            raise WorkspacePolicyError("SYNCHRONIZED_DATA_PATH_REFUSED")
    return base, target


def _known_sync_roots() -> list[str]:
    """Known operator environment and registered Windows sync providers only."""
    import winreg

    roots = [os.environ[key] for key in ("OneDrive", "OneDriveConsumer", "OneDriveCommercial") if os.environ.get(key)]
    registry_path = r"Software\Microsoft\Windows\CurrentVersion\Explorer\SyncRootManager"
    try:
        for hive in (winreg.HKEY_CURRENT_USER, winreg.HKEY_LOCAL_MACHINE):
            try:
                manager = winreg.OpenKey(hive, registry_path)
            except FileNotFoundError:
                continue
            with manager:
                for index in range(winreg.QueryInfoKey(manager)[0]):
                    provider = winreg.EnumKey(manager, index)
                    try:
                        users = winreg.OpenKey(manager, provider + r"\UserSyncRoots")
                    except FileNotFoundError:
                        continue
                    with users:
                        for value_index in range(winreg.QueryInfoKey(users)[1]):
                            _, value, value_type = winreg.EnumValue(users, value_index)
                            if value_type not in (winreg.REG_SZ, winreg.REG_EXPAND_SZ):
                                raise WorkspacePolicyError("SYNC_ROOT_INSPECTION_FAILED")
                            roots.append(os.path.expandvars(value))
    except OSError:
        raise WorkspacePolicyError("SYNC_ROOT_INSPECTION_FAILED") from None
    return roots


class _WindowsAPI:
    def __init__(self):
        self.kernel = ctypes.WinDLL("kernel32", use_last_error=True)
        definitions = {
            "CreateMutexW": ([ctypes.c_void_p, wintypes.BOOL, wintypes.LPCWSTR], wintypes.HANDLE),
            "WaitForSingleObject": ([wintypes.HANDLE, wintypes.DWORD], wintypes.DWORD),
            "ReleaseMutex": ([wintypes.HANDLE], wintypes.BOOL),
            "CloseHandle": ([wintypes.HANDLE], wintypes.BOOL),
            "GetDriveTypeW": ([wintypes.LPCWSTR], wintypes.UINT),
            "CreateFileW": ([wintypes.LPCWSTR, wintypes.DWORD, wintypes.DWORD, ctypes.c_void_p,
                             wintypes.DWORD, wintypes.DWORD, wintypes.HANDLE], wintypes.HANDLE),
            "GetFileInformationByHandle": ([wintypes.HANDLE, ctypes.c_void_p], wintypes.BOOL),
        }
        for name, (arguments, result) in definitions.items():
            function = getattr(self.kernel, name)
            function.argtypes = arguments
            function.restype = result

    @contextmanager
    def writer(self, path: Path):
        # No user-supplied name becomes a kernel-object name directly.
        identity = hashlib.sha256(str(path).casefold().encode("utf-8")).hexdigest()
        handle = self.kernel.CreateMutexW(None, False, "Global\\TDG-" + identity)
        if not handle:
            raise WorkspaceOperationError("WRITER_GUARD_UNAVAILABLE")
        acquired = False
        try:
            result = self.kernel.WaitForSingleObject(handle, 5000)
            if result == 258:  # WAIT_TIMEOUT
                raise WorkspaceBusyError("WORKSPACE_BUSY")
            if result not in (0, 128):  # WAIT_OBJECT_0 / WAIT_ABANDONED
                raise WorkspaceOperationError("WRITER_GUARD_FAILED")
            acquired = True
            # An abandoned mutex grants ownership, never proof of a prior commit.
            # The exclusive new-directory reservation still refuses prior data.
            yield
        finally:
            if acquired:
                self.kernel.ReleaseMutex(handle)
            self.kernel.CloseHandle(handle)

    @contextmanager
    def hold_directory(self, path: Path):
        # Metadata access; OPEN_EXISTING; no FILE_SHARE_DELETE; open the reparse
        # point itself. Keep ancestors and then the new workspace held until close.
        handle = self.kernel.CreateFileW(str(path), 0x01 | 0x80, 0x01 | 0x02, None, 3, 0x02000000 | 0x00200000, None)
        if handle in (None, ctypes.c_void_p(-1).value):
            raise WorkspaceOperationError("DATA_DIRECTORY_GUARD_FAILED")

        class FileInformation(ctypes.Structure):
            _fields_ = [
                ("attributes", wintypes.DWORD),
                ("created", wintypes.FILETIME),
                ("accessed", wintypes.FILETIME),
                ("written", wintypes.FILETIME),
                ("volume", wintypes.DWORD),
                ("size_high", wintypes.DWORD),
                ("size_low", wintypes.DWORD),
                ("links", wintypes.DWORD),
                ("index_high", wintypes.DWORD),
                ("index_low", wintypes.DWORD),
            ]

        try:
            info = FileInformation()
            if not self.kernel.GetFileInformationByHandle(handle, ctypes.byref(info)):
                raise WorkspaceOperationError("DATA_DIRECTORY_INSPECTION_FAILED")
            refused = 0x400 | 0x1000 | 0x40000 | 0x400000  # reparse / offline / recall
            if not info.attributes & 0x10 or info.attributes & refused:
                raise WorkspacePolicyError("REDIRECTED_OR_OFFLINE_DATA_PATH_REFUSED")
            if (path / ".git").exists():
                raise WorkspacePolicyError("REPOSITORY_DATA_PATH_REFUSED")
            yield
        finally:
            self.kernel.CloseHandle(handle)


def initialize_workspace(*, requested: str | None, actor_ref: str, profile: str):
    """CMP-01 orchestration; only CMP-06 initializes database records."""
    from tdg.storage import initialize_empty_store

    if profile != "laboratory":
        raise WorkspacePolicyError("LABORATORY_PROFILE_REQUIRED")
    if not actor_ref.strip():
        raise WorkspacePolicyError("ACTOR_REF_REQUIRED")
    if not supported_host():
        raise WorkspacePolicyError("WINDOWS_X64_PYTHON313_REQUIRED")
    appdata = os.environ.get("LOCALAPPDATA")
    if not appdata:
        raise WorkspacePolicyError("LOCAL_APPDATA_UNAVAILABLE")

    workspace_id = str(uuid4())
    base, target = select_workspace_path(appdata, requested, workspace_id=workspace_id, sync_roots=_known_sync_roots())
    base, target = Path(str(base)), Path(str(target))
    try:
        api = _WindowsAPI()
        if api.kernel.GetDriveTypeW(target.anchor) != 3:  # DRIVE_FIXED
            raise WorkspacePolicyError("LOCAL_FIXED_DRIVE_REQUIRED")
        with api.writer(target), ExitStack() as stack:
            # Lock from drive root down; create only TDG and lab, never an
            # arbitrary missing ancestor. Existing workspace creation is refused
            # by CMP-06. Directory guards prevent rename while writing the store.
            for ancestor in (*reversed(base.parents), base):
                if ancestor in (base.parent, base):
                    try:
                        ancestor.mkdir()
                    except FileExistsError:
                        pass
                stack.enter_context(api.hold_directory(ancestor))
            metadata = initialize_empty_store(
                target, actor_ref=actor_ref, workspace_id=workspace_id,
                directory_guard=api.hold_directory,
            )
        return metadata, target
    except OSError:
        raise WorkspaceOperationError("WORKSPACE_INITIALIZATION_FAILED") from None
