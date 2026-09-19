# Test Design Gatekeeper

## RA-06 — Technique Applicability and Test-Design Coverage

| Field | Value |
| --- | --- |
| Document version and date | 0.1 — 2026-09-18 |
| SDLC phase | Requirements Analysis |
| Status | PROPOSED — AUTHOR CHECKED; OWNER REVIEW PENDING |
| Entry authorization | PG-RA05-001, consolidated in Section 7 of SR-RA05-001 v0.2 — GO to RA-06 |
| Effective upstream baseline | Charter v0.4; RA-01 v0.3; RA-02 v0.3; RA-03 v0.3 with PG-RA03-001 v0.2; RA-04 v0.2 with SR-RA04-001 v0.2; RA-05 v0.2 with SR-RA05-001 v0.2 |
| Decision authority | Project Owner |
| Requirements | 20 MUST requirements, all PROPOSED |
| Validation conditions | 14 proposed conditions; specifications for later verification, not executed product tests |
| Policy decisions | 4 OPEN recommendations |
| RA-07 gate | NOT GRANTED |
| Implementation and confidential-data use | Not authorized |

## 1. Purpose, sources, and conventions

RA-06 defines how TDG reviews a bounded set of existing TC for equivalence partitioning (EP), boundary value analysis (BVA), decision tables, and state transitions. It separates applicability, planned exercise of coverage items, alignment of expected results with supplied evidence, and uncertainty. It specifies observable product behavior without choosing algorithms, a model, a database, a UI, or an import schema.

The [Charter, Sections 8.2–8.4][charter], establishes these four techniques and prohibits penalties for missing technique labels when equivalent coverage is present. [RA-01][ra01] governs authority; [RA-02][ra02] governs workflow; [RA-03][ra03] governs supplied evidence and package identity; [RA-04][ra04] governs qualification; [RA-05][ra05] governs assessment records, findings, and human dispositions. Their acceptance records are [PG-RA03-001 v0.2][gate03], [SR-RA04-001 v0.2][review04], and [SR-RA05-001 v0.2][review05]. Repository references pin commit `bbd222927233095142208e9051979ea3beae1864`. Historical pending notices in preserved upstream snapshots are superseded by those acceptance records.

Methodological references are the official [ISTQB CTFL syllabus v4.0.1, Sections 4.2.1–4.2.4][ctfl], and its [Sample Exam B answers v1.7, Question 21][exam-b] for the BVA boundary convention. The versions and availability were checked on 2026-09-18. The status vocabulary, metric safeguards, acceptance policies, and original examples below are TDG proposals, not an ISTQB certification scheme or requirements imposed by ISTQB. No official conformity claim is introduced.

**Shall** identifies a proposed obligation. It becomes binding only when the Project Owner accepts the corresponding requirement and any applicable policy decision. All new rules in this draft remain proposed. Author checking is not the formal static review, user acceptance, or evidence that TDG has been implemented or tested.

The review concerns **test design**. A TC that describes an exercise has not thereby executed it; neither its stated expected result nor a coverage percentage proves correct system behavior. General experience-based review remains available under the upstream rules, without adding a fifth formal technique.

## 2. Assessment unit and evidence contract

A technique assessment identifies one captured package version, assessment run, original TC or justified within-TC views, relevant business property or behavior, requested review dimensions, and a chosen criterion where quantitative coverage is requested. A group assessment names its members. Views retain the original TC identities and satisfy RA-04's independence and context-preservation conditions.

| Record element | Required meaning |
| --- | --- |
| Subject and boundary | Named property, decision, or state behavior within the declared scope; included TC and visible exclusions |
| Evidence | Supplied source and TC locations; actual content, availability, and relevant contradictions |
| Technique model | Identified and versioned partitions, boundary targets, decision rules, or states and transitions; membership, constraints, and unresolved areas |
| Criterion | Named coverage objective and source of its selection; never silently changed to improve a result |
| Mapping | Which TC content supports which planned exercise; evidence and uncertainty for every claimed link |
| Interpretation provenance | Supplied statements, derived candidates, applicable human decisions, and qualified control versions kept distinct |
| Result and limits | Applicability, coverage observations, expected-result observations, ledger outcome, and any bounded metric |

A model may be explicitly supplied or derived from supplied prose. A derived model remains an assessment artifact, never a replacement source. LLM-proposed semantics are not automatically confirmed business rules. Existing applicable human decisions can be reused under RA-05; repeated confirmation of the same unchanged interpretation is not mandatory.

Role identifiers refer to [RA-01's role and authority definitions][ra01]. ROLE-02 controls the package boundary; ROLE-04 resolves business interpretations; ROLE-05 dispositions findings; ROLE-03 repairs source TC. Control-policy and control-qualification responsibilities remain those assigned in RA-01. Recording an assessment criterion does not grant its requester authority to invent business behavior.

Only the supplied package and explicitly authorized decision context may support assessment. Links, previous packages, similar TC titles, domain familiarity, and prior run history are not permission to retrieve or import additional rules. Unsupported dimensions remain visible while independent supported dimensions may proceed.

## 3. Applicability and the RA-05 ledger

Technique applicability is assessed for the identified property or behavior, not permanently assigned to the entire TC or application.

| Applicability outcome | Required evidence and interpretation |
| --- | --- |
| `APPLICABLE` | Supplied evidence establishes the relevant partition, ordered boundary, conditional decision, or state-dependent behavior. Detailed coverage may still be ungradable. |
| `NOT_INDICATED_WITHIN_SCOPE` | A completed inspection of the identified, accessible material found no grounded indication for this technique in that boundary. This is a bounded observation, not proof of universal non-applicability. |
| `INSUFFICIENT_EVIDENCE` | Missing, ambiguous, inaccessible, or contradictory decisive evidence prevents a supported applicability conclusion. |
| `NOT_APPLICABLE_BY_CRITERIA` | An explicit versioned exclusion criterion is satisfied by the evidence. For example, BVA does not apply to the expressly unordered nominal property being assessed. This says nothing about other properties. |
| `NOT_EVALUATED` | Applicability assessment was not attempted or could not be performed because a prerequisite or authorized capability was unavailable. No substantive applicability conclusion follows. |

An unsupported model output is not evidence for either negative applicability outcome. Both negative outcomes require a recorded boundary, inspected evidence, rationale, and the applicable control or interpretation provenance. Where a missing source could contain the decisive rule, the outcome is insufficient evidence, not absence of indication.

The proposed standard request is **assess applicability; assess coverage where applicability is established**. Applicability and coverage are distinct ledger dimensions. A supported applicability conclusion is `ASSESSED`; an attempted conclusion prevented by insufficient evidence is `UNGRADABLE`; an unavailable capability is `NOT_PERFORMED`; interrupted work is `INCOMPLETE`. An assessed coverage gap is still `ASSESSED`, not `UNGRADABLE` merely because the TC are incomplete.

If an evidence-supported applicability conclusion makes the conditional coverage dimension unnecessary, record why it was not requested under that condition. It does not create an artificial assessment failure. Conversely, if applicability is established but the necessary coverage model cannot be determined, the requested coverage dimension is `UNGRADABLE`. An explicit coverage request cannot be retrospectively removed to hide non-performance.

RA-05's run states, inventory accounting, and result availability remain unchanged. No new global quality status is added. The Charter's conceptual outcomes are represented through applicability, coverage observations, and optional technique-label metadata: coverage can be present with or without a label; applicable behavior can have gaps; assessment can be unsupported. A label alone establishes none of these.

## 4. Planned exercise, expected results, and bounded metrics

### 4.1 Two separate observations

Each identifiable coverage item has a planned-exercise mapping:

- `PLANNED`: supplied TC setup, data, actions, and sequence support exercising the item.
- `NOT_PLANNED`: sufficient inspection of the relevant review boundary establishes no such planned exercise.
- `UNDETERMINED`: a possible mapping, prerequisite, or relevant source cannot be resolved.

The mere appearance of a value in a title, comment, or unused dataset does not establish exercise. Missing setup can prevent a mapping. An ambiguous or unreadable TC that could exercise an otherwise missing item prevents a definite absence claim. A separately supported positive mapping remains valid even if another possible mapping is unknown.

Expected-result alignment is recorded separately as `SUPPORTED`, `MISSING`, `CONFLICTING`, or `UNDETERMINED`, relative to the supplied basis. Expected results may occur in steps, a description, or explicitly applicable shared content. TDG neither demands one particular field layout nor supplies an omitted expected result as though the author wrote it.

For example, a TC can clearly submit a boundary value but omit its expected response. The planned exercise remains visible; the missing expectation is a separate finding. A wrong expected response likewise does not erase the planned input. Neither case supports a conclusion that the test design is satisfactory.

Several invalid inputs in one TC require particular care: one rejection may prevent the other condition from being exercised. Independent validations, checks, or resets can establish otherwise. TDG records the evidence instead of always crediting every invalid value or imposing a universal one-invalid-input-per-TC rule.

### 4.2 Counting and qualification of a metric

A technique-design percentage may be reported only for an explicitly selected criterion with a finite, nonempty, versioned target set and sufficiently resolved mappings. The record exposes the target items, counted members, denominator, relevant exclusions, and evidence. Its numerator is the number of distinct items with supported planned exercise; the denominator is the number of items in that target set.

One TC can exercise several items; several TC can exercise the same item. Count each item once within its defined context. Retain all TC identities: repeated titles, steps, or content do not merge cases. Identical values used for different business properties or contexts are not automatically the same coverage item.

Do not report a headline percentage when the target set is incomplete, feasibility is unresolved, a limit truncated assessment, or uncertain mappings could change the numerator. Report supported observations and uncertainty instead. An explicitly named, independently assessable subset may have its own metric if these conditions hold for that subset; it must not stand in for the whole model. A zero denominator is undefined, never 100%.

A stated 100% means only that all items under that specific planned-exercise criterion are represented. It does not certify expected-result alignment, all requirements, all paths, interactions, execution, or ISTQB conformity. Do not average technique percentages or produce an overall quality score.

The criterion comes from an authorized request or an identified approved review policy. Without one, TDG can report applicability, grounded examples of planned or missing exercise, and questions. It cannot claim failure against an agreed quantitative target that was never selected.

## 5. Equivalence partitioning

The methodological unit is a nonempty partition whose members receive equivalent treatment for the relevant property; partitions for that property are disjoint. Valid and invalid partitions matter. Each-choice coverage considers every partition of each input dimension and does not establish coverage of their combinations. [CTFL Section 4.2.1][ctfl]

TDG needs evidence for the grouping, its domain, and any relevant context. It must not classify values as equivalent merely because they share a datatype or because an LLM considers them similar. A known accepted class does not establish a single universal invalid class: different rejection behaviors may justify different partitions.

For a range rule, a representative strictly inside the accepted range can support that partition; it does not automatically support its boundary targets. Invalid partitions require evidence that their planned exercise is not masked by an earlier rejection. Interactions between independently enumerated partitions remain unassessed unless the supplied behavior supports a relevant combination model.

Where a supplied partition model is incomplete or contradictory, preserve supported classes and identify the missing or conflicting rule. Do not manufacture exhaustive membership or quietly discard a class to obtain full coverage.

## 6. Boundary value analysis

BVA concerns ordered, contiguous partitions. A boundary is an extremal partition value. Two-value BVA uses a boundary and its closest neighbor in the adjacent partition; three-value BVA additionally considers the neighbor on the other side. [CTFL Section 4.2.2][ctfl]

TDG records the assessed property, domain, ordering, unit, precision or successor/predecessor relation, partition endpoints, and inclusivity. BVA can concern amounts, counts, lengths, or dates when their ordering and relevant limits are established. A numeric-looking label is not enough. An expressly unordered category does not acquire an order through sorting its names.

Do not invent a smallest currency increment, clock resolution, timezone, maximum length, or epsilon. If the nearest relevant neighbors cannot be determined, applicability may be established while quantitative BVA remains ungradable. Do not invent values outside an explicitly bounded domain; record unavailable neighbors at its ends.

**Original example.** The supplied rule explicitly defines the domain as all integers, accepts 10 through 20 inclusive, and rejects values below and above that interval. The three partitions are integers at most 9, integers 10–20, and integers at least 21.

| Selected criterion | Distinct target values for this model |
| --- | --- |
| Two-value BVA | 9, 10, 20, 21 |
| Three-value BVA | 8, 9, 10, 11, 19, 20, 21, 22 |

The boundary values across these partitions are 9, 10, 20, and 21. For three-value BVA, including each boundary's neighbors also brings in 8 and 22. A six-point set of 9, 10, 11, 19, 20, and 21 therefore does not fulfill this explicitly selected three-value criterion. The official [Sample Exam B explanation for Question 21][exam-b] confirms that boundaries of invalid partitions, and applicable finite domain endpoints, participate in the criterion; it is not restricted to the endpoints of the accepted interval.

This example has no lower domain endpoint because its stated domain is all integers. A different declared domain requires a different target model. Overlapping roles of the same value within this property are counted once. The chosen two- or three-value criterion is explicit: TDG does not call the former defective because the latter is stronger.

## 7. Decision tables

Decision-table coverage concerns feasible rules connecting condition combinations to actions. An impossible combination is distinct from a condition that does not affect an outcome. A supplied reduced table can be a valid assessment model. [CTFL Section 4.2.3][ctfl]

TDG needs the meaning of each condition and action, the applicable context, and any feasibility, reduction, exclusivity, or priority rules. A tabular source is optional; supplied prose can support an equivalent derived model with explicit interpretation provenance. Unknown values, unanswered conditions, and unspecified actions are not automatically “don't care” cells.

Do not assume every combination is feasible, infer priority between overlapping rules, or exclude a missing rule to improve coverage. A complete Boolean expansion contains 2^n rules only when the n conditions and their independence are established and that full model is the selected criterion.

For a reduced model, expose the reduction and its supported meaning. A TC satisfying one reduced rule may count for that selected rule criterion; it does not prove exercise of every expanded combination represented by the rule. No automatic exhaustive expansion, minimization solver, or enumeration of an unbounded model is required by this slice.

**Original example.** A supplied promotion model explicitly defines four feasible rules:

| Member | Voucher | Discount |
| --- | --- | --- |
| No | No | 0% |
| Yes | No | 10% |
| No | Yes | 5% |
| Yes | Yes | 15% |

TC for “member without voucher” and “voucher without membership” represent 2 of these 4 rules, even though both values of each condition appear somewhere. Duplicating either TC adds no rule coverage. If the combined-discount rule were absent from the supplied basis, TDG would ask for clarification rather than derive 15% by addition.

## 8. State transitions

State coverage, valid-transition coverage, and coverage including invalid transition attempts are different criteria. Visiting every state need not exercise every transition. A state model can describe events, guards, and actions as well as source and target states. [CTFL Section 4.2.4][ctfl]

TDG identifies transitions by their relevant behavior, including source, event, guard where applicable, destination, and action. Two transitions between the same states can be distinct; a self-loop can be an assessable transition. Supplied observations or setup must support the initial state and the successive reachable states.

A TC sequence earns planned-exercise mappings only while its prerequisites and preceding steps support them. An impossible or unresolved transition does not establish the later state. Credit for a later suffix requires an explicitly supported reset or independent setup; TDG cannot repair the sequence silently.

An omitted diagram edge or blank table cell does not automatically mean a forbidden transition. Explicit rules, or a supplied complete table with an unambiguous legend, may establish invalid attempts and their expected reactions. Do not invent an error, unchanged state, rollback, or recovery behavior. Multiple invalid attempts in one TC are acceptable when their independent setup and observability are supported; otherwise explain the dependent uncertainty.

**Original example.** The supplied model contains states `DRAFT`, `ACTIVE`, and `BLOCKED`, and exactly these valid transitions: activate from DRAFT to ACTIVE, block from ACTIVE to BLOCKED, and unblock from BLOCKED to ACTIVE. A TC that activates and then blocks visits all three states but represents only two of the three valid transitions. It supplies no evidence about unspecified invalid attempts.

The chosen criterion identifies states, valid transitions, or all explicitly specified valid and invalid attempts. Full path coverage, n-switch coverage, and exhaustive loop exploration are outside this MVP slice. A sequence may represent several selected items, each counted once.

## 9. Controls, findings, and change consequences

### 9.1 Structured controls and interpretation

Qualified deterministic controls may perform membership, distinct-item counting, boundary-set calculations, finite rule matching, or finite path checks on supported structured premises. This is not a commitment to encode every business rule, build a symbolic solver, execute the SUT, or run supplied test code.

An LLM may propose a partition, interpret prose, or suggest a TC-to-item mapping within the supplied boundary. Unless the relevant semantics and mappings are appropriately confirmed or otherwise established by qualified controls, a subsequent arithmetic calculation does not turn the overall claim into a deterministic finding. Preserve RA-05's derivation distinction and uncertainty. A deterministic count and a semantic recommendation may need separate items.

Parameterized or data-driven TC may establish multiple planned exercises where their supplied definitions guarantee identifiable values and applicable expectations. A statement such as “choose any value” or “generate random values” does not guarantee a boundary or every rule. Assess supplied definitions without executing generators, scripts, or automations.

Configured capacity limits must be visible in the run context and result. On reaching one, retain safe completed observations and mark affected requested work under RA-05. A limit is not evidence that a technique is inapplicable, that a TC is out of scope, or that all coverage items were inspected. Specific limits and implementation mechanisms remain for design and feasibility work.

### 9.2 Actionable, bounded findings

A finding identifies the source location, assessed subject, applicable criterion, established facts, uncertainty, impact within scope, and a human action. Separate a missing business rule, a missing planned exercise, an unsupported expected result, and an inability to interpret the representation. Not every limitation is a TC defect.

It is permissible to identify an existing TC and a grounded missing value, combination, or transition. That makes the recommendation useful without writing replacement steps. Optional educational examples are explicitly illustrative and cannot supply absent business rules. Every new finding starts `PENDING`; acceptance, deferral, rejection, and TC repair remain human responsibilities.

**Tiered-discount illustration from the project discussion.** For the supplied rule concerning exactly three distinct products priced 100, 80, and 60 PLN, the stated discounted amounts 100, 60, and 30 total 190 PLN. This observation establishes neither behavior for two or four products nor a tie-breaking policy. A missing policy for three equal prices is a basis-clarification question. It is not permission to invent product ordering or assert that equal prices necessarily cause rounding errors. Assess any such question only where it concerns the declared package boundary.

### 9.3 Versioning

Retain the model, criterion, mappings, control context, and their evidence with the assessment record. A first applicable ROLE-04 interpretation of already supplied evidence may support a not-yet-assessed entry in an active run only under the accepted RA-05 correction: it replaces no already applied premise and changes no configured behavior artifact.

Changing an applied interpretation, criterion, control, prompt, model, or other configured behavior requires a new run, even if a configured behavior change occurs before the first substantive entry. Reassessment of a committed entry also requires a new run. New or changed supplied business rules, scope, TC, or source context require a new package version. Terminal runs do not restart, and previous finding dispositions do not transfer automatically.

## 10. Proposed requirements and traceability

Every row below has priority **MUST** and status **PROPOSED**. References to RA-03, RA-04, and RA-05 identify accepted upstream requirements; section references identify this draft's proposed behavior. Every listed VAL has its full definition in Section 11.

| ID | Proposed requirement | Primary upstream trace | Direct validation |
| --- | --- | --- | --- |
| RA06-REQ-001 | TDG shall assess only the four selected techniques within a qualified subject and supplied boundary, using substantive evidence rather than technique labels or presumed author intent. | Charter §8.2–8.4; RA04-REQ-002, RA04-REQ-003, RA04-REQ-011 | VAL-001, VAL-014 |
| RA06-REQ-002 | TDG shall distinguish the five applicability outcomes in Section 3 and retain the inspected boundary, supporting evidence, uncertainty, and any explicit versioned exclusion criterion. | RA03-REQ-034; RA04-REQ-011, RA04-REQ-013 | VAL-002 |
| RA06-REQ-003 | TDG shall record applicability and coverage as distinct requested dimensions, map their outcomes to the RA-05 ledger, and preserve visible non-performance without retrospectively narrowing the request. | RA05-REQ-003, RA05-REQ-004 | VAL-001, VAL-002, VAL-013 |
| RA06-REQ-004 | TDG shall identify and version the technique model and selected criterion, trace their premises to supplied evidence and applicable interpretation decisions, and preserve unresolved semantics and authority boundaries. | RA03-REQ-004, RA03-REQ-020, RA03-REQ-035; RA05-REQ-008 | VAL-002, VAL-012, VAL-013 |
| RA06-REQ-005 | TDG shall distinguish planned exercise from expected-result alignment as in Section 4.1, requiring supported setup, data, actions, and relevant sequence while preserving missing, conflicting, or unknown expectations. | RA03-REQ-012, RA03-REQ-022; RA05-REQ-006 | VAL-003, VAL-005, VAL-011 |
| RA06-REQ-006 | TDG shall report a technique-design percentage only under Section 4.2's criterion, finite target-set, and mapping conditions; expose numerator and denominator; and withhold an undefined or unsupported percentage. | RA03-REQ-050; RA05-REQ-005, RA05-REQ-006 | VAL-004, VAL-006, VAL-009, VAL-013 |
| RA06-REQ-007 | TDG shall preserve uncertain mappings, require sufficient bounded inspection before declaring an item not planned, deduplicate item credit without merging TC, and label subset results and exclusions explicitly. | RA03-REQ-041, RA03-REQ-048; RA04-REQ-008 | VAL-003, VAL-004, VAL-014 |
| RA06-REQ-008 | TDG shall assess EP against evidence-supported valid and invalid partitions, retain incomplete or conflicting partition definitions, and distinguish each-choice coverage from combination coverage. | Charter §8.2–8.4; RA03-REQ-034; RA05-REQ-006 | VAL-005, VAL-014 |
| RA06-REQ-009 | TDG shall distinguish selected two-value and three-value BVA, derive their targets from the relevant partition boundaries, and deduplicate overlapping target values within the same property and context. | Charter §8.2–8.4; RA03-REQ-039; RA05-REQ-007 | VAL-006, VAL-007 |
| RA06-REQ-010 | TDG shall require evidence for relevant BVA ordering, domain, granularity, units, and inclusivity, retain finite-domain constraints, and leave unsupported neighbors or endpoints unresolved. | RA03-REQ-010, RA03-REQ-034, RA03-REQ-035 | VAL-006, VAL-007 |
| RA06-REQ-011 | TDG shall assess decision rules using evidence-supported conditions, actions, context, feasibility, and applicable priority rules, preserving missing rules and contradictions without inventing business outcomes. | RA03-REQ-010, RA03-REQ-034, RA03-REQ-035; RA05-REQ-008 | VAL-008, VAL-009 |
| RA06-REQ-012 | TDG shall distinguish unknown, irrelevant, and infeasible decision-table entries, identify any supported reduction, and avoid interpreting reduced-rule coverage as coverage of every expanded combination. | RA03-REQ-004, RA03-REQ-024, RA03-REQ-050; RA05-REQ-006 | VAL-008, VAL-009 |
| RA06-REQ-013 | TDG shall identify state-model items with relevant states, events, guards, destinations, and actions, and treat an invalid attempt as established only by supplied semantics rather than an unexplained omission. | RA03-REQ-024, RA03-REQ-034, RA03-REQ-035; RA05-REQ-006 | VAL-010, VAL-011 |
| RA06-REQ-014 | TDG shall distinguish state, valid-transition, and explicitly specified valid-and-invalid-attempt criteria, and credit sequence items only where supported setup, reachability, and any independent reset justify the exercise. | Charter §8.2–8.4; RA03-REQ-022; RA05-REQ-006 | VAL-010, VAL-011 |
| RA06-REQ-015 | TDG shall assess parameterized or data-driven TC from supplied definitions without executing them and shall not infer guaranteed item exercise from unspecified or random selections. | RA03-REQ-012; RA04-REQ-002, RA04-REQ-014 | VAL-003, VAL-014 |
| RA06-REQ-016 | TDG shall preserve the derivation of models and mappings and shall not classify a semantic conclusion as deterministic solely because subsequent counting or arithmetic was deterministic. | RA03-REQ-039; RA05-REQ-007, RA05-REQ-008 | VAL-012, VAL-014 |
| RA06-REQ-017 | TDG shall ground technique findings in identified evidence and criteria, distinguish basis gaps from design gaps and interpretation limits, and propose human action without rewriting TC or supplying unsupported expected behavior. | RA03-REQ-038, RA03-REQ-049; RA05-REQ-006, RA05-REQ-009, RA05-REQ-022 | VAL-012, VAL-014 |
| RA06-REQ-018 | TDG shall allow evidence-supported credit under multiple techniques while keeping their criteria separate, and shall not infer technique intent, overall test quality, execution coverage, or official conformity from these results. | Charter §8.3–8.4; RA03-REQ-050; RA04-REQ-015; RA05-REQ-005 | VAL-001, VAL-004, VAL-014 |
| RA06-REQ-019 | TDG shall expose assessment limits and affected work, preserve independent safe observations, and obtain no additional business context or execution evidence through external retrieval, supplied-code execution, or silent reuse of historical content. | RA03-REQ-005, RA03-REQ-041; RA04-REQ-014; RA05-REQ-014, RA05-REQ-019 | VAL-013, VAL-014 |
| RA06-REQ-020 | TDG shall retain technique-model, criterion, mapping, and evidence versions with the assessment, apply Section 9.3's package/run change rules, and preserve human disposition authority and the initial PENDING state of new findings. | RA03-REQ-043–RA03-REQ-049; RA05-REQ-009–RA05-REQ-012 | VAL-012, VAL-013 |

## 11. Validation conditions

Identifiers below expand to `RA06-VAL-001` through `RA06-VAL-014`; Section 10 uses their shorter suffixes for readability. These are planned validation obligations. They define expected observations without selecting a framework, creating an executable suite, or claiming successful product execution. All fixtures must be synthetic or otherwise permitted by the laboratory profile.

| ID | Condition and observable acceptance evidence | Direct REQ links |
| --- | --- | --- |
| RA06-VAL-001 | Review equivalent eligible TC with absent, correct, and misleading technique labels, and a package containing separately excluded items. Substantive technique conclusions follow evidence, not labels; exclusions and parent identities remain visible. Completed applicability does not imply execution or quality approval. | REQ-001, REQ-003, REQ-018 |
| RA06-VAL-002 | Provide distinct fixtures for every applicability outcome, including unordered nominal data, absent decisive basis, and unavailable capability. Verify evidence and explicit criteria for negative conclusions; correct ledger states; and conditional versus explicit coverage requests without hiding non-performance. | REQ-002, REQ-003, REQ-004 |
| RA06-VAL-003 | Vary a TC's actual actions, setup, unused values, missing or contradictory expected results, and supplied parameter definitions. Preserve supported exercise independently of oracle quality; leave uncertain exercise unresolved; an unreadable possible candidate prevents a definite absence claim. Random selection guarantees no target. | REQ-005, REQ-007, REQ-015 |
| RA06-VAL-004 | Use duplicate TC, one TC covering several items, a contextually different use of the same value, zero targets, and an incomplete model. Verify distinct-item counting, retained TC identity, explicit subset limits, and suppression of undefined or unresolved percentages and overall scores. | REQ-006, REQ-007, REQ-018 |
| RA06-VAL-005 | Supply complete, incomplete, and overlapping partition interpretations; valid and invalid representatives; and a possible masking rejection. Credit only supported exercise; preserve conflicts; show that each-choice coverage does not establish combinations. Missing expected behavior remains a separate observation. | REQ-005, REQ-008 |
| RA06-VAL-006 | Use Section 6's integer model and independently enumerated two- and three-value target sets. Verify 4 versus 8 distinct targets, no double credit at overlapping boundaries, and no silent substitution of the stronger criterion or invention of a domain endpoint. | REQ-006, REQ-009, REQ-010 |
| RA06-VAL-007 | Contrast discrete, explicitly bounded, unordered, and insufficiently specified amount/date models. Verify endpoint treatment and known-neighbor use; absent precision, ordering, or inclusivity remains unresolved. No implicit cents, epsilon, clock granularity, timezone, or out-of-domain neighbor is introduced. | REQ-009, REQ-010 |
| RA06-VAL-008 | Review equivalent prose and tabular decision models with known priorities, missing actions, contradictory overlaps, unknown cells, and explicit don't-care semantics. Supported models give equivalent conclusions; unresolved semantics remain visible and no priority or action is invented. | REQ-011, REQ-012 |
| RA06-VAL-009 | Use Section 7's four rules, a confirmed reduced model, and a model with unresolved feasibility. Distinguish 2/4 rule exercise from condition-value presence; report a reduced criterion explicitly; do not claim expanded combinations or silently remove uncovered or unknown rules. | REQ-006, REQ-011, REQ-012 |
| RA06-VAL-010 | Use Section 8's model, distinct guarded transitions between the same states, a self-loop, and unspecified versus explicitly invalid attempts. Distinguish state and transition items, 3/3 states from 2/3 valid transitions, and unknown behavior from supported invalidity. | REQ-013, REQ-014 |
| RA06-VAL-011 | Supply missing initial setup, an unreachable sequence suffix, and multiple invalid attempts both with and without supported independent resets. Credit only reachable or independently established exercise; retain separate expected-result limitations; invent no transition or recovery behavior. | REQ-005, REQ-013, REQ-014 |
| RA06-VAL-012 | Compare a qualified calculation over confirmed premises with the same calculation over an unconfirmed LLM model or mapping. Preserve derivation and uncertainty. A missing discount tie policy yields a grounded clarification item, never invented expected behavior; all new findings are PENDING and source TC remain unchanged. | REQ-004, REQ-016, REQ-017, REQ-020 |
| RA06-VAL-013 | Hit a recorded capacity limit or interrupt work; verify safe completed entries, visible limitations, and RA-05 availability. Exercise first applicable interpretation versus replacement of an applied premise, configured criterion/control change before assessment, reassessment, and source change: apply the accepted same-run/new-run/new-package boundaries correctly. | REQ-003, REQ-004, REQ-006, REQ-019, REQ-020 |
| RA06-VAL-014 | Use controlled document variants: remove a technique label, reorder independent TC, duplicate a case, remove its sole boundary witness, and change a supplied rule. Stable evidence preserves conclusions; actual changes affect only justified items and versions. Verify separate cross-technique results, no random-coverage inference, no external/history enrichment, and no TC rewrite. | REQ-001, REQ-007, REQ-008, REQ-015, REQ-016, REQ-017, REQ-018, REQ-019 |

## 12. Open decisions, author check, and exit

### 12.1 Owner decisions requested after review

| ID | Recommendation | Consequence if accepted |
| --- | --- | --- |
| OD-RA06-001 | Accept Section 3's applicability model and the standard conditional request: applicability first, then coverage where established. | Evidence-supported negative applicability is distinct from unknown or unavailable assessment; RA-05 accounting remains authoritative. |
| OD-RA06-002 | Accept separate planned-exercise and expected-result observations, with quantitative reporting only under Section 4.2's conditions. | A percentage cannot hide an incomplete model or imply sound expected results; uncertainty can legitimately prevent a percentage. |
| OD-RA06-003 | Require an explicit request or approved policy to select the coverage criterion; support both BVA variants and the named state criteria without forcing the strongest criterion. | Missing selection permits qualitative review but no claim against an unselected quantitative target. No fixed universal default or threshold is introduced here. |
| OD-RA06-004 | Accept bounded structured controls and provenance-preserving LLM assistance, with grounded recommendations that may reference TC but do not rewrite them. | No exhaustive solver, automatic test generation, source repair, or execution is added to the MVP. |

All four decisions are **OPEN**. These recommendations do not reopen previously accepted scope, privacy, authority, or human-accountability decisions.

### 12.2 Author-check scope

The author check covers requirement and validation identifiers, both directions of direct traceability, the example calculations, the consistency of proposed statuses, source references, and the boundary with accepted upstream policy. It was completed on 2026-09-18 using document checks and manual comparison with the accepted sources. It does not close the formal static review or certify future product behavior.

| Check | Result |
| --- | --- |
| Every MUST requirement has at least one directly linked VAL | PASS — 20/20 requirements |
| Every VAL links only to existing RA-06 requirements; forward/reverse edges agree | PASS — 14/14 VAL; 46 identical direct edges in both directions |
| Requirement/VAL/decision counts, identities, and proposed status are consistent | PASS — 20 unique REQ, 14 unique VAL, 4 unique OPEN decisions; no acceptance inferred |
| BVA, decision-rule, state, and discount example calculations | PASS — 4/8 BVA targets; 2/4 rules; 3/3 states and 2/3 valid transitions; 190 PLN total |
| Upstream identities and accepted authority/version rules | PASS — cited REQ identifiers exist; accepted RA-05 correction and closure govern; prior source wording preserved |
| Markdown structure and reference definitions | PASS — consistent table columns; all named references defined; repository links use the recorded commit |

The carried observation `SR-RA03-OBS-001` about the older indirect RA03-VAL-014 trace remains open: this slice's direct links do not close that separate obligation. `SR-RA03-OBS-002 / R-08` also remains open. This slice therefore uses one review document, reuses upstream lifecycle and authority definitions, and leaves implementation, benchmark construction, and detailed security to their planned work.

### 12.3 Exit and next work

The next step is the Owner's review of this draft, followed by a focused formal static-review record, any verified correction, controlled acceptance of the 20 requirements and policy decisions, and an explicit phase-gate decision. None of these is claimed by delivery of v0.1.

The next planned slice is RA-07, concerning the division of deterministic and LLM responsibilities and the limits of model-assisted conclusions. Detailed security belongs to RA-08; concrete input and output representations to RA-09; benchmark material and empirical success verification to RA-10 and the subsequent test work. These allocations do not authorize those phases or establish technical feasibility.

The controlled repository baseline remains the published RA-05 closure. This RA-06 draft is for review and is not a newly approved baseline or a repository publication instruction.

[charter]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/bbd222927233095142208e9051979ea3beae1864/docs/governance/test-design-gatekeeper-project-charter-v0.4.md
[ra01]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/bbd222927233095142208e9051979ea3beae1864/docs/requirements-analysis/test-design-gatekeeper-ra-01-stakeholders-actors-authority-v0.3.md
[ra02]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/bbd222927233095142208e9051979ea3beae1864/docs/requirements-analysis/test-design-gatekeeper-ra-02-system-context-workflows-use-cases-v0.3.md
[ra03]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/bbd222927233095142208e9051979ea3beae1864/docs/requirements-analysis/test-design-gatekeeper-ra-03-review-package-content-provenance-validation-v0.3.md
[gate03]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/bbd222927233095142208e9051979ea3beae1864/docs/reviews/test-design-gatekeeper-ra-03-gate-record-v0.2.md
[ra04]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/bbd222927233095142208e9051979ea3beae1864/docs/requirements-analysis/test-design-gatekeeper-ra-04-scope-qualification-classification-boundaries-v0.2.md
[review04]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/bbd222927233095142208e9051979ea3beae1864/docs/reviews/test-design-gatekeeper-ra-04-focused-static-review-v0.2.md
[ra05]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/bbd222927233095142208e9051979ea3beae1864/docs/requirements-analysis/ra-05/test-design-gatekeeper-ra-05-findings-dispositions-persistence-v0.2.md
[review05]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/bbd222927233095142208e9051979ea3beae1864/docs/requirements-analysis/ra-05/test-design-gatekeeper-ra-05-focused-static-review-v0.2.md
[ctfl]: https://istqb.org/?download_id=3345&sdm_process_download=1
[exam-b]: https://istqb.org/?download_id=3365&sdm_process_download=1
