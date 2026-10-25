# Test Design Gatekeeper

## SAD-04 — Consolidated Solution Design and I-01 Delivery Boundary

| Field | State |
| --- | --- |
| Basis | Accepted SAD-01/02, corrected SAD-03 v0.3 and SAD-04 v0.2, with the accepted numeric-token clarification |
| Design and implementation decision | SAD-04 and its allocation index accepted on 2026-09-28; both SAD-04 findings closed, B-01 closed for the selected I-01 boundary and GO to I-01 granted in [SR-SAD04-001 v0.2][review04] |
| Current work | Development paused for documentation cleanup; TC-I01-033 remains on hold. [README.md](../../README.md) describes implemented capability and current evidence |
| Text maintenance | Consolidated on 2026-10-25 in the existing SAD-04 file; decision IDs and Section 4–14 contract locations retained |
| Evidence boundary | Accepted design and historical document reviews; the design itself supplies no runtime, model-quality or sealed-readiness evidence |

This is the main description of the accepted solution. It brings the component, data and model boundaries into one place and incorporates the accepted corrections directly. The earlier SAD files and review records preserve the original wording, examples, decisions and checks; their preparation-time pending notices are historical. The original SAD-04 snapshot remains in [Git history][original]. Its recorded hashes identify that snapshot, not this maintained text.

## 1. Purpose and decision convention

TDG is designed as one local application that helps a human review deliberately supplied system-level functional black-box test cases. It preserves the supplied evidence, separates findings from human decisions and keeps unsupported conclusions visible. It can advise on gaps and possible improvements; it cannot approve, directly edit or repair testware, retrieve unsubmitted business material or make project-gate decisions.

The accepted full design and the first delivery increment have different boundaries. Sections 4.1–4.2, 7.4–7.5 and 15 describe responsibilities needed for later review. **I-01 enables only native-JSON capture and inspection**, as specified in Sections 4 and 6–9. CSV, substantive review, model invocation, result export and sealed processing remain outside I-01. A design permission does not establish implementation or successful verification.

The [Requirements Analysis closure][gate] indexes the 249 accepted requirements and 169 validation obligations. Their governing meanings remain authoritative. This consolidation adds no product requirement, implementation permission, model selection or acceptance threshold. A change to required behavior needs an explicit decision; an unresolved choice is not a default.

## 2. Sources and review method

| Governing source or retained record | Purpose |
| --- | --- |
| [Requirements Analysis closure][gate] | Accepted requirements, evaluation duties, capacity and active documentation-growth risk R-08 |
| [RA-03][ra03], [RA-04][ra04], [RA-05][ra05], [RA-06][ra06] | Package content, scope qualification, records, authority and technique semantics |
| [RA-07][ra07], [RA-08][ra08], [RA-09][ra09], [RA-10][ra10] | Model permission, protection, interchange and evaluation contracts |
| [SAD-01 historical source][sad01-history] | Component/flow decisions SAD-D-001–003 and the 2026-09-22 walkthrough |
| [SAD-02 historical source][sad02-history] | Logical data decisions SAD-D-004–008 and the 2026-09-23 walkthrough; its superseded status table and JSON example are not implementation contracts |
| [SAD-03 historical source][sad03-history] and [SR-SAD03-001 v0.2][review03] | SAD-D-009–015, accepted evaluation and failure corrections, closure on 2026-09-27 |
| [SR-SAD04-001 v0.1][verification04] and [v0.2 decision][review04] | Integrated review, correction verification and 2026-09-28 implementation gate |
| [SAD04-I01-NUM-001][numeric] | Numeric-token outcome accepted on 2026-10-03, now included in Section 6.1 |
| [REQ–VAL ledger][trace] and [design allocation index][allocation] | Retained requirements/validation routes and design-work allocation; not executed coverage |

The original integrated review compared the SAD interfaces: input envelope, identity, capture commit, assessment/run status, model permission, protection failure and history. Its findings and checks remain in the existing records. Source examples are versioned development inputs: SAD-01's age range 18–75 and RA-09's 18–120 are different supplied rules, not application defaults.

The allocation index is a historical design snapshot. Its source hashes and older section references identify the inspected versions; it is not a live implementation tracker. The current layout below preserves the accepted responsibilities and points to current requirements without rewriting the historical evidence.

## 3. Integrated review findings and corrections

| Accepted correction | Current rule and recorded disposition |
| --- | --- |
| SR-SAD03-F-001 | Operational review needs current task/configuration qualification. ROLE-08-authorized public/synthetic candidate evaluation uses its own identities and the same gateway controls, without a fictional operational run. Accepted and closed on 2026-09-27; Section 15.1 |
| SR-SAD03-F-002 | Genuine missing business evidence, unsupported capacity before work and failed execution after work begins have different consequences. Keep assessment outcome, run state and availability separate; accepted and closed on 2026-09-27; Section 15.4 |
| SR-SAD04-F-001 — Medium | Substantive ledger outcomes are ASSESSED, UNGRADABLE, NOT_PERFORMED and INCOMPLETE. COMPLETED/BLOCKED are run states; availability is a separate derived axis. Disposition accepted on 2026-09-27, correction verification and closure accepted on 2026-09-28; Section 6.2 |
| SR-SAD04-F-002 — High for I-01 readiness | The native wire envelope contains exactly document_type, contract_version and content, with version "1.0". The old package/submission-root illustration is superseded. Disposition accepted on 2026-09-27, verification and closure accepted on 2026-09-28; Section 6.1 |

The [SAD-03 review][review03] and [SAD-04 verification][verification04] preserve the counterexamples, source comparisons and limits of those checks. They are document evidence from the AI-assisted author/review path, not independent technical assurance or runtime tests. The accepted numeric-token decision is included in Section 6.1; it does not assign outcomes to unrelated resource faults.

## 4. First increment and retained product scope

**I-01: deliberately submit one eligible local JSON file, preserve a coherent immutable snapshot, receive an honest import receipt, and inspect the retained source/projection after restart.** This is the first usable persistence/intake path on which review can later rely.

| Included in I-01 | Completion boundary |
| --- | --- |
| Local laboratory workspace and operator attribution | Only declared public/synthetic development material; logical roles are recorded without claiming verified sealed identity |
| Native review_package_input, version 1.0 | One explicitly selected regular local file, bounded parsing and mechanical capture |
| Source fidelity and projected inventory | Exact source bytes, digest, source locators, generated identities, raw deficient values, unknown content and explicit mappings remain inspectable |
| Immutable versions and deliberate lineage | New operations create new versions; an explicitly selected predecessor links lineage without copying its business content |
| Durable receipt, retry/conflict handling and restart inspection | No package reference before coherent commit; identical identified retry does not duplicate committed effects |
| Safe terminal inspection | Receipt, source inventory and escaped selected fields; no active rendering, external fetch or source TC editing |

I-01 deliberately ends **before the RA-03 core-minimum check**. Its receipt always states minimum_check=NOT_EVALUATED with reason MINIMUM_CHECK_NOT_ENABLED_IN_I01. It may expose observed field presence/mapping issues, but cannot assert MET, NOT_MET, eligibility, technique coverage or a completed review. No ReviewRequest, ReviewRun, substantive LedgerEntry or finding is fabricated for this capture-only path. This is partial delivery, not a waiver of RA03-REQ-031/033 or RA09-REQ-013.

The CLI capability manifest must visibly list unavailable functions. CSV parsing, attachments/extraction, semantic minimum checks, classification, assessment, human finding dispositions, result export, model invocation and sealed processing remain disabled in I-01. JSON claims about additional sources are preserved as unresolved references; the application does not discover or open them. No unsupported source is silently counted as captured.

| Later delivery slice — accepted sequence before the pause | Retained work and enabling condition |
| --- | --- |
| I-02 — Package readiness and review records | Defined CSV/explicit source bindings, core minimums, criterion-level qualification, run/ledger/history and inspection/export; concrete contracts and tests before enabling each path |
| I-03 — Functional test-design review | EP, BVA, decision tables and state transitions in bounded subincrements, with supplied/confirmed premises and human interpretation/disposition; no requirement that all four techniques apply to every TC |
| I-04 — Controlled local model contribution | Authorized synthetic candidate evaluation, task-specific qualification, gateway protections and measured resource/quality evidence; may be planned alongside I-03 but cannot bypass B-06/B-08 prerequisites |
| Later product acceptance / sealed readiness | Full selected MVP evidence and human acceptance; B-09 controls and ROLE-09 authorization separately precede any confidential use |

These are delivery slices within the accepted work packages, not additional SAD documents or promises of fixed dates. GUI and reviewing tests of AI/LLM systems remain parked.

### 4.1 Application responsibilities

The full design uses seven logical components, not seven services. The application core runs in one local process; a controlled parser worker or later inference runtime can be a separate process. Every exposed operation uses trusted actor/profile context and rechecks affected authority before privileged commit or disclosure. Typed laboratory roles provide attribution only.

| Component | Responsibility and owned output | Allowed boundary |
| --- | --- | --- |
| CMP-01 — Application coordinator | Accept identified human operations; apply action/profile policy; invoke capture, review, decision and export services; coordinate run state. | Receives CLI actions and trusted configuration. No command gains scope, qualification or protected-data permission from supplied content. |
| CMP-02 — Intake and capture | Check supported contracts and selected bindings; preserve originals and identified mechanical projections; produce coherent package snapshots and import receipts. | Reads only explicitly selected sources through approved paths. No LLM capture mapping, code execution, URL following or automatic directory search. |
| CMP-03 — Review planner | Account for the original inventory; check minimums, item eligibility, criterion-level qualification and per-dimension prerequisites; prepare the requested-work ledger. | Reads the identified snapshot and applicable decision/configuration context. Semantic assistance goes through CMP-05; no blanket verdict from labels. |
| CMP-04 — Assessment services | Assess requested quality/technique dimensions; preserve models, mappings, premise status and derivation; propose evidence-bearing outcomes and review items. | Deterministic controls receive established structured premises. Semantic model contributions use CMP-05. Neither path repairs source TC or confirms its own business interpretation. |
| CMP-05 — LLM gateway | Check task/envelope permission, construct bounded context, invoke the configured local runtime, validate response structure/references and retain permitted attempt evidence. | Receives only selected package/run evidence. The runtime receives no record-store access, filesystem discovery, arbitrary command, policy-change or network-retrieval capability. |
| CMP-06 — Record and history store | Preserve coherent snapshots, runs, ledger entries, evidence, interpretation/disposition events, operation outcomes and exports; expose controlled reads. | Writes pass through invariant-preserving application operations. Failed writes cannot be reported as success; imported statuses are data rather than trusted history. I-01 storage is specified in Section 7. |
| CMP-07 — Inspection and export | Present authorized selected records; prepare coherent JSON/Markdown export with source limits and a fixed human-history boundary. | Uses retained records and current permission. Presentation adds no semantic findings, executes no supplied content and loads no remote rendering resources. |

CMP-01 coordinates work; only CMP-06 writes the store through invariant-preserving operations. CMP-03/CMP-04 request model assistance through CMP-05. Responses return as data for validation, never as commands or direct writes. CMP-07 reads retained records; it does not ask a model to reconstruct history.

### 4.2 Review flow after capture-only I-01

This is the accepted target review flow. The review steps remain disabled in I-01. Each FLOW identifier retains its SAD-01 meaning.

| Step | Operation and responsible component | Inspectable consequence |
| --- | --- | --- |
| FLOW-01 — Admit | CMP-01 checks the selected operation, actor/role, profile, declared classification, purpose and policy before prohibited processing. | A refused path returns only permitted intake information. No automatic profile switch or external classification call. |
| FLOW-02 — Capture | CMP-02 validates the supported input contract and explicit source bindings, inventories exact sources and applies the identified mechanical mapping. | CMP-06 exposes `CAPTURED` only after a coherent durable snapshot and receipt linkage exist. Rejected/failed capture has no committed package reference. |
| FLOW-03 — Check minimums | CMP-02/CMP-03 apply the RA-03 sequence to the captured candidate, preserving origin, accountability, gaps, provenance and conflicts. | Receipt minimum is `MET`, `NOT_MET` or `NOT_EVALUATED`. An unresolved free-text origin is preserved, not inferred from writing style. |
| FLOW-04 — Request review | CMP-01 records one deliberate request against one immutable package version, with the authorized dimensions and actual behavior context. | A unique `REQUESTED` run exists. Retrying the same identified request does not create another run; a new deliberate request does. |
| FLOW-05 — Plan bounded work | CMP-01 checks start prerequisites and records `RUNNING` before authorized qualification/assessment activity begins. CMP-03 applies RA-04 and accounts for all supplied TC/candidates, exclusions and requested dimensions. | A whole-run impediment can lead from `REQUESTED` or `RUNNING` to `BLOCKED`, as applicable. Each entry retains eligibility, domain, capability and evidence separately. No domain exclusion is invented from a capability failure. |
| FLOW-06 — Establish premises | CMP-03/CMP-04 inspect supported evidence, reuse applicable recorded decisions and expose unresolved interpretations. | Candidate models and mappings remain derived. A qualified LLM may assist; ROLE-04 owns interpretation confirmation. Unsupported dependent claims remain ungradable or unperformed according to their actual cause. |
| FLOW-07 — Assess | CMP-04 applies available qualified controls and, where permitted, CMP-05 assistance within the unchanged requested boundary. | Applicability is separate from conditional coverage, planned exercise from expected-result alignment. Every completed conclusion retains evidence and derivation; new review items start `PENDING`. |
| FLOW-08 — Commit and finalize | CMP-01/CMP-06 commit coherent entry outcomes and related items, then finalize state with an explicit outcome for every requested entry. | Run state and availability derive from actual retained work. No empty model response, successful parser or finding count establishes completion or `AVAILABLE`. |
| FLOW-09 — Human review | CMP-01/CMP-07 expose evidence and record authorized interpretation/disposition operations with their distinct effects. | ROLE-05 disposition is attributable; self-review is visible. ROLE-03 repairs the TC externally. Earlier findings can remain pending while a revised package is submitted. |
| FLOW-10 — Export or revisit | CMP-07 exports a deliberate selection/history cutoff after current permission checks; CMP-01 accepts a separate re-review or explicit comparison request. | Export failure leaves canonical records intact. Re-review has its own run; revised supplied content has a new package version; comparison history cannot silently enrich its basis. |

A captured snapshot can fail the package minimum. A rejected capture creates no fictional package or run. Review qualification accounts for the original inventory and preserves excluded or unassessable items. Applicable technique coverage is conditional on established applicability; an explicitly requested dimension cannot be removed afterwards to improve availability. Independently supported deterministic work may proceed without a model, but it needs established premises and all shared controls.

Safely committed interim results retain availability NOT_FINAL. Unsaved previews are labelled as such and cannot support a finding disposition. At finalization, diagnostics alone supply no substantive assessment and imply availability NONE. Zero findings can coexist with AVAILABLE only when RA-05's requested-work conditions are met. Invalid or ambiguous terminal input grants no human decision; the active operation reports the error and reprompts under its bounded interaction policy.

The [original synthetic walkthrough][sad01-history] retains CUST-01–03, the explicit integer-age rule and its BVA example. It is exposed design material, not a benchmark or runtime result.

## 5. Implementation decisions

### 5.1 Accepted architecture decisions

| ID | Accepted meaning and current boundary |
| --- | --- |
| SAD-D-001 | One local application with distinct logical modules; process/module separation alone is not a security boundary |
| SAD-D-002 | Terminal interface first; all actions use application services. A later GUI must reuse the authority and lifecycle rules |
| SAD-D-003 | One active foreground review run, bounded waiting/cancellation and explicit ledger/finalization. Terminal runs cannot resume; sequential operation still needs stale-write and retry protection |
| SAD-D-004 | Keep captured content, derived review/history and trusted operational context distinguishable; shared physical storage is allowed only with enforceable ownership and write rules |
| SAD-D-005 | TDG identities and immutable package lineage preserve supplied IDs; equal content or hashes cannot merge independent submissions |
| SAD-D-006 | Versioned native JSON, the defined CSV TC adapter and faithful JSON/Markdown export; the exact RA-09 envelope and manifest contract govern |
| SAD-D-007 | Operation identities/fingerprints protect retries; human updates use an expected record version. Changed requests and stale writes cannot silently overwrite history |
| SAD-D-008 | Preserve separate missing, unperformed, ungradable, incomplete, blocked and partial meanings on their governing axes; Section 6.2 contains the corrected vocabulary |
| SAD-D-009 | All operational and candidate-evaluation model calls pass through CMP-05 with purpose-specific permission, context, limits and validation |
| SAD-D-010 | Qualification applies to the exact model/runtime, task, behavior, profile and contract/resource envelope; there is no generic trusted-model flag |
| SAD-D-011 | Build minimal allowlisted context from retained evidence; no arbitrary store read, source discovery or automatic expansion |
| SAD-D-012 | Each attempt has fixed limits, identity and cancellation behavior. Pre-start unsupported work is NOT_PERFORMED; unfinished work after invocation is INCOMPLETE; run state remains separate |
| SAD-D-013 | Model output is data subject to validation; it cannot invoke tools, change scope/policy, write records or repair TC |
| SAD-D-014 | Mandatory admission, identity, storage, egress, audit or policy failure stops every dependent path, including shared-boundary deterministic work; optional diagnostics have a narrower effect |
| SAD-D-015 | Laboratory and sealed profiles have distinct admission, identity, protection and verification evidence; changing a label cannot grant sealed use |

SAD-D-001–003 were accepted on 2026-09-22, SAD-D-004–008 on 2026-09-23, and the corrected SAD-D-009–015 baseline on 2026-09-27. The source records in Section 2 retain the individual acceptance boundaries.

### 5.2 Accepted I-01 implementation choices

| ID | Decision accepted on 2026-09-27 | Reason and scope |
| --- | --- | --- |
| SAD-D-016 — Bound the first implementation permission | Limit implementation permission, when granted through Section 14, to I-01 as defined in Section 4; retain later work in the allocation register. | Starts an end-to-end local path without disguising capture as substantive test review. |
| SAD-D-017 — Python CLI and explicit contract validation | Use CPython 3.13, argparse, sqlite3, uuid and hashlib; use jsonschema's Draft202012Validator for TDG-owned schemas and pytest for verification. Record exact interpreter/SQLite/dependency versions in an environment manifest and lock dependencies during setup. | Builds on the user's Python direction; one supported Windows x64 target first. Minor version 3.13 is selected for TDG, not inferred as installed on the user's machine. A version change needs an explicit compatibility decision. |
| SAD-D-018 — One local transactional store | SQLite, a single application writer, explicit transactions, foreign keys enabled, DELETE rollback journal and synchronous=FULL. Keep original bytes and projections in the same database. | Makes source, snapshot, receipt and capture outcome commit together; avoids a database/filesystem two-phase capture problem. Physical durability still requires verification on the target filesystem. |
| SAD-D-019 — Opaque identities and separate integrity | UUIDv4 text IDs generated by TDG; SHA-256 hex for exact-byte integrity; RFC 6901-style JSON Pointer within the identified original for JSON locators. | Source IDs remain independent; a digest is neither business identity nor evidence of truth/authorship. No content-addressed package deduplication. |
| SAD-D-020 — Strict control, tolerant supplied content | Implement RA-09's version 1.0 envelope; a local schema registry with remote retrieval denied; preserve all content values and deficiencies without coercion. | Rejects malformed control input without discarding capturable incomplete TC. Full schema/profile IDs are separate from package and behavior versions. |
| SAD-D-021 — Laboratory limits and unavailable-path enforcement | Apply Section 9's versioned limits, bounded parser worker, data/copy policy and explicit disabled capabilities. | No LLM endpoint, credentials, browser, renderer or network client is part of the I-01 processing path. Locality alone is not a confidentiality claim. |

SAD-D-016–021 and the detailed I-01 contracts were accepted on 2026-09-27; the complete baseline and implementation gate followed on 2026-09-28. The resource settings are engineering containment limits, not statistical acceptance thresholds or measured hardware performance. Current development remains paused.

## 6. Interchange and status contracts

### 6.1 Native input and mechanical projection

The primary JSON object has exactly these members:

```json
{
  "document_type": "review_package_input",
  "contract_version": "1.0",
  "content": {}
}
```

This example is capturable but substantively deficient; it is not a qualifying TC package. The envelope schema requires an object, all three members, constant document_type/version strings, object-valued content and no additional root properties. It does not impose an editorial completeness schema on content. Runtime validation never downloads a schema, resolves input-supplied $ref values, fills defaults or coerces fields.

| Input condition | I-01 consequence |
| --- | --- |
| Empty content object or missing scope/basis/TC within content | Faithful capture permitted; absent fields visible; minimum NOT_EVALUATED with the I-01 limitation |
| Unknown root member, missing envelope member, wrong kind/version or mistyped content | REJECTED; no package_version_ref |
| Unknown member inside content, explicit null, wrong field type or incomplete TC | Preserve exact raw value/locator and an applicable issue; no invented field value or source correction |
| Duplicate JSON member at any depth; BOM; invalid UTF-8; comments; trailing comma; non-finite token | Reject under RA-09's syntax/profile rules before a lossy accepted projection is constructed |
| Content declares package_id, role, approval, qualification, filesystem path or URL | Preserve as supplied data where allowed; grant no operational identity/authority and perform no retrieval |
| Content claims tc_sources/supporting_sources without supplied bindings | Preserve the claim and UNBOUND_SOURCE/unsupported-capability issue. The actual selected inventory is still the one primary file |

The mechanical mapping follows RA-09 Sections 3.1–4.2: scope; ordered basis_elements and test_cases; case_defaults; source claims; notes/risks/supplementary and unknown content. Preserve narrative and structured steps, ordering and ABSENT/NULL/EMPTY/WHITESPACE_ONLY/VALUE/TYPE_MISMATCH separately from mapping status. Default origin/accountability applies only to genuinely absent fields in the declared set; null, empty, malformed or conflicting values are not upgraded. Literal origin classes can be mapped; free text remains UNMAPPED. Human accountability is not established by a payload Boolean.

Numeric source lexemes are retained without conversion through binary floating point. Raw bytes are authoritative; projections may reference a numeric source location/lexeme rather than manufacture a rounded JSON value. Unsupported representation or configured size limits produce an explicit rejection/limitation, never a changed source number. Ordinary safe display is escaped and bounded; it need not reproduce source bytes visually.

**Numeric-token outcome — SAD04-I01-NUM-001, accepted 2026-10-03.** For otherwise valid input, a numeric token longer than 128 characters detected during the bounded check stops capture before commit: capture outcome REJECTED, CLI exit 2, no new package version/reference and minimum NOT_EVALUATED. The diagnostic identifies the limit and safe affected location without raw numeric payload or unnecessary host path. If a rejection receipt cannot be persisted, expose that separate failure; do not fabricate durable history.

Tokens of 127 or 128 characters pass this length check only and still undergo the other checks. Do not round, truncate or coerce a number to fit. An in-bound exact-representation limitation remains a source-fidelity/projection concern. This decision is specific to numeric-token length; other limits, timeouts, containment and persistence faults retain their own cause/stage outcomes.

The future CSV route is **the already-defined RA-09 native JSON manifest plus explicit tc_sources bindings to tdg-tc-csv version 1**. It is not a new CSV dialect choice. Comma/quote, UTF-8/BOM, logical multiline row, ragged-row, absent/empty and literal Boolean rules remain RA-09 Section 5.1. I-01 does not implement or silently approximate that route.

### 6.2 Status vocabulary and I-01 boundaries

| Axis | Governing values | I-01 use |
| --- | --- | --- |
| Capture receipt | CAPTURED, REJECTED, FAILED | Active; cancellation before commit is FAILED with cancellation cause |
| Core minimum | NOT_EVALUATED, MET, NOT_MET | Always NOT_EVALUATED; the check is not enabled |
| Domain qualification | IN_SCOPE, OUT_OF_SCOPE, UNDETERMINED, NOT_EVALUATED | Not assessed; no manufactured criterion verdict |
| Review run | REQUESTED, RUNNING, COMPLETED, BLOCKED, FAILED, CANCELLED | No review run created by I-01 |
| Substantive assessment outcome | ASSESSED, UNGRADABLE, NOT_PERFORMED, INCOMPLETE | No substantive ledger created by I-01; this is the corrected contract for later work |
| Result availability | NOT_FINAL, NONE, PARTIAL, AVAILABLE | Not calculated without a review run; inspection must say review not performed |
| Finding disposition | RA-05's separate human-event contract | Not implemented and never inferred from intake |

Receipt and snapshot representations retain RA-09 document kinds and envelope version. Receipt content includes operation identity, actor/time and profile/mapping versions, capture outcome, package reference only after commit, actual input inventory, issues and the explicit minimum-check limitation. Issues retain code, stage, affected location/boundary, observed problem, provenance, consequence and bounded human action. No single valid/pass flag replaces these meanings.

## 7. Physical records, identity and failure effects

### 7.1 Minimal store and owned writes

| Physical record group | I-01 content / constraint | Owner |
| --- | --- | --- |
| workspace_meta | Store schema version 1, workspace UUID, laboratory policy/version and compatibility metadata | CMP-01/CMP-06 |
| operations | Operation UUID, trusted actor/action/profile, selected-input manifest, fingerprint when available, processing state and final receipt reference | CMP-01/CMP-06 |
| source_artifacts | Artifact UUID, captured original BLOB, source label, byte length and SHA-256; linked to one snapshot | CMP-02/CMP-06 |
| package_versions | Package/lineage UUID, version UUID, zero-or-one predecessor, source/capture manifest and projection version | CMP-02/CMP-06 |
| captured_items and associations | Basis/candidate/scope/unknown-item identities, ordered membership, raw source pointers, source IDs and supplied-link problems | CMP-02/CMP-06 |
| import_receipts and issues | Coherent outcome and inventory, NOT_EVALUATED reason, safe issue metadata and operation/package linkage | CMP-02/CMP-06 |

These are physical responsibilities to realize with explicit SQL constraints and owned application operations. No placeholder result/model tables or universal EAV framework are required before I-01 needs them. Only CMP-06 writes the database; parameterized SQL is mandatory. Source data cannot supply table names, SQL, extensions or file destinations. Read commands do not create or overwrite a missing database.

The accepted sqlite3 connection policy sets autocommit explicitly and uses one consistent transaction API: autocommit=True with explicit SQL BEGIN IMMEDIATE, COMMIT and ROLLBACK owned by CMP-06. Configure and verify foreign-key, journal, synchronization and quota settings outside the capture transaction. Do not mix this policy with implicit connection-context-manager commits; tests must exercise the actual commit boundary and post-commit acknowledgement loss.

Use a per-workspace Windows named mutex for the complete import operation, acquired before worker release; retain SQLite's transaction locking as the store boundary. A second writer waits only within the configured bound and then receives a busy diagnostic. Process exit releases its mutex ownership; it does not mark an unfinished operation successful. Read-only inspection may proceed where SQLite permits it and must not upgrade itself into a writer. This is the I-01 single-writer mechanism, not an authenticated security boundary.

Read the selected original once into the bounded capture path; hash and parse that same retained byte instance. Detect reported source changes during acquisition and fail rather than mixing multiple reads. The snapshot proves which bytes TDG captured, not an atomic external-business-document version or source authenticity. Bindings and internal locators remain independent of the workstation's absolute path.

### 7.2 Commit, retry and lineage

1. Check laboratory admission and trusted operation context before content processing. Assign/record an operation identity and safe intent when permitted.
2. Acquire the explicitly selected bytes within limits. Derive the request fingerprint from the exact selected byte digest, selected-input identity, action, actor context, predecessor selection and contract/mapping/policy versions. A missing readable input does not yield an invented fingerprint.
3. Parse and project in the bounded worker. The parent accepts only a valid, bounded worker result matching that operation; the worker has no database write authority.
4. Commit original, immutable version, captured inventory/associations, receipt/issues and final operation outcome in **one transaction**. Print CAPTURED/package_version_ref only after successful commit.
5. Reconcile a lost acknowledgement by reading the committed operation. A committed identical authorized retry returns the same receipt and version. Reuse of its ID with a different fingerprint is a conflict.

Cancellation/crash before the capture transaction commits leaves no captured package. Retain or reconcile a FAILED receipt only where safely possible. If the receipt cannot be stored, display a safe persistence diagnostic without claiming durable history. An interrupted intent is reconciled from stored evidence; recovery never silently rereads the source or reruns capture. A finalized rejected/failed operation is inspected as such; a deliberate fresh attempt receives a new operation ID.

A new operation with identical source bytes creates a separately attributable version. Without an explicitly selected predecessor it starts a new lineage. A selected existing predecessor links one new child in its lineage; parent bytes and prior receipts stay unchanged. No predecessor is inferred from names, hashes, titles or copy-pasted steps. Reject invalid predecessor references before capture commit.

### 7.3 Store compatibility and retained data

I-01 opens only store schema version 1. A newer/unknown database version is refused without writes; ordinary import is never a restore or migration operation. No in-place upgrade/downgrade, selective history deletion or backup-restore workflow is enabled in this increment. Future migration needs an explicit compatibility plan and verified backup/rollback before it is introduced; preserved old originals must remain attributable.

Use a dedicated local, non-synchronized data directory, with the accepted default `%LOCALAPPDATA%\TDG\lab\<workspace-id>`. The repository may remain in the user's existing project directory; the operational database and journals should not be placed in OneDrive, a network share or the repository. Path selection is explicit at initialization and verified before writes. Existing stores are never overwritten by init. An integrity failure blocks writes and preserves the original database for deliberate diagnosis; it is not repaired by an LLM or by silent rebuild.

### 7.4 Logical records and independent versions

These full-review responsibilities refine the three information domains. They do not require separate tables or placeholder records in I-01. Normalization, embedding or splitting is permitted only while identities, lineage and ownership remain intact.

| Logical record | Owning responsibility | Minimum meaning and invariant |
| --- | --- | --- |
| `OperationContext` | CMP-01 | Trusted actor/action/profile context, operation identity, request fingerprint and policy decision. Submitted content cannot populate its authority fields. |
| `SourceArtifact` | CMP-02 | The deliberately selected source or opaque attachment, its source locator, media/profile declaration, receipt identity, hash where available and capture outcome. The original is distinguished from projections. |
| `PackageVersion` | CMP-02/CMP-06 | One coherent retained snapshot of scope, test basis, test cases, provenance declarations, gaps, conflicts and source lineage. It is immutable after capture commit. |
| `TestCaseRecord` | CMP-02 | One recognizable supplied TC item with TDG identity, preserved source identity, supplied fields, unknown/unmapped content and package-version lineage. It is not silently repaired. |
| `ReviewRequest` | CMP-01/CMP-06 | The deliberate request for one package version, requested dimensions, behavior/configuration references and operation identity. A retry is not automatically a second request. |
| `ReviewRun` | CMP-01/CMP-06 | The retained lifecycle and terminal state for one review request, including start/finalization effects and availability consequences. |
| `LedgerEntry` | CMP-03/CMP-04/CMP-06 | The requested assessment boundary for one recognizable item and dimension, with eligibility, prerequisites, attempt state, evidence references and cause-specific outcome. |
| `AssessmentResult` | CMP-04/CMP-06 | A conclusion or limitation with derivation, evidence and premise status. It cannot be written directly by raw model text. |
| `EvidenceItem` | CMP-04/CMP-06 | A source locator, deterministic check, model attempt reference, interpretation reference or other inspectable basis. Evidence does not become an authority grant. |
| `InterpretationEvent` | CMP-01/CMP-06 | An attributable human interpretation or clarification, including its input basis, version and impact on later work. It does not rewrite earlier results. |
| `Finding` | CMP-04/CMP-06 | A claim about the supplied testware or review basis with severity/status, evidence and derivation. Findings remain distinct from dispositions. |
| `DispositionEvent` | CMP-01/CMP-06 | An attributable accept/reject/defer/reopen decision over a finding. It records human handling; it does not prove business-rule correctness or TC repair. |
| `ExportArtifact` | CMP-07/CMP-06 | A deliberate projection of selected committed records, history cutoff, format/schema version, export identity and failure/outcome. It is never the canonical source of history. |
| `Policy/QualificationContext` | CMP-01/CMP-05/CMP-06 | The effective profile, permitted task, model/configuration qualification and policy versions used for a relevant operation. It is referenced, not inferred from the package. |

Original bytes, supplied field presence, declared provenance, opaque content and gaps remain the captured basis. Mechanical projections cannot replace originals. Classification, model output, technique assessment and human interpretation are derived/history records with explicit source links. Unknown content stays inspectable; an absent field is not an unreadable source.

TDG-generated identity scopes are retained below. I-01 uses UUIDv4 under SAD-D-019; no identity embeds a status, role or guessed origin. Details for later identities remain subject to OD-SAD02-002 before the corresponding capability is enabled.

| Identifier | Scope | Must remain stable across |
| --- | --- | --- |
| `package_id` | Logical package lineage | New review runs and exports of the same lineage |
| `package_version_id` | One immutable captured snapshot | All derived runs, entries, findings and exports based on that snapshot |
| `source_artifact_id` | One retained source or opaque attachment | Mechanical projections and re-reading within the same snapshot |
| `test_case_id` | One recognizable TC within a package version | Assessment entries and human history for that item |
| `review_request_id` | One deliberate request | Identical authorized retry of that request |
| `run_id` | One assessment lifecycle | Entries, terminal result and export references |
| `ledger_entry_id` | One item/dimension assessment boundary | Attempts, outcomes and later explanatory evidence |
| `event_id` | One interpretation/disposition/operation event | Audit and conflict handling |
| `export_id` | One export attempt/projection | Export receipt, failure or delivered artifact |

Keep source-system IDs/versions, names and bounded locators, origin/authority declarations, observed hashes and capture times where available. Missing or malformed source IDs remain attributable issues. A TDG ID cannot be represented as a source-system ID.

| Version dimension | Meaning | Change consequence |
| --- | --- | --- |
| Contract/schema version | Shape and interpretation of an interchange or retained record | Adapter or migration decision; historical records remain attributable |
| Package version | Captured supplied content and substantive basis | New package lineage snapshot; later review uses a new version |
| Source version | Version declared by the submitting system/document | Preserved provenance; not treated as TDG approval |
| Review-run version/configuration | Behavior, thresholds, technique request and policy context used by a run | New run when a behavior-affecting artifact changes |
| Model/qualification version | Qualified model/runtime/task envelope | New or limited run according to RA-07; no silent fallback |
| Export version | Format and projection rules used for delivery | New export artifact; canonical history is unchanged |

Historical records must remain readable through a supported contract or explicit versioned adapter. Before future migration, specify compatibility, rollback, integrity checks, interrupted-operation reconciliation, unsupported-version behavior and backup/export separation. Migration cannot rewrite earlier source meaning. I-01's refusal of unknown stores and absence of migration remain governed by Section 7.3.

### 7.5 Review commits, human history and version consequences

Beyond capture, the full workflow has separate durable commits for the review request; each ledger outcome with its evidence/items; reconciled run finalization; human interpretation/disposition events; and export outcome with a fixed history cutoff. A committed record must survive restart. Failure of later work preserves safely committed earlier work; unsaved output or failed finalization cannot be reported as success.

Human writes use an expected record version or equivalent compare-and-append check. Stale writes produce a visible conflict. Identical authorized retries reconcile existing effects; an in-progress operation is reported without duplication. Recovery never silently reassesses, rereads input or resumes a terminal run.

| Human action | Effect in this design |
| --- | --- |
| ROLE-02 changes supplied scope, or ROLE-03 supplies corrected TC/origin/accountability | Capture a new package version with lineage; preserve the old snapshot. |
| ROLE-04 makes the first applicable interpretation decision about already supplied evidence during an active run | It may support an entry not yet assessed only if no applied premise is replaced and no configured behavior artifact changes. Retain the exact decision version. |
| ROLE-04 replaces an interpretation already used, or an assessment behavior artifact changes | New run for subsequent assessment; retain earlier conclusions. A behavior change requires a new run even before the first substantive entry commits. |
| A human supplies a genuinely new business rule or clarification document | New package version, even if supplied during an interpretation discussion. |
| ROLE-05 accepts, rejects, defers or reopens a finding | Append a disposition event; preserve the claim and its derivation. Acceptance neither confirms a business rule nor verifies TC repair. |
| A role grant, qualification or required protection becomes invalid | Recheck before affected invocation, result promotion, authority-bearing write and disclosure; stop affected work and retain safe history under policy. |

After a terminal run, a new interpretation can be recorded for later use, but assessment belongs to a new run. Disposition acceptance does not confirm a business rule or verify repair. The human edits source testware externally; a revised package can be submitted while old findings remain pending.

Exports select committed package/run records, a history cutoff, schema/projection version, included interim/partial/failed records and visible omissions. Export has its own identity and delivery outcome; denial or failure releases no unsafe partial artifact and leaves canonical history unchanged. Markdown is a readable projection, not an authority-bearing restore format. Rendering remains inert and performs no external fetch.

Diagnostics correlate their identity with stage, subject scope, category, safe retry advice, actual durable effect and a bounded next action. For multi-entry operations, partial durable progress must be distinguished from an atomic capture commit. Diagnostic text must not expose raw model instructions, secrets or unapproved source content, and cannot misstate a successful commit.

## 8. Terminal contract for the increment

This is the accepted I-01 target contract; current availability is reported by the capability manifest and README. The accepted executable name is `tdg`, with `python -m tdg` as the equivalent development entry. The CLI is a thin adapter over CMP-01 services; tests can call the same services without subprocess-only coupling.

| Command family | Required behavior |
| --- | --- |
| tdg init --data-dir PATH --profile laboratory --actor-ref ID | Create a new workspace only with the selected laboratory policy and explicit logical operator assignment; never overwrite an existing store or grant sealed permission |
| tdg import --input FILE --classification public\|synthetic --purpose lab-development [--operation-id UUID] [--predecessor VERSION] | Capture one selected native JSON source. With no operation ID, generate and display one before the durable operation; an explicit ID supports controlled retry |
| tdg receipt OPERATION_ID | Inspect the attributable receipt or an honest unresolved/failed operation; no implicit re-import |
| tdg package list / tdg package show VERSION | Inspect stored versions and selected escaped source/projection fields, preserving omissions and the fact that review has not run |
| tdg capabilities / tdg version | Show the enabled native-capture surface, disabled review/model/export/sealed paths and effective build/contract/policy versions |

The configured data directory and actor reference are explicit global operation context. Source content cannot override them. Laboratory identity is logical attribution, not authenticated RBAC; the Owner does not automatically acquire every role. The accepted setup assigns only the lab administration/operator responsibilities needed for I-01. ROLE-02/03 declarations in supplied data remain declarations until their applicable later workflow.

Accepted process exit codes: 0 for a successfully delivered command result (including CAPTURED with visible issues and minimum NOT_EVALUATED); 2 for CLI/contract/rejected-input errors; 3 for admission/policy refusal; 4 for operational persistence/resource failure; 5 for operation/predecessor conflicts; 130 for interruption. Machine-readable receipt outcome and diagnostic cause remain authoritative; exit 0 never means TC approval or completed review. Structured stdout is optional for receipts; diagnostics go to stderr without raw payloads.

## 9. Laboratory protection and resource policy

Admission requires an explicit public/synthetic classification and lab-development purpose from the operator context. Missing/unknown/confidential classification is refused before prohibited content processing. A discovered contradiction stops the affected path with a safe diagnostic. This does not claim a reliable automatic detector of confidential text; eligibility of the supplied development corpus remains human-controlled.

| Resource | Accepted I-01 bound / enforcement |
| --- | --- |
| Selected inputs | One native JSON file per import; regular local file only, no directory traversal/search, archive expansion, URL, UNC/network source or automatic link following |
| Raw input | 1 MiB; bounded read stops at limit plus one byte, before accepting a complete parse |
| JSON depth / node count | Maximum 32 nested containers, with the root object at depth 1; at most 20,000 JSON values, counting each container/scalar once and excluding object member names. Preflight and decoded inventory enforce the bounds without silently skipping a remainder |
| Individual text / numeric token | 64 KiB UTF-8 per decoded text value or member name; 128 characters per numeric token; longer numeric tokens are REJECTED with CLI exit 2 under Section 6.1; text exceedance remains an explicit representation/limit failure |
| Candidate inventory | At most 200 native TC array entries and 200 basis array entries, counting deficient/malformed members too; these are capacity bounds, not business-scope or quality rules |
| Parse worker | One worker; 5 seconds wall time and 512 MiB committed memory. Windows Job Object limits are applied before releasing input to the worker; if required containment cannot be established, refuse processing |
| Controlled worker output | At most 8 MiB of framed projection data; parent validates shape, operation identity and size before persistence |
| Store / write waiting | Database main file capped at 512 MiB using page-count policy; write lock wait capped at 5 seconds. Check space for database/journal work; disk exhaustion causes safe failure, not unsafe truncation |
| Copies and logs | No separate raw-input temp files or automatic backups in I-01. SQLite journals remain in the managed directory. Routine diagnostics contain bounded metadata only; source/worker payloads are not debug-logged |

The parent bounds source acquisition and worker communication; the worker has no application database handle, arbitrary plugin invocation or source-discovery interface. Job Objects supply the selected time/resource containment mechanism, **not a complete OS sandbox or proof of zero egress**. The I-01 implementation contains no network-processing path or telemetry; the test environment observes attempted external calls. Full sealed egress/isolation evidence belongs to B-09 and cannot be inferred from this design.

Keep eligible synthetic/public originals, projections and receipts in the designated workspace until explicit authorized workspace disposal. No automatic age-based deletion or implicit promotion to backup/export is enabled. Workspace disposal and host-managed copies require an explicit local handling procedure; I-01 claims neither secure erasure nor recovery from hardware loss. Ordinary terminal display escapes control sequences, limits output and identifies truncation; no link/image is opened or rendered automatically.

These accepted limits must be implemented as a versioned policy and tested at below/at/above boundaries before the importer is enabled. Exact dependency versions, host OS build, CPU/RAM, filesystem, effective SQLite settings and observed resource behavior belong in the implementation environment record. A failed limit or mandatory audit/history write blocks the dependent operation; optional debug logging does not become a new gate.

## 10. Disposition of inherited open decisions

There are eight named decisions in SAD-02 and ten in SAD-03. Several overlap. The table records their accepted treatment for I-01 and the remaining scope that must be resolved before the corresponding later capability is enabled.

| Existing ID | Accepted I-01 disposition | Remainder / before which capability |
| --- | --- | --- |
| OD-SAD02-001 | SQLite and atomic BLOB/projection capture, Sections 5 and 7 | Later review/history/export transactions before I-02 |
| OD-SAD02-002 | UUIDv4, SHA-256 and source locators, Sections 5–7 | Additional model/event identities when introduced |
| OD-SAD02-003 | RA-09 envelope and local schema policy, Section 6 | Full review-export schemas before enabling export; F-002 is closed |
| OD-SAD02-004 | JSON manifest plus explicit CSV bindings as required by RA-09 | CSV implementation and parser limits before I-02 CSV enablement |
| OD-SAD02-005 | Concrete native-JSON/worker/store limits, Section 9 | Measure them during I-01; CSV/model limits before those paths |
| OD-SAD02-006 | Local managed laboratory directory/copy policy, Sections 7 and 9 | Backup/restore, fine-grained retention and all sealed mechanisms remain gated |
| OD-SAD02-007 | I-01 command/input/error contract, Section 8 | Review/interpretation/disposition/export CLI before I-02/I-03 |
| OD-SAD02-008 | Read schema 1 only; refuse unknown versions; no migration in I-01 | Explicit migration/rollback contract before any store version upgrade |
| OD-SAD03-001 | No model runtime selected or invoked in I-01 | Local runtime/endpoint choice before B-06/I-04 |
| OD-SAD03-002 | No model response schema enabled in I-01 | Exact task/output enumeration and validation before model evaluation |
| OD-SAD03-003 | No inference resource promise; intake limits are a different policy | Versioned measured inference/context/retry envelope before B-06/B-08 use |
| OD-SAD03-004 | Development fixture families remain exposed and ineligible as independent held-out evidence | Corpus partitions, oracle, criteria and requalification triggers before decision-bearing B-08 runs |
| OD-SAD03-005 | Bound the untrusted parser; no model/network capability in I-01 | Runtime-specific isolation/egress controls before model invocation; sealed verification separately |
| OD-SAD03-006 | No prompts/responses exist in I-01; raw capture/debug policy is explicit | Prompt/response retention before any model evaluation |
| OD-SAD03-007 | Laboratory originals/journals in one managed store; no protected input | Protected temporary copies, keys, backups and deletion before sealed use |
| OD-SAD03-008 | Parser cancellation is covered in I-01 | Selected model runtime cancellation before its invocation |
| OD-SAD03-009 | Capture/store/contract/policy identity recorded in I-01 | Full model behavior configuration and change impact before B-06 |
| OD-SAD03-010 | Logical laboratory attribution only | Verifiable identity and enforced sealed authorization before B-09 readiness |

Partially resolved decisions retain their remaining scope. A later implementation task cannot treat a deferred decision as a default. The I-01 gate checks that its own paths have no unresolved design blocker; it does not need a model choice for a build that cannot invoke one.

## 11. Requirement allocation and evidence accounting

The accepted [allocation index][allocation] retains all 249 requirement IDs, source identities, design/work owners and the 40 planned partial I-01 contributions; 209 requirements were allocated to later evidence. It reuses the accepted REQ–VAL routes rather than copying requirement text or creating one test per requirement. Its preparation-time pending label is superseded by the [2026-09-28 acceptance][review04].

| Requirement slice | Count | Current design/work location |
| --- | ---: | --- |
| RA-01 | 16 | Authority in Sections 4, 7.5, 8–9 and 15; B-01/B-04/B-07/B-09 |
| RA-02 | 36 | Flow in Section 4.2; records and lifecycle in Sections 6–8; B-03–B-07 |
| RA-03 | 50 | Source, identity and lineage in Sections 6–7; B-03/B-04 |
| RA-04 | 15 | CMP-03 and bounded qualification in Sections 4.1–4.2 and 15; B-04; not enabled in I-01 |
| RA-05 | 22 | Status axes and durable/human history in Sections 6.2, 7 and 15.4; B-03/B-04/B-07 |
| RA-06 | 20 | CMP-04, supported premises and contribution boundaries in Sections 4.2, 7.5 and 15; B-02/B-05; detailed technique algorithms remain later work |
| RA-07 | 20 | Gateway, qualification and evaluation separation in Section 15; B-06/B-08; no I-01 model invocation |
| RA-08 | 24 | Laboratory controls in Section 9 and model/sealed boundaries in Section 15; B-01/B-03/B-06/B-07/B-09 |
| RA-09 | 24 | Interchange, capture and export boundaries in Sections 6–8; B-03/B-07; CSV/export remain later work |
| RA-10 | 22 | Evaluation separation in Section 15 and verification/completion in Sections 12–14; B-02/B-08/B-10 |
| Total | 249 | Design routing, not implemented or fully tested coverage |

An I-01 contribution is partial. Source retention alone cannot satisfy a requirement that also constrains later review/export behavior. All 169 validation obligations remain authoritative and may require evidence from several increments. Neither the allocation count nor this consolidation establishes clause-level design completeness or product quality.

## 12. STLC allocation and first-increment test conditions

The Owner accepted the following allocation and all 16 TCND-I01 conditions on 2026-09-27. The implementation gate followed on 2026-09-28. The tables are the retained plan, not execution results. Current implementation and test-preparation evidence is linked from [README.md](../../README.md).

Fixtures use explicit, versioned synthetic rules. The discussed discount example and publicly exposed customer-creation families are development material, not fresh held-out acceptance evidence. Expected observations derive from accepted contracts before implementation results are inspected.

| STLC activity | I-01 output / responsibility |
| --- | --- |
| Planning | Owner accepts scope, resource assumption and completion criteria; test author identifies risks and required evidence |
| Analysis | Link the conditions below to selected requirements and existing VAL; mark clauses outside I-01 explicitly |
| Design | Independent expected receipts/inventory/identity effects; equivalence classes, boundary values, decision combinations and operation-state transitions |
| Implementation / environment | After GO: executable pytest tests, versioned fixtures/mutations, environment manifest and repeatable failure injection |
| Execution | Record exact build/policy/configuration, actual outcomes, defects, retest and affected regression; do not equate parser success with review success |
| Completion | Compact report with passed/failed/not-run conditions, defects, retained limitations and Owner increment decision; no global MVP acceptance |

| Condition ID | Future challenge and observable oracle | Principal trace |
| --- | --- | --- |
| TCND-I01-01 | Native synthetic source survives capture/restart byte-for-byte; raw digest, item order, locators and receipt/package linkage agree | RA03-REQ-003/006/020; RA09-REQ-005/014 |
| TCND-I01-02 | Same operation/content/configuration after lost acknowledgement returns the same version; changed fingerprint conflicts; a new operation with identical bytes creates a distinct version | RA03-REQ-048; RA05-REQ-018; RA09-REQ-009/014 |
| TCND-I01-03 | Revised source with an explicit predecessor creates one child and preserves the parent; invalid predecessor cannot commit | RA03-REQ-043/044/047 |
| TCND-I01-04 | Missing/extra/mistyped envelope members, wrong document kind/version, and valid empty content produce the Section 6.1 outcomes | RA09-REQ-001/003/013 |
| TCND-I01-05 | Duplicate nested names, BOM, invalid UTF-8, non-finite tokens and huge numeric lexemes cannot become silently changed source values | RA09-REQ-004/006/016 |
| TCND-I01-06 | Missing/null/empty/whitespace/mistyped and unknown fields remain distinguishable; narrative steps and duplicate source IDs are preserved | RA03-REQ-014/022/025; RA09-REQ-006/007/012 |
| TCND-I01-07 | Exact origin codes versus free text; scoped defaults versus absent/null/negative declarations; no inferred accountability or eligibility | RA03-REQ-021; RA09-REQ-008/024 |
| TCND-I01-08 | Imported roles, approval flags, $ref, URLs, path-like values and unbound sources cause no retrieval, identity restoration or authority change | RA03-REQ-005; RA09-REQ-003/005/023/024 |
| TCND-I01-09 | Public/synthetic admission contrasts with unknown/confidential or missing permission; disallowed input is refused before parser release | RA03-REQ-042; RA08-REQ-004/020 |
| TCND-I01-10 | Below/at/above every enabled size/count/depth limit; worker timeout/memory limit and inability to apply required containment | RA09-REQ-016; RA08-REQ-010/020 |
| TCND-I01-11 | Crash/cancel before intent, after intent, before capture commit and after commit/before acknowledgement; never a partially captured package or duplicate retry effect | RA05-REQ-017/018/019; RA09-REQ-014/015 |
| TCND-I01-12 | Write contention, exhausted storage, read-only directory, corrupt/unknown-schema store and mandatory history-write failure preserve safe prior data | RA05-REQ-017/019; RA08-REQ-020; RA09-REQ-014/016 |
| TCND-I01-13 | Second process cannot bypass the application writer boundary; a read command never initializes or rewrites a missing/unsupported database | SAD-D-001/003; RA05-REQ-017/018 |
| TCND-I01-14 | Escape/control sequences and malicious-looking supplied text render inert; diagnostics reveal no raw payload or unnecessary absolute path | RA03-REQ-030; RA08-REQ-014; RA09-REQ-023 |
| TCND-I01-15 | Every captured result visibly says minimum NOT_EVALUATED and review not performed; no run/findings/availability fabricated; unsupported commands do not activate a model/export/sealed path | RA03-REQ-032/050; RA09-REQ-013/015/017; RA07-REQ-010 |
| TCND-I01-16 | Explicit source selection remains bounded under source changes or path redirection; capture never opens undeclared input or combines multiple content instances | RA03-REQ-005/006; RA09-REQ-005/014 |

Use meaningful unit checks for syntax/projection/identity, integration checks with a real temporary SQLite store and controlled commit faults, and a small CLI path on the supported Windows host. Testing TDG at code/integration level is separate from the system-level black-box testware it will review. A fake model can test gateway handling, but cannot qualify a real model or establish semantic accuracy. Coverage percentages alone are not acceptance gates.

Later verification retains the [SAD-01 flow challenges][sad01-history], [SAD-02 identity/history challenges][sad02-history] and [SAD-03 gateway challenge matrix][sad03-history]. It must exercise denial before capture, deficient capture, partial supported review, first interpretation versus changed premises, stale human writes, model/capacity faults, lost commits, failed export and shared protection loss. These historical matrices allocate future tests; they are not successful executions.

## 13. Executable work breakdown and resource estimate

**Accepted with an effort-estimate reservation on 2026-09-27 (Europe/Warsaw).** The Project Owner stated: "akceptuje paragraf 13 z zastrzezeniem ze nakład prac szacowany na 40-60 godzin uważam za mocno szacunkowy, podejrzewam ze same testy tyle zajmą." The work breakdown is accepted. The original 40–62-hour total and its component estimates remain very uncertain, unvalidated planning hypotheses, not an approved budget, effort ceiling or delivery commitment. The Owner's concern that testing alone could require comparable effort is retained as an underestimation risk, not adopted as a new testing estimate or added mechanically to the original total.

The table preserves the accepted W01–W07 sequence and original estimates. Current status and the later provisional test-work forecast are linked from [README.md](../../README.md); this is not a live progress table. Development and further fixture preparation are paused pending documentation cleanup and an agreed revised implementation plan. The sole human remains accountable for understanding changes and evidence; AI assistance is not independent review or additional staffing.

| Work item | Bounded output | Dependency | Original indicative human effort — unvalidated |
| --- | --- | --- | ---: |
| I01-W01 | Project/venv entry point, capability manifest, pinned environment/dependencies and empty-store initialization | Accepted I-01 gate | 3–5 h |
| I01-W02 | Synthetic fixtures, independently specified receipt/identity oracles and traceable test skeletons | W01; approved contracts | 4–6 h |
| I01-W03 | Strict bounded JSON/envelope processing and faithful projection | W01/W02 | 5–8 h |
| I01-W04 | Parser worker containment, admission, local path/copy policy and safe diagnostics | W01/W02; can progress alongside W03 | 7–10 h |
| I01-W05 | Atomic SQLite capture, IDs, lineage and retry/recovery effects | W03/W04 | 4–6 h |
| I01-W06 | CLI receipt/package inspection and integrated failure/regression tests | W05 | 6–10 h |
| I01-W07 | Windows walkthrough, recorded observations, defect disposition and completion report | W06 | 3–5 h |
| Original base estimate | Includes reading, implementation oversight, tests and review; not measured productivity | Owner's underestimation reservation applies | 32–50 h |
| Original provisional contingency | Resource containment, persistence fault behavior and learning/rework; adequacy unverified | Reassess during W02 and after W03/W04 | 8–12 h |
| Initial total estimate | Retained with Owner reservation; actual total may be substantially higher | No approved effort ceiling or calendar commitment | 40–62 h |

The accepted re-estimation rule was to use W02's detailed inventory, then observed W03/W04 work. Account for fixture/oracle preparation, test implementation and fault injection, execution/diagnosis, fixes, retest/regression and completion evidence without double counting. The original total already included testing. A condition count is not an effort estimate, and required verification cannot be reduced to fit the original range.

Approximately five hours per week remains a flexible capacity reference. The earlier 16–32-hour estimate concerned B-01 design, not implementation; actual past effort cannot be reconstructed from chat timestamps. Current forecasts remain provisional. Setup/package installation is separate from Review Package processing. I-01 needs no model, inference hardware, cloud subscription or external-model account; record the actual supported host environment without inferring performance from GPU size.

## 14. Review evidence, acceptance and implementation boundary

### 14.1 Preparation evidence

[SR-SAD04-001 v0.1][verification04] preserves the original source/ID checks, allocation inventory, arithmetic, applied corrections and artifact identities. [SR-SAD04-001 v0.2][review04] records acceptance of that evidence. These were document checks by the same AI-assisted authoring path, not independent assurance or runtime containment, fidelity or durability results.

The SAD-01/02 walkthroughs and SAD-03 correction record remain linked in Section 2. Their historical examples, individual replies and earlier failures are retained without repeating the full acceptance history in the design text.

### 14.2 Recorded implementation GO

On 2026-09-28 the Owner accepted the complete corrected SAD-04 v0.2, allocation index v0.2 and SR-SAD04-001 v0.1; closed both SAD-04 findings and B-01 for the I-01 boundary; and granted GO to I-01. The reply, preserved in [SR-SAD04-001 v0.2][review04], was:

> Tak zatwierdzam i udzielam GO

That permission covered W01 and the remaining accepted increment work without another invented starting gate. It retained public/synthetic laboratory admission, all required tests, the effort reservation and later model/sealed/product gates. The subsequent development pause governs current work; this cleanup does not resume implementation.

### 14.3 I-01 completion and subsequent gates

Completion requires demonstrated source/identity/commit invariants, honest receipts and unavailable-path behavior, all applicable conditions above executed with recorded outcomes, and no unresolved defect that invalidates the selected capture/protection boundary. Unrun required conditions and failures prevent a completion claim; other residual defects need an attributable Owner disposition. Performance observations are reported for the actual environment rather than converted into invented universal thresholds.

The Owner then decides increment acceptance and the next bounded implementation scope. Human oracle/protocol/criteria approvals precede decision-bearing model qualification or product acceptance; explicit ROLE-09 readiness precedes confidential use. These are retained SDLC/STLC gates, not a requirement to invent a new SAD document for each coding task.

### 14.4 Document history

The [original SAD-04 v0.1][history04], [v0.2 snapshot][original], allocation versions and existing reviews preserve their identities and decisions. This file incorporates the accepted architecture and corrections without adding another document version. SAD04-I01-NUM-001 remains the separate dated authority for the Section 6.1 clarification. Historic GO and accepted design do not imply I-01 completion, usefulness or sealed readiness.

## 15. Model contribution and future protection design

This section consolidates the accepted logical SAD-03 design. **No model path is enabled in I-01.** Runtime selection, exact response enums/schemas, numeric inference limits, retention and enforcement mechanisms remain subject to the open decisions in Section 10. Logical component/process boundaries do not establish operating-system isolation.

### 15.1 Invocation purpose and permission

Every call uses CMP-05 and exactly one declared purpose/task. Purpose is distinct from the laboratory/sealed profile; public data alone does not authorize evaluation.

| Boundary | Operational review | Candidate evaluation |
| --- | --- | --- |
| Permission | Current qualification for the exact task/configuration/profile tuple and authorized review operation | Explicit ROLE-08 authorization of a separate laboratory evaluation context; an unqualified candidate may be invoked, with the absence of qualification recorded |
| Identity and inputs | Active review request, run, ledger boundary and selected immutable package version | Identified evaluation run/item, versioned input manifest and effective configuration; applicable protocol, oracle and evaluation-set references; no fictional operational ledger entry |
| Admissible profile/data | The authorized operational profile and its input policy; the immediate project target remains public/synthetic laboratory material | Public or synthetic laboratory material only; no confidential input or reuse of operational content outside the declared evaluation boundary |
| Output authority | Validated candidate contribution, subject to the existing evidence and human-interpretation rules | Visibly evaluative evidence, unqualified where applicable; no automatic operational supported result, finding disposition or qualification grant |

CMP-01 supplies trusted actor/action/profile context; CMP-03/CMP-04 request bounded evidence; CMP-05 enforces authorization, projection, invocation and response checks; CMP-06 retains permitted history. Only operational contributions can be mapped by CMP-04 to their requested ledger boundary. Evaluation has its own run/item/input identities and cannot gain operational authority by passing validation, being recorded or receiving human analysis.

Both purposes keep the applicable admission, resource, cancellation, protection and audit controls. Invalid attempts may be retained under policy for evaluation, with their invalidity preserved. ROLE-08 qualification is a separate attributable decision. Development, qualification and held-out evidence, protocol timing, human oracle and exposure follow [RA-07][ra07] and [RA-10][ra10]; the model is never its sole judge.

Only the RA-07 task catalogue is authorized. LLM-03 assists assessment relationships, not source-field/capture mapping. Check qualification and data permission before invocation and again before affected result promotion/delivery; revoked or stale permission prevents that effect while preserving safe committed history.

### 15.2 Task envelope and minimal context

| Field group | Minimum meaning |
| --- | --- |
| Invocation purpose | Explicit operational review or candidate evaluation, selected through trusted authorization outside supplied content; independent of the laboratory/sealed protection profile |
| Operation identity | `operation_id`, attempt number and retry parent where applicable; operational review additionally references `review_request_id`, `run_id` and `ledger_entry_id`; evaluation instead references its own evaluation run and item identities |
| Subject identity | Operational package version, recognizable TC identity and requested review dimension; or versioned evaluation input manifest and selected item/task references. No free-form subject substitution or evidence from outside the authorized boundary |
| Task identity | stable task type, task contract version and permitted contribution class |
| Behavior context | Prompt/template/configuration identifier and version, model/runtime identifier, and applicable qualification reference/status. Operational use requires a current exact grant; candidate evaluation explicitly records absent qualification where applicable and references its evaluation authorization and protocol |
| Profile/policy | Effective policy version, actor/action authorization decision and data classification. Operational review uses its authorized laboratory or separately verified sealed profile; candidate evaluation under Section 15.1 is laboratory-only on public/synthetic inputs |
| Context manifest | allowlisted evidence item IDs, bounded field names, locators, content hashes and projection reason |
| Limits | input size, output size, duration, retry, concurrency and cancellation policy references |
| Output contract | expected schema, allowed enums, reference rules and promotion state |
| Provenance | Operational source package/version or evaluation input/protocol versions, gateway version, contract version, timestamps and attempt hash where supported |

An attempt cannot replace its selected subject with a free-form one. No envelope or supplied text can grant model authority. The projection rules are:

The projection builder applies the following rules before invocation:

1. start from an empty context and add only fields explicitly required by the task contract;
2. select records by immutable identity and operational package lineage or the authorized evaluation input manifest, never by a model-supplied path or URL;
3. preserve field origin, source locator and sensitivity/classification metadata;
4. cap number of records, field length, total input size and nesting depth according to the effective policy;
5. replace unavailable or disallowed content with an explicit omission marker, not a fabricated value;
6. exclude credentials, access tokens, secrets, unrelated packages, local environment variables and hidden prompts;
7. do not resolve links, call external services or inspect arbitrary directories;
8. include the projection manifest in retained attempt metadata, subject to the profile's sensitive-content policy;
9. make truncation, normalization and redaction visible to downstream validation;
10. prevent a model response from requesting an automatic context expansion within the same attempt.

### 15.3 Qualification and change impact

Qualification applies to `(model, runtime, task contract, behavior/configuration, policy profile, contract/schema versions, resource envelope)`. Behavior-affecting changes—including prompts, quantization, runtime patches, output schemas, context policies or limits—require impact analysis and affected qualification; a model name or moving alias cannot silently preserve permission.

Retain exact identities/integrity references, task and configuration, controlled eligible challenge sets, independently determined structural expectations, human or justified deterministic oracle, resource/failure observations, applicable protection evidence and an attributable qualification decision with expiry/change triggers. Task or profile success does not grant another task/profile. Missing or stale required protection evidence prevents operational reliance; candidate evaluation remains the separate route in Section 15.1.

### 15.4 Cause, execution stage and assessment outcome

CONTEXT_INSUFFICIENT describes a bounded attempt limitation, not proof of absent package evidence. It does not choose an assessment status. Apply the actual cause and stage:

| Established situation | Affected-work consequence |
| --- | --- |
| Necessary business evidence is genuinely absent, ambiguous or contradictory, and a substantive assessment was attempted | Withhold the dependent conclusion; record UNGRADABLE and the specific clarification need for that dimension. |
| No authorized qualified capability is available, or the input is outside its declared envelope before substantive work starts | Record NOT_PERFORMED with the capability reason. This does not establish that the TC is outside MVP. |
| Supplied material exceeds supported context/capacity before work starts | Record NOT_PERFORMED for unsupported requested work; identify the present-but-unprocessed material and any authorized independently assessable subset. |
| Invocation starts but fails, times out, exhausts resources, produces unusable output or is interrupted by a limit | Work without a safely completed conclusion is INCOMPLETE, with an operational cause; do not infer a missing business rule. |
| Mandatory policy, authority or protection prerequisite fails | Block the affected operation and every path depending on the failed shared control. A whole-run prerequisite produces run state BLOCKED; affected ledger work remains NOT_PERFORMED if unstarted or INCOMPLETE if started without a safe conclusion. |

BLOCKED remains a run/operation state. A contained fault can coexist with normal finalization and limited results. Preserve coexisting causes, safely completed independent work and omissions. A supported basis-gap observation can be ASSESSED while a dependent technique conclusion is UNGRADABLE. Availability follows substantive committed entries, not diagnostics or finding count.

Supplied-but-unprocessed evidence is a tool limitation; it does not itself require a tester to rewrite or resubmit TC. Genuine new business material requires a new package version. Subsets and retries must follow the authorized policy and run/version rules; no automatic context expansion, fabricated rule or full-inspection claim follows from a model's confident response. Candidate-evaluation failures remain under evaluation identities, without operational ledger records.

### 15.5 Runtime, retry, cancellation and copies

The runtime receives no arbitrary record-store access, filesystem discovery, environment secrets, commands/tools/plugins, network/DNS/URL retrieval, direct writes/export publication, policy/identity mutation or hidden context-expansion route. Required controls must be enforced and verified; prompt instructions alone are not enforcement. Every output destination is explicit, and release is through the controlled application path.

Each attempt fixes context, model, profile and destination and references explicit limits; absence of a limit is not unlimited permission.

| Limit | Required behavior when reached |
| --- | --- |
| Context record/field count | Stop projection and record the limit and omitted material; pre-start unsupported work is NOT_PERFORMED. |
| Input size or nesting depth | Reject or bound input only under the authorized context policy; retain omissions and stage. Unsupported unstarted work is NOT_PERFORMED; unfinished work interrupted after invocation is INCOMPLETE. |
| Output size | Stop/contain the response and record its validation failure; affected started work without a safe conclusion is INCOMPLETE. |
| Wall-clock time | Cancel if supported; otherwise mark the attempt timed out and prevent promotion. |
| Memory/CPU or runtime quota | Record resource failure; do not silently switch runtime or model. |
| Retry count | Stop at the configured bound; preserve each attempt and final operational cause. |
| Concurrent attempts | Respect the first workflow's one-active-run and configured concurrency policy. |

These are future inference limits, separate from I-01's parser bounds. A lost response reconciles an existing committed operation. A model retry receives a new immutable attempt ID, parent and reason under the same authorized bounded policy. Predeclared qualified retry variants remain part of that policy; retain the actual variant and attributable request context. Retries are limited to unresolved work in an active run: they cannot restart a terminal run or reassess a committed entry. Editing behavior requires a new configuration identity, applicable qualification and a new run. No retry may silently switch model, prompt, destination, context policy or protection profile. Evaluation retries retain their evaluation purpose and protocol.

Cancellation stops new work, signals in-flight work where supported and reconciles committed effects; it cannot turn a partial run into COMPLETED. An unresponsive runtime cannot have output promoted after timeout. Model behavior cannot control emergency stop. Before enabling the runtime, define who can stop it, termination, copy handling, retained evidence and verified restart/recovery. Recovery does not silently rerun assessment.

Create attempt projections/buffers only after admission; record copy creation, classification, lifetime and disposal/retention outcome. Temporary copies are not canonical sources. Prefer metadata/hashes and bounded permitted excerpts over unlimited laboratory prompt/response duplication. Exact raw-retention policy remains an open decision; debug mode grants no secret logging. Mandatory shared protection/audit failure stops dependent deterministic work too; emergency containment remains possible and optional diagnostics have only their policy-defined effect.

### 15.6 Output validation and candidate handling

Validate transport/attempt identity, resources/encoding, schema/enums/cardinality/version, references within the selected input, policy/authority/destination and then semantic support. Passing mechanical checks does not establish that a real citation supports a claim. Required validation failure prevents promotion; malformed or unusable output after work starts leaves unfinished operational work INCOMPLETE, not a newly inferred TC defect.

The accepted logical contribution classes remain design candidates; OD-SAD03-002 must resolve the executable enumeration/schema before use.

| Class | Example use in MVP | What it may not do |
| --- | --- | --- |
| `RELATION_CANDIDATE` | Suggest that a supplied TC may relate to a supplied requirement or business rule. | Establish a missing link as fact or retrieve the requirement. |
| `GAP_CANDIDATE` | Point to a missing precondition, expected result, input value or rule in the supplied material. | Invent the missing rule or modify the TC. |
| `TECHNIQUE_CANDIDATE` | Suggest a possible EP, BVA, decision-table or state-transition question from supplied evidence. | Claim that the technique is mandatory or that coverage is proven. |
| `CLASSIFICATION_CANDIDATE` | Highlight evidence that the TC may not be system-level black-box. | Override deterministic classification or human accountability. |
| `RISK_CANDIDATE` | Highlight ambiguity, contradiction, stale source or potential impact. | Assign authoritative business severity without the approved policy/context. |
| `EXPLANATION` | Explain an independently produced deterministic finding in bounded language. | Change the finding's derivation or turn explanation into evidence of correctness. |

The logical promotion states distinguish raw, candidate, human-interpreted and withheld material; they are not run or finding-disposition enums.

| State | Meaning |
| --- | --- |
| `RECEIVED_UNVALIDATED` | Raw response was received within the operation boundary but is not yet usable. |
| `STRUCTURALLY_VALID` | Transport, resource, schema and reference checks passed. |
| `CANDIDATE_RECORDED` | The response became an explicitly typed candidate contribution linked to evidence. |
| `HUMAN_INTERPRETED` | An authorized human interpreted or confirmed its limited relevance; this is not TC approval. |
| `WITHHELD` | The response remains retained as evidence/diagnostic but cannot support the requested conclusion. |
| `REJECTED` | The response violated structural, policy or provenance rules and cannot enter the derived result set. |

A valid operational contribution is still subject to CMP-04 evidence and human-interpretation rules. A deterministic calculation over an unconfirmed premise retains that limitation; an LLM explanation cannot change the original finding's derivation. Evaluation output remains evaluation evidence in every state. Supplied AI-directed instructions are inert content, never permission to execute tools, alter the context or bypass checks.

### 15.7 Observation, profiles and later verification

Retain, under the profile's content policy: purpose, operation/attempt and review or evaluation identities; actual versioned inputs; task/model/runtime/behavior/policy/contracts; qualification status or explicit absence and evaluation authorization; context manifest and omission/redaction/truncation markers; available hashes; timing/cancellation/resource evidence and retry parent; validation and promotion outcomes; coexisting causes/stages; protection/audit status; and later human-event references. Operational ledger, run state and availability remain separate. Diagnostics, assessment evidence and human decisions are linked records with different meanings.

These records support later reproduction, not a promise of identical model output. Reproduction is a new linked operation, not a history rewrite. Laboratory work remains public/synthetic only; its evidence grants no confidential-data permission.

Before sealed use, [RA-08][ra08] requires verified identity/role authorization on every protected operation; protected sources, projections, keys, temporary copies and backups; enforceable runtime restrictions; mandatory history/audit; controlled retention/deletion/restore; valid egress observation; and explicit ROLE-09 authorization. Sealed runtime permits no external egress, including diagnostics or telemetry. Any allowed internal destination stays inside its verified boundary. A local model, profile string or empty observer result cannot establish readiness.

There is no automatic laboratory-to-sealed transition or silent package reclassification. Profile changes require current qualification context, protection evidence and human authorization; transfers or recapture are explicit and auditable. Missing mandatory evidence prevents the affected admission/operation. The retained [SAD-03 verification matrix][sad03-history] and governing RA-07/08/10 obligations guide later runtime, integration, failure and human-evidence checks.

## References

[gate]: ../requirements-analysis/ra-10/test-design-gatekeeper-requirements-analysis-readiness-v0.2.md
[ra03]: ../requirements-analysis/ra-10/test-design-gatekeeper-ra-03-review-package-content-provenance-validation-v0.4.md
[ra04]: ../requirements-analysis/test-design-gatekeeper-ra-04-scope-qualification-classification-boundaries-v0.2.md
[ra05]: ../requirements-analysis/ra-05/test-design-gatekeeper-ra-05-findings-dispositions-persistence-v0.2.md
[ra06]: ../requirements-analysis/ra-06/test-design-gatekeeper-ra-06-technique-applicability-design-coverage-v0.2.md
[ra07]: ../requirements-analysis/ra-07/test-design-gatekeeper-ra-07-llm-roles-qualification-v0.2.md
[ra08]: ../requirements-analysis/ra-08/test-design-gatekeeper-ra-08-confidentiality-security-privacy-v0.2.md
[ra09]: ../requirements-analysis/ra-09/test-design-gatekeeper-ra-09-data-representations-import-export-contracts-v0.2.md
[ra10]: ../requirements-analysis/ra-10/test-design-gatekeeper-ra-10-evaluation-acceptance-v0.2.md
[review03]: ../reviews/test-design-gatekeeper-sad-03-review-record-v0.2.md
[review04]: ../reviews/test-design-gatekeeper-sad-04-review-record-v0.2.md
[verification04]: ../reviews/test-design-gatekeeper-sad-04-review-record-v0.1.md
[trace]: ../requirements-analysis/ra-10/test-design-gatekeeper-requirements-analysis-traceability-audit-v0.1.json
[allocation]: test-design-gatekeeper-sad-04-requirement-allocation-v0.2.json
[history04]: test-design-gatekeeper-sad-04-integrated-review-increment-plan-v0.1.md
[numeric]: test-design-gatekeeper-sad-04-i01-numeric-token-limit-addendum-v0.1.md
[sad01-history]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/6bf96d9748c1d4faae049786feb8c49397f4c659/docs/solution-design/test-design-gatekeeper-sad-01-components-review-flow-v0.1.md
[sad02-history]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/6bf96d9748c1d4faae049786feb8c49397f4c659/docs/solution-design/test-design-gatekeeper-sad-02-data-identity-contracts-v0.1.md
[sad03-history]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/6bf96d9748c1d4faae049786feb8c49397f4c659/docs/solution-design/test-design-gatekeeper-sad-03-model-protection-v0.3.md
[original]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/6bf96d9748c1d4faae049786feb8c49397f4c659/docs/solution-design/test-design-gatekeeper-sad-04-integrated-review-increment-plan-v0.2.md

Technical references consulted for the original 2026-09-27 choices, retained as mechanism references rather than current verification evidence:

- [Python version lifecycle](https://devguide.python.org/versions/)
- [Python 3.13 sqlite3](https://docs.python.org/3.13/library/sqlite3.html)
- [Python 3.13 json](https://docs.python.org/3.13/library/json.html)
- [jsonschema validation](https://python-jsonschema.readthedocs.io/en/stable/validate/) and [reference retrieval](https://python-jsonschema.readthedocs.io/en/stable/referencing/)
- [Windows Job Objects](https://learn.microsoft.com/en-us/windows/win32/procthread/job-objects)
