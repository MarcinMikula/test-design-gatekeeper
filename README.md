# Test Design Gatekeeper

**An evidence-grounded, ISTQB-informed test case review assistant.**

Test Design Gatekeeper (TDG) is a documentation-first project exploring whether a hybrid of deterministic controls, a bounded local LLM, explicit evidence, and human review can improve the quality of functional test cases.

The project is intentionally **not a test-case generator**. Its purpose is to help a human reviewer detect shallow coverage, missing conditions, weak observability, and opportunities to apply suitable test-design techniques.

## Current status

**SDLC phase:** Requirements Analysis — RA-04 authorized  
**Implementation:** Not started by design  
**Data policy:** Public or synthetic data only during the laboratory phase

Stakeholder and authority modelling (RA-01) and system workflow modelling (RA-02) are closed. The five-document RA-03 decision package completed focused static review on 2026-09-13 under `SR-RA03-001` with the result `PASS WITH OBSERVATIONS`: all five documents were accepted, no correction-required finding was raised, and two non-blocking observations were carried forward.

**RA-03 is closed.** On 2026-09-15, the Project Owner completed acceptance of all **50 requirements, unchanged and with priority MUST**, designated the reviewed replacement baselines, and explicitly granted **GO to RA-04**. The decisions are recorded in [PG-RA03-001 v0.2](docs/reviews/test-design-gatekeeper-ra-03-gate-record-v0.2.md).

The next workstream defines how supplied test cases are qualified against the system-level, functional, black-box MVP boundary, including mixed or ambiguous cases. RA-04 analysis is authorized; its requirements have not yet been produced or accepted.

No source code is included yet because implementation is not authorized before the applicable requirements and design gates are complete.

## Current documentation

The current baseline is designated by [PG-RA03-001 v0.2](docs/reviews/test-design-gatekeeper-ra-03-gate-record-v0.2.md), which also contains the 50-requirement acceptance register and the RA-04 entry decision:

- [Project Charter v0.4](docs/governance/test-design-gatekeeper-project-charter-v0.4.md) — designated baseline;
- [RA-01 v0.3](docs/requirements-analysis/test-design-gatekeeper-ra-01-stakeholders-actors-authority-v0.3.md) — designated baseline;
- [RA-02 v0.3](docs/requirements-analysis/test-design-gatekeeper-ra-02-system-context-workflows-use-cases-v0.3.md) — designated baseline;
- [RA-03 v0.3](docs/requirements-analysis/test-design-gatekeeper-ra-03-review-package-content-provenance-validation-v0.3.md) — designated wording baseline, read together with the accepted requirement dispositions in PG-RA03-001;
- [RA-03 Decision Disposition and Upstream Change Record v0.1](docs/requirements-analysis/test-design-gatekeeper-ra-03-decision-disposition-upstream-change-record-v0.1.md);
- [Focused Static Review SR-RA03-001](docs/reviews/test-design-gatekeeper-ra-03-focused-static-review-v0.1.md).

The reviewed files retain their original content and historical status notices, including the pre-disposition `PROPOSED` column in RA-03. **PG-RA03-001 records the subsequent acceptance, effective baseline, and GO decision.** Read those source documents together with the gate record; their older status notices do not describe the current project state.

The two non-blocking review observations remain active: complete the explicit downstream trace chain for `RA03-VAL-014` before executable test design, and control analysis/documentation growth under `R-08`.

## MVP direction

The initial MVP is intended to review tester-controlled, system-level functional test cases for one bounded feature or small business process.

Its first supported test-design techniques are:

- Equivalence Partitioning (EP);
- Boundary Value Analysis (BVA);
- Decision Table Testing;
- State Transition Testing.

TDG is expected to distinguish independent classification axes such as test level, test type, test-design technique or basis, and execution mode. A label such as unit, integration, system, manual, or automated must not determine a black-box or white-box classification by itself.

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

The working direction is a bounded, serialization-neutral **Review Package**, with canonical JSON and controlled local CSV/JSON import planned for later specification.

A Jira-shaped file is treated as supplied content. TDG does not need to prove that Jira produced it and does not gain permission to access Jira or follow external references.

## Next controlled step

Prepare the RA-04 scope-qualification analysis using the accepted RA-03 baseline:

1. define evidence-based qualification of system-level, functional, black-box cases while preserving independent classification axes;
2. specify treatment of mixed, ambiguous, unsupported, or insufficiently evidenced cases;
3. identify downstream validation obligations, then perform static review and obtain Project Owner disposition.

This repository records engineering progress without presenting unfinished analysis as an implemented product.

## Naming and reference boundary

“ISTQB-informed” describes the methodological reference baseline used by the project. It does not imply endorsement, accreditation, certification, or an official conformity assessment by ISTQB.
