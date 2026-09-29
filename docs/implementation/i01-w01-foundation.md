# I-01 / W01 — Project and Empty-Workspace Foundation

| Field | State |
| --- | --- |
| Date / build | 2026-09-28 / `0.1.0.dev2` |
| Authority | [SR-SAD04-001 v0.2](../reviews/test-design-gatekeeper-sad-04-review-record-v0.2.md): explicit Owner GO to I-01 |
| Work item | W01 VERIFIED — technical evidence complete; formal Owner closure pending |
| Product target | Windows x64 / CPython 3.13 |
| Development observation | CPython 3.13.15 / SQLite 3.53.1 / Linux x86_64 — 44 passed, 4 Windows-only skips |
| Target-platform qualification | Windows 11 Home 10.0.26200 / AMD64 / NTFS / CPython 3.13.15 — 48 passed, 0 failed, 0 skipped |
| Scope of evidence | W01 foundation only; no complete I-01 acceptance decision or later processing capability claimed |
| Publication state | Feature branch published for review through PR #3; repository history records the eventual merge outcome |

## Implemented boundary

- A Python package with equivalent `tdg` and `python -m tdg` entry points, `argparse`, `jsonschema==4.26.0` and `pytest==9.1.1`.
- Exact interpreter pin, `uv.lock` with transitive dependency hashes, a pinned build backend, and an [observed environment record](i01-w01-environment.json). Dependency installation is a setup operation; ordinary direct CLI invocation does not run a package manager.
- Repository text files are normalized to LF through `.gitattributes`, keeping byte-level artifact hashes independent of Windows checkout line-ending conversion.
- `version` and `capabilities` expose build/contract versions, actual runtime and unavailable functions. They do not open a store or process supplied data.
- Windows-only `init --profile laboratory --actor-ref ID [--data-dir PATH]` orchestrates a new empty store. Omission of `--data-dir` selects `%LOCALAPPDATA%\TDG\lab\<generated-workspace-uuid>`. A supplied path is supported only as a new direct child of that managed laboratory root in this build. Other custom roots remain unimplemented, not silently redirected.
- Initialization rejects a non-laboratory profile and an unsupported host before file creation. It refuses an existing workspace even when empty or invalid. No automatic rebuild, migration or cleanup follows a failed initialization.
- Windows admission rejects network/device/relative path forms, path aliases such as parent traversal and alternate streams, repository ancestors, recognized sync roots and reparse/offline directories. It holds ancestor directory handles and the new workspace without delete sharing during creation, and obtains a named per-workspace mutex with a five-second wait bound.
- CMP-06 alone writes the SQLite store. It reserves a new directory exclusively and commits workspace metadata in one explicit transaction, with foreign keys enabled, DELETE journal, FULL synchronization and the selected main-file quota. A failure before commit rolls back metadata; the new failed workspace is retained for diagnosis. Read-only metadata access neither creates a missing store nor repairs an unsupported one.

The native Windows controls were executed on the target operating-system family. Recognition of configured synchronization roots is not an exhaustive detector of every backup or synchronization application. The observed managed laboratory workspace was outside the repository's OneDrive path; broader host backup/synchronization configuration was not independently inspected. These laboratory controls do not claim sealed readiness, authenticated RBAC, protection against an administrator, hardware durability or absence of external host-managed copies.

CLI initialization creates workspace metadata only. It creates no Review Package, receipt, review, findings or source TC. `import`, `receipt` and `package` remain unavailable. Parser containment, resource-boundary enforcement for supplied packages and atomic capture belong to W03–W06 and must precede importer enablement.

## Verification chronology

The expected behaviors derive from the accepted SAD-04 contracts. The same AI-assisted workflow contributed implementation and tests; this is not independent technical review or human acceptance evidence.

### 1. Portable development run

Build `0.1.0.dev1` was first exercised on Linux:

- `44 passed`
- `4 skipped`
- all four skips were native Windows tests.

That result established portable development evidence only and did not satisfy the W01 Windows-verification requirement.

### 2. First native Windows run — defect found

The first full native Windows execution produced:

- `47 passed`
- `1 failed`
- `0 skipped`

The failure was:

`tests/test_windows_workspace.py::test_windows_directory_cannot_be_renamed_while_held`

The test expected a directory held by the TDG guard to reject rename. Rename unexpectedly succeeded.

A focused native experiment compared Windows `CreateFileW` desired-access masks while retaining `FILE_SHARE_READ | FILE_SHARE_WRITE` and omitting `FILE_SHARE_DELETE`:

| Desired access | Observed rename behavior |
| --- | --- |
| `FILE_READ_ATTRIBUTES` | rename succeeded |
| `FILE_LIST_DIRECTORY | FILE_READ_ATTRIBUTES` | rename blocked with WinError 32 |
| `GENERIC_READ` | rename blocked with WinError 32 |
| `DELETE | FILE_READ_ATTRIBUTES` | rename blocked with WinError 32 |

The implementation had requested only `FILE_READ_ATTRIBUTES`. The minimal tested correction changed the directory guard to `FILE_LIST_DIRECTORY | FILE_READ_ATTRIBUTES`; broader `GENERIC_READ` and `DELETE` access were not selected.

### 3. Correction verification

After the directory-guard correction on `0.1.0.dev1`:

- focused failing test: `1 passed`;
- full Windows regression: `48 passed`;
- manual laboratory initialization: exit `0`;
- repeated initialization against the same workspace: `WORKSPACE_ALREADY_EXISTS`, exit `5`.

The initial failure remains part of the W01 evidence rather than being replaced by the corrected result.

### 4. Qualified corrected build — `0.1.0.dev2`

The corrected source was versioned as `0.1.0.dev2` so the failing and corrected implementation states do not share one build identifier.

Observed target environment:

- Microsoft Windows 11 Home `10.0.26200`;
- AMD64 / 64-bit;
- NTFS;
- CPython `3.13.15`;
- SQLite `3.53.1`;
- uv `0.12.19`.

Qualification results:

| Evidence | Observed result | Boundary |
| --- | --- | --- |
| `uv lock --check` | PASS | Project declarations match `uv.lock` |
| `tests/test_windows_workspace.py -q -rs` | 4 passed | Native Windows workspace controls executed |
| full `pytest -q -rs` | 48 passed, 0 failed, 0 skipped | W01 regression on target platform |
| `uv build --wheel --no-sources` | PASS | `test_design_gatekeeper-0.1.0.dev2-py3-none-any.whl` built |
| first `tdg init` | exit 0 | Empty laboratory workspace created under managed LOCALAPPDATA root |
| repeated `tdg init` using the same workspace | `WORKSPACE_ALREADY_EXISTS`, exit 5 | Existing workspace not overwritten |

The runtime capability manifest therefore records `W01_VERIFIED_CLOSURE_PENDING` and `W01_WINDOWS_TRIAL_PASSED_2026-09-28`. These values describe W01 verification of this build; they do not declare the whole I-01 increment accepted.

## Test inventory exercised in W01

| Test file | Contract-derived behavior exercised | Partial trace |
| --- | --- | --- |
| `tests/test_storage.py` | Durable empty-store metadata after reopen; no overwrite; parameterized actor value; missing/corrupt/unknown-schema read behavior; pre-commit rollback; rejected directory guard; actual SQLite connection settings | TCND-I01-12/13, plus initialization behavior in SAD-04 Sections 7–8 |
| `tests/test_cli.py` | Honest capability surface; inactive commands do not open inputs or stores; terminal controls not echoed in errors; equivalent entry points; unsupported host and sealed-profile refusal | TCND-I01-09/14/15, partial only |
| `tests/test_workspace_policy.py` | Managed directory selection; network/device/traversal/stream/reserved-name rejection; synchronization-root boundaries | Initialization path policy in SAD-04 Sections 7.3 and 9; not proof of source-acquisition controls |
| `tests/test_windows_workspace.py` | Real initialization/read/no-overwrite; second-process mutex exclusion; held-directory rename rejection; junction refusal | Native Windows W01 evidence executed successfully after the documented guard correction |

No count is substituted for the 16 accepted I-01 conditions. Their wider capture, crash, resource, input and history obligations remain open.

## Manual trial boundary

The final `0.1.0.dev2` trial used only an empty synthetic laboratory workspace. Its destination had the form:

`%LOCALAPPDATA%\TDG\lab\<generated-workspace-uuid>`

No confidential, project-derived or supplied test-case material was imported. The logical `actor_ref` records a value only; it does not prove identity or grant approval authority.

## Remaining work and closure boundary

The technical prerequisites previously blocking W01 closure are now evidenced: required native Windows behavior was observed and the defect discovered during that observation was corrected and reverified.

Formal W01 closure remains an Owner decision and is not asserted by this implementation record.

W02 develops the synthetic corpus, specified receipt/identity oracles and detailed condition-to-test inventory. That inventory is the first re-estimation point. The Owner's reservation remains unchanged: the original 40–62 hours is a highly uncertain hypothesis; testing alone may require comparable effort, and required tests are not reduced to fit that range.

W03–W07 and the later I-01 completion decision remain ahead.

## Implementation references

Primary mechanism documentation consulted on 2026-09-28; these references support implementation choices, not verification claims:

- [Python 3.13 sqlite3 transaction control](https://docs.python.org/3.13/library/sqlite3.html#transaction-control).
- [uv lock and sync](https://docs.astral.sh/uv/concepts/projects/sync/).
- [CreateFileW sharing and directory flags](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createfilew).
- [CreateMutexW](https://learn.microsoft.com/en-us/windows/win32/api/synchapi/nf-synchapi-createmutexw) and [WaitForSingleObject](https://learn.microsoft.com/en-us/windows/win32/api/synchapi/nf-synchapi-waitforsingleobject).
