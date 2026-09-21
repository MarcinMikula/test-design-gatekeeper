# Test Design Gatekeeper

## SR-RA09-001 — Focused Static Review and Owner Acceptance Record

| Field | Value |
| --- | --- |
| Record version and date | 0.1 — 2026-09-20 |
| Reviewed source | RA-09 v0.1 — Data Representations and Import/Export Contracts |
| Owner content acceptance | COMPLETE — v0.1 accepted in full on 2026-09-20 |
| Review execution | COMPLETE — two Medium findings; corrections prepared and verified at document level |
| Review result for v0.1 | CLARIFICATION REQUIRED |
| Candidate after correction | RA-09 v0.2 — correction verification PASS; final endorsement pending |
| Requirement state | All 24 original MUST statements ACCEPTED; exact statements unchanged |
| Validation state | All 16 original obligations ACCEPTED; refinements to VAL-002 and VAL-010 pending endorsement |
| Original policy decisions | All four recommendations ACCEPTED; 0 original decisions open |
| Finding disposition and review closure | OPEN — Owner endorsement of the two corrections and this record pending |
| Phase gate | PG-RA09-001 proposed in Section 7 — GO to RA-10 NOT GRANTED |

## 1. Review input, baseline, and method

The current stored [RA-09 v0.1](test-design-gatekeeper-ra-09-data-representations-import-export-contracts-v0.1.md) was obtained for this review and matched the exact artifact presented to and accepted by the Owner. Its source is unchanged. The separately prepared [RA-09 v0.2](test-design-gatekeeper-ra-09-data-representations-import-export-contracts-v0.2.md) records that acceptance and makes the two localized corrections described below visible for endorsement.

| Artifact | Bytes | SHA-256 |
| --- | --- | --- |
| RA-09 v0.1 — accepted review input | 72181 | `659b3194b4f104947af14285b9d907991d30e60710dccdc23ba07fd646be334e` |
| RA-09 v0.2 — prepared phase-baseline candidate | 76449 | `8cf8db1f87d0fb8f1dadad347dba7bdf7af8132c0ec2b64b90878a26c760d5ef` |

The governing baseline is the one pinned in RA-09 to repository commit `ff1cd6379717d59da09087120609d41fc7309668`: Charter v0.4; RA-01/02/03 v0.3; RA-04/05/06/07/08 v0.2, with their acceptance and closure records. [SR-RA08-001 v0.2 / PG-RA08-001][gate08] authorizes RA-09. Repository `main` still referenced that commit when checked during this review. Local copies of all nine wording baselines and the RA-08 closure record matched the corresponding pinned Git blobs. Preserved historical pending labels do not reopen accepted upstream decisions.

The Owner conducted the human walkthrough and accepted v0.1. The same assistant that authored the document conducted this focused static review: source inspection, targeted upstream comparison, adversarial/boundary walkthroughs, requirement and validation trace checks, and controlled comparison of the prepared correction. This is an attributable author review following the Owner walkthrough; it is not an independent expert review. No TDG runtime, parser implementation, model, SUT, or deployment was tested. Temporary scripts checked document identities, relationships, and example syntax only.

Review criteria were: an unambiguous supported-format boundary; preservation of deficient testware and exact sources; compatible capture, admissibility, assessment and export semantics; independent identity and authority; consistency with the closed RA-07 task catalogue; safe local processing and failure; testable representation/version rules; and explicit REQ ↔ VAL traceability without expanding MVP.

Official references cited by RA-09 were rechecked for their limited technical claims. JSON member names and their decoded equality are relevant to duplicate handling; TDG's rejection rule is its own stricter profile choice. [RFC 8259 §§4 and 8.3][rfc8259] CSV quoting/field conventions and JSON Pointer syntax support the documented examples. [RFC 4180][rfc4180] [RFC 6901][rfc6901] JSON Schema distinguishes format annotation from assertion, so the draft correctly requires explicit enforcement configuration. [2020-12 validation specification §7.2][schema-validation] No external standard selects TDG's envelope policy or grants an LLM task; those are project decisions.

## 2. Recorded Owner acceptance

The Owner stated:

> Zaapoznałem się z dokumentem RA-09 v0.1 — reprezentacje danych i kontrakty importu/eksportu  i akceptuję go w całości

Under the established whole-document acceptance convention, this accepts the original requirements, validation obligations, and four recommended decisions. The later corrections in this record are separately identified and are not backdated into that acceptance.

| Decision scope | Recorded disposition |
| --- | --- |
| RA-09 v0.1 in full | ACCEPTED — 2026-09-20 |
| RA09-REQ-001 through RA09-REQ-024 | 24/24 original statements ACCEPTED, priority MUST |
| RA09-VAL-001 through RA09-VAL-016 | 16/16 original obligations ACCEPTED for subsequent STLC work |
| OD-RA09-001 | ACCEPTED as recommended — distinct JSON document contracts, a versioned local schema registry, and separate syntax/content/admissibility checks |
| OD-RA09-002 | ACCEPTED as recommended — a defined CSV profile, one logical record per candidate TC, explicit mappings and no automatic dialect/record-grouping inference |
| OD-RA09-003 | ACCEPTED as recommended — trustworthy permitted capture, visible deficiencies, bounded consequences, and coherent durable success |
| OD-RA09-004 | ACCEPTED as recommended — JSON result export and a faithful Markdown projection, explicit selection/history boundaries, no general trusted-history restoration through import |
| F-001/F-002 and VAL-002/VAL-010 refinements | PENDING — prepared after the quoted content acceptance |
| SR-RA09-001 closure and final v0.2 baseline designation | PENDING |
| Explicit GO to RA-10 | NOT GRANTED — the separate exit decision in RA-09 §12.3 remains outstanding |

The 24 unchanged requirement statements and four original decisions need no repeated item-by-item acceptance. This content acceptance does not authorize implementation, confidential-data processing, or a new runtime LLM task.

## 3. Focused review results

| Area examined | Assessment and evidence |
| --- | --- |
| Vendor-independent formats and local source boundary | PASS — native JSON and defined CSV are bounded; a Jira-shaped file does not require vendor-origin authentication, and links do not retrieve content |
| Root envelope versus supplied content | CLARIFICATION REQUIRED — §2.2 excludes silent acceptance of unknown control fields but leaves the precise additional-member reaction and `content` type implicit; F-001 |
| Source, projection, and assessment layers | PASS — exact original identity, located projection, and run-specific interpretation remain separate under RA-03 |
| Deficient TC and presence semantics | PASS — missing/null/empty/whitespace/type mismatch remain distinguishable; absent expectations do not become a parse error or an automatically authored expectation |
| Origin, defaults, and human accountability | PASS — defaults apply only to absence in their explicit containing set; partial CSV accountability is not silently completed; positive eligibility is case-specific |
| Identity, locators, and optional links | PASS — duplicated external IDs and similar cases remain separate; JSON and logical-record CSV locators retain source identity; dangling optional links have bounded effects |
| CSV framing and resource boundaries | PASS — multiline records, ragged rows, ambiguous framing, unknown columns and limits have visible consequences without silent dropping or guessed grouping |
| Runtime LLM role in capture mapping | CLARIFICATION REQUIRED — §5.2 mentions field-correspondence assistance under an allowed RA-07 task, but no accepted task covers source-field/capture mapper configuration; F-002 |
| Capture, minimum checks, retries, and failure | PASS — a durable deficient candidate is distinguishable from rejected/failed capture; retries and independent submissions retain RA-05 identity and persistence meanings |
| Result state, evidence, and human history | PASS — run state, availability, qualification and ledger outcomes remain independent; empty findings cannot supply a successful substantive-review claim |
| Local export, rendering, and round trips | PASS — current authorization, selection/cutoff, evidence omissions, inert output, history and derivation survive the selected representation; export is not source mutation or trusted restoration |
| Scope and downstream allocation | PASS — schemas, parser libraries, concrete limits and executable tests remain design/STLC work; accepted requirements constrain them without choosing architecture |
| Direct trace integrity | PASS — all 24 requirements and 16 obligations have matching forward/reverse references; 49 direct edges |

No Critical or High finding was identified within this review boundary. Two Medium ambiguities require the localized changes below. These findings concern document precision and upstream consistency; they are not evidence of an implemented defect or an actual unauthorized LLM invocation.

## 4. Findings and prepared dispositions

### SR-RA09-F-001 — Additional root fields lack one explicit contract outcome

| Field | Value |
| --- | --- |
| Severity / category | Medium — ambiguity, interoperability, testability |
| Source | RA-09 v0.1 §2.2, read with §§3.1, 3.4 and 6.1 |
| Affected requirements / obligation | RA09-REQ-003; associated content-preservation boundary in REQ-012/013/024; direct refinement in RA09-VAL-002 |
| Status | CORRECTION PREPARED AND VERIFIED — OWNER ENDORSEMENT PENDING |

**Observation.** The source requires a root object with `document_type`, `contract_version`, and `content`, and says arbitrary top-level control additions are not silently accepted. It does not explicitly say whether a recognized envelope with an extra root member is rejected or retained with a diagnostic. Nor does that paragraph explicitly constrain `content` to an object. A parser that rejects the extra member and one that continues with a visible warning could both cite the original phrase. Their native-import outcomes would differ.

This ambiguity matters because unknown supplied content must remain visible, while supplied data must not extend the control vocabulary. It cannot be resolved simply by rejecting every unknown or deficient field: that would break the accepted deficient-TC capture behavior. Choosing a strict root envelope is a project policy refinement, not a JSON or ISTQB mandate.

**Prepared correction.** RA-09 v0.2 §2.2 explicitly limits version `"1.0"` to the three root members. Kind/version are supported string values and `content` is an object. Missing, additional, or mistyped envelope members reject the primary native import path without a package; permitted original retention remains an intake record. Generated JSON documents must satisfy their envelope before being presented as valid output. Unknown members inside `content` remain located supplied content with bounded issues. An empty content object can be captured where permitted and then fail minimum checks; it is not an envelope error.

The consequence is reflected in §6.1, the §8.3 examples and VAL-002. No new requirement identifier, connector, format, or source-retrieval permission is introduced. The original positive JSON example remains unchanged and satisfies the proposed envelope.

**Static counterexamples used for verification.** Start from the same otherwise adequate native input. Add `comment` at the root: native intake is rejected. Add it under `content`: the unknown field is retained and cannot control processing. Remove `content` or set it to null/array: envelope rejection. Keep `content: {}`: permitted capture followed by missing-minimum findings. These are documented expected consequences, not executed importer results.

**Recommended disposition.** Accept the localized clarification and VAL-002 refinement; close F-001 after Owner endorsement.

### SR-RA09-F-002 — The field-mapping assistance reference has no authorized RA-07 task

| Field | Value |
| --- | --- |
| Severity / category | Medium — upstream consistency and scope precision |
| Source | RA-09 v0.1 §5.2; RA-07 v0.2 §3.1 and RA07-REQ-001 |
| Affected requirement / obligation | RA09-REQ-011; direct refinement in RA09-VAL-010; added explicit upstream trace to RA07-REQ-001 |
| Status | CORRECTION PREPARED AND VERIFIED — OWNER ENDORSEMENT PENDING |

**Observation.** Section 5.2 conditionally offers LLM-proposed field correspondences for human consideration under an allowed RA-07 task. The accepted catalogue has five bounded tasks. Its LLM-03 covers TC-to-basis, TC-to-coverage-item, and explicitly authorized comparison relationships; it does not cover configuring source fields/CSV columns into the capture model. RA07-REQ-001 forbids inferring permission for additional tasks. [Accepted RA-07 catalogue and requirement][ra07]

The conditional wording does not itself establish an authorized task. The problem is that it suggests an available path without naming one, and the shared word “mapping” can conceal the distinction between capture configuration and assessment relationships. User approval of a proposed mapper would not, on its own, satisfy runtime task-scope and qualification controls.

**Prepared correction.** RA-09 v0.2 §5.2 states that no runtime LLM source-field/capture-mapping task is authorized within TDG MVP. Intake uses explicitly selected, identified mappings through the approved human configuration process. The accepted LLM-03 assessment relationships remain available within their existing qualified boundaries. Any future runtime mapper-assistance capability requires separate scope/task change control and qualification.

The §8.3 counterexample and VAL-010 explicitly cover attempted use of LLM-03 to generate a capture mapper. REQ-011 gains RA07-REQ-001 in its upstream trace; its actual requirement statement is unchanged. This clarifies TDG's runtime capability boundary; it does not impose a new rule about how a human may develop documentation or configuration outside that runtime.

**Static counterexamples used for verification.** An operator asks TDG to infer a CSV-column mapping using LLM-03: the existing catalogue cannot authorize that invocation or install a resulting mapper. An operator selects an approved explicit deterministic mapper: normal intake remains available. A qualified LLM proposes a TC-to-basis relationship during an allowed assessment: it retains the existing candidate/evidence/human-authority limits and is not incorrectly prohibited by the correction. Recapture and assessment-only mapping changes keep their existing new-package/new-run consequences.

**Recommended disposition.** Accept the localized clarification, VAL-010 refinement and explicit upstream trace; close F-002 after Owner endorsement.

## 5. Correction verification and retained boundary checks

### 5.1 Verification of the prepared artifact

| Check | Result and evidence |
| --- | --- |
| CV-01 — Exact accepted source | PASS — current v0.1 matches the previously delivered hash and remains unchanged |
| CV-02 — Requirement statements | PASS — all 24 statement cells are byte-for-byte unchanged; only REQ-011's upstream-reference cell adds RA07-REQ-001 |
| CV-03 — Validation delta | PASS — only VAL-002 and VAL-010 narratives change; 14 narratives and all 16 target-reference cells remain unchanged |
| CV-04 — Original policy decisions | PASS — all four recommendation rows remain unchanged; their acceptance is recorded without backdating the new corrections |
| CV-05 — Local trace equality | PASS — 49 identical REQ/VAL edges before and after correction; every edge agrees in both directions |
| CV-06 — Upstream reference existence | PASS — 56 distinct cited upstream REQ identifiers in v0.1 and 57 in v0.2 resolve to the pinned wording baselines; the sole addition is RA07-REQ-001 |
| CV-07 — F-001 consistency | PASS at document level — root member/type/rejection rules, unknown-content preservation, empty-content capture and illustrative/VAL consequences agree across §§2.2, 6.1, 8.3 and 10 |
| CV-08 — F-002 consistency | PASS at document level — §5.2 names the catalogue gap explicitly, preserves actual LLM-03 tasks and mapping version rules, and is covered by the §8.3 example and VAL-010 |
| CV-09 — Original examples | PASS — JSON/CSV code blocks are unchanged. JSON parses and uses the three-member envelope; its absent expectations remain absent. CSV decodes to one data record with nine columns, multiline steps and a valid basis-reference array |
| CV-10 — References and formatting | PASS — 15 pinned repository links resolve to paths in the verified tree; Markdown table widths and reference labels are consistent; local candidate/review links identify the prepared artifacts |
| CV-11 — Controlled scope of edits | PASS — substantive changes are confined to the two findings, their consequences/examples, two VAL narratives and one upstream trace. Remaining changes concern acceptance, review status, version record and the pending gate |
| CV-12 — Authority and phase status | PASS — v0.1 acceptance is recorded; the two prepared changes, review closure, final baseline designation and PG-RA09-001 remain pending |

Correction verification means the prepared wording addresses the documented ambiguities and remains consistent with the inspected contracts. It does not mean the Owner has accepted the amendments or that future executable schemas and parsers have passed tests.

### 5.2 Selected adversarial walkthroughs beyond the findings

| Challenged interpretation | Result from the complete contract |
| --- | --- |
| “A missing expected result makes the whole file invalid.” | Rejected by §§3.2 and 6.1: capture preserves the behavioral case and gap; later dependent assessment may be ungradable |
| “An ID, title and Jira link are enough; TDG can fetch the rest.” | Rejected by §§2.1, 3.2 and 6.1: no recognizability from those alone, no substantive basis from a link, and no automatic retrieval |
| “One human-authored case or a package default makes every case eligible.” | Rejected by §4.2: eligibility is case-specific; explicit unknown/negative/partial declarations are not upgraded |
| “CSV accountability defaults can fill a missing actor when an acceptance column exists.” | Rejected by §5.1: either accountability column makes the declaration explicit; defaults cannot replace or complete the partial object |
| “Repeated TC IDs and duplicate JSON members are the same duplicate problem.” | Rejected by §§3.3 and 4.1: independent case identities are preserved; duplicate object member names are a parse/projection ambiguity. Escaped spellings of the same member name do not justify last-value-wins handling |
| “Physical CSV lines are TC; a malformed final quote can be ignored.” | Rejected by §§4.1 and 5.1: logical records can span lines; uncertain framing cannot be guessed or hidden behind a parsed-prefix success claim |
| “A safely retained opaque attachment and an unread selected file are equivalent.” | Rejected by §§3.1 and 6.3: an opaque retained original is inventoried evidence of limited usability; an unread selected original cannot support a faithful captured inventory |
| “A captured package necessarily passed minimum checks.” | Rejected by §6.2: `CAPTURED` can coexist with `NOT_MET` or an explicitly unperformed minimum check |
| “Identical source bytes make a new submission a retry.” | Rejected by §§4.1 and 6.3: operation identity and deliberate selection matter; content equality alone does not merge submissions |
| “COMPLETED with no findings means the TC were reviewed successfully.” | Rejected by §7.1 and RA-05: `NONE` and non-performance reasons remain possible; state, availability and substantive ledger outcomes are distinct |
| “Deterministic calculation confirms an LLM-derived business premise.” | Rejected by §7.1 and RA-05/06: evidence, interpretation authority and derivation remain distinct |
| “A selected export may hide evidence omissions or replay trusted approvals when imported.” | Rejected by §§7.2–7.3: omission/unavailability are explicit and imported statuses cannot restore authority or history |
| “A failed export or safe Markdown presentation permits changing original TC.” | Rejected by §§2.3 and 7.2: exports and display projections reference canonical records; failure and escaping do not rewrite source content |
| “A successful schema validation, local parser or deterministic-only mode establishes sealed permission.” | Rejected by §§2.3, 3.4 and 6.3 plus RA-08: profile, identity, current permission, protection and LLM qualification are separate prerequisites |

These walkthroughs inspect requirement meaning. They are not a benchmark, executable tests, or claims of complete security, model, parser or functional coverage.

## 6. Review completion and carried items

The focused review and correction verification are complete. Both findings remain open for Owner endorsement of the prepared changes and review closure. The recommendation is to accept the two corrections, designate RA-09 v0.2 as the final phase baseline and grant GO to RA-10. No other content correction was identified within the stated review boundary.

| Carried item | Status and allocation |
| --- | --- |
| `SR-RA03-OBS-001` | OPEN / CARRIED — explicitly connect the RA03-VAL-014 path through IS-01–IS-11 to accepted requirements before executable test design. RA09-VAL-011 and this review's 49 local edges do not close that inherited observation |
| `SR-RA03-OBS-002` / R-08 | CARRIED — documentation/review effort remains a delivery risk. Use one consolidated review/acceptance/correction/gate record, review the actual deltas, and avoid new speculative adapters or duplicate format frameworks |
| Executable data contracts and concrete limits | Solution Design and implementation must realize the accepted meanings, identify schemas/parsers/limits and failure mechanisms, and supply verification evidence before enabling the relevant path |
| RA-10 — Evaluation and Acceptance | Next proposed slice: dataset design, human oracle, sampling, metrics/thresholds, usability, robustness, acceptance constraints and consolidated traceability under the existing RA-02/03 allocation |

No claim is made that schema interoperability, local-hardware feasibility, human effort reduction, model quality, recovery, or sealed security has been demonstrated. Those need the later controlled evidence. Acceptance of this review would close a requirements-document review, not approve product testware or a release.

## 7. PG-RA09-001 — Proposed phase exit decision

| Gate condition | Current state |
| --- | --- |
| Owner acceptance of RA-09 v0.1 and its 24 MUST statements | SATISFIED — exact requirement statements unchanged |
| Owner disposition of the four original recommendations | SATISFIED — 4/4 accepted |
| Formal static review | COMPLETE — two Medium findings |
| Prepared corrections and document-level verification | COMPLETE — Sections 4–5 |
| Owner endorsement of F-001/F-002, VAL-002/VAL-010 refinements and the added upstream trace | PENDING |
| Acceptance and closure of SR-RA09-001 | PENDING |
| Designation of RA-09 v0.2 as final phase baseline | PENDING |
| Explicit GO to RA-10 | NOT GRANTED |

**Proposed combined decision:** endorse both localized corrections and their verification, accept and close SR-RA09-001, designate RA-09 v0.2 as the final baseline, and grant **GO to RA-10 — Evaluation and Acceptance**.

This is a concrete proposal, not a recorded gate decision. RA-09 §12.3 explicitly requires the Project Owner's phase-exit decision after review. The original whole-document acceptance does not silently endorse later wording or grant that GO. The gate concerns advancing the requirements work; implementation and protected-data use retain their separate prerequisites.

## 8. Version and preservation record

| Artifact | Meaning |
| --- | --- |
| RA-09 v0.1 | Exact source accepted by the Owner; preserved unchanged |
| RA-09 v0.2 | Records v0.1 acceptance and the two prepared clarifications; final endorsement pending |
| SR-RA09-001 v0.1 | This combined acceptance, review, correction-verification and proposed-gate record |

The sequence remains explicit: Owner acceptance of v0.1, focused review, prepared and verified corrections, then the outstanding final decision. No approval is backdated. Repository publication follows the established authorized documentation workflow after the relevant decision.

[gate08]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/ff1cd6379717d59da09087120609d41fc7309668/docs/requirements-analysis/ra-08/test-design-gatekeeper-ra-08-focused-static-review-v0.2.md
[ra07]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/ff1cd6379717d59da09087120609d41fc7309668/docs/requirements-analysis/ra-07/test-design-gatekeeper-ra-07-llm-roles-qualification-v0.2.md
[rfc8259]: https://www.rfc-editor.org/rfc/rfc8259
[rfc4180]: https://www.rfc-editor.org/rfc/rfc4180
[rfc6901]: https://www.rfc-editor.org/rfc/rfc6901
[schema-validation]: https://json-schema.org/draft/2020-12/json-schema-validation
