# Test Design Gatekeeper

## Project Charter / Concept & Feasibility

| Field | Value |
| --- | --- |
| Document version | 0.4 |
| Document date | 2026-09-12 |
| SDLC phase | Initiation — Concept & Feasibility |
| Status | CONTROLLED AMENDMENT CANDIDATE — v0.3 phase `GO` remains effective; focused delta review required |
| Decision authority | Project Owner |
| Amendment authority | `OD-RA03-003` and `OD-RA03-004` accepted by Project Owner on 2026-09-12 |
| Working product name | Test Design Gatekeeper |
| Product descriptor | An evidence-grounded, ISTQB-informed test case review assistant |

> **Document status notice:** Charter v0.3 remains the approved baseline that authorized Requirements Analysis through the Project Owner's `GO` on 2026-09-08. This v0.4 candidate applies only controlled clarifications accepted during RA-03: origin eligibility follows attributable human accountability rather than purity of authorship, and explicitly supplied experience-based rationale may form part of the test basis without adding experience-based technique assessment to the MVP. The amendment requires focused delta review before replacing v0.3. It does not alter the phase authorization or authorize solution design, implementation, repository creation, or confidential-data use.

### v0.4 controlled amendment summary

| Change | Source decision | Effect | Scope guard |
| --- | --- | --- | --- |
| `CR-RA03-001` | `OD-RA03-004` | Recognize human-authored and human-controlled AI-assisted testware when an identified human accepts ROLE-03 accountability | No TDG test generation, authorship inference, or AI/LLM target-domain review |
| `CR-RA03-002` | `OD-RA03-003` clarification | Recognize an explicitly supplied risk, prior defect, heuristic, or experience-based rationale as possible test-basis evidence | No fifth technique is added to the four-technique MVP |

## 1. Purpose of this Charter

This Charter defines the problem, product hypothesis, intended users, MVP boundaries, evidence and authority model, confidentiality constraints, feasibility assumptions, success measures, principal risks, and phase-exit criteria for Test Design Gatekeeper.

Its purpose is to determine whether the proposed product is sufficiently valuable, bounded, secure, measurable, and technically plausible to justify entering the Requirements Analysis phase. It intentionally does not define detailed functional requirements, user-interface design, implementation technology, or repository structure.

## 2. Problem statement

Testers preparing test cases from user stories, functional requirements, business rules, and project documentation may unintentionally simplify the test basis during test analysis and design. Common symptoms include:

- concentrating on straightforward happy paths;
- representing a business rule with only one example;
- omitting invalid equivalence partitions and boundary values;
- missing relevant combinations of conditions;
- overlooking alternative, negative, or forbidden state transitions;
- losing traceability between requirements, risks, test conditions, and test cases;
- using vague preconditions or expected results;
- treating missing or ambiguous requirements as if they were complete.

The problem is not assumed to result solely from lack of knowledge. Time pressure, routine, fragmented documentation, complexity, cognitive bias, and insufficient review capacity may all contribute.

Existing powerful LLMs can produce convincing reviews, but convincing language is not evidence of correctness. Smaller local models may additionally hallucinate, miss cross-document relationships, or provide generic advice. A useful solution therefore cannot rely on unrestricted LLM judgment.

## 3. Product vision

Test Design Gatekeeper will help a tester review test cases under attributable human accountability, whether human-authored or human-controlled with AI assistance, before peer review or formal approval. It will relate the cases to a bounded test basis, identify demonstrable coverage gaps, indicate test techniques that may address those gaps, distinguish deterministic findings from probabilistic suggestions, and abstain when the evidence is insufficient.

The product will support and strengthen human test analysis and design. It will not replace the tester, certify test completeness, or act as an official ISTQB compliance authority.

## 4. Product hypothesis

> A review combining deterministic controls, bounded local-LLM analysis, explicit evidence, and human decision-making will identify more material test-design gaps than an unaided review or either technical component alone, without generating an unacceptable review burden and without disclosing confidential testware outside the approved environment.

This is a hypothesis to be tested. It is not an assumption that the hybrid solution, any particular LLM, or the project as a whole will succeed.

## 5. Intended users and stakeholders

### 5.1 Primary user

A tester or test analyst who prepares or reviews functional test cases from documented requirements and business rules.

### 5.2 Secondary user

A test lead or reviewer who needs an evidence-based view of identified gaps, unresolved questions, and review decisions.

Additional eligible supporting users may include a business analyst, test coordinator, domain subject-matter expert, or another person with relevant project, domain, or test-method knowledge. They may use the Gatekeeper to support analysis or review, but not as a substitute for accountable human judgment. The primary MVP workflow remains centered on functional test cases deliberately controlled by an identified human acting with testware accountability.

### 5.3 Decision authority

The human user retains authority over:

- the declared review scope;
- the supplied test basis;
- confirmation or correction of extracted rules;
- acceptance or rejection of suggestions;
- modification of test cases;
- readiness of testware for further review or use.

The Gatekeeper does not become the owner or approver of the testware.

## 6. Primary use case

The MVP supports a pre-review performed after a tester has drafted test cases but before the cases are submitted for peer review or test-lead approval.

At a high level:

1. The tester defines a bounded review scope.
2. The tester supplies the relevant test basis and associated test cases.
3. The Gatekeeper qualifies whether the submitted material is in scope and sufficiently assessable.
4. The Gatekeeper relates test-basis elements, risks, and test cases.
5. Deterministic controls assess coverage items that can be calculated from confirmed structured rules.
6. A qualified local LLM may produce evidence-grounded semantic suggestions.
7. The tester accepts, rejects, corrects, or defers individual findings and suggestions.
8. The tester, not the Gatekeeper, edits the test cases.
9. The tester may submit a revised package for another review.

The MVP is an assistant before a human review gate. It is not itself a release-blocking organizational gate.

Insufficient input is an explicit negative path to be specified and tested. When the submitted material is too limited, contradictory, or mismatched for a supported assessment, the Gatekeeper must identify the limitation and narrow or stop the review. The human user supplies or corrects the missing context and remains solely responsible for repairing test cases. The Gatekeeper must not compensate by searching documentation outside the submitted Review Package or by inventing rules.

## 7. Unit of review: Review Package

The primary unit of work is a bounded **Review Package** covering one feature or a small business process.

A minimally admissible Review Package contains:

- a declared bounded review scope;
- at least one identifiable test-basis element, such as a user story, requirement, acceptance criterion, business rule, risk, prior defect, or attributable experience-based rationale;
- at least one associated recognizable test case declared human-authored or human-controlled with AI assistance and governed by an identified human accepting ROLE-03 accountability;
- enough provenance to identify the supplied sources.

Generated testware without accountable human adoption, other origin, and unknown origin do not satisfy the positive minimum by themselves. TDG preserves such input visibly but does not infer or upgrade origin or accountability from writing style. A human-supplied experience-based rationale may support a case without a direct link to one formal requirement; TDG must not invent an unstated rationale or represent it as documented requirement coverage.

A Review Package may additionally contain:

- relevant diagrams, matrices, or specification excerpts;
- contextual information such as test level, test type, user role, business objective, and identified risks;
- pre-existing traceability links;
- other evidence required by a particular assessment.

The absence of an optional item does not by itself invalidate the package. It may, however, make a particular technique or review dimension only partially assessable or unassessable. Detailed conditional input requirements belong to Requirements Analysis.

The tester controls the package boundary and supplied test basis. The Gatekeeper does not search an entire project repository, silently broaden the scope, or invent missing business rules. It may identify that the package appears incomplete, inconsistent, or mismatched.

## 8. MVP scope

### 8.1 Supported test-design scope

The MVP reviews:

- test cases under attributable human accountability, including human-authored and human-controlled AI-assisted testware;
- functional testing;
- system-level testing;
- black-box test design;
- one bounded feature or small business process per Review Package;
- test cases grounded in an explicitly supplied test basis, including documented requirements, risks, prior defects, or attributable experience-based rationale.

The product may preserve and perform generally applicable review of an experience-based case, but the MVP does not add detailed assessment of experience-based techniques such as error guessing, exploratory testing, or checklist-based testing to the four techniques listed below.

### 8.2 Supported black-box test techniques

The initial technique set is:

- Equivalence Partitioning (EP);
- Boundary Value Analysis (BVA);
- Decision Table Testing;
- State Transition Testing.

The Gatekeeper evaluates coverage and the applicability of techniques, not whether the author explicitly named a technique or consciously intended to use it.

The absence of a named technique is not a defect by itself. A finding must be based on a demonstrable coverage gap or assessability problem. If equivalent coverage exists without an explicit technique label or artifact, the Gatekeeper must not penalize the test suite.

### 8.3 Additional review dimensions

The MVP may assess:

- traceability between test-basis elements and test cases;
- presence and clarity of preconditions;
- observability and specificity of expected results;
- coverage of documented negative and alternative behavior;
- coverage of documented risks;
- untested business rules;
- contradictions, ambiguity, or missing information in the test basis;
- mismatch between the declared scope and supplied test cases.

### 8.4 Technique-assessment outcomes

Technique-related assessment may use outcomes such as:

- `COVERAGE_CONSISTENT_WITH_TECHNIQUE`;
- `TECHNIQUE_APPLICABLE_WITH_GAPS`;
- `COVERAGE_PRESENT_WITHOUT_EXPLICIT_TECHNIQUE`;
- `TECHNIQUE_NOT_INDICATED_WITHIN_SCOPE`;
- `INSUFFICIENT_APPLICABILITY_EVIDENCE`;
- `TECHNIQUE_NOT_APPLICABLE_BY_EXPLICIT_CRITERIA`;
- `TECHNIQUE_UNASSESSABLE`.

`TECHNIQUE_NOT_INDICATED_WITHIN_SCOPE` does not assert universal inapplicability; it states only that the bounded supplied evidence does not indicate the technique. A stronger non-applicability conclusion is reserved for explicit, versioned, and reviewable criteria. These names are conceptual at Charter level. The definitive domain model belongs to Requirements Analysis and Solution Design.

## 9. Scope qualification

Scope qualification occurs before substantive review. The Gatekeeper must not provide a seemingly authoritative review of unsupported material merely because an LLM can generate a response.

Relevant qualification outcomes include:

- in-scope system-level functional black-box test cases;
- out-of-scope test level;
- out-of-scope test type;
- white-box or internal-structure test basis outside MVP scope;
- mixed or unclear basis requiring human review;
- unsupported artifact format;
- mismatch between declared process and supplied test cases;
- insufficient or contradictory test basis;
- undetermined classification.

Component tests, integration tests, automated tests, and white-box tests are not treated as synonyms. Test level, test type, test technique, and execution mode remain distinct classification axes.

The informal industry term “gray-box” will not be used as a definitive MVP verdict. Where relevant, the Gatekeeper should describe the actual basis used, such as external behavior, internal structure, or a mixture of both.

## 10. Findings, suggestions, and authority

Every reported item has two independent dimensions:

- derivation: `DETERMINISTIC` or `LLM_ASSISTED`;
- human disposition: `PENDING`, `ACCEPTED`, `REJECTED`, or `DEFERRED`.

Derivation records how the item was produced. Disposition records the human review decision. Neither derivation type assigns its own human disposition, and every new item begins as `PENDING`.

### 10.1 Deterministic finding

`DETERMINISTIC_FINDING` represents a result derived from confirmed structured rules and a deterministic control. It must include reproducible evidence and must produce the same result for the same normalized input and rule configuration.

Deterministic reproducibility does not prove that the source, import mapping, normalized rule, rule precedence, or control is correct. It also does not mean that a human has accepted the finding. A deterministic finding must be traceable to the normalized input, source test-basis element, relevant rule or mapping version, and deterministic-control version.

The product should optimize this class for very high precision.

### 10.2 LLM-assisted review suggestion

`REVIEW_SUGGESTION` represents a probabilistic semantic observation with derivation `LLM_ASSISTED` and requires human judgment. It must:

- identify the supporting source;
- distinguish supplied facts from inference;
- state uncertainty;
- remain reviewable and rejectable;
- never silently modify the testware.

An LLM statement without evidence cannot be promoted to a deterministic finding or assigned disposition `ACCEPTED`. Only a human reviewer may assign the final disposition.

### 10.3 Insufficient or conflicting evidence

The product must be able to abstain. Conceptual assessment statuses include:

- `FINDINGS_IDENTIFIED`;
- `REVIEW_REQUIRED`;
- `NO_SUPPORTED_FINDINGS`;
- `PARTIALLY_ASSESSABLE`;
- `UNGRADABLE`;
- `CONFLICTING_BASIS`;
- `SCOPE_MISMATCH`.

The definitive status model will be specified and tested in later phases.

### 10.4 Prohibited overall claims

The product must not claim that:

- a test suite is “ISTQB compliant” or “ISTQB certified”;
- a test suite is complete;
- all requirements have been correctly tested;
- test cases have been approved;
- the absence of detected findings proves adequate product quality.

An individual deterministic check may pass. The overall product message must instead remain scoped, for example:

> No supported findings were detected within the evaluated scope. This result does not establish test-suite completeness or conformity with ISTQB.

### 10.5 Local review record

The MVP requires organization-controlled local persistence of Review Package identifiers, test-case identifiers and names, findings and gaps, derivation type, human disposition, evidence references, and the versions of assessments, rules, controls, prompts, and models that materially affected a result.

A local database is the working implementation direction, but the database engine, schema, retention model, backup behavior, and access controls belong to Requirements Analysis and Solution Design. Local persistence must remain consistent with the sealed-profile trust boundary and must not imply silent or indefinite retention.

## 11. Deliberately excluded from the MVP

The following are outside the MVP:

- automatic generation of complete test suites;
- autonomous rewriting of existing test steps;
- direct modification of Jira, Xray, or Zephyr records;
- publication of changes without explicit human approval;
- an official ISTQB conformity or certification decision;
- mandatory use of every technique for every requirement;
- invention of missing business rules;
- autonomous discovery across an entire documentation repository;
- review of test cases designed for AI or LLM systems as a separate application domain;
- validation of white-box coverage;
- review of component, integration, acceptance, non-functional, or executable automated-test artifacts as supported MVP targets;
- use of external models for confidential documentation.

Out-of-scope artifacts will still be used as negative test inputs to verify correct classification and abstention.

## 12. Input and integration strategy

### 12.1 Canonical format

The vendor-independent canonical representation of a Review Package will be JSON. The detailed schema is deferred to Requirements Analysis and Solution Design.

### 12.2 MVP import

The MVP will use local file import:

- a canonical Review Package JSON format;
- a defined CSV format for test cases;
- local normalization and explicit field mapping where a source export differs from the canonical model.

Import must not silently discard unknown, malformed, or unmapped fields that can affect an assessment.

### 12.3 Deferred integrations

Direct integration with Jira, Xray, and Zephyr is deferred until the core review value has been demonstrated. A future integration should begin as read-only, use least privilege, preserve the canonical internal model, and remain an adapter rather than a dependency of the review engine.

Direct write-back, automated status changes, and autonomous editing remain outside the MVP.

## 13. Confidentiality and trust boundary

Confidential project documentation and testware must remain inside an organization-controlled trust boundary.

Two conceptually separate operating profiles are planned:

### 13.1 Laboratory profile

- public or synthetic documentation only;
- local and external models may be compared;
- no confidential enterprise testware;
- suitable for benchmarking, model qualification, and public demonstrations.

### 13.2 Sealed execution profile

- local inference only;
- organization-controlled processing and storage;
- no external model calls;
- no cloud fallback;
- no unapproved telemetry;
- no unapproved outbound transfer of source documents, prompts, intermediate representations, findings, or logs;
- fail-closed behavior if the approved local processing path is unavailable;
- deliberate and auditable import and export.

The security boundary must be enforced technically by deployment and network controls, not only by a prompt or user-interface setting. Detailed authentication, authorization, encryption, retention, logging, backup, temporary-file, and deletion requirements are deferred to later phases and require a threat model.

For the sealed profile, the principal confidentiality measure is zero bytes of protected Review Package content transmitted outside the approved trust boundary.

### 13.3 Mandatory precondition for confidential-data use

Before any pilot or validation activity uses confidential data, the project must define and approve:

- asset and data classification, including the Review Package content considered protected;
- a trust-boundary diagram;
- an inventory of approved machines, processes, model services, storage locations, and network endpoints;
- data-flow analysis covering input, processing, logging, temporary storage, backup, and export;
- a threat model;
- testable controls for logs, temporary files, backups, model services, telemetry, and export paths.

Until these artifacts and controls exist and have been verified, confidential data must not enter the product. This condition does not block Requirements Analysis or laboratory work using public or synthetic data. The zero-egress invariant is testable only against the approved data classification and trust-boundary definition; those artifacts form part of its test basis.

## 14. ISTQB-informed reference baseline

The project is independent and is not affiliated with or endorsed by ISTQB.

The initial reference baseline is:

- ISTQB Certified Tester Foundation Level Syllabus v4.0.1 — terminology, test process, traceability, risk, static testing, and the selected black-box techniques;
- ISTQB Certified Tester — Testing with Generative AI Syllabus v1.1 — responsible use of LLMs in software testing, including evaluation, hallucination, bias, privacy, security, and LLM-powered solution considerations;
- ISTQB Certified Tester AI Testing Syllabus v2.0 — principles relevant to testing the Gatekeeper's probabilistic AI component, including non-determinism, oracle limitations, statistical evaluation, and testing of LLM-based systems.

CT-AI does not expand the MVP into reviewing tests written for AI systems. That application-domain capability is deliberately parked for a later product version.

Any future use of ISTQB material must preserve correct attribution and must not imply accreditation, endorsement, or certification.

## 15. Reference data and validation domains

### 15.1 First reference process

The first Review Package will be a synthetic customer-creation process in a conventional business system. It may include bounded rules concerning:

- age or date-of-birth validation;
- customer type;
- country and document requirements;
- required consents;
- duplicate detection;
- roles and permissions;
- customer status transitions.

The reference process will be divided into small, explicit rules rather than treated as an unrestricted end-to-end process.

### 15.2 Later validation campaigns

Later phases may add public or synthetic Review Packages from:

- telecommunications — services, subscriptions, prepaid, and billing;
- e-commerce — promotions and discount interactions;
- banking — consumer and mortgage lending;
- insurance — motor liability/comprehensive insurance and life insurance.

These domains are validation campaigns for generalizability, not additional core product features. No proprietary rules from real enterprise systems may be reconstructed or disclosed for these datasets.

## 16. Evaluation and success measurement

### 16.1 Evaluation principle

Success will be measured against known, reviewable evidence. Agreement with another LLM is not a sufficient oracle, and a powerful external model is not treated as ground truth.

### 16.2 Evaluation corpus and dataset separation

The evaluation corpus must be partitioned by purpose:

1. a visible development set used to create and tune prompts, deterministic rules, mappings, and review logic;
2. a separate qualification set used to decide which defined roles a model may perform;
3. a held-out acceptance set that is not used for prompt, rule, mapping, or model-role tuning and remains unrevealed until the applicable acceptance execution.

If the available corpus is too small to support three credible partitions, the limitation must be reported explicitly and any generalization or success claim must be weakened accordingly. A change made after inspecting held-out acceptance results requires versioned reevaluation and, for a new unbiased acceptance claim, new held-out evidence.

Across the partitions, the corpus will contain public or synthetic Review Packages representing:

- clean controls with no intentionally seeded gap;
- controlled mutant packages;
- naturally authored imperfect packages where feasible;
- incomplete or contradictory test bases;
- later held-out packages from different business domains.

Each expected finding must identify whether its oracle is mutation-grounded or based on human semantic adjudication.

### 16.3 Reference packages and mutation ledger

The evaluation dataset will contain public or synthetic Review Packages with:

- an explicitly documented test basis;
- a human-reviewed reference test design;
- expected applicable and non-applicable techniques;
- known assessability limitations;
- an adjudicated finding set or deterministic mutation ledger.

Controlled testware mutations may include:

- removal of a boundary value;
- removal of an invalid equivalence partition;
- removal of a decision-table rule;
- omission of a forbidden state transition;
- introduction of an incorrect expected result;
- loss of requirement traceability;
- addition of behavior unsupported by the test basis;
- deliberate ambiguity, contradiction, or incompleteness in the test basis.

### 16.4 Human adjudication protocol

Semantic reference decisions must follow a documented human-adjudication protocol. At minimum, it must define reviewer responsibility and competence assumptions, review criteria, the evidence to retain, permitted dispositions, and the method for resolving disagreement. Decisions and rationales must be preserved with the evaluated dataset version.

An external LLM may act as a comparator, source of challenge questions, or analysis aid on public or synthetic data. It must not be the sole or final oracle, and no LLM may approve its own output or qualification.

### 16.5 Compared variants

The benchmark should compare, where feasible:

1. deterministic controls only;
2. a qualified local LLM only;
3. the hybrid of deterministic controls and a qualified local LLM;
4. a strong external model on public or synthetic data only;
5. human review without the Gatekeeper;
6. human review assisted by the Gatekeeper.

### 16.6 Success metrics

The measurement set includes:

- recall of known or seeded gaps;
- precision of reported findings;
- unsupported-finding rate;
- false `NO_SUPPORTED_FINDINGS` rate;
- correct abstention and `UNGRADABLE` behavior;
- evidence traceability rate;
- human acceptance or rejection of suggestions;
- change in review time and reviewer effort;
- repeatability across repeated LLM runs;
- deterministic reproducibility;
- confidentiality and outbound-data-transfer violations measured against an approved data classification and trust boundary.

Results must be reported by dataset partition and relevant package category so that development performance is not presented as held-out acceptance performance.

### 16.7 Threshold policy

Numeric acceptance thresholds will not be invented in the Charter. They will be proposed after an initial baseline measurement and approved before formal acceptance testing. Safety invariants, including evidence requirements for deterministic findings and zero unapproved confidential-data egress, are not relaxed by model performance.

The project will be considered valuable only if the hybrid solution provides measurable benefit over simpler baselines without creating an unacceptable false-positive and review burden.

## 17. Model qualification principle

No LLM is assumed to be suitable solely because it is locally hosted, powerful, popular, or produces convincing prose.

A model must be qualified on the separate public or synthetic qualification set for each permitted role, such as:

- extracting candidate rules;
- mapping test cases to test-basis elements;
- proposing technique applicability;
- identifying semantic inconsistencies;
- explaining deterministic findings.

A model may be approved for some roles and rejected for others. Role permissions, model version, configuration, and qualification evidence must be versioned. Failure to qualify a local model must not disable deterministic-only operation. Models must not evaluate or approve their own qualification results. Held-out acceptance results must not be reused to tune a model or prompt while still being represented as unbiased acceptance evidence.

Model artifacts and their runtime configuration must be treated as changeable dependencies, not permanent capabilities. A change to model weights, artifact digest, quantization, prompt, inference configuration, or runtime that may affect behavior requires impact analysis and requalification for the affected roles. Silent substitution of a moving `latest` model for a previously qualified artifact is not acceptable.

## 18. Feasibility assessment

### 18.1 Technical feasibility

**Preliminary outcome: conditionally feasible.**

Deterministic checks over confirmed structured rules are technically conventional. A vendor-independent canonical model, local import, provenance, and reproducible findings are also feasible.

The adequacy of a resource-constrained local LLM is unproven. It requires qualification against bounded Review Packages. The MVP must therefore decompose tasks, preserve deterministic-only operation, and avoid depending on whole-project document comprehension.

### 18.2 Operational feasibility

**Preliminary outcome: feasible subject to usability validation.**

The pre-review workflow fits an existing tester activity and preserves human authority. Its value depends on findings being concise, evidence-grounded, and cheaper to review than performing the same analysis unaided. This must be validated with representative users or a documented quasi-UAT limitation.

### 18.3 Security feasibility

**Preliminary outcome: conditionally feasible.**

Local import and local inference reduce data exposure and avoid integration credentials in the MVP. A genuine sealed profile remains dependent on later threat modeling and technical verification of network, storage, logging, temporary-file, and retention controls.

### 18.4 Measurement feasibility

**Preliminary outcome: feasible with material effort.**

A mutation ledger and human-adjudicated public or synthetic benchmark can provide a defensible oracle. Creating high-quality reference packages and adjudications is likely to be one of the most labor-intensive parts of the project and must be planned as product work, not incidental test data preparation.

### 18.5 Legal and naming feasibility

**Preliminary outcome: feasible with explicit boundaries.**

The independent product name must not imply official ISTQB affiliation, conformity assessment, accreditation, endorsement, or certification. References must identify the applicable syllabus and version and preserve attribution.

### 18.6 Delivery and resource feasibility

**Preliminary outcome: `NOT_YET_ASSESSED`.**

The Charter does not establish available capacity, delivery schedule, opportunity cost, or the effort needed to construct and adjudicate a credible benchmark. No release date or effort commitment may be made until Requirements Analysis produces an estimable MVP backlog. Available project capacity and major competing priorities must be recorded before implementation authorization.

### 18.7 Overall feasibility conclusion

**Candidate conclusion: `CONDITIONALLY_FEASIBLE`.**

No blocking infeasibility has been identified at concept level across the dimensions assessed. This conclusion is not a delivery estimate or resource commitment. The concept phase is approved and Requirements Analysis may begin; every later SDLC phase still requires its own entry authorization.

## 19. Principal risks and responses

| ID | Risk | Initial significance | Planned response |
| --- | --- | --- | --- |
| R-01 | LLM invents unsupported business rules or findings | High | Evidence requirement, explicit inference labels, human review, abstention |
| R-02 | Local model is inadequate on available hardware | High | Bounded packages, model qualification by role, deterministic-only fallback |
| R-03 | Gatekeeper enforces techniques mechanically where they are not applicable | High | Applicability before coverage; technique absence is not itself a defect |
| R-04 | Defective or incomplete test basis is misreported as a tester failure | High | Separate test-basis findings; `PARTIALLY_ASSESSABLE`, `CONFLICTING_BASIS`, and `UNGRADABLE` |
| R-05 | Confidential documentation leaves the approved environment | Critical | Sealed profile, fail closed, no cloud fallback, verified network and data controls |
| R-06 | Evaluation becomes circular LLM-as-judge validation | High | Separated development, qualification, and held-out acceptance sets; human adjudication; deterministic mutation ledger |
| R-07 | Excessive false positives make review slower and erode trust | High | Precision and reviewer-effort metrics; severity and confidence separation |
| R-08 | The project expands into generation, documentation discovery, all ISTQB techniques, or all test levels | High | Versioned scope, explicit non-goals, phase-gated change control |
| R-09 | Jira/Xray/Zephyr specifics contaminate the core model | Medium | Canonical vendor-independent format and deferred adapters |
| R-10 | Product wording implies official ISTQB approval | High | Independent branding, disclaimer, prohibited-claim rules, static content review |
| R-11 | Import normalization silently loses meaningful testware | High | Explicit mapping, validation, provenance, and fail-visible behavior |
| R-12 | Benchmark is too simple and overstates generalizability | High | Clean controls, mutations, naturally imperfect packages where feasible, incomplete bases, and held-out multi-domain validation |
| R-13 | A deterministic result is treated as automatically correct or human-approved | High | Independent derivation and disposition dimensions; evidence and version traceability; human acceptance only |

Risk scoring, ownership, review cadence, and residual-risk acceptance belong to Test Planning and project governance in later phases.

## 20. SDLC and testing approach

The project will follow an explicit phase-gated SDLC while allowing feedback and correction within each phase:

1. Concept & Feasibility;
2. Requirements Analysis;
3. Solution and Architecture Design;
4. Implementation in bounded vertical increments;
5. Formal Product Validation using a detailed STLC;
6. Controlled Pilot or Deployment;
7. Maintenance and Evolution.

Testing is not postponed until Phase 5. Static testing begins with this Charter and continues for requirements, models, architecture, schemas, prompts, rules, testware, and user documentation. Test planning, risk analysis, test analysis, and test design begin in the corresponding SDLC phases.

The later formal STLC will include:

- test planning and control;
- test analysis;
- test design;
- test implementation;
- test execution and model evaluation;
- test completion and reporting.

Expected test layers include deterministic unit tests, schema and contract tests, import tests, integration tests, model qualification, metamorphic and repeatability checks where appropriate, end-to-end workflow tests, security and privacy tests, negative scope-classification tests, and human acceptance validation.

## 21. Concept-phase static review

Charter v0.1 underwent formal static review `SR-CHARTER-001`. Charter v0.2 incorporated all eight accepted dispositions, their correction verification was recorded as complete in Static Review Report v0.2, and Charter v0.3 recorded the Project Owner's phase decision. That completed review evaluated:

- clarity and unambiguity;
- completeness;
- internal consistency;
- testability and measurability;
- feasibility;
- confidentiality and security boundaries;
- traceability from problem to goals, scope, measures, and risks;
- consistency with the selected ISTQB-informed baseline;
- scope discipline;
- unsupported assumptions and premature design decisions.

Review anomalies will be recorded as findings with severity, evidence, disposition, and resolution status. Suggested lifecycle states are:

- `OPEN`;
- `ACCEPTED`;
- `REJECTED`;
- `RESOLVED`;
- `DEFERRED`.

These static-review lifecycle states are distinct from the product finding dispositions defined in Section 10. The Project Owner remains the final decision authority. The absence of an independent external reviewer must be documented as a limitation rather than concealed.

This v0.4 candidate is not a repetition of `SR-CHARTER-001`. It requires a focused delta review limited to `CR-RA03-001`, `CR-RA03-002`, their internal references, and confirmation that they do not alter the original phase authorization. Until that review and its correction verification are complete, v0.3 remains the approved Charter baseline.

## 22. Phase exit criteria

Concept & Feasibility may close only when:

- the problem and product hypothesis are approved;
- the primary user and primary use case are approved;
- the MVP scope and non-goals are approved;
- Review Package boundaries are approved;
- authority and abstention principles are approved;
- prohibited ISTQB-related claims are approved;
- confidentiality constraints and operating profiles are approved at concept level;
- the evaluation strategy and metric set are approved;
- principal risks and preliminary responses are reviewed;
- the static review is complete;
- no unresolved Critical or High static-review finding remains;
- Medium findings are resolved or explicitly accepted/deferred;
- the Project Owner records `GO`, `REVISE`, or `NO-GO`.

These exit criteria were satisfied for Charter v0.3 and the phase remains closed with `GO`. The v0.4 amendment does not reopen Concept & Feasibility or require a new phase-gate decision; it must nevertheless pass focused delta review before it may replace v0.3 as the controlled Charter baseline.

## 23. Items deliberately deferred to later phases

The following are intentionally unresolved and do not by themselves block concept approval:

- definitive functional and non-functional requirement identifiers;
- detailed Review Package and finding schemas;
- supported document formats for the test basis;
- user-interface and deployment form;
- technology stack and component architecture;
- exact local model and quantization;
- prompt and retrieval strategy;
- detailed local persistence schema and database technology;
- model-identity rules, change detection, and exact requalification triggers;
- numeric model-qualification and acceptance thresholds;
- exact dataset sizes, sampling method, and operational adjudication procedure;
- detailed threat model and security controls;
- data retention, deletion, audit, and backup policies;
- exact CSV profiles and Jira/Xray/Zephyr mappings;
- future read-only integration design;
- available delivery capacity, competing priorities, schedule, effort estimate, and release numbering.

Each deferred item must be routed to Requirements Analysis, Solution Design, Test Planning, or a later roadmap decision before implementation depends upon it.

## 24. Decision register

The status `Agreed during concept discovery` records acceptance of an individual concept decision. It does not constitute approval of the Charter, a phase-gate `GO`, or authorization to implement.

| ID | Decision | Status |
| --- | --- | --- |
| D-001 | Use the working name `Test Design Gatekeeper` | Agreed during concept discovery |
| D-002 | Describe the product as evidence-grounded and ISTQB-informed, not ISTQB-conformant or certified | Agreed during concept discovery |
| D-003 | Keep the Project Owner and tester as final decision authorities | Agreed during concept discovery |
| D-004 | Use pre-review of human-authored test cases as the primary MVP workflow | Agreed during concept discovery; eligibility wording clarified by D-029 |
| D-005 | Limit the MVP target to system-level functional black-box test design | Agreed during concept discovery |
| D-006 | Support EP, BVA, Decision Table Testing, and State Transition Testing in the initial technique set | Agreed during concept discovery |
| D-007 | Evaluate coverage and applicability rather than explicit technique labels or presumed author intent | Agreed during concept discovery |
| D-008 | Use a bounded Review Package controlled by the tester | Agreed during concept discovery |
| D-009 | Do not silently broaden scope or invent missing business rules | Agreed during concept discovery |
| D-010 | Keep result derivation independent from human disposition; deterministic output is not automatically accepted | Agreed during concept discovery |
| D-011 | Require evidence, uncertainty, abstention, and human review for LLM-derived output | Agreed during concept discovery |
| D-012 | Prohibit an overall “ISTQB compliant” or completeness verdict | Agreed during concept discovery |
| D-013 | Use out-of-scope artifacts as negative qualification tests without expanding supported scope | Agreed during concept discovery |
| D-014 | Park review of test cases for AI/LLM systems for a later product version | Agreed during concept discovery |
| D-015 | Use CT-GenAI to guide LLM use and CT-AI to guide testing of the Gatekeeper's AI component | Agreed during concept discovery |
| D-016 | Use public or synthetic data for laboratory benchmarking and external-model comparisons | Agreed during concept discovery |
| D-017 | Require a sealed local profile for confidential documentation | Agreed during concept discovery |
| D-018 | Use a canonical JSON Review Package plus local CSV/JSON import in the MVP | Agreed during concept discovery |
| D-019 | Defer direct Jira/Xray/Zephyr integration; begin any future integration as read-only | Agreed during concept discovery |
| D-020 | Begin validation with a synthetic customer-creation process and later diversify across telco, e-commerce, banking, and insurance | Agreed during concept discovery |
| D-021 | Separate development, model qualification, and held-out acceptance evidence and use documented human adjudication | Agreed during concept discovery |
| D-022 | Use scoped technique-applicability outcomes and reserve strong non-applicability for explicit criteria | Agreed during concept discovery |
| D-023 | Block confidential-data use until the trust boundary and its testable controls are defined and verified | Agreed during concept discovery |
| D-024 | Record delivery and resource feasibility as not yet assessed until an estimable backlog and capacity view exist | Agreed during concept discovery |
| D-025 | Permit additional knowledgeable human roles to use the tool for support while preserving human accountability and the tester-centered MVP workflow | Agreed during concept discovery |
| D-026 | Treat insufficient input as a fail-visible negative path; only the human supplies missing context and repairs test cases | Agreed during concept discovery |
| D-027 | Require version-aware local persistence of review history while deferring database technology and schema decisions | Agreed during concept discovery |
| D-028 | Treat model and inference configuration changes as requalification triggers rather than assuming a permanently stable capability | Agreed during concept discovery |
| D-029 | Apply positive testware-origin eligibility through explicit ROLE-03 human accountability: human-authored and human-controlled AI-assisted cases may qualify; TDG neither infers authorship nor treats unadopted generated content as qualifying by itself | Agreed by Project Owner through `OD-RA03-004`, 2026-09-12 |
| D-030 | Permit an explicitly supplied risk, prior defect, heuristic, or attributable experience-based rationale as test-basis evidence without adding detailed experience-based technique assessment to the four-technique MVP | Agreed by Project Owner through `OD-RA03-003`, 2026-09-12 |

## 25. Phase decision

| Decision | Status |
| --- | --- |
| Static review complete | Yes — `SR-CHARTER-001` closed; corrections verified |
| Critical/High findings resolved | Yes — corrections incorporated in v0.2 |
| Medium/Low findings resolved or explicitly dispositioned | Yes — corrections incorporated in v0.2 |
| Reviewer recommendation | `GO` to Requirements Analysis |
| Project Owner decision | `GO` — 2026-09-08 |
| Authorization to enter Requirements Analysis | GRANTED |
| v0.4 focused delta review | PENDING — v0.3 remains the approved baseline |

### Decision record

- Decision: `GO`
- Decision authority: Project Owner
- Date: 2026-09-08
- Decision statement: “GO — zezwalam projektowi Test Design Gatekeeper przejść do fazy Requirements Analysis.”
- Authorization scope: Requirements Analysis only.
- Not authorized: solution design, implementation, repository creation, deployment, or confidential-data use.
- Carried conditions: all downstream obligations in Static Review Report v0.2 remain active and must be converted into traceable requirements, constraints, risks, or later phase-exit criteria.

### Controlled amendment state

- Amendment direction: `CR-RA03-001` and `CR-RA03-002` accepted by the Project Owner on 2026-09-12 through `OD-RA03-004` and `OD-RA03-003`.
- Phase effect: none; the 2026-09-08 `GO` remains effective and is not reissued or rewritten.
- Baseline effect: v0.3 remains authoritative until a focused delta static review verifies this v0.4 candidate.
- Historical evidence: the original Charter review and phase-decision records remain unchanged.

## References

- [ISTQB Certified Tester Foundation Level Syllabus v4.0.1](https://istqb.org/?download_id=3345&sdm_process_download=1)
- [ISTQB Certified Tester — Testing with Generative AI](https://istqb.org/certifications/gen-ai/)
- [ISTQB Certified Tester AI Testing v2.0](https://istqb.org/certifications/certified-tester-ai-testing-ct-ai/)
- [Jira Cloud REST API v3](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/)
- [Atlassian guidance: export Jira Cloud work items to CSV](https://support.atlassian.com/jira/kb/how-to-export-issues-from-jira-cloud-in-csv-format/)
- [Xray Test Case Importer examples](https://github.com/Xray-App/tutorial-test-case-importer)
