# Test Design Gatekeeper

## SR-RA06-001 — Focused Static Review and Owner Acceptance Record

| Field | Value |
| --- | --- |
| Record version and date | 0.1 — 2026-09-18 |
| Reviewed source | RA-06 v0.1 — Technique Applicability and Test-Design Coverage |
| Corrected candidate | RA-06 v0.2 |
| Review execution | COMPLETE — two Medium findings; both corrections prepared and verified |
| Review result for v0.1 | CORRECTIONS REQUIRED |
| Review closure | OPEN — Owner endorsement of corrections and this record pending |
| Owner decision already recorded | RA-06 v0.1 accepted in full, including 20 MUST requirements, 14 validation obligations, and four recommendations |
| Candidate requirement state | 19 statements unchanged and accepted; amended REQ-015 proposed for endorsement |
| Open original policy decisions | 0 — all four recommendations accepted |
| Proposed phase gate | PG-RA06-001, consolidated in Section 7 — NOT GRANTED |

## 1. Review input, scope, and method

The exact [RA-06 v0.1](test-design-gatekeeper-ra-06-technique-applicability-design-coverage-v0.1.md) accepted by the Owner is retained unchanged. The current stored source was read for this review. The [v0.2 candidate](test-design-gatekeeper-ra-06-technique-applicability-design-coverage-v0.2.md) records that acceptance and the subsequent corrections.

| Artifact | Bytes | SHA-256 |
| --- | --- | --- |
| RA-06 v0.1, review input | 41809 | `8050f25446601afd34cadb783d21f4b56c3c2ddcb57c1f97d4df5c1e7d6662fc` |
| RA-06 v0.2, corrected candidate | 45741 | `de0339bfee72aa8ca7e6366cb079a5f38cc37dedbb7d1dd40c7fbe97952b6791` |

The upstream baseline is pinned by RA-06 to repository commit `bbd222927233095142208e9051979ea3beae1864`: Charter v0.4; RA-01/02/03 v0.3 with the applicable acceptance records; RA-04 v0.2 with SR-RA04-001 v0.2; and RA-05 v0.2 with [SR-RA05-001 v0.2][review05]. The last record governs the accepted RA-05 correction and GO to RA-06. Historical pending labels in earlier sources do not reopen those decisions.

The Owner performed the human review and accepted v0.1. The assistant that authored RA-06 then performed this documented, focused static review: internal consistency inspection, targeted upstream comparison, technique and counterexample reasoning, identifier and trace checks, and correction-difference verification. **This is not an independent expert review.** No TDG implementation, local model, SUT, or supplied test script was executed. Temporary document-check scripts and finite set calculations support the review record only.

The method references remain the official [CTFL syllabus v4.0.1, Sections 4.2.1–4.2.4][ctfl], and [Sample Exam B answers v1.7, Question 21][exam-b]. Their versions were rechecked on 2026-09-18. TDG's static coverage interpretation and the corrections below are project decisions, not an ISTQB certification or an assertion that ISTQB requires random testing.

## 2. Recorded Owner acceptance

The Owner stated:

> Zapoznałem się z dokumentem **RA-06 v0.1** i akceptuje go w całości.

| Decision scope | Recorded disposition |
| --- | --- |
| RA-06 v0.1 in full | ACCEPTED — 2026-09-18 |
| RA06-REQ-001 through RA06-REQ-020 | All 20 original statements ACCEPTED, with priority MUST |
| RA06-VAL-001 through RA06-VAL-014 | All 14 original validation obligations ACCEPTED for subsequent test work; no product test result implied |
| OD-RA06-001 | ACCEPTED as recommended — distinct applicability outcomes and conditional coverage request |
| OD-RA06-002 | ACCEPTED as recommended — separate planned exercise and expected-result alignment; bounded quantitative reporting |
| OD-RA06-003 | ACCEPTED as recommended — explicit coverage-criterion selection without universally forcing the strongest variant |
| OD-RA06-004 | ACCEPTED as recommended — bounded controls, provenance-preserving LLM assistance, and recommendations without TC rewriting |
| Later v0.2 corrections and review closure | PENDING — these changes were prepared after the quoted acceptance |
| Final corrected phase baseline and GO to RA-07 | NOT GRANTED — explicit exit decision outstanding |

The original REQ-015 remains accepted as part of the v0.1 historical record; its changed candidate wording is not silently substituted into that acceptance. The other 19 statements and all four recommendations need no repeated acceptance. The quoted message does not itself authorize repository publication, implementation, or confidential-data use.

## 3. Focused review results

| Area | Outcome |
| --- | --- |
| Supplied boundary and qualification | Four techniques, qualified subjects, evidence locators, and visible exclusions retained; classification labels do not determine technique coverage |
| Applicability and RA-05 accounting | Negative applicability, insufficient evidence, and unavailable capability remain distinct; conditional requests cannot hide failure of explicitly requested work |
| Exercise versus oracle | General separation is explicit in Section 4.1, but the parameterized-TC paragraph contradicts it — F-001 |
| Selection guarantees | Section 9.1, REQ-015, and VAL-003/014 permit a blanket reading against randomness despite a supplied guarantee — F-002 |
| EP and BVA | Partitions versus combinations, relevant ordering and precision, explicit two-/three-value criteria, and boundary targets remain distinct; the original 4-/8-target example is retained |
| Decision rules | Feasible rules, supported reductions, unknown values, priorities, and action evidence remain distinct; no unsupported combination expansion or invented discount |
| States and transitions | State versus transition criteria, reachability, guarded transitions, self-loops, explicit invalidity, and setup/reset evidence are retained |
| Metrics and identities | Finite versioned denominators, unresolved mappings, zero denominators, subset labels, and distinct-item counts do not become global quality or execution claims |
| Interpretation and versioning | Deterministic arithmetic does not confirm LLM premises; accepted RA-05 rules for first interpretations, changed behavior, new runs, and new package versions are preserved |
| Traceability | 20/20 REQ have direct VAL links; 14/14 VAL reference existing REQ; 46 matching direct edges in both directions |

No additional correction-required issue was identified within this review boundary. This conclusion does not establish requirement completeness, benchmark adequacy, feasibility on limited hardware, or the correctness of a future implementation.

## 4. Findings and prepared corrections

### SR-RA06-F-001 — Parameterized exercise incorrectly depends on expected results

| Field | Finding |
| --- | --- |
| Severity | Medium |
| Category | Internal contradiction / representation-dependent coverage |
| Locations in v0.1 | Section 9.1, parameterized-TC paragraph, compared with Section 4.1 and REQ-005 |
| Affected validation | VAL-003 |
| Status | CORRECTION PREPARED AND VERIFIED — OWNER ENDORSEMENT PENDING |

**Evidence and consequence.** Section 9.1 requires supplied definitions to guarantee “identifiable values and applicable expectations” before multiple exercises can be established. Section 4.1 explicitly preserves supported planned exercise when an expected result is missing or wrong. The former permits an implementation to refuse parameterized coverage merely because expectations are absent, while crediting the same individually written TC. This is a specification defect, not an observed product failure.

**Counterexample.** The supplied integer rule accepts 10–20 inclusive. A TC explicitly submits every value in `{9, 10, 20, 21}`, with sufficient independent setup and actions, but contains no expected result. Under the accepted separation, all four two-value BVA items are `PLANNED`, while their expected-result observations are `MISSING`. Neither the dataset format nor the missing oracle justifies removing the planned exercise.

**Prepared correction.** Candidate Section 9.1 applies Section 4.1's exercise/oracle separation explicitly to individually written, parameterized, and data-driven TC. VAL-003 now includes a defined dataset exercised without expected results. REQ-005 is unchanged; no requirement to generate missing expectations is introduced.

### SR-RA06-F-002 — Randomness is confused with absence of an item guarantee

| Field | Finding |
| --- | --- |
| Severity | Medium |
| Category | Overbroad requirement and validation wording |
| Locations in v0.1 | Section 9.1; REQ-015; VAL-003 and VAL-014 |
| Relevant accepted rules | Sections 4.1 and 5; REQ-005, REQ-008, REQ-015, and REQ-016 |
| Status | CORRECTION PREPARED AND VERIFIED — OWNER ENDORSEMENT PENDING |

**Evidence and consequence.** REQ-015 prohibits inference from unspecified or random selections without distinguishing a supported selection guarantee. VAL-003 states “Random selection guarantees no target”; VAL-014 similarly uses an unqualified prohibition. This can cause supported partition or dataset coverage to be rejected based on selection mode alone.

**Counterexamples.** Selecting one integer from 10 through 20 inclusive guarantees membership of an established equivalence partition containing that entire range, although it does not guarantee either specific endpoint. Likewise, an instruction to exercise every value of a fixed dataset in random order can preserve all its items when setup and behavior are independent of ordering. Neither example establishes actual generator or SUT execution.

**Prepared correction.** Section 9.1 distinguishes a supported supplied selection rule from randomness or probability alone. REQ-015 is proposed with this exact replacement:

> TDG shall assess parameterized or data-driven TC from supplied definitions without executing them, preserve supported guarantees about item exercise, and not infer such guarantees from unspecified selection or randomness alone.

VAL-003 now distinguishes partition-level guarantees, individual boundary uncertainty, and exhaustive dataset exercise in random order. VAL-014 prohibits unsupported inference from randomness. Unknown selection contracts and unconfirmed LLM interpretations remain unresolved. A guarantee at partition level does not become a guarantee at value, decision-rule, or transition level.

## 5. Correction verification

Verification refers to the exact source and candidate hashes in Section 1. PASS below concerns document structure, differences, and consistency of the stated consequences. It does not mean that a product test suite has passed.

| Check | Result |
| --- | --- |
| CV-01 — accepted input preserved | PASS — v0.1 remains byte-identical to the recorded 41809-byte source |
| CV-02 — requirement changes bounded | PASS — exactly REQ-015's statement changes; 19 statements, all 20 IDs, MUST priorities, upstream traces, and direct VAL links are retained |
| CV-03 — validation changes bounded | PASS — only VAL-003 and VAL-014 condition text changes; all 14 IDs and reverse links are retained |
| CV-04 — existing decisions preserved | PASS — all four recommendation rows are unchanged; their acceptance is recorded separately |
| CV-05 — unaffected behavior preserved | PASS — Sections 2, 4–8, 9.2, and 9.3 are textually unchanged; Section 3 changes only its accepted-status description |
| CV-06 — trace integrity | PASS — 20/20 forward, 14/14 reverse, 46 identical edges; no dangling target; 20 distinct RA-03, 7 RA-04, and 13 RA-05 requirement identifiers resolve, including expanded ranges |
| CV-07 — correction examples | PASS — the candidate supports the distinct consequences in the scenario table below; finite set checks confirm the bounded-selection and permutation examples |
| CV-08 — acceptance and gate integrity | PASS — original acceptance retained; the amendment, correction endorsement, final baseline designation, and RA-07 gate remain explicitly pending |

Other candidate edits are administrative: version and disposition metadata, acceptance wording, the verification summary, the exit condition, a review link, and a short version record. They do not alter the original scope, source boundaries, criteria selection, or lifecycle policy.

| Static scenario | Consequence supported by the corrected wording |
| --- | --- |
| A defined dataset explicitly exercises all four two-value BVA targets, with independent setup, but no expectations | Four supported `PLANNED` item mappings; separate `MISSING` expected-result observations; no invented oracle |
| The same planned exercise has an expectation contradicting the supplied basis | Exercise credit remains; the affected expected-result observation is `CONFLICTING` |
| One integer is selected from 10–20 inclusive; every possible selection belongs to one established EP class | That partition is `PLANNED`; individual endpoint mappings remain `UNDETERMINED` without an additional guarantee; no transfer of EP credit to BVA |
| Every value of the fixed target set is exercised in arbitrary order with independent setup | All target items remain planned; all 24 permutations of the four-value dataset preserve its membership |
| Four values are sampled with replacement from that same four-value set | No individual target is guaranteed by the sampling instruction alone; four draws could repeat a single value; no claim of full exercise |
| A selection contract is absent or asserted only through an unconfirmed LLM interpretation | No established selection guarantee; retain uncertainty and provenance; arithmetic does not confirm the premise |
| State-dependent actions are placed in random order without supporting setup or resets | Dataset membership alone does not establish transition exercise; apply the unchanged reachability rules to the supplied sequence evidence |

The finite calculations enumerate possible data selections; they do not execute supplied TC, a generator, or the future TDG. Changing a supplied selection rule still creates a new package version. Changing configured assessment behavior against unchanged input still requires a new run under the unchanged Section 9.3 and accepted RA-05 correction.

## 6. Traceability and carried obligations

The candidate's Section 10 contains the forward REQ-to-VAL view, and Section 11 the reverse view. Verification compared their complete sets of 46 edges, checked every target identifier, and confirmed that the two-way relation is unchanged. The existing direct obligations cover the revised REQ-015 through VAL-003 and VAL-014. No new requirement, VAL identifier, or policy decision is added.

The earlier observations remain carried: `SR-RA03-OBS-001` concerns the older RA03-VAL-014 indirect chain through IS-01–IS-11 before executable test design; `SR-RA03-OBS-002 / R-08` concerns analysis and documentation growth at the next Charter risk review. Neither is closed by this slice's trace counts.

To limit growth, this record combines Owner acceptance, review findings, correction verification, and the pending gate. It introduces no separate correction report, benchmark, implementation plan, or status database. Formal review assurance and local-model feasibility remain different questions.

## 7. PG-RA06-001 — Pending phase-gate disposition

| Decision element | Current state |
| --- | --- |
| Accept RA-06 v0.1, its 20 original MUST requirements and 14 original VAL obligations | GRANTED — Owner acceptance quoted in Section 2 |
| Accept OD-RA06-001 through OD-RA06-004 as recommended | GRANTED — same whole-document acceptance |
| Endorse the F-001/F-002 corrections, including candidate REQ-015 and VAL-003/014 | PENDING |
| Accept SR-RA06-001 v0.1 and close the review and its two findings after verified correction | PENDING |
| Designate RA-06 v0.2, read with the disposition record, as the final phase baseline | PENDING |
| GO to RA-07 — permitted LLM roles, deterministic/LLM responsibility boundaries, and qualification | NOT GRANTED |

Recommended final decision: endorse the two verified corrections, accept and close this review, designate the corrected v0.2 baseline, and grant GO to RA-07. The original 19 unchanged statements and four policy decisions do not need to be accepted again.

The separate request follows RA-06 Section 12.3's explicit exit condition and concerns material prepared after the accepted v0.1. The assistant records no gate decision on the Owner's behalf. This record does not authorize implementation, protected-data processing, or publication to the repository.

[review05]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/bbd222927233095142208e9051979ea3beae1864/docs/requirements-analysis/ra-05/test-design-gatekeeper-ra-05-focused-static-review-v0.2.md
[ctfl]: https://istqb.org/?download_id=3345&sdm_process_download=1
[exam-b]: https://istqb.org/?download_id=3365&sdm_process_download=1
