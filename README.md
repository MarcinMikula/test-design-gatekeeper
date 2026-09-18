# Test Design Gatekeeper

**An evidence-grounded, ISTQB-informed test case review assistant.**

Test Design Gatekeeper (TDG) is a documentation-first project exploring whether a hybrid of deterministic controls, a bounded local LLM, explicit evidence, and human review can improve the quality of functional test cases.

The project is intentionally **not a test-case generator**. Its purpose is to help a human reviewer detect shallow coverage, missing conditions, weak observability, and opportunities to apply suitable test-design techniques.

## Current status

**SDLC phase:** Requirements Analysis — RA-06 authorized  
**Implementation:** Not started by design  
**Data policy:** Public or synthetic data only during the laboratory phase

Stakeholder and authority modelling (RA-01) and system workflow modelling (RA-02) are closed. The five-document RA-03 decision package completed focused static review on 2026-09-13 under `SR-RA03-001` with the result `PASS WITH OBSERVATIONS`: all five documents were accepted, no correction-required finding was raised, and two non-blocking observations were carried forward.

**RA-03 is closed.** On 2026-09-15, the Project Owner completed acceptance of all **50 requirements, unchanged and with priority MUST**, designated the reviewed replacement baselines, and explicitly granted **GO to RA-04**. The decisions are recorded in [PG-RA03-001 v0.2](docs/reviews/test-design-gatekeeper-ra-03-gate-record-v0.2.md).

**RA-04 is closed.** The Project Owner accepted **all 15 MUST requirements**, **three policy decisions** and **three verified wording clarifications**. The closure recorded on 2026-09-17 designates **RA-04 v0.2** and grants **GO to RA-05 — Findings and persistence**. The combined [SR-RA04-001 v0.2 / PG-RA04-001](docs/reviews/test-design-gatekeeper-ra-04-focused-static-review-v0.2.md) records `PASS AFTER VERIFIED CORRECTIONS` and the explicit gate decision.

RA-04 defines evidence-based scope qualification, independent classification dimensions, treatment of mixed or undetermined cases, and the limits of partial review. Its 15 requirements and 15 validation obligations have verified direct traceability in both directions.

**RA-05 is closed.** On 2026-09-18, the Project Owner explicitly endorsed the verified run-boundary clarification, the review record, and the **RA-05 v0.2** baseline, and granted **GO to RA-06 — EP, BVA, decision tables, and state transitions**. All **22 MUST requirements** and **four policy decisions** are accepted. The combined [SR-RA05-001 v0.2 / PG-RA05-001](docs/requirements-analysis/ra-05/test-design-gatekeeper-ra-05-focused-static-review-v0.2.md) records `PASS AFTER VERIFIED CORRECTION` and closes the single review finding.

RA-05 defines separate processing outcomes, findings, human dispositions, evidence, version history, comparison, and local persistence requirements. Its 22 requirements and 16 validation obligations have verified direct traceability in both directions through 56 links. This is document verification, not executed product testing. RA-06 analysis is authorized; its requirements have not yet been produced or accepted.

No source code is included yet because implementation is not authorized before the applicable requirements and design gates are complete.

## Current documentation

The effective baseline combines [PG-RA03-001 v0.2](docs/reviews/test-design-gatekeeper-ra-03-gate-record-v0.2.md) for Charter and RA-01 through RA-03, [SR-RA04-001 v0.2 / PG-RA04-001](docs/reviews/test-design-gatekeeper-ra-04-focused-static-review-v0.2.md) for RA-04, and [SR-RA05-001 v0.2 / PG-RA05-001](docs/requirements-analysis/ra-05/test-design-gatekeeper-ra-05-focused-static-review-v0.2.md) for RA-05 and the RA-06 entry decision:

- [Project Charter v0.4](docs/governance/test-design-gatekeeper-project-charter-v0.4.md) — designated baseline;
- [RA-01 v0.3](docs/requirements-analysis/test-design-gatekeeper-ra-01-stakeholders-actors-authority-v0.3.md) — designated baseline;
- [RA-02 v0.3](docs/requirements-analysis/test-design-gatekeeper-ra-02-system-context-workflows-use-cases-v0.3.md) — designated baseline;
- [RA-03 v0.3](docs/requirements-analysis/test-design-gatekeeper-ra-03-review-package-content-provenance-validation-v0.3.md) — designated wording baseline, read together with the accepted requirement dispositions in PG-RA03-001;
- [RA-04 v0.2](docs/requirements-analysis/test-design-gatekeeper-ra-04-scope-qualification-classification-boundaries-v0.2.md) — designated wording baseline, read together with the accepted dispositions and closure in SR-RA04-001 v0.2;
- [RA-04 Focused Static Review and Gate Record v0.2](docs/reviews/test-design-gatekeeper-ra-04-focused-static-review-v0.2.md) — closed review, correction verification, acceptance register and GO to RA-05;
- [RA-05 v0.2](docs/requirements-analysis/ra-05/test-design-gatekeeper-ra-05-findings-dispositions-persistence-v0.2.md) — designated wording baseline, read together with the accepted dispositions and closure in SR-RA05-001 v0.2;
- [RA-05 Focused Static Review and Gate Record v0.2](docs/requirements-analysis/ra-05/test-design-gatekeeper-ra-05-focused-static-review-v0.2.md) — closed review, correction verification, acceptance register and GO to RA-06;
- [RA-03 Decision Disposition and Upstream Change Record v0.1](docs/requirements-analysis/test-design-gatekeeper-ra-03-decision-disposition-upstream-change-record-v0.1.md);
- [Focused Static Review SR-RA03-001](docs/reviews/test-design-gatekeeper-ra-03-focused-static-review-v0.1.md).

The reviewed source files retain their exact content and historical authoring notices, including RA-03's `PROPOSED` column and the RA-04/RA-05 candidate or pending labels. **The current acceptance and GO decisions are recorded in the linked gate records.** Read the source documents together with those records; older authoring notices do not describe the current project state.

Historical review evidence is also retained: [RA-04 v0.1](docs/requirements-analysis/test-design-gatekeeper-ra-04-scope-qualification-classification-boundaries-v0.1.md) and [SR-RA04-001 v0.1](docs/reviews/test-design-gatekeeper-ra-04-focused-static-review-v0.1.md). These snapshots preserve the wording reviewed before the verified clarifications and final gate decision.

The corresponding RA-05 history is [RA-05 v0.1](docs/requirements-analysis/ra-05/test-design-gatekeeper-ra-05-findings-dispositions-persistence-v0.1.md) and [SR-RA05-001 v0.1](docs/requirements-analysis/ra-05/test-design-gatekeeper-ra-05-focused-static-review-v0.1.md). The four RA-05 snapshots are grouped in one directory to preserve their original relative links without altering the reviewed content.

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

Prepare RA-06 — analysis of the four supported techniques using the accepted RA-04 and RA-05 baselines:

1. define when EP, BVA, decision tables, and state transitions are applicable to the supplied scope and evidence;
2. define bounded coverage assessment, deterministic-control allocation, and the evidence needed for technique-related findings, including partial or ungradable cases;
3. identify validation obligations, perform static review, and obtain Project Owner disposition before any later phase gate.

This repository records engineering progress without presenting unfinished analysis as an implemented product.

## Naming and reference boundary

“ISTQB-informed” describes the methodological reference baseline used by the project. It does not imply endorsement, accreditation, certification, or an official conformity assessment by ISTQB.
