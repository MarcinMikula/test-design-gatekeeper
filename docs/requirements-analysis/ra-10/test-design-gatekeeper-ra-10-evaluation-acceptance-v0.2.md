# Test Design Gatekeeper

## RA-10 — Evaluation and Acceptance

| Field | Value |
| --- | --- |
| Basis | Accepted RA-10 v0.2, originally dated 2026-09-21 |
| Acceptance and closure | All 22 requirements, 16 validation obligations and four policy decisions accepted; both source-table corrections, VAL-015 refinement, final baselines and RA-10 closure endorsed on 2026-09-21 in [SR-RA10-001 v0.2][review10] |
| Phase decision | Requirements Analysis closed and GO to Solution and Architecture Design granted on 2026-09-22 in [SR-RA-001 v0.2][phase]; current work remains subject to the development pause |
| Text maintenance | Consolidated on 2026-10-24; section numbers and identifiers retained |
| Decision authority | Project Owner for requirements and project gates; existing evaluation, operational and protection authorities remain unchanged |

This is the maintained evaluation and acceptance contract. The [original v0.2 text][original] remains in Git history; earlier review hashes and byte counts identify that snapshot. [README.md](../../../README.md) describes current capability and the development pause. Requirements acceptance defines how the product must be evaluated; it does not demonstrate its usefulness.

## 1. Purpose, baseline, and scope

RA-10 defines how to check whether TDG finds useful, evidence-backed problems in existing test designs and helps a human reviewer at an acceptable cost. It specifies reference evidence, measurements, comparisons and decision rules. The central question is whether the hybrid improves review over simpler alternatives without an unacceptable burden of false findings and verification work. A persuasive explanation, frequent acceptance of suggestions or agreement with another LLM cannot answer that question alone. [Charter §§4, 16–18][charter]

The accepted scope and related contracts are in the [Charter][charter] and [RA-01][ra01], [RA-02][ra02], [RA-03][ra03], [RA-04][ra04], [RA-05][ra05], [RA-06][ra06], [RA-07][ra07], [RA-08][ra08] and [RA-09][ra09]. The [Requirements Analysis closure][phase] indexes their effective versions and decisions. Entry to RA-10 was granted by `PG-RA09-001` in [SR-RA09-001 v0.2][gate09]. RA-03 v0.4 includes the accepted input-sufficiency corrections used in Section 8.1. RA-09 retains its explicit native envelope and prohibition on unauthorized runtime LLM capture-field mapping.

The methodological references remain CTFL v4.0.1, CT-GenAI v1.1 and CT-AI v2.0 as recorded upstream. These are TDG project policies, with no claim of official ISTQB conformity, certification or endorsement. `Shall` states accepted obligations; evaluation-process requirements may be fulfilled through controlled human work and later tooling without automatically adding runtime features.

The scope remains one supplied, bounded Review Package; system-level functional black-box review; EP, BVA, decision tables and state transitions where supported; independent classification axes; and human interpretation and repair authority. Automatic source retrieval, TC execution or repair and review of AI/LLM-system testware remain outside this scope. Evaluating TDG's own AI component is a separate product-validation activity.

## 2. What is evaluated, and who decides

### 2.1 Units and identities

| Unit | Evaluation meaning |
| --- | --- |
| Campaign | An identified evaluation purpose, protocol, dataset/oracle versions, configurations, conditions, attempts and result record. Exploration, task qualification and product acceptance are separate purposes. |
| Package family | A reference business example and its related variants, paraphrases, translations, mutations and versions. Family identity is used to control exposure and dependence; it does not merge operational packages. |
| Package version | The immutable supplied material governed by RA-03 and RA-09, with exact inventory and capture identity. A campaign selects versions explicitly. |
| Assessment opportunity | A predefined subject and requested review dimension under a specified package/configuration condition. It is the denominator unit for assessability and limitation measurements. |
| Expected issue | An adjudicated, identifiable gap or required clarification that can be justified from the supplied evidence and requested boundary. One issue may affect a bounded group of TC. |
| Reported atomic claim | One separately judgeable assertion or clarification within an output item. A paragraph containing a valid observation and an invented consequence has at least two claims. |
| Attempt / run | An invocation attempt belongs to an identified evaluation or assessment run. Repetitions do not create new independent business examples. |
| Human review session | One participant's bounded review task under an assigned condition, with recorded exposure, time, effort and resulting human decisions. |

Original TC counts, within-TC views, coverage items and reported claims remain separate. Three views of one TC are not three independently reviewed TC. Three repeated descriptions of one missing boundary are not three detected issues. Identical text in unrelated TC does not justify merging their identities. RA-06 technique-design coverage is also different from this document's measurement of TDG detection performance.

### 2.2 Human authority

The roles retain [RA-01's definitions][ra01]. ROLE-04 supplies accountable interpretation of the reference business basis; ROLE-08 approves evaluation protocols and task/configuration qualification; ROLE-09 authorizes data classification, security policy and sealed readiness; ROLE-10 accepts requirements, product-gate evidence and SDLC transitions within project authority. ROLE-03 owns human TC corrections, and ROLE-05's operational finding dispositions remain separate from oracle judgments.

A person may combine roles with explicit acting-role attribution and competence assumptions. A solo experiment is permitted, but cannot be represented as independent human validation. A second competent human is preferred for disputed or consequential semantic judgments where available. If disagreement remains material, the oracle records uncertainty; neither an evaluated LLM nor another LLM decides the final truth or grants qualification.

These decisions are distinct:

| Decision | Required authority and evidence |
| --- | --- |
| Is this reference interpretation justified? | Attributable human adjudication using the supplied basis; ROLE-04 interpretation where required |
| May this exact configuration perform this task? | ROLE-08 decision under RA-07, with a bounded qualification envelope |
| Does the product provide sufficient value for the claimed use? | Approved acceptance protocol, comparison evidence and attributable project acceptance decision |
| May protected data enter this deployment? | RA-08 readiness evidence and separate ROLE-09 authorization |
| May the next SDLC phase begin? | Explicit ROLE-10 gate after the corresponding exit review |

## 3. Evaluation corpus and exposure control

### 3.1 Start with a bounded reference family

The first development family remains the synthetic customer-creation process from Charter §15.1. Use small, explicitly specified rules, such as an age range, document requirement, consent condition or customer-state transition. Do not require every technique to apply to every package. The reference material is constructed and reviewed during later test analysis/design; this document does not silently supply new business rules.

The user's discount example is valuable as a development illustration and later e-commerce campaign seed. It does not replace the agreed first process, establish a production-domain oracle, or become held-out evidence after being discussed here. Telco, e-commerce, banking and insurance campaigns remain later generalization work. A claim about those domains requires evidence for those domains; a customer-creation experiment alone cannot support it.

### 3.2 Partition by purpose and related family

| Partition | Permitted use | Exposure consequence |
| --- | --- | --- |
| Development | Create reference material, tune prompts, controls and mappings; make exploratory measurements and propose criteria | Results are development evidence, never independent acceptance evidence |
| Qualification | Evaluate a frozen candidate against a previously approved task-specific protocol | Record every inspection and adaptation; tuning creates changed behavior and a new evaluation record, not an untouched qualification attempt |
| Held-out acceptance | Evaluate the frozen product/composition against the approved acceptance protocol | Do not use the material or its answers for tuning; after exposure, it cannot provide fresh unbiased evidence for an adapted candidate |

Assign related families to partitions before tuning or decision-bearing execution. Renaming TC, changing prices, translating text, moving files, or producing mutations of a known package does not establish independent held-out content. Record known similarities, authors' prior exposure and any residual uncertainty about leakage, including unknown model pretraining exposure. No claim that a model has never seen equivalent public content is implied.

The exact held-out packages and oracle are not published in the public repository before the applicable campaign. Public documentation can describe categories, protocols and development examples. Controlled access is an evaluation integrity measure even when the material itself is eligible synthetic data. A sole author who already knows the reference answers records that limitation; withholding them only from the prompt does not create independent human evaluation.

A small initial corpus may support exploration only. If three credible partitions cannot be established, report that limitation and withhold the corresponding independent qualification/acceptance claim. Do not solve insufficient evidence by relabelling a development set.

### 3.3 Required category plan

Each campaign records included categories, mandatory slices for its claim, actual counts, and justified exclusions. Full Cartesian coverage is not required; selected interactions must reflect the risks and the proposed envelope.

| Category | Required challenge or comparison |
| --- | --- |
| C-01 — Bounded reference controls | Human-reviewed, adequate designs for the declared criteria, including situations where a technique is not applicable; “no seeded gap” alone does not establish an error-free oracle |
| C-02 — Controlled mutations | Remove a supported EP representative, boundary target, decision rule or specified transition attempt; alter an expected result; remove relevant behavioral evidence; verify each mutation's actual effect |
| C-03 — Imperfect human designs | Happy-path-only and naturally incomplete designs where feasible; retain original context and human adjudication rather than presenting every imperfection as a planted mutation |
| C-04 — Evidence limitations | Missing, conflicting or opaque basis, ambiguous origin, incomplete provenance, unsupported links and safely separable subsets; distinguish package minimum from claim-specific evidence |
| C-05 — Classification boundaries | Mixed levels/types/design bases/execution modes, misleading labels, out-of-scope target domains, and separable/non-separable assertions; an automated system black-box TC is not rejected merely for being automated |
| C-06 — Technique semantics | Missing expected result despite planned boundary exercise, random selection without guaranteed endpoint, incomplete decision model, unreachable sequence suffix, and unsupported numerical coverage |
| C-07 — Representations and identity | Supported native JSON/CSV and prose variations, duplicate source IDs, repeated generic steps, strict envelope errors versus retained content gaps, locators, immutable versions, and import/export fidelity |
| C-08 — Capability and resource limits | Exact permitted tasks/languages, short and long packages, unsupported envelopes, preflight refusal, truncation, timeout, retry exhaustion, cancellation and deterministic-only operation |
| C-09 — Authority and protection | Synthetic instruction injection, self-approval attempts, denied/revoked access, current qualification, diagnostic disclosure, retained copies and valid/invalid egress observation under RA-08 |
| C-10 — Workflow and human use | Review, evidence inspection, disposition, external human repair, new package/run and controlled export; include false suggestions and useful abstention, not just successful detection |

C-07/C-09 include control and security verification of TDG; they are not additional review techniques applied to the user's business TC. Semantic metrics and control-test results are reported separately.

## 4. Reference evidence, human adjudication, and matching

### 4.1 Reference and mutation records

For every reference package retain its family/version, permitted classification, supplied scope and basis, TC inventory, requested dimensions, expected eligibility and assessability, applicable technique models/criteria, expected issues and supported zero-issue boundaries, prohibited conclusions, and oracle provenance. The oracle may contain evaluation labels hidden from TDG, but a required substantive TDG finding must remain inferable from what TDG was actually supplied.

A mutation record identifies the parent, exact change, intended issue, affected dimension, supplied evidence, and a human check that the mutation is effective. Equivalent or redundant mutations are excluded or distinctly labelled: removing one TC does not create a coverage gap if another still exercises the same target. Mutants from one parent remain one related family for exposure and uncertainty analysis.

Missing optional direct TC-to-requirement links are not automatically defects. A traceability mutation must damage a required or explicitly supplied relationship under the accepted contract. Likewise, an unspecified state transition is not automatically forbidden, and removal of an inapplicable technique cannot create a technique defect.

Reference issues distinguish a TC-design gap, a test-basis gap, an intake/authority problem and a warranted clarification. Mandatory expected issues used for recall are identified before scoring. Optional improvement ideas and generic methodological advice are reported separately and cannot inflate gap recall.

### 4.2 Human adjudication procedure

1. Identify the competent reviewer, acting authority, source versions, review criteria and independence limitations. Review supplied evidence before considering model agreement.
2. Record the expected subject/dimension, conclusion or permitted alternatives, evidence locations, material assumptions, and whether the oracle is mutation-grounded or semantically adjudicated.
3. Compare disputed judgments against the same bounded material. Seek an additional competent reviewer where available. Retain both interpretations and rationale rather than deciding by model majority or confidence.
4. Mark the judgment RESOLVED or UNRESOLVED for evaluation. A resolved oracle can correctly expect abstention because the business basis itself is insufficient. That is different from evaluators being unable to agree on the oracle.
5. Preserve versioned corrections. If output reveals a previously missed legitimate issue, adjudicate it rather than automatically calling it false. Record the corrected oracle and recompute comparable results for every affected variant. Disclose post-result correction and sensitivity to it; changing the product afterwards requires the Section 7.4 consequences.

Operational ACCEPTED/REJECTED/DEFERRED dispositions, popularity and a reviewer's willingness to act are not correctness labels. A reviewer may reject a valid low-priority suggestion or accept an incorrect one. Human repair and subsequent verified improvement are also separate observations.

### 4.3 Claim matching and duplicate treatment

Before decision-bearing scoring, define atomic splitting, substantive equivalence and matching rules. Match by affected subject, dimension, asserted problem and supporting evidence, allowing valid paraphrases. Merely mentioning “BVA,” requesting “more negative tests,” or listing all four techniques does not detect a specific missing item.

One supported atomic claim can credit one expected issue at that granularity. A single output item can contain several separately supported claims, each with its own match. Equivalent repeated claims about one issue earn one detection credit; retain repetition counts and their review cost. Conflicting statements, distinct consequences and differences in asserted certainty are not collapsed as harmless duplicates. The scoring projection never rewrites original product records.

Each distinct reported evaluative claim is adjudicated as SUPPORTED, INVALID, or UNRESOLVED. INVALID includes a false assertion, an unsupported asserted premise/consequence, a wrong subject or scope, and a claim whose required support is absent. An appropriately bounded question about a real evidence gap can be supported; a question mark does not excuse an invented premise. Pure procedural diagnostics and non-assertive generic advice are counted separately, with their workload visible.

Substantively valid discoveries absent from the frozen expected-issue list contribute to supported-claim precision after adjudication, but not to frozen known-issue recall. Report novelty separately. If the oracle is revised, preserve both the original comparable score and the revised analysis; do not quietly enlarge recall targets only for one variant.

## 5. Metric contract

### 5.1 Common counting rules

Every metric has a campaign/partition, configuration, subject boundary, category, numerator, denominator, unit and missing-data rule. Report raw counts alongside percentages. A zero denominator yields UNDEFINED with a reason, never an automatic 0% or 100%. Development, qualification and acceptance results are not pooled into one headline score.

For repeated scoring, retain the package-version/run occurrence of each claim, target issue and opportunity. Deduplicate equivalent claims within that occurrence, not across runs. A target missed in one repetition and detected in another has both outcomes recorded; a union of all answers cannot masquerade as the result of one ordinary review. Apply the frozen aggregation policy while reporting family and repetition counts separately.

Count related families and repeated runs explicitly. Large families or repeated prompts must not dominate an undisclosed pooled result. Report relevant task, technique, language, representation, evidence-sufficiency and complexity slices; predeclare any weights and macro/micro aggregation. No aggregate overrides a failed mandatory slice.

Use these symbols within one declared scoring boundary:

- `S`, `F`, `U`: distinct SUPPORTED, INVALID and UNRESOLVED reported evaluative claims after controlled duplicate handling.
- `E`: adjudicated expected issues that are required, supplied-evidence-detectable and within the campaign's requested target capability; `H`: distinct members of `E` detected with a supported matching claim.
- `O`: all prespecified requested assessment opportunities; their expected assessability and actual ledger consequences are separately recorded.

For a capability being claimed, inability, failure or unjustified abstention does not remove its otherwise eligible issues from `E`. A baseline without that capability can be shown on both its declared envelope and a common product target: the latter exposes the benefit gap. Explicitly out-of-scope or inherently ungradable issue classes do not become invented missed TC defects; correct boundary behavior is measured separately.

The precision/recall distinction follows the standard distinction between the supported proportion of reported items and the detected proportion of target items. TDG's atomic units, adjudication, duplicate policy and uncertainty treatment are project-specific extensions. [Introduction to Information Retrieval, evaluation of unranked retrieval sets][ir-metrics]

### 5.2 Measures and interpretation

| ID / measure | Definition and required companion evidence |
| --- | --- |
| M-01 — Supported-claim precision | `S / (S + F)` on adjudicated claims; always also show `U`, total reported occurrences and duplicate count. If `U > 0`, show unresolved share `U / (S + F + U)` and the descriptive sensitivity range from `S / (S + F + U)` to `(S + U) / (S + F + U)`. These bounds are not a statistical confidence interval. |
| M-02 — Known-issue recall | `H / E`, by issue category and declared target. Report missed targets and their causes, including failure and excessive abstention. Repeated wording earns no extra credit; unanticipated valid discoveries remain separate. |
| M-03 — Unsupported assertion rate | Claims with an adjudicated unsupported material assertion divided by `S + F`; these claims are a documented subset of `F`. Show unresolved share and counts separately. Do not call this the whole false-positive rate: other invalid claims may be contradicted, mis-scoped or wrong for another reason. |
| M-04 — False zero-issue conclusion | Count an explicit bounded “no supported findings” conclusion as false when it misses at least one known detectable issue in that same asserted boundary, or claims completed inspection over work that was not adequately assessed. Divide by all such explicit zero-issue conclusions. Separately report defective boundaries receiving that conclusion divided by all adjudicated defective boundaries. |
| M-05 — Assessability and abstention | Report the expected-versus-observed outcome matrix on `O`, with separate causes for missing/conflicting evidence, unsupported capability, policy denial and interrupted work. Correct evidence abstention: correctly withheld dependent conclusions with an accurate limitation divided by opportunities requiring that abstention. Excessive abstention: unjustified evidence-based abstentions divided by opportunities with sufficient evidence and the claimed capability. Keep failures/refusals separate. |
| M-06 — Evidence and derivation | Structural traceability: claims with complete required, resolvable same-version references and derivation/configuration metadata divided by claims requiring that evidence. Separately report human-adjudicated semantic support. A real but irrelevant paragraph passes reference existence only. Missing retention evidence is visible; it cannot be reconstructed or scored as inspected. |
| M-07 — Human disposition and actionability | Report operational disposition counts at a fixed observation cutoff; decided-acceptance share is ACCEPTED divided by ACCEPTED + REJECTED + DEFERRED, with PENDING shown separately. Record whether a reviewer could locate the issue/evidence and identify an appropriate next action without inventing business rules. These are utility observations, not truth labels. |
| M-08 — Review benefit and burden | Compare human-detected supported issues, residual known issues, accepted incorrect suggestions, active review time, elapsed time, clarification work and correction/rework effort under Section 6.2. Report the cost of dismissing invalid, duplicate and generic outputs. A time saving with worse unapproved quality is not success. |
| M-09 — Repeatability | On repeated unchanged configurations/packages, report detection frequency per expected issue, variation of verdicts/limitations, invalid claims and failure frequency. Compare substantive identities and outcomes rather than wording alone. Stable wrong answers and all-empty outputs remain poor quality under other measures. |
| M-10 — Deterministic reproducibility | For repeated identical deterministic inputs, premises and behavior versions, compare substantive outcomes, values and evidence references. Explain permitted run IDs/timestamps separately. An upstream probabilistic premise does not turn the whole pipeline into a deterministic control. |
| M-11 — Resource feasibility | Record target hardware and actual RAM/VRAM, runtime/configuration, package/context size, concurrency, cold/warm conditions, latency distribution, peak measured resources, refusals, timeouts, failures and retries. Report started and completed work, not only successful-call speed. |
| M-12 — Safety and authority | Record applicable invariant/control results independently from semantic quality. Include forbidden retrieval/egress, unauthorized action, self-qualification, silent source mutation and unsupported approval claims. Under RA-08 distinguish blocked attempts, observed forbidden transmission and insufficient observation; missing measurement is not zero violations. |

`NO_SUPPORTED_FINDINGS` in the Charter is a meaning to evaluate, not a new RA-05 run state. An empty findings array, a completed run with no substantive availability, or `NOT_PERFORMED` is not itself an explicit zero-issue conclusion. Such cases remain visible in M-02/M-05 and the operational outcome inventory. Conversely, correct caution does not hide poor detection on assessable material.

M-01/M-03 are reported separately for TC-design findings, basis issues and clarification suggestions. Generic advice and procedural diagnostics cannot dilute a failed substantive-finding slice. Raw output occurrences and per-session burden remain visible even when equivalent claims are deduplicated for semantic scoring.

### 5.3 Illustrative calculation — not an experiment

Suppose an eligible requested boundary has ten known detectable issues. TDG emits eight distinct adjudicated evaluative claims: six supported, matching six different expected issues, and two invalid unsupported assertions. It also repeats one of the six supported claims three extra times.

| Observation | Result |
| --- | --- |
| Known-issue recall | 6 / 10 = 60% |
| Supported-claim precision | 6 / 8 = 75% |
| Unsupported assertion rate | 2 / 8 = 25% |
| Additional duplicate occurrences | 3; no additional recall credit, but included in review burden |
| Remaining known issues | 4, including any missed because an otherwise capable review failed or abstained unjustifiably |

These figures are arithmetic examples, not thresholds or TDG results. If the tool instead emits nothing and refuses every assessable opportunity, precision is UNDEFINED, recall is 0 / 10, and its limitations/failures remain visible. That behavior cannot establish successful assistance.

For the discount example, “the supplied basis does not decide equal-price ordering; please clarify” may be a supported clarification within the requested scope. “Therefore the system will round incorrectly” needs separate supplied support and is not established by the omission. Correctly computing 100 + 60 + 30 = 190 for the stated distinct-price example proves neither the missing tie rule nor overall test-design adequacy.

### 5.4 Sample adequacy and uncertainty

Before decision-bearing execution, approve required category counts, independent family coverage, repeated-run count, participant/session coverage, uncertainty method and stopping rule. Choose them using the risk, intended claim, exploratory variability and available effort; this document does not invent a universally sufficient sample size.

Show uncertainty suitable for the actual sampling unit and dependence. Repeating one package twenty times measures variation on that package, not twenty independent business examples. A binomial proportion interval is appropriate only when its event/unit assumptions are justified; NIST describes Wilson and exact binomial intervals and cautions about small-sample approximations. The campaign must justify its chosen method rather than mechanically applying one to correlated claims. [NIST, confidence intervals for proportions][nist-proportions]

An unresolved oracle is reported as a denominator limitation. A criterion cannot pass merely by dropping difficult unresolved observations: apply its frozen sufficiency rule and sensitivity assessment. Missing a mandatory category, a required interval bound or sufficient independent evidence yields INCONCLUSIVE for that claim. A descriptive small study may still guide design without supporting general acceptance.

## 6. Comparisons and execution protocol

### 6.1 Compared conditions

The Charter comparison set remains available, with applicability and omissions documented:

| Condition | Purpose and fair-comparison boundary |
| --- | --- |
| Deterministic controls only | Establish the simpler machine baseline with known structured premises and explicit unperformed semantic dimensions |
| Qualified local LLM contribution without substantive deterministic review rules | Isolate semantic contribution where feasible; retain mandatory scope, security, qualification and output-contract controls. “LLM only” never disables protective controls. |
| Actual deterministic + qualified local LLM composition | Measure the proposed hybrid, including context handling, output filtering, orchestration, retries and failure consequences |
| Strong external model | Optional comparator on explicitly eligible public/synthetic material; record its accessible version/settings and reproducibility limits. It is not the oracle or a sealed fallback. |
| Human review without TDG | Measure the existing activity against the same bounded reference criteria |
| Human review with TDG | Measure the total assisted workflow, including checking, rejecting and acting on output |

For a claim that adding the LLM improves the human workflow over deterministic assistance, include a human-plus-deterministic condition alongside human-plus-hybrid. Otherwise the study cannot attribute all observed benefit to the LLM. The first exploratory study may be smaller, with the missing comparison and resulting claim limitation explicit.

Compare identical supplied evidence and requested targets where meaningful. If one baseline receives human-confirmed structured rules while another must extract them, disclose this advantage and measure preparation cost. An additional isolated component experiment can supply equal confirmed premises to both, but does not replace the whole-workflow comparison. Record model/tool-specific capability limits and deliberately authorized external processing.

Task-specific RA-07 qualification and product acceptance are separate. Candidate measurements may occur under the permitted unqualified laboratory evaluation context; operational and human-reliance use requires applicable qualification. Evaluators examining unqualified outputs know they are experimental and retain full human review responsibility.

### 6.2 Human benefit protocol

Define one comparable review endpoint before sessions: for example, a bounded list of evidence-backed issues and limitations ready for human disposition. Give participants equivalent task information and measure resulting quality against the adjudicated oracle. TC repair, if studied, is performed by a human outside TDG and timed separately; counting only the tool's response time omits most of the work.

Record participant competence, acting roles, training/familiarization, prior family exposure, assigned condition, session boundary, interruptions and tool availability. Allocate comparable package families and counterbalance condition order where feasible. Do not have the same person immediately review the same now-familiar package unaided and then treat assisted improvement as unbiased evidence. A single-user walkthrough remains useful but is labelled a limited quasi-UAT study.

Capture active preparation, evidence reading, tool invocation/inspection, verification of suggestions, disposition, clarification and any measured repair time. Record elapsed waiting time separately; failures, rejected suggestions and abandoned tasks remain in the observation inventory. Compare both supported issues gained and burden; retain negative assistance, including a human adopting an invalid suggestion or missing a problem because the tool appeared reassuring.

The recommended primary acceptance hypothesis is **quality improvement within an approved burden limit**, because the project's stated problem is shallow test design. A different speed-focused hypothesis requires an explicitly approved quality non-inferiority margin. Choose the hypothesis and margins before acceptance execution; do not select whichever outcome looks best afterwards. Qualitative feedback explains measured results and can identify usability defects, but does not replace the comparison.

### 6.3 Repetition, resources and controlled failure

Freeze the actual model artifact, quantization, templates/instructions, inference/runtime, context policy, supporting controls, output handling and retry/selection policy. Retain all attempts required by the protocol, including failures; report both first-attempt and final policy-level outcomes when retries affect performance. A best-of-many configuration is evaluated with its full selection policy and cost, not its best answer alone.

Measure the intended machine. An 8 GB GPU is a resource constraint to investigate, not a qualification result; record actual VRAM, system RAM, CPU and any offload configuration separately. Establish the supported package/task envelope, response/resource limits and conditions under which useful deterministic-only or partial operation remains possible. A result measured on a larger GPU cannot establish suitability on the intended machine.

Use controlled faults and synthetic boundary fixtures to verify visible refusal, interruption, bounded retries, retained safe results and absence of silent cloud fallback. Deterministic reproducibility checks compare fixed identified premises; whole-pipeline LLM repeatability is a separate measurement.

Metamorphic relations need human-justified assumptions and expected invariants: reordering independent TC with all relevant context retained may preserve substantive coverage conclusions; removing the only supported boundary exercise should alter that coverage observation. Translation, paraphrase, sequence reordering and label changes are not automatically semantically neutral. These are later test-design inputs, not executed checks or permission to mutate accepted sources.

## 7. Criteria, results, and acceptance authority

### 7.1 Criteria are fixed before decision-bearing runs

Following Charter §16.7 and RA-07 §6.1, numerical thresholds are proposed after an initial exploratory baseline measurement, then approved before the corresponding decision-bearing qualification or acceptance campaign. No percentage in Section 5.3 is an acceptance value. This slice owns the definition and controlled completion of those criteria; values remain an explicit prerequisite, not an assumed later detail.

Each criterion record identifies the metric and direction, task/category and claim, numerator/denominator policy, threshold or comparison margin, uncertainty/decision rule, required sample/category sufficiency, handling of unresolved or missing evidence, severity/failure policy, authorized exceptions if any, applicable versions and approving human/date. Separate qualification thresholds from product acceptance thresholds. Any “not applicable” decision needs a predeclared condition and justification, not a post-result omission.

| Criteria group | What must be set before the applicable decision-bearing campaign |
| --- | --- |
| Substantive quality | Minimum useful recall and supported-claim precision for required slices; unsupported assertions and false zero-issue limits; unresolved-oracle tolerance and sufficiency rules |
| Appropriate limitation | Correct abstention/classification expectations, excessive abstention and capability/failure limits, preserving the accepted outcome distinctions |
| Evidence and authority | Required evidence/derivation and authorization invariants; mechanically applicable contracts remain obligations, not adjustable accuracy targets |
| Human utility | Preselected primary hypothesis, baseline(s), quality improvement or non-inferiority margin, and acceptable active/elapsed burden |
| Repeatability and resources | Repetition/selection policy, tolerable substantive instability and failure, measured capacity/latency/resource envelope |
| Protection | Applicable RA-08 control/readiness evidence and invariant outcomes, separate from model performance |

The set must permit a meaningful negative result: the local model may qualify only for explanation, the hybrid may fail to improve review, or the hardware envelope may be too small for useful semantic work. Retain safe deterministic-only capability without presenting it as proof that the hybrid hypothesis succeeded.

### 7.2 Mandatory boundaries cannot be averaged away

Acceptance cannot waive the supplied-data-only boundary, human authority, source immutability, approved task permission, required evidence for deterministic findings, prohibited approval/ISTQB claims, or RA-08's protection policy in exchange for better mean recall or speed. A confirmed violation fails the affected applicable criterion and triggers the relevant impact/containment decision.

Probabilistic semantic quality is measured under explicit risk-based criteria; this does not authorize knowingly promoting unsupported conclusions. A model's unsafe raw proposal that the product successfully withholds is distinguished from an unsafe supported result or unauthorized effect. Report component behavior and end-to-end containment separately; protected processing itself must also remain permitted.

For sealed operation, successful external runtime egress violates the accepted policy even if no protected marker is recognized. Zero observed markers with an invalid observer establishes no pass. Follow RA-08's synthetic pre-confidential verification, deployment/copy coverage and ROLE-09 decision. A laboratory-only acceptance claim cannot be labelled sealed-ready, and does not remove the outstanding requirements for later protected use.

### 7.3 Evaluation result vocabulary

These states belong to evaluation criteria/campaigns, not operational run state, finding disposition or RA-07 qualification state.

| Result | Meaning |
| --- | --- |
| PASS | The applicable frozen criterion is met with sufficient valid evidence for its explicit claim and envelope |
| FAIL | Valid evidence demonstrates failure of an applicable frozen criterion or mandatory invariant |
| INCONCLUSIVE | Execution or evidence exists, but missing observations, unresolved oracle, inadequate sample/category coverage, invalid measurement or insufficient uncertainty resolution prevents the decision |
| NOT_EVALUATED | No decision-bearing evaluation was conducted for the stated criterion; exploratory results may exist separately |
| NOT_APPLICABLE | A justified predeclared applicability condition excludes this criterion from this particular claim; the exclusion cannot establish a broader claim |

For an overall campaign, any failed applicable mandatory criterion prevents PASS; preserve other inconclusive or unperformed criteria alongside that failure. With no failure, a required inconclusive or unperformed criterion still prevents PASS. Only sufficient passing evidence for every applicable mandatory criterion can support the bounded campaign PASS. At least one substantive applicable criterion must exist: declaring every criterion NOT_APPLICABLE establishes no evaluated capability. A wholly unexecuted campaign is NOT_EVALUATED.

The report retains purpose, exact versions/configuration, dataset/oracle lineage and exposure, all scheduled/attempted/completed/failed/excluded units, adjudication and matching records, metrics by required slice, uncertainty, protocol deviations, criterion outcomes, known limitations, residual risks and authorized decisions. An unsuccessful experiment remains a reportable result.

ROLE-08 separately maps qualification evidence into RA-07's permission lifecycle. ROLE-09 separately decides protected-data authorization. ROLE-10 separately records project acceptance or an SDLC gate; a campaign PASS cannot approve itself, approve the user's testware, or open a phase.

### 7.4 Change and reevaluation

Behavior-affecting changes follow RA-07 impact analysis and applicable requalification; security-relevant changes follow RA-08. Select affected regression evidence based on impact rather than rerunning everything without cause. Package changes and changed assessment behavior retain RA-03/RA-05 identities and do not overwrite earlier runs.

After inspecting held-out results, a revised prompt, mapper, rule, model, output filter or threshold cannot inherit an unchanged unbiased acceptance claim. Preserve the failed/exposed campaign, identify the change and use fresh held-out evidence for the new claim. Predeclared retries within an unchanged approved policy remain attempts of that policy, not silent tuning. Oracle-only corrections preserve their before/after effects and all affected comparator results; they do not erase evidence of exposure.

## 8. Traceability, inherited observations, and STLC allocation

### 8.1 Controlled bridge for RA03-VAL-014

The table links RA03-VAL-014 through each existing input-sufficiency rule to its supporting accepted requirements. It addresses `SR-RA03-OBS-001`, which required a direct requirement reference or an inspected chain before validation obligations become executable tests. The Owner accepted the bridge and, separately, the two source-table corrections and VAL-015 refinement on 2026-09-21; [SR-RA10-001 v0.2][review10] records that sequence and closes the targeted observation.

| Existing obligation | Controlled intermediate rule | Accepted RA-03 requirements supporting the rule's consequence |
| --- | --- | --- |
| RA03-VAL-014 | IS-01 — prohibited capture path | RA03-REQ-031, RA03-REQ-040, RA03-REQ-042 |
| RA03-VAL-014 | IS-02 — untrustworthy inventory/capture | RA03-REQ-003, RA03-REQ-007, RA03-REQ-009, RA03-REQ-031, RA03-REQ-040 |
| RA03-VAL-014 | IS-03 — missing scope minimum | RA03-REQ-008, RA03-REQ-033, RA03-REQ-040 |
| RA03-VAL-014 | IS-04 — missing substantive addressable basis | RA03-REQ-005, RA03-REQ-010, RA03-REQ-019, RA03-REQ-033, RA03-REQ-040 |
| RA03-VAL-014 | IS-05 — no recognizable TC | RA03-REQ-011, RA03-REQ-022, RA03-REQ-033, RA03-REQ-040 |
| RA03-VAL-014 | IS-06 — no qualifying accountable origin | RA03-REQ-011, RA03-REQ-021, RA03-REQ-033, RA03-REQ-040 |
| RA03-VAL-014 | IS-07 — insufficient provenance | RA03-REQ-020, RA03-REQ-026, RA03-REQ-029, RA03-REQ-038 |
| RA03-VAL-014 | IS-08 — basis conflict with no supported subset | RA03-REQ-035, RA03-REQ-040 |
| RA03-VAL-014 | IS-09 — conflict with an isolatable supported subset | RA03-REQ-035, RA03-REQ-038, RA03-REQ-041 |
| RA03-VAL-014 | IS-10 — missing conditional evidence | RA03-REQ-031, RA03-REQ-034, RA03-REQ-038, RA03-REQ-041 |
| RA03-VAL-014 | IS-11 — minimum and conditional evidence permit bounded assessment | RA03-REQ-031, RA03-REQ-032, RA03-REQ-041, RA03-REQ-050 |

The bridge retains 41 rule/requirement links to 23 accepted RA-03 requirements. In [RA-03 v0.4 §15.3][ra03], CR-RA10-001 makes G identify a relevant conflict while X distinguishes whether an unaffected supported subset exists. CR-RA10-002 removes X as an additional precondition for conflict-free IS-10/IS-11. Missing conditional evidence limits dependent assessments without erasing satisfied package minima, including when no independent substantive work remains. RA-05 determines actual ledger outcomes, terminal availability and run state.

VAL-015 requires these distinctions to be challenged. The existing review retains the source comparison, counterexamples, table-logic check and inverse bridge. These are document-level checks; links and Boolean coverage alone do not establish adequate executable tests or implemented behavior. The targeted observation is closed, while the general trace obligation remains. The earlier RA-03 v0.3 history is preserved and is not retrospectively claimed to have direct requirement links for all 32 validation obligations.

### 8.2 Phase-wide readiness and proportionality

The [consolidated Requirements Analysis record][phase] contains the accepted inventory of 249 requirements and 169 validation obligations, the phase-wide trace review, remaining allocations and resource-risk assessment. The Owner accepted that review and closed the phase on 2026-09-22. Inventory and trace counts describe the requirements documents; they do not establish implementation or executed coverage.

The continuing trace rule is to inspect both directions: every accepted requirement needs a justified validation route, and every validation obligation must reach existing accepted requirements directly or through inspected intermediates. Preserve the relevant source versions and decisions, inspect gaps and conflicting allocations, and assign unresolved design/test work to an owner and prerequisite milestone. Do not invent links to reach a coverage percentage.

`SR-RA03-OBS-002` / R-08 remains active. Maintain these rules and the existing review records instead of producing parallel status documents or copying complete test specifications. Planning must account for benchmark construction, human adjudication, implementation and verification against available capacity. Accepted requirements alone do not establish an estimable backlog or a realistic schedule. The current cleanup and pause are described in [README.md](../../../README.md).

### 8.3 Allocation to later work

| Work product / decision | Next responsible work and prerequisite |
| --- | --- |
| Executable schemas, importer/exporter, evaluation evidence storage, measured resource limits and architecture controls | Solution and Architecture Design after its explicit GO; preserve RA-09 and RA-08 contracts |
| Reference-family content, human oracle, mutation ledger, partition manifest and test conditions | Test analysis/design using approved requirements; ROLE-04 interpretation and ROLE-08 evaluation governance |
| Exploratory baseline measurements | Authorized laboratory work on eligible material after the required design/implementation permissions; results labelled exploratory |
| Actual numerical criteria, sample plan, repetitions, uncertainty method and comparison margins | Controlled criteria record owned by ROLE-08 for qualification and endorsed for product acceptance by ROLE-10; mandatory before corresponding decision-bearing runs |
| Executable controls, integration, fault, security and workflow tests | Test implementation/execution in the relevant increments; trace to accepted VAL/REQ and record actual results |
| Task qualification and human utility study | Approved protocol, eligible data, fixed versions and applicable qualification/human-study conditions before reliance claims |
| Sealed readiness and protected-data authorization | RA-08 verification on eligible fixtures and explicit ROLE-09 decision before the first confidential input |
| Product acceptance and pilot decision | Consolidated STLC completion evidence and explicit applicable human gates; no inference from requirements acceptance |

These allocations retain their applicable evidence and authorization prerequisites; the historical design-entry decision is recorded in [SR-RA-001 v0.2][phase]. Actual numerical criteria must follow exploratory measurements and precede the corresponding decision-bearing campaigns. Acceptance of this evaluation contract supplies neither those measurements nor confirmation of the product hypothesis.

## 9. Accepted requirements and forward trace

All 22 requirements are **MUST / ACCEPTED** by the Owner's 2026-09-21 decision. Their statements, upstream references and direct validation links remain unchanged. `VAL-xxx` means `RA10-VAL-xxx` in Section 10. Supporting sections define the conditions; this register does not itself require an automatic evaluator, model judge, dashboard or database. The bridge called “proposed” in the retained REQ-020 wording is now accepted as recorded in Section 8.1.

| ID | Requirement statement | Primary upstream basis | Direct validation |
| --- | --- | --- | --- |
| RA10-REQ-001 | Every decision-bearing evaluation shall identify its purpose, claim, frozen protocol, dataset/oracle, actual configuration and operating conditions, retaining the complete attributable execution inventory under Sections 2, 6 and 7. | Charter §16; RA07-REQ-008, RA07-REQ-018 | VAL-001, VAL-008, VAL-010, VAL-016 |
| RA10-REQ-002 | The evaluation process shall separate development, qualification and held-out acceptance by declared purpose and related family, record exposure, and prevent exposed or related evidence from supporting a misleading independent-acceptance claim. | Charter §16.2; RA07-REQ-011 | VAL-002 |
| RA10-REQ-003 | Each campaign shall define and account for the category and interaction coverage needed for its claimed envelope, including relevant positive, negative, ambiguous, mixed, resource and failure conditions from Section 3.3. | Charter §16.2–16.3; RA03-REQ-023; RA07-REQ-013 | VAL-003, VAL-012 |
| RA10-REQ-004 | Reference packages and mutations shall retain the Section 4.1 evidence and verified effect, distinguish required detectable issues from optional improvements, and preserve oracle versions and corrections without inventing supplied business evidence. | Charter §16.3; RA06-REQ-017; RA07-REQ-012 | VAL-002, VAL-004 |
| RA10-REQ-005 | Semantic oracle decisions shall follow attributable human adjudication, preserve unresolved disagreement and independence limitations, and remain distinct from operational dispositions, model agreement and human repair. | Charter §16.4; RA01-REQ-010, RA01-REQ-013; RA05-REQ-010 | VAL-004, VAL-009 |
| RA10-REQ-006 | Scoring shall use predefined atomic claim and matching rules, prevent duplicate detection credit, retain invalid extra assertions and novelty, and preserve original TC and product-record identities under Section 4.3. | RA03-REQ-048; RA05-REQ-005; RA06-REQ-007 | VAL-004, VAL-005 |
| RA10-REQ-007 | Evaluation reports shall implement Section 5's metric definitions and denominator rules, expose raw counts, unresolved and missing evidence, undefined values and applicable uncertainty, and prevent omissions or aggregation from inflating the claimed result. | Charter §16.6; RA07-REQ-013 | VAL-005, VAL-006, VAL-014 |
| RA10-REQ-008 | Evaluation shall distinguish supported assessment, evidence-based abstention, scope/capability/policy non-performance and interruption, and measure excessive abstention and false zero-issue claims without treating empty output as completed review. | RA05-REQ-003, RA05-REQ-004, RA05-REQ-005; RA07-REQ-006 | VAL-006, VAL-013 |
| RA10-REQ-009 | Evaluation shall assess evidence-reference validity, semantic support and derivation separately, and shall not count a citation, deterministic calculation or human disposition as confirmation of an unsupported premise. | RA05-REQ-006, RA05-REQ-007; RA06-REQ-016; RA07-REQ-004 | VAL-007 |
| RA10-REQ-010 | Decision-bearing reports shall expose outcomes by required task and category, enforce predeclared sufficiency and slice criteria, and prevent a successful aggregate or different capability from conferring qualification on failed or unmeasured use. | RA07-REQ-012, RA07-REQ-013, RA07-REQ-019 | VAL-003, VAL-006, VAL-012, VAL-014 |
| RA10-REQ-011 | Comparative evaluation shall include the relevant simpler baselines and actual proposed composition, disclose unequal premises, preparation and omitted comparisons, and retain mandatory controls in an LLM-only comparison under Section 6.1. | Charter §16.5, §16.7; RA07-REQ-002, RA07-REQ-019 | VAL-008 |
| RA10-REQ-012 | Human-benefit evaluation shall compare supported review outcomes and total declared workflow burden under a previously chosen hypothesis, record exposure and competence limitations, and include incorrect suggestions, failures and negative assistance. | Charter §16.6–16.7, §18.2; RA01-REQ-013 | VAL-009 |
| RA10-REQ-013 | Repeated evaluation shall use a predefined bounded retry/selection policy, retain required attempt and failure attribution, measure substantive variability and actual policy cost, and prohibit undisclosed best-answer selection. | RA07-REQ-012, RA07-REQ-014, RA07-REQ-019 | VAL-010, VAL-012 |
| RA10-REQ-014 | Deterministic reproducibility and metamorphic evaluation shall identify fixed premises, behavior and justified relations, distinguish substantive results from incidental metadata, and avoid assuming semantic equivalence or correctness from repetition alone. | RA06-REQ-015, RA06-REQ-016; RA07-REQ-013 | VAL-011 |
| RA10-REQ-015 | Resource-feasibility evidence shall measure the intended configuration and machine, expose its supported task/package envelope and Section 5's resource/failure observations, and prevent unmeasured hardware or capacity claims. | Charter §18.1; RA07-REQ-008, RA07-REQ-019 | VAL-012 |
| RA10-REQ-016 | Applicable safety, evidence and authority invariants shall be evaluated independently from average quality, with valid observation and separate component-proposal versus end-to-end outcomes; violations or missing readiness evidence shall not be traded for performance. | Charter §16.7; RA07-REQ-002; RA08-REQ-023, RA08-REQ-024 | VAL-007, VAL-013 |
| RA10-REQ-017 | Numerical criteria, comparison margins, sufficiency, uncertainty and stopping rules shall be proposed from exploratory evidence and approved before applicable decision-bearing execution, with any later change versioned and its acceptance consequences disclosed. | Charter §16.7; RA07-REQ-012 | VAL-001, VAL-008, VAL-014 |
| RA10-REQ-018 | Evaluation shall apply Section 7.3's result meanings and complete reporting boundary, preserve negative and inconclusive evidence, and keep campaign results separate from human qualification, protected-data authorization and project acceptance/gates. | RA01-REQ-010, RA01-REQ-011; RA07-REQ-009; RA08-REQ-001 | VAL-001, VAL-013, VAL-014, VAL-016 |
| RA10-REQ-019 | Behavior, protocol, oracle or exposure changes shall retain their impact and history under Section 7.4, trigger applicable reevaluation/requalification, and prevent tuning against exposed acceptance data from inheriting an unbiased new claim. | RA03-REQ-044, RA03-REQ-045; RA07-REQ-011, RA07-REQ-015; RA08-REQ-022 | VAL-001, VAL-002, VAL-010, VAL-011 |
| RA10-REQ-020 | Requirements-phase closure shall verify both requirement-to-validation and validation-to-accepted-requirement routes, directly or through controlled intermediates, including the proposed Section 8.1 bridge and explicit disposition of inherited observations. | PG-RA03-001 §4; SR-RA03-OBS-001 | VAL-015 |
| RA10-REQ-021 | RA-10 closure and Requirements Analysis exit shall retain separate evidence and explicit Owner authority, allocate remaining mandatory criteria/design/STLC work and resource assessment, and shall not imply implementation, product acceptance or deployment permission. | Charter §18.6, §20; RA01 AUTH-14; PG-RA09-001 | VAL-015 |
| RA10-REQ-022 | Evaluation artifacts and reports shall retain attributable, policy-permitted evidence with visible unavailability, enforce laboratory eligibility and protected-data restrictions, and control oracle/held-out exposure without public disclosure of unapproved material. | RA05-REQ-016, RA05-REQ-020; RA07-REQ-018; RA08-REQ-003, RA08-REQ-014, RA08-REQ-016 | VAL-002, VAL-013, VAL-016 |

## 10. Validation obligations and reverse trace

All 16 obligations are accepted, including the VAL-015 refinement separately endorsed on 2026-09-21 in [SR-RA10-001 v0.2][review10]. The rows and direct targets below are unchanged from that accepted baseline. They guide static review, later test design and empirical work; they are not executed tests or a requirement for one executable test per requirement. `REQ-xxx` means `RA10-REQ-xxx`.

| ID | Required validation evidence | Direct requirements |
| --- | --- | --- |
| RA10-VAL-001 | Inspect an exploratory record, a properly frozen campaign and one whose threshold/configuration changes after results are seen. Verify exact identity, approval timing, retained earlier results and absence of inherited qualification or acceptance. | REQ-001, REQ-017, REQ-018, REQ-019 |
| RA10-VAL-002 | Trace parent/mutant, renamed, paraphrased and translated families across partitions; inspect prior exposure, public publication, access and oracle corrections. Verify no misleading held-out claim, no hidden product adaptation, and equivalent rescoring of affected variants. | REQ-002, REQ-004, REQ-019, REQ-022 |
| RA10-VAL-003 | Inspect category/envelope coverage, including mixed classification axes, inapplicable techniques, supported automated system TC and unsupported AI-system targets. Show that missing required categories or success only on an easier task prevents the broader claim. | REQ-003, REQ-010 |
| RA10-VAL-004 | Challenge an ineffective mutation, missing optional direct trace, evaluator disagreement, a resolved oracle expecting abstention, valid new discovery, and operational acceptance of an incorrect suggestion. Verify human authority, evidence, versioned corrections and separate truth/disposition meanings. | REQ-004, REQ-005, REQ-006 |
| RA10-VAL-005 | Use a small independently countable scoring fixture containing duplicates, several claims in one item, a valid observation plus an invented consequence, optional advice, unanticipated valid findings, zero denominators and unresolved labels. Verify precision, recall, unsupported-assertion counts and unchanged identities. | REQ-006, REQ-007 |
| RA10-VAL-006 | Contrast a valid zero-issue conclusion, missed known issues, all-abstain output, missing business evidence, unavailable capability and interrupted work. Verify cause-specific outcomes, denominators, false-clean behavior and no inflated score from excluding hard opportunities. | REQ-007, REQ-008, REQ-010 |
| RA10-VAL-007 | Contrast nonexistent, wrong-version and real-but-irrelevant citations; deterministic arithmetic over an invented premise; and a rejected unsafe raw proposal versus a promoted unsupported conclusion. Verify structural, semantic, derivation and applicable invariant judgments remain separate. | REQ-009, REQ-016 |
| RA10-VAL-008 | Inspect deterministic, semantic and hybrid comparison protocols, unequal confirmed premises, preparation costs and missing comparators. Verify protective controls remain active, the prechosen hypothesis/criteria are used, and conclusions do not overattribute human benefit to the LLM. | REQ-001, REQ-011, REQ-017 |
| RA10-VAL-009 | Walk through matched human sessions with order/exposure differences, solo self-review, pending dispositions, accepted incorrect suggestions, duplicate dismissal and separately timed repair. Verify complete effort/quality observations, truthful independence labels and no disposition-as-oracle shortcut. | REQ-005, REQ-012 |
| RA10-VAL-010 | Inspect all planned repetitions and actual attempts, including failed first calls, predeclared retry variants, best-of-many selection and an edited prompt. Verify policy cost, variation reporting, immutable histories and the correct new-configuration consequences. | REQ-001, REQ-013, REQ-019 |
| RA10-VAL-011 | Compare substantive deterministic results with differing run metadata; challenge a stochastic upstream premise and unjustified paraphrase/reordering relation. Verify justified metamorphic expectations, recorded counterexamples and impact-based reevaluation. | REQ-014, REQ-019 |
| RA10-VAL-012 | Inspect measurements on the actual target hardware across the claimed workload envelope, including cold/warm operation, limits, timeout, resource exhaustion and recovery. Verify failures remain counted, retries retain cost, and evidence on another machine or easier category cannot establish target feasibility. | REQ-003, REQ-010, REQ-013, REQ-015 |
| RA10-VAL-013 | Use eligible synthetic fixtures for denied authority, forbidden source retrieval, model self-approval, protected-copy paths, blocked egress, successful forbidden transfer and observer failure. Verify invariant failure or inconclusive evidence is not offset by semantic quality or called ordinary business ungradability; keep ROLE-08/09/10 decisions separate. | REQ-008, REQ-016, REQ-018, REQ-022 |
| RA10-VAL-014 | Challenge zero sample, insufficient families, unresolved oracle, a failed mandatory slice hidden by an aggregate, post-result weights, incomplete criteria and invalid uncertainty assumptions. Verify predeclared sufficiency/decision rules and PASS/FAIL/INCONCLUSIVE/NOT_EVALUATED applicability without invented numeric thresholds. | REQ-007, REQ-010, REQ-017, REQ-018 |
| RA10-VAL-015 | Inspect both directions of local trace and phase-wide direct/intermediate routes. Verify all IS-01–IS-11 bridge targets against the effective RA-03 wording and endorsement of any source-table amendment. Challenge local versus global conflict; no-conflict inputs with missing conditional evidence both with and without supported independent work; and the absence of an extra X prerequisite when conditional evidence exists. Verify package minimum, actual ledger outcome, terminal availability and run state remain distinct. Record inherited-observation dispositions, allocated outstanding work and Owner phase authority. A local 22/22 result or Boolean table check must not be presented as completed phase-wide validation. | REQ-020, REQ-021 |
| RA10-VAL-016 | Reconstruct a campaign report from retained authorized records, including failures, exclusions, unavailable evidence and protected actor metadata. Verify exact versions, cutoff, criterion outcomes, data policy, no invented history and no unintended publication of hidden oracle or protected material. | REQ-001, REQ-018, REQ-022 |

## 11. Accepted policy decisions

The Owner accepted all four recommendations on 2026-09-21. Their original wording is preserved below; no original policy decision remains open. They define evaluation policy, not measured performance, numerical thresholds or new runtime capabilities.

| ID | Decision | Recommendation and consequence |
| --- | --- | --- |
| OD-RA10-001 | How broad should the first empirical campaign be? | Start with small, fully adjudicated customer-creation families and relevant negative/boundary categories. Use the discussed discount case as exposed development material. Add independent families and later domains only as the intended claims require; permit an explicitly limited exploratory result if credible partitions or resources are not yet available. |
| OD-RA10-002 | How should substantive output be scored? | Use atomic evidence-backed claims and distinct expected-issue matching under Section 4.3. Separate optional advice, duplicates, unanticipated discoveries and unresolved judgments; retain both valid and invalid assertions within a mixed output item. Do not use an LLM-as-judge or operational acceptance as the final oracle. |
| OD-RA10-003 | What should constitute useful assistance? | Prefer a predeclared quality-improvement hypothesis with an acceptable burden limit. Measure human review as well as machine output, and include the deterministic-assistance comparison when claiming incremental human benefit from the LLM. Set actual margins after exploration, before decision-bearing evaluation. |
| OD-RA10-004 | Does finishing the final RA slice automatically open design? | No. Close RA-10 through the established focused review, then consolidate phase-wide readiness, traceability, remaining allocations and resource/scope risks in one review/gate record. Obtain explicit GO to Solution and Architecture Design; retain later implementation, acceptance and sealed-use gates. |

These decisions retain the supplied-data boundary, human accountability, sealed egress rule, authorized task catalogue and MVP exclusions.

## 12. Review verification, remaining prerequisites, and exit

### 12.1 Recorded review and correction checks

[SR-RA10-001 v0.2][review10] records the completed focused review and separately endorsed corrections. `SR-RA10-F-001` and `SR-RA10-F-002` are closed. Their counterexamples and verification explain the corrected input-sufficiency rules in Section 8.1; the review also retains the original source identities, arithmetic and reference checks.

The historical local trace check found 22/22 requirements with direct validation links, 16/16 obligations with valid targets and 47 matching links in both directions. The inherited bridge retains 11 rules, 41 links and 23 target requirements. The Owner completed the walkthrough; the same assistant authored the documents and later performed the focused review. These are document checks, with no independent expert review or product/model experiment claimed. The later [phase review][phase] records the broader trace and readiness inspection separately.

### 12.2 Mandatory open prerequisites

Before a decision-bearing campaign, its approved corpus and oracle, family counts and partitions, reviewer availability, target configuration, measurement tools, repetitions, uncertainty method and numerical criteria must be specified and evidenced. Section 8.3 assigns the responsible authorities and prerequisite milestones. Requirements acceptance cannot supply missing people, values, executable tests or empirical results.

The targeted RA03-VAL-014 bridge action and Requirements Analysis review are closed. General trace duties and the documentation-growth risk remain. Subsequent test design, execution, model qualification, protected-use verification and product acceptance require their own evidence and applicable decisions. [README.md](../../../README.md) distinguishes the available foundation and prepared test data from the still-unproven product usefulness.

### 12.3 Exit and next action

The Owner accepted RA-10 v0.1 on 2026-09-21. A separate decision that day endorsed CR-RA10-001/002, the VAL-015 refinement and review, designated RA-10 v0.2 and corrected RA-03 v0.4, and closed RA-10 and the targeted `SR-RA03-OBS-001` action. [SR-RA10-001 v0.2][review10], dated 2026-09-22, records those decisions.

On 2026-09-22 the Owner separately accepted consolidated traceability, downstream allocations and the design-entry resource/risk assessment, closed Requirements Analysis and granted GO to Solution and Architecture Design in [SR-RA-001 v0.2][phase]. These historical decisions need no repeated approval. Neither requirements acceptance nor that design gate authorized product implementation, operational model reliance or confidential input. Product feasibility, model qualification and product acceptance require their own evidence and decisions.

Development is currently paused for the documentation cleanup described in [README.md](../../../README.md). The historical design GO does not override that pause; resuming development requires the Owner's explicit decision.

The original v0.1 review input and v0.2 corrected baseline remain in Git history. The existing [focused review][review10] and [phase record][phase] retain their identities, verified differences and separate Owner decisions. This maintained text incorporates those decisions without creating another document version or changing the accepted evaluation contract.

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
[gate09]: ../ra-09/test-design-gatekeeper-ra-09-focused-static-review-v0.2.md
[review10]: test-design-gatekeeper-ra-10-focused-static-review-v0.2.md
[phase]: test-design-gatekeeper-requirements-analysis-readiness-v0.2.md
[ir-metrics]: https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-of-unranked-retrieval-sets-1.html
[nist-proportions]: https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm
[original]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/1969b646753696111a71032c88f46790c62f4b4e/docs/requirements-analysis/ra-10/test-design-gatekeeper-ra-10-evaluation-acceptance-v0.2.md
