# Test Design Gatekeeper

## RA-01 — Stakeholders, Functional Roles, Responsibilities, and Decision Authority

| Field | Value |
| --- | --- |
| Basis | Accepted RA-01 v0.3, originally dated 2026-09-12 |
| Original acceptance and gate | Role model and five decisions accepted; GO to RA-02 under `PG-RA01-001`, 2026-09-09 |
| Replacement baseline | v0.3 designated on 2026-09-15 in [PG-RA03-001][baseline] |
| Text maintenance | Consolidated on 2026-10-20; section numbers and identifiers retained |
| Decision authority | Project Owner |
| Upstream scope | [Project Charter v0.4][charter] |

This is the maintained role and authority model. The [original v0.3 text][original] remains in Git history; hashes and byte counts in earlier reviews and trace ledgers describe that historical snapshot. The later acceptance resolved its candidate labels. RA-01 defines responsibilities, not implementation permission. Current capability, authorization and the development pause are described in [README.md](../../README.md).

### v0.3 controlled amendment summary

`CR-RA03-001`, based on the Owner's `OD-RA03-004` decision of 2026-09-12, clarified ROLE-03 accountability for human-authored or human-controlled AI-assisted testware. TDG cannot infer origin or accountability, edit testware or act as ROLE-03. The amendment was reviewed and v0.3 became the replacement baseline on 2026-09-15.

## 1. Purpose

Define who is affected by TDG, who may interact with it and who may decide. Keep job titles, application access, system output and self-review distinct from the human authority and independence each action requires.

## 2. Scope of RA-01

RA-01 covers stakeholders, functional roles, responsibilities, decision rights, role combinations, operating profiles and the requirements derived from them. It does not select screens, authentication or role-based access-control technology, database design, package or result schemas, assessment algorithms, models or deployment architecture. Organizational testware approval remains outside TDG's direct MVP authority.

## 3. Source baseline

The accepted [Charter][charter] sets scope. The original analysis also drew on `SR-CHARTER-001` and its correction verification, the Requirements Analysis Entry Record v0.1, and inputs `RA-IN-001`, `RA-IN-002`, `RA-IN-004`, `RA-IN-005`, `RA-IN-006` and `RA-IN-008`: accountability, insufficient input, local history, supplied-data limits, protection and hybrid allocation and model variability.

[PG-RA03-001][baseline] records the reviewed accountability amendment and replacement baseline. If this model conflicts with an accepted Charter boundary, the Charter takes precedence until the Owner explicitly approves a change. Detailed result semantics, qualification and protection rules belong in [RA-05][ra05], [RA-07][ra07] and [RA-08][ra08].

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

Scope changes, rule confirmation, testware edits, finding dispositions, confidential-data permission, model qualification and SDLC gates require an identified human authority.

### AP-02 — Job title and authority are separate

Testers, analysts, leads, coordinators and experts may use TDG. Their titles do not determine decision rights.

### AP-03 — One person may hold several roles

Support solo and small-team work. Record the acting role and any independence limitation when one person holds several roles.

### AP-04 — Access does not imply approval rights

Importing, viewing or operating TDG grants no automatic scope, rule-confirmation, disposition, editing, testware-approval or confidential-data authority.

### AP-05 — Finding disposition is not testware approval

Accepting or rejecting one finding neither proves completeness nor approves testware for execution, release or organizational sign-off.

### AP-06 — TDG never inherits human authority

TDG may calculate, identify, suggest, explain, request clarification, abstain and retain evidence. Human decisions in the authority matrix remain human; TDG cannot edit source cases or qualify itself.

### AP-07 — The supplied-data boundary applies to every role

No role may present unsupported inference as fact or unsubmitted material as evaluated evidence. A human may deliberately add sources in a new package version.

## 6. Stakeholder groups

| ID | Stakeholder group | Main concern | Typical examples | Direct interaction |
| --- | --- | --- | --- | --- |
| STK-01 | Test design practitioners | Useful, accurate review with manageable effort | Tester, test analyst | Yes |
| STK-02 | Test review and coordination | Gaps, questions and human decisions | Reviewer, test lead, coordinator | Yes |
| STK-03 | Test-basis and domain stakeholders | Rules, source precedence and ambiguity | Analyst, requirements owner, expert | Optional |
| STK-04 | Testware approval stakeholders | Human organizational approval | Test manager, acceptance authority | Optional or indirect |
| STK-05 | TDG operations | Configuration, mappings, storage, audit and recovery | Administrator | Yes |
| STK-06 | Evaluation and qualification | Evidence for behavior-affecting versions | Evaluation lead, validation reviewer | Yes |
| STK-07 | Data protection and security | Boundary, access, retention, logs and export | Data owner, security representative | Yes or governance-only |
| STK-08 | Product and project governance | Scope, priorities, risks and gates | Project Owner | Yes or governance-only |
| STK-09 | Future delivery and maintenance | Clear, testable, feasible requirements and controlled change | Design, development, maintenance team | Not in RA-01 operation |

ISTQB is a reference source, not this project's stakeholder, sponsor, certifier or approval authority.

## 7. Functional role catalogue

These are responsibilities, not ten mandatory people or software permission groups. Each role's interaction type is stated below; governance responsibility does not by itself make someone a runtime user.

### ROLE-01 — Review Operator

**Direct operational actor.** Assembles or imports packages, starts assessment under an allowed profile, answers validation or clarification requests when authorized, views results and exports them where policy permits. Operation alone grants none of the content, editing or protection decisions assigned to other roles.

### ROLE-02 — Review Scope Owner

**Direct or represented actor.** Declares the feature or small process, selects the supplied basis and cases, approves explicit scope changes and acknowledges limitations. May authorize ROLE-01 to submit that boundary. Owns the submitted scope, not all project documentation or its correctness; cannot authorize external source discovery.

### ROLE-03 — Testware Owner and Editor

**Direct or adjacent actor.** Accepts explicit human accountability for the submitted human-authored or human-controlled AI-assisted cases. Reviews TDG output, decides changes, edits, adds, removes or retains source cases outside TDG's autonomous control and submits deliberately versioned revisions.

This grants neither basis authority nor formal approval. The attributable accountability declaration does not prove authorship history or absence of AI assistance. TDG cannot infer or upgrade origin or accountability from style.

### ROLE-04 — Test Basis Authority

**Direct or represented actor.** Confirms, corrects, rejects or leaves candidate rules unknown; clarifies source precedence, contradictions and fact versus interpretation. May act through an authorized operator. Authority is limited to the assigned domain and supplied sources. Insufficient evidence must remain visible. Rule confirmation neither dispositions a finding nor approves testware.

### ROLE-05 — Finding Disposition Authority

**Direct decision actor.** Reviews evidence, assigns `ACCEPTED`, `REJECTED` or `DEFERRED` to a `PENDING` item, records the required rationale and reopens a disposition when its supporting package or assessment version changes. The detailed lifecycle is in [RA-05][ra05]. A disposition cannot turn unsupported output into evidence or establish completeness, ISTQB conformity or testware approval.

### ROLE-06 — Testware Approval Authority

**External governance role.** Makes organizational readiness or approval decisions using TDG output as one input. Formal approval is outside the direct MVP decision model; TDG cannot perform this role or publish approval on its behalf.

### ROLE-07 — TDG Administrator

**Direct administrative actor.** Operates the approved local environment; manages authorized configuration, mappings, persistence, retention execution, backup and recovery; installs or activates only approved behavior-affecting versions; maintains auditability. Administrative access grants no basis, disposition, testware-approval, qualification or confidential-data authority without separate role assignment.

### ROLE-08 — Evaluation and Qualification Authority

**Direct qualification actor.** Approves or rejects identified models, prompts, deterministic rules, controls and relevant configurations for defined roles, using qualification evidence separated from held-out acceptance evidence. Defines or approves requalification after behavior-relevant change and records limitations and prohibited roles. Evaluated components cannot qualify themselves; permission for one role does not extend to others.

### ROLE-09 — Data and Security Authority

**Governance and policy actor.** Approves data classification, the organization-controlled trust boundary and policies for security, access, retention, deletion, logging, backup, telemetry and export; authorizes or prohibits confidential use and decides relevant residual security risk within organizational governance. May configure or approve policy without joining routine reviews. Data or infrastructure access alone grants no such authority.

### ROLE-10 — Project Owner

**Project governance role.** Owns scope, priorities, requirements and change control; accepts, rejects or defers project findings and residual risks within their authority; authorizes SDLC transitions and prevents implementation preceding applicable approved requirements and design gates. Ownership does not replace separately accountable domain, security or organizational testware-approval authority.

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

- ROLE-01 + ROLE-02: operate TDG and own package scope.
- ROLE-01 + ROLE-03: submit one's own cases.
- ROLE-02 + ROLE-03: own cases and their review boundary.
- ROLE-03 + ROLE-05: disposition findings on one's own testware, explicitly marked as self-review.
- ROLE-02 + ROLE-04: own scope and confirm the basis when sufficiently knowledgeable and authorized.

### 10.2 Conditional combinations requiring visible limitations

Self-review is not independent peer review. A creator of prompts, rules, mappings or evaluation examples may also qualify them as ROLE-08 in a solo laboratory, but must disclose the lack of independence and limit success claims. ROLE-07 + ROLE-09 is allowed only under organizational policy and still requires explicit confidential-data authorization. ROLE-10 may hold laboratory roles without concealing missing domain, security or qualification competence.

### 10.3 Semantically prohibited substitutions

TDG and LLMs cannot hold ROLE-02 through ROLE-10, qualify themselves or decide on their own findings. Operator access does not confer decision authority; administration does not confer content-review authority; finding disposition does not confer testware approval; qualification does not confer confidential-data authorization.

## 11. TDG authority boundary

TDG may validate required package elements and must identify the evaluated version. Insufficient, contradictory or mismatched input requires narrowing, stopping or marking the affected assessment ungradable as applicable. It may request human-supplied context; new evidence requires a deliberate package version, not autonomous retrieval.

Deterministic findings remain separate from human disposition. Qualified LLM suggestions require evidence, uncertainty and an initial `PENDING` disposition. TDG cannot invent missing rules, assign its own human decisions, edit source cases, approve testware, qualify itself, authorize protected-data use or export or open a phase. It cannot declare a suite complete or ISTQB compliant. The action-to-authority assignments are in Section 9; detailed result states are in [RA-05][ra05].

## 12. Operating-role profiles

### 12.1 Laboratory profile

Use public or synthetic data only for development, requirements examples, qualification and evaluation. One person may hold ROLE-01 through ROLE-05, ROLE-07, ROLE-08 and ROLE-10, while recording the acting role for each authority-bearing action. Label self-review and non-independent qualification and never represent combined roles as independent organizational assurance. Confidential project data remains prohibited.

### 12.2 Sealed organizational profile

Future protected use requires verifiable identity and assigned authority, ROLE-09 authorization and verified controls. ROLE-07 applies behavior-affecting configurations only from versions approved by the applicable authority. Organizational policy determines role separation. Assignments, acting roles and authority-bearing actions must be auditable; missing authority blocks the affected action.

RA-01 does not select an authentication or authorization mechanism. [RA-08][ra08] and later design define protection details while preserving these responsibilities.

## 13. Accepted RA-01 requirements

The Owner accepted these sixteen requirements on 2026-09-09. Their wording, priority, status and source traces are retained unchanged below.

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

`MUST` means required for the accepted concept. It does not prescribe enforcement technology or require every mechanism in the first executable increment; increment allocation belongs in approved planning.

## 14. Downstream validation obligations

These ten obligations guide later test analysis; they are not executed tests or a complete test design. The authority matrix supports decision-table tests, while denied actions, dispositions and version-sensitive reopening also need negative and state-transition coverage.

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

Conditions, data, expected results, coverage targets and test levels belong in test design against the relevant accepted requirements and design.

## 15. Decision disposition record

All five decisions below were accepted as recommended on 2026-09-09. No RA-01 policy decision remains open.

### OD-RA01-001 — May the testware author disposition findings in pre-review?

**Yes, with explicit self-review labeling.** An author assigned ROLE-05 may accept, reject or defer findings. The result must not imply independent peer review or formal approval.

### OD-RA01-002 — Is a separate Test Basis Authority mandatory for every Review Package?

**No for laboratory and basic pre-review.** ROLE-02 or ROLE-03 may also hold ROLE-04 with sufficient domain authority. Record the combined assignment and limitation. Disputed evidence or insufficient competence must preserve an unknown or conflicting state or escalation instead of forced confirmation; detailed states belong in [RA-05][ra05].

### OD-RA01-003 — Must the MVP implement authenticated role-based access control?

**The profile determines the requirement.** Laboratory MVP records logical assignments and acting roles; multi-user RBAC is not a prerequisite for proving value. Sealed operation needs verifiable identity, authorization, audit, least privilege and fail-closed enforcement before protected use. Mechanism selection belongs in protection requirements and design.

### OD-RA01-004 — Should TDG perform formal testware approval in the MVP?

**No.** TDG may provide an exportable record and a human may decide readiness for a later human workflow. Organizational approval remains outside direct MVP authority.

### OD-RA01-005 — Who confirms extracted rules when no separate domain expert is available?

**An explicitly assigned human may combine ROLE-02, ROLE-03 and ROLE-04 within their competence.** Otherwise retain unknown or conflicting evidence or escalate. Missing expertise never permits TDG or its LLM to confirm its own interpretation.

## 16. Static quality check

`SR-RA01-001` completed the v0.2 review with no open findings; its reviewer participated in producing the document, so this was not independent assurance. The later `SR-RA03-001` reviewed and accepted the v0.3 accountability amendment; [PG-RA03-001][baseline] records its completed baseline designation. Earlier review statements and hashes remain tied to their original snapshots, not this maintained text. These documentation reviews are not product test results.

## 17. RA-01 exit criteria

The original exit required acceptance of stakeholders, roles, job-title distinctions, authority matrix, role combinations, operating profiles, five decisions and sixteen requirements; a completed static review; no unresolved Critical or High finding; and Owner GO to RA-02.

Those criteria were met for v0.2 and `PG-RA01-001` authorized RA-02 on 2026-09-09. The later v0.3 amendment was reviewed and designated on 2026-09-15 without reopening that phase or changing the earlier gate's scope.

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

RA-01 is closed; v0.3 is its accepted baseline following [PG-RA03-001][baseline]. No amendment review remains pending. Use the responsibilities and authority matrix for downstream work within its own authorization. Current documentation cleanup and the development pause are described in [README.md](../../README.md).

[charter]: ../governance/test-design-gatekeeper-project-charter-v0.4.md
[baseline]: ../reviews/test-design-gatekeeper-ra-03-gate-record-v0.2.md
[original]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/19948de4cb79b49904980ba335692752f291d3dd/docs/requirements-analysis/test-design-gatekeeper-ra-01-stakeholders-actors-authority-v0.3.md
[ra05]: ra-05/test-design-gatekeeper-ra-05-findings-dispositions-persistence-v0.2.md
[ra07]: ra-07/test-design-gatekeeper-ra-07-llm-roles-qualification-v0.2.md
[ra08]: ra-08/test-design-gatekeeper-ra-08-confidentiality-security-privacy-v0.2.md
