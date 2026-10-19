# Context

A glossary for Test Design Gatekeeper (TDG). These terms describe the intended product as well as the implemented foundation; see [README.md](README.md) for what currently works.

Definitions here are short explanations. The linked requirements and accepted design govern detailed behavior. The [requirements acceptance record][baseline] identifies the accepted baseline; some source documents still carry older preparation-time labels. Agent workflow belongs in [AGENTS.md](AGENTS.md), and historical reasoning in [LEARNINGS.md](LEARNINGS.md).

## Product and project

| Term | Meaning |
| --- | --- |
| **Test Design Gatekeeper (TDG)** | An assistant for human review of functional test cases against deliberately supplied evidence, informed by ISTQB methods. It does not approve testware or certify completeness. |
| **MVP** | The intended first product: review of system-level functional black-box tests for one feature or small process. The initial techniques are equivalence partitioning, boundary-value analysis, decision tables and state transitions, where applicable. |
| **increment** | An authorized portion of implementation and verification. |
| **work item** | A smaller deliverable within an increment, with a defined scope and completion conditions. |
| **I-01** | The first increment, covering local intake/capture and foundation controls before substantive test-design review. |

Scope and design: [Project Charter][charter] and [SAD-04][sad04].

## Supplied material and capture

| Term | Meaning |
| --- | --- |
| **Review Package** | The scope, test basis, test cases and provenance deliberately supplied for one feature or small process. A human controls its boundary. |
| **Review Package candidate** | Material submitted for intake before a trusted, immutable package version exists; capture may be refused. |
| **submission context** | Trusted operation information outside the supplied content: operator, acting role, profile, approved classification/purpose, input bindings, operation identity and requested action. |
| **package snapshot** | The captured sources, declarations, structured view, provenance, metadata and visible deficiencies for one package version. |
| **source artifact** | One supplied source or retained attachment, with its locator, representation, capture outcome and available integrity evidence. |
| **source locator** | A reference to a location within a supplied source, such as a JSON pointer or CSV record/field. It identifies evidence, not authority. |
| **provenance** | Where information came from: supplied content or declarations, system observations, human confirmations or derived interpretation. |
| **external reference** | A supplied URL, issue key, path or filename. Its value alone does not supply the referenced content. |
| **external discovery** | Retrieving or searching for material outside the deliberately supplied package; outside the MVP review workflow. |
| **capture/import transformation** | Identified parsing or mechanical mapping into captured content. Recapture with a changed mapping creates a new package version, even if logical values stay unchanged. |
| **assessment mapping** | Versioned rules for interpreting already captured content. Changing these rules for reassessment creates a new run on the same package version. |
| **canonical content** | Retained source content, field presence, declarations, provenance and visible gaps/conflicts. Assessment results do not rewrite it. |
| **mechanical projection** | A structured view of captured material that adds no inferred business meaning and does not replace the original source. |

Capture, preservation and mapping rules: [RA-09][ra09].

## Native JSON documents

| Term | Meaning |
| --- | --- |
| **control envelope** | The outer JSON object identifying the document type and contract version and carrying its content. RA-09 defines its exact structure and validation rules. |
| **`review_package_input`** | Supplied declarations and a content manifest; it grants no trusted identity, permissions or human approval. |
| **`review_package_snapshot`** | TDG's captured package representation, without substantive assessment conclusions. |
| **`import_receipt`** | The intake outcome and issues. It references a package only after durable capture; capture does not establish review readiness. |
| **`review_export`** | A read-only selection of retained results, context, evidence references and human history; not a mechanism for restoring trusted history. |

Exact fields and document contracts: [RA-09 §2][ra09-kinds]. These are logical document types, not four mandatory files per operation.

## Testware and accountability

| Term | Meaning |
| --- | --- |
| **TC** | Test case. TDG retains the supplied case and its deficiencies; source editing remains with the human owner. |
| **test basis** | Supplied evidence used to review testware, such as requirements, business rules, risks, prior defects or attributable experience-based reasoning. |
| **basis element** | One identifiable item of supplied test-basis content. A link alone is not that content. |
| **human accountability** | An identified human accepts responsibility for the submitted testware and its use. |
| **origin** | The declared authorship category, distinct from human accountability. RA-09 defines the canonical values and their mapping from source declarations. |
| **human-controlled AI-assisted testware** | AI-assisted testware adopted and controlled by an identified accountable human. Writing style cannot establish this status. |

Declaration and mapping rules: [RA-09 §4.2][ra09-origin].

## Human roles

Roles describe responsibilities, not job titles. One person may hold several roles with an explicit acting-role context; this does not create independent review. Operating or administering TDG does not grant other decision authorities.

The full catalogue, **ROLE-01 through ROLE-10**, and its decision-authority matrix are maintained in [RA-01 §§7–9][ra01]. For example, confirming a basis interpretation (ROLE-04), deciding on a finding (ROLE-05) and approving testware (ROLE-06) are separate decisions. TDG cannot assume these human roles.

## Review and assessment

| Term | Meaning |
| --- | --- |
| **review request** | A deliberate request to assess one exact package version under identified behavior/configuration and requested dimensions. |
| **assessment run** | One execution of that assessment. A new run has a new identity; a terminal run does not resume. |
| **review cycle** | Submission, qualification, assessment, human inspection/disposition, optional external repair and re-review. |
| **re-review** | A later assessment of a new package version, or unchanged captured content under identified changed assessment behavior. |
| **assessment scope** | The package items and review dimensions supported in an identified run. |
| **supported subset** | The assessable portion of supplied items/dimensions. Excluded or unsupported material remains visible. |
| **substantive assessment** | Review of test-design quality or coverage once prerequisites permit it. Intake diagnostics and scope classification are separate activities. |
| **review result** | Findings, suggestions, limitations, evidence and run metadata for what was actually assessed. |
| **assessment ledger** | A record of requested checks for recognizable items, their prerequisites, outcomes and reasons for work not done. |
| **ledger entry** | One item/dimension in that record, linking prerequisites, attempts, evidence and outcome. |
| **item eligibility** | Whether an item meets recognizability and accountable human-control conditions. |
| **domain qualification** | Whether an item fits the supported domain. An unknown answer (`UNDETERMINED`) differs from proven exclusion (`OUT_OF_SCOPE`); `NOT_EVALUATED` means no qualification attempt. |
| **evidence sufficiency** | Whether supplied evidence supports a particular conclusion. Different dimensions of one case can have different answers. |

Lifecycle and records: [RA-05][ra05]. Supported-domain criteria: [RA-04][ra04].

## Four different kinds of status

| Concept | Question answered | Example |
| --- | --- | --- |
| **operational run state** | What happened to processing? | `COMPLETED`: processing ended normally, with an outcome recorded for every requested entry. |
| **assessment outcome** | What happened to this particular check? | `UNGRADABLE`: necessary evidence is missing or conflicting. |
| **result availability** | How much substantive assessment is safely available? | `NONE`: the run is terminal, with no completed substantive entry safely available. |
| **human disposition** | What did ROLE-05 decide about a finding or suggestion? | `ACCEPTED`: the item is regarded as justified in its stated context. |

For example, `COMPLETED` with `NONE` can mean processing ended normally but all requested substantive assessments lacked necessary evidence. It does not mean the test cases passed review. The complete status lists, transitions and calculation rules are maintained in [RA-05 §3][ra05-status]; finding dispositions are in [§5.2][ra05-dispositions].

## Findings, suggestions and evidence

| Term | Meaning |
| --- | --- |
| **review item** | A reported claim, question or recommendation tied to an identified subject and evidence. |
| **finding** | A claim about supplied testware or its basis, with evidence, derivation, subject and history. |
| **suggestion** | An inspectable proposal or interpretation that may need human judgment. |
| **derivation** | How an item was produced: `DETERMINISTIC` or `LLM_ASSISTED`, independently of its human disposition. |
| **deterministic finding** | A reproducible result from identified input, confirmed premises, rules and configuration. Reproducibility does not establish source truth. |
| **LLM-assisted suggestion** | An evidence-grounded, probabilistic contribution under a qualified task/configuration; uncertain and rejectable. |
| **evidence item** | An inspectable basis for a claim, such as a source location, check, model-attempt reference or attributable human interpretation. |
| **human disposition** | ROLE-05's attributable decision on one finding/suggestion. It does not replace original evidence or change derivation. |

Item content and human decision history: [RA-05][ra05].

## Identity, history and retries

| Term | Meaning |
| --- | --- |
| **package identity** | The identity of a package lineage across revisions, distinct from one package version. |
| **package version** | An immutable identity for the captured content and its capture mapping. A content-changing recapture creates a distinct version. |
| **TDG-generated identity** | An opaque internal ID for a TDG record, without mutable business meaning. |
| **source identity** | An identifier supplied by a source, preserved separately from TDG's internal IDs. |
| **lineage** | Recorded relationships between versions/events; corrections create attributable records rather than overwriting history. |
| **operation identity** | Identifies a durable operation/request context and distinguishes its retry from a new operation. |
| **request fingerprint** | Identifies the relevant request content/configuration for retry comparison. A changed fingerprint is not the same request. |
| **idempotent retry** | Repeating the same authorized, identified operation without duplicating its committed effect. Independent submissions are not merged merely because their bytes match. |
| **immutable history** | Earlier package versions, runs, findings, interpretations and human events retain their meaning; corrections add linked records. |

Identity and version rules: [RA-09][ra09]. Persistence and retry behavior: [RA-05][ra05].

## Models and qualification

| Term | Meaning |
| --- | --- |
| **deterministic control** | A reproducible check using identified input, confirmed premises and versioned rules; incorrect premises can still produce incorrect conclusions. |
| **model contribution** | A bounded probabilistic proposal from an identified model/runtime/task configuration, subject to structural and policy checks. |
| **model gateway** | The control point for permitted model calls: task authorization, context selection, limits, provenance, response validation and safe failure. |
| **context projection** | The explicitly allowed subset of retained evidence given to one model task. The model cannot expand it by searching or following references. |
| **qualification** | An attributable decision permitting an identified behavior configuration for a defined task, profile and resource boundary; not blanket trust in a model name. |
| **candidate contribution** | A model proposal retained after structural/reference validation, awaiting further interpretation; not automatically an assessment result or human decision. |
| **abstention** | Withholding a conclusion because evidence, capability or qualification is insufficient. This can be correct behavior. |

Model tasks, evaluation access and operational permission: [RA-07][ra07]. Model output remains untrusted, and the runtime gains no filesystem, policy, record-store or human-decision authority.

## Evaluation

| Term | Meaning |
| --- | --- |
| **human oracle** | A human-adjudicated reference for evaluating a defined claim or behavior. Model agreement is not a substitute. |
| **development corpus** | Material used to build, tune or debug behavior; not independent acceptance evidence. |
| **qualification corpus** | Material used under a predefined protocol to decide whether a frozen candidate/configuration is permitted for a defined role. |
| **held-out acceptance corpus** | Material reserved from tuning for product acceptance under an approved protocol. Once exposed, it is not fresh held-out evidence for an adapted candidate. |
| **reference family** | Related controlled examples with known relationships and human-reviewed expected meanings. |
| **mutation** | A deliberate change intended to introduce a known issue or challenge; its actual effect on the expected result must be checked. |

Evaluation procedures and evidence limits: [RA-10][ra10].

## Operating profiles and protection

| Term | Meaning |
| --- | --- |
| **laboratory profile** | Development/experimental operation with public or synthetic material. Local execution alone does not authorize confidential data. |
| **sealed profile** | A future protected operating context requiring separately verified identity, policy, storage, egress, retention, audit and related controls. |
| **trust boundary** | The verified technical and governance controls permitting protected processing; more than the fact that execution is local. |
| **fail closed** | Refusing the affected action when required authority, policy, qualification or protection evidence is missing or unverifiable. |

Protection requirements: [RA-08][ra08].

## Implementation foundation

| Term | Meaning |
| --- | --- |
| **workspace** | TDG's local data area for its store and retained records; distinct from a Review Package. |
| **empty-store initialization** | Creating workspace metadata and the initial store before any package processing. |
| **capability manifest** | A machine-readable description of functions the build exposes or keeps unavailable. |
| **qualified build** | A specific build/configuration tied to recorded executed verification. Later project decisions do not rewrite that historical build. |

Implemented foundation and evidence: [W01][w01]. Work-item completion, increment acceptance and product acceptance are separate decisions.

[baseline]: docs/requirements-analysis/ra-10/test-design-gatekeeper-requirements-analysis-readiness-v0.2.md
[charter]: docs/governance/test-design-gatekeeper-project-charter-v0.4.md
[sad04]: docs/solution-design/test-design-gatekeeper-sad-04-integrated-review-increment-plan-v0.2.md
[ra01]: docs/requirements-analysis/test-design-gatekeeper-ra-01-stakeholders-actors-authority-v0.3.md
[ra04]: docs/requirements-analysis/test-design-gatekeeper-ra-04-scope-qualification-classification-boundaries-v0.2.md
[ra05]: docs/requirements-analysis/ra-05/test-design-gatekeeper-ra-05-findings-dispositions-persistence-v0.2.md
[ra05-status]: docs/requirements-analysis/ra-05/test-design-gatekeeper-ra-05-findings-dispositions-persistence-v0.2.md#3-run-state-assessment-ledger-and-result-availability
[ra05-dispositions]: docs/requirements-analysis/ra-05/test-design-gatekeeper-ra-05-findings-dispositions-persistence-v0.2.md#52-finding-dispositions--accepted-od-ra05-002
[ra07]: docs/requirements-analysis/ra-07/test-design-gatekeeper-ra-07-llm-roles-qualification-v0.2.md
[ra08]: docs/requirements-analysis/ra-08/test-design-gatekeeper-ra-08-confidentiality-security-privacy-v0.2.md
[ra09]: docs/requirements-analysis/ra-09/test-design-gatekeeper-ra-09-data-representations-import-export-contracts-v0.2.md
[ra09-kinds]: docs/requirements-analysis/ra-09/test-design-gatekeeper-ra-09-data-representations-import-export-contracts-v0.2.md#22-distinct-json-document-kinds
[ra09-origin]: docs/requirements-analysis/ra-09/test-design-gatekeeper-ra-09-data-representations-import-export-contracts-v0.2.md#42-origin-and-accountable-human-adoption
[ra10]: docs/requirements-analysis/ra-10/test-design-gatekeeper-ra-10-evaluation-acceptance-v0.2.md
[w01]: docs/implementation/i01-w01-foundation.md
