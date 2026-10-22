# Test Design Gatekeeper

## RA-04 — Scope Qualification and Classification Boundaries

| Field | Value |
| --- | --- |
| Basis | Accepted RA-04 v0.2, originally dated 2026-09-16 |
| Acceptance and gate | All 15 requirements, three policy decisions and verified corrections accepted; v0.2 designated and GO to RA-05 recorded on 2026-09-17 in [SR-RA04-001 v0.2 / PG-RA04-001][review04] |
| Text maintenance | Consolidated on 2026-10-21; section numbers and identifiers retained |
| Decision authority | Project Owner |

This is the maintained scope-qualification policy. The [original v0.2 text][original] remains in Git history; earlier review hashes and byte counts identify that snapshot. Current capability and the development pause are described in [README.md](../../README.md). Acceptance of these requirements is not evidence that qualification works in the product.

## 1. Purpose, sources, and boundaries

RA-04 defines how to decide whether supplied test cases or assessment dimensions fit the MVP. Evidence that a test is outside scope is different from insufficient evidence to decide.

The [Charter][charter] sets product scope; [RA-01][ra01] sets human authority; [RA-02][ra02] defines the workflow; and [RA-03 v0.4][ra03] defines input, identity and sufficiency. The historical entry was authorized by [PG-RA03-001 v0.2][gate] on 2026-09-15. The accepted versions and their decisions are indexed in the [Requirements Analysis closure][phase].

The original analysis checked terminology against [ISTQB CTFL v4.0.1, Sections 2.2 and 4.1][ctfl] on 2026-09-16. TDG uses separate operational dimensions for test level, objective, design basis, technique and execution mode. These are not mutually exclusive labels. Its admission rules and evidence thresholds are project policy, not ISTQB certification criteria.

Detailed result meanings belong to [RA-05][ra05], techniques to [RA-06][ra06], LLM roles to [RA-07][ra07], security to [RA-08][ra08], input formats to [RA-09][ra09], and evaluation to [RA-10][ra10]. The examples below are synthetic fragments, not complete packages, implemented checks or an acceptance benchmark.

## 2. Separate the decisions

Record qualification per identifiable TC and, where justified, per assessment dimension. Package membership does not make every item eligible.

| Decision | Question | Consequence |
| --- | --- | --- |
| Intake and policy | Is processing permitted, and does the package meet RA-03 minimums? | A failed package minimum or policy gate follows RA-03; no supported substantive review |
| Item eligibility | Is this a recognizable TC with applicable accountable human control? | A positive case elsewhere in the package does not confer eligibility on this item |
| Domain qualification | Does the described test satisfy the MVP criteria in Section 3? | Supported in scope, established outside scope, or undetermined, with reasons |
| Capability availability | Can the authorized capability inspect the needed representation and perform this assessment? | Missing capability is reported separately from domain exclusion |
| Assessment sufficiency | Is the evidence sufficient for the particular claim? | Limit that claim while retaining independent supported work |

An in-scope functional case may lack the data needed for BVA. A missing expected result remains a quality gap under RA03-REQ-022; it does not automatically change test level or design basis.

These distinctions do not prescribe an execution pipeline. Inspection for qualification does not establish authorization or completion of substantive review. [RA-05 §3.2][ra05] defines the recorded statuses.

## 3. Independent dimensions and the MVP boundary

| Dimension | Evidence to inspect | Boundary or caution |
| --- | --- | --- |
| Declared feature or process | Supplied scope and the behavior actually described | Membership in the package alone does not establish a match |
| Test level | Identified test object, its boundary, objective, and relevant supplied context | The MVP supports system-level review; names of tools, endpoints or environments are insufficient shortcuts |
| Functional objective | The behavior or business rule being checked | Non-functional objectives are outside the supported assessment; mixed objectives need separation |
| Design basis | What determines test conditions, chosen data and required observations | External behavior can support the MVP route; dependence on implementation structure must be exposed |
| Technique evidence | Supplied rationale and demonstrable technique-related material | Naming EP, BVA, decision tables or state transitions is neither required nor sufficient; detailed assessment is RA-06 |
| Execution and context | Manual/automated mode, representation, role and environment where relevant | Preserve independently; absence matters only where it prevents a particular decision |

A positive domain conclusion requires support for all five criteria below. The subject is normally the whole TC; Section 5 governs narrower views.

| Criterion | Required support for the MVP route |
| --- | --- |
| RA04-C-01 | The described behavior belongs to the explicitly authorized feature or small process |
| RA04-C-02 | The identified object and objective support system-level testing of that product, rather than an isolated component, integration-specific objective, or acceptance-readiness objective |
| RA04-C-03 | The reviewed objective concerns functional behavior |
| RA04-C-04 | The proposed assessment has an external-behavior basis and does not depend on evaluating implementation-structure coverage |
| RA04-C-05 | The assessed subject is ordinary business-system behavior, not evaluation of AI/LLM behavior as the parked target domain |

A system boundary may include several deployable components. UI/API access, mocks, stubs, a database connection or an E2E label does not establish the test level. Integration and acceptance objectives remain outside this MVP even when functional and specification-based. A UAT environment name alone does not establish an acceptance objective.

An attributable experience-based rationale may support general functional review. Preserve its family and rationale; do not relabel error guessing as specification-based or add it to the four assessed techniques. Likewise, AI within an application does not by itself mean a case evaluates AI behavior: its supplied objective and relevant dependencies decide that boundary.

## 4. Evidence and qualification consequences

### 4.1 Evidence contract — accepted OD-RA04-001

Use substantive TC content and attributable supplied context identifying the object, objective and design basis. Shared package context is usable when it applies unambiguously to the item. No mandatory field template or direct requirement link is added.

Labels, titles, tool names and model confidence are insufficient alone. Absence of code does not prove black-box design. Missing execution-mode metadata need not block qualification when irrelevant to the criteria.

Keep declarations separate from evidence-supported interpretations. An isolated label discrepancy need not defeat otherwise sufficient context. Substantive contradictions about the object, purpose or basis require attributable clarification or a source-precedence decision. Do not automatically prefer the newest, longest or most formal-looking source.

Authorized, qualified RA-07 capabilities may assist interpretation, with visible derivation, evidence and uncertainty. Unsupported decisive inference leaves qualification undetermined and calls for the missing context. Model confidence cannot replace evidence or human confirmation. RA-04 selects no numerical threshold, classifier, prompt or implementation mechanism.

### 4.2 Consequence table

Apply the first applicable row after prerequisites and permitted separation. Retain additional established reasons and unresolved dimensions.

| Rule | Condition | Required meaning and action |
| --- | --- | --- |
| RA04-Q-01 | Package policy, trusted capture or a core minimum prevents the operation | Report the RA-03 prerequisite failure; do not manufacture a domain verdict or review result |
| RA04-Q-02 | Prerequisites permit inspection and reliable supplied evidence establishes failure of any criterion C-01 to C-05 | Established outside the requested MVP boundary, with the criterion and evidence; other axes may remain unknown |
| RA04-Q-03 | No established exclusion, but at least one decisive criterion lacks support or has an unresolved substantive conflict | Undetermined; identify the missing fact or conflict and the affected review limitation |
| RA04-Q-04 | All five criteria are supported for the identified subject | Supported in scope; substantive review still depends on item eligibility, capability and assessment-specific evidence |

A capability failure is not evidence of domain exclusion. Retain independent supported qualification evidence and show the capability limitation. Under [RA-05 §3.2][ra05], qualification not attempted is `NOT_EVALUATED`; an attempted qualification without a supported conclusion is `UNDETERMINED`. These remain distinct from an established exclusion.

An excluded item may receive attributable intake and scope diagnostics, but no unsupported technique or coverage review.

## 5. Technical detail, mixed cases, and human control

### 5.1 Technical detail is assessed by its role

Distinguish setup, observation and the basis used to derive the test. SQL preparing a known starting condition can coexist with a functional system scenario. For an internal observation, supplied context must explain whether it observes a business outcome or creates dependence on implementation structure. A private branch flag or code-coverage target differs from an API response or documented business state. Unexplained fields or logs need clarification, not a guessed black-box or white-box label.

Preserve a supplied "gray-box" label as source text. Describe the actual external, internal, mixed or unknown dependencies and their consequences instead of issuing a definitive gray-box verdict.

### 5.2 Separability — accepted OD-RA04-002

The accepted ability to review supported subsets is retained. A narrower view inside one TC is defensible only when all of the following hold:

1. The relevant behavior and source locations are identifiable without inventing or rewriting steps.
2. Required setup, data, preceding actions and shared context remain attached to the view.
3. The supported claim does not depend on an excluded internal/non-functional assertion or an unresolved assumption; any required observation for that claim is identifiable.
4. The view remains within the existing human-authorized boundary and reports every excluded part and limitation.

This is an assessment view, not a new authored TC. If these conditions cannot be established, do not claim a supported slice; record the known exclusion or unresolved basis according to Section 4. Preserving a visible subset inside the unchanged boundary does not require redundant scope confirmation. A deliberate change of that boundary requires ROLE-02 and a new package version. An oversized declared multi-process scope still requires human narrowing under RA02-REQ-035; partial review cannot bypass that requirement.

### 5.3 Package reporting — accepted OD-RA04-003

List each original TC once using its RA-03 internal identity. Show its domain conclusion or mixed/partial explanation, item-eligibility and capability restrictions, any separately assessed dimensions, and included/excluded identities with reasons. Duplicate external IDs or repeated text do not merge cases. A partial review cannot count as a complete review or several new TCs. Qualification counts are not coverage percentages or a package quality verdict. An empty supported subset means no supported substantive review is available.

ROLE-02 owns scope decisions, ROLE-04 disputed test-basis interpretations and source precedence, and ROLE-03 source correction. Findings and suggestions retain the RA-02 human-disposition boundary. Clarification cannot make unsupported evidence true or expand the MVP without Owner change approval.

Package/run consequences follow [RA-03 §16][ra03] and [RA-05 §5.1][ra05]: supplied-content changes create a new package version; a first applicable ROLE-04 interpretation decision can support an unassessed entry in an active run under RA-05's conditions. Replacing an applied premise, changing a behavior artifact or reassessing a committed entry requires a new run. A terminal run cannot resume; earlier evidence and outcomes remain preserved.

## 6. Requirements and acceptance state

All fifteen requirements are MUST / ACCEPTED under [SR-RA04-001 v0.2][review04], including the clarified positive direction of REQ-004. `Shall` states mandatory behavior and `MUST` its priority; neither selects an implementation. Requirement statements, priorities and upstream traces remain unchanged from the accepted v0.2 wording.

| ID | Requirement | Priority | Status | Upstream trace |
| --- | --- | --- | --- | --- |
| RA04-REQ-001 | TDG shall distinguish package prerequisites, item eligibility, domain qualification, capability availability and assessment-specific sufficiency before relying on an affected substantive result. | MUST | ACCEPTED | RA02-REQ-007; RA03-REQ-031; RA03-REQ-032 |
| RA04-REQ-002 | TDG shall retain test level, functional objective, design basis, technique evidence, execution mode and relevant context as separate dimensions without deriving one solely from another. | MUST | ACCEPTED | RA02-REQ-011; RA03-REQ-023 |
| RA04-REQ-003 | TDG shall ground qualification in addressable supplied content and applicable context; labels, titles, tool names, confidence scores and absence of implementation details shall not independently establish eligibility or exclusion. | MUST | ACCEPTED | RA02-REQ-012; RA03-REQ-020; RA03-REQ-039 |
| RA04-REQ-004 | A positive in-scope domain conclusion shall satisfy RA04-C-01 through RA04-C-05 for the identified subject; integration, acceptance, structural-coverage and AI/LLM-evaluation objectives shall not be admitted through relabeling. | MUST | ACCEPTED | Charter Sections 8–9; RA02-REQ-015; RA02-REQ-035; RA02-REQ-036 |
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

These are conditions for later test design, not executed tests. Each obligation directly references requirements, and every requirement has at least one obligation.

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

The separate `SR-RA03-OBS-001` action for RA03-VAL-014 was subsequently closed through the accepted RA-10 bridge, as recorded in [SR-RA10-001 v0.2][review10]. RA04-VAL-014 is a different obligation. Evaluation still needs independently adjudicated good, bad and borderline cases; these illustrative examples alone do not establish classifier effectiveness or form a held-out acceptance set.

## 9. Policy decision disposition

The three decisions below are accepted in [SR-RA04-001 v0.2][review04]. Their applicable rules are in Sections 4–5.

| Decision | Recommendation | Impact if revised | Status |
| --- | --- | --- | --- |
| OD-RA04-001 | Accept the evidence contract in Section 4.1: substantive object/objective/basis context, shared where unambiguous; labels and confidence alone are insufficient; no mandatory new field template. | Changes the boundary between supported and undetermined qualification; affects REQ-003/005/010 | ACCEPTED |
| OD-RA04-002 | Accept all four Section 5.2 conditions for a review view inside a TC; otherwise retain the limitation and request human clarification or source revision. | Changes safe partial-review eligibility and reporting; affects REQ-007/012 | ACCEPTED |
| OD-RA04-003 | Accept item inventory plus separately marked partial dimensions, with no qualification-to-coverage percentage or whole-package quality score. | Changes aggregation and the RA-05 handoff; affects REQ-008/013/015 | ACCEPTED |

## 10. Author check, handoff, and exit

[SR-RA04-001 v0.2][review04] records the Owner's acceptance on 2026-09-17: all fifteen requirements, three policy decisions, the static review, three verified wording corrections, the v0.2 baseline and GO to RA-05. RA-04 is closed. `SR-RA04-F-001` clarified the positive direction of REQ-004 and the MVP exclusions in EX-11 and EX-20; those corrections are already included here.

The original document checks found 15/15 requirements with direct validation links, 15/15 obligations with valid targets and 28 direct REQ–VAL links. The same assistant authored and checked the source; the Owner performed the walkthrough. These are historical document checks, not independent assurance, executed product tests or model-effectiveness evidence.

Detailed outcomes, techniques, model roles, protection, formats and evaluation are governed by the related sources in Section 1. Historical GO to RA-05 does not override the current development pause. `SR-RA03-OBS-002` / R-08 remains relevant: additions need a distinct decision, risk or validation purpose, and documentation must not delay empirical evaluation. Current work is described in [README.md](../../README.md).

[charter]: ../governance/test-design-gatekeeper-project-charter-v0.4.md
[ra01]: test-design-gatekeeper-ra-01-stakeholders-actors-authority-v0.3.md
[ra02]: test-design-gatekeeper-ra-02-system-context-workflows-use-cases-v0.3.md
[ra03]: ra-10/test-design-gatekeeper-ra-03-review-package-content-provenance-validation-v0.4.md
[gate]: ../reviews/test-design-gatekeeper-ra-03-gate-record-v0.2.md
[review04]: ../reviews/test-design-gatekeeper-ra-04-focused-static-review-v0.2.md
[phase]: ra-10/test-design-gatekeeper-requirements-analysis-readiness-v0.2.md
[ra05]: ra-05/test-design-gatekeeper-ra-05-findings-dispositions-persistence-v0.2.md
[ra06]: ra-06/test-design-gatekeeper-ra-06-technique-applicability-design-coverage-v0.2.md
[ra07]: ra-07/test-design-gatekeeper-ra-07-llm-roles-qualification-v0.2.md
[ra08]: ra-08/test-design-gatekeeper-ra-08-confidentiality-security-privacy-v0.2.md
[ra09]: ra-09/test-design-gatekeeper-ra-09-data-representations-import-export-contracts-v0.2.md
[ra10]: ra-10/test-design-gatekeeper-ra-10-evaluation-acceptance-v0.2.md
[review10]: ra-10/test-design-gatekeeper-ra-10-focused-static-review-v0.2.md
[ctfl]: https://istqb.org/?download_id=3345&sdm_process_download=1
[original]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/ade85a1b39e145ed9409d94869c3041bbe7219b1/docs/requirements-analysis/test-design-gatekeeper-ra-04-scope-qualification-classification-boundaries-v0.2.md
