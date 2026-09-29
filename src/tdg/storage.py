"""CMP-06 empty-store primitive, called through workspace admission.

Callers must supply an admitted, managed local directory. The Windows service
owns the path and writer guards; the CLI never calls this primitive directly.
Test-only use of a temporary Linux directory does not establish that boundary.
"""

from contextlib import ExitStack
from dataclasses import dataclass
from datetime import datetime, timezone
import os
from pathlib import Path
import sqlite3
from uuid import uuid4

from tdg import __version__
from tdg.capabilities import CONTRACT_VERSION, LAB_POLICY_VERSION, STORE_SCHEMA_VERSION

STORE_NAME = "workspace.sqlite3"
APPLICATION_ID = 0x54444731  # TDG1; store identification, not authentication.
STORE_LIMIT_BYTES = 512 * 1024 * 1024
WRITE_TIMEOUT_SECONDS = 5


class StoreError(Exception):
    """Metadata-only cause; never include raw database or input content."""


class StoreExistsError(StoreError):
    pass


class UnsupportedStoreError(StoreError):
    pass


@dataclass(frozen=True)
class WorkspaceMetadata:
    workspace_id: str
    schema_version: int
    profile: str
    actor_ref: str
    created_at_utc: str
    build_version: str
    contract_version: str
    policy_version: str


def _configure_writer(connection: sqlite3.Connection) -> None:
    connection.execute("PRAGMA foreign_keys = ON")
    journal_mode = connection.execute("PRAGMA journal_mode = DELETE").fetchone()[0]
    connection.execute("PRAGMA synchronous = FULL")
    page_size = connection.execute("PRAGMA page_size").fetchone()[0]
    # Only application-owned integers form PRAGMA expressions.
    max_pages = STORE_LIMIT_BYTES // page_size
    actual_max = connection.execute(f"PRAGMA max_page_count = {max_pages}").fetchone()[0]
    if (
        connection.execute("PRAGMA foreign_keys").fetchone()[0] != 1
        or journal_mode.lower() != "delete"
        or connection.execute("PRAGMA synchronous").fetchone()[0] != 2
        or actual_max != max_pages
        or connection.in_transaction
    ):
        raise StoreError("STORE_POLICY_NOT_ESTABLISHED")


def _insert_metadata(connection: sqlite3.Connection, metadata: WorkspaceMetadata) -> None:
    connection.execute(
        """CREATE TABLE workspace_meta (
            singleton INTEGER PRIMARY KEY CHECK (singleton = 1),
            workspace_id TEXT NOT NULL UNIQUE,
            schema_version INTEGER NOT NULL CHECK (schema_version = 1),
            profile TEXT NOT NULL CHECK (profile = 'laboratory'),
            actor_ref TEXT NOT NULL,
            created_at_utc TEXT NOT NULL,
            build_version TEXT NOT NULL,
            contract_version TEXT NOT NULL,
            policy_version TEXT NOT NULL
        ) STRICT"""
    )
    connection.execute(
        """INSERT INTO workspace_meta (
            singleton, workspace_id, schema_version, profile, actor_ref,
            created_at_utc, build_version, contract_version, policy_version
        ) VALUES (1, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (
            metadata.workspace_id,
            metadata.schema_version,
            metadata.profile,
            metadata.actor_ref,
            metadata.created_at_utc,
            metadata.build_version,
            metadata.contract_version,
            metadata.policy_version,
        ),
    )
    connection.execute(f"PRAGMA application_id = {APPLICATION_ID}")
    connection.execute(f"PRAGMA user_version = {STORE_SCHEMA_VERSION}")


def initialize_empty_store(data_dir: Path, *, actor_ref: str, workspace_id: str | None = None,
                           directory_guard=None) -> WorkspaceMetadata:
    """Create a fresh laboratory workspace in a caller-admitted parent.

    The parent must exist; the workspace directory must not exist, even if empty.
    On failure, retain the new partial workspace for diagnosis, never recreate
    or overwrite it automatically. This primitive does not admit external paths.
    """
    if not isinstance(actor_ref, str) or not actor_ref.strip():
        raise StoreError("ACTOR_REF_REQUIRED")
    metadata = WorkspaceMetadata(
        workspace_id=workspace_id if workspace_id is not None else str(uuid4()),
        schema_version=STORE_SCHEMA_VERSION,
        profile="laboratory",
        actor_ref=actor_ref,
        created_at_utc=datetime.now(timezone.utc).isoformat(),
        build_version=__version__,
        contract_version=CONTRACT_VERSION,
        policy_version=LAB_POLICY_VERSION,
    )
    connection = None
    directory_stack = ExitStack()
    try:
        # Atomic reservation; concurrent init never opens an existing store.
        data_dir.mkdir(mode=0o700, parents=False, exist_ok=False)
        if directory_guard is not None:
            directory_stack.enter_context(directory_guard(data_dir))
        database = data_dir / STORE_NAME
        fd = os.open(database, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
        os.close(fd)
        connection = sqlite3.connect(
            database,
            timeout=WRITE_TIMEOUT_SECONDS,
            autocommit=True,
        )
        _configure_writer(connection)
        connection.execute("BEGIN IMMEDIATE")
        _insert_metadata(connection, metadata)
        connection.execute("COMMIT")
        return metadata
    except FileExistsError:
        raise StoreExistsError("WORKSPACE_ALREADY_EXISTS") from None
    except (OSError, sqlite3.Error):
        raise StoreError("STORE_INITIALIZATION_FAILED") from None
    finally:
        try:
            if connection is not None:
                try:
                    if connection.in_transaction:
                        connection.execute("ROLLBACK")
                except sqlite3.Error:
                    # Preserve the original metadata-only failure. Close still
                    # releases the connection; no success was returned.
                    pass
                finally:
                    connection.close()
        finally:
            directory_stack.close()


def read_workspace_metadata(data_dir: Path) -> WorkspaceMetadata:
    """Read schema 1 with mode=ro; do not create, migrate or repair anything."""
    database_uri = (data_dir / STORE_NAME).absolute().as_uri() + "?mode=ro"
    connection = None
    try:
        connection = sqlite3.connect(database_uri, uri=True, autocommit=True)
        connection.execute("PRAGMA query_only = ON")
        if (
            connection.execute("PRAGMA user_version").fetchone()[0] != STORE_SCHEMA_VERSION
            or connection.execute("PRAGMA application_id").fetchone()[0] != APPLICATION_ID
        ):
            raise UnsupportedStoreError("UNSUPPORTED_STORE")
        if connection.execute("PRAGMA quick_check").fetchone() != ("ok",):
            raise StoreError("STORE_INTEGRITY_CHECK_FAILED")
        rows = connection.execute(
            """SELECT workspace_id, schema_version, profile, actor_ref,
                created_at_utc, build_version, contract_version, policy_version
                FROM workspace_meta"""
        ).fetchall()
        if len(rows) != 1 or rows[0][1] != STORE_SCHEMA_VERSION or rows[0][2] != "laboratory":
            raise StoreError("INVALID_WORKSPACE_METADATA")
        return WorkspaceMetadata(*rows[0])
    except (OSError, sqlite3.Error):
        raise StoreError("STORE_READ_FAILED") from None
    finally:
        if connection is not None:
            connection.close()
