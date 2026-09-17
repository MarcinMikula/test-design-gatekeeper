# Test Design Gatekeeper

## RA-04 — Scope Qualification and Classification Boundaries

| Field | Value |
| --- | --- |
| Document version and date | 0.2 — 2026-09-16 |
| SDLC phase | Requirements Analysis |
| Status | CORRECTED CANDIDATE — FINAL OWNER ENDORSEMENT PENDING |
| Entry authorization | PG-RA03-001 v0.2 — GO to RA-04, 2026-09-15 |
| Effective baseline | Charter v0.4; RA-01 v0.3; RA-02 v0.3; RA-03 v0.3 with the acceptance register in PG-RA03-001 v0.2 |
| Decision authority | Project Owner |
| Requirement state | All 15 v0.1 requirements accepted by the Project Owner; 14 wordings unchanged; REQ-004 editorial clarification awaits endorsement |
| Policy decisions | OD-RA04-001 through OD-RA04-003 ACCEPTED; 0 open policy decisions |
| Review and correction record | SR-RA04-001 v0.1; original v0.1 retained as the reviewed predecessor |
| RA-05 gate | NOT GRANTED |
| Implementation and confidential-data use | Not authorized |

## 1. Purpose, sources, and boundaries

RA-04 defines the evidence and consequences for deciding which supplied test cases or assessment dimensions fit the MVP. It preserves the distinction between an established exclusion and an inability to decide.

The governing sources are [Charter Sections 6, 8 and 9][charter], [RA-01 authority rules][ra01], [RA-02 qualification workflow and accepted requirements][ra02], and [RA-03 input and identity requirements][ra03]. Their effective acceptance and baseline are recorded in [PG-RA03-001 v0.2][gate]. All repository references identify the published baseline commit `c428df6e80211c8415d4cd96a4f3707df8e080e3`; earlier status notices in the source files are historical.

Terminology was checked against [ISTQB CTFL Syllabus v4.0.1, Sections 2.2 and 4.1][ctfl], accessed 2026-09-16. CTFL distinguishes test levels using context such as the test object and objectives. It discusses functional, non-functional, black-box and white-box testing as test types, and distinguishes black-box, white-box and experience-based technique families. TDG separates these considerations into operational dimensions to avoid treating them as mutually exclusive labels. Its admission rules and evidence thresholds below are TDG project policy, not ISTQB certification criteria. Credit for the referenced syllabus belongs to ISTQB and its authors; no syllabus text is reproduced.

RA-04 adds qualification policy to the accepted model. Final result enums and persistence belong to RA-05; technique applicability and coverage to RA-06; LLM roles and qualification to RA-07; security controls to RA-08; supported import representations to RA-09; evaluation datasets and thresholds to RA-10. The examples below are synthetic classification fragments, not implemented checks, complete Review Packages, or a finalized benchmark.

## 2. Separate the decisions

Qualification is recorded per identifiable TC and, where defensible, per assessment dimension. A package is an inventory of these outcomes, not evidence that every contained TC is eligible.

| Decision | Question | Consequence |
| --- | --- | --- |
| Intake and policy | Is processing permitted, and does the package meet RA-03 minimums? | A failed package minimum or policy gate follows RA-03; no supported substantive review |
| Item eligibility | Is this a recognizable TC with applicable accountable human control? | A positive case elsewhere in the package does not confer eligibility on this item |
| Domain qualification | Does the described test satisfy the MVP criteria in Section 3? | Supported in scope, established outside scope, or undetermined, with reasons |
| Capability availability | Can the authorized capability inspect the needed representation and perform this assessment? | Missing capability is reported separately from domain exclusion |
| Assessment sufficiency | Is the evidence sufficient for the particular claim? | Limit that claim while retaining independent supported work |

For example, an in-scope functional TC may lack data needed for BVA analysis. Qualification can be supported while BVA assessability remains unresolved. Missing expected results remain a quality gap under RA03-REQ-022, not an automatic change of test level or design basis.

The descriptions in this document specify meanings, not final RA-05 status names or a software execution pipeline. Inspection needed to qualify material does not imply that substantive review has already been authorized or completed.

## 3. Independent dimensions and the MVP boundary

| Dimension | Evidence to inspect | Boundary or caution |
| --- | --- | --- |
| Declared feature or process | Supplied scope and the behavior actually described | Membership in the package alone does not establish a match |
| Test level | Identified test object, its boundary, objective, and relevant supplied context | The MVP supports system-level review; names of tools, endpoints or environments are insufficient shortcuts |
| Functional objective | The behavior or business rule being checked | Non-functional objectives are outside the supported assessment; mixed objectives need separation |
| Design basis | What determines test conditions, chosen data and required observations | External behavior can support the MVP route; dependence on implementation structure must be exposed |
| Technique evidence | Supplied rationale and demonstrable technique-related material | Naming EP, BVA, decision tables or state transitions is neither required nor sufficient; detailed assessment is RA-06 |
| Execution and context | Manual/automated mode, representation, role and environment where relevant | Preserve independently; absence matters only where it prevents a particular decision |

For a proposed qualification subject, all five conditions below need support for a positive domain conclusion. A subject is normally the whole TC; Section 5 governs narrower views.

| Criterion | Required support for the MVP route |
| --- | --- |
| RA04-C-01 | The described behavior belongs to the explicitly authorized feature or small process |
| RA04-C-02 | The identified object and objective support system-level testing of that product, rather than an isolated component, integration-specific objective, or acceptance-readiness objective |
| RA04-C-03 | The reviewed objective concerns functional behavior |
| RA04-C-04 | The proposed assessment has an external-behavior basis and does not depend on evaluating implementation-structure coverage |
| RA04-C-05 | The assessed subject is ordinary business-system behavior, not evaluation of AI/LLM behavior as the parked target domain |

The system boundary may include multiple deployable components. UI/API access, mocks, stubs, a database connection, or an E2E label do not establish a test level. Actual integration and acceptance objectives remain outside this MVP even when their tests are functional and specification-based. A deployment named UAT does not by itself establish an acceptance objective.

An attributable experience-based rationale may support general functional review within the existing Charter allowance. Preserve that rationale and technique family; do not relabel error guessing as a specification-based technique or add it to the four assessed techniques. Likewise, the presence of AI somewhere in a business application does not alone prove that a TC evaluates AI behavior; the supplied objective and relevant dependencies decide the boundary.

## 4. Evidence and qualification consequences

### 4.1 Evidence contract — accepted OD-RA04-001

Use substantive TC content and attributable supplied context identifying the object, objective and basis relevant to the decision. Shared package context is usable when its application to the item is unambiguous. This adds no mandatory physical fields or one-TC-to-one-requirement link.

An operator's label, a title, a framework name or an LLM confidence score is insufficient alone. Absence of code in a submission is not proof of black-box design. Missing execution-mode metadata need not prevent qualification when it is irrelevant to the criteria.

Preserve the declared labels separately from the evidence-supported interpretation. An isolated label discrepancy may be reported without defeating otherwise sufficient context. Contradictory substantive accounts of the object, purpose or basis remain unresolved until an attributable clarification or source-precedence decision exists. No rule silently makes the newest, longest or most formal-looking source authoritative.

Qualified, authorized capabilities may assist interpretation under RA-07. Their output remains visibly derived, with evidence and uncertainty. If a decisive inference lacks sufficient support, retain an undetermined result and request the missing context. A model's confidence cannot upgrade missing evidence or record human confirmation. This document chooses no numerical threshold, classifier, prompt or implementation mechanism.

### 4.2 Consequence table

Apply the first applicable row to the qualification subject after accounting for prerequisites and any permitted separation. Preserve additional known reasons and unresolved dimensions.

| Rule | Condition | Required meaning and action |
| --- | --- | --- |
| RA04-Q-01 | Package policy, trusted capture or a core minimum prevents the operation | Report the RA-03 prerequisite failure; do not manufacture a domain verdict or review result |
| RA04-Q-02 | Prerequisites permit inspection and reliable supplied evidence establishes failure of any criterion C-01 to C-05 | Established outside the requested MVP boundary, with the criterion and evidence; other axes may remain unknown |
| RA04-Q-03 | No established exclusion, but at least one decisive criterion lacks support or has an unresolved substantive conflict | Undetermined; identify the missing fact or conflict and the affected review limitation |
| RA04-Q-04 | All five criteria are supported for the identified subject | Supported in scope; substantive review still depends on item eligibility, capability and assessment-specific evidence |

A capability failure supplies no evidence of being outside scope. Retain any independent supported qualification evidence; otherwise qualification remains undetermined with the capability limitation visible. An excluded item may still receive attributable intake and scope diagnostics; it does not receive unsupported technique or coverage review.

## 5. Technical detail, mixed cases, and human control

### 5.1 Technical detail is assessed by its role

Distinguish setup, observation and the basis used to derive the test. SQL used to prepare a known starting condition can coexist with a functional system scenario. An internal observation needs enough supplied meaning to determine whether it merely observes a business outcome or makes the test dependent on implementation structure. A private branch flag or code-coverage target provides different evidence from an API response or a documented business state. Unexplained database fields or logs call for clarification; they do not justify guessing either black-box or white-box.

The label "gray-box" may be retained as supplied text. The conclusion describes the actual external, internal, mixed or unknown dependencies and their consequences, rather than issuing a definitive gray-box verdict.

### 5.2 Separability — accepted OD-RA04-002

The accepted ability to review supported subsets is retained. A narrower view inside one TC is defensible only when all of the following hold:

1. The relevant behavior and source locations are identifiable without inventing or rewriting steps.
2. Required setup, data, preceding actions and shared context remain attached to the view.
3. The supported claim does not depend on an excluded internal/non-functional assertion or an unresolved assumption; any required observation for that claim is identifiable.
4. The view remains within the existing human-authorized boundary and reports every excluded part and limitation.

This is an assessment view, not a new authored TC. If these conditions cannot be established, do not claim a supported slice; record the known exclusion or unresolved basis according to Section 4. Preserving a visible subset inside the unchanged boundary does not require redundant scope confirmation. A deliberate change of that boundary requires ROLE-02 and a new package version. An oversized declared multi-process scope still requires human narrowing under RA02-REQ-035; partial review cannot bypass that requirement.

### 5.3 Package reporting — accepted OD-RA04-003

List each original TC once by its unambiguous RA-03 package-local identity, with its domain conclusion or mixed/partial explanation, item-eligibility and capability restrictions, and separately attributable dimensions where used. Duplicate external IDs and repeated text do not merge those identities. A partially reviewed TC must not be counted as a fully reviewed TC or as several new TCs. Show included and excluded identities and reasons; do not turn qualification counts into coverage percentages or a package-wide quality verdict. An empty supported subset means no substantive supported review is available.

ROLE-02 owns scope decisions, ROLE-04 owns disputed test-basis interpretations and source precedence, and ROLE-03 owns source TC correction. New findings or suggestions retain the RA-02 human-disposition boundary. A human can clarify evidence but cannot make unsupported evidence true or expand the product MVP without Project Owner change control. Changes to supplied content create a new package version; reinterpretation or reassessment of unchanged content creates a new run, preserving both outcomes.

## 6. Requirements and acceptance state

`Shall` expresses mandatory behavior within an effective baseline. The Project Owner accepted all fifteen v0.1 requirements during the walkthrough. This candidate retains fourteen requirement wordings unchanged and clarifies the positive direction of REQ-004 under SR-RA04-F-001. The revised REQ-004 wording and designation of this candidate baseline await final endorsement; the earlier acceptance of its policy is retained. Binding baseline effect requires completion of the applicable review and baseline controls. `MUST` expresses priority, not an implementation choice.

| ID | Requirement | Priority | Status | Upstream trace |
| --- | --- | --- | --- | --- |
| RA04-REQ-001 | TDG shall distinguish package prerequisites, item eligibility, domain qualification, capability availability and assessment-specific sufficiency before relying on an affected substantive result. | MUST | ACCEPTED | RA02-REQ-007; RA03-REQ-031; RA03-REQ-032 |
| RA04-REQ-002 | TDG shall retain test level, functional objective, design basis, technique evidence, execution mode and relevant context as separate dimensions without deriving one solely from another. | MUST | ACCEPTED | RA02-REQ-011; RA03-REQ-023 |
| RA04-REQ-003 | TDG shall ground qualification in addressable supplied content and applicable context; labels, titles, tool names, confidence scores and absence of implementation details shall not independently establish eligibility or exclusion. | MUST | ACCEPTED | RA02-REQ-012; RA03-REQ-020; RA03-REQ-039 |
| RA04-REQ-004 | A positive in-scope domain conclusion shall satisfy RA04-C-01 through RA04-C-05 for the identified subject; integration, acceptance, structural-coverage and AI/LLM-evaluation objectives shall not be admitted through relabeling. | MUST | ACCEPTED POLICY / WORDING ENDORSEMENT PENDING | Charter Sections 8–9; RA02-REQ-015; RA02-REQ-035; RA02-REQ-036 |
| RA04-REQ-005 | TDG shall apply RA04-Q-01 through RA04-Q-04, distinguishing evidence-supported exclusion from undetermined qualification and preserving additional established reasons and unresolved dimensions. | MUST | ACCEPTED | RA02-REQ-013; RA03-REQ-035; RA03-REQ-040 |
| RA04-REQ-006 | TDG shall assess the role of technical setup, observations and implementation dependencies before classifying the design basis, preserving a supplied gray-box label without using it as a definitive verdict. | MUST | ACCEPTED | Charter Section 9; RA02-REQ-012; RA02-REQ-013 |
| RA04-REQ-007 | An assessment view within a mixed TC shall meet all four separability conditions in Section 5.2, retain source references and necessary dependencies, and shall not rewrite the TC or imply whole-case qualification. | MUST | ACCEPTED | RA02-REQ-014; RA03-REQ-006; RA03-REQ-041 |
| RA04-REQ-008 | TDG shall expose the supported subset and all exclusions or unresolved items without double-counting original TCs, hiding partial dimensions, or treating qualification counts as coverage or completeness. | MUST | ACCEPTED | RA02-REQ-014; RA02-REQ-022; RA03-REQ-041 |
| RA04-REQ-009 | Substantive review of a TC shall require its applicable recognizable-content and accountable-origin conditions; another eligible TC in the package shall not satisfy those conditions on its behalf. | MUST | ACCEPTED | Charter Section 8.1; RA03-REQ-011; RA03-REQ-021 |
| RA04-REQ-010 | TDG shall preserve supplied declarations, derived qualification, uncertainty and human decisions separately; unsupported decisive inference shall yield undetermined qualification, and probabilistic output shall not become a deterministic fact or human confirmation. | MUST | ACCEPTED | RA02-REQ-020; RA02-REQ-023; RA03-REQ-027; RA03-REQ-039 |
| RA04-REQ-011 | TDG shall keep domain qualification separate from quality gaps, technique labels and technique-specific evidence; attributable experience-based cases may receive the accepted general review without forced reclassification or expansion of the four assessed techniques. | MUST | ACCEPTED | Charter Section 8; RA03-REQ-016; RA03-REQ-022; RA03-REQ-024; RA03-REQ-034 |
| RA04-REQ-012 | Scope changes, source-precedence decisions and source correction shall retain their assigned human authority; clarification, changed supplied content and reassessment shall preserve the accepted package-versus-run version consequences. | MUST | ACCEPTED | RA01-REQ-004; RA01-REQ-005; RA01-REQ-006; RA03-REQ-035; RA03-REQ-044; RA03-REQ-046 |
| RA04-REQ-013 | Each qualification result shall identify its package version, run, original item and any assessed view, criteria, supporting and conflicting source locations, derivation, behavior versions, limitations and actionable clarification need where applicable. | MUST | ACCEPTED | RA02-REQ-018; RA02-REQ-022; RA03-REQ-038 |
| RA04-REQ-014 | Execution mode and supported representation shall be handled independently from domain eligibility; unavailable parsing or interpretation shall remain a capability limitation, without executing submitted testware or selecting an unauthorized fallback. | MUST | ACCEPTED | RA02-REQ-021; RA03-REQ-012; RA03-REQ-019; RA03-REQ-025 |
| RA04-REQ-015 | Qualification shall express the scope and limits of TDG's review, without declaring an excluded TC defective merely because of exclusion or claiming testware approval, completeness, product quality or official ISTQB conformity. | MUST | ACCEPTED | RA01-REQ-014; RA02-REQ-024; RA03-REQ-050 |

## 7. Synthetic boundary examples

Unless changed in a row, assume a permitted synthetic package, accountable recognizable TCs, readable content, and a ROLE-02-authorized customer-creation feature of a fictional CRM product. Supplied context identifies system-level verification, an external business-rule basis and an ordinary business-system target. These shared assumptions supply the context omitted from short fragments; titles alone never produce the expected conclusion.

| ID | Fragment or controlled variation | Expected qualification consequence |
| --- | --- | --- |
| RA04-EX-01 | Create a customer through the deployed CRM and verify its identifier through the specified external interface. | Supported domain; subsequent assessment still needs its own evidence |
| RA04-EX-02 | Same object, objective, basis and behavior as EX-01, executed by Playwright or through the public API instead of manual UI actions. | Same domain qualification; no promise to import every code representation |
| RA04-EX-03 | A retained item is only an opaque executable; its behavior cannot be inspected with the permitted capability. Other valid TCs preserve the package minimum. | Capability limitation; no invented domain conclusion and no execution to discover behavior |
| RA04-EX-04 | Invoke one validation function in isolation using documented input/output rules. | Outside system-level scope; specification-based design does not turn it into a system test or a white-box test |
| RA04-EX-05 | Test a service–repository interaction against its supplied interface contract, with an explicit component-integration objective. | Outside supported level; retain its independently supported basis |
| RA04-EX-06 | Verify the CRM–billing interface contract with an explicit system-integration objective. | Outside supported level; a business-facing outcome alone does not change the objective |
| RA04-EX-07 | EX-01 has a UAT label, but substantive supplied context consistently identifies system verification; only the tag differs. | Preserve the label discrepancy; qualify described behavior without silently repairing the tag |
| RA04-EX-08 | Supplied purpose and responsibilities explicitly establish business acceptance and deployment readiness. | Outside supported level; not a defect in that acceptance test |
| RA04-EX-09 | Measure only response-time compliance under specified load. | Outside the functional assessment objective |
| RA04-EX-10 | One TC independently asserts customer creation and a latency threshold; setup and observations are explicit and separable. | Supported functional view, excluded performance dimension; original TC remains partially assessed |
| RA04-EX-11 | Choose inputs to traverse specified code branches and assert branch coverage. | Outside MVP scope because the objective is structural coverage, even if labeled system-functional |
| RA04-EX-12 | SQL prepares a supplied initial state; the test checks external customer-creation behavior independently of storage structure. | Technical setup alone does not exclude the functional view |
| RA04-EX-13 | Success is asserted only through an unexplained internal database flag, with no supplied mapping to a business outcome. | Undetermined basis for the claim; request the missing meaning |
| RA04-EX-14 | A mixed TC makes success depend inseparably on a private implementation path as well as a business result. | No supported separable view; established implementation dependency excludes the requested whole-case assessment |
| RA04-EX-15 | Actions are recognizable, but no supplied context establishes whether the object is a function or the deployed product. | Undetermined level; do not assume either system or component testing |
| RA04-EX-16 | Substantive sources disagree about the object and purpose, and no precedence decision exists. | Undetermined affected qualification; preserve both sources |
| RA04-EX-17 | The package boundary is customer creation; the supplied TC clearly tests an unrelated refund flow. | Scope mismatch; do not count it as customer-creation coverage |
| RA04-EX-18 | A tester supplies a past-defect rationale for a functional duplicate-customer scenario and its current external business rule. | General review may proceed; preserve experience-based rationale and the four-technique limit |
| RA04-EX-19 | The system-functional objective and external basis are clear, but the TC omits its expected result. | Domain may be supported; expose the material gap and restrict dependent assessments |
| RA04-EX-20 | The actual objective is judging hallucinations in generated LLM answers. | Outside MVP scope; AI/LLM-behavior review remains a parked target domain |
| RA04-EX-21 | A domain-compatible TC was generated elsewhere and has no accountable human adoption; another TC meets the package minimum. | Do not borrow eligibility; block its substantive review on the item condition, not on a fabricated design-basis verdict |
| RA04-EX-22 | Two TCs share generic steps and similar titles; their supplied objects and purposes are respectively an isolated function and system verification. | Keep distinct identities and qualify from the different contexts; shared text is not interchangeability evidence |

## 8. Downstream validation obligations

These are future validation conditions, not executed tests or implemented acceptance checks. Every obligation directly references RA-04 requirements; every requirement has at least one obligation.

| ID | Validation obligation | Primary trace |
| --- | --- | --- |
| RA04-VAL-001 | Exercise prerequisite failure, an oversized declared scope and every Q-table row; verify that successful import or partial-view extraction never bypasses the applicable prerequisite. | RA04-REQ-001; RA04-REQ-004; RA04-REQ-005 |
| RA04-VAL-002 | Cross level, objective, basis and execution dimensions; hold substantive context fixed while changing only misleading labels. Include EX-02 and EX-04 through EX-08. | RA04-REQ-002; RA04-REQ-003; RA04-REQ-004 |
| RA04-VAL-003 | Supply each established criterion failure, each missing decisive fact and substantive contradictions; verify specific exclusion reasons versus undetermined outcomes. | RA04-REQ-003; RA04-REQ-004; RA04-REQ-005 |
| RA04-VAL-004 | Contrast technical setup, explained business observation, unexplained internal flags and structural-coverage objectives; retain gray-box wording without a forced gray-box verdict. | RA04-REQ-006 |
| RA04-VAL-005 | Start with a separable mixed case, then invalidate each separability condition individually; verify retained context, no invented steps and no whole-case eligibility from a slice. | RA04-REQ-007 |
| RA04-VAL-006 | Mix supported, excluded, partial and undetermined cases, including duplicate external IDs handled under RA-03; verify visible inventories, original-item counts and an empty supported subset. | RA04-REQ-008; RA04-REQ-013 |
| RA04-VAL-007 | Vary recognizable content, origin and accountability independently across cases; confirm that one positive case does not admit unrelated ineligible cases. | RA04-REQ-009 |
| RA04-VAL-008 | Present weak or contradictory evidence alongside high model confidence; verify uncertainty, no self-confirmation, pending human disposition for suggestions and no unsupported admission. | RA04-REQ-003; RA04-REQ-010 |
| RA04-VAL-009 | Remove technique labels, direct requirement links or expected results from otherwise supported contexts; retain experience-based rationale without forced technique naming or concealed gaps. | RA04-REQ-011 |
| RA04-VAL-010 | Exercise scope-owner and basis-authority clarifications, source edits and unchanged-content reruns; verify correct authority, package/run identity and preserved prior outcomes. | RA04-REQ-012; RA04-REQ-013 |
| RA04-VAL-011 | Inspect every qualification consequence for evidence locators, the criterion, original item/view, derivation, relevant versions and actionable limits. | RA04-REQ-013 |
| RA04-VAL-012 | Compare equivalent supported representations and execution modes; introduce an opaque representation or unavailable semantic role without treating the capability gap as domain exclusion or executing the artifact. | RA04-REQ-014 |
| RA04-VAL-013 | Reuse generic steps across substantively different test objects and objectives; verify distinct identities and different justified outcomes where appropriate. | RA04-REQ-002; RA04-REQ-003; RA04-REQ-008 |
| RA04-VAL-014 | Contrast ordinary functional behavior in a product that contains AI with an objective that evaluates model behavior; omit decisive context and require abstention rather than assumption. | RA04-REQ-004; RA04-REQ-005 |
| RA04-VAL-015 | Check positive, excluded and empty-result reports for false defect, approval, completeness, product-quality or ISTQB-conformity implications. | RA04-REQ-008; RA04-REQ-015 |

RA03-VAL-014 retains its separate carried trace action from SR-RA03-OBS-001. This direct RA-04 matrix does not close or replace that earlier action. Actual evaluation data must later contain independently adjudicated good, bad and borderline cases; the examples above alone do not demonstrate classifier effectiveness or provide a held-out acceptance set.

## 9. Policy decision disposition

Inherited scope, roles, partial-review permission and version semantics are already accepted. The Project Owner accepted the three RA-04 recommendations below during the walkthrough, including an explicit acceptance of Section 9. No accepted upstream decision is reopened.

| Decision | Recommendation | Impact if revised | Status |
| --- | --- | --- | --- |
| OD-RA04-001 | Accept the evidence contract in Section 4.1: substantive object/objective/basis context, shared where unambiguous; labels and confidence alone are insufficient; no mandatory new field template. | Changes the boundary between supported and undetermined qualification; affects REQ-003/005/010 | ACCEPTED |
| OD-RA04-002 | Accept all four Section 5.2 conditions for a review view inside a TC; otherwise retain the limitation and request human clarification or source revision. | Changes safe partial-review eligibility and reporting; affects REQ-007/012 | ACCEPTED |
| OD-RA04-003 | Accept item inventory plus separately marked partial dimensions, with no qualification-to-coverage percentage or whole-package quality score. | Changes aggregation and the RA-05 handoff; affects REQ-008/013/015 | ACCEPTED |

## 10. Author check, handoff, and exit

The following table distinguishes original author checks from subsequent verification recorded in SR-RA04-001. The Project Owner completed the walkthrough of Sections 1–10. The same assistant authored and checked the source and corrections; this is not independent assurance.

| Check | State |
| --- | --- |
| Source identity and entry authority | Verified against the five published baseline/gate file identities |
| Upstream scope and role boundaries | Checked against Charter Sections 8–9, RA-01 authority and RA-02 partial-review/qualification rules |
| Normative status | 15 MUST; all v0.1 requirements owner-accepted; REQ-004 wording clarification awaits endorsement |
| Bidirectional REQ/VAL references | PASS — 15/15 REQ covered; 15/15 VAL directly reference existing REQ; no dangling upstream requirement references |
| Boundary distinctions | Intake/domain/capability/sufficiency, outside/undetermined, declaration/inference, and whole-TC/view remain separate |
| Focused static review and correction verification | COMPLETE — correction verification PASS; new finding disposition and candidate baseline endorsement PENDING |
| RA-05 gate | NOT GRANTED |

RA-05 receives outcome meanings and reporting obligations; RA-06 receives only supported subjects with their evidence limits; RA-07 receives the qualification-role evidence and abstention contract; RA-08/09 receive existing policy/capability boundaries; RA-10 receives the validation obligations and difficult example families. Detailed algorithms and numeric confidence or quality thresholds remain with those later workstreams.

RA-04 closes after disposition of the three recommendations and fifteen requirements, a focused static review, correction verification where needed, a verified baseline record, and an explicit Project Owner decision for RA-05. The human walkthrough is complete. The remaining owner decision concerns SR-RA04-F-001's three verified wording corrections, the review record, this candidate baseline and the RA-05 gate. It does not repeat acceptance of unchanged requirements or policy decisions. R-08 remains active: future additions need a distinct decision, risk or validation purpose.

[charter]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/c428df6e80211c8415d4cd96a4f3707df8e080e3/docs/governance/test-design-gatekeeper-project-charter-v0.4.md
[ra01]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/c428df6e80211c8415d4cd96a4f3707df8e080e3/docs/requirements-analysis/test-design-gatekeeper-ra-01-stakeholders-actors-authority-v0.3.md
[ra02]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/c428df6e80211c8415d4cd96a4f3707df8e080e3/docs/requirements-analysis/test-design-gatekeeper-ra-02-system-context-workflows-use-cases-v0.3.md
[ra03]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/c428df6e80211c8415d4cd96a4f3707df8e080e3/docs/requirements-analysis/test-design-gatekeeper-ra-03-review-package-content-provenance-validation-v0.3.md
[gate]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/c428df6e80211c8415d4cd96a4f3707df8e080e3/docs/reviews/test-design-gatekeeper-ra-03-gate-record-v0.2.md
[ctfl]: https://istqb.org/?download_id=3345&sdm_process_download=1
