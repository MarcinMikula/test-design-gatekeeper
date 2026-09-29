# I-01 / W01 — Owner Closure Record

| Field | Recorded state |
| --- | --- |
| Date | 2026-09-29 (Europe/Warsaw) |
| Work item | I01-W01 |
| Reviewed pull request | PR #3 — `feat: establish I-01 W01 workspace foundation` |
| Reviewed evidence head | `fe54914f94d52afad23f5c8341222e2e13f27f95` |
| Qualified build | `0.1.0.dev2` |
| Decision | W01 CLOSED |
| Next work | GO GRANTED to I01-W02 |
| Increment boundary | I-01 remains incomplete and unaccepted as a whole |

## 1. Decision

After the W01 implementation and evidence review, the Project Owner was asked:

> Czy zatwierdzasz W01 jako formalnie zamknięty na podstawie evidence w PR #3, przy zachowaniu granicy, że zamknięcie W01 nie oznacza ukończenia ani akceptacji całego I-01, oraz udzielasz GO do rozpoczęcia W02?

The Owner replied affirmatively:

> taak

This decision formally closes W01 and authorizes the start of W02. It does not close I-01, does not accept any later work item, and does not enable any capability that remains disabled in the qualified W01 build.

## 2. Evidence considered

The closure decision is based on the W01 evidence already recorded in [i01-w01-foundation.md](i01-w01-foundation.md) and [i01-w01-environment.json](i01-w01-environment.json), including:

- native Windows qualification of corrected build `0.1.0.dev2`: 48 passed, 0 failed, 0 skipped;
- 4/4 native Windows workspace tests passed;
- successful `uv lock --check` and wheel build;
- manual laboratory initialization succeeded, while repeat initialization against the same workspace returned `WORKSPACE_ALREADY_EXISTS` with exit 5;
- the first native Windows run exposed the directory-sharing defect, which was retained in the evidence, corrected with `FILE_LIST_DIRECTORY | FILE_READ_ATTRIBUTES`, and reverified;
- follow-up PR review corrected line-ending/hash reproducibility, Windows CPU/RAM evidence, effective SQLite-policy evidence, and the transient publication-state wording;
- the accepted SAD-04 artifact identities were rechecked against repository bytes after the line-ending control was added.

The review found no remaining blocking W01 implementation or evidence finding after the follow-up correction commit.

## 3. Closure boundary

W01 closure means the project/venv entry point, capability manifest, pinned environment/dependencies, and empty-store initialization foundation have sufficient evidence for this work-item boundary.

It does **not** mean:

- the full I-01 increment is complete or accepted;
- any of the 16 accepted I-01 test conditions is globally marked passed;
- native JSON Review Package capture is enabled;
- receipt/package processing, parser containment, lineage/retry semantics or full capture persistence are complete;
- CSV, model invocation, substantive test-design review, result export, sealed processing or confidential use are enabled;
- TDG may approve, repair or directly modify a test case.

The qualified `0.1.0.dev2` runtime manifest still contains the pre-closure string `W01_VERIFIED_CLOSURE_PENDING`. That value identifies the status embedded in the qualified build snapshot; this later Owner record governs the current project/work-item status without altering the already-qualified executable build.

## 4. Next authorized work

I01-W02 is authorized to begin under the accepted SAD-04 boundary. Its purpose is to prepare the synthetic corpus, independently specified receipt/identity oracles, and the traceable detailed test inventory before native capture implementation proceeds.

The original 40–62 hour I-01 estimate remains an unvalidated planning hypothesis with the Owner's earlier underestimation reservation. W02 remains the first explicit re-estimation point.

W03–W07 and the later I-01 completion decision remain gated by their own evidence and applicable conditions.
