# Test Design Gatekeeper

## RA-01 — Stakeholders, Functional Roles, Responsibilities, and Decision Authority

| Field | Value |
| --- | --- |
| Document version | 0.3 |
| Document date | 2026-09-12 |
| SDLC phase | Requirements Analysis |
| Workstream | `RA-01` |
| Status | CONTROLLED AMENDMENT CANDIDATE — RA-01 v0.2 and `PG-RA01-001` remain effective; focused delta review required |
| Decision authority | Project Owner |
| Project Owner review | RA-01 and all five recommendations accepted on 2026-09-09 |
| Phase-gate record | `PG-RA01-001` — `GO` to RA-02, 2026-09-09 |
| Approved upstream baseline | Project Charter v0.3 |
| Amendment source | `OD-RA03-004`, accepted by Project Owner on 2026-09-12; Charter v0.4 amendment candidate |
| Implementation authorization | NOT GRANTED |

> **Document status notice:** The Project Owner accepted the RA-01 role model and all five recommended decisions on 2026-09-09, and `PG-RA01-001` subsequently authorized RA-02. RA-01 v0.2 remains the approved baseline and that historical gate remains effective. This v0.3 candidate applies only the human-accountability clarification accepted through `OD-RA03-004`. It requires focused delta review before replacing v0.2. No authentication, authorization, user-interface, database, or architecture design is selected here.

### v0.3 controlled amendment summary

| Change | Source | Effect | Boundary preserved |
| --- | --- | --- | --- |
| `CR-RA03-001` | `OD-RA03-004` | ROLE-03 may own accountable human-authored or human-controlled AI-assisted testware; eligibility depends on explicit human accountability, not purity of authorship | TDG cannot infer origin or accountability, edit testware, or act as ROLE-03 |

## 1. Purpose

This document defines who is affected by Test Design Gatekeeper, who may interact with it, which human responsibilities must remain outside the system, and who may make each class of decision.

Its purpose is to prevent four recurring authority errors:

- treating a job title as automatic decision authority;
- treating access to TDG as permission to approve every action;
- treating an LLM or deterministic result as a human decision;
- treating self-review as independent peer or organizational approval.

## 2. Scope of RA-01

RA-01 covers:

- stakeholder groups;
- human functional roles;
- the relationship between organizational job titles and TDG roles;
- responsibility and decision-authority boundaries;
- permitted combinations of roles;
- the distinction between laboratory and sealed organizational operation;
- requirements derived from the accepted role model;
- recorded Project Owner decisions.

RA-01 does not define:

- screens, navigation, or user-interface design;
- authentication or role-based access-control technology;
- database tables or implementation technology;
- detailed Review Package fields;
- detailed finding and status schemas;
- the algorithms for EP, BVA, Decision Table, or State Transition assessment;
- model selection, prompts, or deployment architecture;
- organizational testware-approval workflow outside TDG.

## 3. Source baseline

The analysis is constrained by:

- Project Charter v0.3, the currently approved baseline;
- Project Charter v0.4 controlled amendment candidate for the `OD-RA03-004` clarification only;
- Static Review `SR-CHARTER-001` and its correction-verification record;
- Requirements Analysis Entry Record v0.1;
- `RA-IN-001` — eligible users, roles, and accountability;
- `RA-IN-002` — insufficient, contradictory, or mismatched input;
- `RA-IN-004` — local review history and version traceability;
- `RA-IN-005` — supplied-data-only boundary;
- `RA-IN-006` — security and privacy requirements;
- `RA-IN-008` — model variability and hybrid allocation.

If this document conflicts with an approved Charter boundary, the Charter takes precedence until the Project Owner approves an explicit change.

## 4. Terminology

| Term | Meaning in this project |
| --- | --- |
| Stakeholder | A person, group, or organizational function affected by TDG or able to affect its requirements, operation, or acceptance |
| Job title | An organization-specific label such as tester, business analyst, test lead, or coordinator; it does not by itself grant TDG authority |
| Functional role | A bounded set of responsibilities and decision rights relevant to TDG |
| Actor | A human functional role that directly interacts with TDG for a goal |
| Decision authority | The human role entitled to make or approve a defined decision |
| Performer | The human role that carries out an action; the performer need not be its final authority |
| Combined-role assignment | One person explicitly holding more than one functional role |
| Self-review | Review in which the testware author also dispositions findings; permitted only if labeled accurately and not represented as independent review |
| TDG | The system under specification; never a human decision authority |

Internal deterministic controls, LLM components, local storage, and import adapters are parts of TDG, not independent stakeholders or human authorities.

## 5. Authority principles

### AP-01 — Human authority is explicit

Every decision that changes scope, confirms a business rule, modifies testware, dispositions a finding, authorizes confidential data, qualifies a model, or opens an SDLC gate belongs to an identified human role.

### AP-02 — Job title and authority are separate

A tester, test analyst, business analyst, test lead, coordinator, or domain expert may use TDG. Their job title alone does not determine which decisions they may make.

### AP-03 — One person may hold several roles

The product must support a solo laboratory workflow and smaller teams. A person may therefore hold multiple functional roles, but the acting role and any independence limitation must remain visible.

### AP-04 — Access does not imply approval rights

The ability to import a package, view a result, or operate the application does not automatically grant authority to change scope, confirm a rule, accept a finding, approve testware, or authorize confidential data.

### AP-05 — Finding disposition is not testware approval

Accepting or rejecting an individual TDG finding records a human judgment about that finding. It does not prove test-suite completeness and does not approve the testware for execution, release, or organizational sign-off.

### AP-06 — TDG never inherits human authority

TDG may calculate, identify, suggest, explain, request clarification, abstain, and persist evidence. It may not assign its own human disposition, edit source test cases, approve testware, qualify itself, authorize data use, or make an SDLC gate decision.

### AP-07 — The supplied-data boundary applies to every role

No human role may instruct TDG to conceal unsupported inference as fact or to treat unsubmitted documentation as evaluated evidence. A human may add material by deliberately creating a new version of the Review Package.

## 6. Stakeholder groups

| ID | Stakeholder group | Interest or concern | Typical examples | Direct TDG interaction |
| --- | --- | --- | --- | --- |
| STK-01 | Test design practitioners | Useful, accurate, evidence-based pre-review with low review burden | Tester, test analyst | Yes |
| STK-02 | Test review and coordination | Visibility of gaps, unresolved questions, and human dispositions | Reviewer, test lead, test coordinator | Yes |
| STK-03 | Test-basis and domain stakeholders | Correct interpretation of requirements, business rules, source precedence, and ambiguity | Business analyst, requirements owner, domain expert | Optional |
| STK-04 | Testware approval stakeholders | Confidence that organizational approval remains human and outside unsupported TDG claims | Test manager, test lead, acceptance authority | Optional or indirect |
| STK-05 | TDG operations | Stable local operation, configuration, import mappings, storage, audit, and recoverability | Local application administrator | Yes |
| STK-06 | Evaluation and qualification | Defensible qualification of model, prompt, rule, control, and assessment versions | Evaluation lead, validation reviewer | Yes |
| STK-07 | Data protection and security | Confidentiality, approved trust boundary, retention, access, logging, and export | Data owner, information-security representative | Yes or governance-only |
| STK-08 | Product and project governance | Product scope, prioritization, risks, phase gates, and accepted residual risk | Project Owner | Yes or governance-only |
| STK-09 | Future delivery and maintenance | Clear, testable, feasible requirements and controlled change | Future solution, development, and maintenance team | Not in RA-01 operation |

ISTQB is a reference source, not a stakeholder, certifier, approver, sponsor, or authority for this project.

## 7. Functional role catalogue

Functional roles describe responsibility. They are deliberately more precise than organizational job titles.

The catalogue includes both direct system actors and governance roles. A governance role does not become a direct runtime actor merely because its authority affects TDG.

| Role | Interaction classification | Explanation |
| --- | --- | --- |
| ROLE-01 | Direct operational actor | Operates TDG for the review workflow |
| ROLE-02 | Direct or represented actor | May act directly or authorize ROLE-01 to submit the declared boundary |
| ROLE-03 | Direct or adjacent actor | Reviews TDG output but performs the actual source-testware edit outside autonomous TDG control |
| ROLE-04 | Direct or represented actor | May confirm rules directly or through an authorized operator interaction |
| ROLE-05 | Direct decision actor | Assigns human disposition to individual findings |
| ROLE-06 | External governance role | Formal organizational approval remains outside direct MVP authority |
| ROLE-07 | Direct administrative actor | Performs approved operational and configuration actions |
| ROLE-08 | Direct qualification actor | Records qualification decisions for identified behavior-affecting versions |
| ROLE-09 | Governance and policy actor | May configure or approve policy, but need not participate in routine reviews |
| ROLE-10 | Project governance role | Makes scope, requirements, change-control, and SDLC gate decisions |

### ROLE-01 — Review Operator

Primary responsibilities:

- interact with TDG;
- import or assemble the submitted Review Package;
- start an assessment under an allowed operating profile;
- respond to validation and clarification requests when authorized;
- view and, where policy permits, export review results.

Authority boundary:

- operation alone does not grant authority over scope, source-rule confirmation, finding disposition, test-case editing, or confidential-data approval.

### ROLE-02 — Review Scope Owner

Primary responsibilities:

- declare the bounded feature or small process under review;
- decide which supplied test-basis elements and test cases intentionally belong to that boundary;
- approve an explicit package-scope change;
- acknowledge known scope limitations.

Authority boundary:

- owns the submitted boundary, not the completeness or correctness of the entire project documentation;
- cannot authorize TDG to search outside the submitted Review Package.

### ROLE-03 — Testware Owner and Editor

Primary responsibilities:

- own or maintain the submitted test cases for which the identified human accepts ROLE-03 accountability, whether human-authored or human-controlled with AI assistance;
- decide whether and how a finding results in a test-case change;
- edit, add, remove, or retain test cases outside the autonomous control of TDG;
- submit a deliberately versioned revision for re-review.

Authority boundary:

- editing testware does not automatically grant test-basis authority or formal approval authority;
- an accountability declaration is an attributable human decision, not proof of authorship history or absence of AI assistance; TDG must not infer or upgrade origin or accountability from writing style.

### ROLE-04 — Test Basis Authority

Primary responsibilities:

- confirm, correct, reject, or mark as unknown a candidate rule extracted from supplied sources;
- clarify source precedence and known contradictions;
- distinguish documented fact from interpretation;
- identify when the supplied basis is insufficient rather than inventing a missing rule.

Authority boundary:

- authority applies only to the assigned domain and submitted source set;
- confirmation of a rule does not accept a TDG finding or approve testware.

### ROLE-05 — Finding Disposition Authority

Primary responsibilities:

- review evidence attached to individual findings and suggestions;
- assign `ACCEPTED`, `REJECTED`, or `DEFERRED` to a previously `PENDING` item;
- record or supply an appropriate rationale under later-defined rules;
- reopen a disposition when its supporting package or assessment version changes.

Authority boundary:

- cannot convert unsupported output into evidence;
- cannot turn an individual disposition into an overall completeness, ISTQB-conformity, or testware-approval decision.

### ROLE-06 — Testware Approval Authority

Primary responsibilities:

- make any organizational decision that testware is ready for a later workflow, execution, or formal approval state;
- consider TDG output as one input among other project evidence.

Authority boundary:

- formal approval remains outside the direct MVP decision model;
- TDG cannot perform this role or publish an approval on its behalf.

### ROLE-07 — TDG Administrator

Primary responsibilities:

- operate the approved local environment;
- manage authorized configuration, import mappings, persistence, retention execution, backup, and recovery;
- install or activate only approved behavior-affecting artifact versions;
- maintain operational auditability.

Authority boundary:

- administrative access does not grant authority to confirm business rules, disposition content findings, approve testware, qualify a model, or authorize confidential data unless those roles are separately assigned.

### ROLE-08 — Evaluation and Qualification Authority

Primary responsibilities:

- approve or reject identified model, prompt, deterministic-rule, control, and relevant configuration versions for defined assessment roles;
- use qualification evidence separated from held-out acceptance evidence;
- define or approve requalification after behavior-relevant change;
- record limitations and prohibited roles.

Authority boundary:

- neither an LLM nor another evaluated component may exercise this authority over itself;
- qualification for one role does not grant qualification for another.

### ROLE-09 — Data and Security Authority

Primary responsibilities:

- approve data classification and the organization-controlled trust boundary;
- authorize or prohibit confidential-data use;
- approve security, access, retention, deletion, logging, backup, telemetry, and export policy;
- accept or reject relevant residual security risk under organizational governance.

Authority boundary:

- a Review Operator or TDG Administrator does not acquire this authority merely through access to data or infrastructure.

### ROLE-10 — Project Owner

Primary responsibilities:

- own product scope, priorities, requirements decisions, and change control;
- accept, reject, or defer project-level findings and residual risks within their authority;
- authorize entry into later SDLC phases;
- prevent implementation from preceding approved requirements and design gates.

Authority boundary:

- project authority does not replace domain, security, or organizational testware-approval authority where those require separately accountable stakeholders.

## 8. Indicative job-title-to-role mapping

This table is illustrative, not an authorization rule.

| Organizational title or persona | Common role assignments | Assignments that require explicit additional authority |
| --- | --- | --- |
| Tester or test analyst | ROLE-01, ROLE-02, ROLE-03; often ROLE-05 | ROLE-04 when qualified for the domain; ROLE-06 under project governance |
| Business analyst or requirements owner | ROLE-04; optionally ROLE-01 | ROLE-02, ROLE-05, or ROLE-06 only when explicitly assigned |
| Domain subject-matter expert | ROLE-04; optionally ROLE-01 | Any testware or approval role only when explicitly assigned |
| Test reviewer | ROLE-05; optionally ROLE-01 | ROLE-06 if organizationally accountable for approval |
| Test lead or test coordinator | ROLE-02, ROLE-05; possibly ROLE-06 | ROLE-04 only with sufficient domain authority |
| Local TDG administrator | ROLE-07 | ROLE-04, ROLE-05, ROLE-08, or ROLE-09 only through separate assignment |
| Evaluation or validation lead | ROLE-08 | Content, security, or project-gate roles only through separate assignment |
| Data owner or security representative | ROLE-09 | Operational or test-content roles only through separate assignment |
| Project Owner | ROLE-10 | Domain, security, qualification, or testware approval only through explicit additional assignment |

## 9. Decision-authority matrix

| ID | Decision or action | Final human authority | Typical performer | TDG's permitted contribution |
| --- | --- | --- | --- | --- |
| AUTH-01 | Assemble and submit a Review Package | ROLE-02 for its declared boundary | ROLE-01 | Validate structure and record provenance |
| AUTH-02 | Declare or change the review scope | ROLE-02 | ROLE-01 or ROLE-02 | Detect mismatch; request explicit confirmation; never broaden scope itself |
| AUTH-03 | Add missing source material to a new package version | ROLE-02, with ROLE-04 consulted where needed | ROLE-01 | Identify missing or conflicting evidence; never retrieve it autonomously |
| AUTH-04 | Confirm, correct, reject, or mark an extracted rule unknown | ROLE-04 | ROLE-04, possibly through ROLE-01 interaction | Present source evidence and candidate interpretation |
| AUTH-05 | Modify a test case | ROLE-03 | ROLE-03 | Identify a gap or candidate coverage item; never edit the source testware |
| AUTH-06 | Accept, reject, defer, or reopen an individual finding | ROLE-05 | ROLE-05 | Preserve evidence, uncertainty, derivation, assessment version, and history |
| AUTH-07 | Decide that a revised package is ready to be submitted for peer review | ROLE-03 | ROLE-03 | Summarize review state without claiming completeness or approval |
| AUTH-08 | Formally approve testware under an organizational process | ROLE-06 | ROLE-06 | Provide evidence as an input only; never issue the approval |
| AUTH-09 | Apply an approved operational configuration or mapping version | ROLE-07 | ROLE-07 | Validate version identity and record activation |
| AUTH-10 | Qualify a model, prompt, rule, control, or configuration for a defined role | ROLE-08 | ROLE-08 or assigned evaluator | Provide reproducible evidence; never approve itself |
| AUTH-11 | Authorize confidential-data use | ROLE-09 | ROLE-09 | Enforce the recorded policy and fail closed when authorization is absent |
| AUTH-12 | Authorize protected-data export, retention, or deletion policy | ROLE-09 | ROLE-07 executes approved operations | Enforce policy and create an audit record |
| AUTH-13 | Change approved product scope or requirements | ROLE-10 | ROLE-10 | Provide traceability and impact information |
| AUTH-14 | Open or close an SDLC phase | ROLE-10 | ROLE-10 | Report exit evidence; never make the gate decision |

## 10. Role combinations and independence

### 10.1 Generally compatible combinations

- ROLE-01 + ROLE-02: the person operating TDG may own the bounded package scope.
- ROLE-01 + ROLE-03: the testware author may submit their own cases.
- ROLE-02 + ROLE-03: the testware owner may also own the review boundary.
- ROLE-03 + ROLE-05: the author may disposition findings during assisted self-review, subject to an explicit self-review label.
- ROLE-02 + ROLE-04: a sufficiently knowledgeable person may own scope and confirm the supplied basis.

### 10.2 Conditional combinations requiring visible limitations

- ROLE-03 + ROLE-05 must not be represented as independent peer review.
- A person who created prompts, rules, mappings, or evaluation examples may also hold ROLE-08 in a solo laboratory profile, but the lack of independence must be recorded and success claims weakened accordingly.
- ROLE-07 + ROLE-09 may be combined in a small local setup only when organizational policy permits; this does not remove the need for explicit confidential-data authorization.
- ROLE-10 may hold other roles in the project laboratory, but must not use project ownership to conceal missing domain, security, or qualification competence.

### 10.3 Semantically prohibited substitutions

- TDG or an LLM cannot hold ROLE-02 through ROLE-10.
- ROLE-01 does not automatically imply any decision authority.
- ROLE-07 administrative privilege does not imply content-review authority.
- ROLE-05 finding disposition does not imply ROLE-06 testware approval.
- ROLE-08 qualification does not imply ROLE-09 confidential-data authorization.
- A model cannot qualify itself, accept its own finding, or approve its own output.

## 11. TDG authority boundary

| TDG action | Permitted? | Boundary |
| --- | --- | --- |
| Validate whether required package elements are present | Yes | Must report the evaluated package version |
| Identify insufficient, contradictory, or mismatched input | Yes | Must narrow, stop, or mark affected assessment ungradable |
| Request additional human-supplied context | Yes | Request is not autonomous discovery |
| Search documentation outside the submitted package | No | New evidence requires a deliberate new package version |
| Invent a missing business rule | No | May state a question or evidence gap only |
| Produce a deterministic finding | Yes | Derivation remains separate from human disposition |
| Produce an LLM-assisted suggestion | Yes, after qualification | Must carry evidence, uncertainty, and `PENDING` disposition |
| Accept, reject, or defer its own output | No | ROLE-05 only |
| Edit or overwrite a source test case | No | ROLE-03 only |
| Declare a suite complete or ISTQB compliant | No | Prohibited product claim |
| Approve testware | No | ROLE-06 only and outside direct MVP authority |
| Qualify a model or control version | No | ROLE-08 only |
| Authorize confidential-data use or export | No | ROLE-09 only |
| Open an SDLC phase | No | ROLE-10 only |

## 12. Operating-role profiles

### 12.1 Laboratory profile

Purpose: product development, requirements examples, qualification, and evaluation using public or synthetic data only.

Permitted role arrangement:

- one person may hold ROLE-01 through ROLE-05, ROLE-07, ROLE-08, and ROLE-10;
- each authority-bearing action must still identify the acting role;
- self-review and non-independent qualification must be labeled;
- the profile must not represent combined-role decisions as independent organizational assurance;
- confidential project data remains prohibited regardless of combined roles.

### 12.2 Sealed organizational profile

Purpose: future operation with protected enterprise documentation inside an approved trust boundary.

Required direction:

- human identity and assigned authority must be verifiable rather than merely asserted in free text;
- ROLE-09 authorization and verified security controls are mandatory before confidential-data use;
- behavior-affecting configuration must be applied by ROLE-07 only from versions approved under the applicable authority;
- organization policy determines required separation among content, administration, qualification, and security roles;
- role assignment, acting role, and authority-bearing actions must be auditable;
- absence of an authorized role must fail closed for the affected action.

The detailed authentication and authorization mechanism belongs to later requirements and design. RA-01 defines the authority semantics it must preserve.

## 13. Accepted RA-01 requirements

The Project Owner accepted all sixteen requirements on 2026-09-09 as part of the acceptance of RA-01 and the five recorded decisions. Later consolidation may normalize identifiers or wording, but it must not weaken the accepted authority boundary without controlled change approval.

| ID | Requirement | Priority | Status | Source |
| --- | --- | --- | --- | --- |
| RA01-REQ-001 | TDG shall represent functional responsibilities independently of organization-specific job titles | MUST | ACCEPTED | RA-IN-001; AP-02 |
| RA01-REQ-002 | TDG shall permit one human to hold multiple functional roles while preserving the acting role for authority-bearing actions | MUST | ACCEPTED | Laboratory profile; AP-03 |
| RA01-REQ-003 | Access to operate or view TDG shall not by itself grant content, qualification, security, or approval authority | MUST | ACCEPTED | AP-04 |
| RA01-REQ-004 | A declaration or change of Review Package scope shall require an identified ROLE-02 decision | MUST | ACCEPTED | Charter Sections 6–7; AUTH-02 |
| RA01-REQ-005 | Confirmation, correction, rejection, or unknown classification of an extracted source rule shall require an identified ROLE-04 decision | MUST | ACCEPTED | Charter human-authority model; AUTH-04 |
| RA01-REQ-006 | TDG shall not modify source test cases; any testware change shall remain a ROLE-03 action | MUST | ACCEPTED | Charter MVP exclusion; RA-IN-002 |
| RA01-REQ-007 | Each human finding disposition shall record the responsible human identity or local actor identifier, acting role, disposition, affected item, and assessment version | MUST | ACCEPTED | RA-IN-004; AUTH-06 |
| RA01-REQ-008 | TDG shall keep finding disposition separate from finding derivation and from testware approval | MUST | ACCEPTED | Charter Section 10; AP-05 |
| RA01-REQ-009 | Administrative privilege shall not automatically grant test-basis, finding-disposition, qualification, security, or testware-approval authority | MUST | ACCEPTED | ROLE-07 |
| RA01-REQ-010 | Qualification authority shall remain human, role-specific, version-specific, and unavailable to the evaluated component itself | MUST | ACCEPTED | Charter Section 17; ROLE-08 |
| RA01-REQ-011 | TDG shall block confidential-data processing when required ROLE-09 authorization or applicable verified controls are absent | MUST | ACCEPTED | Charter Section 13; RA-IN-006 |
| RA01-REQ-012 | No role assignment shall permit TDG to search outside the submitted Review Package or invent missing business rules | MUST | ACCEPTED | RA-IN-005; AP-07 |
| RA01-REQ-013 | Combined-role self-review or non-independent qualification shall be recorded and shall not be represented as independent assurance | MUST | ACCEPTED | Static-review limitation; AP-03 |
| RA01-REQ-014 | Acceptance or rejection of an individual finding shall not produce an overall completeness, ISTQB-conformity, or testware-approval claim | MUST | ACCEPTED | Charter Sections 10 and 14 |
| RA01-REQ-015 | For every authority-bearing action recorded by TDG, TDG shall retain the human authority and applicable version evidence in the local review history | MUST | ACCEPTED | RA-IN-004 |
| RA01-REQ-016 | The direct MVP shall not publish an organizational testware approval on behalf of ROLE-06 | MUST | ACCEPTED | Charter primary use case; ROLE-06 |

Priority `MUST` means required for the approved concept to remain coherent. It does not predetermine the technical enforcement mechanism or imply that every mechanism must appear in the first executable increment. Allocation to MVP increments will be decided in later requirements prioritization and planning.

## 14. Downstream validation obligations

The role and authority model is testable. It will become a test basis during test analysis and STLC planning, not merely descriptive project documentation. The decision-authority matrix is a natural source for Decision Table Testing; negative tests and State Transition Testing will cover denied actions, disposition changes, and version-sensitive reopening behavior.

The items below are validation obligations, not executable test cases and not a complete STLC test design.

| ID | Future verification objective | Principal test-design direction | Primary trace |
| --- | --- | --- | --- |
| RA01-VAL-001 | Verify that an authority-bearing action is permitted when the correctly assigned human acts in the applicable role | Positive decision-table rules | AUTH-01 through AUTH-14; RA01-REQ-002 |
| RA01-VAL-002 | Verify that access, a job title, or an unrelated assigned role cannot substitute for the required authority | Negative decision-table rules | AP-02; AP-04; RA01-REQ-001, 003, and 009 |
| RA01-VAL-003 | Verify that author disposition is permitted in pre-review but the result is persistently identified as `SELF_REVIEW` and never as independent review | Positive and negative classification tests | OD-RA01-001; RA01-REQ-013 |
| RA01-VAL-004 | Verify that one person may combine allowed roles while each authority-bearing action records the acting role | Decision-table and audit-evidence tests | AP-03; RA01-REQ-002, 007, and 015 |
| RA01-VAL-005 | Verify that administrative access cannot confer content, qualification, security, or approval authority | Negative authorization tests | ROLE-07; RA01-REQ-009 |
| RA01-VAL-006 | Verify that TDG or its LLM component cannot assign a human disposition, confirm its own unsupported interpretation, qualify itself, or approve testware | Negative boundary and misuse tests | AP-06; OD-RA01-005; RA01-REQ-008 and 010 |
| RA01-VAL-007 | Verify fail-closed behavior when confidential processing lacks the required ROLE-09 authorization or applicable verified controls | Negative security-policy tests | AUTH-11 and AUTH-12; RA01-REQ-011 |
| RA01-VAL-008 | Verify that finding disposition and readiness for a later workflow cannot become formal organizational testware approval | Decision-table and output-claim tests | AP-05; OD-RA01-004; RA01-REQ-014 and 016 |
| RA01-VAL-009 | Verify that no role, including administrator or Project Owner, can bypass the supplied-data-only boundary | Negative scope and provenance tests | AP-07; RA01-REQ-012 |
| RA01-VAL-010 | Verify disposition transitions, reopening after a relevant package or assessment-version change, and preservation of prior history | State-transition and audit-history tests | ROLE-05; RA01-REQ-007 and 015 |

Detailed conditions, data, expected results, coverage targets, and test levels will be defined only after the relevant requirements and design baselines exist.

## 15. Decision disposition record

| Decision ID | Project Owner disposition | Decision date |
| --- | --- | --- |
| OD-RA01-001 | ACCEPTED as recommended | 2026-09-09 |
| OD-RA01-002 | ACCEPTED as recommended | 2026-09-09 |
| OD-RA01-003 | ACCEPTED as recommended | 2026-09-09 |
| OD-RA01-004 | ACCEPTED as recommended | 2026-09-09 |
| OD-RA01-005 | ACCEPTED as recommended | 2026-09-09 |

No RA-01 policy decision remains open.

### OD-RA01-001 — May the testware author disposition findings in pre-review?

Decision: **Yes, with an explicit self-review label.**

The primary use case is assistance before peer review. The author may accept, reject, or defer suggestions as ROLE-05, but the result must be marked as self-review and must not be represented as independent peer review or formal approval.

### OD-RA01-002 — Is a separate Test Basis Authority mandatory for every Review Package?

Decision: **No for the laboratory and basic pre-review workflow.**

The Review Scope Owner or Testware Owner may also hold ROLE-04 when that person has sufficient domain authority. The combined assignment and its limitation must be recorded. Where the basis is disputed or outside that person's competence, TDG must preserve `UNKNOWN`, a later-defined equivalent of `CONFLICTING_BASIS`, or escalation instead of forcing confirmation.

### OD-RA01-003 — Must the MVP implement authenticated role-based access control?

Decision: **The requirement differs by operating profile.**

- Laboratory MVP records logical role assignments and acting role; multi-user RBAC is not a prerequisite for proving review value.
- The sealed organizational profile requires verifiable identity, authorization, audit, least privilege, and fail-closed enforcement before protected use.

The specific authentication and authorization design remains deferred to later requirements and design work.

### OD-RA01-004 — Should TDG perform formal testware approval in the MVP?

Decision: **No.**

TDG may provide an exportable review record and a human may decide that a package is ready for the next human workflow. Formal organizational approval remains outside the direct MVP authority.

### OD-RA01-005 — Who confirms extracted rules when no separate domain expert is available?

Decision: **An explicitly assigned human may combine ROLE-02, ROLE-03, and ROLE-04, but uncertainty must remain expressible.**

The absence of a separate expert never permits TDG or its LLM component to auto-confirm its own interpretation. The human may confirm only within their competence; otherwise the result remains unknown, conflicting, or escalated.

## 16. Static quality check

| Check | Result |
| --- | --- |
| Organizational titles separated from functional authority | PASS |
| Direct actors distinguished from adjacent and governance roles | PASS |
| Human and TDG authority separated | PASS |
| Finding disposition separated from testware approval | PASS |
| Solo laboratory workflow remains possible | PASS |
| Sealed-profile direction remains fail closed | PASS |
| Supplied-data-only boundary preserved | PASS |
| No authentication or architecture solution selected prematurely | PASS |
| Project Owner decisions fully recorded | PASS — 5 of 5 accepted |
| Requirements promoted without weakening the accepted boundaries | PASS — 16 of 16 accepted |
| ROLE-03 wording reflects accountable human control without implying forensic authorship proof | PASS AS CANDIDATE — `CR-RA03-001`; focused delta review pending |

Focused structured static review `SR-RA01-001` is complete for RA-01 v0.2, and the Project Owner subsequently authorized RA-02 through `PG-RA01-001`. The reviewer participated in producing RA-01, so the review does not constitute independent assurance. This v0.3 amendment candidate still requires a focused delta review of `CR-RA03-001`; the completed v0.2 review must not be presented as verification of the later wording.

## 17. RA-01 exit criteria

RA-01 may close only when:

- stakeholder groups are accepted;
- functional role names and responsibilities are accepted;
- the job-title-to-role distinction is accepted;
- the decision-authority matrix is accepted;
- permitted and conditional role combinations are accepted;
- the laboratory and sealed-profile role directions are accepted;
- all five decision records are accepted;
- RA-01 requirements are accepted and baselined;
- a structured static review is complete;
- no unresolved Critical or High RA-01 finding remains;
- the Project Owner authorizes transition to `RA-02`.

All RA-01 phase-exit criteria were satisfied for v0.2, and `PG-RA01-001` authorized RA-02 on 2026-09-09. The v0.3 amendment does not reopen RA-01 or require a new phase gate, but it cannot replace v0.2 as the controlled baseline until its focused delta review is complete.

## 18. Traceability summary

| Upstream source | RA-01 realization |
| --- | --- |
| Charter Sections 3 and 5 | AP-01 through AP-06; stakeholder and role catalogues |
| Charter Sections 6, 7, 9, and 11 | ROLE-02; AUTH-01 through AUTH-03; RA01-REQ-004 and RA01-REQ-012 |
| Charter Section 10 | ROLE-05 and ROLE-06; AUTH-06 through AUTH-08; RA01-REQ-007, 008, 014, and 016 |
| Charter Section 10.5 | ROLE-07; RA01-REQ-007 and RA01-REQ-015 |
| Charter Section 13 | ROLE-09; AUTH-11 and AUTH-12; RA01-REQ-011 |
| Charter Sections 16 and 17 | ROLE-08; AUTH-09 and AUTH-10; RA01-REQ-010 and RA01-REQ-013 |
| Charter Sections 20, 22, and 25 | ROLE-10; AUTH-13 and AUTH-14; RA-01 exit criteria |
| RA-IN-001 | Job-title-independent actor and authority model |
| RA-IN-002 | Human-only testware repair and explicit insufficient-input path |
| RA-IN-004 | Identity, acting role, disposition, and version history |
| RA-IN-005 | Supplied-data-only invariant across all roles |
| Project Owner decision of 2026-09-09 | OD-RA01-001 through OD-RA01-005; RA01-REQ-001 through RA01-REQ-016 |
| Project Owner decision `OD-RA03-004` of 2026-09-12 | `CR-RA03-001`: clarify ROLE-03 ownership through explicit human accountability for human-authored or human-controlled AI-assisted testware |

## 19. Review state and next action

Current state: `RA-01 CLOSED; RA-02 AUTHORIZED; v0.3 CONTROLLED AMENDMENT CANDIDATE AWAITS FOCUSED DELTA REVIEW`.

The Project Owner accepted the stakeholder catalogue, ten functional roles, authority matrix, role combinations, sixteen RA-01 requirements, and all five RA-01 decision recommendations. Focused static review `SR-RA01-001` is complete with zero open findings, and `PG-RA01-001` authorized RA-02 on 2026-09-09. The later `OD-RA03-004` decision has been incorporated only as `CR-RA03-001` in this candidate. The next action for this document is focused delta review and correction verification; no new phase authorization is requested.
