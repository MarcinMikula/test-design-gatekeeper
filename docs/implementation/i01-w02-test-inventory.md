# Test Design Gatekeeper

## I-01 / W02-B — Concrete Test Inventory

| Field | State |
| --- | --- |
| Version / preparation date | v0.1 — 2026-10-04 (Europe/Warsaw) |
| Status at initial publication | WORKING DRAFT — prepared for review, not accepted or executed |
| Review progress — 2026-10-05 | CASE GROUPS ACCEPTED — Sections 1–3 and groups A–H accepted without changes; Sections 5–8 remain open |
| Decision evidence | [SR-I01-W02B-001 v0.3](../reviews/test-design-gatekeeper-i01-w02b-review-progress-v0.3.md); Section 1 accepted on 2026-10-05 after G–H; no execution or closure |
| Work authority | W01 closure grants W02; Owner's 2026-10-03 instruction continues the work |
| Source pin | `0dc8d61144e82271839194de1fa7a466bbb4f92b`, plus the accepted numeric-token addendum |
| Governing numeric decision | [SAD04-I01-NUM-001](../solution-design/test-design-gatekeeper-sad-04-i01-numeric-token-limit-addendum-v0.1.md): REJECTED / exit 2 above 128 characters |
| Oracle basis | [W02-A](i01-w02-test-design.md), read with RA/SAD and their acceptance records |
| Fixtures / executable tests | Recipes and test design only; materialization remains W02-C |
| Execution / closure | No runtime results, W02 closure or I-01 acceptance claimed |

### 1. Scope and counting

This inventory turns all 16 accepted I-01 conditions into test designs. Each row
has an explicit stimulus/state, expected observation, source route, test level,
evidence and fault point. It is not a claim of exhaustive defect coverage or full
fulfilment of a traced requirement. Later review/model/export/sealed clauses of
those requirements remain outside I-01.

One row can be parameterized. Its listed variants receive `.01`, `.02`, etc. in
the displayed order; a single-variant case keeps the row ID. No hidden Cartesian
product is counted. Running one variant at two levels is not two distinct input
variants. The 72 rows and 208 listed parameter variants are design inventory counts, not tests collected or
executed. Additional combinations may be needed when W02-C binds concrete seams.

### 2. Common fixture and observation contract

All bytes are public/synthetic, including cases whose **declaration** says
confidential. No actual confidential data is needed. Default context is the
accepted Windows x64 / CPython 3.13 laboratory target, an initialized isolated
schema-1 workspace, attributable logical operator `qa-demo`, synthetic
classification and `lab-development` purpose. Use public service boundaries;
lower-level tests explicitly target the named parser/persistence/admission seam.

`BASE-01` is a recipe for a native version-1.0 envelope. Its content declares a
synthetic customer-registration scope; basis `BR-AGE-01` states that integer ages
18 through 120 inclusive are accepted; TC `TC-CREATE-01` submits age 30 and expects
registration acceptance, with narrative preconditions, a structured step,
`HUMAN_AUTHORED` origin and a `basis_refs` link. This is supplied test data, not a
business rule inferred or assessed by I-01. Human authority does not arise from
payload fields. W02-C will materialize and independently inspect the exact bytes.

Unless a row says otherwise: clone BASE-01, vary only the stated factor, use a new
operation ID and a healthy eligible store, perform the indicated operation, and
inspect both observable result and relevant durable/non-effect boundary. A unit
test checks its component consequence; it cannot claim persistence or CLI proof.
Other size/count limits stay below their thresholds. An operation ID reused by a
retry is deliberate. Never use TDG's produced projection as the expected fixture.

| Shorthand | Required observation at the applicable level |
| --- | --- |
| CAP | Completed controlled capture is CAPTURED with coherent original/projection/inventory/receipt and generated identities; package reference only after commit; minimum NOT_EVALUATED with MINIMUM_CHECK_NOT_ENABLED_IN_I01; review not performed; CLI successful delivery exits 0 |
| REJ | Input-contract rejection: REJECTED, exit 2 at CLI, no new committed package/reference, minimum NOT_EVALUATED; safe issue/receipt only where permission and persistence allow |
| FAIL | Attempted capture fails before commit: FAILED if failure receipt can safely persist, no new package; operational persistence/resource failure exits 4, explicit interruption exits 130 |
| Gate pass/failure | Exact component-level capacity/permission decision stated in the row; a gate pass alone does not claim full capture, and a gate failure is not an invented universal receipt-status/CLI mapping |

CLI syntax errors and admission-policy refusal are different boundaries. Missing
required arguments/invalid CLI choices are exit 2; a well-formed command refused
by applicable admission policy is exit 3. The service-level negative admission
cases do not require an otherwise unsupported CLI value to reach the service.
Only the numeric-token excess has the new specific REJECTED/2 classification;
do not generalize it to other resource failures. When a full CLI mapping is not
specified by a row, its present oracle concerns the named lower-level boundary.

An atomic capture assertion uses a separate store connection after completion or
restart. Compare prior immutable records, not the whole changing SQLite file:
an honest FAILED receipt or operation intent may legitimately add rows. When a
store cannot be inspected, lack of access is not evidence of absent records.

### 3. Levels, evidence and fault points

| Level | Planned evidence boundary |
| --- | --- |
| U | Unit/component: syntax, projection, counters, literal mapping or validation; no simulated database result presented as durability proof |
| I | Integration: real disposable SQLite store and collaborating services; process variants start distinct processes |
| W | Native Windows: real directory/reparse/mutex/Job Object/resource behavior; unavailable/skipped platform evidence is not PASS |
| C | CLI/system: actual entry point, stdout/stderr, exit code and independently inspected effects |

These test levels concern **TDG itself**. They do not expand TDG's supported
domain beyond system-level functional black-box TC.

| Design technique | Application in this inventory |
| --- | --- |
| Equivalence partitioning | Supported/unsupported envelope and syntax, field presence/types, origins, selected-source classes and admission declarations: groups B–D and G |
| Boundary-value analysis | Numeric tokens 127/128/129 and below/at/above byte/depth/node/item/frame bounds: TC-I01-018, 038–043; real resource enforcement additionally needs native observations |
| Decision combinations | Eligible classification plus purpose versus missing/denied trusted context and unavailable containment: TC-I01-034–037, 047; payload approval never substitutes for trusted permission |
| State transitions | Capture before/after commit, acknowledgement loss, failed receipt, terminal-operation inspection and new attempt: TC-I01-004–010, 049–053, 058–060 |

These are targeted techniques and combinations, not claims of every possible
partition, decision-table column or state transition being covered. Do not force
all four techniques onto each case.

| Evidence | What W02-C must arrange and later retain |
| --- | --- |
| E1 | Versioned raw fixture/recipe and independently verified byte length, digest, lexical/presence/order/count expectations; no expected result copied from TDG output |
| E2 | Receipt/projection plus separate store inspection, IDs, links, row counts, unchanged prior-record digests and restart observation as applicable |
| E3 | Ordered operation/fault trace and boundary observers for source opens, worker release, network/execution attempts, transaction effects and recovery; include a harmless observer-positive control |
| E4 | Captured bounded stdout/stderr/routine logs, synthetic leakage markers, escaped-display checks and safe diagnostic cause; no new raw-payload log archive |
| E5 | Windows build, effective policy, filesystem/runtime configuration, process/handle/job observations, memory/time/size measurements and cleanup; separate configured limits from exercised enforcement |

| Fault point | Controlled event |
| --- | --- |
| F0 | Before operation intent can be retained |
| F1 | Required containment setup before worker receives input |
| F2 | After safe intent/admission, around source acquisition or before capture transaction |
| F3 | Worker-result validation or capture transaction before successful COMMIT; exact substep specified by the case |
| F4 | Worker processing/cancellation/timeout/resource exhaustion |
| F5 | After successful COMMIT but before acknowledgement/output delivery |
| F6 | Attempt to persist the failure receipt after initial capture failure |

Failures are injected at owned boundaries; mocks alone cannot prove SQLite
atomicity, filesystem protection or Windows containment. Clock-controlled unit
checks of timeout decisions complement native measurements. Native timing/memory
harnesses must account for measured overhead and record observation validity;
they must not add an arbitrary grace period that changes the product limit.

### 4. Concrete cases

In Trace, numbers before `/` mean `TCND-I01-xx`. Short oracle names such as
`FID-005` mean `OR-I01-FID-005` in W02-A; slash suffixes retain the same prefix.
Direct RA/SAD clauses supply the oracle for the newly expanded protection/store
cases. Section 5 provides each condition's requirement/VAL route.

#### A — Capture, identity and lineage

| ID / variants | Controlled stimulus or state | Expected observation | Trace | Level | Evidence / fault |
| --- | --- | --- | --- | --- | --- |
| TC-I01-001 / 1 | Import BASE-01 into a fresh eligible workspace; terminate normally, reopen in another process and inspect receipt/version. | CAP; original bytes, digest, length, ordered inventory and coherent references survive restart. | 01,15 / FID-005; RCP-001/004 | I + C | E1,E2; none |
| TC-I01-002 / 3 | Use CRLF, alternate insignificant JSON whitespace, or escaped versus literal Unicode; new operation per source. | Retain each exact source instance; separate versions, no normalization or merging from apparent logical equality. | 01,02,06 / FID-003/005; ID-003/008 | U + I | E1,E2; none |
| TC-I01-003 / 3 | Add unknown key a/b, a~b, or empty key, with a distinct marker. | Located marker resolves through original artifact plus correctly escaped JSON Pointer; no full host path required. | 01,06,14 / FID-006; RA09 §4.1 | U + I | E1,E2,E4; none |
| TC-I01-004 / 1 | After commit, suppress acknowledgement; repeat import with same operation ID, readable identical input and unchanged fingerprint components. | Same committed receipt/version; no second source, snapshot or inventory effect. | 02,11 / ID-001 | I + C | E2,E3; F5 |
| TC-I01-005 / 7 | At the fingerprint-comparison seam, reuse operation ID changing one component: bytes, selected-input identity, action, actor context, predecessor, mapping version, policy version. Supply valid context; this does not activate a new runtime mapping/policy. | Conflict; prior outcome/receipt/version unchanged. CLI-exposed conflicts exit 5; service tests assert the service conflict. | 02 / ID-002; SAD-04 §7.2/§8 | U + I; C for exposed variants | E2,E3; F5 |
| TC-I01-006 / 3 | After acknowledgement loss, inspect receipt while original source is edited, deleted or unreadable. | Same stored committed result; zero external-source opens or recapture. | 02,11,16 / ID-007 | I + C | E2,E3; F5 |
| TC-I01-007 / 2 | Repeat import with same operation ID after selected source deletion or read denial. | Input-acquisition failure; no invented identical fingerprint, fresh capture or overwrite of committed result; receipt remains inspectable. | 02,11,16 / ID-010 | I + C | E2,E3; none |
| TC-I01-008 / 1 | Submit identical bytes with a new operation ID and no predecessor. | New version and new lineage; equal hashes cannot merge identities. | 02 / ID-003/008 | I | E1,E2; none |
| TC-I01-009 / 2 | Select existing version as predecessor in a new operation with edited TC or unchanged bytes. | One new immutable child in selected lineage; parent content/receipt unchanged; no claim that TC was repaired. | 03 / ID-004 | I | E1,E2; none |
| TC-I01-010 / 2 | Use nonexistent predecessor version ID or an existing operation ID in place of version ID. | No child commit; predecessor conflict and CLI exit 5; prior records unchanged. | 03 / ID-005; SAD-04 §7.2/§8 | I + C | E2; none |

#### B — Envelope, syntax and exact numbers

| ID / variants | Controlled stimulus or state | Expected observation | Trace | Level | Evidence / fault |
| --- | --- | --- | --- | --- | --- |
| TC-I01-011 / 3 | Remove document_type, contract_version or content, one per input. | REJ; no guessed default, schema or snapshot. | 04 / ENV-002 | U + C | E1,E2,E4; none |
| TC-I01-012 / 2 | Add same unknown marker at root versus inside content. | Root: REJ. Content: CAP with marker retained, located and mapping state visible. | 04,06,08 / ENV-003/007 | U + I | E1,E2; none |
| TC-I01-013 / 9 | Wrong types: document_type null/integer; contract_version null/number; content null/array/string; separately whole document array/scalar. | REJ in every variant; no type coercion. | 04 / ENV-004; SAD-04 §6.1 | U + C | E1,E2; none |
| TC-I01-014 / 4 | Set kind to review_export, review_package_snapshot or unknown-kind; separately set contract_version to 999.0. | REJ; no restore, migration or newest-version fallback. | 04 / ENV-005 | U + C | E1,E2; none |
| TC-I01-015 / 1 | Exact supported envelope with content={} and eligible context. | CAP; missing content dimensions remain visible; minimum NOT_EVALUATED, never MET/NOT_MET. | 04,15 / ENV-001/006; RCP-004 | U + I + C | E1,E2; none |
| TC-I01-016 / 3 | Duplicate member at root, inside TC, or using names a and escaped \u0061 in one object. | REJ before lossy last-value-wins projection; duplicate detection uses decoded member names. | 05 / SYN-001; RA09 §3.3 | U + C | E1,E3; none |
| TC-I01-017 / 7 | Leading UTF-8 BOM, invalid UTF-8 byte, comment, trailing comma, NaN, Infinity or -Infinity. | REJ with syntax/profile cause; no automatic repair or lossy projection. | 05 / SYN-002/003 | U + C | E1,E2,E4; none |
| TC-I01-018 / 3 | Unquoted 1 followed by 126, 127 or 128 zeros in test_data.n; other prerequisites valid. | 127/128 characters: CAP on complete controlled path. 129: REJECTED / exit 2, safe limit/location diagnostic, no package/reference, minimum NOT_EVALUATED. | 05,10 / SYN-004; SAD04-I01-NUM-001 | U + I + C | E1,E2,E4; none |
| TC-I01-019 / 3 | Use in-bound lexeme 9007199254740993, 0.1000000000000000000001 or -0. | Exact lexeme/source location retained; exact projection or explicit limited projection with source reference; no rounded source claim or false length violation. | 05,06 / SYN-005 | U + I | E1,E2; none |
| TC-I01-020 / 1 | Use 129 digits as a JSON string in test_data. | CAP under the text bound; no numeric-token limit or implicit conversion. | 05,06,10 / FID-003; SYN-004; SAD-04 §6.1/§9 | U + I | E1,E2; none |

#### C — Content, presence and accountability

| ID / variants | Controlled stimulus or state | Expected observation | Trace | Level | Evidence / fault |
| --- | --- | --- | --- | --- | --- |
| TC-I01-021 / 7 | Text-only title: absent, null, empty string, whitespace-only, text, integer, empty array. | Preserve ABSENT, NULL, EMPTY, WHITESPACE_ONLY, VALUE, TYPE_MISMATCH, TYPE_MISMATCH respectively; CAP despite deficiency. | 06 / FID-001/004; RA09 §3.3 | U + I | E1,E2; none |
| TC-I01-022 / 3 | Steps as narrative, ordered objects with nested expected_result, or repeated identical steps with numbering. | CAP; representation, order, repeated items, numbering and nested expectations preserved; no invented actions. | 01,06 / FID-002 | U + I | E1,E2; none |
| TC-I01-023 / 2 | Same source_id on two TC; separately on two basis elements referenced by a TC. | Distinct internal IDs; duplicates/ambiguous reference retained; no guessed target. | 06 / FID-007; RA09-REQ-009 | U + I | E1,E2; none |
| TC-I01-024 / 4 | Source IDs with leading zeros, case differences, surrounding whitespace, or canonically equivalent but differently encoded Unicode. | Preserve supplied strings/code points; no trimming, case folding, normalization or merging. | 01,06 / FID-003 | U + I | E1,E2; none |
| TC-I01-025 / 3 | Unknown nested content, malformed test_cases member, or title-only TC. | CAP under valid envelope/safety conditions; raw located boundary, inventory deficiency and applicable issue remain. | 06,15 / FID-004; ENV-007; RA09-REQ-012 | U + I | E1,E2; none |
| TC-I01-026 / 5 | Each origin literal: HUMAN_AUTHORED, HUMAN_CONTROLLED_AI_ASSISTED, WITHOUT_ACCOUNTABLE_ADOPTION, OTHER, UNKNOWN. | Preserve declaration and literal mapping; no I-01 eligibility verdict or human-authority grant. | 07,15 / AUTH-001; RCP-004 | U + I | E1,E2; none |
| TC-I01-027 / 2 | Origin is written by QA engineer; separately lowercase human_authored under a mapping with no alias for it. | Preserved text with UNMAPPED meaning, no inferred authorship or alias. | 07 / AUTH-002; RA09 §4.2 | U | E1,E2; none |
| TC-I01-028 / 2 | Valid case_defaults with one absent and one explicitly declared case field; repeat for origin and accountability. | Default affects only absent field in declared set; explicit declaration preserved; supplied and effective values distinguishable. | 07 / AUTH-003/004 | U + I | E1,E2; none |
| TC-I01-029 / 6 | Positive defaults versus per-case origin null, empty, UNKNOWN, wrong type, free text; or accountability.accepted=false. | No upgrade by defaults; preserve explicit presence, mapping and negative declaration. | 07 / AUTH-004/005 | U + I | E1,E2; none |
| TC-I01-030 / 1 | Payload accountability.accepted=true and ROLE-03/actor claim without corresponding trusted authority. | Declaration only; no positive accountability or role grant from Boolean/text; minimum and qualification not assessed. | 07,08,15 / AUTH-005; FID-009 | U + I | E1,E2,E3; none |

#### D — Untrusted data and admission

| ID / variants | Controlled stimulus or state | Expected observation | Trace | Level | Evidence / fault |
| --- | --- | --- | --- | --- | --- |
| TC-I01-031 / 5 | Put URL, local path, $ref, issue key or executable-looking instruction inside content; instrument boundary effects. | CAP as inert data; no supplied-reference read, schema fetch, network call or code execution. | 08,16 / FID-008; RA08-REQ-010; RA08-VAL-004/007 | U + I | E1,E3,E4; none |
| TC-I01-032 / 5 | Payload package_id, role, approval, status or qualification field. | Preserve declaration; no ID restoration, authority change, accepted history or manufactured review result. | 08,15 / FID-009; RA09-REQ-024 | U + I | E1,E2,E3; none |
| TC-I01-033 / 2 | Declare unbound tc_sources or supporting_sources; operation selects only primary JSON. | Inventory remains one selected source; unbound/unsupported issue visible; no file search/attachment opening. | 08,16 / FID-010 | U + I | E1,E2,E3; none |
| TC-I01-034 / 2 | Trusted context declares public or synthetic, laboratory profile and lab-development purpose. | Admission permits selected path; CAP when remaining controls hold; context declaration preserved. | 09 / SAD-04 §9; RA08-REQ-004; RA08-VAL-003 | I + C | E2,E3; none |
| TC-I01-035 / 4 | At admission-service boundary, classification absent, UNKNOWN, confidential or conflicting; file bytes remain synthetic. | Policy refusal before parser release; no captured package or prohibited processing; bounded permitted metadata only. Do not assert CLI behavior for invalid CLI tokens. | 09 / SAD-04 §8/§9; RA08-REQ-004/020; RA08-VAL-003 | I | E2,E3,E4; none |
| TC-I01-036 / 2 | Admission service receives missing lab-development purpose; separately payload says public/approved while trusted context denies. | Refuse before parser release; payload cannot fill/override authority; no sealed fallback. | 08,09 / SAD-04 §8/§9; RA08-REQ-004; RA08-VAL-003 | I | E2,E3,E4; none |
| TC-I01-037 / 1 | After admission, before commit, introduce an explicit policy/operator indication that classification is in doubt; synthetic fixture only. | Stop affected capture/delivery; safe diagnostic and policy-permitted handling; no automatic classifier claim or external service request. | 09,12 / SAD-04 §9; RA08-REQ-004/020; RA08-VAL-003/014 | I | E2,E3,E4; F2 |

#### E — Capacity and containment

| ID / variants | Controlled stimulus or state | Expected observation | Trace | Level | Evidence / fault |
| --- | --- | --- | --- | --- | --- |
| TC-I01-038 / 3 | Valid JSON of 1 MiB minus 1, exactly 1 MiB, plus 1 byte; distribute padding below individual-string bound. | First two pass raw-size gate; above bound read stops by limit+1, explicit size failure, no complete capture or unbounded read. | 10 / SAD-04 §9; RA09-REQ-016; RA09-VAL-003 | U + I | E1,E3; none |
| TC-I01-039 / 3 | 31, 32, 33 nested containers, root object counted at depth 1; other limits controlled. | 31/32 pass depth gate; 33 fails before accepted complete projection/capture; no silent subtree drop. | 10 / SAD-04 §9; RA09-REQ-016; RA09-VAL-003 | U | E1,E3; none |
| TC-I01-040 / 3 | 19,999 / 20,000 / 20,001 JSON values; count every container/scalar once, exclude object member names. | Below/at pass node gate; above fails without skipped remainder; independent fixture count agrees. | 10 / SAD-04 §9; RA09-REQ-016; RA09-VAL-003 | U | E1,E3; none |
| TC-I01-041 / 6 | Decoded UTF-8 length 65,535 / 65,536 / 65,537 bytes, first as text value then member name; multibyte literals in values, escaped multibyte characters in names. | Below/at pass; above fails; bound uses decoded UTF-8 bytes, not character count or raw escape length. | 10 / SAD-04 §9; RA09-REQ-016; RA08-REQ-010 | U | E1,E3; none |
| TC-I01-042 / 6 | 199 / 200 / 201 native TC entries; repeat for basis elements; include malformed members, keep node/raw-size bounds valid. | Below/at pass respective capacity gate; above fails; malformed entries count and cannot be discarded to fit. | 06,10 / SAD-04 §9; RA09-REQ-016; RA08-REQ-010 | U + I | E1,E2,E3; none |
| TC-I01-043 / 3 | Otherwise valid, operation-bound worker projection frame of 8 MiB minus 1, exactly 8 MiB, plus 1 byte. | Below/at pass frame-size gate; oversized output refused before persistence; no truncated accepted projection or package. | 10 / SAD-04 §9; RA09-REQ-016; RA08-REQ-010/020 | I | E2,E3; F3 |
| TC-I01-044 / 3 | Worker result has wrong operation ID, malformed shape or truncated framing, within size bound. | Parent refuses result; no committed capture or worker-controlled identity/effect. | 10,12 / SAD-04 §7.2/§9; RA08-REQ-010/020 | I | E2,E3; F3 |
| TC-I01-045 / 2 | Controlled Windows worker completes before deadline; separately worker deliberately never completes. | Normal result may proceed; stalled worker terminated under 5-second wall-time policy with no capture/live child. Record enforcement latency; do not invent zero scheduling tolerance. | 10,11 / SAD-04 §9; RA09-REQ-016; RA08-REQ-010/013/020 | W | E3,E5; F4 |
| TC-I01-046 / 2 | Measured job-accounted committed memory below 512 MiB; separately force demand above bound. | Limit applied before input release and exercised by above-bound denial/termination; no uncontrolled continuation or capture on exhaustion. | 10 / SAD-04 §9; RA09-REQ-016; RA08-REQ-010/020 | W | E3,E5; F4 |
| TC-I01-047 / 2 | Fail Job Object creation; separately fail worker assignment/required-limit setup. | No input release to uncontained worker, fallback parse in parent or capture; safe containment cause. | 09,10 / SAD-04 §9; RA08-REQ-020; RA08-VAL-014 | W + I | E2,E3,E5; F1 |
| TC-I01-048 / 3 | Verify max_page_count × page_size at 512 MiB policy; allocate up to cap, then request an additional page with journal space separately controlled. | Policy arithmetic correct; no main-file growth beyond cap; excess allocation fails safely without partial package or false CAP; preserve prior history. | 10,12 / SAD-04 §7/§9; RA05-REQ-017/019; RA09-REQ-016 | I + W | E2,E3,E5; F3 |

#### F — Transactions, interruption and recovery

| ID / variants | Controlled stimulus or state | Expected observation | Trace | Level | Evidence / fault |
| --- | --- | --- | --- | --- | --- |
| TC-I01-049 / 3 | Fail after original insert, after version/inventory insert or after receipt insert before COMMIT; failure-receipt storage remains usable. | Rollback full capture; retain FAILED receipt separately with cause and no package reference; no orphan capture records or changed prior package. | 11,12 / RCP-003; ID-006; RA05-VAL-012 | I | E2,E3; F3 |
| TC-I01-050 / 3 | Crash before intent, after intent or immediately before capture commit; restart after external file changes with storage usable. | No captured package; a retained interrupted intent is reconciled to FAILED with cause. If no intent survived, do not invent one; no hidden import or fabricated completion. | 11 / ID-006; SAD-04 §7.2; RA05-VAL-012 | I processes | E2,E3; F0/F2/F3 |
| TC-I01-051 / 2 | Cancel during acquisition or worker processing before commit; failure receipt can be stored. | No package; FAILED receipt with cancellation cause and NOT_EVALUATED; CLI exit 130; safe child/copy cleanup. | 11 / ID-006; SAD-04 §6.2/§7.2/§8; RA05-VAL-012 | I + W + C | E2,E3,E5; F2/F4 |
| TC-I01-052 / 2 | After COMMIT/before acknowledgement, crash process or fail output delivery, then restart. | CAPTURED remains authoritative; inspect same version; output failure cannot relabel committed capture FAILED. | 02,11 / ID-007; RCP-001; RA05-VAL-012 | I processes + C | E2,E3; F5 |
| TC-I01-053 / 2 | Fail capture and failure-receipt write; use existing safe intent versus no retained intent. | No new package/final receipt; safe diagnostic, exit 4 and explicit absence of durable failure receipt. After access restored inspect real evidence and unchanged prior history. | 11,12,14 / RCP-006; RA05-VAL-012; RA08-VAL-014 | I + C | E2,E3,E4; F3/F6 |
| TC-I01-054 / 2 | Exhaust database/journal storage for next capture; separately deny workspace write permission after prior valid capture. | Safe dependent failure with no partial new package; preserve prior records; no unsafe truncation, rebuild or raw temp fallback. | 12 / SAD-04 §7.2/§9; RA05-REQ-017/019; RA08-REQ-020; RA08-VAL-014 | I + W | E2,E3,E5; F3 |
| TC-I01-055 / 2 | Controlled corrupt store; separately unknown/newer schema version. | Refuse affected writes/unsupported opening without migration, repair or empty-store replacement; preserve original store. | 12,13 / SAD-04 §7.3; RA05-REQ-019 | I + C | E2,E3; none |
| TC-I01-056 / 2 | Fail mandatory receipt/history insertion while other writes work; separately fail only optional diagnostic sink. | Mandatory failure blocks capture atomically; optional-debug failure alone cannot block otherwise safe CAP. | 12 / SAD-04 §9; RA05-REQ-017; RA08-REQ-020; RA08-VAL-014 | I | E2,E3,E4; F3 |
| TC-I01-057 / 1 | Inspect SQLite connection settings; attempt capture relation with nonexistent required parent at persistence boundary. | Explicit transaction policy: autocommit enabled, BEGIN IMMEDIATE/COMMIT/ROLLBACK, foreign_keys ON, DELETE journal, synchronous FULL; no committed dangling capture. | 12 / SAD-04 §7.1; RA05-REQ-017; RA05-VAL-001/012 | I | E2,E3; none |
| TC-I01-058 / 2 | Inspect finalized REJECTED or FAILED operation; then make deliberate fresh attempt with new operation ID. | Terminal history preserved; new attempt separately attributable; no hidden reopening or rerun by inspection/recovery. | 02,11 / SAD-04 §7.2; RA05-REQ-018/019; RA05-VAL-012 | I + C | E2,E3; none |

#### G — Concurrency and source selection

| ID / variants | Controlled stimulus or state | Expected observation | Trace | Level | Evidence / fault |
| --- | --- | --- | --- | --- | --- |
| TC-I01-059 / 2 | Process A holds workspace mutex; B imports; release within configured wait versus hold beyond 5 seconds. | B cannot release worker/write while A owns mutex; in-bound release permits B; expiry gives bounded busy failure without capture or bypass. | 10,13 / SAD-04 §7.1/§9; RA05-REQ-017/018 | W processes | E2,E3,E5; none |
| TC-I01-060 / 1 | Terminate mutex owner with unfinished intent; next authorized operation follows reconciliation. | Mutex available after process exit; unfinished operation not successful; no duplicate effect. | 11,13 / SAD-04 §7.1/§7.2; RA05-REQ-019 | W processes | E2,E3,E5; F2 |
| TC-I01-061 / 2 | Hold real SQLite write contention below/above configured wait while importer owns application mutex. | Bounded wait; explicit failure on expiry; no duplicate writer effect, lock bypass or unsafe write. | 12,13 / SAD-04 §7.1/§9; RA05-REQ-017 | I processes | E2,E3,E5; none |
| TC-I01-062 / 4 | Receipt/package read against absent DB, unsupported schema, valid store, valid store with concurrent writer transaction. | No creation, initialization, upgrade or write by read. Deliver committed records when SQLite permits; otherwise honest busy/inability, never fabricated empty success. | 12,13 / SAD-04 §7.1/§7.3; RA05-REQ-017 | I + C | E2,E3; none |
| TC-I01-063 / 4 | Select directory, URL, UNC/network source or archive instead of supported primary local JSON. | Refuse unsupported source; no traversal, fetch, expansion or package capture. | 08,16 / SAD-04 §9; RA08-REQ-010; RA08-VAL-004 | I + W + C | E2,E3; none |
| TC-I01-064 / 2 | Selected source is symlink/reparse redirect; separately redirect path after admission before acquisition. | Refuse/detect redirected input; no undeclared source read or mixed instance capture. | 16 / ID-009; SAD-04 §7.1/§9; RA08-VAL-004 | W | E1,E3,E5; F2 |
| TC-I01-065 / 2 | Change selected source during acquisition; separately change external file only after retained-byte acquisition finishes. | Detected acquisition change fails capture. Later external changes cannot alter retained instance: hash/parse same bytes, never reread to substitute new content. | 01,16 / ID-009; SAD-04 §7.1 | I + W | E1,E3; F2 |
| TC-I01-066 / 1 | Neighbour file appears to match a supplied reference; monitor opens/enumeration while only primary JSON selected. | No neighbour search, heuristic binding or hidden context; acquire only declared source. | 08,16 / FID-010; SAD-04 §9; RA03-REQ-005 | I + W | E1,E3; none |

#### H — Diagnostics, copies and capability boundaries

| ID / variants | Controlled stimulus or state | Expected observation | Trace | Level | Evidence / fault |
| --- | --- | --- | --- | --- | --- |
| TC-I01-067 / 3 | Display retained field with ESC/control characters, remote-image markup or executable-looking text. | Bounded escaped inert display; no resource opening/execution; original bytes unchanged. | 14 / SAD-04 §9; RA08-REQ-010/014; RA08-VAL-007/011 | U + C | E1,E3,E4; none |
| TC-I01-068 / 3 | Force parser, worker or persistence error containing synthetic payload/secret/full-path markers. | Routine diagnostics exclude markers/unnecessary full path; preserve bounded cause/context, no raw evidence in logs. | 14 / RCP-005; RA08-REQ-014; RA08-VAL-011 | I + C | E4; F3/F4 |
| TC-I01-069 / 1 | Display long retained field below intake limits. | Bounded escaped output with explicit truncation; stored source untouched. Exact display-size setting is a W02-C binding prerequisite, not invented here. | 14 / SAD-04 §6.1/§9; RA08-REQ-010/014 | C | E1,E2,E4; none |
| TC-I01-070 / 3 | Observe managed copies after success, pre-commit cancellation or capture failure with synthetic markers. | No separate raw-input temp file or automatic backup; journals inside managed directory; no automatic age deletion or unsupported secure-erasure claim. | 11,14 / SAD-04 §9; RA08-REQ-013; RA08-VAL-014 | W | E2,E3,E5; F3/F4 |
| TC-I01-071 / 2 | Capture rich TC versus TC missing expected_result/basis content, with other controls satisfied. | Minimum NOT_EVALUATED with I-01 reason; no qualification, run, ledger, findings, availability or approval fabricated. | 15 / RCP-004; RA03-REQ-032/050; RA09-REQ-017 | I + C | E2,E4; none |
| TC-I01-072 / 4 | Attempt model invocation, CSV import, review export or sealed processing through available adapters/services. | Explicit unavailable/denied result; no model/network start, source repair or hidden fallback; capability manifest matches enabled surface. | 15 / SAD-04 §4/§8/§9; RA08-REQ-001; RA08-VAL-001 | I + C | E3,E4; none |

### 5. Bidirectional condition trace

This is planned clause-level evidence within I-01. A route to a VAL that also
covers CSV, review, export or sealed processing claims only its applicable
capture/protection part. A row is not a new requirement or an executed result.

| Condition | Case rows | Requirement / validation / design route |
| --- | --- | --- |
| TCND-I01-01 | TC-I01-001, TC-I01-002, TC-I01-003, TC-I01-022, TC-I01-024, TC-I01-065 | RA03-REQ-003/006/020; RA09-REQ-005/014; RA09-VAL-005/011/012 |
| TCND-I01-02 | TC-I01-002, TC-I01-004, TC-I01-005, TC-I01-006, TC-I01-007, TC-I01-008, TC-I01-052, TC-I01-058 | RA03-REQ-048; RA05-REQ-018; RA09-REQ-009/014; RA05-VAL-012; RA09-VAL-008/012 |
| TCND-I01-03 | TC-I01-009, TC-I01-010 | RA03-REQ-043/044/047; RA03-VAL-020/022; SAD-04 §7.2 |
| TCND-I01-04 | TC-I01-011, TC-I01-012, TC-I01-013, TC-I01-014, TC-I01-015 | RA09-REQ-001/003/013; RA09-VAL-002/011 |
| TCND-I01-05 | TC-I01-016, TC-I01-017, TC-I01-018, TC-I01-019, TC-I01-020 | RA09-REQ-004/006/016; RA09-VAL-003; SAD04-I01-NUM-001 |
| TCND-I01-06 | TC-I01-002, TC-I01-003, TC-I01-012, TC-I01-019, TC-I01-020, TC-I01-021, TC-I01-022, TC-I01-023, TC-I01-024, TC-I01-025, TC-I01-042 | RA03-REQ-014/022/025; RA09-REQ-006/007/012; RA09-VAL-003/006/008 |
| TCND-I01-07 | TC-I01-026, TC-I01-027, TC-I01-028, TC-I01-029, TC-I01-030 | RA03-REQ-021; RA09-REQ-008/024; RA09-VAL-007/008 |
| TCND-I01-08 | TC-I01-012, TC-I01-030, TC-I01-031, TC-I01-032, TC-I01-033, TC-I01-036, TC-I01-063, TC-I01-066 | RA03-REQ-005; RA09-REQ-003/005/023/024; RA09-VAL-002/005/013; RA08-VAL-004/007 |
| TCND-I01-09 | TC-I01-034, TC-I01-035, TC-I01-036, TC-I01-037, TC-I01-047 | RA03-REQ-042; RA08-REQ-004/020; RA08-VAL-003/014 |
| TCND-I01-10 | TC-I01-018, TC-I01-020, TC-I01-038, TC-I01-039, TC-I01-040, TC-I01-041, TC-I01-042, TC-I01-043, TC-I01-044, TC-I01-045, TC-I01-046, TC-I01-047, TC-I01-048, TC-I01-059 | RA09-REQ-016; RA08-REQ-010/020; RA09-VAL-003/012; RA08-VAL-004/014 |
| TCND-I01-11 | TC-I01-004, TC-I01-006, TC-I01-007, TC-I01-045, TC-I01-049, TC-I01-050, TC-I01-051, TC-I01-052, TC-I01-053, TC-I01-058, TC-I01-060, TC-I01-070 | RA05-REQ-017/018/019; RA09-REQ-014/015; RA05-VAL-012; RA09-VAL-012 |
| TCND-I01-12 | TC-I01-037, TC-I01-044, TC-I01-048, TC-I01-049, TC-I01-053, TC-I01-054, TC-I01-055, TC-I01-056, TC-I01-057, TC-I01-061, TC-I01-062 | RA05-REQ-017/019; RA08-REQ-020; RA09-REQ-014/016; RA05-VAL-012; RA08-VAL-014 |
| TCND-I01-13 | TC-I01-055, TC-I01-059, TC-I01-060, TC-I01-061, TC-I01-062 | SAD-D-001/003; RA05-REQ-017/018; RA05-VAL-012; SAD-04 §7.1/§7.3 |
| TCND-I01-14 | TC-I01-003, TC-I01-053, TC-I01-067, TC-I01-068, TC-I01-069, TC-I01-070 | RA03-REQ-030; RA08-REQ-014; RA09-REQ-023; RA08-VAL-011; RA09-VAL-013 |
| TCND-I01-15 | TC-I01-001, TC-I01-015, TC-I01-025, TC-I01-026, TC-I01-030, TC-I01-032, TC-I01-071, TC-I01-072 | RA03-REQ-032/050; RA09-REQ-013/015/017; RA07-REQ-010; RA09-VAL-011/014; SAD-04 §6.2 |
| TCND-I01-16 | TC-I01-006, TC-I01-007, TC-I01-031, TC-I01-033, TC-I01-063, TC-I01-064, TC-I01-065, TC-I01-066 | RA03-REQ-005/006; RA09-REQ-005/014; RA09-VAL-005/012; RA08-VAL-004; SAD-04 §7.1/§9 |

### 6. Review boundary and W02-C binding work

The oracle designs above precede implementation. W02-C must materialize exact
fixture bytes, expand listed variants to separate stable IDs and bind assertions
to the selected service/CLI boundary. Preserve the original failing evidence if
the future implementation contradicts an accepted oracle; do not update expected
values merely to match it.

Before an affected executable test is considered ready:

- validate each recipe independently, including exact encoded byte sizes, decoded
  text sizes, numeric-token lengths and total depth/node counts;
- bind concrete issue-code and display-size configuration where accepted contracts
  leave implementation choices open; no invented code names or output thresholds;
- bind real transaction, process, worker and file-access fault seams without a
  universal abstraction created solely for tests;
- qualify the native observer/harness and record any platform or resource gap;
  a mocked control or skipped Windows test does not satisfy native evidence;
- keep end-to-end receipt/exit assertions separate from component gate assertions;
  resolve any genuinely missing product classification through change control;
- keep development fixtures exposed; do not later relabel them independent held-out
  acceptance data or call solo AI-assisted review independent assurance.

No automatic verdict is assigned from the number of cases. W02 remains open:
fixture/skeleton materialization, review corrections and the applicable completion
decision remain. W03 is not started by publication of this inventory.

### 7. Effort reassessment

This is a **provisional planning forecast for remaining test/evidence work**, not
measured human effort, an approved budget or the full I-01 implementation total.
Drivers are real transaction-fault setup, process interruption, platform controls,
boundary fixtures and diagnosis; case count alone is not the estimate.

| Activity | Allocation | Provisional human effort |
| --- | --- | ---: |
| Refine fixture/oracle recipes and materialize W02-C assets/skeletons | Remaining W02 | 8–14 h |
| Test adapters and persistence/crash injection harness | Testing share of W03/W05/W06 | 8–14 h |
| Native Windows containment/path/concurrency verification assets | Testing share of W04/W06 | 8–16 h |
| Execute and diagnose the selected suite | Testing share of W03–W07 | 6–10 h |
| Required retest and regression after changes | Testing share of W03–W07 | 4–8 h |
| Completion evidence and Owner walkthrough | W07 | 2–4 h |
| Testing/evidence subtotal | Remaining work; each activity counted once | 36–66 h |
| Separate provisional defect-correction contingency | Product fixes arising from execution; excludes diagnosis/retest above | 8–16 h |
| Test/evidence work plus that contingency | Planning hypothesis only | 44–82 h |

These ranges are author estimates, not an Owner-approved replacement ceiling.
Product feature implementation is not included; W01 and past analysis effort are
not reconstructed. Do not add this subtotal to all original W03–W07 estimates:
those already included testing and would double-count the same work. The original
40–62-hour full-I-01 hypothesis remains historical and challenged; no new full
increment total or delivery date is asserted here.

Revisit after the first fixture family and the first real persistence/native
harness, recording actual human effort by these categories, and again after
W03/W04. Approximately five flexible hours per week remains a capacity assumption,
not a schedule. Required coverage is not reduced to fit either forecast.

### 8. Preparation checks and handoff

The author checks unique case IDs, variant arithmetic, links, existing REQ/VAL
identities, all 16 condition routes, known W02-A oracle references, frozen baseline
preservation and consistency of the numeric decision. These are static document
checks, not executed product tests or independent review.

The Owner accepted Sections 2–3 and groups A–F without changes on 2026-10-04,
then groups G–H and Section 1 without changes on 2026-10-05. All 72 case rows / 208
listed variants have recorded test-design acceptance.
[SR-I01-W02B-001 v0.3](../reviews/test-design-gatekeeper-i01-w02b-review-progress-v0.3.md)
records Section 1 acceptance and carries forward v0.2, including the parked idea
of reusing case copies as future reviewer-development input. Sections 5–8,
including the Section 7 forecast, remain without separate Owner acceptance.
Resume with Section 5.

Review whether the stimuli can distinguish the required effects, whether the
oracles are supported, and whether the selected levels/faults provide sufficient
evidence. Corrections belong here before affected fixture/test materialization.
Acceptance of the case groups and Sections 2–3 does not close W02, accept the
remaining inventory/forecast, or establish execution evidence.

### Source navigation

- [RA-03 corrected baseline](../requirements-analysis/ra-10/test-design-gatekeeper-ra-03-review-package-content-provenance-validation-v0.4.md)
- [RA-05](../requirements-analysis/ra-05/test-design-gatekeeper-ra-05-findings-dispositions-persistence-v0.2.md), especially §§7.2–7.3 and VAL-012
- [RA-08](../requirements-analysis/ra-08/test-design-gatekeeper-ra-08-confidentiality-security-privacy-v0.2.md), especially §§4, 6.2, 7.1
- [RA-09](../requirements-analysis/ra-09/test-design-gatekeeper-ra-09-data-representations-import-export-contracts-v0.2.md)
- [Accepted SAD-04 v0.2](../solution-design/test-design-gatekeeper-sad-04-integrated-review-increment-plan-v0.2.md), §§6–9, 12–13
- [SAD-04 acceptance record](../reviews/test-design-gatekeeper-sad-04-review-record-v0.2.md)
- [W01 closure](i01-w01-closure.md)
