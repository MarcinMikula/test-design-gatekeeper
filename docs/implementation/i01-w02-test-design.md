# Test Design Gatekeeper

## I-01 / W02 - Test Design, Oracle Basis, and Traceable Test Inventory

| Field | Working state |
| --- | --- |
| Document date | 2026-10-02 (Europe/Warsaw) |
| Review clarification date | 2026-10-03 (Europe/Warsaw) |
| Increment | I-01 - bounded native-JSON capture and durable inspection |
| Work item | I01-W02 |
| Status | WORKING DRAFT - W02-A ORACLE BASIS; W02-B INVENTORY ACCEPTED; W02-C IN PROGRESS |
| Entry authority | I01-W01 closed; GO granted to I01-W02 in `docs/implementation/i01-w01-closure.md` |
| Current activity | W02-C: eight fixture families prepared; latest is [source-ID fidelity](i01-w02c-source-id-fidelity-fixtures.md); forecast remains provisional; W02 open |
| Product implementation in this document | NONE |
| Fixture corpus progress | BASE-01 plus 52 variants across TC-I01-011–024 (group B and four group-C cases) and two valid controls materialized; remaining families pending |
| Executable test progress | 153 fixture checks passed; 108 product skeletons skipped/unbound; no capture execution evidence |
| I-01 acceptance | NOT CLAIMED |
| W02 closure | NOT CLAIMED |
| Source-inspection pin | Repository `main` as inspected after commit `e15438973564cc790237cce7e9f1bba5e14f4846` |
| Clarification source pin | Repository `main` at `d9a6b15513f94f710cd96853f46552c1499e0f79`; governing RA-09 and SAD-04 sources unchanged |
| Numeric-limit decision | Owner accepted `REJECTED` / exit `2` on 2026-10-03; [SAD04-I01-NUM-001](../solution-design/test-design-gatekeeper-sad-04-i01-numeric-token-limit-addendum-v0.1.md) |
| W02-B preparation | 2026-10-04, using repository `0dc8d61144e82271839194de1fa7a466bbb4f92b` plus the recorded Owner decision |
| W02-B Owner review | Section 8 and the whole inventory accepted 2026-10-07 as the basis for W02-C; prior section/group decisions retained; Section 7 forecast remains provisional — [acceptance record v0.7](../reviews/test-design-gatekeeper-i01-w02b-review-progress-v0.7.md) |

## 1. Purpose

W02 prepares the test assets that must exist before native capture implementation
continues. The accepted SAD-04 work breakdown defines W02 as:

> Synthetic fixtures, independently specified receipt/identity oracles and
> traceable test skeletons.

This document starts with **W02-A: test-basis extraction**. It records expected
observable behavior from accepted TDG contracts before implementation results are
available.

The sequence is intentionally:

```text
accepted contract
-> independent oracle
-> fixture/test inventory
-> executable test skeleton
-> implementation
-> execution evidence
```

and not:

```text
implementation result
-> expected result copied from observed behavior
```

This oracle basis does not create product behavior or mark any requirement or
TCND condition as passed. Dated W02-C asset checks are recorded separately in the
[numeric-token](i01-w02c-numeric-fixtures.md),
[envelope](i01-w02c-envelope-fixtures.md),
[syntax/encoding](i01-w02c-syntax-fixtures.md),
[numeric/text retention](i01-w02c-numeric-retention-fixtures.md),
[title presence](i01-w02c-title-presence-fixtures.md),
[step representation](i01-w02c-step-representation-fixtures.md) and
[source-ID collisions](i01-w02c-source-id-collision-fixtures.md) and
[source-ID fidelity](i01-w02c-source-id-fidelity-fixtures.md) slices.

## 2. W02 boundary

W02 is limited to test analysis, test design, synthetic test-data design,
independent oracles, traceability, and later executable skeleton preparation.

### In scope

- extract effective native-JSON intake behavior from accepted requirements and
  design;
- identify independent receipt, source-fidelity, identity, retry, and lineage
  oracles;
- identify concrete equivalence classes and failure variants needed for the
  synthetic corpus;
- trace those oracles to accepted REQ/VAL/design sources and
  `TCND-I01-01` through `TCND-I01-16`;
- prepare the later W02-B fixture/oracle inventory;
- prepare the later W02-C materialized fixtures and test skeletons;
- provide evidence for the W02 re-estimation point once the detailed inventory
  exists.

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

W02 uses accepted repository authority, not historical status labels preserved
inside older snapshots.

### 3.1 RA-09

Effective source:

`docs/requirements-analysis/ra-09/test-design-gatekeeper-ra-09-data-representations-import-export-contracts-v0.2.md`

Authority record:

`docs/requirements-analysis/ra-09/test-design-gatekeeper-ra-09-focused-static-review-v0.2.md`

The review record designates RA-09 v0.2 as the final phase baseline, closes
F-001/F-002, and records all 24 requirements and all 16 validation obligations
as accepted.

Therefore the historical "Owner endorsement pending" wording retained in the
RA-09 v0.2 snapshot does not make the root-envelope clarification pending for
W02.

### 3.2 RA-03

Effective source:

`docs/requirements-analysis/ra-10/test-design-gatekeeper-ra-03-review-package-content-provenance-validation-v0.4.md`

Authority records:

- `docs/reviews/test-design-gatekeeper-ra-03-gate-record-v0.2.md`
- `docs/requirements-analysis/ra-10/test-design-gatekeeper-ra-10-focused-static-review-v0.2.md`

All 50 RA-03 requirement statements are accepted. SR-RA10-001 v0.2 establishes
RA-03 v0.4 as the accepted corrected baseline.

The preserved `PROPOSED` cells and pre-endorsement notices inside the historical
RA-03 wording are therefore not the current requirement status.

### 3.3 SAD-02

Source:

`docs/solution-design/test-design-gatekeeper-sad-02-data-identity-contracts-v0.1.md`

SAD-02 remains the accepted source for identity, version, provenance, commit and
retry design except where a later accepted correction/addendum governs.

In particular, historical SAD-02 envelope/status wording must not be used to
override the accepted SAD-04 corrections.

### 3.4 SAD-04

Effective source:

`docs/solution-design/test-design-gatekeeper-sad-04-integrated-review-increment-plan-v0.2.md`

Decision record:

`docs/reviews/test-design-gatekeeper-sad-04-review-record-v0.2.md`

For W02, SAD-04 Sections 6-9 and 12 are the effective design/test anchors for:

- the exact three-member native JSON envelope;
- I-01 status vocabulary;
- minimal physical identity responsibilities;
- commit/retry/lineage effects;
- the 16 accepted I-01 test conditions;
- the rule that expected outcomes are specified before implementation results.

### 3.5 Conflict rule used by this document

If historical wording conflicts with an accepted later correction, this document
uses the accepted later correction and preserves the historical difference.

If source authority does not resolve a material conflict, W02 stops and requests
a human decision instead of choosing the easiest-to-implement interpretation.

No unresolved source-authority conflict was found in the inspected source set.
The 2026-10-03 review identified an under-specified numeric-limit outcome mapping.
The Owner subsequently accepted its classification; Section 9.5 records the
resolution and the governing SAD-04 addendum.

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
These are fixture recipes; files and executable tests are not materialized here.

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
| OR-I01-ID-001 | Explicit authorized import retry after acknowledgement loss; exact selected bytes/input identity/action/actor/predecessor/configuration establish the same request fingerprint for the same `operation_id` | Return the same committed receipt/package version after the fingerprint comparison; no duplicate committed effect | Assuming identical intent from operation ID/path alone or creating a new package because the CLI call was repeated | RA09-REQ-014; RA09-VAL-012; SAD-02 §7.3; SAD-04 §7.2 | TCND-I01-02, 11 |
| OR-I01-ID-002 | Same `operation_id` reused with changed request fingerprint, including a file edited after commit/acknowledgement loss | Visible conflict; CLI exit 5; existing committed operation/receipt/version remains unchanged | Returning the old receipt as a successful identical import retry, silent overwrite, merge, or last-write-wins | RA09-REQ-014; RA09-VAL-012; SAD-02 §7.3; SAD-04 §7.2/§8 | TCND-I01-02 |
| OR-I01-ID-003 | New operation submits byte-identical source without deliberate selection of an existing version | Create a separately attributable package version; without predecessor selection it starts a new lineage | Fingerprint-based merge or semantic equivalence | RA03-REQ-048; RA09-REQ-009/014; RA03-VAL-023; SAD-04 §7.2 | TCND-I01-02 |
| OR-I01-ID-004 | New capture explicitly selects one valid predecessor | Create one new immutable child version linked to that predecessor; parent bytes/receipts/history stay unchanged | That the child fixed earlier findings or supersedes parent for every purpose | RA03-REQ-043/044/047; RA03-VAL-020/022; SAD-04 §7.2 | TCND-I01-03 |
| OR-I01-ID-005 | Invalid predecessor reference | Reject/conflict before capture commit; no child package version is committed | Predecessor inferred from name/hash/title/content similarity | RA03-REQ-047; RA03-VAL-022; SAD-04 §7.2 | TCND-I01-03 |
| OR-I01-ID-006 | Cancellation/crash before capture transaction commit | No captured package/version exists; where safely recordable, retain/reconcile a failed attempt with cause | Partially committed package or automatic hidden recapture | RA09-REQ-014; RA09-VAL-012; SAD-04 §7.2 | TCND-I01-11 |
| OR-I01-ID-007 | Commit succeeds but acknowledgement/output is lost; authorized `tdg receipt OPERATION_ID` inspection or stored-operation reconciliation follows | Read the durable committed result without rereading the external source or rerunning capture; retain the same receipt/package version even if the external file later changes or disappears | Applying this source-free inspection rule to a new import invocation and bypassing its fingerprint comparison | RA09-REQ-014; RA09-VAL-012; SAD-04 §7.2/§8 | TCND-I01-02, 11 |
| OR-I01-ID-008 | Content digest/hash of two sources is equal | Equality supports integrity/comparison only; identity, lineage, authority and semantic equivalence remain separate | Automatic package/item merge | RA03-REQ-028/048; RA09-REQ-009; SAD-02 §6.1 | TCND-I01-01, 02 |
| OR-I01-ID-009 | Source changes or path redirection is detected during bounded acquisition | Fail the affected capture rather than combine multiple reads/content instances; retained snapshot, if any, proves only the bytes actually captured | Atomic authenticity of an external business document | RA03-REQ-005/006; RA09-REQ-005/014; SAD-04 §7.1 | TCND-I01-16 |
| OR-I01-ID-010 | After commit/acknowledgement loss, the selected source is removed or unreadable and the operator repeats import with that path and the same operation ID | Report the input-acquisition failure; no invented fingerprint or claim of a verified identical retry, no new capture, and no overwrite of the committed result. Authorized receipt inspection remains based on stored evidence under `OR-I01-ID-007` | Substituting previously stored bytes for the unreadable newly selected input or silently changing import into receipt inspection | RA09-REQ-014; RA09-VAL-012; SAD-04 §7.2/§8 | TCND-I01-02, 11, 16 |

## 6. First coverage view against accepted I-01 conditions

This is the initial W02-A extraction view, retained with the numeric-limit
resolution. The [W02-B inventory](i01-w02-test-inventory.md) now decomposes all 16
conditions, including the remaining RA-05/RA-08 routes identified below. These
are design traces only; no condition is marked executed or passed.

| I-01 condition | W02-A status after this extraction |
| --- | --- |
| TCND-I01-01 | Oracle basis identified: byte fidelity, digest limits, order, locators, package/receipt linkage |
| TCND-I01-02 | Oracle basis identified: fingerprint-checked import retry versus source-free stored-result inspection, changed/unreadable input, independent identical-byte submission |
| TCND-I01-03 | Oracle basis identified: predecessor/child/immutability/invalid predecessor |
| TCND-I01-04 | Oracle basis identified: exact envelope classes and empty-content distinction |
| TCND-I01-05 | Oracle basis identified: duplicate names, BOM, UTF-8/syntax/non-finite handling, distinct numeric-token capacity and exact-representation cases; §9.5 status mapping accepted |
| TCND-I01-06 | Oracle basis identified: presence states, wrong type, unknown fields, representation/order/source-ID preservation |
| TCND-I01-07 | Oracle basis identified: literal origin, free text, defaults, absent/null/negative accountability |
| TCND-I01-08 | Oracle basis identified: imported authority-like data, refs/URLs/paths, unbound source claims |
| TCND-I01-09 | Not yet decomposed in W02-A; requires RA-08/SAD-04 admission-focused extraction |
| TCND-I01-10 | Numeric-token 127/128/129-character variants identified with the accepted §9.5 outcome mapping; remaining limits are decomposed in the W02-B inventory |
| TCND-I01-11 | Oracle basis identified for pre-commit and post-commit/pre-ack crash/cancel semantics; detailed fault points remain W02-B |
| TCND-I01-12 | Partial basis identified: failed capture with and without safely retained failure receipt; remaining persistence/storage/history faults require W02-B using RA-05/SAD-04 |
| TCND-I01-13 | Not yet decomposed in W02-A; writer/mutex/read-only boundary remains for W02-B |
| TCND-I01-14 | Partial basis identified for inert supplied content and diagnostic/path minimization; dedicated RA-08 diagnostic cases remain |
| TCND-I01-15 | Oracle basis identified: minimum `NOT_EVALUATED`, review not performed, no fabricated run/findings/availability |
| TCND-I01-16 | Oracle basis identified: explicit source selection, no external retrieval, no mixed content instance |

The unexpanded conditions above are not missing requirements. They mark the
intentional boundary of this first W02-A extraction, which focused on RA-09,
RA-03, SAD-02 and SAD-04 receipt/identity behavior.

## 7. Candidate fixture families for W02-B

The W02-A extraction proposed the following families for W02-B. Materialization
progress is now recorded separately in the W02-C slice linked above.

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

The inspected sources contain historical pending/proposed wording, but the later
accepted review/closure records resolve those status differences:

- RA-09 v0.2 is the accepted final RA-09 baseline;
- RA-03 v0.4 is the accepted corrected baseline;
- SAD-04 supplies the accepted I-01 envelope/status corrections and W02 test
  conditions;
- W01 closure grants GO to W02.

No new Owner decision is required merely to use those accepted contracts for
test design. The separate numeric-limit classification identified during review
was explicitly accepted by the Owner and is recorded in Section 9.5.

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

**RESOLVED — Project Owner decision, 2026-10-03.**

The review exposed an absent classification, rather than a dispute about the
128-character bound. The Owner explicitly accepted `REJECTED` and CLI exit `2`
for exceeding that bound, with no new package version/reference and minimum
`NOT_EVALUATED`. The attributable decision, safe-diagnostic rule and scope are
recorded in [SAD04-I01-NUM-001](../solution-design/test-design-gatekeeper-sad-04-i01-numeric-token-limit-addendum-v0.1.md).

This resolves the former decision prerequisite for `OR-I01-SYN-004`. For
otherwise eligible inputs, 127/128-character tokens pass this bound;
129-character tokens are rejected. Exact representation within the bound remains
the separate `OR-I01-SYN-005` concern. Existing safety and persistence failures
retain their cause-specific handling; the numeric decision is not generalized
to all resource failures.

The accepted SAD-04 v0.2 bytes remain frozen. Read that baseline with the addendum.
No product execution, W02 closure or new phase/work-item GO is claimed.

## 10. W02-B inventory and review

The [W02-B inventory](i01-w02-test-inventory.md) converts this oracle basis and
the remaining RA-05/RA-08/SAD-04 conditions into concrete parameterized cases.
The Owner accepted Section 8 and the whole inventory on 2026-10-07 as the basis
for W02-C. The
[acceptance record v0.7](../reviews/test-design-gatekeeper-i01-w02b-review-progress-v0.7.md)
records that decision and preserves the earlier section/group decisions. All 72
case rows / 208 variants are accepted for test design. The Section 7 forecast
remains provisional and must be checked against actual work; the future
corpus-reuse idea remains parked. Fixtures and executable skeletons remain W02-C
work, and W02 is still open.

It covers capture/identity, envelope/syntax, presence/accountability, admission
and inert content, resource/containment boundaries, transactions/recovery,
concurrency/source selection, diagnostics/copies and unavailable capabilities.
Each row carries its stimulus, expected observation, condition/oracle route,
test level, evidence and fault point. The bidirectional condition table reaches
all 16 accepted conditions without claiming execution or full requirement fulfilment.

Review particularly the separation of fingerprint-checked import retry from
source-free receipt inspection, numeric capacity from precision retention, and
capture failure with a stored receipt from failure that cannot retain a receipt.
The inventory retains these concrete variants and exposes its remaining test
harness/configuration bindings and provisional effort forecast.

## 11. Current handoff state

W02-A establishes a first independent oracle matrix before product capture
implementation.

It does **not** establish:

- that the planned cases establish exhaustive coverage or executed evidence;
- that the whole fixture corpus or executable product assertions are ready;
- that W03 may start merely because this draft exists;
- that any I-01 condition has passed;
- that W02 is complete;
- that I-01 is accepted.

W02-C began with BASE-01 and TC-I01-018.01–.03; the
[2026-10-08 slice record](i01-w02c-numeric-fixtures.md) separates passing asset
checks from unbound product skeletons and states the runtime limitation.
The subsequent [envelope slice](i01-w02c-envelope-fixtures.md) adds 19 variants
from TC-I01-011–015, with the same separation of asset and product evidence.
The [syntax/encoding slice](i01-w02c-syntax-fixtures.md) adds ten variants from
TC-I01-016–017 and two valid controls, retaining the initial authoring-guard
failure and its correction separately from product evidence.
The [numeric/text retention slice](i01-w02c-numeric-retention-fixtures.md) adds
four TC-I01-019–020 variants and reuses existing controls. This completes asset
materialization and unbound skeletons for the listed group-B inputs, not product
verification or condition acceptance.
The [title-presence slice](i01-w02c-title-presence-fixtures.md) begins group C
with seven TC-I01-021 variants, including explicit absence, null and empty-array
type mismatch. Asset observations remain separate from the unbound U/I product
assertions and do not invent mapping status or repair a supplied title.
The [step-representation slice](i01-w02c-step-representation-fixtures.md) adds
three TC-I01-022 variants: narrative, ordered structured steps and identical
numbered repetitions. It prepares exact-content/order/location observations
without executing the unbound product assertions or inventing actions.
The [source-ID collision slice](i01-w02c-source-id-collision-fixtures.md) adds
two TC-I01-023 variants with separate identical TC or basis items. Source-position
and candidate-reference observations distinguish duplicated TC keys from an
ambiguous basis reference; actual generated identities and durable links remain
unbound U/I assertions. Equal content does not authorize merging either pair.
The [source-ID fidelity slice](i01-w02c-source-id-fidelity-fixtures.md) adds
four TC-I01-024 pairs distinguishing leading zeros, case, surrounding whitespace
and Unicode code points. Its asset checks do not establish product preservation.
Continue the remaining fixture families and real assertion bindings under the
accepted inventory's Section 6 controls. The whole inventory has recorded Owner
acceptance; the Section 7 forecast remains provisional and subject to
reassessment. No product execution evidence, full I-01 total, budget ceiling or
delivery date is claimed.
W02 remains open pending its remaining deliverables and completion review; this
inventory acceptance does not start W03 or accept I-01.
