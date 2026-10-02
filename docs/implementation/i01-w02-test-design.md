# Test Design Gatekeeper

## I-01 / W02 - Test Design, Oracle Basis, and Traceable Test Inventory

| Field | Working state |
| --- | --- |
| Document date | 2026-10-02 (Europe/Warsaw) |
| Increment | I-01 - bounded native-JSON capture and durable inspection |
| Work item | I01-W02 |
| Status | WORKING DRAFT - W02-A TEST-BASIS EXTRACTION |
| Entry authority | I01-W01 closed; GO granted to I01-W02 in `docs/implementation/i01-w01-closure.md` |
| Current activity | Extract accepted observable behavior before fixture/test implementation |
| Product implementation in this document | NONE |
| Fixture corpus in this revision | NOT YET MATERIALIZED |
| Executable tests in this revision | NOT YET IMPLEMENTED |
| I-01 acceptance | NOT CLAIMED |
| W02 closure | NOT CLAIMED |
| Source-inspection pin | Repository `main` as inspected after commit `e15438973564cc790237cce7e9f1bba5e14f4846` |

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

This revision does not create product behavior, execute tests, or mark any
requirement or TCND condition as passed.

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

For W02, SAD-04 Sections 6, 7 and 12 are the effective design/test anchors for:

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

No unresolved authority conflict was found in the source set used for the
W02-A matrix below.

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
| OR-I01-SYN-004 | Numeric token/value cannot be retained within supported exact representation or configured token bound | Produce an explicit representation/limit rejection or limitation; never present a rounded/coerced value as the source | Binary-float rounded source value | RA09-REQ-004/006/016; RA09-VAL-003; SAD-04 §6.1/§9 | TCND-I01-05, 10 |

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
| OR-I01-RCP-003 | Capture is attempted but fails before coherent durable snapshot | `capture_outcome=FAILED`; no committed package/version reference; minimum remains `NOT_EVALUATED` | A partially saved package labelled captured | RA09-REQ-014/015; RA09-VAL-011/012 | TCND-I01-11, 12, 15 |
| OR-I01-RCP-004 | Any I-01 `CAPTURED` result | `minimum_check=NOT_EVALUATED` with the explicit I-01 reason; inspection says substantive review not performed | `MET`, `NOT_MET`, qualification, review-run outcome, result availability, findings, approval | RA03-REQ-032/050; RA09-REQ-013/015/017; SAD-04 §6.2 | TCND-I01-15 |
| OR-I01-RCP-005 | Receipt contains issues | Each retained issue exposes stable machine meaning plus stage/boundary/location/evidence/consequence/action to the degree permitted; raw protected payload/full path is not required in diagnostics | Severity or control behavior inferred only from localized prose | RA09-REQ-015/023; RA09-VAL-013; RA03-REQ-038/030 | TCND-I01-14, 15 |

### 5.5 Operation identity, retry, lineage, and durable effects

| Oracle ID | Controlled condition | Independent expected observation | Must not be inferred | Primary trace | I-01 condition |
| --- | --- | --- | --- | --- | --- |
| OR-I01-ID-001 | Same authorized `operation_id`, same exact selected bytes/input identity/action/actor/predecessor/configuration after acknowledgement loss | Reconcile the committed operation and return the same receipt/package version; no duplicate committed effect | New package because the CLI call was repeated | RA09-REQ-014; RA09-VAL-012; SAD-02 §7.3; SAD-04 §7.2 | TCND-I01-02, 11 |
| OR-I01-ID-002 | Same `operation_id` reused with changed request fingerprint | Visible conflict; existing committed operation/version remains unchanged | Silent overwrite, merge, or last-write-wins | RA09-REQ-014; RA09-VAL-012; SAD-02 §7.3; SAD-04 §7.2 | TCND-I01-02 |
| OR-I01-ID-003 | New operation submits byte-identical source without deliberate selection of an existing version | Create a separately attributable package version; without predecessor selection it starts a new lineage | Fingerprint-based merge or semantic equivalence | RA03-REQ-048; RA09-REQ-009/014; RA03-VAL-023; SAD-04 §7.2 | TCND-I01-02 |
| OR-I01-ID-004 | New capture explicitly selects one valid predecessor | Create one new immutable child version linked to that predecessor; parent bytes/receipts/history stay unchanged | That the child fixed earlier findings or supersedes parent for every purpose | RA03-REQ-043/044/047; RA03-VAL-020/022; SAD-04 §7.2 | TCND-I01-03 |
| OR-I01-ID-005 | Invalid predecessor reference | Reject/conflict before capture commit; no child package version is committed | Predecessor inferred from name/hash/title/content similarity | RA03-REQ-047; RA03-VAL-022; SAD-04 §7.2 | TCND-I01-03 |
| OR-I01-ID-006 | Cancellation/crash before capture transaction commit | No captured package/version exists; where safely recordable, retain/reconcile a failed attempt with cause | Partially committed package or automatic hidden recapture | RA09-REQ-014; RA09-VAL-012; SAD-04 §7.2 | TCND-I01-11 |
| OR-I01-ID-007 | Commit succeeds but acknowledgement/output is lost | Durable committed operation/version remains authoritative; retry reconciles it rather than rereading/reimporting source | A second package/version caused by response loss | RA09-REQ-014; RA09-VAL-012; SAD-04 §7.2 | TCND-I01-02, 11 |
| OR-I01-ID-008 | Content digest/hash of two sources is equal | Equality supports integrity/comparison only; identity, lineage, authority and semantic equivalence remain separate | Automatic package/item merge | RA03-REQ-028/048; RA09-REQ-009; SAD-02 §6.1 | TCND-I01-01, 02 |
| OR-I01-ID-009 | Source changes or path redirection is detected during bounded acquisition | Fail the affected capture rather than combine multiple reads/content instances; retained snapshot, if any, proves only the bytes actually captured | Atomic authenticity of an external business document | RA03-REQ-005/006; RA09-REQ-005/014; SAD-04 §7.1 | TCND-I01-16 |

## 6. First coverage view against accepted I-01 conditions

This is a design trace only. It does not mark any condition executed or passed.

| I-01 condition | W02-A status after this extraction |
| --- | --- |
| TCND-I01-01 | Oracle basis identified: byte fidelity, digest limits, order, locators, package/receipt linkage |
| TCND-I01-02 | Oracle basis identified: retry identity, fingerprint conflict, independent identical-byte submission |
| TCND-I01-03 | Oracle basis identified: predecessor/child/immutability/invalid predecessor |
| TCND-I01-04 | Oracle basis identified: exact envelope classes and empty-content distinction |
| TCND-I01-05 | Oracle basis identified: duplicate names, BOM, UTF-8/syntax/non-finite/numeric-loss handling |
| TCND-I01-06 | Oracle basis identified: presence states, wrong type, unknown fields, representation/order/source-ID preservation |
| TCND-I01-07 | Oracle basis identified: literal origin, free text, defaults, absent/null/negative accountability |
| TCND-I01-08 | Oracle basis identified: imported authority-like data, refs/URLs/paths, unbound source claims |
| TCND-I01-09 | Not yet decomposed in W02-A; requires RA-08/SAD-04 admission-focused extraction |
| TCND-I01-10 | Only representation/limit principle identified here; exact below/at/above policy inventory remains for RA-08/SAD-04 limit extraction |
| TCND-I01-11 | Oracle basis identified for pre-commit and post-commit/pre-ack crash/cancel semantics; detailed fault points remain W02-B |
| TCND-I01-12 | Not yet decomposed in W02-A; persistence/storage/history fault inventory remains for W02-B using RA-05/SAD-04 |
| TCND-I01-13 | Not yet decomposed in W02-A; writer/mutex/read-only boundary remains for W02-B |
| TCND-I01-14 | Partial basis identified for inert supplied content and diagnostic/path minimization; dedicated RA-08 diagnostic cases remain |
| TCND-I01-15 | Oracle basis identified: minimum `NOT_EVALUATED`, review not performed, no fabricated run/findings/availability |
| TCND-I01-16 | Oracle basis identified: explicit source selection, no external retrieval, no mixed content instance |

The unexpanded conditions above are not missing requirements. They mark the
intentional boundary of this first W02-A extraction, which focused on RA-09,
RA-03, SAD-02 and SAD-04 receipt/identity behavior.

## 7. Candidate fixture families for W02-B

No fixture files are created by this revision. The following families are the
minimum next design step suggested by the matrix.

| Family | Purpose | Principal oracle groups |
| --- | --- | --- |
| `native-envelope` | Exact valid envelope and root-member partitions | `OR-I01-ENV-*` |
| `native-syntax` | Duplicate members, BOM, UTF-8, JSON syntax, non-finite/numeric limits | `OR-I01-SYN-*` |
| `native-presence` | Absent/null/empty/whitespace/value/type mismatch | `OR-I01-FID-001`, `OR-I01-FID-004` |
| `native-order-and-fidelity` | Byte retention, order, narrative/structured forms, identifiers | `OR-I01-FID-002/003/005/006/007` |
| `native-untrusted-controls` | URLs, paths, refs, imported IDs/roles/approvals/status | `OR-I01-FID-008/009/010` |
| `origin-accountability` | Canonical origin, free text, defaults, explicit negative/unknown values | `OR-I01-AUTH-*` |
| `receipt-boundary` | CAPTURED/REJECTED/FAILED and minimum/review separation | `OR-I01-RCP-*` |
| `operation-retry` | Same-operation retry, changed fingerprint, lost acknowledgement | `OR-I01-ID-001/002/007` |
| `lineage` | New operation, identical bytes, predecessor child, invalid predecessor | `OR-I01-ID-003/004/005/008` |
| `source-acquisition` | Source change/redirection and single-content-instance boundary | `OR-I01-ID-009` |

Fixture families must remain synthetic/public laboratory material.

## 8. Test-skeleton rules for W02-C

Executable skeletons are not yet created. When W02-C begins, each skeleton should
record at least:

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
test design.

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

### 9.4 Re-estimation is not ready yet

SAD-04 requires re-estimation during W02 using the **detailed test inventory**.

This W02-A matrix establishes the oracle basis but does not yet contain enough
fixture/test rows or fault-injection detail to replace the original estimate.
Re-estimation should therefore wait until W02-B has decomposed all 16 TCND
conditions into concrete cases.

## 10. Next controlled step - W02-B

W02-B should convert the accepted oracle basis into a concrete inventory.

For each case, record:

```text
case ID
fixture family
input mutation / state setup
oracle ID
expected intake/identity/receipt observation
TCND-I01 trace
REQ/VAL/design trace
planned test level
required fault injection, if any
evidence to retain
explicit non-claim
```

The next extraction should also complete the conditions only partially covered
here:

- TCND-I01-09 - admission/public/synthetic versus denied classifications;
- TCND-I01-10 - all accepted size/count/depth/time/memory boundaries;
- TCND-I01-12 - contention/storage/read-only/schema/history-write failures;
- TCND-I01-13 - second-writer and read-command database boundaries;
- TCND-I01-14 - complete safe-diagnostic and inert-rendering cases.

Those rows require focused use of RA-08, RA-05, and SAD-04 Sections 7-9 in
addition to the sources already inspected.

## 11. Current handoff state

W02-A establishes a first independent oracle matrix before product capture
implementation.

It does **not** establish:

- that the oracle set is yet complete for all 16 I-01 conditions;
- that fixtures exist;
- that test code exists;
- that W03 may start merely because this draft exists;
- that any I-01 condition has passed;
- that W02 is complete;
- that I-01 is accepted.

The next review question is whether the W02-A source interpretation, oracle
boundaries, and proposed W02-B decomposition are correct before fixture
materialization begins.
