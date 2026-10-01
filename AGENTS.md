# AGENTS.md

## Purpose

This file is the operating contract for an AI or coding agent working in
Test Design Gatekeeper (TDG).

It is a router and execution discipline. It is **not** a source of product
requirements, design authority, project status, implementation authorization,
acceptance, or Owner decisions.

Use this file to determine:

- what to read;
- which source is authoritative for the current question;
- how to bound a change;
- what evidence is required before making a claim;
- when to stop and request a human decision.

Current product status belongs in `README.md`. Canonical terminology belongs in
`CONTEXT.md`. Historical reasoning belongs in `LEARNINGS.md`. Normative
requirements, accepted design, review decisions, implementation evidence, and
closure records remain in `docs/`.

If this file conflicts with an accepted governing artifact, the governing
artifact wins.

---

## 1. Start here

Before any non-trivial change:

1. Read `CONTEXT.md` for canonical project terminology.
2. Read `README.md` for current project status and supported capability.
3. Identify the exact task type.
4. Read the smallest authoritative source set needed for that task.
5. Establish the currently authorized increment and work-item boundary.
6. Pin the repository state before editing.
7. Identify the acceptance oracle or evidence boundary before implementation.
8. Do not proceed when authority, scope, or governing behavior is unresolved.

Do not read the whole repository mechanically before every small change. Read the
sources required to understand the current decision boundary.

A trivial editorial correction may require less review than a behavioral,
contract, architecture, persistence, authority, or evidence change.

---

## 2. Source routing

Use the source that is authoritative for the question being answered.

| Question or task | Read first |
| --- | --- |
| What is the current public project status? | `README.md` plus the relevant latest review/closure record |
| What does a TDG term mean? | `CONTEXT.md` |
| Why does an important boundary or decision exist? | `LEARNINGS.md`, then the source requirement/design/review artifact |
| What is the approved product scope or project-level boundary? | `docs/governance/` |
| What behavior, authority, data rule, or evaluation obligation is required? | the relevant `docs/requirements-analysis/` artifact |
| What technical/logical solution was accepted? | the relevant `docs/solution-design/` artifact plus its review/decision record |
| Was a document, work item, or phase actually accepted or authorized? | the relevant review, decision, gate, or closure record |
| What was actually implemented? | source code plus `docs/implementation/` |
| What was actually executed or verified? | executable tests plus recorded implementation/verification evidence |
| What was learned from a defect, review, or course correction? | `LEARNINGS.md` |
| What does an old `PROPOSED`, `PENDING`, or pre-GO snapshot mean now? | read that snapshot together with its later review/closure record |

Do not use chat history as a stronger source than the repository contract.

Do not use `LEARNINGS.md` as a substitute for normative requirements.

Do not use `CONTEXT.md` as a substitute for accepted data/status contracts.

Do not use `README.md` alone to reconstruct detailed behavior when an accepted
RA/SAD contract exists.

---

## 3. Source authority and conflict handling

TDG does not use one universal document hierarchy.

Authority depends on the question.

In general:

- the Charter and accepted governance records define project scope and
  project-level constraints;
- Requirements Analysis defines required behavior, authority, domain boundaries,
  data/evaluation obligations, and validation intent;
- Solution and Architecture Design defines accepted technical/logical decisions
  within its approved scope;
- review, decision, gate, and closure records establish whether a proposal was
  accepted, corrected, rejected, closed, or authorized;
- implementation records and executable evidence establish what was actually
  built and exercised;
- `README.md` summarizes current public status but does not replace the source
  contracts;
- `CONTEXT.md` explains terminology but is not normative authority;
- `LEARNINGS.md` preserves engineering reasoning but is not normative authority.

Use the source authoritative for the specific question.

### Conflict rule

Do not silently reconcile conflicting artifacts.

If accepted source authority resolves the conflict:

```text
identify the governing source
-> follow it
-> preserve the historical difference
```

If authority does not resolve the conflict:

```text
preserve the conflict
-> identify the affected behavior/decision
-> stop
-> request a human decision
```

Do not choose the interpretation that is easiest to implement or easiest to make
green.

---

## 4. Historical artifact preservation

Historical TDG artifacts are evidence of what was known, proposed, or authorized
at a particular time.

Do not rewrite an old snapshot merely because a later decision changed the
project state.

Examples include:

- `PROPOSED`;
- `PENDING`;
- `GO NOT GRANTED`;
- earlier requirement/design versions;
- historical examples later corrected by a governing contract;
- a status string embedded in an already-qualified build;
- a first failing verification run later corrected.

Where a later state must be recorded, use the mechanism appropriate to the
project:

```text
new version
review record
correction notice
addendum
implementation evidence
closure record
```

Do not create a timeless-looking history by silently editing evidence after the
fact.

A later PASS does not erase an earlier FAIL.

A later Owner decision does not rewrite the historical state of an already
qualified artifact.

---

## 5. Authorization and scope control

Before implementation or a substantive documentation change, establish exactly
what is authorized.

At minimum determine:

```text
Which increment?
Which work item?
Which capability?
Which accepted contracts govern it?
Which activities remain outside the authorized boundary?
```

Authorization is bounded.

The following implications are invalid:

```text
work-item GO
-> permission to implement the next work item
```

```text
work-item closure
-> increment acceptance
```

```text
increment acceptance
-> MVP acceptance
```

```text
design acceptance
-> implementation GO
```

```text
implementation complete
-> product acceptance
```

Do not implement adjacent future capability "while already in the area".

Do not enable unavailable capability merely because the supporting code would be
easy to add.

Do not convert planned future behavior into current product claims.

---

## 6. Human authority

TDG preserves explicit human authority. An AI/coding agent is not a substitute
for that authority.

An agent may:

- analyze accepted sources;
- identify contradictions or gaps;
- propose a design or correction;
- implement work that is already authorized;
- create tests and evidence;
- prepare a review or closure record for human decision;
- record a human decision after that decision has actually been made.

An agent must not independently:

- accept or reject a project requirement on behalf of the Owner;
- grant an SDLC phase gate;
- grant implementation GO;
- close a work item;
- accept an increment or product;
- qualify a model/configuration;
- disposition a finding on behalf of the designated human authority;
- approve testware;
- authorize confidential-data use;
- infer that silence or continued work means approval.

Human authority must be attributable to the actual human decision.

A recommendation produced by the agent remains a recommendation until accepted
through the applicable project mechanism.

---

## 7. Test and oracle discipline

Expected behavior must come from accepted contracts before implementation results
are observed.

Prefer:

```text
accepted contract
-> independent expected outcome
-> fixture/oracle/test
-> implementation
-> execution evidence
```

Avoid:

```text
implementation behaves this way
-> encode observed behavior as expected
-> call the test independent
```

A test is evidence only for the behavior it can actually distinguish.

Before implementing a material behavior:

- identify the governing requirement/design contract;
- identify the observable boundary;
- define the expected outcome;
- decide the correct test level;
- identify relevant negative/failure cases;
- state what the test will **not** prove.

Do not weaken a test, assertion, fixture, or oracle merely to obtain GREEN.

Do not derive an acceptance claim from line coverage alone.

---

## 8. Failure preservation and defect diagnosis

A material first failure is engineering evidence.

When a real defect is suspected:

```text
reproduce
-> preserve the first meaningful RED
-> classify the failure
-> identify the correct seam
-> define/confirm the oracle
-> apply the smallest justified correction
-> focused GREEN
-> original scenario
-> broader required regression
```

Before changing product behavior, classify the observation where possible as:

- product defect;
- test/validation-harness defect;
- environment/platform problem;
- contract ambiguity or contradiction;
- unsupported capability;
- insufficient evidence;
- expected fail-closed behavior.

A failing test is not automatically a product defect.

A passing test after a harness correction is not automatically product evidence.

Do not overwrite or delete the original failure merely because a later run passes.

---

## 9. Evidence discipline

Keep evidence layers distinct.

These implications are invalid:

```text
configured != exercised
exercised != passed
passed != accepted
traceability != implementation
implementation != executed verification
verification != product acceptance
local execution != confidential/sealed readiness
deterministic != automatically correct
LLM-assisted != qualified != accepted
```

A claim must not be stronger than the evidence supporting it.

Examples:

- a green portable test suite does not prove a native platform-specific control;
- successful package capture does not prove minimum review admissibility;
- a completed run does not prove good testware;
- zero findings do not prove complete coverage;
- a valid model response does not prove semantic correctness;
- 100% requirement traceability does not prove implementation completion;
- a self-review does not become independent assurance.

When evidence is incomplete, say exactly what is and is not established.

---

## 10. Fail-visible behavior, abstention, and unavailable capability

TDG is designed to preserve uncertainty instead of guessing it away.

An agent must not "repair" the product merely because a result is:

- `UNGRADABLE`;
- `NOT_PERFORMED`;
- `INCOMPLETE`;
- `PARTIAL`;
- `BLOCKED`;
- an explicit unavailable capability;
- a justified abstention.

Those states may represent correct product behavior.

Always distinguish:

```text
evidence missing
capability unavailable
policy denied
work started but incomplete
technical failure
whole-run prerequisite blocked
```

Do not flatten them into one generic failure.

Where a required authority, policy, qualification, or protection boundary cannot
be established, fail closed rather than inventing permission.

---

## 11. Change discipline

### Before editing

- pin branch and HEAD;
- inspect working-tree state;
- identify the authorized scope;
- identify the governing contract;
- understand whether the change is behavioral, documentary, evidential, or
  historical.

### During editing

- make the smallest justified change;
- avoid opportunistic scope growth;
- preserve unrelated historical evidence;
- do not refactor authority, identity, persistence, or status semantics merely for
  convenience;
- do not introduce abstractions only to make a test easier;
- keep unsupported capability explicitly unavailable.

### After editing

- run focused checks for the changed boundary;
- run the required broader regression/verification gate;
- inspect the diff;
- preserve meaningful failures and corrections;
- update documentation only to the strength supported by evidence;
- request the required human decision before claiming closure.

---

## 12. Documentation-change discipline

TDG documentation is part of the engineered product boundary.

Before changing a document, classify the change.

Possible classes include:

**Editorial correction**

Formatting, spelling, grammar, or wording that does not change normative meaning.

**Normative change**

A change to required behavior, authority, status meaning, data contract, allowed
operation, invariant, or acceptance rule.

**Controlled amendment**

A deliberate change to an accepted baseline using the project's recorded
change-control mechanism.

**New version**

A successor artifact preserving the previous version as historical evidence.

**Review finding/correction**

A documented contradiction, defect, or ambiguity and its accepted disposition.

**Implementation evidence update**

A record of what was actually built, executed, observed, or qualified.

**Closure/acceptance decision**

An attributable human governance decision.

Do not treat every Markdown change as a harmless `docs:` edit.

Changing `shall` to `may`, an enum value, envelope field, authority boundary,
identity rule, retry rule, or acceptance condition can alter the product contract.

When a historical artifact contains wording that became obsolete, prefer a
governing correction/addendum/new version over silent retroactive editing.

---

## 13. Data, model, and protection boundaries

The supplied-data-only rule applies to agent work as well as product behavior.

Do not introduce hidden project context into product logic merely because the
agent can access more repository information.

Do not make a supplied URL/path/reference executable by default.

Do not infer:

- authorship from writing style;
- accountability from a job title;
- approval from a status-like source field;
- domain truth from model confidence;
- sealed readiness from local execution;
- permission from the existence of credentials or infrastructure.

Model output remains untrusted data until the applicable deterministic checks,
policy checks, qualification boundary, and human workflow permit its use.

An LLM cannot:

- qualify itself;
- grant itself more context;
- create human authority;
- turn a suggestion into source truth;
- silently repair source testware;
- use unavailable external discovery as a fallback.

---

## 14. Stop conditions

Stop implementation or substantive document change when any of these is true:

- the governing authority cannot be identified;
- two authoritative sources remain materially contradictory;
- the acceptance oracle is unclear;
- the proposed change exceeds the authorized increment/work item;
- implementation requires a new unaccepted design decision;
- the observed failure has not been classified well enough to justify a product
  change;
- available evidence is insufficient for the requested claim;
- a required human authority would be replaced by agent inference;
- the change would cross the supplied-data-only boundary;
- the change would cross the laboratory/sealed protection boundary without
  authority;
- the only way to make a test pass is to weaken the accepted contract;
- the only way to continue is to treat historical evidence as if it never
  existed.

When stopping:

```text
preserve what is known
-> identify the unresolved decision
-> identify the governing sources
-> present the evidence and options
-> escalate to the appropriate human authority
```

Stopping on insufficient evidence is correct behavior.

---

## 15. Completion and handoff

Agent work is ready for handoff only when the evidence supports that statement.

A useful completion check is:

```text
scope remained bounded
governing contract was followed
required checks were executed
material failures were classified
historical evidence was preserved
documentation matches the evidence strength
no unresolved authority conflict is hidden
required human decision is clearly identified
```

Do not reduce completion to:

```text
tests are green
```

Green tests are one evidence source, not the complete project decision.

Agent completion is not Owner acceptance.

A work item is not closed merely because implementation and tests are complete.
Closure requires the applicable review/evidence boundary and the human decision
defined by the project governance model.

---

## 16. Durable operating principles

When in doubt, prefer these rules:

```text
authority before action
contract before implementation
oracle before result
evidence before claim
preserve history before cleanup
smallest authorized change before adjacent improvement
explicit uncertainty before convenient guessing
human decision before governance closure
```

These principles are intended to keep future AI-assisted work aligned with TDG's
evidence-grounded design without turning `AGENTS.md` into a second requirements or
architecture specification.
