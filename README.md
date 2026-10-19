# Test Design Gatekeeper

**An experimental assistant for reviewing functional test cases against supplied requirements and business rules.**

Test Design Gatekeeper (TDG) aims to help a human reviewer find missing test conditions, gaps in coverage and unclear expected results. The planned approach combines deterministic checks with a local LLM and human review. Its usefulness has not yet been demonstrated through a product evaluation.

## Current status

**Development is paused for documentation cleanup.** On 18 October 2026, the Project Owner paused feature development and further test-data preparation to address duplication, conflicting descriptions and excessive documentation. TC-I01-033 remains on hold. Documents are being reviewed one at a time, with Owner approval before each change is applied.

The current build, `0.1.0.dev2`, provides the application foundation:

| Command | Available behavior |
| --- | --- |
| `tdg version` | Shows the build, runtime and contract versions. |
| `tdg capabilities` | Lists available and unavailable functions. |
| `tdg init` | Creates a new empty laboratory workspace on Windows x64 / CPython 3.13. |

Importing JSON or CSV, inspecting captured packages and receipts, reviewing test cases, invoking a model and exporting review results are not implemented. The `import`, `receipt` and `package` commands report that they are unavailable.

## Evidence so far

- **Application foundation (W01):** the recorded Windows run on 28 September 2026 passed 48 tests with no skips. It covers workspace initialization and its supporting controls. The Owner accepted this work on 29 September. See the [implementation and verification record](docs/implementation/i01-w01-foundation.md) and [closure decision](docs/implementation/i01-w01-closure.md).
- **Test preparation (W02):** at the pause, the prepared material comprised the baseline example `BASE-01`, 81 input variants for 22 planned test cases and two valid comparison files. The [latest preparation record](docs/implementation/i01-w02c-imported-claims-fixtures.md) reports 238 passing checks of the data and setup on Linux/Python 3.12. The 164 product-test placeholders are skipped until connected to the implementation. These checks do not establish importer behavior; target Windows/Python 3.13 verification of these materials remains pending.

W02 and the first implementation increment, I-01, remain incomplete. The accepted test inventory contains 72 test cases and 208 input variants. Detailed expectations belong in the [test inventory](docs/implementation/i01-w02-test-inventory.md) and the files under [tests](tests).

This is a solo project supported by AI, with about five flexible hours available per week. The [test-work forecast](docs/implementation/i01-w02-test-inventory.md#7-effort-reassessment) remains provisional. There is no validated total effort estimate or committed delivery date.

## Intended MVP

The intended first product reviews system-level, functional black-box test cases for one feature or small business process. The reviewer deliberately supplies the test cases, scope and test basis. Planned input formats are native JSON and a defined local CSV profile.

The four planned test-design techniques are equivalence partitioning, boundary-value analysis, decision tables and state transitions. A technique is used only when the supplied evidence supports it. Test level, test type, design basis and execution mode are assessed separately; automation alone does not make a test white-box.

The reviewer retains decisions and edits the source test cases. TDG is intended to show the evidence and uncertainty behind each observation. It does not generate or repair test suites, approve testware, invent missing business rules, fetch unsubmitted project sources or write changes back to Jira, Xray or Zephyr. Reviewing test cases for AI/LLM systems remains outside this MVP.

Current laboratory work permits only public or synthetic data. Confidential use requires separately verified protection and authorization; a local model alone does not establish that readiness.

[ISTQB CTFL](https://www.istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0/) and the [ISTQB Glossary](https://glossary.istqb.org/) provide methodological references. TDG's product policies are project decisions. The project claims no official ISTQB endorsement, certification or proof of test-suite completeness.

## Running the foundation

The product target is Windows x64 with CPython 3.13. From the repository root, with [uv installed](https://docs.astral.sh/uv/getting-started/installation/):

```powershell
uv sync --locked
.\.venv\Scripts\python.exe -m tdg version
.\.venv\Scripts\tdg.exe capabilities
.\.venv\Scripts\python.exe -m pytest -q
```

Setup may download the pinned interpreter and dependencies. Versions are recorded in `.python-version`, `pyproject.toml` and `uv.lock`. Direct commands from the virtual environment do not invoke a package manager.

`init` supports a new direct child of `%LOCALAPPDATA%\TDG\lab` and refuses an existing workspace. The [W01 record](docs/implementation/i01-w01-foundation.md) explains path restrictions and verified controls. Linux can be used for portable development checks with `.venv/bin/python`; it is not an additional supported product target.

## Documentation guide

| Question | Start here |
| --- | --- |
| What is the project's purpose and scope? | [Project Charter](docs/governance/test-design-gatekeeper-project-charter-v0.4.md) |
| Which requirements were accepted? | [Requirements baseline and acceptance record](docs/requirements-analysis/ra-10/test-design-gatekeeper-requirements-analysis-readiness-v0.2.md) |
| What is the planned input contract? | [RA-09](docs/requirements-analysis/ra-09/test-design-gatekeeper-ra-09-data-representations-import-export-contracts-v0.2.md), with its [accepted clarifications](docs/requirements-analysis/ra-09/test-design-gatekeeper-ra-09-focused-static-review-v0.2.md) |
| What design was accepted for I-01? | [SAD-04](docs/solution-design/test-design-gatekeeper-sad-04-integrated-review-increment-plan-v0.2.md), its [acceptance record](docs/reviews/test-design-gatekeeper-sad-04-review-record-v0.2.md) and [numeric-token clarification](docs/solution-design/test-design-gatekeeper-sad-04-i01-numeric-token-limit-addendum-v0.1.md) |
| What must the tests observe? | [Expected-behavior basis](docs/implementation/i01-w02-test-design.md) and [case inventory](docs/implementation/i01-w02-test-inventory.md) |
| What do project terms mean? | [CONTEXT.md](CONTEXT.md) |
| What rules guide agent work? | [AGENTS.md](AGENTS.md) |

Documentation consolidation is in progress. Existing requirements and design decisions remain in place until an approved change replaces them. Older files can contain preparation-time labels such as `PENDING`; their linked acceptance records establish the later decisions. [Review records](docs/reviews) and the full [documentation tree](docs) retain the history.

## Next step

Consolidate the documentation and make the current rules easy to find. Then review the delivery sequence so a small, useful test-case review can be evaluated sooner. The revised implementation plan still needs to be agreed before development resumes.
