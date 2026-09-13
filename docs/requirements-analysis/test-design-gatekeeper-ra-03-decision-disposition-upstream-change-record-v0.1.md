# Test Design Gatekeeper

## RA-03 — Decision Disposition and Upstream Change Record

| Field | Value |
| --- | --- |
| Document version | 0.1 |
| Document date | 2026-09-12 |
| SDLC phase | Requirements Analysis |
| Related workstream | `RA-03` |
| Status | PREPARED — deterministic document checks complete; formal focused delta review pending |
| Decision authority | Project Owner |
| Trigger | Project Owner disposition of `OD-RA03-001` through `OD-RA03-010` |
| Entry authorization preserved | `PG-RA02-001` — `GO` to RA-03, 2026-09-09 |
| Implementation authorization | NOT GRANTED |
| Confidential-data use | NOT AUTHORIZED |

> **Control statement:** This record consolidates accepted RA-03 decision directions and identifies their controlled document impact. It does not rewrite historical baselines or gate evidence, promote the fifty RA-03 requirements from `PROPOSED` to `ACCEPTED`, complete a static review, authorize RA-04, or authorize implementation.

## 1. Purpose

This record provides one auditable bridge between the Project Owner's ten RA-03 decisions and the resulting candidate documents. It exists to prevent accepted clarifications from being applied silently or from being mistaken for changes that existed when earlier static reviews and phase gates were approved.

It records:

- the exact disposition state of all ten RA-03 decisions;
- clarifications accepted during the decision walkthrough;
- the affected approved baselines and replacement candidates;
- the boundaries that must not change;
- deterministic document-verification evidence;
- the remaining review and approval steps.

## 2. Baseline-preservation rule

The following approved artifacts remain effective until their candidate replacements pass focused delta review and correction verification:

| Approved artifact | Effective decision or review evidence | Replacement candidate |
| --- | --- | --- |
| Project Charter v0.3 | Project Owner `GO` to Requirements Analysis, 2026-09-08; `SR-CHARTER-001` history | Project Charter v0.4 |
| RA-01 v0.2 | `SR-RA01-001`; `PG-RA01-001` `GO` to RA-02, 2026-09-09 | RA-01 v0.3 |
| RA-02 v0.2 | `SR-RA02-001` and correction verification; `PG-RA02-001` `GO` to RA-03, 2026-09-09 | RA-02 v0.3 |
| RA-03 v0.2 | Corrected Project Owner review candidate | RA-03 v0.3 baseline candidate |

Historical files `test-design-gatekeeper-ra-01-gate-record-v0.1.md` and `test-design-gatekeeper-ra-02-gate-record-v0.1.md`, the Charter phase-decision record in Charter v0.3, and completed static-review records remain unchanged. The amendments neither revoke nor reissue their decisions.

## 3. Project Owner decision disposition

All decisions were accepted on 2026-09-12.

| Decision | Disposition | Accepted meaning |
| --- | --- | --- |
| `OD-RA03-001` | ACCEPTED as recommended | A changed capture/import transformation affecting captured logical content creates a new package version; changed assessment behavior against unchanged capture creates a new run only |
| `OD-RA03-002` | ACCEPTED WITH CLARIFICATION | Recognizability requires identity, a non-empty title or equivalent description, and non-title behavioral content; identifier, title, link, or precondition alone is insufficient; missing expected behavior remains a material gap without necessarily erasing recognizability |
| `OD-RA03-003` | ACCEPTED WITH CLARIFICATION | Scope membership is mandatory, direct trace links may be zero, one, or multiple, and an attributable experience-based rationale may be supplied without invented formal requirement coverage or expansion of the four-technique MVP |
| `OD-RA03-004` | ACCEPTED | Positive origin eligibility follows explicit ROLE-03 human accountability for human-authored or human-controlled AI-assisted testware, not purity-of-authorship inference |
| `OD-RA03-005` | ACCEPTED as recommended | Package-local internal IDs are permitted, while missing or duplicate external IDs remain visible and source repair or write-back remains prohibited |
| `OD-RA03-006` | ACCEPTED as recommended | A reference or opaque artifact cannot satisfy substantive minimum alone; authorized extraction must preserve uncertainty; Jira-shaped content is analyzed without proving that Jira produced it |
| `OD-RA03-007` | ACCEPTED as recommended | TDG extraction and inference stay run-scoped; human confirmation enters supplied package content only through a deliberate new package version |
| `OD-RA03-008` | ACCEPTED as recommended | Minimum provenance provides attributable local identity and traceability without proving external authenticity or requiring an absolute workstation path |
| `OD-RA03-009` | ACCEPTED as recommended | A package version has zero or one direct predecessor and may have multiple children; multi-parent merge is outside MVP |
| `OD-RA03-010` | ACCEPTED as recommended | Fingerprint equality never merges automatically; deliberate existing-version selection creates a new run, while an unselected identical re-upload remains separately attributable |

No RA-03 decision remains open.

## 4. Controlled change set

| Change | Decision source | Affected candidate | Principal locations | Intended effect |
| --- | --- | --- | --- | --- |
| `CR-RA03-001` | `OD-RA03-004` | Charter v0.4; RA-01 v0.3; RA-03 v0.3 | Charter Sections 3, 5.2, 7, 8.1, 24–25; RA-01 ROLE-03 and review state; RA-03 origin model | Replace purity-of-authorship eligibility with explicit accountable human control without authorizing TDG authorship inference or test generation |
| `CR-RA03-002` | `OD-RA03-003` | Charter v0.4; RA-03 v0.3 | Charter Sections 7, 8.1, 24; RA-03 basis, traceability, requirements, validations, and examples | Preserve an explicitly supplied experience-based rationale without inventing requirement coverage or adding a fifth assessed technique |
| `CR-RA03-003` | `OD-RA03-001` | RA-02 v0.3; RA-03 v0.3 | RA-02 terminology, context, use case, alternate flow, version principle, `RA02-REQ-018`, allocation, validation, constraint, and review state; RA-03 three-layer/version model | Separate capture/import transformation from assessment mapping and apply the correct package-versus-run consequence |
| `RA03-CD-002` | `OD-RA03-002` | RA-03 v0.3 | Terminology; Sections 11, 17–20, 22 | Apply the clarified recognizable-case and missing-expected-result boundary |
| `RA03-CD-003` | `OD-RA03-003` | RA-03 v0.3 | Terminology; Sections 10, 12, 17–24 | Support zero/one/multiple direct links and attributable experience-based rationale with scope guards |
| `RA03-CD-005-010` | `OD-RA03-005` through `010` | RA-03 v0.3 | Sections 10, 13, 15–24 | Consolidate accepted identity, supplied-content, provenance, extraction, lineage, and deduplication rules |

## 5. Boundary invariants checked

The candidate changes preserve these previously approved boundaries:

- TDG supports and informs a human; it is not the testware owner, formal approver, or SDLC gate authority.
- TDG uses only deliberately supplied content and does not dereference links, search Jira, or discover unsubmitted documentation.
- Source testware remains immutable to TDG; only a human changes it and submits a deliberate package version.
- AI-assisted testware eligibility does not authorize TDG to generate or repair test cases.
- Reviewing test cases written to evaluate AI/LLM systems remains parked outside MVP.
- EP, BVA, Decision Table Testing, and State Transition Testing remain the initial assessed technique set.
- Neither structural admissibility nor a no-finding result implies completeness, approval, product quality, official ISTQB conformity, or certification.
- Earlier phase gates remain effective and are not retroactively edited.
- No implementation, repository creation, deployment, integration, or confidential-data processing is authorized.

## 6. Requirement-status effect

The Project Owner accepted all ten decision directions, but RA-03 v0.3 continues to contain exactly fifty `MUST / PROPOSED` requirements. This distinction is deliberate:

- a decision disposition selects the intended policy direction;
- a requirement disposition accepts, revises, defers, or rejects an individual normative obligation;
- static review verifies the candidate requirement set and its controlled upstream amendments;
- a separate phase gate authorizes transition to RA-04.

Accordingly, no RA-03 requirement is represented as accepted merely because its supporting decision was accepted.

## 7. Deterministic document verification

Verification was run on 2026-09-12 against the four candidate documents.

| Check | Result |
| --- | --- |
| Markdown table column consistency | PASS — all four candidates |
| Fenced-block balance | PASS — all four candidates |
| Tab and trailing-whitespace scan | PASS — all four candidates |
| RA-03 requirement inventory | PASS — 50 distinct requirement rows; 50 `MUST / PROPOSED` |
| Explicit reverse `REQ` to `VAL` coverage | PASS — 50/50 requirements referenced by at least one validation obligation |
| RA-03 validation-obligation inventory | PASS — 32 rows |
| RA-03 decision inventory | PASS — 10 rows; 10 accepted; 0 open |
| RA-03 input-sufficiency decision rules | PASS — 11 rows (`IS-01` through `IS-11`) |
| RA-03 controlled example inventory | PASS — 18 variants (`EX-01` through `EX-18`) |
| Stale pre-gate or nine-open-decision statements in the four candidates | PASS — none detected |

These checks establish document structure and trace presence. They are not a substitute for semantic static review, independent assurance, requirement acceptance, or correction verification.

## 8. Candidate integrity manifest

| Candidate document | Bytes | SHA-256 before formal delta review |
| --- | ---: | --- |
| `test-design-gatekeeper-project-charter-v0.4.md` | 46126 | `8fa60d4bda8267ac56ef929218f763fff58e37225a56b349ae4f5cb74bd92586` |
| `test-design-gatekeeper-ra-01-stakeholders-actors-authority-v0.3.md` | 37380 | `77f41bc86913acefd05f0ad67d27fdb84d07abc7bcd76f8f5484b3256e8972c8` |
| `test-design-gatekeeper-ra-02-system-context-workflows-use-cases-v0.3.md` | 73811 | `7ab90321bc1c7fee0dcf688afeb07cb17f80aef839a137a6d44bcb15d2f215a9` |
| `test-design-gatekeeper-ra-03-review-package-content-provenance-validation-v0.3.md` | 106862 | `5da14b2ef8d99d74530162debb617d600c2d8792a49a8e4805662badff553c98` |

Any edit after this manifest requires regeneration of the affected size and hash before correction verification is closed.

## 9. Required focused review scope

The next static review must verify at least:

1. exact correspondence between the ten Project Owner dispositions and the candidate wording;
2. absence of conflict with approved human authority, supplied-data-only, confidentiality, and non-approval boundaries;
3. correct package-version versus assessment-run consequences;
4. recognizable-case behavior at the accepted positive and negative boundaries;
5. separation of optional direct traceability, explicit experience-based rationale, and documented requirement coverage;
6. origin eligibility for mixed human-authored, human-controlled AI-assisted, generated-without-adoption, other, and unknown cases;
7. visible handling of internal IDs, opaque/reference-only input, authorized extraction uncertainty, and Jira-shaped files;
8. minimum provenance, single-predecessor branching, and non-deduplication behavior;
9. continued 50/50 explicit `REQ` to `VAL` trace coverage;
10. unchanged effect of historical phase decisions.

The review must record findings by severity and disposition, identify its independence limitation, and perform correction verification for every accepted corrective action.

## 10. Remaining controlled actions

1. Perform the focused upstream delta review of Charter v0.4, RA-01 v0.3, and RA-02 v0.3.
2. Perform the focused semantic static review of RA-03 v0.3, including the decision-to-requirement and requirement-to-validation traces.
3. Correct and verify any accepted review findings.
4. Obtain explicit Project Owner disposition of all fifty RA-03 requirements and priorities.
5. Designate verified replacement baselines only after the preceding controls pass.
6. Prepare a separate RA-03 gate record and request an explicit `GO`, `REVISE`, or `NO-GO` decision for RA-04.

No item in this record skips or pre-approves a later action.
