# Test Design Gatekeeper

## RA-09 — Data Representations and Import/Export Contracts

| Field | Value |
| --- | --- |
| Document version and date | 0.1 — 2026-09-20 |
| SDLC phase | Requirements Analysis |
| Status | DRAFT FOR OWNER REVIEW |
| Entry authorization | PG-RA08-001, recorded in SR-RA08-001 v0.2 — GO to RA-09 |
| Effective upstream baseline | Charter v0.4; RA-01 v0.3; RA-02 v0.3; RA-03 v0.3; RA-04 v0.2; RA-05 v0.2; RA-06 v0.2; RA-07 v0.2; RA-08 v0.2, read with their acceptance and closure records |
| Decision authority | Project Owner for requirements, open decisions, and the SDLC gate; existing operational authorities remain unchanged |
| Requirements | 24 MUST statements — all PROPOSED |
| Validation obligations | 16 proposed obligations; no product tests executed |
| Open decisions | OD-RA09-001 through OD-RA09-004 — recommendations awaiting Owner decision |
| Static-review state | Author checks only; formal review has not started |
| RA-10 gate | NOT GRANTED |

## 1. Purpose, baseline, and conventions

RA-09 specifies how supplied material becomes an identifiable Review Package and how retained review results can be exported without losing their evidence, limitations, or human decision history. It separates readable file syntax, trustworthy capture, minimum package admissibility, and substantive assessment. A file can be syntactically correct while containing a deficient TC; a successfully captured package can still be inadmissible for review.

The governing sources are the [Charter][charter] and [RA-01][ra01] through [RA-08][ra08], including [RA-02][ra02], [RA-03][ra03], [RA-04][ra04], [RA-05][ra05], [RA-06][ra06], and [RA-07][ra07]. Their accepted status is established through [PG-RA03-001][gate03] and the closure records for [RA-04][gate04], [RA-05][gate05], [RA-06][gate06], [RA-07][gate07], and [RA-08 / PG-RA08-001][gate08]. Repository references pin commit `ff1cd6379717d59da09087120609d41fc7309668`. Historical pending labels in preserved wording snapshots do not override the subsequent closure records.

**Shall** describes a proposed obligation in this draft and becomes binding only when the Project Owner accepts that requirement. **MUST** denotes proposed priority, not an already granted acceptance. Sections 2–8 elaborate the proposed requirements in Section 9. Examples illustrate those rules; they do not supply new business requirements or constitute executed tests.

The Charter already selects a vendor-independent JSON representation, a defined CSV import format, and explicit local field mapping. RA-09 makes those choices concrete at the requirements level. It does not select a database, programming language, parser library, CLI, or UI. Executable schemas and implementation artifacts will realize the accepted contracts during Solution Design and implementation. Any design change to their accepted meaning requires change control.

The scope remains pre-review of system-level, functional, black-box TC, using EP, BVA, decision tables, and state transitions where evidence supports them. This document adds no live Jira connection, external source retrieval, automatic TC repair, formal testware approval, or claim of official ISTQB conformity.

## 2. Supported boundaries and document kinds

### 2.1 Local input and output surfaces

| Surface | Proposed MVP contract | Boundary |
| --- | --- | --- |
| Native Review Package submission | UTF-8 JSON containing a declared scope, supplied basis, TC, and other supplied content; Section 3 | One file may contain both substantive basis and TC and satisfy the supplied-artifact minimum |
| TC file import | The defined `tdg-tc-csv` profile, version `1`, selected with its package context; Section 5 | CSV supplies TC content; it does not replace the required scope or test basis |
| Customized source layout | An explicitly selected, identified local capture mapping into the same logical model | No automatic claim to support every Jira/Xray/Zephyr export or customer customization |
| Other selected local material | Exact source inventory and, where an identified supported extraction exists, addressable content | An opaque attachment is visible but does not become readable basis merely because it was attached |
| Machine-readable result export | JSON `review_export`; Section 7 | Selected retained records and explicit evidence/omission boundaries; no automatic source mutation |
| Human-readable result export | Markdown projection of the same selected export | Preserves meaning and limitations; rendered supplied content remains inert |

The minimum combined-file path is a native JSON submission with `tc_sources` entries bound to explicitly selected CSV files. The JSON can also contain native TC. All selected sources are inventoried. These are contract surfaces, not requirements for a particular upload screen or command syntax.

A Jira-shaped file is assessed by its supplied content and explicit mapping. TDG does not have to establish that Jira actually produced it. External issue keys, URLs, document paths, and filenames remain references unless their content was separately and explicitly supplied under the permitted intake process.

### 2.2 Distinct JSON document kinds

Each JSON contract has a top-level object with `document_type`, `contract_version`, and `content`. The proposed initial contract version is the string `"1.0"`. This is a data-contract version, independent of this document's v0.1 version. Control-envelope fields must be recognizable and well typed before routing; arbitrary top-level control additions are not silently accepted. Unknown content fields follow the preservation rules in Sections 3 and 6.

| `document_type` | Producer and meaning | Authority limit |
| --- | --- | --- |
| `review_package_input` | A supplied declaration and content manifest | Does not create trusted identity, a stored package version, accepted findings, qualification, or security authorization |
| `review_package_snapshot` | TDG's coherent captured package representation: exact-source inventory, declarations, projection, and capture metadata | Represents captured content; excludes substantive assessment conclusions |
| `import_receipt` | TDG's intake outcome and issues, with a package reference only after durable capture | Capture success does not mean minimum admissibility or successful review |
| `review_export` | TDG's selected retained result, context, evidence references, and human history | Read-only interchange/reporting; not a backup-restoration or trusted-decision import mechanism |

These are logical document contracts, not a requirement to write four separate files per operation. The snapshot can be stored using the later chosen local persistence design. An import receipt must be inspectable; a dedicated UI is not implied.

Submitting a `review_export` where `review_package_input` is expected does not restore its package/run identities or human decisions. If such a file is deliberately supplied as supporting evidence through an allowed path, it remains untrusted supplied material. General history migration and backup restoration through this import contract are outside MVP.

### 2.3 Three semantic layers remain separate

| Layer | Information owned by the layer | Prohibited promotion |
| --- | --- | --- |
| Submission context | Current operator and acting role, profile, approved classification/purpose, selected input bindings, operation identity and requested action | A field inside a supplied file cannot overwrite this context or authorize processing |
| Immutable package snapshot | Original content instances, attributable supplied declarations, identified capture projection, provenance, local identities, scope membership and lineage | Mechanical mapping cannot introduce inferred business rules or LLM verdicts as supplied facts |
| Derived assessment and result | Qualification, interpretation, technique models/mappings, evidence sufficiency, ledger outcomes, findings and human decisions, tied to an identified run | Findings, exports, or accepted suggestions cannot edit the package snapshot |

ROLE-01 operates the intake, ROLE-02 controls scope, ROLE-03 accepts accountability for and repairs TC, ROLE-04 confirms business interpretations, and ROLE-05 dispositions findings. Administrative, qualification, security, and Owner authorities retain their [RA-01 definitions][ra01]. Roles can be combined with attributable acting-role context. A source field that names a role is a declaration to check, not an authorization grant.

## 3. Canonical JSON and the captured logical model

### 3.1 Proposed native input fields

The following vocabulary defines the initial logical contract. Content fields can be absent or deficient in a captured candidate: core-minimum and assessment checks determine the consequence. In particular, the input envelope does not demand a complete editorial TC template merely to preserve submitted testware. Incorrectly typed content is retained as a raw, located value with an issue rather than coerced into the expected type.

| Location within `content` | Intended representation | Meaning and deficiency handling |
| --- | --- | --- |
| `scope` | Object with `description` text; optional supplied `source_id` and `notes` | Description identifies target context, one feature/small process, and included behavior. The applicable ROLE-02 declaration/decision must be attributable. Presence of an empty object is insufficient |
| `basis_elements` | Ordered array of objects with `text`; optional `source_id`, `title`, `external_refs`, and `provenance` | Substantive supplied rules or justified experience-based basis. Each projected element obtains a source artifact and locator. Links alone are not substantive basis |
| `test_cases` | Ordered array of TC objects using Section 3.2 | Native TC; missing fields and malformed members remain identifiable in the captured inventory |
| `case_defaults` | Optional object containing `origin` and/or `accountability` declarations | Applies only to native TC whose corresponding field is absent, under Section 4.2; it does not silently extend to separate CSV sources |
| `tc_sources` | Ordered array of objects with `binding_ref`, `profile_id`, `profile_version`; optional `case_defaults` scoped to that source | Each binding resolves only to an explicitly selected input in the current operation. The declared profile must be available and approved locally |
| `supporting_sources` | Ordered array of objects with `binding_ref`, optional purpose/label/provenance | Other explicitly selected material. Supported parsing/extraction must be separately identified; attachments can remain opaque |
| `notes`, `risks`, `supplementary_content` | Optional supplied text or JSON content | Preserved with provenance; not silently promoted to authoritative business rules |

The operation records the actor's attributable declarations and selected scope decision through the existing authority workflow. It can reference declarations in the input; the presence of those declarations does not bypass the workflow. All native elements belong to the one declared package scope, with that containment recorded. Conflicting explicit source membership is preserved and reported, not overwritten.

`binding_ref` is a label in the operation's selected-input inventory. It is not a filesystem path instruction or a URL to retrieve. Missing or ambiguous bindings produce visible issues; TDG never searches for a matching file. If all actually selected originals can be captured faithfully, a manifest's unresolved claim about an additional source may be retained as an unresolved reference. Failure to read an actually selected required content instance is a different problem: TDG cannot claim a faithful snapshot of that requested inventory.

### 3.2 TC content fields

| Field or group | Intended representation | Contract rule |
| --- | --- | --- |
| `source_id` | String or explicit null | Optional external identity; internal identity is separate. Preserve missing, duplicated, or deficient values |
| `title`, `summary`, `objective`, `scenario` | Text fields | At least one non-empty value is needed for recognizability, together with non-title behavioral content; no single field name is compulsory |
| `description` | Text | Can contain behavioral content or expectations; TDG does not require moving them into a preferred template |
| `preconditions`, `postconditions` | Text or ordered text array | Preserve the author's sequence and expression; preconditions alone do not establish a recognizable TC |
| `steps` | Narrative text or ordered array of objects containing `action`, `data`, and/or `expected_result` | Preserve step order, supplied numbering if present, nested expectations, and missing step dimensions; do not invent executable actions |
| `test_data` | Text or JSON value | Preserve values and structure without execution or business interpretation during capture |
| `expected_result` | Text | Optional at capture; missing expectations remain visible and limit dependent assessment. Expectations can instead be supplied in steps or narrative |
| `origin` | Text declaration | Map only as specified in Section 4.2; preserve original wording and unresolved meaning |
| `accountability` | Object with `actor_ref` and `accepted` | `actor_ref` is a string; `accepted` is a Boolean declaration. Positive eligibility requires an attributable, applicable ROLE-03 acceptance, not the Boolean alone |
| `basis_refs` | Ordered array of strings referring to supplied basis `source_id` values | Optional direct links. Resolve only unambiguous matches within this package; retain unresolved/ambiguous links |
| `test_level`, `test_type`, `design_basis`, `execution_mode`, `target_role`, `environment` | Independent supplied text or ordered text-array declarations | These are separate axes/context, not classification verdicts. Preserve conflicting or unknown labels |
| `external_refs`, `provenance`, other supplied content | Located supplied metadata/content | Source assertions remain assertions; unmapped content remains available and its assessment effect visible |

Explicit null is preserved as null in any content field, with its deficiency assessed separately; it is not substituted for a missing field. An ID/title/link-only record is retained but does not satisfy the recognizable-case minimum. A TC with a title and genuine actions but no expected result can be recognizable while remaining ungradable for expected-result alignment. Those are inherited RA-03 meanings, not JSON-schema decisions.

### 3.3 Source fidelity, presence, and mapping state

Exact supplied bytes are retained separately from the capture projection, within the permitted security and retention policy. JSON objects use the syntax defined by [RFC 8259][rfc8259]. TDG's proposed native profile requires UTF-8 without a leading BOM, rejects duplicate object member names before any last-value-wins materialization, and rejects non-JSON constructs such as comments, trailing commas, or non-finite number tokens. Rejecting duplicate names is a stricter TDG interoperability rule, not a claim that the RFC mandates rejection.

For every assessment-relevant projected field, capture must preserve its source locator, raw value/reference, capture mapping identity, and a distinguishable presence condition:

| Presence condition | Meaning |
| --- | --- |
| `ABSENT` | No field/column was supplied at the applicable location |
| `NULL` | JSON null was explicitly supplied; CSV has no implicit null token |
| `EMPTY` | An explicitly empty string or collection was supplied |
| `WHITESPACE_ONLY` | A string contains only whitespace; original characters remain preserved |
| `VALUE` | A value of the intended representation is present |
| `TYPE_MISMATCH` | A supplied non-null value does not fit the field's intended representation; raw content remains located |

Presence checks use this precedence: absent field, explicit null, type mismatch, then empty, whitespace-only, or populated value of the intended type. Thus an empty array supplied as a text-only title is `TYPE_MISMATCH`, not `EMPTY`. Presence is separate from mapping state: `MAPPED`, `UNMAPPED`, or `CONFLICTING`. A supplied origin value of `UNKNOWN` is not the same observation as an unrecognized phrase that remains `UNMAPPED`. The later schema may encode these distinctions through a common field record or equivalent typed structures, but cannot erase them.

Capture does not silently trim strings, case-fold identifiers, normalize Unicode, convert text to dates/numbers, or round supplied numeric values. Identifiers remain strings, including leading zeros. Array and TC/step order are preserved. JSON object-member order does not imply business precedence. If a supported numeric representation cannot be retained without loss, its original token remains available and the affected projection is explicitly limited; a rounded value is not presented as the source. Source bytes preserve lexical distinctions beyond logical JSON value equivalence.

Unknown content fields are retained with location and mapping status. If malformed structure prevents safe field projection, retain the relevant raw subtree or opaque artifact and expose the affected boundary. A projection must not claim schema conformance while hiding discarded or mistyped source content.

### 3.4 Versioned local schemas

The proposed schema dialect is [JSON Schema Draft 2020-12][schema-core]. Contract kind/version selects an explicitly installed, identified local schema and mapping profile. Unknown or unsupported versions are not interpreted using whichever schema happens to be newest. A primary input whose envelope cannot be routed safely is rejected from that native import path; any permitted raw retention remains an intake record, not a falsely conforming package.

Schema identifiers and references resolve only through the approved local registry. A supplied `$schema`, `$ref`, URI, or similar field cannot trigger a download or register a validator. Schema validation checks structural properties; role authority, cross-record references, minimum admissibility, and business sufficiency require their own checks. The implementation must explicitly configure and verify any required format assertions: the 2020-12 validation specification distinguishes format annotation from assertion, so using a `format` keyword alone does not establish enforcement. [Validation specification][schema-validation]

## 4. Identity, provenance, origin, and locators

### 4.1 Identity and evidence references

System-generated package-version, lineage, artifact, item, run, and operation identities remain distinct from supplied keys. An external `source_id` collision does not merge records. Equal steps, titles, preconditions, complete TC text, or source hashes do not prove that two cases or submissions have the same identity. Independent native array members and CSV records obtain independent internal item identities even when their content is identical.

Every captured artifact has an internal identity, safe human-readable label, integrity identity, capture provenance, and retained-content availability. Internal artifact references do not require exposing host absolute paths. A digest establishes content integrity/equality for its declared purpose, not authorship, business truth, permission, or semantic equivalence.

| Source representation | Locator contract |
| --- | --- |
| JSON | Artifact identity plus a JSON Pointer into that exact original JSON instance. Array indices are zero based; `/` and `~` in member names are escaped as `~1` and `~0` respectively |
| CSV | Artifact identity plus one-based logical data-record ordinal, excluding the header, and column name with one-based ordinal where distinguishable. A quoted multiline field remains part of one logical record |
| Opaque/whole artifact | Explicit whole-artifact marker; no invented page, cell, or field locator |
| Derived projection | Separate projection locator and mapping provenance that lead back to the original source locator; never relabel a projection location as an original location |

The JSON locator syntax follows [RFC 6901][rfc6901]; the plain pointer and artifact identity are sufficient without a retrievable external URI. A CSV physical line span can supplement, but cannot replace, logical-record identity. If ambiguity prevents a precise column locator, use the smallest trustworthy record/artifact boundary and say why.

Cross-record evidence references identify the package version and internal target, plus the source locator when applicable. Optional direct TC-to-basis links preserve their supplied target strings. Missing or duplicated basis source keys leave a link unresolved/ambiguous; they do not authorize a guessed match or erase independent TC. Each evidence item retains its RA-03 provenance class: supplied declaration, supplied source metadata, system observation, human confirmation, or derived inference.

### 4.2 Origin and accountable human adoption

The proposed canonical codes name the five accepted origin meanings; they do not replace the source declaration:

| Code | RA-03 meaning | Can contribute to the positive minimum? |
| --- | --- | --- |
| `HUMAN_AUTHORED` | Human-authored testware | Yes, with applicable attributable ROLE-03 accountability and the other minimum conditions |
| `HUMAN_CONTROLLED_AI_ASSISTED` | Human-controlled testware developed with AI assistance | Yes, under the same accountability and content conditions |
| `WITHOUT_ACCOUNTABLE_ADOPTION` | Generated or supplied from another process without accountable human adoption | No |
| `OTHER` | Explicitly declared other origin | No |
| `UNKNOWN` | Explicitly declared unknown origin | No |

A versioned, explicitly selected mapping may map agreed literal source values to these codes. A free-text declaration such as “Napisane przez QA Engineera w celu optymalizacji struktury i wyliczeń matematycznych” remains preserved but `UNMAPPED` unless its meaning has been resolved through the permitted human declaration/mapping process. TDG must not infer authorship, AI involvement, or human adoption from writing style, job title, or fluent wording.

Containing-set defaults are explicit declarations with a recorded scope. A native `case_defaults` applies only to native `test_cases`; a `tc_sources` entry's defaults apply only to that identified source's records. A default fills an absent origin or absent accountability field only. Explicit null, empty, unknown, negative, malformed, or conflicting item declarations remain visible and are not upgraded. Conflicting declarations are reported even where a mechanical mapping can identify the item-level value.

One qualifying accountable case can satisfy the package's positive-case minimum; it does not confer eligibility on every other case. Accountability and origin remain separate. A human correction or adoption that changes a captured declaration produces a new package version. No declaration grants the named person a role that they do not hold in the applicable operating profile.

## 5. Defined CSV profile and explicit source mapping

### 5.1 `tdg-tc-csv`, version `1`

The baseline CSV profile uses comma separators, double-quoted fields, doubled double quotes within quoted fields, and quoting for fields containing commas or line breaks. These conventions follow [RFC 4180][rfc4180]. The profile explicitly accepts CRLF or LF record separators, permits an optional final record separator, requires UTF-8, and accepts one leading UTF-8 BOM on input while recording its presence. These profile choices are not claims that RFC 4180 mandates all of them. Exported JSON/Markdown uses UTF-8 without a BOM.

| Aspect | Proposed contract |
| --- | --- |
| Header | Required; column names are non-empty, case-sensitive, and unique. No silent trimming or alias guessing |
| Known columns | `source_id`, `title`, `summary`, `objective`, `scenario`, `description`, `preconditions`, `steps`, `test_data`, `expected_result`, `postconditions`, `origin`, `accountable_actor_ref`, `accountability_accepted`, `basis_refs`, `test_level`, `test_type`, `design_basis`, `execution_mode`, `target_role`, `environment` |
| Optional columns | Individual TC columns may be absent. The file can be parsed and captured while its rows fail recognizability or another minimum condition |
| Record unit | One logical data record represents one candidate TC. Repeated source IDs or similar text do not join records |
| Field counts | Each well-formed data record has the header's number of fields. A ragged record is retained with an issue; no padding, truncation, or shifting values into other columns |
| Narrative fields | Decoded cell text is preserved. A multiline `steps` cell remains narrative text; line breaks or digits do not implicitly create structured steps |
| Values | No implicit number/date conversion, formula evaluation, or special `NULL` text token. Empty cells mean `EMPTY`; a missing column means `ABSENT` |
| `accountability_accepted` | Only the exact non-empty literals `true` and `false` map to the corresponding Boolean declaration; other values remain unresolved with their raw text |
| `basis_refs` | A non-empty cell contains a JSON array of strings; blank means `EMPTY`. Decode explicitly under this profile and retain the original cell. Invalid inner JSON affects this field, not CSV framing |
| Other columns | Retain header, ordinal, and raw cell values as unmapped content; expose any dependent review limitation |

The two accountability columns map into one accountability declaration. That declaration is absent only if both columns are absent. If either column exists, preserve the supplied object and each subfield's absence/emptiness; a containing-set default cannot fill or replace that partial declaration. An absent `origin` column can receive its explicit source-scoped default, whereas an empty origin cell cannot.

A record containing a quoted line break spans multiple physical lines but still represents one TC. A completely blank physical record outside a quoted field is not silently skipped: account for it as an empty/deficient logical record under the declared parser behavior. A single permitted final separator does not create a phantom extra TC. These cases require explicit fixtures in later test design.

Ambiguous duplicate headers prevent a unique column mapping. Unterminated quotes or other unreliable framing prevent reliable record boundaries. Preserve the original affected source as opaque where capture is permitted; do not pretend that guessed rows or a parsed prefix represent the complete file. If framing is reliable and just one row has a wrong field count, retain that raw record and distinguish it from safely projected independent rows.

A semicolon-separated or otherwise customized file is not auto-detected as a different profile. A comma parser might see it as an unmapped single column; that is not successful TC normalization. Supporting a different layout requires an explicit identified profile/mapping, not a hidden heuristic.

### 5.2 Capture mapping contract

An approved capture mapping identifies its version, supported source layout, source paths/columns, target fields, literal aliases, explicit defaults and their scopes, record/grouping and ordering rules, locator mapping, resource bounds, and treatment of unsupported content. The canonical CSV profile does not group multiple rows into one TC; a future customized mapping can do so only through explicit validated rules and traceable source membership.

Mapping is a mechanical capture transformation. LLM-proposed field correspondences may be offered for human consideration under an allowed RA-07 task, but they cannot install a mapping, manufacture missing fields, or confirm a semantic interpretation. Capture mapping changes followed by recapture create a new package version. Changes to semantic mapping used only in assessment create a new run on the same captured package. The two operations must remain distinguishable.

No universal Jira adapter is required. A source file with Jira-like fields needs only a supported explicit mapping and supplied content; provenance assertions about Jira remain source assertions.

## 6. Intake outcomes, errors, and durable capture

### 6.1 Ordered checks and bounded consequences

The RA-03 validation order remains binding after acceptance of these contracts: permitted context; trustworthy inventory/capture; identified immutable candidate; core minimum; relationships/provenance/coherence; dimension-specific sufficiency. A later check cannot excuse an earlier failed safety prerequisite.

| Condition | Required intake consequence |
| --- | --- |
| Disallowed or unresolved data/profile permission | Reject before prohibited processing; retain only policy-permitted rejection metadata |
| Unsupported/malformed primary control envelope or contract version | Reject the native import path without guessing a schema; raw intake retention only where separately permitted |
| Actually selected originals cannot be captured faithfully | Do not claim a coherent package snapshot. Record the bounded rejection/failure and any permitted diagnostic context |
| Supported envelope and trustworthy capture, but missing scope, substantive basis, recognizable TC, or positive accountable TC | Preserve a candidate and explicit core-minimum failure; block substantive review as required by RA-03 |
| Deficient field, unresolved link, unknown origin, or opaque selected attachment | Preserve exact source/inventory and issue; limit the narrowest defensible dependent item, relationship, or dimension. Check whether the package minimum still holds |
| Non-separable conflicting basis or provenance | Preserve conflicting evidence; no guessed precedence. Apply package-wide blocking when an independent trustworthy subset cannot be established |
| Independent safe subset exists | Preserve the whole requested inventory and explicit exclusions; allow only the justified independent processing under RA-03/RA-04 |
| Parser/resource/security limit reached | Stop the affected operation or projection safely; disclose the exact unprocessed boundary without silently truncating or claiming complete inspection |

Trustworthy capture is not a requirement to accept malformed or unauthorized control structures. Conversely, missing expected results, optional direct links, or source IDs are not reasons to reject otherwise capturable content as invalid file syntax. All RA-03 IS-01 through IS-11 outcomes remain applicable; these contracts do not collapse them into one `valid` flag.

### 6.2 Import receipt and issue records

| Receipt field | Meaning |
| --- | --- |
| `operation_id`, `contract_version`, capture profile/mapping identity, actor/time context | Identify the attempted operation and actual processing configuration, subject to permitted disclosure |
| `capture_outcome` | `REJECTED`: a prerequisite prevented capture; `FAILED`: an attempted capture did not produce a coherent durable snapshot; `CAPTURED`: a coherent snapshot was durably retained |
| `package_version_ref` | Present only for `CAPTURED`; never an unsaved preview identifier presented as a committed package |
| `minimum_check` | `NOT_EVALUATED`, `MET`, or `NOT_MET`, with reasons and check version; `MET` is neither scope qualification nor assessment sufficiency |
| `input_inventory` | Accounts for every selected input and its capture/projection outcome; protected detail appears only where permitted |
| `issues` | Stable issue records, including explicit affected scope and human action; an empty list is distinguishable from an unavailable/not-produced list |

For `REJECTED` or `FAILED`, no committed package is claimed and `minimum_check` remains `NOT_EVALUATED`. A durable candidate may be `CAPTURED` and `NOT_MET`. If processing stops after durable capture but before the minimum check is completed, report `CAPTURED` with `NOT_EVALUATED` and the reason; do not fabricate a check result. Cancellation before durable capture is a failed attempt with an explicit cancellation reason; it does not create a partially committed package. These are intake outcomes, separate from RA-05 review-run states.

Each issue contains its identity, processing stage, stable machine code, submission/package context as available, target and source locator where safely known, observed problem, evidence reference, affected claim/work, effect scope, applicable rule/mapping version, derivation/uncertainty where relevant, and suggested human action/acting role. Safe explanatory text can be localized; clients must not derive control behavior by parsing its wording.

Proposed code families include `UNSUPPORTED_CONTRACT`, `JSON_SYNTAX`, `JSON_DUPLICATE_MEMBER`, `UNBOUND_SOURCE`, `CSV_HEADER_AMBIGUOUS`, `CSV_RECORD_SHAPE`, `FIELD_UNMAPPED`, `ORIGIN_UNMAPPED`, `REFERENCE_AMBIGUOUS`, `LIMIT_EXCEEDED`, `POLICY_DENIED`, and `PERSISTENCE_FAILED`. The executable code catalog will be versioned with the contract; these examples do not replace the required issue fields or the full RA-03 rule set. Effects distinguish capture, package review, item, relationship, dimension, and informational scope; a code alone is not a universal severity or blanket-block rule.

Routine errors must not echo protected TC text, credentials, full host paths, or raw model payloads. Protected source evidence can remain available through authorized record access. If permission forbids revealing even an input identity, the diagnostic uses a permitted bounded reference rather than leaking it to satisfy the inventory field.

### 6.3 Atomicity, retries, and limits

Capture success means a coherent durable logical snapshot, its originals or permitted integrity-identifiable retained instances, projection, identities, provenance, and receipt linkage can be inspected consistently. No partially saved candidate is labelled `CAPTURED`. A safely captured opaque source differs from an unread or silently missing source. Failed staging and temporary copies follow the RA-08 lifecycle.

Retrying the same identified operation with the same submitted content and configuration returns or completes that operation without duplicate committed effects, subject to current authorization. Reusing its identity with different content/configuration is a visible conflict. A new deliberate submission remains a separately attributable operation/package; byte equality does not merge it with an older version. Failure, cancellation, or restart cannot fabricate successful capture or reopen a terminal review run for hidden reassessment.

Before a parser/profile is enabled, its supported sizes, nesting, field/record counts, processing time, and memory/storage limits must be identified and enforced. Concrete values are a later design/configuration allocation, not guessed performance promises here. Exceeding a limit has an attributable effect and cleanup behavior. No parser silently drops the remainder and reports the whole requested package as processed. Shared authorization, mandatory audit, or protection failures block all affected paths, including deterministic-only fallback; optional debugging failure is not automatically such a shared failure.

## 7. Result representation, exports, and round-trip fidelity

### 7.1 Retained result contract

The result representation carries the accepted RA-04, RA-05, RA-06, and RA-07 meanings. It does not add a single pass/fail score that replaces them.

| Result group | Required information and invariants |
| --- | --- |
| Identity and context | Package version, run identity, actual assessment behavior/configuration, requested tasks/dimensions, operating context, and applicable qualification references |
| Lifecycle | RA-05 run state: `REQUESTED`, `RUNNING`, `COMPLETED`, `BLOCKED`, `FAILED`, or `CANCELLED`; terminal states stay terminal |
| Availability | `NOT_FINAL`, `NONE`, `PARTIAL`, or `AVAILABLE`, derived using RA-05 §3.3; not calculated from finding count or disposition |
| Original inventory and assessment ledger | Original TC identities, any separable views and their parent TC, qualification, capability, evidence sufficiency and outcomes: `ASSESSED`, `UNGRADABLE`, `NOT_PERFORMED`, or `INCOMPLETE` |
| Qualification | Independent RA-04 `IN_SCOPE`, `OUT_OF_SCOPE`, `UNDETERMINED`, or `NOT_EVALUATED`; supplied classification labels remain separate |
| Technique evidence | Applicability and coverage as separate dimensions; identified technique models, criteria, premises, mappings, uncertainty and exclusions; planned exercise separate from expected-result alignment |
| Review items | Stable item identity, subject and claim/dimension, evidence/premise references, uncertainty, bounded human action, and derivation under RA-05 §4 |
| Human decisions | Separate ROLE-04 interpretation decisions and ROLE-05 dispositions, attributable rationale, event order, history cutoff, self-review/independence context, and correction history |
| Summary and limitations | Reconcilable original-TC counts, requested/processed boundaries, absent/unavailable evidence, omissions and reasons; any coverage metric has its criterion, numerator and denominator |
| Comparisons, if selected | Explicit selected run correspondence, comparability evidence and uncertainty; non-redetection does not prove repair |

An `AVAILABLE` result concerns only the requested assessment boundary. `COMPLETED` does not mean all TC were eligible or substantively assessed. An empty review-item array can accompany `NONE`; it cannot be reported as “no problems found” without supported assessment context. Excluded, ungradable, or unfinished dimensions stay in the ledger; the requested boundary is not retrospectively reduced.

`DETERMINISTIC_FINDING` retains `DETERMINISTIC` derivation; `REVIEW_SUGGESTION` retains `LLM_ASSISTED` derivation. Deterministic arithmetic over an unconfirmed inferred business premise does not become an established deterministic business finding. New review items begin with `PENDING` disposition; similar past items or imported text do not supply a human decision. Human acceptance does not change derivation or repair source TC.

### 7.2 Controlled local export

A `review_export` contains an export identity/time, contract and rendering versions, authorizing actor/context, applicable classification/policy, exact package/run selection, record/history cutoff, and a manifest of included and omitted sections/evidence. The selected result includes the context and limitations needed to interpret it; users cannot create a misleading “findings-only success” projection by silently hiding `NONE`, exclusions, or unavailable evidence.

Selection can omit raw source bodies where allowed, but it must retain their identified references and mark that they are not included. An unavailable/deleted evidence dependency is distinguished from an intentionally omitted but retained source. The report does not claim to be self-contained when required source content is absent. Empty, omitted, unavailable, and not-yet-produced result sections have distinct representations. Human history is bounded by the declared cutoff; event ordering must not rely solely on equal/coarse timestamps.

Export requires current actor/action/object permission, approved local destination handling, and applicable protection of persistent and temporary copies. Authorization is rechecked before a new protected committed effect or delivery. Required audit/protection failure prevents affected publication. A failed or denied export leaves canonical package/results/history unchanged and must not leave an unsafe partial file presented as a successful export.

JSON is the machine-readable contract. Markdown is a readable projection with the same material boundaries, identities, derivations, decisions, and limitations. It can arrange content differently but cannot imply a broader assessment. Source-derived markup, HTML, remote image references, formulas, embedded commands, or code remain inert; rendering must not execute or automatically fetch supplied content. Display escaping affects the projection, not preserved originals. No CSV result export, PDF generation, or DOCX report is required by MVP.

### 7.3 Round trips and change consequences

“Canonical” means a vendor-independent vocabulary and meaning, not one mandated byte ordering or a canonical cryptographic JSON serialization. A supported serialize/read round trip preserves logical values, presence distinctions, array/step order, identities/references, unknown-content records, provenance, outcome/derivation, and selected human history. Original bytes are separately retained and integrity-identifiable. Equivalent formatting is not byte equality.

| Change or operation | Required consequence |
| --- | --- |
| Edit supplied scope, TC, basis, origin/accountability, supplied links, or provenance-affecting declarations | New package version; preserved prior lineage/history where applicable |
| Recapture using a changed capture mapping | New package version even if the assessment logic is unchanged |
| Change assessment behavior, semantic mapping, model/configuration or applicable interpretation for a new assessment | New run on the identified captured package; prior result remains historical |
| Render/serialize a retained snapshot or export in another permitted presentation | No source mutation or fictitious new assessment; representation version and selection remain identified |
| Deliberately submit a newly serialized file as new source | New attributable submission/capture under RA-03; no automatic merging based on apparently equivalent content |
| Import a prior report or copy identity/status/approval fields into an input | No restoration of operational identities, permissions, dispositions, qualification, or security authorization |
| Encounter an unsupported contract/profile version | Visible refusal/limitation under the selected path; no silent migration or latest-version fallback |

Contract version, capture-profile/mapping version, package version, assessment-behavior version, and export-renderer version are separate. Any future supported migration must identify source/target versions, preserve the original, disclose semantic losses, and apply the relevant package/run consequences. This requirement does not add a general historical migration facility to MVP.

Round-trip fidelity applies to the declared representation and export selection, not to omitted source bodies or unsupported formats. The MVP does not promise lossless automatic CSV-to-JSON-to-CSV authoring conversion, byte-identical report regeneration, or trusted backup restoration through ordinary import.

## 8. Synthetic examples for walkthrough and later test design

### 8.1 Native package with an intentional TC gap

This is eligible synthetic laboratory material. In the example's operational context, the actor `qa-demo` is attributed to the required logical roles, accepts the declared scope as ROLE-02, and accepts TC accountability as ROLE-03. The JSON alone does not establish those role assignments. The synthetic business rule is supplied explicitly, rather than inferred from the TC.

```json
{
  "document_type": "review_package_input",
  "contract_version": "1.0",
  "content": {
    "scope": {
      "description": "Synthetic customer-registration system: validation of the supplied integer age during registration."
    },
    "basis_elements": [
      {
        "source_id": "BR-AGE-01",
        "text": "For this synthetic scenario, the supplied age is an integer. Values from 18 through 120 inclusive are accepted; values outside this interval are rejected."
      }
    ],
    "case_defaults": {
      "origin": "HUMAN_AUTHORED",
      "accountability": {
        "actor_ref": "qa-demo",
        "accepted": true
      }
    },
    "test_cases": [
      {
        "source_id": "TC-AGE-001",
        "title": "Register a customer aged 18",
        "preconditions": "Other required registration fields contain valid synthetic data.",
        "steps": [
          {"action": "Enter age 18."},
          {"action": "Submit the registration form."}
        ],
        "basis_refs": ["BR-AGE-01"],
        "test_level": "system",
        "test_type": "functional",
        "design_basis": "black-box",
        "execution_mode": "manual"
      }
    ]
  }
}
```

Expected contract observations: the native file can supply both the basis and the TC; the TC is recognizable and can meet the positive accountability minimum under the stated operational context. Its first action is located at `/content/test_cases/0/steps/0/action`. Its expected result is absent, including in the supplied narrative and steps. Capture preserves that absence. The basis provides a rule against which a human may repair the TC, but TDG does not copy that rule into a fabricated supplied expected result. Any BVA conclusion remains subject to RA-06's evidence, criterion, qualification, and ledger requirements; importing the example alone performs no assessment.

### 8.2 A CSV TC source

The following is one logical data record, despite its multiline `steps` cell. It uses explicit per-record origin/accountability and an optional direct basis reference.

```csv
source_id,title,preconditions,steps,expected_result,origin,accountable_actor_ref,accountability_accepted,basis_refs
TC-AGE-002,"Reject age 17","Other required fields contain valid synthetic data.","Enter age 17.
Submit registration.","Registration is rejected.",HUMAN_AUTHORED,qa-demo,true,"[""BR-AGE-01""]"
```

To assemble it with supplied scope/basis, a native manifest uses a `tc_sources` entry with `binding_ref` equal to a selected-input label and profile `tdg-tc-csv`, version `1`. The operation explicitly supplies the matching file. The CSV does not itself establish the actor's ROLE-03 authority. Its steps locator identifies logical data record 1, column `steps` at ordinal 4; physical line numbering is supplementary. The manifest can omit native `test_cases` when the bound CSV supplies them.

### 8.3 Boundary variants

| Variant | Required observation |
| --- | --- |
| Delete `expected_result` from a behavioral TC | Preserve the gap; do not reject it as invalid JSON or automatically author an expectation |
| Keep only ID, title, and a documentation link | Retain the item; it does not satisfy recognizability or retrieve the linked document |
| Duplicate the TC's `source_id` on a second record | Preserve two internal cases and the identifier problem; no deduplication or join |
| Duplicate the `origin` JSON member inside one object | Reject that JSON parse/projection path as ambiguous; do not take the last value |
| Supply the Polish free-text origin from Section 4.2 | Preserve the declaration as unresolved; a positive package-level neighbor does not qualify this TC |
| Set explicit `origin: "UNKNOWN"` beside a positive containing-set default | Preserve `UNKNOWN`; the default applies only to absence |
| Supply a Jira link as the only basis content | Keep the reference; no source fetch and no substantive basis established |
| Put a role grant, accepted disposition, or sealed authorization inside supplied JSON | Preserve as untrusted content where permitted; no operational authority change |
| Include a safely captured but malformed CSV beside independent native TC | Preserve the full inventory and affected opacity; evaluate separability/minimum conditions rather than silently omitting the file |
| Export a completed run with no substantively assessed dimensions and no findings | Preserve `COMPLETED`, `NONE`, and the non-performance reasons; no clean-review claim |

These are review examples and future test-design seeds. Product behavior has not been executed or shown to pass them.

## 9. Proposed requirements and direct traceability

All requirements below have **Priority = MUST** and **Status = PROPOSED**. Local `VAL-nnn` references mean `RA09-VAL-nnn`. Existing upstream requirements are read in their accepted baselines, not reopened by this draft. Each requirement has an explicit validation edge; Section 10 supplies the reverse edges.

| ID | Proposed requirement | Principal upstream basis | Validation |
| --- | --- | --- | --- |
| RA09-REQ-001 | TDG shall use the vendor-independent contracts in Sections 2–3 while preserving submission context, captured package, and derived assessment as separate layers. | Charter §12; RA03-REQ-001; RA03-REQ-002; RA03-REQ-003 | VAL-001 |
| RA09-REQ-002 | MVP shall support native local JSON and the defined local TC CSV path with supplied scope/basis, use explicit identified mappings for supported customized layouts, and make no implicit all-format, Jira-origin-authentication, or live-connector promise. | Charter §12; RA03-REQ-005; RA03-REQ-012 | VAL-001, VAL-004 |
| RA09-REQ-003 | TDG shall route by document kind and supported contract/profile version through an approved local schema/mapping registry, enforce configured structural assertions, and prevent remote resolution, guessed compatibility, or silent migration. | RA03-REQ-005; RA08-REQ-009; RA08-REQ-010 | VAL-002, VAL-003 |
| RA09-REQ-004 | Native JSON processing shall enforce Section 3.3's syntax/encoding and duplicate-member rules before lossy materialization, and expose unsupported numeric or other representation limits without misrepresenting source values. | RA03-REQ-006; RA03-REQ-025; RA08-REQ-010 | VAL-003 |
| RA09-REQ-005 | TDG shall bind source references only to explicitly selected supplied content, retain exact source identity separately from projection, and preserve stable original/projection locators and provenance under Section 4.1. | RA03-REQ-005; RA03-REQ-006; RA03-REQ-020 | VAL-001, VAL-005 |
| RA09-REQ-006 | TDG shall preserve source values, ordering, presence distinctions and mapping state under Section 3.3, without silent trimming, coercion, rounding, normalization, or replacement of raw content by a projection. | RA03-REQ-006; RA03-REQ-022; RA03-REQ-025 | VAL-003, VAL-006 |
| RA09-REQ-007 | TDG shall accept the supported narrative and structured TC representations, preserve deficient items, and apply RA-03 recognizability and evidence sufficiency separately from file syntax and editorial field completeness. | RA03-REQ-011; RA03-REQ-012; RA03-REQ-022; RA03-REQ-032 | VAL-006, VAL-007 |
| RA09-REQ-008 | TDG shall preserve and map origin/accountability declarations using Section 4.2, constrain defaults to their explicit scope and absent fields, and leave unresolved or conflicting declarations visible without inferring positive eligibility. | RA03-REQ-011; RA03-REQ-021; RA01 authority rules | VAL-007, VAL-008 |
| RA09-REQ-009 | TDG shall distinguish internal and source identities, preserve deficient/duplicated source keys and optional unresolved associations, and prevent content similarity or identifier equality from merging independent items or packages. | RA03-REQ-013; RA03-REQ-014; RA03-REQ-016; RA03-REQ-017; RA03-REQ-048 | VAL-005, VAL-008 |
| RA09-REQ-010 | The canonical CSV importer shall enforce the declared dialect, header, logical-record, value and field-count rules in Section 5.1, including multiline fields, explicit scalar mapping, and visible deficient records. | Charter §12; RA03-REQ-012; RA03-REQ-025 | VAL-004, VAL-009 |
| RA09-REQ-011 | TDG shall identify capture mapping versions and their rules under Section 5.2, require explicit selection of supported mappings, and separate mechanical capture transformations from assessment-time semantic interpretation. | RA03-REQ-003; RA03-REQ-006; RA03-REQ-044; RA07-REQ-004 | VAL-002, VAL-009, VAL-010 |
| RA09-REQ-012 | TDG shall retain unknown, unmapped, malformed, or opaque assessment-relevant content with trustworthy source boundaries and visible effects, without guessing record framing, silently discarding fields, or claiming false projection conformance. | RA03-REQ-019; RA03-REQ-025; RA08-REQ-010 | VAL-003, VAL-009 |
| RA09-REQ-013 | TDG shall distinguish permitted capture, core-minimum admissibility, qualification, and dimension-specific sufficiency, apply all RA-03 input-sufficiency outcomes, and limit only the narrowest defensible scope while preserving the requested inventory. | RA03-REQ-031; RA03-REQ-032; RA03 §15; RA04 qualification rules | VAL-010, VAL-011 |
| RA09-REQ-014 | TDG shall report capture success only for a coherent durable snapshot, preserve retry/conflict semantics, and account for failure, cancellation and recovery under Section 6.3 without duplicate effects or fabricated completion. | RA05-REQ-017; RA05-REQ-018; RA05-REQ-019 | VAL-011, VAL-012 |
| RA09-REQ-015 | TDG shall produce the receipt and issue information in Section 6.2, keep intake outcomes distinct from review outcomes, and provide stable codes, affected boundaries and human actions without exposing prohibited diagnostic content. | RA03 §15.2; RA05-REQ-002; RA08-REQ-014 | VAL-011, VAL-013 |
| RA09-REQ-016 | TDG shall enforce declared parser/profile resource limits before enabling their use, expose affected omissions and termination reasons, and apply safe cleanup without silent truncation or bypass of shared safety prerequisites. | RA07-REQ-007; RA08-REQ-010; RA08-REQ-013; RA08-REQ-020 | VAL-003, VAL-009, VAL-012 |
| RA09-REQ-017 | TDG shall represent run state, result availability, original inventory, qualification and ledger outcomes independently under Section 7.1, preserving requested boundaries and reconcilable counts without a misleading empty-findings success claim. | RA05-REQ-002; RA05-REQ-003; RA05-REQ-004; RA05-REQ-005 | VAL-014 |
| RA09-REQ-018 | TDG shall retain and export claim/evidence, technique criterion/model, derivation, configuration, uncertainty and selected human-history context under Section 7.1 without promoting inferred premises, transferring dispositions, or erasing limitations. | RA05-REQ-006; RA05-REQ-007; RA05-REQ-008; RA05-REQ-011; RA06-REQ-004; RA06-REQ-006; RA07-REQ-018 | VAL-014, VAL-015 |
| RA09-REQ-019 | TDG shall perform controlled local export with current authorization, declared selection/history cutoff, protected destination/copies, and coherent delivery; export failure shall not mutate canonical records or publish an unsafe partial output. | RA05-REQ-021; RA08-REQ-006; RA08-REQ-019; RA08-REQ-020 | VAL-012, VAL-015 |
| RA09-REQ-020 | MVP shall provide JSON result export and a Markdown projection with equivalent material meaning, explicit omitted/unavailable sections and evidence, and distinct document kinds that do not act as ordinary backup-restoration or trusted-history import. | RA05-REQ-014; RA05-REQ-020; RA05-REQ-021; RA08-REQ-018 | VAL-002, VAL-015, VAL-016 |
| RA09-REQ-021 | TDG shall distinguish contract, capture, package, assessment and rendering versions, apply Section 7.3's change consequences, and preserve historical content rather than silently upgrading or reassessing it. | RA03-REQ-043; RA03-REQ-044; RA03-REQ-045; RA03-REQ-046; RA05-REQ-012 | VAL-002, VAL-010, VAL-016 |
| RA09-REQ-022 | Supported round trips shall preserve Section 7.3's logical content, presence/order, unknown-content records, identities, provenance, limitations and selected human history, while distinguishing logical fidelity, source-byte integrity and declared export omissions. | RA03-REQ-006; RA03-REQ-025; RA03-REQ-048; RA05-REQ-021 | VAL-006, VAL-016 |
| RA09-REQ-023 | TDG shall treat imported and rendered content as inert untrusted data, prevent execution or automatic external retrieval, and keep safe display/diagnostic projections separate from protected original evidence. | RA03-REQ-005; RA08-REQ-007; RA08-REQ-009; RA08-REQ-010; RA08-REQ-014 | VAL-013, VAL-015 |
| RA09-REQ-024 | TDG shall prevent supplied or imported identity, role, status, adoption, approval, qualification, or policy fields from granting operational authority, restoring history as trusted, or bypassing applicable human and security checks. | RA01 authority/profile rules; RA05-REQ-022; RA08-REQ-001; RA08-REQ-004; RA08-REQ-005; RA08-REQ-006 | VAL-008, VAL-015 |

## 10. Validation obligations and reverse trace

These are requirements-stage obligations for later STLC design, not finished executable TC or evidence that the product works. Both directions of the REQ ↔ VAL relationship are explicit. Each row must later gain representative inputs, preconditions, controlled expected observations and retained evidence.

| ID | Validation condition and required oracle | Direct RA09 requirements |
| --- | --- | --- |
| RA09-VAL-001 | Compare a native JSON package with a combined manifest/selected-CSV package. Verify substantive scope/basis availability, inventory, supported mapping and three-layer separation. Include a link-only source and a Jira-shaped source whose claimed vendor origin is not authenticated or fetched. | REQ-001, REQ-002, REQ-005 |
| RA09-VAL-002 | Exercise supported/unsupported document kinds, contract/profile versions and local schemas, required assertion configuration, external reference attempts, and changed mappings. No remote resolution, guessed newest version, implicit report restoration or silent migration is allowed; version consequences remain explicit. | REQ-003, REQ-011, REQ-020, REQ-021 |
| RA09-VAL-003 | Use duplicate JSON member names, invalid encoding/syntax, non-finite tokens, precise large/decimal values, mistyped/unknown fields and size/nesting boundaries. Verify pre-materialization rejection or lossless bounded handling, retained permitted raw evidence, and no rounded/coerced/truncated success claim. | REQ-003, REQ-004, REQ-006, REQ-012, REQ-016 |
| RA09-VAL-004 | Cover CSV quoted commas/quotes, multiline fields, CRLF/LF, optional final separator, accepted leading BOM, leading-zero text, literal `NULL`, blank cells and absent columns. Check the declared narrow format and explicit accountability/basis-reference decoding; a semicolon/custom layout is not silently normalized. | REQ-002, REQ-010 |
| RA09-VAL-005 | Use missing/duplicate source IDs, ambiguous/unbound references, JSON member names containing `/` and `~`, multiline CSV and opaque artifacts. Verify independent internal identities, precise versioned locators, visible optional link problems and no retrieval, path disclosure or content-based merging. | REQ-005, REQ-009 |
| RA09-VAL-006 | Distinguish absent, null, empty, whitespace-only, mistyped and present values through capture and serialization. Compare narrative/structured steps and nested/narrative expectations; order is preserved, missing expectations remain missing, and no complete-template requirement suppresses deficient TC. | REQ-006, REQ-007, REQ-022 |
| RA09-VAL-007 | Compare all five canonical origins, unresolved free text, missing/negative accountability, title-only items and behavioral TC. Exercise native/source-scoped defaults versus explicit null/empty/unknown/conflicting declarations. Only genuinely eligible, attributable cases satisfy the positive minimum. | REQ-007, REQ-008 |
| RA09-VAL-008 | Attempt origin/accountability upgrades through neighboring cases, copied roles/approvals, source-ID collisions, similar TC, and supplied historical identities. Check that content remains attributable without granting roles, eligibility, dispositions or identity merges. | REQ-008, REQ-009, REQ-024 |
| RA09-VAL-009 | Use unknown/duplicate headers, ragged/blank records, unclosed quoted fields, invalid inner `basis_refs` JSON, source row-order changes and field/record limits. Verify raw preservation, the smallest reliable boundary, explicit selected mapping, no heuristic grouping or shifted/padded/dropped content, and safe independent projections only where framing is trustworthy. | REQ-010, REQ-011, REQ-012, REQ-016 |
| RA09-VAL-010 | Separate recapture under changed capture mapping from assessment-only semantic mapping changes. Combine deficient/opaque inputs with independent sufficient items and with non-separable conflicts. Verify package/run identities and consequences without silently shrinking the submitted boundary. | REQ-011, REQ-013, REQ-021 |
| RA09-VAL-011 | Build cases for every RA-03 IS-01 through IS-11 rule, including a durable candidate that fails minimum checks and a failure before faithful capture. Verify receipt outcomes, inventory, package reference, issue effects and human remedies; parsing/capture success never substitutes for admissibility or review success. | REQ-013, REQ-014, REQ-015 |
| RA09-VAL-012 | Interrupt capture/export during staging and persistence; retry the same operation and conflict it with changed content/configuration. Include cancellation, resource exhaustion, restart and permission/audit/protection loss before delivery. Verify coherent durable results only, no duplicate effect, safe cleanup, no unsafe partial export and unchanged canonical records on export failure. | REQ-014, REQ-016, REQ-019 |
| RA09-VAL-013 | Compare issue codes and effect scopes across localized messages and unavailable evidence. Supply secrets, absolute paths, active markup, commands and external references. Verify safe permitted diagnostic fields, stable machine meaning, no execution/fetch, and separation from protected evidence access. | REQ-015, REQ-023 |
| RA09-VAL-014 | Serialize results combining terminal/nonterminal runs, every availability and ledger outcome, separable views and zero findings. In particular, `COMPLETED` plus `NONE` is not a clean review. Reconcile original-TC counts and technique denominators and preserve model/configuration, interpretation, uncertainty and derivation distinctions. | REQ-017, REQ-018 |
| RA09-VAL-015 | Export selected results/history as JSON and Markdown under allowed, denied and revoked access. Compare claims, source/premise references, human event order and cutoff, self-review context, limitations and evidence omissions; unsupported conclusions and imported authority do not appear. Verify destination protection, inert rendering and no remote-resource fetch. | REQ-018, REQ-019, REQ-020, REQ-023, REQ-024 |
| RA09-VAL-016 | Round-trip supported representations and compare explicitly equivalent logical inputs, including unknown content, presence/order and selected human history. Separate logical equality from byte identity and independent submissions. Exercise renderer-only changes and unsupported versions; report omission is explicit and re-import does not restore trusted history or trigger an assessment. | REQ-020, REQ-021, REQ-022 |

Trace coverage here means every proposed requirement has at least one explicit validation obligation and every obligation references existing requirements. It does not establish test adequacy, executed test coverage, or product acceptance.

## 11. Open decisions and recommendations

| ID | Owner decision requested | Recommendation and consequence |
| --- | --- | --- |
| OD-RA09-001 | Confirm native document kinds, versioned schema approach and the syntax/content distinction | Accept Sections 2–3: JSON contracts with an approved local 2020-12 schema registry; structural checks remain separate from deficient captured content and substantive admissibility. Executable schemas follow in design without changing these meanings |
| OD-RA09-002 | Confirm the first supported CSV contract | Accept Section 5: one logical record per candidate TC, multiline narrative steps, explicit optional columns and source-specific defaults/mappings. Do not add automatic dialect detection, universal Jira support, or implicit multi-row grouping |
| OD-RA09-003 | Confirm capture and error semantics | Accept Section 6: preserve trustworthy permitted candidates and visible content gaps; separate durable capture from minimum admissibility, with bounded consequences and atomic success. Reject unsafe/unrouteable capture rather than guessing content |
| OD-RA09-004 | Confirm output formats and the fidelity promise | Accept Section 7: JSON result export plus a faithful Markdown projection, exact selection/history boundaries and explicit omissions. General backup restoration, trusted history import and CSV authoring round trips remain outside MVP |

All four decisions are OPEN in v0.1. Existing upstream acceptances do not automatically accept these proposed contract details. None of the recommendations authorizes confidential-data operation, new model tasks, or changes to the TC-review scope.

## 12. Author checks, remaining allocation, and exit

### 12.1 Author check scope

The author check concerns this draft and its references. It is not the formal static review, independent reviewer agreement, or product validation. The following results are recorded only after checking the delivered artifact.

| Check | Result and boundary |
| --- | --- |
| Entry baseline | PASS — referenced accepted source snapshots and RA-08 closure match the pinned repository state; GO to RA-09 is recorded |
| Unique requirement and obligation identities | PASS — 24 unique requirements and 16 unique validation obligations; all requirements remain PROPOSED |
| REQ → VAL | PASS — 24/24 proposed MUST requirements have at least one explicit obligation |
| VAL → REQ | PASS — 16/16 obligations point to existing RA09 requirements; reverse edges agree with the requirement table |
| Upstream references and authority | PASS — referenced upstream identifiers exist; original role/profile, scope, capture, run and authority boundaries are preserved |
| JSON/CSV illustrations | PASS — JSON syntax and sample field/reference paths checked; CSV illustration decodes to one data record with nine columns, including multiline steps and a JSON-array basis reference. This is document-fixture verification only |
| Failure and deficient-content distinctions | PASS — incomplete TC, unknown origin, duplicate source IDs, duplicate JSON members, ambiguous CSV framing and unavailable evidence have distinct documented consequences |
| Document growth and scope | PASS — one focused draft; upstream business and security rules are referenced rather than replaced by new frameworks; no extra implementation or review artifacts are required to read it |
| Formal static review / implemented behavior | NOT PERFORMED — no `SR-RA09-001` verdict, product test result, acceptance, or RA-10 authorization is claimed |

### 12.2 Carried observations and downstream work

| Item | Allocation / retained status |
| --- | --- |
| Executable schemas and parser/export implementation | Solution Design produces the machine-readable forms, complete versioned issue-code catalog and concrete mapping/locator structures from accepted RA-09 meaning; implementation follows its own gate |
| Concrete resource limits and storage/transaction mechanisms | Design selects measured bounds, enforcement points, persistence and cleanup mechanisms; evidence is required before the relevant profile is enabled |
| Detailed tests and acceptance evidence | Later STLC expands the validation obligations into fixtures and TC, including malformed, mixed, adversarial and cross-representation cases; human-reviewed expected observations must not be generated solely by the component under test |
| RA-10 | Consolidate evaluation/acceptance criteria, measurement and requirements-to-validation traceability before closing Requirements Analysis; no gate granted here |
| `SR-RA03-OBS-001` | OPEN / CARRIED — make the RA03-VAL-014 path through IS-01–IS-11 explicitly traceable to accepted requirements before executable test design. RA09-VAL-011 adds an obligation to exercise those rules; it does not retroactively close the inherited trace observation |
| `SR-RA03-OBS-002` / R-08 | CARRIED — monitor scope/documentation growth. Avoid duplicate schema catalogs, status documents or speculative adapters; add artifacts only for a concrete review/design/validation need |

### 12.3 Review and exit sequence

The next action is the Project Owner's review of this draft, including the four recommendations. After substantive acceptance, conduct and record the focused formal static review, resolve findings, and verify corrections and both directions of traceability. A controlled v0.2 baseline then records the accepted requirements/decisions and the review outcome.

Only an explicit Owner decision can endorse the formal record, baseline RA-09, and grant GO to RA-10. Repository publication follows the established authorized documentation-commit workflow. This draft records neither that future acceptance nor a commit instruction.

## 13. Version record

| Version | Date | Change |
| --- | --- | --- |
| 0.1 | 2026-09-20 | Initial RA-09 draft following accepted RA-08 closure and GO: proposed local JSON/CSV input contracts, capture/issue semantics, result/export fidelity, 24 requirements, 16 validation obligations, and four open decisions |

[charter]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/ff1cd6379717d59da09087120609d41fc7309668/docs/governance/test-design-gatekeeper-project-charter-v0.4.md
[ra01]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/ff1cd6379717d59da09087120609d41fc7309668/docs/requirements-analysis/test-design-gatekeeper-ra-01-stakeholders-actors-authority-v0.3.md
[ra02]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/ff1cd6379717d59da09087120609d41fc7309668/docs/requirements-analysis/test-design-gatekeeper-ra-02-system-context-workflows-use-cases-v0.3.md
[ra03]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/ff1cd6379717d59da09087120609d41fc7309668/docs/requirements-analysis/test-design-gatekeeper-ra-03-review-package-content-provenance-validation-v0.3.md
[ra04]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/ff1cd6379717d59da09087120609d41fc7309668/docs/requirements-analysis/test-design-gatekeeper-ra-04-scope-qualification-classification-boundaries-v0.2.md
[ra05]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/ff1cd6379717d59da09087120609d41fc7309668/docs/requirements-analysis/ra-05/test-design-gatekeeper-ra-05-findings-dispositions-persistence-v0.2.md
[ra06]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/ff1cd6379717d59da09087120609d41fc7309668/docs/requirements-analysis/ra-06/test-design-gatekeeper-ra-06-technique-applicability-design-coverage-v0.2.md
[ra07]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/ff1cd6379717d59da09087120609d41fc7309668/docs/requirements-analysis/ra-07/test-design-gatekeeper-ra-07-llm-roles-qualification-v0.2.md
[ra08]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/ff1cd6379717d59da09087120609d41fc7309668/docs/requirements-analysis/ra-08/test-design-gatekeeper-ra-08-confidentiality-security-privacy-v0.2.md
[gate03]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/ff1cd6379717d59da09087120609d41fc7309668/docs/reviews/test-design-gatekeeper-ra-03-gate-record-v0.2.md
[gate04]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/ff1cd6379717d59da09087120609d41fc7309668/docs/reviews/test-design-gatekeeper-ra-04-focused-static-review-v0.2.md
[gate05]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/ff1cd6379717d59da09087120609d41fc7309668/docs/requirements-analysis/ra-05/test-design-gatekeeper-ra-05-focused-static-review-v0.2.md
[gate06]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/ff1cd6379717d59da09087120609d41fc7309668/docs/requirements-analysis/ra-06/test-design-gatekeeper-ra-06-focused-static-review-v0.2.md
[gate07]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/ff1cd6379717d59da09087120609d41fc7309668/docs/requirements-analysis/ra-07/test-design-gatekeeper-ra-07-focused-static-review-v0.2.md
[gate08]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/ff1cd6379717d59da09087120609d41fc7309668/docs/requirements-analysis/ra-08/test-design-gatekeeper-ra-08-focused-static-review-v0.2.md
[rfc8259]: https://www.rfc-editor.org/rfc/rfc8259
[rfc4180]: https://www.rfc-editor.org/rfc/rfc4180
[rfc6901]: https://www.rfc-editor.org/rfc/rfc6901
[schema-core]: https://json-schema.org/draft/2020-12/json-schema-core
[schema-validation]: https://json-schema.org/draft/2020-12/json-schema-validation
