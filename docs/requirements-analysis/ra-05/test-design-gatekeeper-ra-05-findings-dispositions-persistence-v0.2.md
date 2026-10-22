# Test Design Gatekeeper

## RA-05 — Findings, Dispositions, and Persistence

| Field | Value |
| --- | --- |
| Basis | Accepted RA-05 v0.2, originally dated 2026-09-17 |
| Acceptance and gate | All 22 requirements and four policy decisions accepted; the verified clarification, v0.2 baseline and GO to RA-06 endorsed on 2026-09-18 in [SR-RA05-001 v0.2 / PG-RA05-001][review05] |
| Text maintenance | Consolidated on 2026-10-22; section numbers and identifiers retained |
| Decision authority | Project Owner |

This is the maintained contract for assessment results, human decisions and retained history. The [original v0.2 text][original] remains in Git history; earlier review hashes and byte counts identify that snapshot. Current capability and the development pause are described in [README.md](../../../README.md). Requirement acceptance does not establish implemented or tested behavior.

## 1. Purpose, sources, and boundaries

RA-05 defines what TDG records after a review and how a human can inspect the result, decide on a finding and follow later changes. Processing completion, available assessment results, human acceptance, source repair and formal testware approval have separate meanings.

The [Charter][charter] sets product scope; [RA-01][ra01] defines authority; [RA-02][ra02] defines workflow; [RA-03 v0.4][ra03] governs supplied content and identity; and [RA-04][ra04] governs scope qualification. Historical entry to RA-05 was granted by `PG-RA04-001` in [SR-RA04-001 v0.2][review04]. The [Requirements Analysis closure][phase] indexes accepted versions and decisions.

This document specifies logical records and behavior. Physical design, protection, retention periods and file formats belong to the sources in Section 12.2. The statuses are TDG policy, not an ISTQB workflow or an overall test-quality score. `Shall` states required behavior; `MUST` its priority.

Every new finding starts `PENDING`; only the four dispositions in Section 5.2 apply. TDG does not edit source test cases or formally approve testware. Laboratory work permits only public or synthetic data.

## 2. Logical records and identities

Record identity does not establish correctness. Source IDs, titles, repeated steps and matching hashes do not replace internal identities or prove equivalence across versions.

| Record | Required relationship and meaning |
| --- | --- |
| Captured package version | The immutable RA-03 source, declarations, projection, capture manifest, and lineage; referenced rather than rewritten by assessment |
| Assessment run | One unique run referring to exactly one captured package version, one explicit requested boundary, and the applicable behavior and policy context |
| Assessment ledger entry | One identifiable subject and requested review dimension; records prerequisites, qualification, capability, evidence sufficiency, and what was actually assessed |
| Review item | A finding or suggestion originating in exactly one run; identifies its subject, claim, derivation, evidence, limitations, and initial disposition |
| Basis-interpretation decision | An attributable ROLE-04 decision about a particular interpretation of identified supplied evidence; distinct from a review-item disposition |
| Disposition event | An attributable ROLE-05 judgment or reopening of one review item; appends history without replacing the original item |
| Impact or comparison record | A versioned observation about applicability or correspondence between identified records; cannot modify historical source or silently transfer decisions |
| Export instance | An authorized snapshot of identified records and a defined history boundary; distinct from the canonical retained record |

A subject may be a source fragment, TC, justified within-TC view or explicitly bounded group. Views retain parent identity and source locations without authoring a new TC. Group findings identify their affected members and boundary.

Problems before trusted package capture remain intake diagnostics; do not fabricate a package or run to hold them. Record only what the operating profile and [RA-08][ra08] permit.

## 3. Run state, assessment ledger, and result availability

### 3.1 Operational run state — accepted OD-RA05-001

Run state describes processing, not TC quality or human approval.

| State | Meaning | Permitted next states |
| --- | --- | --- |
| `REQUESTED` | A uniquely identified assessment request refers to an existing captured package version | `RUNNING`, `BLOCKED`, `FAILED`, `CANCELLED` |
| `RUNNING` | Authorized assessment activity has started | `COMPLETED`, `BLOCKED`, `FAILED`, `CANCELLED` |
| `COMPLETED` | Processing ended normally and every requested ledger entry has an explicit outcome, including limitations or non-performance | None |
| `BLOCKED` | A policy, authority, or package-level prerequisite prevents continuing the run | None |
| `FAILED` | An unhandled technical interruption prevents normal completion | None |
| `CANCELLED` | An authorized cancellation ended the run before normal completion | None |

The last four states are terminal. A new deliberate assessment has a new run identity; a terminal run never returns to `RUNNING`. Cancellation records its initiator and the applicable operator or administrative authority. A late cancellation request cannot overwrite a committed terminal outcome.

An expected unavailable capability can produce an explicit limited result and a `COMPLETED` run. It does not automatically mean `FAILED`, `BLOCKED`, or outside MVP. An isolated component error can likewise be contained if independent work completes and the affected entry is explicitly limited. Loss of the core processing path is a technical failure. Whole-run blocking is reserved for a prerequisite that actually affects the whole operation.

### 3.2 Assessment ledger

The ledger accounts for all supplied TC and recognizable candidate items, their qualification consequences, and the review dimensions requested for them. It retains unknown or unmapped material under RA-03. Dimensions not requested are identified as outside this assessment boundary; TDG does not silently add techniques or enlarge the package.

Each relevant entry preserves these separate questions:

| Axis | Recorded meaning |
| --- | --- |
| Item eligibility | Whether this item satisfies the applicable recognizability and human-accountability conditions, with its own evidence |
| Domain qualification | `IN_SCOPE`, `OUT_OF_SCOPE`, `UNDETERMINED`, or `NOT_EVALUATED`, with RA-04 criterion-level reasons |
| Capability | Whether the authorized, appropriately qualified capability is available for this representation and dimension |
| Evidence sufficiency | Whether supplied evidence supports this particular claim; missing and conflicting premises remain visible |
| Assessment outcome | One of the outcomes below, with source locations and limitations |

`NOT_EVALUATED` means that qualification was not attempted. `UNDETERMINED` means that the attempted qualification could not establish a conclusion. Neither is an established exclusion. The RA-04 precedence remains unchanged: a supported failed criterion can establish `OUT_OF_SCOPE` even when other criteria remain unknown.

| Assessment outcome | Meaning |
| --- | --- |
| `ASSESSED` | A bounded substantive review dimension has a safely recorded, evidence-supported conclusion; it may or may not produce a review item |
| `UNGRADABLE` | The dimension cannot receive a supported conclusion because necessary evidence is missing or conflicting |
| `NOT_PERFORMED` | The dimension was not substantively reviewed for an explicit reason, such as exclusion, item ineligibility, unavailable capability, policy restriction, or not being requested |
| `INCOMPLETE` | Work started but no safely completed conclusion for this entry is available |

Operational diagnostics, intake checks, and scope classification are not counted as completed substantive review dimensions. A supported observation about a missing TC element can be an assessed quality dimension while a separate technique dimension is ungradable. Detailed technique applicability and coverage meanings are defined in [RA-06][ra06].

Within-TC views must satisfy all RA-04 separability conditions. One supported view does not mark its entire parent TC as reviewed. All omitted assertions and their consequences remain visible.

### 3.3 Result availability

Availability is derived from safely retained assessment entries and processing state. It is independent of the number of findings and their human dispositions. Apply the first matching row.

| Condition | Availability | Required qualification |
| --- | --- | --- |
| Run is `REQUESTED` or `RUNNING` | `NOT_FINAL` | Any inspectable committed items are interim, bounded results |
| Run is terminal and no completed substantive assessment entry is safely available | `NONE` | Preserve the reasons: for example, ungradable evidence, no eligible subject, policy block, cancellation, or technical failure |
| Run is `COMPLETED`, at least one substantive entry is assessed, every requested dimension for the supplied TC inventory is assessed, and no supplied TC or assertion is excluded, undetermined, ungradable, or incomplete within that requested boundary | `AVAILABLE` | Available only for the explicit requested boundary; not a completeness or quality claim |
| Any other terminal run has at least one safely available completed substantive entry | `PARTIAL` | State every exclusion, unevaluated dimension, interrupted part, and affected original TC |

An explicit reason inventory prevents `NONE` from collapsing ungradable, blocked, failed, cancelled, and entirely excluded cases into one generic outcome. Intake or scope diagnostics may still exist when substantive availability is `NONE`. Access and retention policy can restrict inspection of any record; availability is not permission to display it.

An unrequested dimension does not by itself make availability partial. An excluded supplied TC or excluded assertion within a requested dimension does. Authorization to inspect a supported subset does not erase the remainder of the supplied inventory. Changing the captured package boundary follows RA-03 versioning.

### 3.4 Summaries and counts

Summaries show run state, availability, the requested boundary, and the counts of original TC fully assessed within that boundary, partially assessed, and not substantively assessed. These three mutually exclusive TC counts reconcile to the original identifiable TC inventory; unrecognized items are reported separately. A TC is fully assessed only when all its requested dimensions and relevant assertions are assessed without exclusions. Multiple views do not multiply its TC count. Reasons for non-assessment can overlap and therefore must not be presented as disjoint totals.

Finding and disposition counts are separate. A supported zero-item result means only **no reportable issues were identified by the stated review against the supplied evidence**. It does not mean complete technique coverage, correct requirements, repaired testware, readiness for release, or official ISTQB conformity. `COMPLETED` and all findings `ACCEPTED` cannot establish any of those claims either.

## 4. Review-item and evidence contract

Retain enough context for an authorized human to inspect a finding or suggestion and its premises.

| Content | Required meaning |
| --- | --- |
| Identity and subject | Internal item ID, package-version ID, originating run ID, and affected TC/view/source or explicitly bounded group |
| Claim and dimension | The exact alleged gap, inconsistency, or improvement opportunity; distinguish a source-basis issue from a TC-design issue |
| Evidence | Identifiable supplied source locations, relevant observed content, and dependencies on any normalized rule or human decision |
| Derivation | `DETERMINISTIC` or `LLM_ASSISTED`, with the applicable behavior artifacts and versions |
| Interpretation boundary | Supplied facts, derived interpretation, assumptions, uncertainty, conflicts, and relevant exclusions distinguished |
| Review assistance | An actionable question or bounded recommendation; no invented business rule or replacement source TC |
| Human history | Initial `PENDING` and subsequent attributable disposition events, separately from the original claim |

A claimed absence must identify what supplied material was inspected and what is missing. It cannot extend to unsubmitted documentation. Record unavailable evidence explicitly; do not reconstruct it from a link. This contract requires no severity score. Any impact label must disclose its evidence rather than invent business priority.

### 4.1 Derivation remains independent of disposition

| Item kind inherited from the Charter | Derivation and constraint |
| --- | --- |
| `DETERMINISTIC_FINDING` | `DETERMINISTIC`: a reproducible control over identified normalized input and confirmed structured premises; retain control, mapping, rule, and configuration versions |
| `REVIEW_SUGGESTION` | `LLM_ASSISTED`: a grounded, uncertain, rejectable interpretation; retain the relevant role, prompt, model, configuration, evidence, and qualification context |

Reproducibility does not prove source truth. A deterministic script using an unconfirmed LLM interpretation cannot establish a deterministic business or coverage conclusion. It may establish a narrower structural fact that does not depend on that interpretation.

An LLM explanation is a separately identified contribution; it cannot change the original deterministic claim, evidence or derivation. A new semantic claim needs its own grounded suggestion. Withhold unsupported conclusions regardless of confidence and record the limitation or clarification need. Human acceptance cannot supply missing evidence or change derivation.

## 5. Human decisions and their history

[RA-01][ra01] defines the roles: ROLE-04 decides test-basis interpretations, ROLE-05 accepts, rejects, defers or reopens findings, and ROLE-03 edits source testware. One role does not confer another's authority. Laboratory attribution does not establish enforced sealed-profile access control.

### 5.1 Basis interpretation is a separate decision

ROLE-04 may confirm, correct, reject, or explicitly leave an interpretation `UNKNOWN`. Retain the interpretation, exact evidence and version references, competing evidence, uncertainty, responsible human, acting role, rationale, and affected assessment. No decision yet means unconfirmed; it is not a fabricated human `UNKNOWN` decision.

A correction preserves the earlier interpretation and identifies the replacement. Record explicitly whether ROLE-04 confirms the corrected interpretation for the stated context; correction and confirmation may occur in one attributable action. Finding acceptance by ROLE-05 cannot substitute for this decision. Lack of a separate domain expert cannot authorize LLM self-confirmation.

A decision about already supplied evidence is an assessment record, not a change to the captured package. Newly supplied business rules or clarification documents enter a new package version. A first applicable ROLE-04 decision may support a not-yet-assessed entry in an active run when it neither replaces a premise already applied in that run nor changes a configured assessment behavior artifact. Record the exact decision version used. Replacing a previously applied interpretation, changing an assessment behavior artifact, or reassessing a committed entry requires a new run. A terminal run cannot resume. Initial human confirmation of an evidence interpretation is distinct from modifying a configured rule, mapping, control, prompt, model, runtime, or other behavior artifact; it is not an exception to RA03-REQ-045.

### 5.2 Finding dispositions — accepted OD-RA05-002

| Disposition | Meaning |
| --- | --- |
| `PENDING` | No current human judgment; also the state after explicit reopening |
| `ACCEPTED` | ROLE-05 regards the identified finding or suggestion as justified in its stated context |
| `REJECTED` | ROLE-05 rejects the identified finding or suggestion, with a reason |
| `DEFERRED` | ROLE-05 deliberately postpones a decision, with the unresolved question or dependency recorded |

`ACCEPTED` does not mean that source TC have changed or that corrective work was verified. `UNKNOWN` is not a fifth finding disposition. A reviewer unable to decide can defer, while any ROLE-04 unknown interpretation remains separately visible.

| Current disposition | Action | Result and authority |
| --- | --- | --- |
| New item | TDG records it | `PENDING`; system initialization, not a human judgment |
| `PENDING` | Accept, reject, or defer | Corresponding state; attributable ROLE-05 decision and rationale |
| `ACCEPTED`, `REJECTED`, or `DEFERRED` | Reconsider and select a different decided state | New attributable ROLE-05 decision and rationale; earlier event retained |
| `ACCEPTED`, `REJECTED`, or `DEFERRED` | Explicitly reopen | `PENDING`; ROLE-05 records the reason for reconsideration |
| Any state | Repeat the same identified operation | No duplicate transition; retain the original operation result |

A new attempt to select the already current state is not a state transition. A separate attributable note may record additional reasoning without fabricating a decision change. An LLM, automatic comparison, admin privilege alone, or a new package submission cannot disposition or reopen a finding.

### 5.3 Event contract

Each authority-bearing event retains its identity, target and assessment version, actor or local actor ID, acting role, action, previous/resulting state where relevant, rationale, evidence references, recorded time and authoritative order within the target history. Source timestamps remain distinct from TDG record times; equal or changed clocks cannot reorder decisions.

Record self-review when the reviewer authored or owns the affected testware under RA-01. Keep combined roles visible. Unknown independence is not independent review, and later role changes do not relabel past actions.

A disposition needs an identifiable retained item and the evidence required for that judgment. Missing evidence or an explicitly unconfirmed dependency prevents accepting a dependent claim as established. This does not guarantee TDG can determine every human judgment's truth. ROLE-05 may accept a grounded clarification request or a supported uncertain suggestion without confirming the underlying rule. Reopening an old item may cite evidence loss or an impact record without claiming the missing source was inspected.

Concurrent decisions cannot silently overwrite each other. Expose a stale action as a conflict requiring renewed human consideration; retain both the existing history and the attempted action's outcome as policy permits.

## 6. Version impact and comparison — accepted OD-RA05-003

| Change or action | Required consequence |
| --- | --- |
| Source TC, supplied basis, scope, provenance declaration, or capture projection changes | New captured package version under RA-03; prior retained version remains unchanged |
| An assessment behavior artifact changes against unchanged captured content | New run referencing the same package version and the changed behavior context, including when no substantive entry has yet committed |
| A first applicable ROLE-04 decision concerns an entry not yet assessed in an active run, without replacing a premise already applied or changing a configured behavior artifact | The active run may continue under Section 5.1; retain the exact decision version used |
| A previously applied interpretation changes or a committed entry is reassessed | New run referencing the same package version and the actual decision context; preserve earlier conclusions |
| Human deliberately repeats an unchanged assessment | New run; nondeterministic output is not represented as the earlier result |
| Human dispositions an item | New event on that item; neither the source package nor the originating claim changes |
| A newly created item resembles an earlier item | New item identity and `PENDING`; no automatic inheritance of human disposition |

Pending or deferred findings do not block a new package submission or authorized assessment. A new version neither proves repair nor closes earlier findings or erases their rationale.

### 6.1 Comparison observations

An explicit authorized comparison identifies selected runs, package versions, subjects, relevant dimensions and behavior contexts, with evidence for correspondence and uncertainty. Similar titles, generic steps, identical preconditions or matching source IDs alone cannot establish the same issue.

| Observation | Required evidence and limit |
| --- | --- |
| `OBSERVED_AGAIN` | Supported correspondence to a separately recorded item in the later assessment; human disposition still belongs to each item |
| `NOT_REDETECTED_IN_COMPARABLE_REVIEW` | Supported corresponding subject and check, sufficient current evidence, compatible interpretation/behavior context, and a completed relevant assessment with no corresponding item; this is an observation, not verified repair |
| `COMPARISON_UNDETERMINED` | Correspondence or comparability is unsupported, the relevant dimension was not assessed, or evidence is unavailable; retain the specific reason |

Without a selected predecessor, there is no comparison and no basis for claiming an issue is new. Absence from a later item list does not establish non-redetection. A failed or cancelled run can support that observation only if the relevant entry independently completed, is safely retained and satisfies every comparability condition. Overall failure does not erase supported repeated findings or prove repair.

Comparison assistance remains derived, with evidence, behavior identity and uncertainty, and cannot change human decisions. [RA-07][ra07] governs any permitted LLM role; this contract selects no automatic semantic matcher.

### 6.2 Current-use limitations and source boundaries

When TDG receives attributable evidence of a relevant change, it records an impact notice on the affected retained result. Examples are changed package context, withdrawn qualification of a used behavior version, a corrected premise or lost evidence. Separate the historical result from its fitness for present reuse. Until impact is evaluated, reuse applicability is undetermined.

An impact notice cannot rewrite a finding, change its historical derivation or replace its disposition. ROLE-04 controls interpretation, ROLE-08 behavior qualification, and ROLE-05 reconsideration or reopening; TDG cannot invent their decisions.

Inspecting or comparing selected history does not add it to a new package's test basis. TDG cannot search unrelated stored documents to fill gaps. A human must deliberately supply earlier content through the controlled package boundary before it can support a new substantive review.

## 7. Local persistence, recovery, retention, and export

### 7.1 Retained logical content — accepted OD-RA05-004

The accepted direction is local, organization-controlled persistence. Retain linked, distinguishable package versions, TC identities and supplied names, runs, ledger outcomes, findings, evidence, interpretation decisions, dispositions, impact/comparison records and exports. Capture transformations remain separate from assessment rules, mappings, controls, prompts, models, configuration and applicable qualification/policy records. Do not attribute a result to unused behavior artifacts.

Evidence references must resolve to authorized retained material or give an explicit unavailability reason. A finding need not copy an entire source, and an export need not include all source bodies. Minimize duplication and absolute workstation paths. Local storage alone does not establish confidentiality, sealed-profile readiness or recoverability.

### 7.2 Save, concurrency, and retries

TDG reports a save as successful only when the intended logical record and the references required for its integrity have been durably recorded together. It must not expose a saved disposition pointing to an item that never committed, a final result with missing required ledger entries, or an export claiming an uncommitted decision. An unsaved preview remains visibly unsaved and cannot be confused with retained history.

Historical claims and authority-bearing events are not edited in place. Corrections and state changes append attributable records; current-state views can be derived from retained history. This is a behavioral requirement, not a mandate for a particular database or event-sourcing architecture.

A retry of the **same identified operation with the same content** returns the existing committed outcome when it already succeeded. Reusing that operation identity for different content produces an explicit conflict. A **new deliberate assessment request** creates a new run even when its package and parameters equal an earlier request. Identical content must not collapse independent package or run identities.

### 7.3 Failure, cancellation, and recovery

On failure or cancellation, retain only safely committed records permitted by policy. Completed independent assessment entries remain distinguishable from interrupted, provisional, or never-started work. Result availability follows Section 3; diagnostics alone cannot establish a partial substantive review.

Recovery must not present an interrupted `RUNNING` record as completed without evidence. It records the interruption and reconciles it to an explicit terminal outcome, normally `FAILED` when no prior terminal decision was committed. A previously committed terminal decision remains authoritative. Any subsequent assessment uses a new run. No unattended recovery re-executes assessment or external data retrieval under an old identity.

Neither source bytes nor old decisions are silently overwritten to make recovery appear successful. Detailed backup media, restore procedures, durability mechanisms, and security verification belong to RA-08 and Solution Design.

### 7.4 Retention and authorized deletion

Immutability applies while records are retained; it does not require indefinite retention. ROLE-09 approves retention, deletion, logging, backup and export policy; ROLE-07 executes authorized operations. Missing policy or authority cannot be replaced by a TDG decision.

Deletion must account for dependencies so surviving results do not appear fully evidenced after their sources are removed. Keep a minimal attributable deletion or evidence-unavailability record only where policy permits. If policy requires removing that record too, history preservation does not override it.

Do not retrieve deleted evidence from external references or unsubmitted sources. Deletion does not resolve a finding. Claims about erasure from backups or prior exports require the scope and verification set by policy; deleting an active copy is insufficient. Specific periods and mechanisms follow [RA-08][ra08] and the authorized operating policy.

### 7.5 Controlled export

A deliberate authorized local export identifies its instance, package version, run, selected content, applicable policy and exact disposition/history boundary. Preserve run state, availability, scope, omissions, derivation, uncertainty, human decisions and non-approval meaning. Later decisions do not alter an earlier export; a new export has a new attributable instance.

Viewing, persistence and export are distinct operations. Export denial or failure must not corrupt the canonical record. Export neither edits test cases nor publishes directly to Jira, Xray or Zephyr. [RA-09][ra09] governs formats; [RA-08][ra08] governs policy enforcement and protection.

## 8. Synthetic boundary examples

These fragments illustrate the accepted record behavior. They are not complete packages, executed tests, model-capability evidence or a finished benchmark. Assume permitted synthetic input and the stated prerequisite evidence. When those assumptions do not hold, apply the relevant input, policy and assessment rules.

| ID | Situation | Expected record consequence |
| --- | --- | --- |
| RA05-EX-01 | ROLE-05 accepts a grounded observation that a customer-creation TC lacks an expected result; the tester has not edited the TC | Item `ACCEPTED`; original TC and package unchanged; no repair or approval claim |
| RA05-EX-02 | An identified deterministic control reports a confirmed-rule contradiction, and an LLM explains it | Original deterministic claim retained; explanation visibly LLM-assisted; no semantic addition hidden in the original item |
| RA05-EX-03 | A model confidently alleges a missing discount rule with no supporting supplied evidence | Unsupported conclusion withheld; evidence limitation or clarification need recorded; no deterministic promotion or automatic acceptance |
| RA05-EX-04 | All requested dimensions of the supplied eligible inventory have supported conclusions and no findings | `COMPLETED` + `AVAILABLE`; scoped zero-item statement only |
| RA05-EX-05 | The sole requested substantive dimension cannot be assessed because its necessary business premise remains conflicting | `COMPLETED` + `NONE`; explicit ungradable reason, competing evidence, and ROLE-04 clarification need |
| RA05-EX-06 | One TC is fully assessed, a second has a safe functional view with an excluded performance assertion, and a third is an established component test | `COMPLETED` + `PARTIAL`; original-TC counts: one fully, one partially, one not substantively assessed; excluded does not mean defective |
| RA05-EX-07 | A required qualified LLM role is unavailable, but independent supported deterministic dimensions complete | `COMPLETED` + `PARTIAL`; capability limitation retained, no substitute model or outside-scope inference |
| RA05-EX-08 | A core failure occurs after one independent substantive entry commits; another remains incomplete | `FAILED` + `PARTIAL` where the retained entry remains safe and inspectable; no whole-run completion claim |
| RA05-EX-09 | Cancellation happens before any substantive result commits | `CANCELLED` + `NONE`; safely retained diagnostics remain distinguishable from findings |
| RA05-EX-10 | ROLE-04 leaves a source-rule interpretation unknown, while ROLE-05 wants to accept a dependent claim as established | Separate ROLE-04 decision retained; unsupported acceptance prevented; ROLE-05 can defer pending sufficient evidence |
| RA05-EX-11 | A revised TC is supplied and the corresponding dimension is reviewed again without redetecting an earlier issue | New package and run; comparison only when correspondence and comparability are supported; old disposition not auto-resolved |
| RA05-EX-12 | The later review has no corresponding finding because that dimension could not run | `COMPARISON_UNDETERMINED` with non-assessment reason; absence is not evidence of repair |
| RA05-EX-13 | A save response is lost after committing; the operator retries the same operation and later deliberately requests a new assessment | Retry returns the existing record without duplication; the later deliberate request creates a new run |
| RA05-EX-14 | A TC author also holds ROLE-05; an administrator without that role attempts the same disposition action | Author action is attributable self-review; admin privilege alone is insufficient; lab attribution does not prove enforced RBAC |
| RA05-EX-15 | Approved retention removes evidence needed to recheck an old item; an earlier export still exists | Policy-permitted impact/history records expose unavailability; no hidden retrieval, repair inference, or unsupported claim that the earlier export was erased |

## 9. Accepted requirements

All 22 requirements remain MUST / ACCEPTED, with statements, priorities and traces unchanged. [SR-RA05-001 v0.2][review05] also records endorsement of the supporting clarification in Sections 5.1 and 6 and VAL-006/009.

| ID | Requirement | Priority | Status | Primary upstream trace |
| --- | --- | --- | --- | --- |
| RA05-REQ-001 | TDG shall distinguish the records and identities in Section 2, bind every run to exactly one captured package version, and preserve valid subject, evidence, and history references without treating source labels or content equality as identity. | MUST | ACCEPTED | RA02-REQ-017; RA03-REQ-013, RA03-REQ-048, RA03-REQ-049 |
| RA05-REQ-002 | TDG shall implement the run meanings and permitted transitions in Section 3.1, retain terminal reasons and human or system event origin with applicable authority for human actions, and prevent a terminal run from resuming assessment. | MUST | ACCEPTED | RA02-REQ-006, RA02-REQ-029, RA02-REQ-032, RA02-REQ-033 |
| RA05-REQ-003 | TDG shall retain the Section 3.2 assessment ledger, separating item eligibility, domain qualification, capability, evidence sufficiency, and substantive assessment outcome while preserving RA-04 precedence and separability. | MUST | ACCEPTED | RA04-REQ-001, RA04-REQ-005, RA04-REQ-007, RA04-REQ-013 |
| RA05-REQ-004 | TDG shall derive result availability using Section 3.3, preserve specific reasons for absent or partial review, and prevent finding counts or human dispositions from determining availability. | MUST | ACCEPTED | RA02-REQ-013, RA02-REQ-014, RA02-REQ-022, RA02-REQ-032 |
| RA05-REQ-005 | TDG shall produce bounded summaries and reconcilable original-TC counts under Section 3.4, distinguish diagnostic-only and zero-item substantive outcomes, and make no unsupported completeness, quality, repair, approval, or ISTQB-conformity claim. | MUST | ACCEPTED | RA02-REQ-024, RA02-REQ-034; RA04-REQ-008, RA04-REQ-015 |
| RA05-REQ-006 | Each reported finding or suggestion shall satisfy the evidence and subject contract in Section 4, distinguish supplied facts from interpretation and uncertainty, and identify missing or unavailable evidence without inventing source content. | MUST | ACCEPTED | RA02-REQ-022, RA02-REQ-025; RA03-REQ-020, RA03-REQ-038 |
| RA05-REQ-007 | TDG shall preserve the derivation rules in Section 4.1, including confirmed premises for deterministic business conclusions, attributable LLM behavior, separate explanatory contributions, and withholding unsupported conclusions. | MUST | ACCEPTED | RA02-REQ-019, RA02-REQ-020, RA02-REQ-021; RA03-REQ-039 |
| RA05-REQ-008 | TDG shall record ROLE-04 interpretation decisions and their evidence, uncertainty, correction history, and assessment impact separately from finding dispositions under Section 5.1; absence of authority shall not be replaced by model self-confirmation. | MUST | ACCEPTED | RA01-REQ-005; RA02-REQ-016; UC-RA02-004 |
| RA05-REQ-009 | Every newly created review item shall start with disposition PENDING, including an item resembling a previously accepted, rejected, or deferred item; derivation and prior-run history shall not supply an automatic human judgment. | MUST | ACCEPTED | RA02-REQ-023, RA02-REQ-028, RA02-REQ-030 |
| RA05-REQ-010 | TDG shall support the four inherited dispositions and Section 5.2 transitions through ROLE-05 decisions, require attributable rationale, and prevent disposition from implying source repair, confirming a source rule, or accepting an unsupported claim as established. | MUST | ACCEPTED | RA01-REQ-007, RA01-REQ-008, RA01-REQ-014; RA02-REQ-026, RA02-REQ-034 |
| RA05-REQ-011 | TDG shall preserve the event information, acting authority, order, and self-review context in Section 5.3 without erasing prior decisions or presenting unknown independence as independent review. | MUST | ACCEPTED | RA01-REQ-002, RA01-REQ-013, RA01-REQ-015; RA02-REQ-027, RA02-REQ-030 |
| RA05-REQ-012 | TDG shall apply the package, run, decision, and item consequences in Sections 5.1 and 6; new submissions and reassessments shall neither overwrite historical records nor automatically resolve earlier items. | MUST | ACCEPTED | RA03-REQ-043, RA03-REQ-044, RA03-REQ-045, RA03-REQ-046, RA03-REQ-047; RA02-REQ-028 |
| RA05-REQ-013 | TDG shall record selected cross-run comparisons under Section 6.1 with explicit correspondence, comparability evidence, and uncertainty; non-redetection shall not establish repair or transfer human disposition. | MUST | ACCEPTED | RA02-REQ-030; RA03-REQ-047, RA03-REQ-048; RA04-REQ-012 |
| RA05-REQ-014 | TDG shall support authorized inspection of retained result context and selected history, expose unavailable evidence, and preserve the supplied-only assessment boundary when viewing, comparing, or exporting records. | MUST | ACCEPTED | RA02-REQ-002, RA02-REQ-003, RA02-REQ-025; RA03-REQ-005, RA03-REQ-019 |
| RA05-REQ-015 | TDG shall make attributable changes affecting present reuse visible under Section 6.2, preserve the original result and human history, and avoid representing unevaluated impact as established current validity. | MUST | ACCEPTED | RA01-REQ-010; RA02-REQ-018, RA02-REQ-030; RA04-REQ-012 |
| RA05-REQ-016 | TDG shall retain the linked local record set in Section 7.1 within the applicable profile and policy, distinguish capture from assessment behavior, and preserve inspectable evidence references or explicit unavailability. | MUST | ACCEPTED | Charter Section 10.5; RA02-REQ-018, RA02-REQ-022; RA03-REQ-006, RA03-REQ-030 |
| RA05-REQ-017 | TDG shall report persistence success only for coherent durable logical records, distinguish unsaved previews, append historical changes, and expose conflicting stale writes rather than silently overwriting human decisions. | MUST | ACCEPTED | RA01-REQ-015; RA02-REQ-030; RA03-REQ-043, RA03-REQ-049 |
| RA05-REQ-018 | TDG shall distinguish retry of the same identified operation from a new deliberate request under Section 7.2, preventing duplicate committed effects and identity reuse with different content without merging independent runs or packages. | MUST | ACCEPTED | RA02-REQ-017, RA02-REQ-029; RA03-REQ-046, RA03-REQ-048 |
| RA05-REQ-019 | TDG shall preserve safe committed outcomes during failure, cancellation, and recovery under Section 7.3, explicitly account for interrupted work, and prevent recovery from fabricating completion or silently reassessing under a terminal run identity. | MUST | ACCEPTED | RA02-REQ-032, RA02-REQ-033; RA03-REQ-049 |
| RA05-REQ-020 | TDG shall apply authorized retention and deletion under Section 7.4, retain only policy-permitted history, expose lost evidence dependencies, and make no unsupported claim about repair, recovery, or erasure from other copies. | MUST | ACCEPTED | RA01 AUTH-12; RA01-REQ-009, RA01-REQ-011, RA01-REQ-015; Charter Sections 10.5 and 13 |
| RA05-REQ-021 | TDG shall create controlled local exports under Section 7.5 with exact record and history boundaries, preserve limitations and human decisions, and keep export failure or denial separate from canonical persistence. | MUST | ACCEPTED | RA02-REQ-031, RA02-REQ-034; RA03-REQ-049 |
| RA05-REQ-022 | TDG shall apply the inherited role and operating-profile boundaries to record operations, prevent admin or viewing access from conferring content authority, preserve laboratory restrictions, and neither edit source TC nor perform formal testware approval. | MUST | ACCEPTED | RA01-REQ-003, RA01-REQ-006, RA01-REQ-009, RA01-REQ-011, RA01-REQ-016; RA03-REQ-042 |

## 10. Validation obligations and direct traceability

These obligations guide test analysis and design; they are not executed tests. Every requirement has at least one direct VAL link and every VAL references existing RA05 requirements. Those links do not by themselves establish adequate test coverage.

| ID | Validation obligation | Direct requirement trace |
| --- | --- | --- |
| RA05-VAL-001 | Inspect and exercise record relationships: one package per run, legitimate view/group subjects, unique internal IDs despite repeated titles and source IDs, and no fabricated run for pre-capture failure or dangling committed references. | RA05-REQ-001, RA05-REQ-016, RA05-REQ-017 |
| RA05-VAL-002 | Cover every permitted run transition and representative prohibited transitions, including terminal restart, completion after failed processing, late cancellation, expected missing capability, and terminal reasons that apply only to a subset. | RA05-REQ-002, RA05-REQ-003, RA05-REQ-019 |
| RA05-VAL-003 | Use mixed, undetermined, excluded, and safely separable TC; verify independent axes, known-exclusion precedence, complete inventory, non-duplicated original-TC counts, and visibility of excluded assertions. | RA05-REQ-003, RA05-REQ-005 |
| RA05-VAL-004 | Exercise all Section 3.3 rows and boundary combinations: no substantive entry, diagnostics only, all requested dimensions assessed with zero findings, ungradable evidence, excluded TC, partial views, unrequested dimensions, and failed/cancelled runs with or without safe entries. | RA05-REQ-002, RA05-REQ-004, RA05-REQ-005 |
| RA05-VAL-005 | Inspect claim/evidence contracts for deterministic and LLM-assisted items; challenge unconfirmed structured premises, unsupported high-confidence claims, missing source locators, explanatory semantic additions, and attempted automatic disposition. | RA05-REQ-006, RA05-REQ-007, RA05-REQ-009 |
| RA05-VAL-006 | Verify ROLE-04 confirmation, correction, rejection, explicit unknown, and absence of decision; retain competing evidence and old interpretations; distinguish a decision on supplied evidence from new supplied business content and from ROLE-05 acceptance. Contrast first applicable confirmation before dependent assessment with replacement of an interpretation already applied in the run. | RA05-REQ-008, RA05-REQ-011, RA05-REQ-012 |
| RA05-VAL-007 | Cover the disposition transition table, explicit reopening, rationale, no-op actions, deferred judgment, self-review, and unsupported acceptance attempts; confirm that no decision edits a TC, establishes repair, or implies approval. | RA05-REQ-009, RA05-REQ-010, RA05-REQ-011, RA05-REQ-022 |
| RA05-VAL-008 | Present simultaneous decisions against the same prior state, retries, equal timestamps, and changed role assignments; verify visible conflict, authoritative event order, retained actors, and unchanged historical self-review attribution. | RA05-REQ-011, RA05-REQ-017, RA05-REQ-018 |
| RA05-VAL-009 | Compare source recapture, changed assessment mapping, first applicable interpretation confirmation, replacement of an applied interpretation, unchanged deliberate rerun, and new submission with unresolved old items; verify the Section 6 package/run consequences and new-item PENDING. Include a behavior-artifact change before any substantive entry commits: a new run is still required. | RA05-REQ-009, RA05-REQ-012, RA05-REQ-018 |
| RA05-VAL-010 | Challenge comparisons with copied steps, duplicate source IDs, revised scope, changed rules, absent capability, interrupted relevant work, and trustworthy completed relevant work; verify observation limits, no inherited disposition, and no automatic history injection into the test basis. | RA05-REQ-013, RA05-REQ-014 |
| RA05-VAL-011 | Supply a corrected premise, withdrawn qualification, changed context, and lost evidence; verify attributable current-use limitations, original-result preservation, undetermined unevaluated impact, and human-controlled reconsideration. | RA05-REQ-008, RA05-REQ-014, RA05-REQ-015 |
| RA05-VAL-012 | Inject failure around logical saves and responses, then recover or retry; verify no false save success, no orphan decisions, safe committed entries, no duplicate effect, different-content conflict, and no reassessment under a recovered terminal identity. | RA05-REQ-001, RA05-REQ-016, RA05-REQ-017, RA05-REQ-018, RA05-REQ-019 |
| RA05-VAL-013 | Review and later test allowed role combinations and denied operations: viewer, operator, basis authority, disposition authority, administrator, and security authority; distinguish laboratory attribution from sealed enforcement and retain the protected-data prohibition. | RA05-REQ-008, RA05-REQ-010, RA05-REQ-014, RA05-REQ-022 |
| RA05-VAL-014 | Apply a defined synthetic retention policy to source, result, and dependent history; verify authorized execution, policy-limited audit survival, explicit evidence unavailability, no retrieval of deleted material, and no unverified backup/export erasure claim. | RA05-REQ-014, RA05-REQ-015, RA05-REQ-016, RA05-REQ-020 |
| RA05-VAL-015 | Export selected versions and dispositions at a defined history boundary; then change a disposition or deny/fail another export. Verify exact snapshot semantics, limitations, canonical-record integrity, destination-policy handling, and absence of approval or write-back. | RA05-REQ-011, RA05-REQ-014, RA05-REQ-021, RA05-REQ-022 |
| RA05-VAL-016 | Walk through an accepted finding, external TC revision, new captured package, reassessment, comparison, and optional human reconsideration; include partial or failed reassessment and confirm that acceptance, non-redetection, repair, and formal approval never collapse into one milestone. | RA05-REQ-004, RA05-REQ-005, RA05-REQ-006, RA05-REQ-010, RA05-REQ-012, RA05-REQ-013, RA05-REQ-019 |

## 11. Accepted policy decisions

The Owner accepted all four decisions with v0.1 and subsequently endorsed the v0.2 clarification. [SR-RA05-001 v0.2][review05] preserves the sequence and scope of those decisions.

| ID | Decision | Accepted recommendation | Status |
| --- | --- | --- | --- |
| OD-RA05-001 | Operational states, ledger outcomes, availability, and counting | Accept Section 3: separate axes, explicit non-success reasons, normal completion compatible with limited or absent substantive review, and no quality implication | ACCEPTED |
| OD-RA05-002 | Human disposition transitions and evidence history | Accept Section 5: retain the four inherited dispositions; require attributable rationale and ROLE-05 reopening; separate ROLE-04 interpretation decisions and preserve self-review | ACCEPTED |
| OD-RA05-003 | Comparison and present reuse after change | Accept Section 6: explicit evidence for correspondence and comparability; no automatic resolution or decision inheritance; retained history remains outside the new test basis unless deliberately supplied | ACCEPTED |
| OD-RA05-004 | Persistence guarantees and policy interfaces | Accept Section 7: coherent durable records, retry identity, explicit recovery, policy-governed retention, and exact export snapshots; defer physical mechanisms and periods to their allocated phases | ACCEPTED |

## 12. Author check, remaining allocations, and exit condition

### 12.1 Author check

[SR-RA05-001 v0.2][review05] records the completed static review and the Owner's endorsement on 2026-09-18. `SR-RA05-F-001` is closed: Section 5.1 and the Section 6 table distinguish first confirmation in an active run from changing an applied interpretation or configured behavior artifact. VAL-006/009 cover that distinction. The correction did not change the 22 requirement statements or four policy decisions.

The original trace check found 22/22 requirements with direct validation links, 16/16 obligations with valid targets and 56 direct links. The same assistant authored and reviewed the source; the Owner performed the walkthrough. This is historical document evidence, not independent expert assurance, product testing or model evaluation.

### 12.2 Allocations and carried observations

| Governing source or record | Responsibility or current disposition |
| --- | --- |
| [RA-06][ra06] | Four-technique applicability, coverage and evidence; no automatic requirement to apply every technique |
| [RA-07][ra07] | Permitted LLM roles, grounding, abstention, qualification and change impact; comparison assistance needs an authorized qualified role |
| [RA-08][ra08] | Classification, sealed identity/access, logs, retention, deletion, backup/restore, storage/export protection and security verification |
| [RA-09][ra09] | Input/export contracts, schemas, capture transformations and physical error/report formats |
| [RA-10][ra10] and test design | Challenging data, human oracle, thresholds, executable tests and empirical local-hardware feasibility |
| [Solution Design][design] | Storage, transactions, retries, physical data model, deployment and interface decisions |
| `SR-RA03-OBS-001` | The RA03-VAL-014 trace action was closed by the accepted RA-10 bridge; see [SR-RA10-001 v0.2][review10]. General trace obligations remain |
| `SR-RA03-OBS-002` / R-08 | Keep documentation proportional to the decisions and risks it resolves; empirical product validation remains necessary |

Read the related requirements with their accepted decisions, indexed in the [Requirements Analysis closure][phase]. These references replace the old pending-work descriptions; they do not establish that the product implements those contracts.

### 12.3 Version record

The Owner accepted v0.1 before its focused review. The later 2026-09-18 decision endorsed the verified v0.2 clarification, accepted the review, designated the baseline, closed RA-05 and granted GO to RA-06. [SR-RA05-001 v0.2][review05] retains that chronology and the original file identities. No approval is awaiting repetition.

This maintained text consolidates those decisions and references the current contracts. Historical GO to RA-06 does not override the development pause; [README.md](../../../README.md) carries current work status.

[charter]: ../../governance/test-design-gatekeeper-project-charter-v0.4.md
[ra01]: ../test-design-gatekeeper-ra-01-stakeholders-actors-authority-v0.3.md
[ra02]: ../test-design-gatekeeper-ra-02-system-context-workflows-use-cases-v0.3.md
[ra03]: ../ra-10/test-design-gatekeeper-ra-03-review-package-content-provenance-validation-v0.4.md
[ra04]: ../test-design-gatekeeper-ra-04-scope-qualification-classification-boundaries-v0.2.md
[review04]: ../../reviews/test-design-gatekeeper-ra-04-focused-static-review-v0.2.md
[review05]: test-design-gatekeeper-ra-05-focused-static-review-v0.2.md
[phase]: ../ra-10/test-design-gatekeeper-requirements-analysis-readiness-v0.2.md
[ra06]: ../ra-06/test-design-gatekeeper-ra-06-technique-applicability-design-coverage-v0.2.md
[ra07]: ../ra-07/test-design-gatekeeper-ra-07-llm-roles-qualification-v0.2.md
[ra08]: ../ra-08/test-design-gatekeeper-ra-08-confidentiality-security-privacy-v0.2.md
[ra09]: ../ra-09/test-design-gatekeeper-ra-09-data-representations-import-export-contracts-v0.2.md
[ra10]: ../ra-10/test-design-gatekeeper-ra-10-evaluation-acceptance-v0.2.md
[review10]: ../ra-10/test-design-gatekeeper-ra-10-focused-static-review-v0.2.md
[design]: ../../solution-design
[original]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/469d9a6c5119b1b6eed8f8bd97a0ef5e5f254d28/docs/requirements-analysis/ra-05/test-design-gatekeeper-ra-05-findings-dispositions-persistence-v0.2.md
