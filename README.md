# Test Design Gatekeeper

**An evidence-grounded, ISTQB-informed test case review assistant.**

Test Design Gatekeeper (TDG) is a documentation-first project exploring whether a hybrid of deterministic controls, a bounded local LLM, explicit evidence, and human review can improve the quality of functional test cases.

The project is intentionally **not a test-case generator**. Its purpose is to help a human reviewer detect shallow coverage, missing conditions, weak observability, and opportunities to apply suitable test-design techniques.

## Current status

**SDLC phase:** Solution and Architecture Design — GO granted on 2026-09-22

**Requirements Analysis:** Closed — RA-01 through RA-10 and the consolidated static review accepted

**SAD-01:** First B-01 design activity reviewed and closed on 2026-09-22; continuation of B-01 remains pending

**SAD-02:** Logical data, identity and contract activity reviewed and closed on 2026-09-23; model/protection architecture remains pending

**Implementation:** Not started; a later implementation gate is required

**Data policy:** Public or synthetic data only during the laboratory phase

The Project Owner accepted [SR-RA-001](docs/requirements-analysis/ra-10/test-design-gatekeeper-requirements-analysis-readiness-v0.2.md), including the consolidated trace review, delivery work packages, resource assessment and carried risks, and explicitly closed Requirements Analysis. The next work is the bounded solution design under that accepted baseline.

The documentation accounts for **249 accepted requirements** and **169 validation obligations**. Every requirement has a justified validation route, and every obligation reaches existing accepted requirements, directly or through inspected intermediates. The [trace evidence](docs/requirements-analysis/ra-10/test-design-gatekeeper-requirements-analysis-traceability-audit-v0.1.json) records **424 direct relations** and the inspected intermediate paths. These figures describe requirements traceability; product test execution and feasibility measurements are still ahead.

[RA-10 v0.2](docs/requirements-analysis/ra-10/test-design-gatekeeper-ra-10-evaluation-acceptance-v0.2.md) and [SR-RA10-001 v0.2](docs/requirements-analysis/ra-10/test-design-gatekeeper-ra-10-focused-static-review-v0.2.md) close evaluation and acceptance analysis. Two verified source-table corrections are incorporated in [RA-03 v0.4](docs/requirements-analysis/ra-10/test-design-gatekeeper-ra-03-review-package-content-provenance-validation-v0.4.md); the targeted `SR-RA03-OBS-001` trace action is closed. Documentation/scope-growth risk `R-08` and declared independence/resource limitations remain active.

Planning assumes a **solo, AI-assisted side project with approximately 5 hours per week available flexibly**. The accepted initial design estimate is revisable; no fixed delivery date or full-MVP feasibility claim has been established.

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
| [SAD-02](docs/solution-design/test-design-gatekeeper-sad-02-data-identity-contracts-v0.1.md) | Review closed | Logical data, identity and import/export contract boundaries |
| [Trace evidence ledger](docs/requirements-analysis/ra-10/test-design-gatekeeper-requirements-analysis-traceability-audit-v0.1.json) | v0.1 | Bidirectional requirement/validation paths and source identities |

The [earlier review records](docs/reviews) and [requirements history](docs/requirements-analysis) remain available. The [RA-10 publication package](docs/requirements-analysis/ra-10) retains exact original, corrected and accepted review snapshots, including the corrected RA-03 source. Grouping these documents preserves their original relative links.

Retained source files contain historical authoring notices such as `PROPOSED`, `ENDORSEMENT PENDING` or a then-ungranted phase gate. Read them with their later acceptance records. **SR-RA10-001 v0.2 establishes the corrected RA-03/RA-10 baseline; SR-RA-001 v0.2 records the current phase authority.** The older snapshots and the trace ledger's pre-acceptance status have not been silently rewritten.

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

The approved [RA-09 contract](docs/requirements-analysis/ra-09/test-design-gatekeeper-ra-09-data-representations-import-export-contracts-v0.2.md) defines a bounded, serialization-neutral **Review Package** represented through native JSON and a specified local CSV profile for TC. Scope and substantive test basis accompany the TC. Capture preserves deficient content and separates import success from minimum admissibility and supported review. Result exports use JSON and a readable Markdown projection; implementation follows the later design gate.

A Jira-shaped file is treated as supplied content. TDG does not need to prove that Jira produced it and does not gain permission to access Jira or follow external references.

## Roadmap and next controlled step

| Stage | State | Next evidence or outcome |
| --- | --- | --- |
| Concept and Feasibility | Closed | Accepted Charter and bounded product hypothesis |
| Requirements Analysis | Closed | Ten accepted slices, static-review closure and bidirectional trace |
| Solution and Architecture Design | GO granted; SAD-01 and SAD-02 B-01 activities closed | Model/protection interfaces, consolidated design review and refined increment plan |
| Implementation | Pending its gate | Bounded laboratory increments with eligible data and traceable verification |
| Evaluation and product acceptance | Planned | Human-adjudicated evidence, task qualification, measured utility and explicit acceptance decisions |
| Confidential deployment | Separate future gate | Verified sealed controls and explicit ROLE-09 authorization before protected input |

Static reviews accompany each phase. STLC planning, analysis, design, implementation, execution and completion evidence will grow with the relevant product increments. Finishing a requirements review does not establish model quality or executed product coverage.

The first two authorized design activities — component responsibilities/one bounded flow and logical data, identity and contract boundaries — are recorded in [SAD-01](docs/solution-design/test-design-gatekeeper-sad-01-components-review-flow-v0.1.md) and [SAD-02](docs/solution-design/test-design-gatekeeper-sad-02-data-identity-contracts-v0.1.md) and closed for review. The next bounded activity is model/protection architecture. Concrete technology choices will be recorded with their rationale; the accepted scope and later approval boundaries remain in force.

## Naming and reference boundary

“ISTQB-informed” describes the methodological reference baseline used by the project. It does not imply endorsement, accreditation, certification, or an official conformity assessment by ISTQB.
