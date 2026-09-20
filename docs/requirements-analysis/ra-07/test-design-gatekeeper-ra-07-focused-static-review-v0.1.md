# Test Design Gatekeeper

## SR-RA07-001 — Focused Static Review and Owner Acceptance Record

| Field | Value |
| --- | --- |
| Record version and date | 0.1 — 2026-09-19 |
| Reviewed source | RA-07 v0.1 — LLM Roles and Qualification |
| Corrected candidate | RA-07 v0.2 |
| Review execution | COMPLETE — one Medium finding; correction prepared and verified |
| Review result for v0.1 | CLARIFICATION REQUIRED |
| Review closure | OPEN — Owner endorsement of the clarification and this record pending |
| Owner decision already recorded | RA-07 v0.1 accepted in full, including 20 MUST requirements, 14 validation obligations and four recommendations |
| Candidate requirement state | All 20 original statements unchanged and ACCEPTED |
| Candidate validation state | All 14 original obligations ACCEPTED; localized VAL-008 refinement awaits endorsement |
| Open original policy decisions | 0 — all four recommendations accepted |
| Proposed phase gate | PG-RA07-001, consolidated in Section 7 — NOT GRANTED |

## 1. Review input, criteria, and method

The current stored [RA-07 v0.1](test-design-gatekeeper-ra-07-llm-roles-qualification-v0.1.md) was read in full and compared with the retained local artifact. Its identity is unchanged from the version presented to the Owner. The original snapshot remains intact; the [v0.2 candidate](test-design-gatekeeper-ra-07-llm-roles-qualification-v0.2.md) records the actual acceptance followed by the clarification.

| Artifact | Bytes | SHA-256 |
| --- | --- | --- |
| RA-07 v0.1, accepted review input | 44354 | `ee883ce37265f82d0259b724c85308d64169a8014f06f91255f2a5b2f72d7892` |
| RA-07 v0.2, corrected candidate | 46876 | `91621b65c78741d6d7d99ba668708f7126d6dd281eb8c7a52bf3a80080252699` |

The effective baseline is the one pinned in RA-07 to repository commit `2b21be5294eb28f1918ff37feb7789132e85a4a5`. [SR-RA06-001 v0.2 / PG-RA06-001][gate06] closes RA-06 and authorizes RA-07. Earlier source-status notices do not reopen the accepted Charter and RA-01 through RA-06 baselines.

The Owner performed the human walkthrough and accepted the document. The same assistant that authored RA-07 then performed this focused static review: complete source inspection, targeted comparison against accepted upstream contracts, counterexample walkthroughs, direct traceability checks, and exact comparison of corrected and unchanged content. **This is not an independent expert review.** No TDG implementation, model, SUT, security control, or supplied test script was executed.

The review criteria were: evidence-grounded task boundaries; preservation of human authority; operational/evaluation separation; cause-specific ledger consequences; consistency of configuration identity, qualification and retries; compatibility with immutable package/run history; non-circular evaluation; trace integrity; testability without selecting an implementation; and preservation of confidentiality and MVP scope boundaries.

The methodological references remain those identified in RA-07. This review checks TDG's own requirements and their consistency; it introduces no new ISTQB rules, model recommendation or conformity claim.

## 2. Recorded Owner acceptance

The Owner stated:

> Akceptuję cały dokument, zwłaszcza proponowane wymagania odobają mi się. Otwarte decyzje też

This accepts the whole presented v0.1 and the recommendations attached to its four open decisions.

| Decision scope | Recorded disposition |
| --- | --- |
| RA-07 v0.1 in full | ACCEPTED — 2026-09-19 |
| RA07-REQ-001 through RA07-REQ-020 | All 20 original statements ACCEPTED, priority MUST |
| RA07-VAL-001 through RA07-VAL-014 | All 14 original obligations ACCEPTED for subsequent validation work; no executed test result implied |
| OD-RA07-001 | ACCEPTED as recommended — identified configuration plus bounded task/subtask envelope, with actual composition considered |
| OD-RA07-002 | ACCEPTED as recommended — explicit laboratory candidate evaluation, separate from operational use; four permission states |
| OD-RA07-003 | ACCEPTED as recommended — cause-specific limitations, supported subsets and deterministic-only continuation |
| OD-RA07-004 | ACCEPTED as recommended — qualified bounded retry/selection policy, attempt history and controlled behavior changes |
| Subsequent clarification and localized VAL-008 refinement | PENDING — prepared after the quoted acceptance |
| Review closure, final v0.2 baseline and GO to RA-08 | PENDING — the explicit exit decision remains outstanding |

The original requirements and recommendations need no repeated acceptance. Original VAL-008 remains accepted as historical wording; its refined candidate wording is separately visible below. The quoted message does not by itself constitute the explicit GO required by RA-07 Section 12.3.

## 3. Focused review results

| Area | Outcome and evidence |
| --- | --- |
| Task catalogue and authority | PASS within the review boundary — five bounded contributions remain distinct from human roles, business-rule confirmation, finding disposition and qualification authority |
| Evidence and output | PASS — supplied context is identified; valid references or structure do not prove semantic support; unsupported confidence, arithmetic and explanations cannot promote an unconfirmed premise |
| Scope and technique continuity | PASS — independent classification axes and RA-06's planned-exercise/expected-result distinction are retained; no fifth formal technique or AI-system-test review capability is introduced |
| Data boundary and embedded instructions | PASS as requirements — package instructions cannot grant retrieval or authority; concrete enforcement and confidential-data authorization remain assigned to RA-08 and ROLE-09 |
| Faults and abstention | PASS — absent evidence, unavailable capability and interrupted work have distinct consequences; limited independent results and deterministic-only operation remain possible |
| Qualification and evaluation | PASS — candidate evaluation has an explicit laboratory route; configuration/envelope permission, protocol approval, human oracle and held-out evidence remain distinct |
| Permission lifecycle | PASS — current permission is checked before invocation and output promotion; suspension/withdrawal cannot erase history or be reversed by the evaluated component itself |
| Retry versus behavior change | CLARIFICATION REQUIRED — Section 4.3 permits predeclared instruction variants, but the unqualified “prompt changes” example in Section 8 can contradict that distinction; F-001 |
| Upstream version consequences | PASS after F-001 clarification — configured changes still require a new run under RA-03/RA-05; executing an already qualified policy is not silently redefined as editing that policy |
| Traceability | PASS — 20/20 requirements directly covered, 14/14 VAL reference existing requirements, and 42 identical direct edges in both directions |
| Acceptance and remaining allocations | PASS — original acceptance is recorded; later edits and GO remain explicit; RA-08/09/10 allocations and the two carried observations are retained |

No Critical or High finding, and no other correction-required finding, was identified in this review boundary. This result does not establish requirement completeness, implementation correctness, empirical model suitability or security readiness.

## 4. Finding and prepared clarification

### SR-RA07-F-001 — Prompt-change example obscures the accepted retry-policy boundary

| Field | Finding |
| --- | --- |
| Severity | Medium |
| Category | Internal ambiguity / inconsistent change-trigger example |
| Locations in v0.1 | Section 4.3 retry paragraph; Section 7.2 behavior-change row; Section 8 prompt-change example; RA07-VAL-008 |
| Related accepted requirements | RA07-REQ-008, RA07-REQ-009, RA07-REQ-014, RA07-REQ-015; inherited run protection also relies on RA07-REQ-016 |
| Status | CORRECTION PREPARED AND VERIFIED — OWNER ENDORSEMENT PENDING |

**Observed issue.** Section 4.3 already permits a predeclared instruction variant as part of the qualified retry policy. Section 8, however, says that a prompt change after failure requires a new behavior identity and a new run, without distinguishing the concrete request generated by that unchanged policy from an edit to the configured template or policy. Section 7.2 also uses the unqualified word “prompt”; VAL-008 emphasizes prohibitions without explicitly checking the permitted variant.

**Counterexample.** A qualified policy contains two identified attempt variants. After an unusable first response, its fixed rule selects the second variant for still-unresolved work in an active run. The rendered request differs, but the qualified policy, model, package, task and relevant configuration have not changed. A literal reading of the original Section 8 example would nevertheless demand a new configuration, requalification and a new run. Conversely, calling an actual template edit a “retry” must never permit it to continue under the old identity.

**Risk.** Two implementations or test designers could reach opposite conclusions for the same permitted retry. The restrictive reading would defeat the accepted bounded policy; an overbroad exception could conceal a real behavior change. The distinction affects identity, audit evidence and the practicality of qualification.

**Prepared correction.**

- Section 4.3 explicitly distinguishes executing a predeclared instruction variant under the unchanged qualified policy from editing a configured template, instruction policy, retry policy or another behavior artifact.
- Actual request and variant identity remain attributable. Permitted continuation is bounded by the approved budget and RA-05's active, unresolved work rules; it cannot restart a terminal run or reassess a committed assessment entry.
- Section 7.2 names the configured template/instruction policy as the change-controlled artifact.
- Section 8 contains paired examples: permitted execution of an existing variant and a genuine configuration edit requiring a new identity and run.
- VAL-008 now checks both paths and the terminal/committed-entry restrictions.

This clarifies the distinction already present in accepted Section 4.3 and OD-RA07-004. It grants no new LLM task, no unqualified prompt variant, no extra retry budget, and no exception for a genuine configured behavior change. Exact requirement statements, decision recommendations and direct trace links remain unchanged.

## 5. Correction verification

### 5.1 Static checks

| Check | Result and evidence |
| --- | --- |
| CV-01 — Accepted source preservation | PASS — the original v0.1 artifact retains the Section 1 identity |
| CV-02 — Exact requirement comparison | PASS — 20/20 entire requirement rows, including statement, upstream basis and VAL links, are identical |
| CV-03 — Policy decision comparison | PASS — all four original decision/recommendation rows are identical and their acceptance is recorded |
| CV-04 — Validation delta | PASS — only VAL-008's narrative changed; all 14 identifiers and all direct targets are preserved |
| CV-05 — Forward and reverse trace | PASS — the same 42 edges exist in both directions; no missing requirement coverage, nonexistent target or orphan VAL |
| CV-06 — Localized content delta | PASS — substantive edits are confined to Sections 4.3, 7.2, 8 and VAL-008; other edits record acceptance, review status, references and exit state |
| CV-07 — Boundary compatibility | PASS by static walkthrough — the scenarios in Section 5.2 distinguish allowed retry, actual change, exhausted budget and forbidden reuse |
| CV-08 — Document structure and references | PASS — consistent table widths; reference definitions resolve; cited upstream identifiers and pinned paths exist |
| CV-09 — Decision honesty | PASS — original content is accepted; subsequent clarification, final baseline designation and GO are not represented as already approved |

The checks validate document changes and their trace structure. They are not executable product tests, model evaluations or an assertion that all future faults have been covered.

### 5.2 Counterexample walkthrough

| Scenario | Expected contract consequence after clarification | Static result |
| --- | --- | --- |
| Unchanged qualified policy selects its already declared second instruction variant; active unresolved work; budget remains | Same configuration may continue under the existing run; preserve attempts and actual variant/request identity | PASS — Sections 4.3 and 8 agree |
| Operator edits a configured prompt template after a failure | Changed configuration requires impact assessment and applicable requalification; changed behavior requires a new run | PASS — Sections 4.3, 7.2 and 8 agree |
| A variant is selected outside the qualified policy or an envelope condition is unmet | No permission to invoke under the old grant; a retry label supplies no exemption | PASS — Sections 4.3, 5 and 7 preserve qualification |
| Qualified policy is unchanged but its attempt budget is exhausted | No additional retry under that policy; retain affected-work limitations and attempt history | PASS — Section 4.3 and VAL-007/008 preserve the bound |
| The run is terminal, or the requested assessment entry is already committed | No restart or reassessment under that run identity; a deliberate later assessment requires a new run | PASS — Section 4.3 agrees with RA-05 |
| Qualification is suspended during an in-flight attempt | Do not promote its output as newly supported under the invalidated grant; a configured retry cannot restore authority | PASS — Section 7.1 remains unchanged |
| Source TC is corrected while model configuration and envelope remain applicable | New package and assessment context under RA-03/RA-05; source change alone does not demand model requalification | PASS — Section 7.2 remains consistent |

These are logical walkthroughs of the requirements. No model was called to obtain these outcomes. The new VAL-008 wording carries the applicable positive and negative paths into later test work.

## 6. Review completion and carried items

The focused review and correction verification are complete. F-001 remains open only for Owner endorsement of the prepared clarification and review closure. The review recommendation is to accept that clarification and designate RA-07 v0.2 as the final slice baseline before opening RA-08.

The preserved requirements, four policy decisions and 13 unmodified validation narratives need no repeated walkthrough solely because governance labels changed. The actual semantic review delta is specified in Section 4; the full candidate remains available for inspection.

The following allocations remain:

| Destination | Carried responsibility |
| --- | --- |
| RA-08 | Concrete confidentiality, security, privacy, identity, retention, logging and fail-closed requirements; model qualification cannot replace authorized data use |
| RA-09 | Input/output representations, schemas, mappings and import/export error formats |
| RA-10 and subsequent STLC | Qualification/acceptance corpus, decision criteria, numerical budgets and thresholds, human adjudication, executable tests and empirical feasibility |
| SR-RA03-OBS-001 | Complete the indirect RA03-VAL-014 downstream trace before executable test design; RA-07's direct trace does not close it |
| SR-RA03-OBS-002 / R-08 | Keep analysis and documentation growth under review; no new requirements or policy decisions were added by this correction |

## 7. PG-RA07-001 — Proposed phase exit decision

| Gate condition | Current state |
| --- | --- |
| Owner acceptance of RA-07 v0.1 | SATISFIED |
| Owner acceptance of 20 MUST requirements | SATISFIED — exact statements unchanged |
| Owner disposition of all four policy recommendations | SATISFIED — 4/4 accepted |
| Focused static review | EXECUTED — one Medium finding |
| Prepared clarification and correction verification | COMPLETE — documented in Sections 4–5 |
| Owner endorsement of clarification, including VAL-008 refinement | PENDING |
| Acceptance and closure of SR-RA07-001 | PENDING |
| Designation of RA-07 v0.2 as final phase baseline | PENDING |
| Explicit GO to RA-08 | NOT GRANTED |

**Proposed combined decision:** endorse F-001's localized clarification and verified correction, accept and close SR-RA07-001, designate RA-07 v0.2 as the final baseline, and grant GO to RA-08 — confidentiality, security, privacy and fail-closed requirements.

This proposal is not the gate decision. RA-07 Section 12.3 requires the Project Owner's explicit GO. Neither acceptance of the original document nor completion of this review supplies it automatically.

## 8. Version and preservation record

| Artifact | Meaning |
| --- | --- |
| RA-07 v0.1 | Exact source accepted by the Owner; preserved unchanged |
| RA-07 v0.2 | Records that acceptance and the localized clarification; final endorsement pending |
| SR-RA07-001 v0.1 | This acceptance, review and correction-verification record, with proposed PG-RA07-001 |

The record preserves the actual sequence: Owner acceptance of v0.1, focused review, prepared clarification, then the outstanding exit decision. It does not backdate approval of the new wording. Repository publication of the completed slice remains a subsequent documentation action; no product execution or confidential-data use has been established by this record.

[gate06]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/2b21be5294eb28f1918ff37feb7789132e85a4a5/docs/requirements-analysis/ra-06/test-design-gatekeeper-ra-06-focused-static-review-v0.2.md
