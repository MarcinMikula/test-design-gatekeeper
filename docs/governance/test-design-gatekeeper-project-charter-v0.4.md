# Test Design Gatekeeper

## Project Charter / Concept & Feasibility

| Field | Value |
| --- | --- |
| Basis | Accepted Charter v0.4, originally dated 2026-09-12 |
| Baseline designation | Project Owner decision, 2026-09-15; [PG-RA03-001][baseline] |
| Text maintenance | Consolidated on 2026-10-19; section numbers and decision/risk identifiers retained |
| Decision authority | Project Owner |
| Product descriptor | An evidence-grounded, ISTQB-informed test case review assistant |

This is the maintained description of the accepted concept and scope. The [original v0.4 text][original] remains in Git history; byte counts and hashes in earlier reviews describe that historical snapshot. Later acceptance resolved its preparation-time candidate labels. Current implementation, the documentation-cleanup pause and next work are described in [README.md](../../README.md).

### v0.4 controlled amendment summary

| Change | Accepted decision | Meaning |
| --- | --- | --- |
| `CR-RA03-001` | `OD-RA03-004`, 2026-09-12 | Positive origin eligibility depends on explicit ROLE-03 human accountability, including controlled AI-assisted testware. No authorship inference or test generation is added. |
| `CR-RA03-002` | `OD-RA03-003`, 2026-09-12 | Supplied risks, prior defects, heuristics and attributable experience-based reasoning may form test-basis evidence. No fifth technique is added. |

Both amendments were reviewed and the v0.4 replacement baseline was designated on 2026-09-15. The original concept-phase GO remains dated 2026-09-08.

## 1. Purpose of this Charter

This Charter defines the problem, product hypothesis, intended users, scope, authority, protection principles, evaluation approach and principal risks. It established the concept basis for Requirements Analysis. Detailed behavior belongs in the accepted requirements and design referenced below.

## 2. Problem statement

Test-case design can miss negative partitions, boundaries, condition combinations or state transitions. Preconditions and expected results may be vague; traceability may be weak; missing requirements may be treated as complete. Time pressure, fragmented documentation, complexity and limited review capacity can contribute.

LLMs can produce convincing reviews while inventing rules or missing relationships. A useful assistant needs evidence and controls beyond fluent language.

## 3. Product vision

Help a tester review accountable human-authored or human-controlled AI-assisted cases before peer review or formal approval. Relate cases to the supplied test basis, identify supported gaps, distinguish reproducible findings from probabilistic suggestions, and withhold conclusions when evidence is insufficient. Human reviewers retain responsibility for decisions and edits.

## 4. Product hypothesis

Combining deterministic controls, bounded local-LLM analysis, explicit evidence and human decisions will identify more material design gaps than unaided review or either technical component alone, without unacceptable review effort or disclosure of confidential testware outside the approved environment.

This remains a hypothesis to test, not an established product benefit.

## 5. Intended users and stakeholders

### 5.1 Primary user

A tester or test analyst preparing or reviewing functional test cases against requirements and business rules.

### 5.2 Secondary user

A test lead or reviewer inspecting gaps, unresolved questions and decisions. Business analysts, coordinators and domain experts may support the work within their competence. The workflow remains centered on testware controlled by an identified accountable human.

### 5.3 Decision authority

Humans control scope, supplied evidence, confirmation of interpretations, finding dispositions, test-case edits and readiness for further use. TDG does not own or approve testware. The responsibility and authority model is maintained in [RA-01][ra01].

## 6. Primary use case

1. The tester defines a bounded scope and supplies the test basis and cases.
2. TDG checks scope and assessability, then relates supported basis elements, risks and cases.
3. Deterministic controls check confirmed structured rules; a qualified local LLM may contribute supported semantic suggestions.
4. An authorized human reviews findings and suggestions, resolves interpretations and records dispositions.
5. The testware owner edits the source cases outside TDG and may submit a revised package.

The product supports pre-review before a human gate. It is not an organizational release gate. Missing, contradictory or mismatched inputs must cause a visible limitation, narrowed assessment or refusal. The human supplies missing context; TDG cannot retrieve unsubmitted documentation or invent rules to complete the review.

## 7. Unit of review: Review Package

A Review Package covers one feature or small business process. Its positive minimum is a declared bounded scope, at least one identifiable supplied basis element, at least one associated recognizable case under explicit ROLE-03 accountability with an eligible human-authored or human-controlled AI-assisted origin, and source provenance.

Unadopted generated testware, other origin and unknown origin remain visible but do not satisfy that positive minimum by themselves. TDG cannot infer or upgrade origin or accountability from writing style. A supplied experience-based rationale may support a case without a direct formal-requirement link; TDG cannot invent that rationale or present it as documented requirement coverage.

Diagrams, contextual labels, existing trace links and additional evidence are optional unless a particular assessment requires them. Their absence may limit that assessment without invalidating the whole package. Humans control scope; TDG may report missing or inconsistent material. Exact minimum, preservation and version rules are in [RA-03][ra03] and [RA-09][ra09].

## 8. MVP scope

### 8.1 Supported test-design scope

System-level, functional, black-box test cases for one feature or small process, supported by deliberately supplied evidence and attributable human accountability. Experience-based cases may receive generally applicable review, but detailed error-guessing, exploratory or checklist-technique assessment is outside this MVP.

### 8.2 Supported black-box test techniques

Equivalence Partitioning, Boundary Value Analysis, Decision Table Testing and State Transition Testing. Assess applicability and demonstrated coverage. An absent technique label is not itself a defect, and equivalent coverage without a named technique must not be penalized.

### 8.3 Additional review dimensions

Review may address traceability, clear preconditions, observable expected results, documented negative/alternative behavior and risks, untested business rules, defects in the supplied basis, and mismatch between scope and cases.

### 8.4 Technique-assessment outcomes

Distinguish supported coverage, demonstrable gaps, lack of applicability evidence, explicit non-applicability and inability to assess. A technique not indicated by this package is not universally inapplicable. Stronger conclusions need explicit, versioned, reviewable criteria. The definitive vocabulary and rules are maintained in [RA-06][ra06]; the original Charter labels were conceptual.

## 9. Scope qualification

Qualify scope before substantive review. Unsupported levels, types, internal-structure bases, representations, mixed cases and insufficient or conflicting evidence need explicit treatment, including an undetermined result where appropriate. An LLM's ability to answer does not establish supported scope.

Keep test level, type, design basis and execution mode separate. Component, integration, automated and white-box tests are not synonyms. Describe external behavior, internal structure or their mixture instead of using “gray-box” as a definitive verdict. Detailed criteria are in [RA-04][ra04].

## 10. Findings, suggestions, and authority

How an item was produced and what a human decided about it are separate facts. Neither deterministic nor LLM-assisted derivation can assign its own acceptance. New findings start pending human disposition; the definitive result and decision model is in [RA-05][ra05].

### 10.1 Deterministic finding

A reproducible finding based on confirmed structured rules and an identified control. The same normalized input and rule configuration must yield the same result. Retain traceability to the input, basis, mappings, rules and control versions. Reproducibility does not prove those premises correct or imply human acceptance. Very high precision is the intended quality objective.

### 10.2 LLM-assisted review suggestion

A probabilistic observation requiring human judgment. Identify supporting sources, distinguish facts from inference, expose uncertainty and allow rejection. It cannot silently edit testware. An unsupported model statement cannot become a deterministic finding or an accepted item merely because the model produced it.

### 10.3 Insufficient or conflicting evidence

Withhold or limit conclusions when evidence is missing, contradictory or outside the supported boundary. Report the reason. The definitive processing, assessment, availability and disposition vocabulary is maintained in [RA-05][ra05], replacing the Charter's early conceptual status list.

### 10.4 Prohibited overall claims

Do not claim ISTQB compliance or certification, test-suite completeness, correct testing of all requirements, approved test cases or adequate product quality from an absence of findings. Individual checks may pass. Overall statements must remain bounded to the assessed scope and supplied evidence.

### 10.5 Local review record

Retain package and case identities/names, findings, derivation, dispositions, evidence references and behavior-affecting assessment, rule, control, prompt and model versions in organization-controlled local storage. Persistence must respect protection and retention policy, without implying indefinite retention. Detailed records and storage behavior are in [RA-05][ra05], [RA-08][ra08] and [SAD-04][sad04].

## 11. Deliberately excluded from the MVP

- Automatic generation of complete suites or autonomous rewriting of source test cases.
- Direct Jira/Xray/Zephyr modification, automated status changes or publication without explicit human approval.
- Official ISTQB conformity decisions, completeness certification or mandatory use of every technique.
- Invented business rules or autonomous discovery outside the supplied package.
- Review of AI/LLM-system test cases, white-box coverage, or component, integration, acceptance, non-functional or executable automation artifacts as supported targets.
- External-model use for confidential documentation.

Out-of-scope artifacts remain useful negative inputs for classification and abstention tests.

## 12. Input and integration strategy

### 12.1 Canonical format

A vendor-independent JSON Review Package. The schema and document contracts are defined in [RA-09][ra09].

### 12.2 MVP import

Local JSON and a defined CSV test-case profile, with explicit mapping for supported source layouts. Preserve assessment-relevant unknown, malformed or unmapped content according to the capture rules; never silently discard its meaning.

### 12.3 Deferred integrations

Direct Jira/Xray/Zephyr integration waits until core review value is demonstrated. Any later integration should begin read-only, use least privilege and remain an adapter to the vendor-independent model. Write-back and autonomous editing remain outside MVP.

## 13. Confidentiality and trust boundary

Confidential documentation and testware must stay within an approved organization-controlled trust boundary. Detailed protection requirements are maintained in [RA-08][ra08].

### 13.1 Laboratory profile

Public or synthetic material only, for development, benchmarking, qualification and demonstrations. Local and external models may be compared; confidential enterprise testware is excluded.

### 13.2 Sealed execution profile

Local inference and organization-controlled processing/storage, with no external model calls, cloud fallback, unapproved telemetry or unapproved transfer of documents, prompts, intermediate data, findings or logs. Import/export must be deliberate and auditable; loss of the approved processing path must fail closed.

Deployment and network controls must enforce this boundary. Prompts or UI settings alone are insufficient. The confidentiality measure is zero bytes of protected package content transmitted outside the approved boundary.

### 13.3 Mandatory precondition for confidential-data use

Before confidential pilot or validation work, approve the protected-data classification, trust-boundary diagram, permitted machines/processes/services/storage/endpoints, complete input-to-export data flows, threat model and testable controls. Cover authentication, authorization, encryption, logs, temporary files, backups, retention, deletion, model services, telemetry and export.

The necessary artifacts must exist and controls must be verified before protected data enters TDG. Public/synthetic work can proceed within its authorization. Zero-egress verification needs that explicit classification and boundary as its test basis.

## 14. ISTQB-informed reference baseline

The project is independent of ISTQB. The reference editions selected at concept stage are CTFL v4.0.1 for testing methods and terminology, Testing with Generative AI v1.1 for responsible LLM use, and AI Testing v2.0 for evaluating TDG's probabilistic component. CT-AI does not expand the MVP into reviewing tests of AI systems. Preserve attribution and make no affiliation, accreditation, endorsement or certification claim.

## 15. Reference data and validation domains

### 15.1 First reference process

A synthetic customer-creation process, divided into small explicit rules. Candidate examples include age, customer type, country/documents, consents, duplicates, roles/permissions and status transitions.

### 15.2 Later validation campaigns

Public or synthetic telecom, e-commerce, banking and insurance examples may test generalizability. These are evaluation domains, not new product features. Do not reconstruct or disclose proprietary enterprise rules for them.

## 16. Evaluation and success measurement

### 16.1 Evaluation principle

Judge results against reviewable evidence. Agreement with another LLM, including a strong external model, is not sufficient ground truth. Detailed evaluation rules are maintained in [RA-10][ra10].

### 16.2 Evaluation corpus and dataset separation

Keep development data for tuning, separate qualification data for role permission, and held-out acceptance data unrevealed until the applicable acceptance execution. Report insufficient partition size and weaken claims accordingly. Adaptation after seeing acceptance results requires versioned reevaluation and fresh held-out evidence for a new unbiased claim.

Include clean controls, controlled mutations, naturally authored imperfect cases where feasible, incomplete/conflicting bases and later held-out domains. Identify whether each expected finding is mutation-grounded or human-adjudicated.

### 16.3 Reference packages and mutation ledger

Record the supplied basis, human-reviewed reference design, expected technique applicability, assessability limits and expected findings or mutations. Examples include missing boundaries, invalid partitions, decision rules or forbidden transitions; incorrect expected results; damaged traceability; unsupported behavior; and ambiguous, conflicting or incomplete basis material.

### 16.4 Human adjudication protocol

Define responsible reviewers and competence assumptions, criteria, retained evidence, dispositions and disagreement resolution. Preserve decisions and rationale with the dataset version. External LLMs may support challenges or comparisons on public/synthetic data, but cannot be the sole/final oracle or approve their own output or qualification.

### 16.5 Compared variants

Where feasible compare deterministic-only, qualified local-LLM-only, hybrid, strong external-model analysis of public/synthetic data, unaided human review and TDG-assisted human review.

### 16.6 Success metrics

Measure known-gap recall, finding precision, unsupported findings, false no-finding results, correct abstention, evidence traceability, human dispositions, reviewer time/effort, repeated-run consistency, deterministic reproducibility and confidentiality/egress violations against the approved boundary. Report by partition and material package category; development performance is not held-out acceptance performance.

### 16.7 Threshold policy

Propose numeric thresholds after initial baseline measurement and approve them before formal acceptance testing. Do not trade evidence or confidentiality invariants for higher average model scores. Product value requires measurable benefit over simpler baselines without unacceptable false positives or review burden.

## 17. Model qualification principle

Qualify identified models/configurations for bounded roles on separate public/synthetic qualification data. Roles may include candidate-rule extraction, case-to-basis mapping, applicability suggestions, semantic inconsistency detection or explaining deterministic findings. Exact permitted tasks belong in [RA-07][ra07]. Permission for one role does not grant all others; deterministic-only operation must remain possible when a model fails qualification.

Record model identity, configuration, permitted roles and evidence. Behavior-affecting changes to weights, digest, quantization, prompt, inference settings or runtime require impact analysis and affected-role requalification. A moving `latest` alias cannot silently replace the qualified artifact. Models cannot approve their qualification, and tuning on acceptance results invalidates a claim that those results remain unbiased for the adapted candidate.

## 18. Feasibility assessment

These are concept-stage conclusions, not evidence of present implementation or validated usefulness.

### 18.1 Technical feasibility

**Conditionally feasible.** Structured deterministic checks, local import and provenance are plausible. Resource-constrained local-LLM adequacy is unproven; use bounded tasks and preserve deterministic-only operation.

### 18.2 Operational feasibility

**Subject to usability validation.** Pre-review fits tester work only if inspecting its output is useful and less burdensome than the corresponding unaided analysis. Validate with representative users or disclose the limitation of a quasi-UAT exercise.

### 18.3 Security feasibility

**Conditionally feasible.** Local processing reduces exposure, but sealed readiness depends on threat modeling and verified network, storage, logging, temporary-file and retention controls.

### 18.4 Measurement feasibility

**Feasible with material effort.** Human-adjudicated examples and verified mutations can support evaluation. Their preparation is planned product work, not incidental test data.

### 18.5 Legal and naming feasibility

**Feasible with explicit boundaries.** Use independent branding, preserve source/version attribution and avoid official ISTQB affiliation or certification claims.

### 18.6 Delivery and resource feasibility

**Not established at concept stage.** Capacity, competing priorities, benchmark effort and an estimable backlog were required before implementation authorization. No delivery commitment follows from concept approval. Current estimates and capacity are described in the work plan and [README.md](../../README.md).

### 18.7 Overall feasibility conclusion

**Conditionally feasible at concept level.** This supported entry to Requirements Analysis, not a delivery guarantee. Later work requires the applicable authorization and evidence.

## 19. Principal risks and responses

| ID | Risk | Initial significance | Response |
| --- | --- | --- | --- |
| R-01 | Unsupported model rules or findings | High | Evidence, explicit inference, human review and abstention |
| R-02 | Local model inadequate on available hardware | High | Bounded tasks, qualification by role and deterministic fallback |
| R-03 | Mechanically enforcing inapplicable techniques | High | Establish applicability; missing labels alone are not defects |
| R-04 | A defective basis is blamed on the tester | High | Separate basis issues and explain limited or impossible assessment |
| R-05 | Confidential data leaves the approved environment | Critical | Verified sealed controls, no cloud fallback and fail-closed operation |
| R-06 | Circular model-as-judge evaluation | High | Separate datasets, human adjudication and verified mutations |
| R-07 | False positives increase effort and erode trust | High | Precision and reviewer-effort measures; distinguish impact from confidence |
| R-08 | Product scope or documentation expands and delays useful evaluation | High | Explicit non-goals and scope decisions; maintain rules in one place, consolidate repetitions and review documentation cost and evaluation delay |
| R-09 | Vendor formats shape the core model | Medium | Vendor-independent model and deferred adapters |
| R-10 | Wording implies official ISTQB approval | High | Independent branding, clear attribution and prohibited-claim checks |
| R-11 | Import loses meaningful content | High | Explicit mapping, validation, provenance and visible limitations |
| R-12 | A simple benchmark overstates generalizability | High | Controls, mutations, imperfect/incomplete inputs and held-out domains |
| R-13 | Deterministic output is treated as true or human-approved | High | Separate derivation/disposition, traceable premises and human decisions |

R-08 now states the documentation-growth concern already carried by `SR-RA03-OBS-002` and observed in the October audit; see [LEARNINGS.md](../../LEARNINGS.md). The original scope examples include generation, external discovery, all techniques and all test levels. Risk ownership, scoring, review cadence and residual-risk decisions remain matters for planning and the appropriate human authority.

## 20. SDLC and testing approach

The accepted lifecycle covers Concept & Feasibility, Requirements Analysis, Solution and Architecture Design, bounded implementation increments, formal product validation, controlled pilot/deployment, and maintenance. It permits feedback and correction, with explicit authorization for the relevant phase or scope.

Testing starts with static review and early planning, analysis and design. Formal STLC work includes planning/control, analysis, design, test implementation, execution/model evaluation and completion/reporting. Applicable layers include unit, schema/contract, import, integration, model qualification, metamorphic/repeatability, end-to-end, security/privacy, negative classification and human acceptance checks.

## 21. Concept-phase static review

`SR-CHARTER-001` reviewed v0.1. Version 0.2 incorporated its eight accepted dispositions; v0.3 recorded the concept-phase GO. The review covered clarity, completeness, consistency, testability, feasibility, protection, traceability, reference alignment, scope and premature assumptions.

The focused RA-03 review subsequently accepted the two v0.4 amendments, and [PG-RA03-001][baseline] designated the replacement baseline. These reviews and their original evidence remain historical records. Review findings need identifiable evidence, disposition and resolution; review lifecycle labels are separate from TDG product dispositions. Disclose the absence of independent review where applicable.

## 22. Phase exit criteria

Concept exit required approval of the problem/hypothesis, users/use case, scope/non-goals, package boundary, authority/abstention, prohibited claims, protection profiles, evaluation strategy/metrics and principal risks. Static review had to be complete, with no unresolved Critical/High finding and Medium findings resolved or explicitly accepted/deferred, followed by the Owner's `GO`, `REVISE` or `NO-GO` decision.

The phase closed with GO on 2026-09-08. The later v0.4 amendment review and baseline designation were completed without reopening that phase.

## 23. Items deliberately deferred to later phases

Concept-stage allocations now lead to these sources; an allocation is not proof of implemented or verified capability:

| Topic | Governing detail or remaining decision |
| --- | --- |
| Functional/non-functional requirements, package minimum, input representations, findings and authority | [Accepted requirements baseline][requirements], including RA-01 through RA-09 |
| UI, deployment form, stack, architecture, storage engine/schema, operational entry points and implementation increments | [SAD-04][sad04] and its linked design records |
| Model selection/quantization, prompts/context, identity, change detection and requalification | [RA-07][ra07] and [SAD-03][sad03] |
| Dataset size/sampling, adjudication, qualification and acceptance thresholds | [RA-10][ra10] and the later approved evaluation protocol |
| Threat model, protection, retention, deletion, audit and backup | [RA-08][ra08] and [SAD-03][sad03] |
| CSV profiles, source mappings and future read-only integrations | [RA-09][ra09]; external integrations remain deferred |
| Capacity, competing priorities, schedule, effort and release planning | Current work planning; the implementation sequence must be reconsidered after cleanup before development resumes |

## 24. Decision register

D-001–028 originated in concept discovery; D-029–030 record the accepted 2026-09-12 clarifications. Their accepted content is summarized below. Phase authorization has its own date and scope in Section 25.

| ID | Accepted decision |
| --- | --- |
| D-001 | Use the working name Test Design Gatekeeper. |
| D-002 | Describe it as evidence-grounded and ISTQB-informed, without conformity or certification claims. |
| D-003 | Keep the Project Owner and tester as final decision authorities. |
| D-004 | Use test-case pre-review as the primary workflow; origin eligibility follows D-029. |
| D-005 | Limit supported design to system-level functional black-box cases. |
| D-006 | Begin with EP, BVA, decision tables and state transitions. |
| D-007 | Evaluate coverage/applicability, not technique labels or presumed author intent. |
| D-008 | Use a bounded package controlled by the tester. |
| D-009 | Do not broaden scope silently or invent rules. |
| D-010 | Keep derivation separate from human disposition; deterministic findings are not automatically accepted. |
| D-011 | Require evidence, uncertainty, abstention and human review for model contributions. |
| D-012 | Prohibit overall ISTQB compliance or completeness verdicts. |
| D-013 | Use out-of-scope artifacts for negative tests without expanding support. |
| D-014 | Defer review of AI/LLM-system tests. |
| D-015 | Use CT-GenAI to inform LLM use and CT-AI to inform testing TDG's AI component. |
| D-016 | Use public/synthetic data for laboratory benchmarks and external-model comparisons. |
| D-017 | Require a sealed local profile for confidential material. |
| D-018 | Use canonical JSON with local JSON/CSV import. |
| D-019 | Defer vendor integrations; start any later integration read-only. |
| D-020 | Start with synthetic customer creation, then diversify evaluation domains. |
| D-021 | Separate development, qualification and held-out acceptance, with human adjudication. |
| D-022 | Keep applicability conclusions scoped; require explicit criteria for strong non-applicability. |
| D-023 | Block confidential use until its trust boundary and controls are defined and verified. |
| D-024 | Record delivery/resource feasibility as not yet assessed until an estimable backlog and capacity view exist. |
| D-025 | Permit knowledgeable supporting users while keeping the tester-centered, accountable workflow. |
| D-026 | Expose insufficient input; humans provide missing context and repair cases. |
| D-027 | Keep local, version-aware history; assign detailed storage decisions downstream. |
| D-028 | Treat behavior-affecting model/configuration changes as requalification triggers. |
| D-029 | Positive origin eligibility needs explicit ROLE-03 accountability for human-authored or controlled AI-assisted cases; no inferred authorship or automatic adoption of generated content. |
| D-030 | Allow explicitly supplied risk, defect, heuristic or experience-based evidence without adding experience-based technique assessment. |

## 25. Phase decision

| Decision | Recorded outcome |
| --- | --- |
| Concept static review and correction verification | Complete; findings resolved or explicitly dispositioned |
| Project Owner GO to Requirements Analysis | Granted, 2026-09-08 |
| v0.4 amendment review and replacement baseline | Complete; baseline designated 2026-09-15 in [PG-RA03-001][baseline] |

### Decision record

On 2026-09-08 the Owner stated: “GO — zezwalam projektowi Test Design Gatekeeper przejść do fazy Requirements Analysis.” That decision authorized Requirements Analysis only. Later architecture, implementation, deployment or protected-data permissions require their own applicable decisions. The original review's downstream obligations remained allocated for later work.

### Controlled amendment state

`CR-RA03-001/002`, based on the 2026-09-12 `OD-RA03-004/003` decisions, were reviewed and accepted. The Owner designated Charter v0.4 on 2026-09-15. The September 8 phase decision retains its original scope and date. [PG-RA03-001][baseline] records the completed designation, while [Git history][original] preserves the exact earlier wording.

## References

- [ISTQB Certified Tester Foundation Level Syllabus v4.0.1](https://istqb.org/?download_id=3345&sdm_process_download=1)
- [ISTQB Certified Tester — Testing with Generative AI](https://istqb.org/certifications/gen-ai/)
- [ISTQB Certified Tester AI Testing v2.0](https://istqb.org/certifications/certified-tester-ai-testing-ct-ai/)
- [Jira Cloud REST API v3](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/)
- [Atlassian guidance: export Jira Cloud work items to CSV](https://support.atlassian.com/jira/kb/how-to-export-issues-from-jira-cloud-in-csv-format/)
- [Xray Test Case Importer examples](https://github.com/Xray-App/tutorial-test-case-importer)

[baseline]: ../reviews/test-design-gatekeeper-ra-03-gate-record-v0.2.md
[original]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/19948de4cb79b49904980ba335692752f291d3dd/docs/governance/test-design-gatekeeper-project-charter-v0.4.md
[ra01]: ../requirements-analysis/test-design-gatekeeper-ra-01-stakeholders-actors-authority-v0.3.md
[ra03]: ../requirements-analysis/ra-10/test-design-gatekeeper-ra-03-review-package-content-provenance-validation-v0.4.md
[ra04]: ../requirements-analysis/test-design-gatekeeper-ra-04-scope-qualification-classification-boundaries-v0.2.md
[ra05]: ../requirements-analysis/ra-05/test-design-gatekeeper-ra-05-findings-dispositions-persistence-v0.2.md
[ra06]: ../requirements-analysis/ra-06/test-design-gatekeeper-ra-06-technique-applicability-design-coverage-v0.2.md
[ra07]: ../requirements-analysis/ra-07/test-design-gatekeeper-ra-07-llm-roles-qualification-v0.2.md
[ra08]: ../requirements-analysis/ra-08/test-design-gatekeeper-ra-08-confidentiality-security-privacy-v0.2.md
[ra09]: ../requirements-analysis/ra-09/test-design-gatekeeper-ra-09-data-representations-import-export-contracts-v0.2.md
[ra10]: ../requirements-analysis/ra-10/test-design-gatekeeper-ra-10-evaluation-acceptance-v0.2.md
[requirements]: ../requirements-analysis/ra-10/test-design-gatekeeper-requirements-analysis-readiness-v0.2.md
[sad03]: ../solution-design/test-design-gatekeeper-sad-03-model-protection-v0.3.md
[sad04]: ../solution-design/test-design-gatekeeper-sad-04-integrated-review-increment-plan-v0.2.md
