# Test Design Gatekeeper

## SAD-03 — Model Contribution and Protection Architecture

| Field | State |
| --- | --- |
| Version / date | 0.2 — 2026-09-26; administrative publication revision of the reviewed v0.1 body |
| SDLC phase | Solution and Architecture Design; continuation of B-01 after SAD-02 |
| Work allocation | B-01, third activity: model gateway, qualification, context protection and safe execution boundaries |
| Document status | OWNER WALKTHROUGH ACCEPTED — Sections 1–17; integrated correction verification, baseline designation and next-activity gate remain pending |
| Design decisions | SAD-D-009 through SAD-D-015 accepted without changes; physical choices remain open |
| Requirements baseline | The 249 accepted requirements identified by SR-RA-001 v0.2 remain authoritative |
| Evidence boundary | Document-level design and threat-oriented walkthrough; no product implementation, model qualification or executed product tests |
| Author / review independence | AI-assisted draft and author check by the same assistant; no independent review claimed |

**Current reading status:** The Owner accepted all seventeen sections and SAD-D-009–SAD-D-015 in the project conversation and authorized publication on 2026-09-26. [SR-SAD03-001](../reviews/test-design-gatekeeper-sad-03-review-record-v0.1.md) records those decisions, the publication checks and two cross-contract findings awaiting correction. Sections 1–17 and their source references retain the reviewed v0.1 wording; their original proposal and future-walkthrough notices describe the drafting stage. The ten open decisions in Section 15 remain open. Accepted upstream requirements take precedence where wording needs reconciliation. This administrative revision records acceptance without claiming a new product requirement, a completed integrated design review or an implementation GO.

## 1. Purpose and reading convention

SAD-01 established one local modular application, a terminal-first entry point and one active review run. SAD-02 defined the logical data, identity, lineage and contract boundaries that preserve supplied content and human history. SAD-03 defines how a local language model may contribute bounded analysis without becoming a source of authority, an unrestricted agent or an untraceable second data store.

The document covers the logical gateway around model invocation, qualification of a model/configuration/task combination, context minimization, runtime limits, response validation, failure handling, diagnostics and the separation between laboratory and future sealed operation. It deliberately stops before selecting a particular model, runtime, prompt library, database, operating-system sandbox or encryption product.

The following reading convention applies:

1. **PROPOSED** describes a design direction awaiting Owner acceptance.
2. **MUST**, **SHOULD** and **MAY** in this draft express proposed design language; they do not create an accepted product requirement until the corresponding section and decision are accepted and recorded.
3. Inherited obligations retain the meaning and status of the accepted Requirements Analysis baseline. A conflict with an accepted requirement is a change request, not an implicit exception.
4. A model response is always a data contribution. It cannot grant authority, expand scope, create a business rule, change a package, approve a finding or repair a test case.

The first operational target remains a local laboratory path using deliberately supplied public or synthetic material. Acceptance of this document alone will not authorize confidential project input, a sealed deployment, implementation or an official claim of ISTQB compliance.

## 2. Governing sources and bounded deliverable

| Source | Used here for |
| --- | --- |
| [SR-RA-001 v0.2][gate] | Design authorization, B-01 continuation, flexible solo capacity and active R-08 |
| [SAD-01 v0.1][sad01] | Local modular shape, component responsibilities, one active run and flow commit points |
| [SAD-02 v0.1][sad02] | Logical records, immutable lineage, guarded writes, explicit incomplete states and contract-first serialization |
| [RA-03 v0.4][ra03] | Review Package content, provenance, human accountability, insufficient-input behavior and version consequences |
| [RA-04 v0.2][ra04] | Eligibility, independent classification axes and bounded MVP scope |
| [RA-05 v0.2][ra05] | Run, ledger, result, interpretation, disposition and durable-history separation |
| [RA-06 v0.2][ra06] | Technique applicability, planned exercise, evidence and expected-result alignment |
| [RA-07 v0.2][ra07] | Permitted model tasks, model/configuration qualification, response checks and change consequences |
| [RA-08 v0.2][ra08] | Admission, confidentiality, trust boundaries, protected copies and safe failure |
| [RA-09 v0.2][ra09] | Serialization-neutral input, local JSON/CSV intake and controlled JSON/Markdown export |
| [RA-10 v0.2][ra10] | Evaluation separation, human oracle, acceptance governance and empirical feasibility |

The bounded deliverable is one coherent logical protection model for model-assisted review. It must be precise enough for a later implementation-ready contract and security verification activity. It does not claim that the model is qualified, that a local endpoint is safe, or that a runtime profile is already enforceable.

## 3. Design goals and inherited constraints

The design must make the following properties inspectable:

1. the difference between supplied information, deterministic derivation and model suggestion;
2. the exact model, runtime, task, configuration, policy and qualification evidence used by an attempt;
3. the difference between a permitted context projection and an unrestricted source-store read;
4. the difference between a model response being structurally valid and its claims being substantively supported;
5. the difference between an operational retry and a new review request;
6. the difference between a candidate contribution and a human-confirmed interpretation;
7. the difference between a laboratory capability and a sealed capability;
8. the effect of a timeout, cancellation, resource limit, audit failure or protection failure;
9. the reason why an assessment was not performed, could not be graded or remained incomplete;
10. the model contribution's inability to approve or modify testware.

The design remains constrained by the accepted project boundaries:

| Constraint | Design consequence |
| --- | --- |
| Supplied-data only | The gateway receives only an explicit context projection. It does not follow links, search repositories, browse the internet or discover files. |
| Human accountability | Origin and accountability come from supplied declarations and trusted human operations. The model cannot infer, upgrade or self-certify them. |
| TDG advisory-only | The model may suggest missing information, relationships, risks or technique questions. It cannot approve, reject or repair a TC. |
| Functional black-box MVP | The gateway supports the bounded review of system-level functional black-box TC and EP, BVA, decision tables and state transitions. It is not a generic AI-testing framework. |
| Local first | The initial path works with a local runtime and public/synthetic lab material. A network service is not an assumed dependency. |
| Confidentiality | No confidential project input enters the laboratory merely because a model is local. Sealed handling requires its own identity, policy, storage, egress and verification controls. |
| One active run | The first operator flow remains foreground and explicitly interruptible. Model attempts cannot become hidden background jobs. |
| R-08 active | Reuse one gateway contract and shared policy concepts; do not create a bespoke mini-architecture per technique or sample. |

## 4. Proposed design directions

The following directions are proposed for Owner review. They refine the accepted SAD-01 and SAD-02 boundaries without granting implementation authority.

| Decision | Proposed direction | Reason and review consequence |
| --- | --- | --- |
| SAD-D-009 — Single controlled model gateway | Every operational model invocation passes through one logical gateway contract owned by CMP-05. Assessment services cannot call a runtime directly. | Creates one place for task qualification, context filtering, limits, provenance, response validation and safe failure. It does not require a separate process or service. |
| SAD-D-010 — Qualification is tuple-specific | Qualification applies to the model/runtime, behavior configuration, task type, policy profile and relevant contract version together. There is no generic “trusted model” flag. | Prevents a model qualified for one suggestion task from being silently reused for another task, profile or behavior version. |
| SAD-D-011 — Explicit minimal context projection | The caller supplies an allowlisted projection of retained evidence. The gateway passes only the selected fields and bounded excerpts needed for the declared task. | Prevents arbitrary source-store reads, hidden context expansion and unnecessary exposure. A link or identifier remains data unless an explicitly authorized operation resolves it. |
| SAD-D-012 — Bounded, cancellable execution | Each attempt has explicit input/output/resource/time/retry limits, a cancellation path and one immutable attempt identity. Retries cannot silently change model, context, task or destination. | Makes weak local hardware and model variability observable. A limit or cancellation produces an explicit incomplete outcome, not a pass or a silent fallback. |
| SAD-D-013 — Data-only model output | Raw output is untrusted data. It must pass structural and reference validation before it can become a candidate contribution. It cannot invoke tools, write records, alter policy or change scope. | Contains prompt-injection-like instructions and malformed output. Semantic support remains a separate evidence and human-interpretation question. |
| SAD-D-014 — Fail closed at shared protection boundaries | Loss of mandatory admission, protected storage, egress control, identity, audit or policy verification blocks dependent model and deterministic work. Optional diagnostics have a narrower effect. | Prevents the deterministic path from becoming an unprotected escape route around the model/security boundary. |
| SAD-D-015 — Profile separation | Laboratory and sealed profiles are different policy contexts with different admission, identity, storage, egress and verification evidence. A laboratory profile cannot be relabeled as sealed. | Keeps the current public/synthetic experiment safe while reserving a verifiable path for future confidential use. |

### 4.1 Decision boundary for this activity

Acceptance of SAD-D-009 through SAD-D-015 would accept logical architecture directions only. It would not select Ollama or another runtime, a model name, an embedding/vector store, a database, an OS sandbox, an encryption mechanism, numeric limits, a network topology or an implementation language. Those choices require later design and verification records.

## 5. Model contribution architecture

### 5.1 Logical components and ownership

The gateway is a logical responsibility within the local application. It may initially run in the same process as the coordinator, but a process boundary or endpoint must not be mistaken for a security boundary.

| Responsibility | Owner | Required boundary |
| --- | --- | --- |
| Request admission and trusted actor/profile context | CMP-01 | The gateway receives a trusted operation context, not authority claims from the package or prompt. |
| Task and qualification lookup | CMP-05 with CMP-01 policy input | A request is denied unless the exact task/configuration/profile tuple has current qualification evidence. |
| Context projection | CMP-03/CMP-04 request; CMP-05 enforces | Only allowlisted evidence references and bounded content are copied into the attempt. |
| Local runtime invocation | CMP-05 | The runtime is treated as an untrusted computation endpoint with no record-store, filesystem-discovery, command or network authority. |
| Response validation | CMP-05 | Structural, size, reference and schema checks occur before any result promotion. |
| Candidate contribution mapping | CMP-04 | A validated response is linked to the requested ledger entry as a candidate contribution, never as a direct result or disposition. |
| Retention and audit | CMP-06 | Attempt metadata, outcome and permitted evidence are durably recorded through guarded writes. |
| Human inspection/export | CMP-07 | Reports distinguish model suggestion, deterministic finding and human interpretation. Raw sensitive content is not copied into an export by default. |

### 5.2 Gateway invariants

The following invariants are proposed for every model attempt:

1. one attempt references exactly one `review_request_id`, `run_id`, ledger boundary and task identity;
2. the attempt records the selected package version and behavior/configuration versions;
3. an attempt cannot reference a package version that is not part of the active request;
4. the model cannot create a new package, TC, requirement, business rule, role, finding disposition or project gate;
5. a response cannot be promoted if its schema, references, limits or policy context are invalid;
6. an attempt cannot change its context, model, profile or output destination during execution;
7. a retry has a new attempt identity but preserves the parent operation and retry reason;
8. an absent response, malformed response and semantically unsupported response remain distinguishable;
9. the attempt remains linked to the evidence actually supplied, not to an inferred source the model mentions;
10. no model output is treated as durable truth until CMP-04 and the applicable human workflow accept its limited role.

### 5.3 Proposed contribution classes

The gateway should expose explicit contribution classes instead of one generic `answer` field:

| Class | Example use in MVP | What it may not do |
| --- | --- | --- |
| `RELATION_CANDIDATE` | Suggest that a supplied TC may relate to a supplied requirement or business rule. | Establish a missing link as fact or retrieve the requirement. |
| `GAP_CANDIDATE` | Point to a missing precondition, expected result, input value or rule in the supplied material. | Invent the missing rule or modify the TC. |
| `TECHNIQUE_CANDIDATE` | Suggest a possible EP, BVA, decision-table or state-transition question from supplied evidence. | Claim that the technique is mandatory or that coverage is proven. |
| `CLASSIFICATION_CANDIDATE` | Highlight evidence that the TC may not be system-level black-box. | Override deterministic classification or human accountability. |
| `RISK_CANDIDATE` | Highlight ambiguity, contradiction, stale source or potential impact. | Assign authoritative business severity without the approved policy/context. |
| `EXPLANATION` | Explain an independently produced deterministic finding in bounded language. | Change the finding's derivation or turn explanation into evidence of correctness. |

The exact final enumeration remains an open contract decision. The important invariant is that a model response is typed as a proposal with provenance rather than flattened into a verdict.

## 6. Task envelope and context projection contract

### 6.1 Proposed task envelope

Every invocation is represented by a versioned logical envelope. The exact serialization is deferred to SAD-04 or the implementation-ready contract activity.

| Field group | Minimum meaning |
| --- | --- |
| Operation identity | `operation_id`, `review_request_id`, `run_id`, `ledger_entry_id`, attempt number and retry parent where applicable |
| Subject identity | package version, recognizable TC identity and requested review dimension; no free-form subject substitution |
| Task identity | stable task type, task contract version and permitted contribution class |
| Behavior context | prompt/template/configuration identifier and version, model/runtime identifier and qualification reference |
| Profile/policy | laboratory or sealed profile, effective policy version, actor/action authorization decision and data classification |
| Context manifest | allowlisted evidence item IDs, bounded field names, locators, content hashes and projection reason |
| Limits | input size, output size, duration, retry, concurrency and cancellation policy references |
| Output contract | expected schema, allowed enums, reference rules and promotion state |
| Provenance | source package/version, gateway version, contract version, timestamps and attempt hash where supported |

The envelope must not contain an instruction granting the model authority. Any text inside a supplied document that says “ignore policy”, “approve this TC” or similar is content to analyze, not an executable gateway instruction.

### 6.2 Context projection rules

The projection builder applies the following rules before invocation:

1. start from an empty context and add only fields explicitly required by the task contract;
2. select records by immutable identity and package lineage, never by a model-supplied path or URL;
3. preserve field origin, source locator and sensitivity/classification metadata;
4. cap number of records, field length, total input size and nesting depth according to the effective policy;
5. replace unavailable or disallowed content with an explicit omission marker, not a fabricated value;
6. exclude credentials, access tokens, secrets, unrelated packages, local environment variables and hidden prompts;
7. do not resolve links, call external services or inspect arbitrary directories;
8. include the projection manifest in retained attempt metadata, subject to the profile's sensitive-content policy;
9. make truncation, normalization and redaction visible to downstream validation;
10. prevent a model response from requesting an automatic context expansion within the same attempt.

### 6.3 Context sufficiency and abstention

An insufficient projection is not a reason to widen scope automatically. The gateway returns a bounded `CONTEXT_INSUFFICIENT` outcome with the missing evidence category and a human-readable explanation. The coordinator may ask the responsible human to supply a new or corrected package version, or may record the dependent assessment as `UNGRADABLE`/`NOT_PERFORMED` according to the governing RA contract.

The model may identify that a supplied rule appears incomplete, but it cannot fill the gap from general knowledge. A model's confident wording is not evidence that the supplied package contained the missing fact.

## 7. Model and configuration qualification

### 7.1 Qualification unit

Qualification is attached to a tuple, not to a model name alone:

```text
(model identity, runtime identity, task contract, behavior/configuration,
 policy profile, contract/schema versions, resource envelope)
```

A change to any behavior-affecting member invalidates or limits the existing qualification according to its declared impact. A patch-level runtime change, prompt/template change, output schema change, context projection change, quantization change or limit change must not be silently treated as equivalent.

### 7.2 Qualification evidence

The future qualification record should identify, at minimum:

| Evidence | Purpose |
| --- | --- |
| Model/runtime identity and integrity reference | Establish which executable capability was exercised. |
| Task/configuration contract version | Establish what the model was allowed to do. |
| Fixed synthetic challenge set | Exercise valid, incomplete, contradictory, ambiguous and adversarial-looking supplied content. |
| Expected structural outcomes | Check schema, enum, reference, abstention and limit behavior independently of semantic quality. |
| Human or deterministic oracle | Provide an external comparison basis; the model cannot qualify itself. |
| Resource and failure observations | Record latency, timeout, memory/size behavior, cancellation and retry consequences. |
| Protection observations | Verify egress, filesystem, command, persistence and audit boundaries applicable to the profile. |
| Qualification decision and expiry/change trigger | State who accepted the evidence and when it must be revisited. |

Qualification of one task does not qualify a model for another task. Qualification evidence itself is a project artifact with provenance and sensitivity; it must not contain confidential production documents merely to make the model appear more capable.

### 7.3 No self-qualification and no circular evidence

The model under qualification cannot be the sole evaluator of its own responses, define its own passing criteria, or confirm that its context was sufficient. A second model may assist an evaluation experiment only if the evaluation design identifies the external oracle and preserves the limitations; it does not remove the need for human accountability.

Operational review cannot rely on a qualification result whose required protection evidence is missing, stale or tied to another profile. A model may be available locally and still be `NOT_QUALIFIED` for TDG.

## 8. Runtime protection boundaries

### 8.1 Minimum logical deny list

Unless a separately approved and verified capability explicitly permits an operation, the model runtime must not have:

- arbitrary access to the TDG record store or review history;
- filesystem discovery outside the gateway-provided temporary input/output area;
- authority to read environment variables, credentials, tokens or private keys;
- command execution, code execution or tool/plugin invocation;
- network egress, DNS resolution or URL retrieval;
- direct database writes, file replacement or export publication;
- the ability to alter policy, qualification, actor identity or active run state;
- a mechanism to request hidden context expansion or bypass output validation.

The exact operating-system and runtime enforcement remains a later design/verification task. A prompt sentence saying “do not use the network” is not enforcement evidence.

### 8.2 Copy and retention boundaries

The gateway may create a bounded attempt projection and runtime buffer only after policy admission. It must record whether a copy was created, its classification, lifetime policy and deletion/retention outcome. Temporary copies cannot silently become canonical source records.

Raw prompts and model responses may contain sensitive content. The default laboratory retention policy should prefer hashes, structured metadata and bounded excerpts over unlimited raw duplication. The sealed profile must make the permitted raw-content retention, key handling, backup and deletion policy explicit before use.

### 8.3 Egress and destination controls

The gateway must identify every permitted output destination. A response can be returned to CMP-04 and CMP-06 only through the controlled contract; it cannot publish directly to Jira, Xray, email, cloud storage or another external endpoint. An export is a separate authorized operation governed by CMP-07 and the profile.

If a mandatory egress control or audit mechanism cannot be verified, dependent model work is blocked. Deterministic work that shares the same unverified protection boundary is blocked as well; it cannot be used as an escape route.

## 9. Resource, retry and cancellation contract

### 9.1 Bounded execution

An attempt references policy limits for:

| Limit | Required behavior when reached |
| --- | --- |
| Context record/field count | Stop projection and return an explicit context-limit outcome. |
| Input size or nesting depth | Reject or truncate according to policy; retain the action and exact consequence. |
| Output size | Stop/contain the response and mark it structurally unusable or incomplete. |
| Wall-clock time | Cancel if supported; otherwise mark the attempt timed out and prevent promotion. |
| Memory/CPU or runtime quota | Record resource failure; do not silently switch runtime or model. |
| Retry count | Stop at the configured bound; preserve each attempt and final operational cause. |
| Concurrent attempts | Respect the first workflow's one-active-run and configured concurrency policy. |

The numerical values remain open decisions. A missing limit is not interpreted as unlimited permission.

### 9.2 Retry identity and fallback

An identical authorized retry of an operation after a lost response may reconcile to the existing committed attempt outcome. A model retry after timeout or malformed output creates a new attempt identity with an explicit parent and reason. It must use the same approved tuple unless a human-controlled new request changes the configuration and starts a new run.

There is no silent fallback to another model, another prompt, a cloud service, a broader context or a weaker protection profile. If a configured capability is unavailable, the dependent work becomes `NOT_PERFORMED`, `INCOMPLETE` or `BLOCKED` according to the actual cause.

### 9.3 Cancellation and interruption

The operator can request cancellation of an active run. The coordinator stops starting new attempts, signals a running attempt where supported and reconciles committed versus uncommitted effects. A cancellation cannot convert a partial result into `COMPLETED`. The terminal run and each affected ledger entry retain the reason and availability consequence.

## 10. Response validation and promotion

### 10.1 Validation layers

Response handling is staged:

1. **Transport validation** — the gateway received a bounded response from the expected runtime and attempt.
2. **Resource validation** — size, time, encoding and output limits were respected.
3. **Schema validation** — required fields, allowed enums, cardinality and contract version are valid.
4. **Reference validation** — cited package, TC, evidence and locator identities exist in the selected context.
5. **Policy validation** — no prohibited authority, tool request, destination or context expansion is present.
6. **Semantic support review** — a qualified downstream service and/or human checks whether the suggestion is supported by supplied evidence.

Passing layers 1–5 does not prove that the model's claim is correct. Failing any required layer prevents promotion and leaves a cause-specific attempt outcome.

### 10.2 Promotion states

The following logical states are proposed:

| State | Meaning |
| --- | --- |
| `RECEIVED_UNVALIDATED` | Raw response was received within the operation boundary but is not yet usable. |
| `STRUCTURALLY_VALID` | Transport, resource, schema and reference checks passed. |
| `CANDIDATE_RECORDED` | The response became an explicitly typed candidate contribution linked to evidence. |
| `HUMAN_INTERPRETED` | An authorized human interpreted or confirmed its limited relevance; this is not TC approval. |
| `WITHHELD` | The response remains retained as evidence/diagnostic but cannot support the requested conclusion. |
| `REJECTED` | The response violated structural, policy or provenance rules and cannot enter the derived result set. |

An answer saying that a rule is missing cannot itself create a missing-rule fact. An answer proposing a boundary value cannot establish coverage unless the accepted test basis and the human/deterministic review support that conclusion.

### 10.3 Prompt-injection-like content

Supplied testware, documentation and model output may contain instructions addressed to an AI. The gateway treats them as content. It may pass them to a task whose purpose is to identify such content, but it never executes them or lets them override the envelope, policy, context manifest, limits or actor authority.

## 11. Failure, containment and safe outcomes

### 11.1 Cause-specific outcomes

| Situation | Gateway/run consequence |
| --- | --- |
| No current qualification for the tuple | Do not invoke; dependent work is `NOT_PERFORMED` or `BLOCKED` with qualification reason. |
| Context unavailable or insufficient | Do not widen scope; return `CONTEXT_INSUFFICIENT` and preserve the missing category. |
| Model timeout or resource exhaustion | Mark the affected attempt `INCOMPLETE`; retain operational evidence; no semantic finding is inferred. |
| Malformed, oversized or prohibited response | Withhold/reject the response; the entry remains incomplete or ungradable according to the actual stage. |
| Runtime process crash | Reconcile committed history; do not report unsaved output or rerun silently. |
| Mandatory policy/audit/protection failure | Stop dependent model and shared-boundary deterministic work; retain a safe diagnostic if permitted. |
| Optional debug/diagnostic failure | Continue only if the profile explicitly allows it and the required audit/history remains intact. |
| Cancellation | Stop new work and reconcile in-flight work; terminal state is not a successful completion. |
| Stale authority or qualification during processing | Reject the affected promotion/write; preserve already committed history and the revocation cause. |

### 11.2 Containment actions

Containment is a logical capability, not an assumed emergency implementation. A later security design must define who can stop the gateway, how running attempts are terminated, how temporary copies are handled, what evidence is retained and how restart/recovery is verified. The stop action cannot be delegated to the model.

### 11.3 No false success

The following are explicitly not success criteria:

- the model returned non-empty text;
- the parser found a JSON object without checking references and policy;
- the model expressed confidence;
- a timeout was followed by a second model without a recorded retry;
- a finding count was non-zero or zero;
- a human accepted a disposition without reviewing the supplied evidence;
- a deterministic path completed while the common protection/audit boundary was unavailable.

## 12. Laboratory and sealed profiles

### 12.1 Laboratory profile

The laboratory profile is the only immediate target for the project experiment. It uses public or synthetic material, a deliberately selected local runtime and a documented policy/configuration. It must still exercise the gateway, context minimization, validation, limits, audit and failure paths. “Local” is not used as a synonym for “confidentially safe.”

The laboratory profile may produce qualification evidence and synthetic reports, but those artifacts cannot authorize sealed use or prove suitability for a real project's confidential documentation.

### 12.2 Sealed profile

The sealed profile is a future, separately verified capability. Before any confidential package is admitted, it needs at least:

| Control area | Evidence required before use |
| --- | --- |
| Identity and role | Verifiable human identity, acting role and authorization on every protected operation |
| Input/storage | Protected source, package, temporary projection, backup and key boundaries |
| Runtime | Identified model/runtime build and enforceable filesystem, process and network restrictions |
| Egress | Explicit allowlist and denial evidence for external destinations |
| Secrets | No secret exposure to prompts/logs; controlled key lifecycle |
| Audit/history | Tamper-evident or otherwise verifiable operational and human history, including failure paths |
| Retention/deletion | Approved retention, deletion and recovery behavior for raw and derived model material |
| Verification | Reproducible checks showing that the profile actually enforces its stated boundary |

A sealed label is a policy result, not a model response or a configuration string supplied by the user. If any mandatory evidence is stale or unavailable, admission is refused or the affected operation is blocked.

### 12.3 Profile transition rule

There is no automatic laboratory-to-sealed promotion. A new profile, qualification context, protection evidence and human authorization are required. A package captured in one profile is not silently reclassified in another; the transfer/recapture decision must be explicit and auditable.

## 13. Diagnostics, provenance and observability

### 13.1 Minimum retained attempt metadata

Subject to profile-specific sensitive-content rules, the history should retain:

- attempt, operation, review-request, run and ledger identities;
- package version and selected evidence identities;
- task, model/runtime, behavior/configuration, policy and contract versions;
- qualification reference and validity decision;
- context-manifest summary, redaction/truncation markers and input/output hashes where available;
- start/end/cancellation/timeout/resource timestamps and retry parent;
- structural/policy validation outcomes;
- candidate class, promotion state and withheld/rejection reason;
- protection/audit status relevant to the attempt;
- human interpretation or disposition references, when later supplied.

The system must not log secrets merely to improve debugging. Raw prompt/response retention is a separately controlled decision and cannot be assumed from “debug mode.”

### 13.2 Diagnostic separation

Operational diagnostics describe what happened to the attempt. Assessment evidence describes what supports a finding or candidate. Human interpretation describes an accountable decision. These are linked but not interchangeable. A stack trace cannot become a business-rule justification; a model explanation cannot become source evidence merely because it is readable.

### 13.3 Reproducibility boundary

The record should make a later reproduction attempt possible by preserving the relevant versions, context manifest, limits and outcome. It must not promise bit-for-bit deterministic model output when the runtime, hardware or model configuration cannot provide it. A reproduction attempt is a new operation linked to the original, not a rewrite of history.

## 14. Proposed verification and STLC handoff

This section defines what must be challenged later; it is not a claim that the checks have passed.

| Verification slice | Representative challenge | Evidence expected |
| --- | --- | --- |
| Gateway routing | Assessment service tries to bypass CMP-05 or invoke a disallowed task. | Deterministic denial and retained policy reason. |
| Context minimization | Input contains unrelated package, credential-like field, URL and hidden instruction. | Projection excludes them; manifest records exclusions; no external retrieval. |
| Qualification | Same model changes task contract, prompt version, runtime build or profile. | Qualification is rejected/limited and no silent reuse occurs. |
| Output safety | Model returns valid-looking JSON with unknown IDs, extra authority fields or tool instructions. | Structural/reference/policy validation with no promotion or side effect. |
| Abstention | Required rule, expected result or source locator is absent. | Explicit insufficiency/abstention; no invented rule or source. |
| Limits | Slow response, oversized context, oversized output, memory pressure and retry exhaustion. | Cause-specific incomplete/blocked outcome and preserved attempts. |
| Cancellation | Operator cancels during queued and running attempts. | No new attempts start; committed work remains; terminal result is not false success. |
| Persistence | Response is lost after commit, or process crashes during finalization. | Idempotent reconciliation, no duplicate run, no unsaved success. |
| Shared protection | Audit, storage, identity or egress control becomes unavailable. | Dependent model and shared-boundary deterministic work stop safely. |
| Profile separation | Laboratory package is labeled sealed or sealed controls are missing. | Admission denial and explicit profile evidence. |
| Human boundary | Model suggests approval or repair; operator submits a changed TC. | Suggestion remains advisory; human-originated new package/version is required. |
| Evaluation separation | Qualification uses the same model as sole judge or leaks operational documents. | Evaluation is marked invalid/limited; no operational promotion. |

The STLC design will later split these into static contract checks, deterministic integration checks, controlled synthetic runtime trials and human review of evidence. Tests must preserve the distinction between model/runtime level, integration level, system-level black-box review and operational security verification.

## 15. Open decisions and follow-up allocations

The following decisions remain open and must not be guessed by the implementation:

| ID | Open decision | Why it matters | Proposed owner/activity |
| --- | --- | --- | --- |
| OD-SAD03-001 | Local runtime and endpoint/process boundary | Determines enforceable isolation, health checks and failure behavior. | B-01 implementation-ready architecture |
| OD-SAD03-002 | Exact task/contribution enumeration and schema | Determines response validation and forward compatibility. | SAD-04 contract design |
| OD-SAD03-003 | Numeric context, time, memory, output and retry limits | Balances an 8 GB-class local environment, useful review and safe containment. | Feasibility experiment plus SAD-04 |
| OD-SAD03-004 | Qualification dataset, oracle and requalification triggers | Prevents circular self-approval and stale capability claims. | B-02/B-09 evaluation design |
| OD-SAD03-005 | Runtime isolation and egress enforcement | “Local” alone does not prove confidentiality or no tool access. | B-09 security design |
| OD-SAD03-006 | Raw prompt/response retention and redaction policy | Aids diagnosis but may expose project material or secrets. | B-09 privacy/security design |
| OD-SAD03-007 | Protected temporary storage, keys, backups and deletion | Controls copies created for inference and recovery. | B-09 security design |
| OD-SAD03-008 | Cancellation semantics for the selected runtime | Determines whether an in-flight attempt can actually be stopped. | Runtime feasibility experiment |
| OD-SAD03-009 | Model behavior/configuration versioning and change impact | Prevents silent drift between qualification and operation. | SAD-04 contract design |
| OD-SAD03-010 | Sealed-profile identity and authorization enforcement | Logical roles alone are insufficient for confidential use. | B-09 and later verification gate |

Resolving these decisions may change this document or create a successor baseline. A missing answer is a visible design gap, not permission to choose a convenient default silently.

## 16. Self-check and completion boundary

Before this document can be proposed for acceptance, the author check must verify:

- every SAD-D-009–015 direction has a stated reason and a non-implementation boundary;
- every model invocation has a task, package/run subject, context manifest, limits and qualification reference;
- supplied content, deterministic results, model contributions and human decisions remain distinct;
- no model output can grant authority, expand scope, execute a tool or repair a TC;
- laboratory and sealed profiles have distinct admission and evidence rules;
- timeout, cancellation, retry, crash, malformed output and protection failure have explicit consequences;
- shared protection failure blocks the dependent deterministic path where required by RA-08;
- no external link or repository search is implied by a source locator or model request;
- no numeric limit, runtime, database, sandbox or encryption choice is presented as accepted;
- the 249-item accepted requirements baseline remains the traceability authority;
- follow-up decisions are recorded rather than filled by assumption;
- scope growth is controlled by reusing the shared gateway/protection model.

This self-check is documentary. It does not qualify a model, verify a sandbox, prove confidentiality or authorize implementation.

## 17. Proposed review gate

The Owner walkthrough should proceed by section:

1. Sections 1–3: purpose, sources, goals and inherited constraints;
2. Section 4: SAD-D-009 through SAD-D-015;
3. Sections 5–6: gateway responsibilities, invariants, task envelope and context projection;
4. Section 7: qualification and evaluation independence;
5. Sections 8–9: runtime protection, limits, retry and cancellation;
6. Sections 10–11: response promotion, failure and containment;
7. Sections 12–13: laboratory/sealed separation and diagnostics;
8. Sections 14–16: verification handoff, open decisions and self-check;
9. Section 17: correction record, baseline decision and possible GO to the next B-01 activity.

Acceptance of a section should be recorded with the exact scope of the acceptance. No acceptance of one section should be inferred to accept unreviewed physical mechanisms or implementation work.

## References

[gate]: ../requirements-analysis/ra-10/test-design-gatekeeper-requirements-analysis-readiness-v0.2.md
[sad01]: test-design-gatekeeper-sad-01-components-review-flow-v0.1.md
[sad02]: test-design-gatekeeper-sad-02-data-identity-contracts-v0.1.md
[ra03]: ../requirements-analysis/ra-10/test-design-gatekeeper-ra-03-review-package-content-provenance-validation-v0.4.md
[ra04]: ../requirements-analysis/test-design-gatekeeper-ra-04-scope-qualification-classification-boundaries-v0.2.md
[ra05]: ../requirements-analysis/ra-05/test-design-gatekeeper-ra-05-findings-dispositions-persistence-v0.2.md
[ra06]: ../requirements-analysis/ra-06/test-design-gatekeeper-ra-06-technique-applicability-design-coverage-v0.2.md
[ra07]: ../requirements-analysis/ra-07/test-design-gatekeeper-ra-07-llm-roles-qualification-v0.2.md
[ra08]: ../requirements-analysis/ra-08/test-design-gatekeeper-ra-08-confidentiality-security-privacy-v0.2.md
[ra09]: ../requirements-analysis/ra-09/test-design-gatekeeper-ra-09-data-representations-import-export-contracts-v0.2.md
[ra10]: ../requirements-analysis/ra-10/test-design-gatekeeper-ra-10-evaluation-acceptance-v0.2.md
