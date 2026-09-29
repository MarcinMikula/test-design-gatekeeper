"""Initial partial evidence for SAD-04 TCND-I01-12/13; not full conditions."""

import hashlib
from contextlib import contextmanager
import sqlite3
from uuid import UUID

import pytest

from tdg import storage


def test_new_store_survives_close_and_contains_only_workspace_metadata(tmp_path):
    workspace = tmp_path / "lab"
    actor = "qa'; DROP TABLE workspace_meta; --"
    created = storage.initialize_empty_store(workspace, actor_ref=actor)

    # Reopen through a separate read-only connection; inspect durable SQL state.
    loaded = storage.read_workspace_metadata(workspace)
    assert loaded == created
    assert UUID(loaded.workspace_id).version == 4
    assert loaded.actor_ref == actor
    assert loaded.profile == "laboratory"
    assert loaded.schema_version == 1
    connection = sqlite3.connect((workspace / storage.STORE_NAME).as_uri() + "?mode=ro", uri=True)
    try:
        tables = connection.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
        assert tables == [("workspace_meta",)]  # No fabricated reviews or packages.
        assert connection.execute("PRAGMA journal_mode").fetchone() == ("delete",)
        assert connection.execute("PRAGMA user_version").fetchone() == (1,)
        assert connection.execute("PRAGMA integrity_check").fetchone() == ("ok",)
    finally:
        connection.close()


@pytest.mark.parametrize("existing_content", [None, b"existing unknown or corrupt store\x00\xff"])
def test_existing_workspace_is_never_overwritten(tmp_path, existing_content):
    workspace = tmp_path / "existing"
    workspace.mkdir()
    database = workspace / storage.STORE_NAME
    if existing_content is not None:
        database.write_bytes(existing_content)

    with pytest.raises(storage.StoreExistsError, match="^WORKSPACE_ALREADY_EXISTS$"):
        storage.initialize_empty_store(workspace, actor_ref="qa-01")

    assert database.exists() is (existing_content is not None)
    if existing_content is not None:
        assert database.read_bytes() == existing_content


def test_reinitialization_preserves_original_identity_and_bytes(tmp_path):
    workspace = tmp_path / "lab"
    metadata = storage.initialize_empty_store(workspace, actor_ref="qa-01")
    database = workspace / storage.STORE_NAME
    before = database.read_bytes()
    with pytest.raises(storage.StoreExistsError):
        storage.initialize_empty_store(workspace, actor_ref="qa-02")
    assert database.read_bytes() == before
    assert storage.read_workspace_metadata(workspace) == metadata


@pytest.mark.parametrize("existing_directory", [False, True])
def test_read_missing_store_never_creates_it(tmp_path, existing_directory):
    workspace = tmp_path / "missing"
    if existing_directory:
        workspace.mkdir()
    with pytest.raises(storage.StoreError, match="^STORE_READ_FAILED$"):
        storage.read_workspace_metadata(workspace)
    assert workspace.exists() is existing_directory
    assert not (workspace / storage.STORE_NAME).exists()


def test_read_unknown_schema_refuses_without_mutation(tmp_path):
    workspace = tmp_path / "lab"
    storage.initialize_empty_store(workspace, actor_ref="qa-01")
    database = workspace / storage.STORE_NAME
    connection = sqlite3.connect(database, autocommit=True)
    connection.execute("PRAGMA user_version = 99")
    connection.close()
    before = hashlib.sha256(database.read_bytes()).digest()
    with pytest.raises(storage.UnsupportedStoreError, match="^UNSUPPORTED_STORE$"):
        storage.read_workspace_metadata(workspace)
    assert hashlib.sha256(database.read_bytes()).digest() == before


def test_corrupt_store_is_not_repaired_and_diagnostic_does_not_echo_content(tmp_path):
    workspace = tmp_path / "lab"
    workspace.mkdir()
    database = workspace / storage.STORE_NAME
    original = b"synthetic sensitive marker\x1b[2J"
    database.write_bytes(original)
    with pytest.raises(storage.StoreError) as failure:
        storage.read_workspace_metadata(workspace)
    assert str(failure.value) == "STORE_READ_FAILED"
    assert database.read_bytes() == original


def test_transaction_failure_leaves_no_partial_metadata(tmp_path, monkeypatch):
    workspace = tmp_path / "lab"
    original_insert = storage._insert_metadata

    def fail_after_insert(connection, metadata):
        original_insert(connection, metadata)
        raise sqlite3.OperationalError("injected pre-commit failure")

    monkeypatch.setattr(storage, "_insert_metadata", fail_after_insert)
    with pytest.raises(storage.StoreError, match="^STORE_INITIALIZATION_FAILED$"):
        storage.initialize_empty_store(workspace, actor_ref="qa-01")

    # The failed new workspace is retained, not silently erased or repaired.
    connection = sqlite3.connect(workspace / storage.STORE_NAME, autocommit=True)
    try:
        assert connection.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall() == []
        assert connection.execute("PRAGMA user_version").fetchone() == (0,)
        assert connection.execute("PRAGMA application_id").fetchone() == (0,)
    finally:
        connection.close()
    with pytest.raises(storage.StoreExistsError):
        storage.initialize_empty_store(workspace, actor_ref="qa-01")


def test_failed_directory_guard_prevents_database_creation(tmp_path):
    workspace = tmp_path / "lab"

    @contextmanager
    def refused_guard(path):
        assert path == workspace
        raise storage.StoreError("DIRECTORY_NOT_ADMITTED")
        yield  # Establish the contextmanager protocol; intentionally unreachable.

    with pytest.raises(storage.StoreError, match="^DIRECTORY_NOT_ADMITTED$"):
        storage.initialize_empty_store(workspace, actor_ref="qa", directory_guard=refused_guard)
    assert workspace.is_dir()
    assert list(workspace.iterdir()) == []


def test_writer_settings_are_effective_before_transaction(tmp_path):
    connection = sqlite3.connect(tmp_path / "policy.sqlite3", timeout=5, autocommit=True)
    try:
        storage._configure_writer(connection)
        assert connection.autocommit is True
        assert not connection.in_transaction
        assert connection.execute("PRAGMA foreign_keys").fetchone() == (1,)
        assert connection.execute("PRAGMA journal_mode").fetchone() == ("delete",)
        assert connection.execute("PRAGMA synchronous").fetchone() == (2,)
        assert connection.execute("PRAGMA busy_timeout").fetchone() == (5000,)
        pages = connection.execute("PRAGMA max_page_count").fetchone()[0]
        page_size = connection.execute("PRAGMA page_size").fetchone()[0]
        assert pages * page_size == 512 * 1024 * 1024
    finally:
        connection.close()


@pytest.mark.parametrize("actor", ["", "   ", None])
def test_missing_actor_refuses_before_creating_data(tmp_path, actor):
    workspace = tmp_path / "lab"
    with pytest.raises(storage.StoreError, match="^ACTOR_REF_REQUIRED$"):
        storage.initialize_empty_store(workspace, actor_ref=actor)
    assert not workspace.exists()
