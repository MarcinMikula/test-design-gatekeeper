# Context

Canonical domain language for Test Design Gatekeeper.

This file is a glossary and orientation aid. It does not contain current sprint status, implementation plans, historical reasoning, or acceptance decisions.

Current project status belongs in `README.md` and the relevant closure/review records. Historical reasoning belongs in `LEARNINGS.md`. Normative requirements and design contracts remain authoritative in `docs/`.

If this glossary conflicts with an accepted governing artifact, the governing artifact wins.

---

## Product and project terms

**Test Design Gatekeeper (TDG)**

An evidence-grounded, ISTQB-informed assistant for reviewing functional test cases against a deliberately supplied and bounded test basis.

TDG supports human test analysis and review. It does not approve testware, certify completeness, repair source test cases autonomously, or act as an official ISTQB conformity authority.

**MVP**

The bounded first product scope: review of system-level functional black-box test cases for one feature or small business process, using supplied evidence and the initial four test-design techniques:

- Equivalence Partitioning;
- Boundary Value Analysis;
- Decision Table Testing;
- State Transition Testing.

MVP scope does not imply that every technique applies to every Review Package.

**increment**

A bounded implementation and verification slice authorized by the project governance process.

**work item**

A smaller deliverable inside an increment, with its own scope, evidence, and closure boundary.

**I-01**

The first implementation increment: bounded local intake/capture of one eligible native JSON Review Package candidate, immutable retained source/projection, receipt/identity behavior, restart inspection, and related foundation controls.

I-01 ends before substantive test-design review.

---

## Review Package and intake terms

**Review Package**

A deliberately bounded set of supplied scope, test-basis material, test cases, and provenance concerning one feature or small business process.

The package boundary is controlled by the human review scope. TDG does not silently broaden it.

**Review Package candidate**

Supplied material presented for intake before a trusted immutable package version has been established.

A candidate may be malformed, incomplete, disallowed, or otherwise unable to become a captured package version.

**submission context**

Trusted operation context outside supplied package content.

It includes the current operator, acting role, operating profile, approved data classification/purpose, selected input bindings, operation identity, and requested action.

A field inside a supplied file cannot grant or overwrite this authority.

**package identity**

The logical lineage of one package across deliberately versioned revisions.

It is distinct from any one captured package version.

**package version**

An immutable identity for the exact supplied content captured for assessment.

A content-changing recapture creates a distinct package version.

**package snapshot**

The coherent captured representation of one package version, including source inventory, supplied declarations, projection, provenance, capture metadata, and visible deficiencies.

It contains captured source truth for that version, not substantive review conclusions.

**source artifact**

One deliberately supplied source or opaque retained attachment together with its source locator, declared representation/profile, integrity evidence where available, and capture outcome.

**source locator**

A bounded reference to where supplied evidence came from inside an identified source artifact.

For JSON this may use an RFC 6901-style pointer. For CSV it may identify a logical record and, where trustworthy, a field/column location.

A locator is evidence provenance, not authority.

**provenance**

Information that identifies where supplied or derived information came from and how it entered the review record.

TDG distinguishes supplied declarations, supplied source metadata, system observations, human confirmations, and derived inference.

**external reference**

A URL, issue key, document path, filename, or similar value supplied as data.

It remains a reference unless its content is separately and deliberately supplied through an authorized intake path.

**external discovery**

Retrieval or search of material that was not deliberately included in the Review Package.

External discovery is outside the MVP review workflow.

**capture/import transformation**

Identified parsing, import mapping, or structural normalization used to establish the captured logical content of a package version.

If changed transformation behavior changes captured content, a new package version is required.

**assessment mapping**

A versioned behavior artifact used to interpret an already captured package during assessment.

Changing an assessment mapping against unchanged captured content creates a new assessment run, not a new package version.

**canonical content**

Captured source text, source field presence, supplied declarations, provenance, opaque retained content, and visible gaps/conflicts belonging to a package version.

Derived assessment results do not rewrite canonical captured content.

**mechanical projection**

A structured view produced from captured material without inventing semantic meaning.

A projection can support assessment but does not replace the original retained source.

---

## Native interchange terms

**control envelope**

The top-level native JSON contract with exactly:

```text
document_type
contract_version
content
```

for the applicable contract version.

Unknown fields inside `content` may be preserved. Unsupported or malformed control-envelope structure is not silently guessed.

**`review_package_input`**

A supplied declaration and content manifest.

It does not create trusted identity, a stored package version, qualification, human approval, or accepted findings by itself.

**`review_package_snapshot`**

TDG's coherent captured package representation.

It represents captured content and capture metadata, not substantive assessment conclusions.

**`import_receipt`**

TDG's intake outcome.

A package reference may exist only after coherent durable capture. Capture success does not imply that the package satisfies review minimums or that a substantive review occurred.

**`review_export`**

A controlled projection of selected retained results, evidence references, context, and human history.

It is read-only interchange/reporting, not a trusted history-restoration mechanism.

---

## Testware and accountability terms

**TC**

Test case.

TDG preserves the supplied TC and its deficiencies. It does not silently rewrite the source TC.

**test basis**

Supplied evidence against which testware may be interpreted or reviewed.

Examples can include requirements, acceptance criteria, business rules, risks, prior defects, or attributable experience-based rationale.

**basis element**

One identifiable supplied test-basis item.

A link alone is not automatically substantive basis content.

**human accountability**

An identified human accepts responsibility for the submitted testware and its use.

Eligibility depends on attributable human accountability rather than purity of authorship.

**origin**

The declared source/origin category of testware.

Canonical meanings include:

```text
HUMAN_AUTHORED
HUMAN_CONTROLLED_AI_ASSISTED
WITHOUT_ACCOUNTABLE_ADOPTION
OTHER
UNKNOWN
```

Origin and accountability are separate facts.

**human-controlled AI-assisted testware**

Testware developed with AI assistance but adopted and controlled by an identified accountable human.

TDG must not infer this status from writing style.

---

## Human roles and authority

Roles are functional responsibilities, not organizational job titles.

One person may hold multiple roles when the acting-role context is explicit. Combined roles do not create independent review.

**ROLE-01 — Review Operator**

Operates TDG, deliberately supplies/imports the Review Package, starts permitted assessment activity, responds to workflow requests when authorized, and inspects results.

Operation alone does not grant scope, domain, disposition, approval, security, or qualification authority.

**ROLE-02 — Review Scope Owner**

Owns the deliberately bounded feature/process and decides what supplied material belongs to that package boundary.

Scope authority does not permit TDG to search outside the submitted package.

**ROLE-03 — Testware Owner and Editor**

Owns accountable source testware and decides whether and how it is changed after review.

Actual test-case editing remains outside autonomous TDG control.

**ROLE-04 — Test Basis Authority**

Confirms, corrects, rejects, or leaves unknown an interpretation of supplied test basis within assigned competence.

Basis confirmation is not finding disposition or testware approval.

**ROLE-05 — Finding Disposition Authority**

Makes the attributable human decision on an individual finding or suggestion.

Typical dispositions are `ACCEPTED`, `REJECTED`, or `DEFERRED`; a new or reopened item is `PENDING`.

**ROLE-06 — Testware Approval Authority**

Owns formal organizational approval/readiness decisions outside the direct MVP decision model.

TDG cannot perform this role.

**ROLE-07 — TDG Administrator**

Operates approved environment/configuration and administrative functions.

Administrative access does not imply domain, finding, qualification, security, or testware-approval authority.

**ROLE-08 — Evaluation and Qualification Authority**

Makes qualification decisions for identified behavior-affecting models, prompts, controls, rules, and relevant configuration versions.

An evaluated component cannot qualify itself.

**ROLE-09 — Data and Security Authority**

Owns confidential-data authorization and the applicable security, retention, egress, backup, and trust-boundary decisions.

Local execution alone does not grant this authority.

**ROLE-10 — Project Owner**

Owns project scope, requirements decisions, change control, residual-risk decisions within authority, and SDLC phase gates.

---

## Review lifecycle terms

**review request**

A deliberate request to assess one exact package version under identified behavior/configuration and requested dimensions.

An identical authorized retry is not automatically a new request.

**assessment run**

One execution of identified TDG assessment behavior against one exact package version.

A new run has a new run identity. A terminal run does not resume.

**review cycle**

Submission, qualification, assessment, human inspection/disposition, optional external repair, and optional versioned re-review.

**re-review**

A later assessment after either:

- a new package version is supplied; or
- unchanged captured content is assessed under explicitly identified changed assessment behavior.

**assessment scope**

The package items and review dimensions TDG can support in one identified run.

**supported subset**

The portion of supplied items/dimensions that can be assessed without pretending that excluded, unclear, or unsupported material was reviewed.

**substantive assessment**

Evaluation of test-design quality or coverage after intake, policy, scope, and evidence prerequisites permit it.

Intake diagnostics and scope classification are not automatically substantive assessment.

**review result**

The scoped findings, suggestions, limitations, evidence, and run metadata produced by an assessment.

A result is bounded to what was actually assessed.

---

## Operational run state

Run state describes processing, not TC quality or human approval.

Canonical run states are:

**`REQUESTED`** — an identified assessment request exists for an existing package version.

**`RUNNING`** — authorized assessment processing has started.

**`COMPLETED`** — processing ended normally and every requested ledger entry has an explicit outcome, including limitations or non-performance.

`COMPLETED` does not mean "all tests are good" or "no gaps exist".

**`BLOCKED`** — a policy, authority, or package-level prerequisite prevents the run from continuing.

**`FAILED`** — an unhandled technical interruption prevents normal completion.

**`CANCELLED`** — an authorized cancellation ended the run before normal completion.

`BLOCKED`, `FAILED`, and `CANCELLED` are operational states, not assessment verdicts about testware.

---

## Assessment ledger terms

**assessment ledger**

The run-level inventory that accounts for supplied recognizable items and the requested review dimensions, including eligibility, qualification, capability, evidence sufficiency, outcome, and limitations.

The ledger makes non-performance visible instead of silently dropping work.

**ledger entry**

One identified item/dimension assessment boundary within a run.

It links prerequisites, attempts, evidence, and the cause-specific assessment outcome.

**item eligibility**

Whether a supplied item satisfies the applicable recognizability and accountable human-control conditions.

**domain qualification**

Whether an item is within the supported review domain.

Relevant outcomes include:

```text
IN_SCOPE
OUT_OF_SCOPE
UNDETERMINED
NOT_EVALUATED
```

`UNDETERMINED` is not the same as `OUT_OF_SCOPE`.

**evidence sufficiency**

Whether the supplied evidence supports a particular conclusion.

Evidence sufficiency is dimension-specific; one part of a TC can be assessable while another remains ungradable.

---

## Assessment outcomes

Assessment outcome is separate from operational run state.

**`ASSESSED`** — a bounded substantive review dimension has a safely recorded, evidence-supported conclusion.

**`UNGRADABLE`** — a supported conclusion cannot be made because necessary evidence is missing or conflicting.

**`NOT_PERFORMED`** — the dimension was not substantively reviewed for an explicit reason, such as ineligibility, exclusion, policy, unavailable capability, or not being requested.

**`INCOMPLETE`** — work started, but no safely completed conclusion is available for that entry.

These meanings must not be collapsed into one generic "failed" or empty result.

---

## Result availability

Availability describes how much safely completed substantive result is available. It is separate from run state and from finding disposition.

**`NOT_FINAL`** — the run is still `REQUESTED` or `RUNNING`.

**`NONE`** — the run is terminal and no safely completed substantive assessment entry is available. The cause must remain visible.

**`PARTIAL`** — at least one safely completed substantive entry exists, but the requested boundary was not fully assessed.

**`AVAILABLE`** — the explicit requested boundary has safely completed substantive assessment without the exclusions/undetermined/ungradable/incomplete conditions that would make it partial.

`AVAILABLE` is not a claim of global completeness or correctness.

---

## Findings, suggestions, and evidence

**review item**

A bounded reported claim, question, or recommendation attached to an identified subject and evidence.

A review item must not silently become a package-wide verdict.

**finding**

A claim about supplied testware or review basis with explicit evidence, derivation, subject, and history.

A finding remains distinct from its human disposition.

**suggestion**

A bounded, inspectable proposal or interpretation that may require human judgment.

A suggestion does not become true because it was generated by a model.

**derivation**

How a reported item was produced.

The core distinction is:

```text
DETERMINISTIC
LLM_ASSISTED
```

Derivation is independent of human disposition.

**deterministic finding**

A reproducible result derived from identified structured input, confirmed premises, rules/controls, and configuration.

Reproducibility does not prove that the upstream source or premise was correct.

**LLM-assisted suggestion**

A grounded but probabilistic contribution produced under an identified qualified task/configuration boundary.

It remains inspectable, uncertain, and rejectable.

**evidence item**

An inspectable basis for a claim, such as a supplied source locator, deterministic check, model-attempt reference, or attributable human interpretation.

Evidence does not grant authority.

**human disposition**

The attributable ROLE-05 decision on one finding/suggestion.

Canonical dispositions:

```text
PENDING
ACCEPTED
REJECTED
DEFERRED
```

Disposition does not rewrite the original derivation or evidence.

---

## Identity, history, and retry terms

**TDG-generated identity**

An opaque internal identity created by TDG for records such as package versions, runs, ledger entries, events, and exports.

TDG IDs must not embed mutable business meaning.

**source identity**

An identifier supplied by the source material or source system.

TDG preserves source identity where supplied but does not confuse it with its own internal identity.

**lineage**

The explicit relationship between versions/events over time.

A correction or revised submission creates a new attributable record/version rather than silently overwriting history.

**operation identity**

The identity of one durable operation attempt/request context.

It is used to distinguish an authorized retry from a new deliberate operation.

**request fingerprint**

A bounded identity of the request content/configuration relevant to idempotent retry behavior.

An identical authorized retry may return the prior committed result; a changed fingerprint must not be silently treated as the same request.

**idempotent retry**

Repeating the same identified authorized operation without duplicating the already committed effect.

Retry semantics do not mean deduplicating independent submissions merely because their bytes are identical.

**immutable history**

Previously committed package versions, runs, findings, interpretations, and human events retain their historical meaning.

Later correction appends or links new evidence; it does not erase the earlier state.

---

## Model and qualification terms

**deterministic control**

A reproducible control whose result follows from identified input, confirmed premises, explicit rules, and versioned behavior.

A deterministic control is not automatically semantically correct if its premises are wrong.

**model contribution**

A bounded probabilistic proposal produced by an identified model/runtime/task configuration.

Model output is untrusted data until structural and policy checks pass.

**model gateway**

The logical control boundary through which permitted model invocations pass.

It owns task authorization, context projection, limits, provenance, response validation, and safe failure.

The model runtime itself does not gain filesystem, policy, record-store, or human-decision authority.

**context projection**

The explicit allowlisted subset of retained evidence supplied to one model task.

The model cannot automatically expand that context by following references or searching outside the authorized boundary.

**qualification**

An attributable decision that an identified behavior configuration is permitted for a defined task/profile/resource envelope.

Qualification is tuple-specific rather than a generic "trusted model" flag.

**candidate contribution**

A model-produced proposal that passed structural/reference validation sufficiently to be retained for later bounded interpretation.

It is not automatically an assessment result, finding disposition, or human decision.

**abstention**

Withholding a conclusion when evidence, capability, or qualification is insufficient.

A justified abstention can be correct behavior.

---

## Evaluation terms

**human oracle**

An attributable human-adjudicated reference used to decide whether an evaluated TDG claim or behavior is supported for a defined evaluation boundary.

Model agreement does not replace the human oracle.

**development corpus**

Material used to create, tune, debug, or explore product behavior.

Development results are not independent acceptance evidence.

**qualification corpus**

Material used under a previously defined protocol to determine whether a frozen candidate/configuration is permitted for a particular role.

**held-out acceptance corpus**

Material reserved from tuning and used for decision-bearing product acceptance under a previously approved protocol.

Exposure destroys the claim that the same material is fresh held-out evidence for a later adapted candidate.

**reference family**

A bounded family of synthetic or otherwise controlled evaluation material with known relationships and human-reviewed expected meanings.

**mutation**

A deliberate change to reference material intended to create one known issue or challenge.

The mutation must be checked to confirm that it actually changed the intended oracle.

---

## Operating-profile and protection terms

**laboratory profile**

The development/experimental operating context intended for public or synthetic material.

Laboratory operation is not confidential-data authorization merely because TDG runs locally.

**sealed profile**

A future protected operating context requiring separately verified identity, policy, storage, egress, retention, audit, and related controls before confidential use.

A laboratory profile cannot simply be relabeled as sealed.

**trust boundary**

The set of verified technical and governance controls within which protected processing is allowed.

"Local machine" alone is not a complete trust boundary.

**fail closed**

Refuse the affected operation or action when required authority, policy, qualification, or protection evidence is absent or cannot be verified.

Fail-closed behavior preserves uncertainty instead of guessing permission.

---

## Implementation-foundation terms

**workspace**

The local TDG data area containing the initialized store and later retained TDG records.

A workspace is not a Review Package.

**empty-store initialization**

Creation of workspace metadata and the initial local store before any Review Package processing.

Initialization is not package import and does not imply review capability.

**capability manifest**

The machine-readable description of functions the current build exposes or keeps unavailable.

A capability being listed as unavailable is intentional product truth, not a failed attempt to hide unfinished functionality.

**qualified build**

A specific build/configuration for which the recorded verification evidence was actually executed.

A later governance decision does not silently rewrite the historical state embedded in that already-qualified build.

---

## Boundary rules worth remembering

```text
supplied fact
!= interpretation
!= model suggestion
!= deterministic derivation
!= human decision
```

```text
package identity
!= package version
!= review request
!= assessment run
```

```text
run state
!= assessment outcome
!= result availability
!= finding disposition
```

```text
capture success
!= minimum admissibility
!= substantive review
!= testware approval
```

```text
deterministic
!= automatically correct
```

```text
LLM-assisted
!= authorized
!= accepted
```

```text
local execution
!= sealed/confidential readiness
```

```text
traceability
!= implementation
!= executed verification
!= product acceptance
```

```text
work-item closure
!= increment acceptance
!= MVP acceptance
```

---

## Where to look for authority

Use this file for terminology only.

For authoritative detail, use:

- `README.md` — current public project status and supported capability;
- `LEARNINGS.md` — historical reasoning and turning points;
- `docs/governance/` — Charter and project-level scope;
- `docs/requirements-analysis/` — accepted behavior, authority, data, review, and evaluation requirements;
- `docs/solution-design/` — accepted design contracts and implementation boundaries;
- `docs/reviews/` — review findings, corrections, and Owner decisions;
- `docs/implementation/` — executed implementation evidence and work-item closure records.

Do not treat chat history, an old candidate snapshot, or this glossary as stronger than the accepted governing artifact.
