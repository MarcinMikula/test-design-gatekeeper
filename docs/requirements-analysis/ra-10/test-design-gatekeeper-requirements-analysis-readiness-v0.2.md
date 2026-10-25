# Test Design Gatekeeper

## SR-RA-001 — Consolidated Requirements Analysis Review and Phase-Gate Record

| Field | State |
| --- | --- |
| Basis | Accepted SR-RA-001 v0.2, originally dated 2026-09-22 |
| Recorded decision | Requirements Analysis closed and GO to Solution and Architecture Design granted by the Owner on 2026-09-22; Section 7 preserves the decision and its scope |
| Review boundary | Requirements documents, their validation links and readiness for design; no product-test or independent expert assurance claim |
| Planning evidence | Flexible capacity, preliminary design effort and resource risks accepted for design entry; full-delivery feasibility and a completion date were not established |
| Text maintenance | Consolidated on 2026-10-24; section numbers, decisions and historical evidence retained |

This record explains why the requirements phase was closed and design was authorized. It also indexes the accepted requirements. The [original v0.2 record][original] remains in Git history. The counts, work sequence and estimates below describe the September review and planning decision; they are not a current progress report or a new authorization.

**Development is paused for documentation cleanup.** [README.md](../../../README.md) describes current capability and the next agreed work. The historical design GO does not override that pause. Requirements acceptance and document traceability do not establish product usefulness, model quality, hardware feasibility or permission to process confidential material.

## 1. Effective source inventory

The links below lead to the maintained requirements. Their accepted versions are read with the decision records they cite. RA-03 v0.4 includes the source-table corrections accepted through [SR-RA10-001 v0.2][sr10]; that record also closes RA-10 and the targeted `SR-RA03-OBS-001` action. Earlier pending labels do not reopen those decisions.

| Source | Accepted version | Requirements | Validation obligations |
| --- | --- | ---: | ---: |
| [Project Charter][charter] | v0.4 | — | — |
| [RA-01][ra01] | v0.3 | 16 | 10 |
| [RA-02][ra02] | v0.3 | 36 | 20 |
| [RA-03][ra03] | v0.4 | 50 | 32 |
| [RA-04][ra04] | v0.2 | 15 | 15 |
| [RA-05][ra05] | v0.2 | 22 | 16 |
| [RA-06][ra06] | v0.2 | 20 | 14 |
| [RA-07][ra07] | v0.2 | 20 | 14 |
| [RA-08][ra08] | v0.2 | 24 | 16 |
| [RA-09][ra09] | v0.2 | 24 | 16 |
| [RA-10][ra10] | v0.2 | 22 | 16 |
| Total |  | 249 | 169 |

The [trace ledger][trace] identifies the exact filenames, byte counts and SHA-256 values inspected on 2026-09-22. RA-01/02/04–09 were checked at commit `be657405920aba0f2da2653f56266942a6ecc22e`; RA-03 v0.4 and RA-10 v0.2 were the accepted snapshots identified in [SR-RA10-001 v0.2][sr10]. The hashes describe those inspected snapshots, not later editorial maintenance. Acceptance and repository publication remain separate events.

## 2. Bidirectional trace review

### 2.1 Method and result

The September review expanded the recorded requirement-to-validation links, including shorthand and ranges, compared forward and reverse tables where both existed, and checked endpoint existence and whether the validation purpose supported the accepted requirement. Intermediate workflow, authority and decision-table links were inspected. A downstream requirement was used only when its validation purpose supported the earlier requirement; a shared reference alone was insufficient.

| Check | Result | Meaning |
| --- | --- | --- |
| Direct REQ–VAL relations | 424 distinct pairs | Relations already declared in the validation tables |
| Requirements with a local direct route | 239/249 | Ten earlier requirements additionally need the inspected paths in Section 2.2 |
| VAL rows with direct requirement targets | 165/169 | Four obligations use controlled workflow or decision-table objects |
| All requirements with a justified route | 249/249 | At least one direct or inspected intermediate route per requirement |
| All VAL with existing accepted requirement targets | 169/169 | No validation obligation is left attached only to an unresolved label |
| Published forward/reverse mirrors, RA-06–RA-10 | 230/230 edges agree | Earlier slices are not retrospectively claimed to publish equivalent mirrors |
| Explicit full REQ/VAL references across the ten sources | 752 source/identifier pairs resolve | A repeated identifier in another source is a separate reference check |
| Dangling endpoints or duplicate recorded paths | 0 / 0 | Within the inspected ledger |
| Full executable and clause-level test coverage | NOT ESTABLISHED | This belongs to later test analysis, design and execution |

The ledger retains 530 distinct paths: 424 direct, 41 through the accepted RA-03 IS bridge, 52 through inspected authority/workflow links and 13 through existing requirement-refinement chains. Both indices derive from that same set.

**Meaning of PASS:** every requirement and validation obligation had an inspected route at document level. This does not prove complete clause-level or executable coverage. One obligation can require several test conditions and cases. No product test was run by this audit; the Owner accepted the disclosed review evidence and its limits.

### 2.2 Ten requirements without local direct VAL references

These inspected paths connect existing controls and refinements. They add no behavior to the accepted requirements. Further supporting paths remain in the ledger.

| Accepted requirement | Inspected route to validation | Why the route is relevant |
| --- | --- | --- |
| RA01-REQ-004 | AUTH-02 → RA01-VAL-001 | The requirement names the scope-authority action; the VAL explicitly covers the authority table |
| RA01-REQ-005 | AUTH-04 → RA01-VAL-001 | The requirement names ROLE-04 interpretation authority; the VAL covers the applicable human action |
| RA01-REQ-006 | RA02-REQ-004 → RA02-VAL-002; RA05-REQ-022 → RA05-VAL-007 | Explicit refinements retain the source-editing prohibition; input and disposition checks challenge source mutation |
| RA02-REQ-002 | RA05-REQ-014 → RA06-REQ-019 → RA06-VAL-014 | Explicit refinements preserve the supplied-only boundary in record use and technique review; validation challenges external/history enrichment |
| RA02-REQ-003 | RA05-REQ-014 → RA06-REQ-019 → RA07-REQ-003 → RA07-VAL-009 | The cited refinement chain reaches bounded model context; hostile instructions cannot confer retrieval permission |
| RA02-REQ-007 | PWF-03 → RA02-VAL-001; RA03-REQ-031 → RA03-VAL-031 | Nominal prerequisite ordering is supported by the later explicit validation-stage negative checks |
| RA02-REQ-013 | AF-RA02-006/007/008 → RA02-VAL-007 | Mixed, ambiguous and unsupported qualification outcomes are explicitly challenged |
| RA02-REQ-014 | AF-RA02-006 → RA02-VAL-007 | A mixed package preserves the supported subset and visible exclusions |
| RA02-REQ-022 | PWF-13/14 → RA02-VAL-001; RA05-REQ-006 → RA05-VAL-005 | Result context is exercised in the workflow and challenged through the later claim/evidence contract |
| RA02-REQ-025 | PWF-14/15 → RA02-VAL-001; RA05-REQ-014 → RA05-VAL-013 | Inspectable context and viewing authority are exercised without granting disposition authority |

AUTH identifiers belong to RA-01; PWF and AF identifiers belong to RA-02. An authority check covers the human action actually permitted. It must not be turned into permission for TDG to edit or approve testware or make a phase-gate decision.

### 2.3 Four obligations using controlled intermediates

| Existing obligation | Inspected intermediary | Requirement endpoint evidence |
| --- | --- | --- |
| RA02-VAL-001 | All PWF-01 through PWF-18 | Every step is explicitly mapped in Appendix A; the complete nominal business workflow remains the validation subject |
| RA02-VAL-007 | AF-RA02-006 through AF-RA02-009 | Mixed subset → REQ-013/014; ambiguity/structural exclusion → REQ-013; misleading labels → REQ-011/012 |
| RA02-VAL-010 | AF-RA02-011 and UC-RA02-004 | REQ-016/026 preserve ROLE-04 authority, UNKNOWN and escalation when no separate expert is available |
| RA03-VAL-014 | IS-01 through IS-11 in corrected RA-03 v0.4 | The accepted RA-10 §8.1 bridge provides 41 edges to 23 RA-03 requirements; SR-RA10-001 v0.2 records correction verification and closure |

REQ shorthand in the two middle rows means RA02-REQ. The accepted RA-03 bridge is reused without expansion. Closing its targeted observation leaves the general trace duty in force.

## 3. Cross-slice consistency inspection

The following are the September review's document-level challenges and supported consequences. They are retained as review evidence, not observed runtime behavior or an exhaustive proof of every combination.

| Challenged boundary | Supported consequence | Principal evidence |
| --- | --- | --- |
| A source is readable and captured but minimum content is absent | Capture can be retained with an explicit deficiency; substantive package review cannot be claimed | RA03-REQ-031/032/033; RA09-REQ-013/014/015 |
| Minimum passes but all requested substantive work lacks conditional evidence | Preserve minimum admission and the limitation; use actual ledger entries to determine terminal NONE/PARTIAL, without inventing an attempted assessment | Corrected RA-03 §15.3; RA05 §§3.2–3.3; RA10-VAL-015 |
| A local source conflict coexists with independent supported evidence | Retain the conflict and ROLE-04 authority; isolate supported work only where separability is defensible | RA03 IS-08/09; RA04-REQ-005/007; RA05-REQ-003 |
| Another TC has a positive origin or copied accountability label | Eligibility is item-specific; imported labels cannot grant human authority | RA03-REQ-011/021; RA04-REQ-009; RA09-REQ-008/024 |
| Automated, integration or gray-box wording appears in supplied testware | Preserve independent classification axes and actual basis evidence; execution mode alone does not decide eligibility | RA03-REQ-023; RA04-REQ-002/003/006/014; RA07-REQ-020 |
| A TC exercises a boundary but lacks its expected result | Preserve supported planned exercise and report the separate expectation gap; do not invent the missing result | RA03-REQ-022; RA06-REQ-005/007/015; RA09-REQ-007 |
| Correct arithmetic follows an unconfirmed semantic premise | The business conclusion retains derivation and uncertainty; arithmetic cannot supply human confirmation | RA05-REQ-007/008; RA06-REQ-016; RA07-REQ-005; RA10-REQ-009 |
| Capture mapping, behavior or only rendering changes | Changed recapture creates a package version; changed assessment behavior creates a run; rendering alone does not reassess source | RA03-REQ-044/045/046; RA05 §6; RA09-REQ-021 |
| A human confirms the first applicable interpretation during an active run | Use the accepted narrow first-confirmation rule; replacing an already applied interpretation or editing behavior has different consequences | RA05 §5.1/§6; RA06 §9.3; RA07-REQ-016 |
| An LLM qualified for assessment mapping is asked to map importer fields | RA-09 does not authorize runtime LLM capture mapping; operational qualification does not grant an unlisted task | RA07-REQ-001/009; RA09 §5.2 and REQ-011; SR-RA09-F-002 |
| A run completes with no substantive ledger entry or with zero findings | Completion, availability, issue count and human disposition remain distinct; neither outcome supplies a completeness verdict | RA05-REQ-002/003/004/005; RA09-REQ-017; RA10-REQ-008 |
| A local model is qualified but protected-data controls are missing | Model permission does not establish sealed readiness; the protected path stays unavailable | RA07-REQ-009; RA08-REQ-001/023; RA10-REQ-016/018 |
| Mandatory audit fails while optional diagnostics also fail | Stop the affected authority/protection-dependent operation; preserve safe history and contain copies; do not equate optional diagnostic loss with every mandatory control loss | RA08 §6.2/§7.1 and REQ-015/020; RA05-REQ-019 |
| An export is valid JSON and contains historical accepted statuses | Report import cannot restore trusted authority, dispositions or package identity; unknown content and omissions stay visible | RA09-REQ-020/022/024; RA05-REQ-021 |
| Public development examples or repeated favorable runs are used to claim independent acceptance | Exposure, family partitions, complete attempt cost and predeclared selection rules govern the strength of the claim | RA07-REQ-011/014; RA10-REQ-002/013/019/022 |
| Every requirement is accepted and has a VAL route | The product hypothesis and resource feasibility remain untested; a design gate depends on its separately recorded readiness evidence and Owner decision | RA10-REQ-015/020/021; Charter §18.6 |

The review identified no additional blocking contradiction in these boundaries. Later test design must still cover adverse combinations, all supported entry points and invalid transitions. The broad RA-02 nominal workflow check cannot replace negative and fault tests.

## 4. Sequenced delivery work packages

This is the work-package breakdown accepted for design entry on 2026-09-22. It groups related requirements for further estimation; all accepted MUST requirements remain in scope. A limited first demonstration cannot be called the full MVP. The table preserves the original outputs, dependencies and uncertainties, rather than reporting their present completion.

The first usable demonstration was to use eligible laboratory data, with security considered from the start. Sealed verification and authorization remain mandatory before confidential input.

| Work package | Concrete output and completion evidence | Dependencies / earliest authorized stage | Main effort and uncertainty |
| --- | --- | --- | --- |
| B-01 — Architecture and design decisions | A reviewed component/data-flow design; local persistence and identity model; contract/schema approach; operational entry points; limits; error, authorization and protection allocation | Explicit GO to Solution and Architecture Design; baseline RA-01–RA-10 | Design and threat-analysis work; entry-point and deployment choices remain open; no UI, database engine or model selected by this record |
| B-02 — Reference material and test analysis | Versioned customer-creation families; clean, deficient and insufficient examples; verified mutations; human oracle; exposure/partition manifest; traceable test conditions | Can be planned from accepted requirements; executable preparation follows the applicable implementation permission; coordinates with B-01 | Domain authoring and human adjudication; family diversity and unresolved interpretation dominate; the discount example is exposed development material |
| B-03 — Safe capture and package lifecycle | Native local JSON and the defined CSV path; preserved source/projection; exact origin handling; locators; minimum checks; coherent capture and version lineage | Reviewed B-01 design and separate implementation authorization; B-02 fixtures | Parser and persistence failure boundaries; malformed/unknown input; conditional sufficiency and ambiguous origin |
| B-04 — Qualification and review records | Item/domain qualification; supported subsets; requested-work ledger; run states and availability; attributable evidence, human interpretation and disposition history | B-03 foundations; RA-04/05 contracts; tests from B-02 | Multi-axis classification and partial outcomes; human authority; retries, stale writes and interrupted work |
| B-05 — Four-technique assessment | Separate EP, BVA, decision-table and state-transition assessment against versioned, supported premises; criterion and mapping evidence; visible limits | B-04; confirmed models and oracles from B-02; each technique can be delivered as a bounded increment | Business-model adequacy and mapping uncertainty; unsupported precision, ties, guards or missing expectations must remain unresolved |
| B-06 — Controlled local LLM contribution | Segregated candidate evaluation; bounded context and output validation; exact task/configuration permission; attempt history, abstention and failure handling | B-03/04 contracts; B-02 partition controls; reviewed B-01 design; eligible data and applicable evaluation authorization | Actual local hardware performance and semantic reliability; begin with a bounded task envelope and retain every unqualified dimension as unavailable |
| B-07 — Human review and local export | Authorized inspection/disposition, version comparison and JSON/Markdown export with selected history and explicit evidence limits; source TC repaired externally | B-04 records; RA-08 export constraints and RA-09 contracts | Human effort and clarity; safe rendering, selected-history semantics and coherent failed/denied export |
| B-08 — Evaluation and qualification evidence | Exploratory comparisons; recorded resource/quality/burden evidence; approved numerical criteria and sample plan; subsequent frozen qualification and acceptance campaigns | B-02 plus the actual B-03–07 capabilities being claimed; criteria before decision-bearing runs | Human adjudication and study time; negative assistance; repetitions and sample sufficiency; no outcome promised in advance |
| B-09 — Sealed readiness | Actual deployment inventory and threat model, enforced identity/permissions, protected copies/keys/audit, retention/deletion/restore, valid egress observation and ROLE-09 readiness decision | Security design begins in B-01; implemented applicable paths; eligible synthetic verification before protected use | Deployment-specific controls and security expertise; dependency and copy-path coverage; cannot be waived by a successful lab benchmark |
| B-10 — Integrated verification and release decision | Completed applicable component, integration, workflow, fault, security and regression evidence; defect dispositions; STLC completion report and explicit product/pilot decision | Verification grows with every increment; final report after the evidence required for the claimed release envelope | Regression across histories and failure states; incomplete evidence and residual risks; no automatic acceptance from green checks |

RA-03/09 principally drive B-03; RA-01/02/04/05 drive B-04/07; RA-06 drives B-05; RA-07 drives B-06; RA-08 drives B-01/03/06/07/09; RA-10 drives B-02/08/10. These are planning allocations; the REQ–VAL ledger records the inspected validation links.

The accepted next planning step was to break these packages into bounded deliverables against the selected design, then reconcile responsibilities, estimates and capacity before implementation authorization. Section 5 preserves the input used for design entry. Current work is described in [README.md](../../../README.md).

## 5. Remaining work and prerequisite milestones

The table records the allocations at design entry. Roles follow the accepted authority model; they do not appoint extra people or make an administrator the architect, developer or security approver. ROLE-10 assigns contributors, and combined roles retain their independence limitations.

| Allocation | Accountable decision or work owner | Required before |
| --- | --- | --- |
| A-01 — Capacity declaration and initial effort/resource assessment | COMPLETE FOR DESIGN ENTRY — Owner input and Sections 5.1–5.3 assessment ACCEPTED; declared risks carried | Design-entry condition satisfied; refine work-package estimates against design before implementation authorization |
| A-02 — Concrete architecture, schema, database, entry-point and deployment choices; impact and executable backlog | ROLE-10 assigns design/implementation responsibility; ROLE-09 owns protection decisions | Design baseline and later implementation authorization |
| A-03 — Reference family content, mutation-effect checks, human oracle and partition governance | ROLE-04 for supplied business meaning; ROLE-08 for evaluation governance | Use as reference/qualification evidence and before any claim of independent held-out acceptance |
| A-04 — Numerical quality, burden, resource and stability criteria; sample/repetition/stopping plan | ROLE-08 for qualification; ROLE-10 for product acceptance | Applicable decision-bearing evaluation, after labelled exploratory measurement |
| A-05 — Actual local runtime/configuration and task envelope measurement | Assigned implementation/evaluation contributors under ROLE-08 | Corresponding feasibility or operational qualification claim; 8 GB alone is not evidence |
| A-06 — Protected-copy policy, enforced controls, current deployment verification and explicit sealed permission | ROLE-09, with assigned engineering support | First confidential input or affected changed protected use |
| A-07 — Executable test conditions/cases, environment/data readiness, execution, defect handling, regression and completion report | ROLE-10 assigns test work; ROLE-08 governs qualification evidence | Applicable increment completion, reliance and product/pilot gates |

A-01 was accepted as sufficient for design entry. A-02–A-07 were allocated to later milestones. These entries preserve the decision and dependencies; they are not a current completion tracker.

### 5.1 Recorded capacity and working model

On 2026-09-22 the Owner described a spare-time project with **approximately 5 flexible hours per week**, working alone with AI assistance. One hour on five days was an illustration, not a required rhythm. Lower, higher and zero-hour weeks carry no catch-up obligation or completion-date commitment.

This is one human's capacity, including understanding, decisions, design, implementation oversight, verification, learning, adjudication and fixes. AI is neither a second human contributor nor an assumed productivity multiplier. Combined roles still require appropriate authority and competence, and self-review remains non-independent.

### 5.2 Initial effort assessment for the design gate

The Owner endorsed this **low-confidence estimate proposed by the assistant on 2026-09-22**. It covers active human effort with AI assistance, including reading and corrections. It is a historical planning estimate, not measured productivity, a timebox or a commitment.

| B-01 design activity | Initial active-human effort | Required output |
| --- | ---: | --- |
| Component boundaries and one complete local review flow | 4–8 hours | Reviewed flow, responsibilities and operational entry-point decision |
| Data, identity, persistence and import/export design | 4–8 hours | Coherent source/package/run/history model and contract decisions |
| Model interfaces and protection architecture | 4–8 hours | Bounded LLM/qualification interfaces, laboratory/sealed boundaries and control allocation |
| Static design review and next-increment planning | 4–8 hours | Reviewed decisions, resolved blocking defects, refined implementation work and STLC allocations |
| Initial B-01 total | 16–32 hours | Reviewed design package within the stated boundary |

The estimate excludes product implementation, executable benchmark construction/campaigns and sealed-control verification. It was to be reviewed after the first design activity using actual effort and remaining scope; increased complexity could increase the estimate. Incomplete design must not be hidden to fit the range. This record contains no measured actual effort or calendar deadline.

Section 4 retains the workload and uncertainty for B-02–B-10. The main uncertainties were human corpus/oracle work and evaluation, technique models and mapping, local-model capability and deployment-specific protection. A reliable numeric estimate for the full MVP was not established. The design-entry decision required later increment estimates, including benchmark and verification work, before implementation authorization.

### 5.3 Resource risks and accepted disposition

| Constraint or risk | Accepted response |
| --- | --- |
| Variable spare-time capacity and one human contributor | Work through small increments, preserve a short next-action record and permit pauses; retain self-review and competence limitations |
| Documentation growth under SR-RA03-OBS-002 / R-08 | Reuse this record and existing requirements; keep one coherent design package and record decisions when they resolve an actual choice |
| AI output needs human verification; total engineering/evaluation effort is uncertain | Include understanding and rework in estimates; revise them from completed work before committing to another increment |
| Local-model feasibility and sealed readiness are unproven | Obtain the applicable measurements and protection evidence at their allocated milestones; no resource estimate grants protected-data permission |

The Owner accepted the capacity, preliminary estimate and carried risks as sufficient to begin bounded design. Full-delivery feasibility was not established. R-08 remains active; the current cleanup addresses that risk. Section 7 records the phase decision.

## 6. Observations, proportionality and gate state

| Item | Recorded disposition and continuing duty |
| --- | --- |
| `SR-RA10-F-001` / `SR-RA10-F-002` | Closed after verified corrections; [SR-RA10-001 v0.2][sr10] retains the findings and acceptance |
| `SR-RA03-OBS-001` | The RA03-VAL-014 bridge action is closed; general bidirectional trace duties remain |
| `SR-RA03-OBS-002` / R-08 | Active: reuse the requirements and existing evidence, avoid parallel status documents and review documentation effort against the project's capacity |

The consolidated review, design-entry resource assessment and phase decision were accepted on 2026-09-22; Section 7 records their scope. Implementation, operational model reliance, protected use and product acceptance were not authorized by this record. Their separate prerequisites remain applicable.

## 7. Recorded Owner acceptance and phase gate

On 2026-09-22 the Owner quoted the concrete pending decision:

> Czy zatwierdzasz zaktualizowany rekord `SR-RA-001`, wraz z oceną zasobów i pozostawionymi ryzykami, zamykasz fazę Requirements Analysis oraz udzielasz `GO` do Solution and Architecture Design?

The Owner answered:

> Tak zatwierdzam, wyrównajmy dokumentacje w repozytorium.

| Decision scope | Recorded disposition |
| --- | --- |
| Updated SR-RA-001 v0.1, including the trace review and controlled correspondences | ACCEPTED |
| Work-package sequence, downstream allocations and resource/risk assessment | ACCEPTED; A-01 satisfied for design entry; later prerequisites retain their milestones |
| Approximately 5 hours per week and solo AI-assisted work | Flexible planning reference retained; no fixed cadence or completion-date commitment |
| Initial 16–32-hour B-01 design estimate | Endorsed as a low-confidence, revisable planning estimate; refine after the first completed activity |
| Requirements Analysis | CLOSED — all ten slices and consolidated exit review complete |
| Solution and Architecture Design | GO GRANTED — proceed with B-01 under the accepted requirements baseline |
| Documentation publication | AUTHORIZED — align the repository with these accepted artifacts and decisions |
| R-08, independence and resource uncertainties | CARRIED as stated; no claim of full-delivery feasibility or independent expert assurance |

The authorized work at that time was Solution and Architecture Design: component boundaries and a bounded review flow; data, identity and contracts; model and protection interfaces; then static review and refined implementation/test planning. That gate did not authorize product implementation, operational LLM reliance, confidential input or product acceptance. It does not override the current development pause.

### 7.1 Administrative change verification

The accepted [v0.1 review input][accepted-review] is retained: 32,071 bytes, SHA-256 `4c32c1638d0817ba7f09abe4e1cfbbc7bd7adf82ac8acfbfa7dba98694bb798d`. The original v0.2 update recorded the subsequent approval without changing the requirements, validation statements, trace evidence, work-package outputs, estimates, capacity flexibility or downstream restrictions.

The [trace ledger][trace] remains unchanged, with SHA-256 `82e7b2bcc59183532ad5edb1673555f38a777d547d24637dbc7362509dbe96ed`. Its pre-acceptance status describes when it was prepared; Section 7 supplies the later acceptance. That historical label does not reopen the phase. The current editorial cleanup changes neither that ledger nor the Owner's decision.

The same assistant authored and reviewed the material; no independent expert assurance is claimed. No product requirement, scope expansion, model selection or security exception follows from maintaining this record.

## Appendix A. Nominal workflow correspondence

This is the explicit semantic mapping used for the previously indirect RA02-VAL-001 route. All identifiers in this table belong to RA-02. The PWF steps and requirement statements remain unchanged. The evidence ledger records source locations, individual paths and the corresponding reverse index.

| Workflow step | Existing requirement endpoints | Inspected meaning |
| --- | --- | --- |
| PWF-01 | REQ-001 | Deliberate bounded package submission |
| PWF-02 | REQ-004 | Submission context preserves source testware |
| PWF-03 | REQ-005/006/007/008 | Authority, profile and minimum checks precede review |
| PWF-04 | REQ-008/009/010/016 | Missing, conditional, malformed and conflicting evidence remains visible |
| PWF-05 | REQ-001/018 | Available package and capture identity are explicit |
| PWF-06 | REQ-011/012/013 | Independent classification axes and scoped outcomes |
| PWF-07 | REQ-005/026 | Scope-owner authority and no duplicate unchanged confirmation |
| PWF-08 | REQ-016/026 | Human supplied-rule interpretation authority |
| PWF-09 | REQ-013/014/015 | Supported subset, exclusions and scope mismatch |
| PWF-10 | REQ-017/018 | Distinct run and relevant version identities |
| PWF-11 | REQ-019 | Confirmed structured evidence for deterministic claims |
| PWF-12 | REQ-020/021 | Qualified authorized LLM use and no silent substitution |
| PWF-13 | REQ-022/023 | Scoped evidence and no assigned human disposition |
| PWF-14 | REQ-022/025 | Inspectable evaluated/unevaluated context |
| PWF-15 | REQ-025/026 | Viewing and disposition preserve their authorities |
| PWF-16 | REQ-005/027/030 | Acting role, self-review and decision history |
| PWF-17 | REQ-004 | External human testware repair |
| PWF-18 | REQ-001/026/028 | Human-controlled new bounded package version |

## Record history

| Version | Date | Change |
| --- | --- | --- |
| 0.1 — initial draft | 2026-09-22 | Consolidated accepted source inventory; bidirectional trace inspection and controlled correspondences; cross-slice challenges; delivery work packages, downstream allocations and explicit remaining capacity/effort gap |
| 0.1 — working update | 2026-09-22 | Owner's flexible approximately 5-hour weekly capacity and solo AI-assisted working model recorded; initial design-effort estimate, remaining workload and resource-risk response added; consolidated acceptance and design GO remain pending |
| 0.2 | 2026-09-22 | Later explicit Owner acceptance, risk disposition, Requirements Analysis closure, design GO and documentation-publication authorization recorded; accepted substantive content and evidence retained |

The original records remain in Git history. Editorial maintenance uses this file and the existing evidence; it does not create another review or document version.

[charter]: ../../governance/test-design-gatekeeper-project-charter-v0.4.md
[ra01]: ../test-design-gatekeeper-ra-01-stakeholders-actors-authority-v0.3.md
[ra02]: ../test-design-gatekeeper-ra-02-system-context-workflows-use-cases-v0.3.md
[ra03]: test-design-gatekeeper-ra-03-review-package-content-provenance-validation-v0.4.md
[ra04]: ../test-design-gatekeeper-ra-04-scope-qualification-classification-boundaries-v0.2.md
[ra05]: ../ra-05/test-design-gatekeeper-ra-05-findings-dispositions-persistence-v0.2.md
[ra06]: ../ra-06/test-design-gatekeeper-ra-06-technique-applicability-design-coverage-v0.2.md
[ra07]: ../ra-07/test-design-gatekeeper-ra-07-llm-roles-qualification-v0.2.md
[ra08]: ../ra-08/test-design-gatekeeper-ra-08-confidentiality-security-privacy-v0.2.md
[ra09]: ../ra-09/test-design-gatekeeper-ra-09-data-representations-import-export-contracts-v0.2.md
[ra10]: test-design-gatekeeper-ra-10-evaluation-acceptance-v0.2.md
[sr10]: test-design-gatekeeper-ra-10-focused-static-review-v0.2.md
[trace]: test-design-gatekeeper-requirements-analysis-traceability-audit-v0.1.json
[accepted-review]: test-design-gatekeeper-requirements-analysis-readiness-v0.1.md
[original]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/4e9ddf926c1863c4de71067c8e29c55a3372c895/docs/requirements-analysis/ra-10/test-design-gatekeeper-requirements-analysis-readiness-v0.2.md
