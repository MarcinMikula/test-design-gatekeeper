# Test Design Gatekeeper

**An evidence-grounded, ISTQB-informed test case review assistant.**

Test Design Gatekeeper (TDG) is a documentation-first project exploring whether a hybrid of deterministic controls, a bounded local LLM, explicit evidence, and human review can improve the quality of functional test cases.

The project is intentionally **not a test-case generator**. Its purpose is to help a human reviewer detect shallow coverage, missing conditions, weak observability, and opportunities to apply suitable test-design techniques.

## Current status

**SDLC phase:** Implementation — bounded I-01 GO granted on 2026-09-28

**Requirements Analysis:** Closed — RA-01 through RA-10 and the consolidated static review accepted

**SAD-01:** First B-01 design activity reviewed and closed on 2026-09-22

**SAD-02:** Logical data, identity and contract activity reviewed and closed on 2026-09-23

**SAD-03:** Model contribution and protection architecture reviewed and closed on 2026-09-27. [SAD-03 v0.3](docs/solution-design/test-design-gatekeeper-sad-03-model-protection-v0.3.md) is the accepted corrected baseline; [SR-SAD03-001 v0.2](docs/reviews/test-design-gatekeeper-sad-03-review-record-v0.2.md) records both closed findings, documentary verification and the Owner's closure decision.

**SAD-04:** Closed on 2026-09-28. The Owner accepted [SAD-04 v0.2](docs/solution-design/test-design-gatekeeper-sad-04-integrated-review-increment-plan-v0.2.md), allocation index v0.2 and SR-SAD04-001 v0.1, closed both findings and B-01 for I-01, and granted implementation GO. The later [decision record, SR-SAD04-001 v0.2](docs/reviews/test-design-gatekeeper-sad-04-review-record-v0.2.md), records that authority while retaining the exact accepted snapshots and the effort-estimate reservation.

**Implementation:** I-01 / W01 formally closed by the Project Owner on 2026-09-29 after review of PR #3 evidence; GO is granted to begin W02. Corrected build `0.1.0.dev2` remains the qualified W01 foundation and provides `tdg version`, `tdg capabilities` and Windows-only empty-workspace initialization with directory and writer guards. Native Windows qualification completed on 2026-09-28 with 48 passing tests and no skips; all package-processing commands remain disabled. See the [W01 work and verification record](docs/implementation/i01-w01-foundation.md) and [W01 closure record](docs/implementation/i01-w01-closure.md). W02 is in test design: the [W02-B inventory](docs/implementation/i01-w02-test-inventory.md) is prepared for review; fixture/test materialization and W02 closure remain ahead. The Owner accepted the [numeric-token limit clarification](docs/solution-design/test-design-gatekeeper-sad-04-i01-numeric-token-limit-addendum-v0.1.md) on 2026-10-03.

**Data policy:** Public or synthetic data only during the laboratory phase

The Project Owner accepted [SR-RA-001](docs/requirements-analysis/ra-10/test-design-gatekeeper-requirements-analysis-readiness-v0.2.md), including the consolidated trace review, delivery work packages, resource assessment and carried risks, and explicitly closed Requirements Analysis. The completed design now authorizes the bounded native-JSON capture/inspection increment I-01; substantive TC review remains later work.

The documentation accounts for **249 accepted requirements** and **169 validation obligations**. Every requirement has a justified validation route, and every obligation reaches existing accepted requirements, directly or through inspected intermediates. The [trace evidence](docs/requirements-analysis/ra-10/test-design-gatekeeper-requirements-analysis-traceability-audit-v0.1.json) records **424 direct relations** and the inspected intermediate paths. These figures describe requirements traceability. Initial implementation tests provide limited evidence; no complete requirement or accepted I-01 condition is declared fulfilled by the W01 foundation.

[RA-10 v0.2](docs/requirements-analysis/ra-10/test-design-gatekeeper-ra-10-evaluation-acceptance-v0.2.md) and [SR-RA10-001 v0.2](docs/requirements-analysis/ra-10/test-design-gatekeeper-ra-10-focused-static-review-v0.2.md) close evaluation and acceptance analysis. Two verified source-table corrections are incorporated in [RA-03 v0.4](docs/requirements-analysis/ra-10/test-design-gatekeeper-ra-03-review-package-content-provenance-validation-v0.4.md); the targeted `SR-RA03-OBS-001` trace action is closed. Documentation/scope-growth risk `R-08` and declared independence/resource limitations remain active.

Planning assumes a **solo, AI-assisted side project with approximately 5 hours per week available flexibly**. The original I-01 estimate of 40–62 hours is explicitly challenged: testing alone may require comparable effort. It is an unvalidated planning hypothesis, not an approved budget or ceiling. Re-estimation follows detailed test design and observed work; no fixed delivery date or full-MVP feasibility claim is established.

## Running the foundation

The first product target is Windows x64 with CPython 3.13. Development dependencies are pinned in `pyproject.toml` and `uv.lock`; the initial interpreter patch is recorded in `.python-version`. With [uv installed](https://docs.astral.sh/uv/getting-started/installation/), run setup once from the repository root:

```powershell
uv sync --locked
.\.venv\Scripts\python.exe -m tdg version
.\.venv\Scripts\tdg.exe capabilities
.\.venv\Scripts\python.exe -m pytest -q
```

Setup may download the pinned interpreter and dependencies. The subsequent direct virtual-environment commands do not invoke a package manager. On Linux, use `.venv/bin/python` and `.venv/bin/tdg` for development checks; this does not add Linux as a supported product target.

This build does not accept Review Packages. `import`, `receipt` and `package` return an explicit unavailable-capability diagnostic. `init` is available only on Windows x64 / CPython 3.13 and only for a new direct child of `%LOCALAPPDATA%\TDG\lab`. It refuses existing workspaces, network paths, redirection, repository ancestors and recognized sync roots. See the [work record](docs/implementation/i01-w01-foundation.md) for the native Windows trial, the defect found during first execution, its correction, and the remaining control limitations.

## Current documentation

Start with the [consolidated review and phase-gate record](docs/requirements-analysis/ra-10/test-design-gatekeeper-requirements-analysis-readiness-v0.2.md). It gives the effective baseline, accepted source precedence, both directions of traceability, the work-package sequence and downstream SDLC/STLC allocations.

| Document | Effective version | Subject |
| --- | --- | --- |
| [Project Charter](docs/governance/test-design-gatekeeper-project-charter-v0.4.md) | v0.4 | Product hypothesis, scope, risks and confidentiality boundary |
| [RA-01](docs/requirements-analysis/test-design-gatekeeper-ra-01-stakeholders-actors-authority-v0.3.md) | v0.3 | Stakeholders, roles and decision authority |
| [RA-02](docs/requirements-analysis/test-design-gatekeeper-ra-02-system-context-workflows-use-cases-v0.3.md) | v0.3 | System context, workflows and use cases |
| [RA-03](docs/requirements-analysis/ra-10/test-design-gatekeeper-ra-03-review-package-content-provenance-validation-v0.4.md) | v0.4 | Review Package content, provenance and input sufficiency |
| [RA-04](docs/requirements-analysis/test-design-gatekeeper-ra-04-scope-qualification-classification-boundaries-v0.2.md) | v0.2 | Scope qualification and classification boundaries |
| [RA-05](docs/requirements-analysis/ra-05/test-design-gatekeeper-ra-05-findings-dispositions-persistence-v0.2.md) | v0.2 | Findings, dispositions, persistence and histories |
| [RA-06](docs/requirements-analysis/ra-06/test-design-gatekeeper-ra-06-technique-applicability-design-coverage-v0.2.md) | v0.2 | EP, BVA, decision tables and state transitions |
| [RA-07](docs/requirements-analysis/ra-07/test-design-gatekeeper-ra-07-llm-roles-qualification-v0.2.md) | v0.2 | Bounded LLM tasks and configuration-specific qualification |
| [RA-08](docs/requirements-analysis/ra-08/test-design-gatekeeper-ra-08-confidentiality-security-privacy-v0.2.md) | v0.2 | Confidentiality, security and privacy |
| [RA-09](docs/requirements-analysis/ra-09/test-design-gatekeeper-ra-09-data-representations-import-export-contracts-v0.2.md) | v0.2 | Data representations and local import/export contracts |
| [RA-10](docs/requirements-analysis/ra-10/test-design-gatekeeper-ra-10-evaluation-acceptance-v0.2.md) | v0.2 | Evaluation, human oracle, metrics and acceptance governance |
| [SR-RA10-001](docs/requirements-analysis/ra-10/test-design-gatekeeper-ra-10-focused-static-review-v0.2.md) | v0.2 | RA-10 review, verified upstream corrections and slice closure |
| [SR-RA-001](docs/requirements-analysis/ra-10/test-design-gatekeeper-requirements-analysis-readiness-v0.2.md) | v0.2 | Consolidated phase closure and GO to Solution and Architecture Design |
| [SAD-01](docs/solution-design/test-design-gatekeeper-sad-01-components-review-flow-v0.1.md) | Review closed | Component boundaries, Review Package flow, fault paths and B-01 completion boundary |
| [SAD-02](docs/solution-design/test-design-gatekeeper-sad-02-data-identity-contracts-v0.1.md) | Original review closed; 2026-09-28 correction addendum | Historical text retained with governing ledger/envelope corrections from SAD-04 |
| [SAD-03](docs/solution-design/test-design-gatekeeper-sad-03-model-protection-v0.3.md) | v0.3; accepted baseline, review closed | Model/protection design with separate candidate evaluation and cause-specific assessment outcomes |
| [SR-SAD03-001](docs/reviews/test-design-gatekeeper-sad-03-review-record-v0.2.md) | v0.2; accepted closure record | Section and correction acceptances, documentary verification and granted SAD-04 gate |
| [SAD-04](docs/solution-design/test-design-gatekeeper-sad-04-integrated-review-increment-plan-v0.2.md) | v0.2; accepted baseline | Integrated review, bounded I-01 design and STLC plan; explicit effort reservation |
| [SR-SAD04-001](docs/reviews/test-design-gatekeeper-sad-04-review-record-v0.2.md) | v0.2; closure and GO recorded | Owner acceptance of the v0.1 verification, two closed findings and the selected B-01 boundary |
| [SAD-04 requirement allocation](docs/solution-design/test-design-gatekeeper-sad-04-requirement-allocation-v0.2.json) | v0.2; accepted frozen plan | 249 IDs retained; 40 partial I-01 contributions, 16 planned conditions; execution evidence recorded separately |
| [I-01 / W01](docs/implementation/i01-w01-foundation.md) | Closed 2026-09-29; Owner GO to W02 | CLI foundation, controlled empty-store initialization and recorded Windows evidence |
| [W01 closure](docs/implementation/i01-w01-closure.md) | Owner decision 2026-09-29 | Formal W01 closure after PR #3 evidence review; authorizes W02 without accepting the whole I-01 increment |
| [I-01 / W02](docs/implementation/i01-w02-test-design.md) | Working draft; numeric-limit decision recorded | Oracle basis, accepted REJECTED/2 limit outcome and link to concrete test design |
| [W02-B test inventory](docs/implementation/i01-w02-test-inventory.md) | v0.1; prepared for review | 72 case rows, 208 listed parameter variants, all 16 condition routes; no execution or acceptance claim |
| [SAD-04 numeric-token addendum](docs/solution-design/test-design-gatekeeper-sad-04-i01-numeric-token-limit-addendum-v0.1.md) | v0.1; Owner decision 2026-10-03 | REJECTED and CLI exit 2 above the 128-character token bound; frozen design baseline preserved |
| [Trace evidence ledger](docs/requirements-analysis/ra-10/test-design-gatekeeper-requirements-analysis-traceability-audit-v0.1.json) | v0.1 | Bidirectional requirement/validation paths and source identities |

The [earlier review records](docs/reviews) and [requirements history](docs/requirements-analysis) remain available. The [RA-10 publication package](docs/requirements-analysis/ra-10) retains exact original, corrected and accepted review snapshots, including the corrected RA-03 source. Grouping these documents preserves their original relative links.

Retained source files contain historical authoring notices such as `PROPOSED`, `ENDORSEMENT PENDING` or a then-ungranted phase gate. Read them with their later acceptance records. **SR-RA10-001 v0.2 establishes the corrected RA-03/RA-10 baseline; SR-RA-001 v0.2 records the design-entry authority; SR-SAD04-001 v0.2 records the current I-01 implementation authority.** Earlier snapshots, including the SAD-04 candidate labels and pending-GO metadata, have not been silently rewritten.

## MVP direction

The initial MVP is intended to review tester-controlled, system-level functional test cases for one bounded feature or small business process.

Its first supported test-design techniques are:

- Equivalence Partitioning (EP);
- Boundary Value Analysis (BVA);
- Decision Table Testing;
- State Transition Testing.

TDG is expected to distinguish independent classification axes such as test level, test type, test-design technique or basis, and execution mode. A label such as unit, integration, system, manual, or automated must not determine a black-box or white-box classification by itself.

## Methodological references

TDG is **ISTQB-informed**, not an ISTQB certification or conformity product. The project uses official ISTQB material as a methodological reference for testing terminology, test analysis and the supported black-box test-design techniques. TDG-specific evidence, authority, workflow, persistence, model qualification, protection and LLM rules remain project engineering decisions and are not presented as ISTQB requirements.

Primary references:

- [ISTQB Certified Tester Foundation Level (CTFL) v4.0](https://www.istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0/) — the official CTFL page and source for the current CTFL 4.0 syllabus materials. Chapter 4 provides the test-analysis/design context; Sections 4.2.1–4.2.4 cover Equivalence Partitioning, Boundary Value Analysis, Decision Table Testing and State Transition Testing.
- [ISTQB Glossary](https://glossary.istqb.org/) — the terminology reference for general software-testing terms.
- [RA-06 — Technique Applicability and Test-Design Coverage](docs/requirements-analysis/ra-06/test-design-gatekeeper-ra-06-technique-applicability-design-coverage-v0.2.md) — TDG's project-level treatment of the four supported techniques, including evidence, applicability, coverage and uncertainty boundaries. RA-06 applies the methodology to TDG; it does not reproduce or replace the official syllabus.

The external references provide methodological and terminological context. The accepted TDG requirements, design records and review/closure records remain authoritative for product behavior.

## Core principles

- **Human authority:** TDG supports decisions; it does not own, repair, approve, or certify testware.
- **Supplied-data only:** the review uses only the deliberately submitted Review Package and does not search external project sources.
- **Evidence before verdict:** findings and suggestions must expose their basis, limitations, and uncertainty.
- **Deterministic and probabilistic separation:** reproducible controls remain distinguishable from LLM-assisted semantic suggestions.
- **Fail-visible behavior:** missing, conflicting, opaque, or unsupported input is reported rather than guessed away.
- **Immutable review history:** package versions, assessment runs, findings, and human dispositions remain attributable.
- **Confidentiality by design:** confidential enterprise documentation must not leave an approved sealed environment.

## Deliberate MVP exclusions

The MVP does not:

- automatically write complete test suites;
- modify source test-case steps without human action;
- write changes back to Jira, Xray, or Zephyr;
- claim official ISTQB conformity, certification, or test-suite completeness;
- force every technique onto every requirement;
- invent missing business rules;
- review test cases designed specifically to evaluate AI or LLM systems;
- send confidential project documentation to external models.

## Input direction

The approved [RA-09 contract](docs/requirements-analysis/ra-09/test-design-gatekeeper-ra-09-data-representations-import-export-contracts-v0.2.md) defines a bounded, serialization-neutral **Review Package** represented through native JSON and a specified local CSV profile for TC. Scope and substantive test basis accompany the TC. Capture preserves deficient content and separates import success from minimum admissibility and supported review. I-01 implements only the bounded native JSON capture/inspection path; CSV and result exports follow later increments.

A Jira-shaped file is treated as supplied content. TDG does not need to prove that Jira produced it and does not gain permission to access Jira or follow external references.

## Roadmap and next controlled step

| Stage | State | Next evidence or outcome |
| --- | --- | --- |
| Concept and Feasibility | Closed | Accepted Charter and bounded product hypothesis |
| Requirements Analysis | Closed | Ten accepted slices, static-review closure and bidirectional trace |
| Solution and Architecture Design | SAD-01–04 closed for the I-01 boundary | Accepted baseline and closed findings; later capability decisions remain allocated |
| Implementation | I-01 GO granted; W01 closed; W02-B inventory prepared for review | Review concrete cases and testing forecast, then materialize W02-C fixtures/skeletons before W02 completion |
| Evaluation and product acceptance | Planned | Human-adjudicated evidence, task qualification, measured utility and explicit acceptance decisions |
| Confidential deployment | Separate future gate | Verified sealed controls and explicit ROLE-09 authorization before protected input |

Static reviews accompany each phase. STLC planning, analysis, design, implementation, execution and completion evidence will grow with the relevant product increments. Finishing a requirements review does not establish model quality or executed product coverage.

The four design activities culminate in the [accepted SAD-04 baseline](docs/solution-design/test-design-gatekeeper-sad-04-integrated-review-increment-plan-v0.2.md) and [Owner's implementation GO](docs/reviews/test-design-gatekeeper-sad-04-review-record-v0.2.md). SAD-04 Section 10 retains the decisions that must precede later review/model/sealed capabilities. This GO authorizes I-01 implementation; increment acceptance and confidential use retain their subsequent gates.

## Naming and reference boundary

“ISTQB-informed” describes the methodological reference baseline used by the project. It does not imply endorsement, accreditation, certification, or an official conformity assessment by ISTQB.