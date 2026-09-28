# Test Design Gatekeeper

## SAD-04 — Integrated Design Review and Next-Increment Planning

| Field | State |
| --- | --- |
| Version / date | 0.1 — 2026-09-27 (Europe/Warsaw) |
| Status | PROPOSED — Owner walkthrough in progress; Section 3 corrective dispositions and Sections 4–12 accepted; Section 13 accepted with effort-estimate reservation; no implementation GO |
| Entry authority | SR-SAD03-001 v0.2: accepted SAD-03 v0.3, closed third B-01 activity and explicit GO to SAD-04 |
| Inspected baseline | `583356e148378c0669cee5baa9bc4cdbd2cc3182` on main; SAD-01/02 accepted, SAD-03 v0.3 accepted |
| Work allocation | Fourth and final planned B-01 activity: integrated review, blocking design choices, first-increment plan and STLC allocation |
| Implementation boundary — scope accepted, GO pending | I-01 — local laboratory native-JSON capture and inspection; a foundation increment, not the complete MVP |
| Authority retained | 249 accepted requirements and 169 validation obligations under SR-RA-001 v0.2 |
| Review evidence | Documentary author review by the same AI-assisted author; no independent review or executed product tests claimed |

## 1. Purpose and decision convention

SAD-04 connects the component design, data contracts and model/protection design to a bounded implementation proposal. It must make the next coding task understandable, testable and small enough for a solo side project. It does not reproduce the requirements catalogue or add another analysis phase.

The Owner has authorized this design activity. **All six SAD-D-016–021 choices are ACCEPTED as design decisions.** On 2026-09-27, the Owner accepted both Section 3 corrective dispositions and Sections 4–12: scope, implementation choices, interchange/status contracts, persistence/identity/failure behavior, the terminal contract, laboratory/resource policy, the disposition of inherited open decisions, requirement allocation/evidence accounting, and the STLC plan with all 16 I-01 test conditions. Section 13 is accepted with an explicit reservation about the very uncertain effort estimate and possible testing effort of comparable size to the initial total. Correction verification, finding closure, review of Section 14 and implementation GO remain pending. Normative wording in unaccepted proposals states the intended design contract, not a permission already granted. Accepted upstream requirements remain authoritative throughout.

Closing this document may authorize implementation of I-01 only, through the explicit gate in Section 14. Later increments retain all outstanding requirements and their own applicable readiness checks. Completing I-01 cannot be described as completion of TDG, model qualification, sealed readiness or official ISTQB conformity.

## 2. Sources and review method

| Source | Role in this review |
| --- | --- |
| [SR-RA-001 v0.2][gate] | Accepted phase authority, B-01–B-10 work allocation, flexible five-hour weekly capacity and R-08 |
| [SAD-01][sad01] | Seven logical components, controlled flow, operating entry points and commit effects |
| [SAD-02][sad02] | Record ownership, immutable identity, operation retry semantics and unresolved physical choices |
| [SAD-03 v0.3][sad03] and [SR-SAD03-001 v0.2][review03] | Model purposes, qualification, protection, cause/stage outcomes and entry GO |
| [RA-03 v0.4][ra03], [RA-05 v0.2][ra05], [RA-08 v0.2][ra08], [RA-09 v0.2][ra09] | Capture, minimum checks, lifecycle, laboratory controls and exact interchange contract |
| [Accepted REQ–VAL ledger][trace] | Existing requirement inventory and validation routes; unchanged by this document |
| [SAD-04 allocation index][allocation] | Compact routing of all 249 requirement IDs to design/work owners; no implementation or full clause-coverage claim |

The author compared the three SAD documents at their shared interfaces: input envelope, identity, capture commit, assessment/run status, model permission, protection failure and history. The focused I-01 checks then traced capture/inspection behavior to applicable requirements and future test conditions. Source examples remain versioned examples: the age ranges 18–75 in SAD-01 and 18–120 in RA-09 are different supplied fixture rules, not interchangeable business defaults.

Historical pending notices in retained RA snapshots are read with their accepted closure records. The two findings below concern design wording; they do not reopen the accepted requirements baseline.

## 3. Integrated review findings and corrections

| Finding | Evidence and impact | Disposition accepted on 2026-09-27 | Verification before closure |
| --- | --- | --- | --- |
| SR-SAD04-F-001 — Ledger vocabulary mixes processing and assessment | SAD-02 Section 7.1 lists COMPLETED and BLOCKED as ledger outcomes. RA-05 Section 3.2, RA-09 Section 7.1 and SAD-03 Section 6.3 distinguish assessment outcomes from run state. Implementing the illustrative table literally would create incompatible records. | Use exactly ASSESSED, UNGRADABLE, NOT_PERFORMED and INCOMPLETE for substantive ledger outcomes. Keep any internal pending/in-progress marker separate. BLOCKED and COMPLETED remain run states. Availability is an independent derived axis, not a lifecycle with NONE as a universally non-terminal state. | Compare serializers and future enum tests to the four outcome sets in Section 6.2; annotate the historical SAD-02 table with the accepted correction reference at closure. |
| SR-SAD04-F-002 — Illustrative JSON shape conflicts with the accepted wire envelope | SAD-02 Section 8.1 shows package/submission at the root and a different version string. RA-09 Sections 2.2–3 require document_type, contract_version and content only, with version "1.0". The example is explicitly illustrative, but is unsafe as an implementation template. | Adopt RA-09's exact three-member control envelope. Put supplied scope, basis and TC inside content; trusted operation context and generated TDG identities stay outside supplied authority. Unknown content fields remain preservable. | Exercise the positive/negative envelope table in Section 6.1; annotate the historical example rather than silently treating its shape as valid. |

Both findings are **OPEN — RESOLUTION ACCEPTED; CORRECTION VERIFICATION PENDING**. On 2026-09-27 (Europe/Warsaw), the Project Owner accepted the Section 3 dispositions in the walkthrough: "tak, akceptuje ustalenia z paragrafu 3". Their corrected meanings are used in the candidate below under the already-authoritative RA contracts. The historical SAD-02 correction notices and documented correction verification remain required before finding closure and B-01 closure. No additional substantive contradiction was identified in the other inspected interfaces; this is not a claim of exhaustive defect absence.

F-001 is Medium for design consistency and must be corrected before a ledger implementation. F-002 is High for I-01 readiness because it determines the primary importer contract. Acceptance of these dispositions does not accept the remaining SAD-04 proposals or grant implementation GO.

Existing SAD-D-001–015 remain accepted. SAD-03's two closed findings stay closed: candidate evaluation does not require fictional operational ledger records, and a model failure cannot become evidence of a TC or business-rule defect.

## 4. First increment and retained product scope

**Scope accepted on 2026-09-27 (Europe/Warsaw).** In response to the walkthrough question covering the I-01 boundary and the division of later work, the Project Owner stated: "tak akceptuje zaproponowany zakres". That decision accepted the scope and delivery split below without granting implementation GO. The subsequent, separate acceptance of the technical choices is recorded in Section 5.

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

| Later delivery slice | Retained work and enabling condition |
| --- | --- |
| I-02 — Package readiness and review records | Defined CSV/explicit source bindings, core minimums, criterion-level qualification, run/ledger/history and inspection/export; concrete contracts and tests before enabling each path |
| I-03 — Functional test-design review | EP, BVA, decision tables and state transitions in bounded subincrements, with supplied/confirmed premises and human interpretation/disposition; no requirement that all four techniques apply to every TC |
| I-04 — Controlled local model contribution | Authorized synthetic candidate evaluation, task-specific qualification, gateway protections and measured resource/quality evidence; may be planned alongside I-03 but cannot bypass B-06/B-08 prerequisites |
| Later product acceptance / sealed readiness | Full selected MVP evidence and human acceptance; B-09 controls and ROLE-09 authorization separately precede any confidential use |

These are delivery slices within the accepted work packages, not additional SAD documents or promises of fixed dates. GUI and reviewing tests of AI/LLM systems remain parked.

## 5. Implementation decisions

| ID | Decision accepted on 2026-09-27 | Reason and scope |
| --- | --- | --- |
| SAD-D-016 — Bound the first implementation permission | Limit implementation permission, when granted through Section 14, to I-01 as defined in Section 4; retain later work in the allocation register. | Starts an end-to-end local path without disguising capture as substantive test review. |
| SAD-D-017 — Python CLI and explicit contract validation | Use CPython 3.13, argparse, sqlite3, uuid and hashlib; use jsonschema's Draft202012Validator for TDG-owned schemas and pytest for verification. Record exact interpreter/SQLite/dependency versions in an environment manifest and lock dependencies during setup. | Builds on the user's Python direction; one supported Windows x64 target first. Minor version 3.13 is selected for TDG, not inferred as installed on the user's machine. A version change needs an explicit compatibility decision. |
| SAD-D-018 — One local transactional store | SQLite, a single application writer, explicit transactions, foreign keys enabled, DELETE rollback journal and synchronous=FULL. Keep original bytes and projections in the same database. | Makes source, snapshot, receipt and capture outcome commit together; avoids a database/filesystem two-phase capture problem. Physical durability still requires verification on the target filesystem. |
| SAD-D-019 — Opaque identities and separate integrity | UUIDv4 text IDs generated by TDG; SHA-256 hex for exact-byte integrity; RFC 6901-style JSON Pointer within the identified original for JSON locators. | Source IDs remain independent; a digest is neither business identity nor evidence of truth/authorship. No content-addressed package deduplication. |
| SAD-D-020 — Strict control, tolerant supplied content | Implement RA-09's version 1.0 envelope; a local schema registry with remote retrieval denied; preserve all content values and deficiencies without coercion. | Rejects malformed control input without discarding capturable incomplete TC. Full schema/profile IDs are separate from package and behavior versions. |
| SAD-D-021 — Laboratory limits and unavailable-path enforcement | Apply Section 9's versioned limits, bounded parser worker, data/copy policy and explicit disabled capabilities. | No LLM endpoint, credentials, browser, renderer or network client is part of the I-01 processing path. Locality alone is not a confidentiality claim. |

All six decisions are **ACCEPTED**. On 2026-09-27 (Europe/Warsaw), the Project Owner accepted Section 5 in full: "tak, akceptuje paragraf 5 w całości". This accepts the design choices, including the technology selection; implementation GO remains subject to Section 14. The detailed contracts and controls in Sections 6–9 were subsequently accepted in separate walkthrough decisions. The accepted numeric limits are engineering containment settings, not statistical product-acceptance thresholds or claims of performance on an 8 GB GPU.

The official Python lifecycle, sqlite3 transaction documentation, jsonschema reference policy and Windows Job Objects documentation were consulted for these choices; see technical references below. The sources describe available mechanisms. Their correct integration remains implementation and test work.

## 6. Interchange and status contracts

**Accepted without changes on 2026-09-27 (Europe/Warsaw).** The Project Owner stated: "ok, akceptuje paragraf 6 bez uwag". This accepts Sections 6.1 and 6.2, including the input-preservation rules and the separate status axes; it does not grant implementation GO.

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

**Accepted without changes on 2026-09-27 (Europe/Warsaw).** The Project Owner stated: "ok, tu też nie mam uwag, akceptuję paragraf w całości" in response to the Section 7 walkthrough. This accepts Sections 7.1–7.3, including the transaction/retry boundary, explicit lineage, store compatibility and data location; implementation GO remains pending.

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

## 8. Terminal contract for the increment

**Accepted without changes on 2026-09-27 (Europe/Warsaw).** The Project Owner stated: "tak, nic tu lepszego nie wymyśle więc akceptuje w całości" in response to the Section 8 walkthrough. This accepts the command families, operator context, process exit codes and output conventions; implementation GO remains pending.

The accepted executable name is `tdg`, with `python -m tdg` as the equivalent development entry. The CLI is a thin adapter over CMP-01 services; tests can call the same services without subprocess-only coupling.

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

**Accepted without changes on 2026-09-27 (Europe/Warsaw).** The Project Owner stated: "tak, akceptuję" in response to the Section 9 walkthrough question covering the laboratory rules and numeric resource limits. This accepts the admission, containment, copy/log/retention rules and the proposed limit values as design settings. Runtime verification and implementation GO remain pending; acceptance does not establish measured performance or sealed readiness.

Admission requires an explicit public/synthetic classification and lab-development purpose from the operator context. Missing/unknown/confidential classification is refused before prohibited content processing. A discovered contradiction stops the affected path with a safe diagnostic. This does not claim a reliable automatic detector of confidential text; eligibility of the supplied development corpus remains human-controlled.

| Resource | Accepted I-01 bound / enforcement |
| --- | --- |
| Selected inputs | One native JSON file per import; regular local file only, no directory traversal/search, archive expansion, URL, UNC/network source or automatic link following |
| Raw input | 1 MiB; bounded read stops at limit plus one byte, before accepting a complete parse |
| JSON depth / node count | Maximum 32 nested containers, with the root object at depth 1; at most 20,000 JSON values, counting each container/scalar once and excluding object member names. Preflight and decoded inventory enforce the bounds without silently skipping a remainder |
| Individual text / numeric token | 64 KiB UTF-8 per decoded text value or member name; 128 characters per numeric token; exceedance is an explicit representation/limit failure |
| Candidate inventory | At most 200 native TC array entries and 200 basis array entries, counting deficient/malformed members too; these are capacity bounds, not business-scope or quality rules |
| Parse worker | One worker; 5 seconds wall time and 512 MiB committed memory. Windows Job Object limits are applied before releasing input to the worker; if required containment cannot be established, refuse processing |
| Controlled worker output | At most 8 MiB of framed projection data; parent validates shape, operation identity and size before persistence |
| Store / write waiting | Database main file capped at 512 MiB using page-count policy; write lock wait capped at 5 seconds. Check space for database/journal work; disk exhaustion causes safe failure, not unsafe truncation |
| Copies and logs | No separate raw-input temp files or automatic backups in I-01. SQLite journals remain in the managed directory. Routine diagnostics contain bounded metadata only; source/worker payloads are not debug-logged |

The parent bounds source acquisition and worker communication; the worker has no application database handle, arbitrary plugin invocation or source-discovery interface. Job Objects supply the selected time/resource containment mechanism, **not a complete OS sandbox or proof of zero egress**. The I-01 implementation contains no network-processing path or telemetry; the test environment observes attempted external calls. Full sealed egress/isolation evidence belongs to B-09 and cannot be inferred from this design.

Keep eligible synthetic/public originals, projections and receipts in the designated workspace until explicit authorized workspace disposal. No automatic age-based deletion or implicit promotion to backup/export is enabled. Workspace disposal and host-managed copies require an explicit local handling procedure; I-01 claims neither secure erasure nor recovery from hardware loss. Ordinary terminal display escapes control sequences, limits output and identifies truncation; no link/image is opened or rendered automatically.

These accepted limits must be implemented as a versioned policy and tested at below/at/above boundaries before the importer is enabled. Exact dependency versions, host OS build, CPU/RAM, filesystem, effective SQLite settings and observed resource behavior belong in the implementation environment record. A failed limit or mandatory audit/history write blocks the dependent operation; optional debug logging does not become a new gate.

## 10. Disposition of inherited open decisions

**Accepted without changes on 2026-09-27 (Europe/Warsaw).** The Project Owner replied: "Tak, akceptuję." to the walkthrough question about the Section 10 dispositions and deferral of the remaining decision scope. This accepts the I-01 treatment and the retained enabling conditions for later capabilities. Deferred parts remain open, the Section 3 correction closures remain pending, and no implementation GO is granted by this decision.

There are eight named decisions in SAD-02 and ten in SAD-03. Several overlap. The table records their accepted treatment for I-01 and the remaining scope that must be resolved before the corresponding later capability is enabled.

| Existing ID | Accepted I-01 disposition | Remainder / before which capability |
| --- | --- | --- |
| OD-SAD02-001 | SQLite and atomic BLOB/projection capture, Sections 5 and 7 | Later review/history/export transactions before I-02 |
| OD-SAD02-002 | UUIDv4, SHA-256 and source locators, Sections 5–7 | Additional model/event identities when introduced |
| OD-SAD02-003 | RA-09 envelope and local schema policy, Section 6 | Full review-export schemas before enabling export; F-002 must close |
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

**Accepted without changes on 2026-09-27 (Europe/Warsaw).** The Project Owner stated: "ok, akceptuje bez zmian" in response to the Section 11 walkthrough. This accepts the allocation of all 249 requirements and the distinction between partial and full evidence. The companion index records the same allocation decision and the subsequent, separate acceptance of Section 12's condition definitions. No requirement is thereby marked implemented or validated, and implementation GO remains pending.

The companion [allocation index][allocation] lists all 249 requirement IDs from the accepted trace ledger, their source documents, design-route group, work packages and whether an I-01 clause-level contribution is planned. It reuses existing REQ–VAL routes rather than duplicating the requirement text or generating 249 new tests.

| Requirement slice | Count | Primary design/work routing |
| --- | ---: | --- |
| RA-01 | 16 | SAD-01 authority boundaries; SAD-02 Section 9; SAD-04 Sections 8–9; B-01/B-04/B-07/B-09 |
| RA-02 | 36 | SAD-01 workflow; SAD-02 lifecycle; SAD-04 Sections 4 and 6–9; B-03–B-07 |
| RA-03 | 50 | SAD-02 source/identity; SAD-04 Sections 6–7; B-03/B-04 |
| RA-04 | 15 | SAD-01 planner; SAD-03 classification contributions; B-04; substantive classification deferred from I-01 |
| RA-05 | 22 | SAD-01 commit effects; SAD-02 records; SAD-03/SAD-04 corrected status axes; B-03/B-04/B-07 |
| RA-06 | 20 | SAD-01 assessment service and SAD-03 contribution boundary; B-02/B-05; detailed technique algorithms still required |
| RA-07 | 20 | SAD-03 gateway, qualification and evaluation separation; B-06/B-08; model invocation disabled in I-01 |
| RA-08 | 24 | SAD-03 protection; SAD-04 laboratory controls; B-01/B-03/B-06/B-07/B-09 |
| RA-09 | 24 | SAD-02 contracts corrected by Section 6; native intake in I-01, CSV/export later; B-03/B-07 |
| RA-10 | 22 | SAD-03 evaluation independence; SAD-04 Sections 12–14; B-02/B-08/B-10 |
| Total | 249 | Routing inventory, not implemented or fully detailed coverage |

Every I-01 selection in that index means **partial contribution only**. For example, implementing source retention does not satisfy an entire requirement that also constrains future review/export behavior. Requirements about unimplemented review/model paths remain allocated, not passed. All 169 VAL remain authoritative; their future evidence may span multiple increments. A numeric 249/249 routing result does not establish clause-level architecture completeness, product quality or 249 implemented requirements.

## 12. STLC allocation and first-increment test conditions

**Accepted without changes on 2026-09-27 (Europe/Warsaw).** The Project Owner stated: "ok, akceptuje bez uwag" in response to the Section 12 walkthrough. This accepts the STLC allocation and all 16 conditions, TCND-I01-01–16, as the test plan for I-01. Detailed executable tests, execution evidence and implementation GO remain pending; condition acceptance does not mark any requirement implemented or validated.

Static testing continues during design and implementation. Before product tests are written, the author and Owner resolve the two findings and approve the selected contracts/limits. Fixtures are synthetic customer-creation development material, with one explicit rule/version per family. The previously discussed discount example is exposed development material; it cannot later be described as unseen acceptance evidence.

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

Expected outcomes are defined from these contracts before observing implementation results. Use meaningful unit tests for syntax/projection/identity decisions, integration tests with a real temporary SQLite store and injected commit faults, and a small CLI smoke path on the supported Windows host. Code-level/integration tests of TDG are separate from the system-level black-box TC that TDG will eventually review. No line-coverage percentage alone is an acceptance gate.

## 13. Executable work breakdown and resource estimate

**Accepted with an effort-estimate reservation on 2026-09-27 (Europe/Warsaw).** The Project Owner stated: "akceptuje paragraf 13 z zastrzezeniem ze nakład prac szacowany na 40-60 godzin uważam za mocno szacunkowy, podejrzewam ze same testy tyle zajmą." The work breakdown is accepted. The original 40–62-hour total and its component estimates remain very uncertain, unvalidated planning hypotheses, not an approved budget, effort ceiling or delivery commitment. The Owner's concern that testing alone could require comparable effort is retained as an underestimation risk, not adopted as a new testing estimate or added mechanically to the original total.

All tasks below await implementation GO. The sole human is accountable for understanding changes, decisions and evidence; AI assistance may draft code/tests but is not an independent reviewer or extra staffing capacity. Role-specific authority remains explicit when a later task needs it.

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

Re-estimate during W02 using the detailed test inventory and update after W03/W04 using observed work. Identify effort for fixture/oracle preparation, test implementation and fault injection, execution/diagnosis, defect correction, retest/regression and completion evidence. Testing is already included across the original work items; separate it transparently when revising the forecast to avoid double counting. The 16 accepted conditions can expand into many concrete tests, and a condition count alone is not an effort estimate. No replacement total is asserted before that breakdown and evidence exist.

The reference remains approximately five flexible hours per week. It does not establish a fixed schedule. Completing the agreed scope and required evidence governs increment acceptance; reaching the original hour range does not justify reducing tests or relaxing criteria. Expose deviations and revise the forecast as evidence develops. The earlier 16–32-hour estimate concerned B-01 design, not this coding increment; actual past human effort is not known and is not reconstructed from chat timestamps.

Development-time package installation and tooling setup are explicit setup operations, separate from processing Review Packages. No inference hardware, cloud subscription or external model is required for I-01. Actual host resources and permissions are recorded during setup; no performance result is inferred from GPU memory size.

## 14. Author check, walkthrough and proposed implementation gate

### 14.1 Preparation evidence

The author checked local source references, requirement IDs in the I-01 conditions, the complete 249-ID allocation inventory, table consistency, numeric effort totals and the two cross-contract findings. These are document checks. Runtime containment, fidelity, durability and usability remain unexecuted obligations.

The walkthrough should start with Section 3's two corrections, then accept or revise the I-01 boundary in Section 4, proposed decisions in Section 5, concrete contracts/limits in Sections 6–9, deferred work in Section 10, evidence/STLC in Sections 11–12 and effort/gate in Sections 13–14. Accepting an early section does not implicitly accept the later ones.

Walkthrough progress on 2026-09-27: Section 3's two corrective dispositions and Sections 4–12 are accepted by the Project Owner. Section 13 is accepted with the explicit effort-estimate reservation recorded there. Section 14 is the next review item. No acceptance of Sections 1–2 or 14 is inferred from these decisions; both finding closures and the final implementation gate remain pending.

### 14.2 Evidence required before a coding GO

- Owner accepts the I-01 scope, SAD-D-016–021, concrete limits, work breakdown and flexible resource assumption, with Section 13's explicit underestimation risk and re-estimation approach retained. The original 40–62 hours is not an approved budget or acceptance ceiling.
- Both SR-SAD04 findings are dispositioned and their corrections verified. Accepted correction notices identify the governing SAD-04 clauses in the historical SAD-02 document before closure publication.
- Each enabled I-01 operation has a defined input, trusted context, durable effect, failure outcome and test condition; no unresolved safety/contract blocker remains for those operations.
- The allocation index retains every accepted requirement and identifies partial/deferred delivery; no requirement is marked fulfilled merely because its ID is routed.
- Owner accepts the static-review record and the specific permission boundary: implementation of I-01 with synthetic/public development material only.

The proposed final question is: **Accept the corrected SAD-04 baseline and review record, retaining Section 13's effort-estimate reservation, close B-01 for the selected implementation boundary, and grant GO to implement I-01?** No such decision has been made by this v0.1 document. A rejection or requested correction is recorded and resolved; it does not silently turn into permission.

### 14.3 I-01 completion and subsequent gates

Completion requires demonstrated source/identity/commit invariants, honest receipts and unavailable-path behavior, all applicable conditions above executed with recorded outcomes, and no unresolved defect that invalidates the selected capture/protection boundary. Unrun required conditions and failures prevent a completion claim; other residual defects need an attributable Owner disposition. Performance observations are reported for the actual environment rather than converted into invented universal thresholds.

The Owner then decides increment acceptance and the next bounded implementation scope. Human oracle/protocol/criteria approvals precede decision-bearing model qualification or product acceptance; explicit ROLE-09 readiness precedes confidential use. These are retained SDLC/STLC gates, not a requirement to invent a new SAD document for each coding task.

## References

[gate]: ../requirements-analysis/ra-10/test-design-gatekeeper-requirements-analysis-readiness-v0.2.md
[sad01]: test-design-gatekeeper-sad-01-components-review-flow-v0.1.md
[sad02]: test-design-gatekeeper-sad-02-data-identity-contracts-v0.1.md
[sad03]: test-design-gatekeeper-sad-03-model-protection-v0.3.md
[review03]: ../reviews/test-design-gatekeeper-sad-03-review-record-v0.2.md
[ra03]: ../requirements-analysis/ra-10/test-design-gatekeeper-ra-03-review-package-content-provenance-validation-v0.4.md
[ra05]: ../requirements-analysis/ra-05/test-design-gatekeeper-ra-05-findings-dispositions-persistence-v0.2.md
[ra08]: ../requirements-analysis/ra-08/test-design-gatekeeper-ra-08-confidentiality-security-privacy-v0.2.md
[ra09]: ../requirements-analysis/ra-09/test-design-gatekeeper-ra-09-data-representations-import-export-contracts-v0.2.md
[trace]: ../requirements-analysis/ra-10/test-design-gatekeeper-requirements-analysis-traceability-audit-v0.1.json
[allocation]: test-design-gatekeeper-sad-04-requirement-allocation-v0.1.json

Technical references consulted on 2026-09-27; they support mechanism selection, not a TDG verification claim:

- [Python version lifecycle](https://devguide.python.org/versions/): supported-runtime planning.
- [Python 3.13 sqlite3](https://docs.python.org/3.13/library/sqlite3.html): explicit connection/transaction and backup interfaces.
- [Python 3.13 json](https://docs.python.org/3.13/library/json.html): resource cautions, duplicate-name and non-finite handling require deliberate application policy.
- [jsonschema validation](https://python-jsonschema.readthedocs.io/en/stable/validate/) and [reference retrieval](https://python-jsonschema.readthedocs.io/en/stable/referencing/): local validator/registry configuration; no automatic remote schema retrieval in TDG.
- [Windows Job Objects](https://learn.microsoft.com/en-us/windows/win32/procthread/job-objects): resource/process containment primitive; not by itself a complete security sandbox.
