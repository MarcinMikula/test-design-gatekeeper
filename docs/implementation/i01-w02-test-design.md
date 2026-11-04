# Test Design Gatekeeper

## I-01 / W02 - Test Design, Oracle Basis, and Traceable Test Inventory

This document defines the expected observations for I-01 tests and links them to
the accepted requirements and design. The detailed cases are in the
[W02-B inventory](i01-w02-test-inventory.md); Section 11 indexes the prepared
W02-C test data.

| Field | Recorded basis |
| --- | --- |
| Preparation / review clarification | 2026-10-02 / 2026-10-03 (Europe/Warsaw) |
| Work item | I01-W02 — test preparation for bounded native-JSON capture and durable inspection |
| Earlier work authorization | [W01 closure](i01-w01-closure.md), 2026-09-29 |
| Original W02-A source inspection | Repository `main` after `e15438973564cc790237cce7e9f1bba5e14f4846` |
| Original clarification inspection | `d9a6b15513f94f710cd96853f46552c1499e0f79`; governing RA-09 and SAD-04 sources were unchanged |
| Original W02-B preparation | 2026-10-04, using `0dc8d61144e82271839194de1fa7a466bbb4f92b` plus the recorded Owner decision |
| W02-B decision | Inventory accepted on 2026-10-07 as the basis for W02-C; Section 10 links the decision |

**W02 remains open. Development and further test-data preparation are paused for
documentation cleanup.** [README.md](../../README.md) reports current capability,
prepared-data counts and execution limits. Test specifications and checks of input
files do not establish that TDG imports those files correctly or that I-01 is accepted.

## 1. Purpose

W02 prepares synthetic inputs, expected results and test skeletons before native
capture implementation. W02-A extracts the expected behavior from accepted
contracts; W02-B turns it into concrete cases; W02-C prepares the files and tests.

An **oracle** is the independently specified expected observation against which a
test will check TDG. Define it from the accepted contract before observing the
implementation. Copying an implementation result into the expected value would
remove that independent check.

## 2. W02 boundary

W02 covers test analysis, test design, synthetic test data, independent expected
results, links to the governing requirements and design, and executable skeletons.

### In scope

- extract effective native-JSON intake behavior from accepted requirements and
  design;
- identify independent receipt, source-fidelity, identity, retry, and lineage
  oracles;
- identify concrete equivalence classes and failure variants needed for the
  synthetic corpus;
- trace those oracles to accepted REQ/VAL/design sources and
  `TCND-I01-01` through `TCND-I01-16`;
- define concrete cases and expected observations in the W02-B inventory;
- prepare the input files and product test placeholders in W02-C;
- support W02 re-estimation using the detailed inventory and actual preparation
  effort.

### Out of scope

- implementation of the native JSON parser or projection (`I01-W03`);
- parser-worker containment, admission enforcement, source-copy/path protection,
  or safe-diagnostic implementation (`I01-W04`);
- SQLite capture, retry/recovery implementation, package lineage persistence, or
  other durable writer implementation (`I01-W05`);
- final CLI receipt/package inspection and integrated regression implementation
  (`I01-W06`);
- Windows completion walkthrough or I-01 completion decision (`I01-W07`);
- CSV intake;
- substantive TC review;
- model invocation;
- result export;
- sealed/confidential processing;
- any claim that TDG approves or repairs testware.

## 3. Effective authority and source precedence

Use the maintained requirements and consolidated design below. The source pins
above identify the original inspections; earlier wording remains available in
Git history. Preparation-time labels do not replace later recorded decisions.

### 3.1 RA-09

[RA-09 v0.2](../requirements-analysis/ra-09/test-design-gatekeeper-ra-09-data-representations-import-export-contracts-v0.2.md)
defines native input and receipt contracts. All 24 requirements and 16 validation
obligations are accepted. The [acceptance record](../requirements-analysis/ra-09/test-design-gatekeeper-ra-09-focused-static-review-v0.2.md)
closes F-001/F-002; their clarifications are incorporated in the current text.

### 3.2 RA-03

[RA-03 v0.4](../requirements-analysis/ra-10/test-design-gatekeeper-ra-03-review-package-content-provenance-validation-v0.4.md)
defines supplied content, provenance and identity. Its 50 requirements are
accepted: the [RA-03 gate](../reviews/test-design-gatekeeper-ra-03-gate-record-v0.2.md)
records requirement acceptance, and [SR-RA10-001 v0.2](../requirements-analysis/ra-10/test-design-gatekeeper-ra-10-focused-static-review-v0.2.md)
records the corrected v0.4 baseline.

### 3.3 SAD-02

[SAD-02](../solution-design/test-design-gatekeeper-sad-02-data-identity-contracts-v0.1.md)
now points to its historical record and the current rules in SAD-04. Its accepted
identity and retry decisions are in SAD-04 Section 5.1; I-01 commit, retry and
lineage rules are in Section 7.2. Oracle traces below use those current locations.

### 3.4 SAD-04

[SAD-04](../solution-design/test-design-gatekeeper-sad-04-integrated-review-increment-plan-v0.2.md)
is the consolidated design. Sections 6–9 define the native envelope, status
meanings, persistence, retry, CLI and protection boundaries; Section 12 retains
the 16 I-01 test conditions. Its [acceptance record](../reviews/test-design-gatekeeper-sad-04-review-record-v0.2.md)
and the [numeric-token decision](../solution-design/test-design-gatekeeper-sad-04-i01-numeric-token-limit-addendum-v0.1.md)
preserve the human decisions. Accepted corrections, including the numeric-token
outcome, are incorporated directly in SAD-04.

### 3.5 Conflict rule used by this document

Follow recorded acceptance and corrections when older wording differs. If those
sources do not resolve a material conflict, stop the affected work and request a
human decision. Do not choose an interpretation because it is easier to implement.

The original inspection found no blocking source-authority conflict. The
2026-10-03 review did identify a missing numeric-limit outcome classification;
the Owner resolved it as recorded in Section 9.5.

## 4. Oracle design rules

The following rules apply to every later fixture and executable test derived from
this document.

1. An oracle states only an observable consequence supported by the accepted
   contract.
2. Parsing success is not minimum admissibility, review success, package
   approval, or ISTQB conformity.
3. `CAPTURED`, `REJECTED`, and `FAILED` are intake outcomes, not review outcomes.
4. A package reference exists only after coherent durable capture.
5. I-01 always reports the core-minimum check as `NOT_EVALUATED`; substantive
   review is not performed.
6. Exact source bytes, projection, supplied declarations, generated identity,
   and later assessment meaning remain separate.
7. Source identity equality, content equality, or hash equality does not merge
   independent submissions.
8. Supplied role, approval, package ID, path, URL, `$ref`, status, or
   qualification-like content does not grant authority or trigger retrieval.
9. Missing, null, empty, whitespace-only, typed value, and type mismatch are
   distinct observations where the contract defines them.
10. A failing or rejected variant is valid evidence when rejection/failure is
    the required behavior; tests must not be weakened to force `CAPTURED`.
11. The later test must state what it does **not** establish.
12. The first meaningful RED observed during implementation/execution is
    preserved as evidence rather than overwritten by later GREEN.

## 5. W02-A independent oracle matrix

The matrix below is a pre-implementation oracle catalogue. IDs are stable working
identifiers for W02. They are not runtime issue codes and do not add product
requirements.

The 2026-10-03 clarification narrows `OR-I01-SYN-004` to the numeric-token
capacity bound and separates representation fidelity into `OR-I01-SYN-005`.
`OR-I01-ID-007` now explicitly concerns stored-result inspection/reconciliation;
import retries remain governed by `OR-I01-ID-001/002/010`.

### 5.1 Envelope, routing, and syntax

| Oracle ID | Controlled condition | Independent expected observation | Must not be inferred | Primary trace | I-01 condition |
| --- | --- | --- | --- | --- | --- |
| OR-I01-ENV-001 | Exact root members `document_type`, `contract_version`, `content`; kind=`review_package_input`; version=`1.0`; object-valued content | Envelope is eligible to proceed to the next permitted intake/capture stage | Minimum admissibility, review success, TC quality | RA09-REQ-001/003; RA09-VAL-002; SAD-04 §6.1 | TCND-I01-04 |
| OR-I01-ENV-002 | One required root envelope member absent | Native intake is `REJECTED`; no package version is created/referenced | A guessed default envelope or newest compatible schema | RA09-REQ-003; RA09-VAL-002; SAD-04 §6.1 | TCND-I01-04 |
| OR-I01-ENV-003 | Additional root envelope member | Native intake is `REJECTED`; no package version is created/referenced | That an unknown root field can be treated like unknown `content` | RA09-REQ-003; RA09-VAL-002; SAD-04 §6.1 | TCND-I01-04 |
| OR-I01-ENV-004 | Root member has wrong type, including non-object `content` | Native intake is `REJECTED`; no package version is created/referenced | Coercion into the required root type | RA09-REQ-003; RA09-VAL-002; SAD-04 §6.1 | TCND-I01-04 |
| OR-I01-ENV-005 | Unsupported/wrong `document_type` or `contract_version` | Native intake is `REJECTED`; no guessed schema/version is used | Restore/migration semantics or guessed compatibility | RA09-REQ-003/020/021; RA09-VAL-002; SAD-04 §6.1 | TCND-I01-04 |
| OR-I01-ENV-006 | Valid envelope with `content: {}` | Capture is permitted if other prerequisites allow it; in I-01 the minimum remains `NOT_EVALUATED` with the explicit I-01 limitation | That empty content is an envelope error, admissible package, or successful review | RA09-REQ-013/015; RA09-VAL-002/011; SAD-04 §6.1-6.2 | TCND-I01-04, 15 |
| OR-I01-ENV-007 | Unknown member inside `content` | Preserve the supplied member with source location/mapping state and applicable issue/limitation; do not execute it as control data | Operational instruction, authority, field invention | RA09-REQ-006/012; RA09-VAL-002/003; SAD-04 §6.1 | TCND-I01-06, 08 |
| OR-I01-SYN-001 | Duplicate JSON object member at any depth | Reject before last-value-wins or another lossy accepted projection can be constructed | Which duplicate value was "intended" | RA09-REQ-004; RA09-VAL-003; SAD-04 §6.1 | TCND-I01-05 |
| OR-I01-SYN-002 | Leading BOM on native JSON | Reject under the native JSON profile | BOM stripping followed by a success claim | RA09-REQ-004; RA09-VAL-003; SAD-04 §6.1 | TCND-I01-05 |
| OR-I01-SYN-003 | Invalid UTF-8, JSON comments, trailing comma, or non-finite numeric token | Reject under syntax/profile rules before lossy accepted projection | Automatic syntax repair or non-finite normalization | RA09-REQ-004; RA09-VAL-003; SAD-04 §6.1 | TCND-I01-05 |
| OR-I01-SYN-004 | Otherwise valid input contains a numeric token of 127, 128, or 129 characters; all other prerequisites and limits are satisfied | 127/128 do not fail the token-length check; 129 produces `capture_outcome=REJECTED`, CLI exit `2`, no new package version/reference and `minimum_check=NOT_EVALUATED`, with safe limit/location diagnostics. Do not round or truncate to fit. See the accepted §9.5 clarification | Successful capture from a length check alone; treating a hard capacity bound as an optional projection warning | RA09-REQ-004/006/016; RA09-VAL-003; SAD-04 §6.1/§9; SAD04-I01-NUM-001 | TCND-I01-05, 10 |
| OR-I01-SYN-005 | Valid numeric lexeme within all accepted bounds would lose precision through the selected numeric projection | Exact source bytes and numeric lexeme/location remain available. Preserve an exact projected value where supported; otherwise expose the affected projection limitation with a retained lexeme reference. Never present a rounded/coerced number as source or report a token-length violation for an in-bound token | That a lossy binary-float conversion is an acceptable source value, or that projection limitations erase the original | RA09-REQ-004/006; RA09-VAL-003; RA09 §3.3; SAD-04 §6.1 | TCND-I01-05, 06 |

For the token-length variants, use an unquoted JSON number consisting of `1`
followed by 126, 127, or 128 zeros in the same otherwise capturable input. These
are 127-, 128-, and 129-character numeric tokens, not JSON strings. Keep raw size,
container depth, item counts and other limits below their bounds. Separate
precision probes, such as `9007199254740993` and `0.1000000000000000000001`,
exercise exact source/lexeme retention without crossing the token-length bound.
The prepared inputs and their checks are recorded under
[numeric-token limits](i01-w02c-numeric-fixtures.md) and
[numbers and text](i01-w02c-numeric-retention-fixtures.md).

### 5.2 Source fidelity, presence, and mapping

| Oracle ID | Controlled condition | Independent expected observation | Must not be inferred | Primary trace | I-01 condition |
| --- | --- | --- | --- | --- | --- |
| OR-I01-FID-001 | Same logical field exercised as absent, explicit null, empty, whitespace-only, intended value, and wrong type | Preserve distinct presence observations: `ABSENT`, `NULL`, `EMPTY`, `WHITESPACE_ONLY`, `VALUE`, `TYPE_MISMATCH` according to the accepted precedence | That null/empty/whitespace/type mismatch are equivalent or can be default-filled | RA09-REQ-006/007; RA09-VAL-006; SAD-04 §6.1 | TCND-I01-06 |
| OR-I01-FID-002 | Narrative versus structured steps; repeated/ordered cases and steps | Preserve original representation, sequence, supplied numbering/content, and nested expectations where present | Invented executable steps or reordered semantic precedence | RA09-REQ-006/007; RA09-VAL-006; RA03-REQ-006/022 | TCND-I01-01, 06 |
| OR-I01-FID-003 | Text identifiers with leading zeros, case differences, whitespace, or Unicode distinctions | Preserve supplied values without trimming, case-folding, type conversion, or Unicode normalization | Semantic equality created by normalization | RA09-REQ-006; RA09-VAL-003/006 | TCND-I01-01, 06 |
| OR-I01-FID-004 | Unknown/mistyped assessment-relevant content | Retain raw located value/subtree or trustworthy opaque boundary with visible mapping/limitation state | Schema conformance obtained by dropping the offending data | RA09-REQ-006/012; RA09-VAL-003; RA03-REQ-025 | TCND-I01-06 |
| OR-I01-FID-005 | Original captured native source survives persistence/restart | Retained bytes remain byte-for-byte identical; recorded byte length/digest and package/source linkage agree | Source authenticity, authorship, semantic truth, or permission | RA03-REQ-003/006; RA09-REQ-005/014; SAD-04 §7.1 | TCND-I01-01 |
| OR-I01-FID-006 | Addressable JSON item | Source reference resolves through artifact identity plus JSON Pointer into that exact retained source instance; projection locator remains distinguishable | Need to expose an absolute workstation path | RA03-REQ-020/030; RA09-REQ-005; RA09-VAL-005; RA09 §4.1 | TCND-I01-01, 14 |
| OR-I01-FID-007 | Same external `source_id` appears on multiple independent items | Items receive/remain distinct internal identities; duplicated source key remains visible | Record merge, identity repair, or guessed referential target | RA09-REQ-009; RA09-VAL-005/008; RA03-REQ-014/037 | TCND-I01-06 |
| OR-I01-FID-008 | Unknown member or source content looks like a path, URL, `$ref`, issue key, or external document reference | Preserve as inert supplied data where allowed; do not retrieve external content, resolve remote schema, or treat reference as substantive supplied evidence | Permission to access external content | RA03-REQ-005; RA09-REQ-003/005/023; RA09-VAL-002/013 | TCND-I01-08 |
| OR-I01-FID-009 | Payload contains `package_id`, role, approval, status, qualification, or authority-like fields | Preserve as supplied data where allowed, but do not restore internal identity, grant role, change policy, or create accepted history | Operational authority from payload content | RA09-REQ-024; RA09-VAL-008/015; SAD-04 §6.1 | TCND-I01-08 |
| OR-I01-FID-010 | `tc_sources`/`supporting_sources` claim an unbound source | Preserve the claim and visible unbound/unsupported issue; actual selected inventory remains the explicitly selected operation inventory; no search is performed | Automatic path search or hidden source acquisition | RA03-REQ-005; RA09-REQ-005/012; RA09-VAL-001/005; SAD-04 §6.1 | TCND-I01-08, 16 |

### 5.3 Origin, defaults, and accountability

| Oracle ID | Controlled condition | Independent expected observation | Must not be inferred | Primary trace | I-01 condition |
| --- | --- | --- | --- | --- | --- |
| OR-I01-AUTH-001 | Canonical origin literal is supplied | Preserve original declaration and map only according to the accepted versioned mapping | Eligibility without the separate accountability requirements | RA09-REQ-008; RA09-VAL-007; RA03-REQ-021 | TCND-I01-07 |
| OR-I01-AUTH-002 | Free-text origin phrase not covered by an accepted literal mapping | Preserve original text and mark unresolved/unmapped meaning | Authorship, AI assistance, or human adoption from wording/style/job title | RA09-REQ-008; RA09-VAL-007; RA03-REQ-021 | TCND-I01-07 |
| OR-I01-AUTH-003 | Containing-set default exists and the case field is genuinely absent | Apply the default only within its declared scope | Cross-source or neighboring-case propagation | RA09-REQ-008; RA09-VAL-007 | TCND-I01-07 |
| OR-I01-AUTH-004 | Case field is explicit null, empty, malformed, conflicting, or negative | Do not replace/upgrade it with a containing-set default | Positive eligibility from default completion | RA09-REQ-008; RA09-VAL-007; SAD-04 §6.1 | TCND-I01-07 |
| OR-I01-AUTH-005 | Payload `accountability.accepted=true` or copied role/approval value without attributable applicable human authority | Preserve declaration, but do not establish operational authority or positive accountability solely from the Boolean/text | Human acceptance or role grant | RA09-REQ-008/024; RA09-VAL-007/008; SAD-04 §6.1 | TCND-I01-07, 08 |

### 5.4 Receipt and I-01 status boundary

| Oracle ID | Controlled condition | Independent expected observation | Must not be inferred | Primary trace | I-01 condition |
| --- | --- | --- | --- | --- | --- |
| OR-I01-RCP-001 | Capture transaction commits coherent original, projection, identities, inventory, issues and receipt linkage | `capture_outcome=CAPTURED`; `package_version_ref` is present and inspectable only after durable commit | Minimum admissibility or review success | RA09-REQ-014/015; RA09-VAL-011/012; SAD-04 §6.2/§7.2 | TCND-I01-01, 15 |
| OR-I01-RCP-002 | Safety/contract prerequisite prevents capture | `capture_outcome=REJECTED`; no committed package/version reference; minimum remains `NOT_EVALUATED` | Partial package or review result | RA09-REQ-013/014/015; RA09 §6.1-6.2 | TCND-I01-04, 09, 15 |
| OR-I01-RCP-003 | Capture fails before coherent snapshot commit, but a failure receipt can still be safely retained | Retain `capture_outcome=FAILED`; no committed package/version reference; minimum remains `NOT_EVALUATED`. If the failure receipt cannot be stored, use the distinct `OR-I01-RCP-006` condition | A partially saved package labelled captured; assuming receipt persistence always succeeds | RA09-REQ-014/015; RA09-VAL-011/012; SAD-04 §7.2 | TCND-I01-11, 12, 15 |
| OR-I01-RCP-004 | Any I-01 `CAPTURED` result | `minimum_check=NOT_EVALUATED` with the explicit I-01 reason; inspection says substantive review not performed | `MET`, `NOT_MET`, qualification, review-run outcome, result availability, findings, approval | RA03-REQ-032/050; RA09-REQ-013/015/017; SAD-04 §6.2 | TCND-I01-15 |
| OR-I01-RCP-005 | Receipt contains issues | Each retained issue exposes stable machine meaning plus stage/boundary/location/evidence/consequence/action to the degree permitted; raw protected payload/full path is not required in diagnostics | Severity or control behavior inferred only from localized prose | RA09-REQ-015/023; RA09-VAL-013; RA03-REQ-038/030 | TCND-I01-14, 15 |
| OR-I01-RCP-006 | Capture fails before its transaction commits and an operational storage failure also prevents saving the FAILED receipt | No new committed package or final receipt; prior committed history remains unchanged. Emit a safe persistence diagnostic to stderr with exit 4, explicitly disclosing that the failure receipt was not durably recorded. Later inspection/reconciliation reports only actually stored evidence, including a prior intent if one exists | A durable FAILED receipt inferred from terminal text; fabricated history or CAPTURED/package success | RA09-REQ-014/015/016; RA09-VAL-012/013; SAD-04 §7.2/§8 | TCND-I01-11, 12, 14, 15 |

### 5.5 Operation identity, retry, lineage, and durable effects

| Oracle ID | Controlled condition | Independent expected observation | Must not be inferred | Primary trace | I-01 condition |
| --- | --- | --- | --- | --- | --- |
| OR-I01-ID-001 | Explicit authorized import retry after acknowledgement loss; exact selected bytes/input identity/action/actor/predecessor/configuration establish the same request fingerprint for the same `operation_id` | Return the same committed receipt/package version after the fingerprint comparison; no duplicate committed effect | Assuming identical intent from operation ID/path alone or creating a new package because the CLI call was repeated | RA09-REQ-014; RA09-VAL-012; SAD-04 §5.1/§7.2 | TCND-I01-02, 11 |
| OR-I01-ID-002 | Same `operation_id` reused with changed request fingerprint, including a file edited after commit/acknowledgement loss | Visible conflict; CLI exit 5; existing committed operation/receipt/version remains unchanged | Returning the old receipt as a successful identical import retry, silent overwrite, merge, or last-write-wins | RA09-REQ-014; RA09-VAL-012; SAD-04 §5.1/§7.2/§8 | TCND-I01-02 |
| OR-I01-ID-003 | New operation submits byte-identical source without deliberate selection of an existing version | Create a separately attributable package version; without predecessor selection it starts a new lineage | Fingerprint-based merge or semantic equivalence | RA03-REQ-048; RA09-REQ-009/014; RA03-VAL-023; SAD-04 §7.2 | TCND-I01-02 |
| OR-I01-ID-004 | New capture explicitly selects one valid predecessor | Create one new immutable child version linked to that predecessor; parent bytes/receipts/history stay unchanged | That the child fixed earlier findings or supersedes parent for every purpose | RA03-REQ-043/044/047; RA03-VAL-020/022; SAD-04 §7.2 | TCND-I01-03 |
| OR-I01-ID-005 | Invalid predecessor reference | Reject/conflict before capture commit; no child package version is committed | Predecessor inferred from name/hash/title/content similarity | RA03-REQ-047; RA03-VAL-022; SAD-04 §7.2 | TCND-I01-03 |
| OR-I01-ID-006 | Cancellation/crash before capture transaction commit | No captured package/version exists; where safely recordable, retain/reconcile a failed attempt with cause | Partially committed package or automatic hidden recapture | RA09-REQ-014; RA09-VAL-012; SAD-04 §7.2 | TCND-I01-11 |
| OR-I01-ID-007 | Commit succeeds but acknowledgement/output is lost; authorized `tdg receipt OPERATION_ID` inspection or stored-operation reconciliation follows | Read the durable committed result without rereading the external source or rerunning capture; retain the same receipt/package version even if the external file later changes or disappears | Applying this source-free inspection rule to a new import invocation and bypassing its fingerprint comparison | RA09-REQ-014; RA09-VAL-012; SAD-04 §7.2/§8 | TCND-I01-02, 11 |
| OR-I01-ID-008 | Content digest/hash of two sources is equal | Equality supports integrity/comparison only; identity, lineage, authority and semantic equivalence remain separate | Automatic package/item merge | RA03-REQ-028/048; RA09-REQ-009; SAD-04 §5.1/§7.1 | TCND-I01-01, 02 |
| OR-I01-ID-009 | Source changes or path redirection is detected during bounded acquisition | Fail the affected capture rather than combine multiple reads/content instances; retained snapshot, if any, proves only the bytes actually captured | Atomic authenticity of an external business document | RA03-REQ-005/006; RA09-REQ-005/014; SAD-04 §7.1 | TCND-I01-16 |
| OR-I01-ID-010 | After commit/acknowledgement loss, the selected source is removed or unreadable and the operator repeats import with that path and the same operation ID | Report the input-acquisition failure; no invented fingerprint or claim of a verified identical retry, no new capture, and no overwrite of the committed result. Authorized receipt inspection remains based on stored evidence under `OR-I01-ID-007` | Substituting previously stored bytes for the unreadable newly selected input or silently changing import into receipt inspection | RA09-REQ-014; RA09-VAL-012; SAD-04 §7.2/§8 | TCND-I01-02, 11, 16 |

## 6. First coverage view against accepted I-01 conditions

The initial W02-A analysis focused on RA-09/RA-03 input, receipt and identity
behavior. It left admission, other resource limits, storage faults, concurrency
and dedicated diagnostic cases for W02-B. The [original extraction table](https://github.com/MarcinMikula/test-design-gatekeeper/blob/27f30a5fc38e41df48475bee8d7802719a44e2c8/docs/implementation/i01-w02-test-design.md#6-first-coverage-view-against-accepted-i-01-conditions)
retains that preparation history.

The current [condition-to-case mapping](i01-w02-test-inventory.md#5-bidirectional-condition-trace)
is maintained in the W02-B inventory. It covers all 16 accepted I-01 conditions,
including the later RA-05/RA-08 routes. These are design links, not executed or
passing results.

## 7. Candidate fixture families for W02-B

The W02-A extraction proposed the following groups of test data for W02-B.
The concrete cases are in the accepted W02-B inventory; Section 11 links the
prepared W02-C files and their checks.

| Family | Purpose | Principal oracle groups |
| --- | --- | --- |
| `native-envelope` | Exact valid envelope and root-member partitions | `OR-I01-ENV-*` |
| `native-syntax` | Duplicate members, BOM, UTF-8, JSON syntax, non-finite/numeric limits | `OR-I01-SYN-*` |
| `native-presence` | Absent/null/empty/whitespace/value/type mismatch | `OR-I01-FID-001`, `OR-I01-FID-004` |
| `native-order-and-fidelity` | Byte retention, order, narrative/structured forms, identifiers | `OR-I01-FID-002/003/005/006/007` |
| `native-untrusted-controls` | URLs, paths, refs, imported IDs/roles/approvals/status | `OR-I01-FID-008/009/010` |
| `origin-accountability` | Canonical origin, free text, defaults, explicit negative/unknown values | `OR-I01-AUTH-*` |
| `receipt-boundary` | CAPTURED/REJECTED/FAILED and minimum/review separation | `OR-I01-RCP-*` |
| `operation-retry` | Fingerprint-checked import retry, changed/unreadable input, stored-result inspection after lost acknowledgement | `OR-I01-ID-001/002/007/010` |
| `lineage` | New operation, identical bytes, predecessor child, invalid predecessor | `OR-I01-ID-003/004/005/008` |
| `source-acquisition` | Source change/redirection and single-content-instance boundary | `OR-I01-ID-009` |

Fixture families must remain synthetic/public laboratory material.

## 8. Test-skeleton rules for W02-C

Each W02-C skeleton should record at least:

- test ID;
- fixture ID or generated mutation;
- oracle ID(s);
- `TCND-I01-*` condition(s);
- requirement/VAL/design trace;
- test level;
- controlled preconditions;
- exact expected observable;
- evidence to retain;
- explicit non-claim;
- whether the test is expected to be RED, GREEN, skipped/not implemented, or
  unavailable at the current work-item boundary.

A future parser test that is intentionally RED because W03 is not implemented is
not a W02 failure. The test must distinguish "behavior not implemented yet" from
a contradiction in the accepted oracle.

## 9. W02-A observations

### 9.1 No blocking source-authority conflict found

The original analysis used the accepted RA-09 and RA-03 baselines, SAD-04's
I-01 contracts and the W01 authorization. Section 3 now links their maintained
text and decision records. The separate numeric-limit classification was later
accepted by the Owner; it is recorded in Section 9.5.

### 9.2 Do not over-specify issue codes yet

RA-09 Section 6.2 gives stable code-family examples, while SAD-04 names some
I-01-specific issue/reason concepts. The executable code catalogue is still an
implementation artifact.

W02 tests should assert a specific code only where the accepted design already
makes that code/reason part of the observable contract. Otherwise they should
assert the required category/stage/effect information without inventing a final
runtime code name.

### 9.3 Identifier encoding is not the primary oracle

Identity distinction, stability, lineage, and attribution are contract
requirements. Tests should not overfit to a display encoding unless the accepted
design fixes it for I-01.

### 9.4 First inventory-based reassessment

SAD-04 requires re-estimation during W02 using the **detailed test inventory**.

The initial W02-A matrix was insufficient for a revised forecast. The
[W02-B inventory](i01-w02-test-inventory.md#7-effort-reassessment) now provides the
first case-based testing forecast and its assumptions. It is a provisional
planning estimate, not measured effort, an approved ceiling or a full I-01 total.

### 9.5 Numeric-token limit: accepted outcome mapping

The review found a missing outcome classification for exceeding the existing
128-character bound. On 2026-10-03 the Owner accepted `REJECTED`, CLI exit `2`,
no new package version/reference and minimum `NOT_EVALUATED`. The exact decision
and scope remain in [SAD04-I01-NUM-001](../solution-design/test-design-gatekeeper-sad-04-i01-numeric-token-limit-addendum-v0.1.md).

The full rule is incorporated in [SAD-04 Section 6.1](../solution-design/test-design-gatekeeper-sad-04-integrated-review-increment-plan-v0.2.md#61-native-input-and-mechanical-projection).
`OR-I01-SYN-004` specifies the 127/128/129-character boundary observations;
`OR-I01-SYN-005` separately covers exact representation within the bound. Other
safety, resource and persistence failures keep their cause-specific handling.

## 10. W02-B inventory and review

The [W02-B inventory](i01-w02-test-inventory.md) turns this oracle basis and the
remaining RA-05/RA-08/SAD-04 conditions into concrete cases. On 2026-10-07 the
Owner accepted Section 8 and the whole inventory as the basis for W02-C: 72 case
rows and 208 listed variants. The [acceptance record](../reviews/test-design-gatekeeper-i01-w02b-review-progress-v0.7.md)
preserves that decision and the earlier section/group decisions.

The inventory defines each stimulus, expected observation, condition/oracle link,
test level, evidence and fault point. Keep these distinctions when preparing or
reviewing tests: import retry versus stored-receipt inspection, numeric capacity
versus precision retention, and a failed capture with a stored receipt versus a
failure that prevents receipt storage.

The inventory's Section 6 lists the remaining work needed to connect tests to
specific implementation entry points and fault controls. Section 7's forecast
remains provisional; the future corpus-reuse idea remains parked. Inventory
acceptance did not close W02, authorize W03 or accept I-01.

<a id="11-current-handoff-state"></a>

## 11. What is ready and what remains to do

The following records describe the prepared test data and retain their dated
checks. Exact inputs and assertions belong with the tests and fixture manifests.

| Record | Inputs prepared and purpose |
| --- | --- |
| [Numeric-token limits — 2026-10-08](i01-w02c-numeric-fixtures.md) | BASE-01 and TC-I01-018.01–.03; numbers around the accepted token-length limit |
| [Document envelope](i01-w02c-envelope-fixtures.md) | 19 TC-I01-011–015 variants covering fields, types and versions |
| [JSON syntax and encoding](i01-w02c-syntax-fixtures.md) | Ten TC-I01-016–017 variants and two valid comparison files; the record also preserves the initial data-generator failure and its correction |
| [Numbers and text](i01-w02c-numeric-retention-fixtures.md) | Four TC-I01-019–020 variants, reusing existing comparison files; this completes the input data and test placeholders for group B |
| [Title presence and type](i01-w02c-title-presence-fixtures.md) | Seven TC-I01-021 variants, including an absent field, explicit null and an empty array of the wrong type |
| [Step representation](i01-w02c-step-representation-fixtures.md) | Three TC-I01-022 variants: narrative, structured steps and repeated numbered steps |
| [Repeated source identifiers](i01-w02c-source-id-collision-fixtures.md) | Two TC-I01-023 variants that keep separate TC or basis records with identical content and expose ambiguous references |
| [Preserving source identifiers](i01-w02c-source-id-fidelity-fixtures.md) | Four TC-I01-024 pairs that differ in leading zeros, case, surrounding whitespace or Unicode code points |
| [Incomplete and unfamiliar content](i01-w02c-deficient-content-fixtures.md) | Three TC-I01-025 variants: unknown nested content, a TC object instead of an array, and a title-only TC |
| [Declared test-case origin](i01-w02c-origin-literal-fixtures.md) | Five TC-I01-026 variants: each recognized origin value, preserved and mapped without inventing human responsibility or deciding eligibility for review |
| [Unrecognized origin declarations](i01-w02c-origin-unmapped-fixtures.md) | Two TC-I01-027 variants: a job-title phrase and lowercase human_authored without an agreed alias; preserve the text and leave its meaning unresolved |
| [Defaults for missing declarations](i01-w02c-case-defaults-fixtures.md) | Two TC-I01-028 variants: defaults for absent origin or accountability, with explicit per-case declarations preserved and each effective value traced to its source |
| [Explicit declarations and defaults](i01-w02c-default-preservation-fixtures.md) | Six TC-I01-029 variants: preserve null, empty, unknown, mistyped, free-text and negative declarations without replacing them with positive defaults |
| [Claims of role and responsibility](i01-w02c-payload-authority-fixtures.md) | One TC-I01-030 input: retain a role, actor and accepted=true declaration without granting authority or inventing human adoption or review |
| [Links and instructions as data](i01-w02c-inert-content-fixtures.md) | Five TC-I01-031 variants: retain a URL, file path, schema reference, issue key and command text without retrieving content or executing instructions |
| [Imported identity and status claims](i01-w02c-imported-claims-fixtures.md) | Five TC-I01-032 variants: retain supplied package ID, role, approval, status and qualification without restoring trusted identity, history or authority |

These checks verify the input files and setup. Product tests still need to be
connected to TDG and exercise the required observations, including preserved
values, item identities, source locations and stored links. Prepared data alone
do not establish correct importer behavior or complete defect coverage.

Further preparation is paused, including TC-I01-033. [README.md](../../README.md)
records the current status and the need to review the delivery sequence after
cleanup. Any resumed work must follow the resulting Owner decision. The remaining
W02 deliverables, review corrections and completion review are still required;
this document does not restart them.
