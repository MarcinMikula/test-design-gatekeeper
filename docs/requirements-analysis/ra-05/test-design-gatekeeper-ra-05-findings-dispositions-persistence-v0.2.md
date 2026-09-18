# Test Design Gatekeeper

## RA-05 — Findings, Dispositions, and Persistence

| Field | Value |
| --- | --- |
| Document version and date | 0.2 — 2026-09-17 |
| SDLC phase | Requirements Analysis |
| Status | CORRECTED CANDIDATE — LOCAL CLARIFICATION AWAITS OWNER ENDORSEMENT |
| Entry authorization | PG-RA04-001, consolidated in Section 7 of SR-RA04-001 v0.2 — GO to RA-05 |
| Effective baseline | Charter v0.4; RA-01 v0.3; RA-02 v0.3; RA-03 v0.3 with PG-RA03-001 v0.2; RA-04 v0.2 with SR-RA04-001 v0.2 |
| Decision authority | Project Owner |
| Requirement state | All 22 v0.1 requirements ACCEPTED by the Project Owner; all requirement statements and MUST priorities unchanged |
| Policy decisions | OD-RA05-001 through OD-RA05-004 ACCEPTED as recommended; 0 open policy decisions |
| Static review and acceptance record | SR-RA05-001 v0.1; one clarification prepared and verified, final endorsement pending |
| RA-06 gate | NOT GRANTED |
| Implementation and confidential-data use | Not authorized |

## 1. Purpose, sources, and boundaries

RA-05 defines what TDG retains after a review: the bounded assessment result, its findings or suggestions, the evidence behind them, human decisions, and subsequent history. It distinguishes completion of analysis from the availability of a supported result, acceptance of a finding, external repair of a TC, and formal approval of testware.

The governing sources are [Charter Sections 10 and 17][charter], [RA-01 authority rules][ra01], [RA-02 Sections 11–15][ra02], [RA-03 content and identity requirements][ra03], and [RA-04 qualification rules][ra04]. The effective acceptance records are [PG-RA03-001 v0.2][gate03] and [SR-RA04-001 v0.2, including PG-RA04-001][review04]. Repository links pin commit `7b5612b19525a97e7c43d2450b0e0e94dbbd7940`. Earlier candidate or pending notices in source documents are historical; the subsequent acceptance records govern.

This is a logical information and behavior model. It selects no database engine, physical schema, API, UI, cryptographic mechanism, retention duration, or export format. It introduces no overall score for test quality or ISTQB conformity. The status vocabulary is TDG project policy, not an ISTQB-prescribed workflow.

The Project Owner accepted RA-05 v0.1 in full, including all 22 MUST requirements and the four recommended decisions. **Shall** therefore expresses an accepted obligation for that reviewed wording. This v0.2 candidate preserves every requirement statement and records the acceptance; it also proposes a localized clarification in Sections 5.1 and 6 and corresponding refinements to VAL-006 and VAL-009. Those later edits are not retroactively covered by acceptance of v0.1. [SR-RA05-001 v0.1][review05] records the decision, the review, and the exact change boundary. Final endorsement of these edits and GO to RA-06 remain pending.

The following inherited rules are not reopened: every new finding starts `PENDING`; finding dispositions are `PENDING`, `ACCEPTED`, `REJECTED`, and `DEFERRED`; TDG does not edit source TC or formally approve testware; confidential or possibly protected material is prohibited in the laboratory profile.

## 2. Logical records and identities

An identity names a record; it does not prove that its contents are correct. Source identifiers, titles, repeated steps, and content hashes do not replace TDG's internal identities or establish equivalence across versions.

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

A subject can be a supplied source fragment, a TC, a justified within-TC view, or an explicitly bounded group of TC. A view retains its parent TC identity and original source locations; it is not a newly authored TC. Group findings name the affected members and scope instead of becoming an unsupported package-wide verdict.

Intake problems occurring before a trusted package version exists remain intake diagnostics. TDG must not fabricate a package or assessment run to attach them. Their safe recording follows the applicable profile and later RA-08 policy.

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

Operational diagnostics, intake checks, and scope classification are not counted as completed substantive review dimensions. A supported observation about a missing TC element can be an assessed quality dimension while a separate technique dimension is ungradable. Detailed technique applicability and coverage meanings remain allocated to RA-06.

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

Every reported finding or suggestion needs enough retained context for an authorized human to inspect the claim without guessing its subject or premises.

| Content | Required meaning |
| --- | --- |
| Identity and subject | Internal item ID, package-version ID, originating run ID, and affected TC/view/source or explicitly bounded group |
| Claim and dimension | The exact alleged gap, inconsistency, or improvement opportunity; distinguish a source-basis issue from a TC-design issue |
| Evidence | Identifiable supplied source locations, relevant observed content, and dependencies on any normalized rule or human decision |
| Derivation | `DETERMINISTIC` or `LLM_ASSISTED`, with the applicable behavior artifacts and versions |
| Interpretation boundary | Supplied facts, derived interpretation, assumptions, uncertainty, conflicts, and relevant exclusions distinguished |
| Review assistance | An actionable question or bounded recommendation; no invented business rule or replacement source TC |
| Human history | Initial `PENDING` and subsequent attributable disposition events, separately from the original claim |

A reported absence identifies the bounded material inspected and the missing element; it cannot assert absence from documentation that was not supplied. Unavailable evidence is recorded as unavailable, not reconstructed from a link. No mandatory severity score is introduced here; any later impact label must disclose its supporting context rather than manufacture business priority.

### 4.1 Derivation remains independent of disposition

| Item kind inherited from the Charter | Derivation and constraint |
| --- | --- |
| `DETERMINISTIC_FINDING` | `DETERMINISTIC`: a reproducible control over identified normalized input and confirmed structured premises; retain control, mapping, rule, and configuration versions |
| `REVIEW_SUGGESTION` | `LLM_ASSISTED`: a grounded, uncertain, rejectable interpretation; retain the relevant role, prompt, model, configuration, evidence, and qualification context |

Reproducibility does not establish source truth. A deterministic script over an unconfirmed LLM interpretation does not establish a deterministic business or coverage conclusion. It may establish a narrower observable structural fact if that claim does not depend on the unconfirmed interpretation.

LLM wording added to explain a deterministic finding is identified as a separate explanatory contribution and cannot change the original claim, evidence, or derivation. A new semantic claim needs its own supported suggestion. A high-confidence assertion without the required evidence is withheld as an unsupported conclusion; TDG records the limitation or clarification need instead. Human acceptance cannot convert missing support into evidence or change an item's derivation.

## 5. Human decisions and their history

Role identifiers retain their definitions in [RA-01 Sections 7–9][ra01]. ROLE-04 is the Test Basis Authority; ROLE-05 is the Finding Disposition Authority; ROLE-03 owns source-testware editing. Acting in one role does not confer the authority of another. Laboratory role attribution is not a claim of enforced sealed-profile RBAC.

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

Each authority-bearing event retains its own identity; target record and assessment version; actor identity or local actor identifier; acting role; action; previous and resulting state where applicable; rationale and evidence references; recorded time; and an authoritative order within the target history. Supplied-source timestamps remain distinguishable from TDG record times. Clock equality or clock changes cannot silently reorder decisions.

Self-review is recorded when the acting reviewer authored or owns the affected testware under the applicable RA-01 rule. Role combinations remain visible. Unknown independence is not presented as independent review, and later role changes do not relabel past actions.

Disposition requires an identifiable retained item and access to the evidence needed for that judgment. Missing required evidence or an explicitly unconfirmed dependency prevents accepting a dependent claim as established. This is not a guarantee that TDG can determine the truth of every human judgment. ROLE-05 can accept a grounded recommendation to clarify an ambiguity, or a supported suggestion retaining its uncertainty, without confirming the unknown business rule. Reopening a retained historical item can cite an evidence-unavailability or impact record without pretending that the missing source was inspected.

Two humans acting on the same prior decision must not silently overwrite each other. A stale action is exposed as a conflict requiring renewed human consideration; both the existing history and the attempted action's outcome remain attributable under policy.

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

Earlier pending or deferred findings do not prevent submission of a new package or a new authorized assessment. A new version does not establish repair, close an earlier finding, or erase its rationale.

### 6.1 Comparison observations

An explicit, authorized comparison names the selected runs, package versions, subjects, relevant assessment dimensions, and behavior contexts. It states the evidence for correspondence and any uncertainty. Similar titles, generic steps, identical preconditions, or matching source IDs alone cannot establish that two records concern the same issue.

| Observation | Required evidence and limit |
| --- | --- |
| `OBSERVED_AGAIN` | Supported correspondence to a separately recorded item in the later assessment; human disposition still belongs to each item |
| `NOT_REDETECTED_IN_COMPARABLE_REVIEW` | Supported corresponding subject and check, sufficient current evidence, compatible interpretation/behavior context, and a completed relevant assessment with no corresponding item; this is an observation, not verified repair |
| `COMPARISON_UNDETERMINED` | Correspondence or comparability is unsupported, the relevant dimension was not assessed, or evidence is unavailable; retain the specific reason |

No selected predecessor means no comparison, not a claim that an issue is new. Mere absence from a later item list cannot satisfy the second row. Failed or cancelled processing cannot support that row unless the relevant assessment entry independently completed, is safely retained, and meets every comparability condition. Overall run failure alone neither proves repair nor erases a supported repeated finding.

Comparison assistance remains derived and carries its evidence, behavior identity, and uncertainty. It cannot change human decisions. RA-07 will allocate any permitted LLM role; no automatic semantic matcher is selected here.

### 6.2 Current-use limitations and source boundaries

When TDG is given attributable evidence of a relevant change, it records an impact notice against the affected retained result. Examples include changed package context, withdrawn qualification of a used behavior version, a corrected premise, or loss of necessary evidence. The notice distinguishes the original historical result from its fitness for present reuse. Lack of impact evaluation means reuse applicability is undetermined, not automatically valid or invalid.

The notice does not rewrite the original finding, change its historical derivation, or automatically replace its human disposition. ROLE-04 owns basis interpretation, ROLE-08 owns behavior qualification, and ROLE-05 may reconsider or reopen the finding. TDG does not invent these authority decisions.

Authorized inspection and comparison of selected retained history do not add that history to a new package's test basis. TDG cannot search its database for unrelated documentation to fill gaps. If a human wants previous content to become supplied context for a new substantive review, it must enter through the controlled package boundary.

## 7. Local persistence, recovery, retention, and export

### 7.1 Retained logical content — accepted OD-RA05-004

The approved direction is local, organization-controlled persistence. The retained record set must make package versions, TC identities and supplied names, runs, ledger outcomes, findings, evidence references, interpretation decisions, disposition histories, impact/comparison records, and exports distinguishable and linked. Capture transformations are identified separately from assessment rules, mappings, controls, prompts, model versions, configuration, and applicable qualification/policy records. Unused behavior artifacts are not reported as having contributed to the result.

Evidence inspection needs resolvable retained references to the relevant authorized material or an explicit unavailability reason. It does not require copying whole source documents into every finding or exporting all source content. Minimize unnecessary content duplication and absolute workstation paths. Local storage alone does not demonstrate confidentiality, sealed-profile readiness, or recoverability.

### 7.2 Save, concurrency, and retries

TDG reports a save as successful only when the intended logical record and the references required for its integrity have been durably recorded together. It must not expose a saved disposition pointing to an item that never committed, a final result with missing required ledger entries, or an export claiming an uncommitted decision. An unsaved preview remains visibly unsaved and cannot be confused with retained history.

Historical claims and authority-bearing events are not edited in place. Corrections and state changes append attributable records; current-state views can be derived from retained history. This is a behavioral requirement, not a mandate for a particular database or event-sourcing architecture.

A retry of the **same identified operation with the same content** returns the existing committed outcome when it already succeeded. Reusing that operation identity for different content produces an explicit conflict. A **new deliberate assessment request** creates a new run even when its package and parameters equal an earlier request. Identical content must not collapse independent package or run identities.

### 7.3 Failure, cancellation, and recovery

On failure or cancellation, retain only safely committed records permitted by policy. Completed independent assessment entries remain distinguishable from interrupted, provisional, or never-started work. Result availability follows Section 3; diagnostics alone cannot establish a partial substantive review.

Recovery must not present an interrupted `RUNNING` record as completed without evidence. It records the interruption and reconciles it to an explicit terminal outcome, normally `FAILED` when no prior terminal decision was committed. A previously committed terminal decision remains authoritative. Any subsequent assessment uses a new run. No unattended recovery re-executes assessment or external data retrieval under an old identity.

Neither source bytes nor old decisions are silently overwritten to make recovery appear successful. Detailed backup media, restore procedures, durability mechanisms, and security verification belong to RA-08 and Solution Design.

### 7.4 Retention and authorized deletion

Immutability applies while records are retained; it is not a rule of indefinite retention. ROLE-09 approves the applicable retention, deletion, logging, backup, and export policy; ROLE-07 executes approved operations. Where required policy or authority is absent, TDG cannot invent a retention or deletion decision.

Authorized deletion must account for dependencies and prevent surviving records from appearing fully evidenced when their supporting content is gone. Retain a minimal attributable deletion or evidence-unavailability record only to the extent the governing policy permits. If policy requires its removal too, it must not be retained merely to preserve history.

Do not restore deleted evidence by following external references or searching unsubmitted material. Deletion does not resolve a finding. A claim about erasure from backups or prior exports requires the scope and verification demanded by the applicable policy; deleting one active copy is insufficient evidence. Exact periods and mechanisms remain open work for RA-08.

### 7.5 Controlled export

A deliberate authorized local export identifies its export instance, package version, run, selected content, applicable policy, and the exact disposition/history boundary used. It preserves run state, availability, scope, omissions, derivation, uncertainty, human decisions, and non-approval meaning. Later human decisions do not alter an earlier export's recorded contents; a new export has a new attributable instance.

Export is separate from successful persistence and from the ability to view a record. A denied or failed export does not corrupt the canonical record. Export does not edit TC or publish directly to Jira, Xray, or Zephyr. RA-09 will define physical formats; RA-08 will define policy enforcement and protection requirements.

## 8. Synthetic boundary examples

These fragments illustrate the proposed record behavior. They are not complete Review Packages, executed tests, evidence of model capability, or a finished benchmark. Assume lawful synthetic input and the stated prerequisite evidence; otherwise the relevant inherited gate applies.

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

All 22 requirement statements below are unchanged from v0.1 and are MUST / ACCEPTED under the recorded Project Owner decision. Source traces are unchanged. Acceptance of those statements does not imply endorsement of the subsequent supporting-text clarification identified in Section 1.

| ID | Proposed requirement | Priority | Status | Primary upstream trace |
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

These are obligations for later static review and test design, not executed TC or passing software tests. Every requirement has a direct VAL link, and every VAL names existing RA05 requirements. The mapping is many-to-many; a link alone does not prove that its future tests will be adequate.

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

All four recommendations below were accepted by the Project Owner with v0.1. Their acceptance does not reopen upstream policies or select an implementation technology. The localized v0.2 clarification is tracked separately and awaits endorsement; it does not create a fifth open policy decision.

| ID | Decision | Accepted recommendation | Status |
| --- | --- | --- | --- |
| OD-RA05-001 | Operational states, ledger outcomes, availability, and counting | Accept Section 3: separate axes, explicit non-success reasons, normal completion compatible with limited or absent substantive review, and no quality implication | ACCEPTED |
| OD-RA05-002 | Human disposition transitions and evidence history | Accept Section 5: retain the four inherited dispositions; require attributable rationale and ROLE-05 reopening; separate ROLE-04 interpretation decisions and preserve self-review | ACCEPTED |
| OD-RA05-003 | Comparison and present reuse after change | Accept Section 6: explicit evidence for correspondence and comparability; no automatic resolution or decision inheritance; retained history remains outside the new test basis unless deliberately supplied | ACCEPTED |
| OD-RA05-004 | Persistence guarantees and policy interfaces | Accept Section 7: coherent durable records, retry identity, explicit recovery, policy-governed retention, and exact export snapshots; defer physical mechanisms and periods to their allocated phases | ACCEPTED |

## 12. Author check, remaining allocations, and exit condition

### 12.1 Author check

The checks below concern this candidate and its trace structure. The focused review and correction verification are recorded in SR-RA05-001 v0.1. They are not an independent expert review, a software test report, or evidence that a local model can satisfy the requirements.

| Check | Result and limit |
| --- | --- |
| Entry and effective baseline | PASS — RA-05 entry is granted by PG-RA04-001 in SR-RA04-001 v0.2; prior source-status notices are treated historically |
| Requirement identity and status | PASS — 22 unique statements unchanged from v0.1; MUST / ACCEPTED through an explicit Owner decision |
| Forward trace, REQ to VAL | PASS — 22/22 requirements directly referenced by at least one validation obligation |
| Reverse trace, VAL to REQ | PASS — 16/16 validation obligations reference existing RA05 requirements; no orphan or nonexistent RA05 target |
| Role and disposition continuity | PASS — four inherited dispositions retained; ROLE-04, ROLE-05, ROLE-07, ROLE-08, and ROLE-09 responsibilities remain separate |
| Identity and supplied-data boundaries | PASS — source versions, runs, human events, and comparisons have separate consequences; retained history does not silently enrich a package |
| Status-table consistency | PASS — proposed terminal-state and availability cases have explicit outcomes; no supported substantive entry means NONE even if diagnostics exist |
| Scope of verification | NOT EXECUTED — no implementation, model evaluation, recovery test, security test, or executable TC has been produced by this slice |
| Focused review and final endorsement | SR-RA05-001 v0.1 records one Medium clarification and its verified correction; acceptance of v0.1 is recorded, while endorsement of the correction and RA-06 gate remain pending |

### 12.2 Allocations and carried observations

| Destination or record | Remaining responsibility |
| --- | --- |
| RA-06 | EP, BVA, decision-table, and state-transition applicability and coverage; technique-specific finding evidence; no automatic requirement to apply every technique |
| RA-07 | Permitted LLM roles, grounding, abstention, qualification/requalification, and behavior-change impact; any semantic comparison assistance must fit an authorized qualified role |
| RA-08 | Data classification, sealed identity and authorization, logging, retention periods, deletion, backup/restore, storage and export protections, and concrete security validation |
| RA-09 | Canonical input/export representations, schemas, capture/import transformations, and physical error/report formats |
| RA-10 and subsequent test design | Challenging datasets, human oracle, thresholds, full TC derived from these obligations, and empirical feasibility on the intended local hardware |
| Solution Design | Storage technology, transaction and retry mechanisms, physical data model, deployment, and interface choices |
| SR-RA03-OBS-001 | Earlier indirect RA03-VAL-014 trace through IS-01–IS-11 still needs a verifiable chain to accepted requirements before executable test design; this document's direct trace does not close that observation |
| SR-RA03-OBS-002 / R-08 | Retain the analysis-growth risk for the next Charter risk review; use this focused requirements document and a consolidated review/acceptance record, referencing earlier baselines; feasibility remains unproven |

The Project Owner accepted v0.1 before the focused review record was issued; that actual sequence is preserved rather than backdated. The remaining decision is endorsement of the localized correction and its verification, closure of SR-RA05-001, and designation of the final RA-05 baseline with explicit GO to RA-06. This candidate records none of those remaining approvals.

### 12.3 Version record

| Version | Meaning |
| --- | --- |
| 0.1 | Original reviewed wording, accepted in full by the Project Owner; retained unchanged as the review input |
| 0.2 | Acceptance/status update plus the SR-RA05-F-001 clarification in Sections 5.1 and 6 and VAL-006/009; all 22 requirement statements, priorities, identifiers, and 56 REQ–VAL links unchanged; final endorsement pending |

[charter]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/7b5612b19525a97e7c43d2450b0e0e94dbbd7940/docs/governance/test-design-gatekeeper-project-charter-v0.4.md
[ra01]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/7b5612b19525a97e7c43d2450b0e0e94dbbd7940/docs/requirements-analysis/test-design-gatekeeper-ra-01-stakeholders-actors-authority-v0.3.md
[ra02]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/7b5612b19525a97e7c43d2450b0e0e94dbbd7940/docs/requirements-analysis/test-design-gatekeeper-ra-02-system-context-workflows-use-cases-v0.3.md
[ra03]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/7b5612b19525a97e7c43d2450b0e0e94dbbd7940/docs/requirements-analysis/test-design-gatekeeper-ra-03-review-package-content-provenance-validation-v0.3.md
[gate03]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/7b5612b19525a97e7c43d2450b0e0e94dbbd7940/docs/reviews/test-design-gatekeeper-ra-03-gate-record-v0.2.md
[ra04]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/7b5612b19525a97e7c43d2450b0e0e94dbbd7940/docs/requirements-analysis/test-design-gatekeeper-ra-04-scope-qualification-classification-boundaries-v0.2.md
[review04]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/7b5612b19525a97e7c43d2450b0e0e94dbbd7940/docs/reviews/test-design-gatekeeper-ra-04-focused-static-review-v0.2.md

[review05]: test-design-gatekeeper-ra-05-focused-static-review-v0.1.md
