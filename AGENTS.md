# AGENTS.md

This file guides agents working on Test Design Gatekeeper (TDG). It explains how to find the relevant sources, keep work within its authorized scope and make claims supported by evidence. Product requirements and accepted design decisions belong in their governing documents, not here.

Keep project documentation in **English**. Explain proposed changes and document contents to the Owner in **Polish**.

## Current work boundary

The Owner has paused development for documentation cleanup; see [README.md](README.md). TC-I01-033 remains on hold. Prepare changes **one file at a time**, explain the exact proposal in Polish and obtain the Owner's approval before publishing that file. Do not resume development without an explicit decision to do so.

Carry out work already covered by approval without asking for the same permission again. Silence is not a substitute for a required human decision.

## Read the sources needed for the task

Before a substantive change, establish the branch and commit, inspect local changes, identify the authorized scope and read the relevant governing sources. Use [README.md](README.md) for orientation and [CONTEXT.md](CONTEXT.md) for unfamiliar terms. Do not read the whole repository mechanically before every small edit.

| Question | Source |
| --- | --- |
| What is the project scope? | Accepted Charter and decisions in [docs/governance](docs/governance) |
| What behavior, authority or data rule is required? | Relevant accepted document in [docs/requirements-analysis](docs/requirements-analysis) |
| What solution was accepted? | Relevant document in [docs/solution-design](docs/solution-design), with its acceptance or correction record |
| What was approved, closed or authorized? | Actual Owner decision and its recorded scope; existing records in [docs/reviews](docs/reviews) or the relevant work-item document |
| What is implemented? | [Source code](src/tdg) and relevant [implementation records](docs/implementation) |
| What was exercised and observed? | [Tests](tests), execution results and dated verification evidence |
| Why was a boundary introduced? | [LEARNINGS.md](LEARNINGS.md), then the original source |

Authority depends on the question. README, CONTEXT, LEARNINGS and this file help navigation and understanding; they do not replace accepted product contracts. An example or a newer filename does not override an accepted rule by itself. Read an old proposal together with its later decision when establishing what is currently accepted.

A new explicit Owner decision can change the authorized work or an accepted baseline. Establish and record its scope; do not treat it as proof of implementation or verification. If accepted decisions resolve a conflict, follow them. If a material conflict remains unresolved, show the affected rule and sources and ask for a decision before changing that behavior.

## Keep documentation small and current

- Give each active document a clear purpose. Keep a rule or definition in its governing source and link to it where needed, instead of copying it into successive layers.
- Put approved corrections into the current text so a reader can find the applicable rule. Preserve the earlier wording and decision history through Git history and, where needed, linked evidence or an archive.
- Do not create another version, addendum, review record or closure document solely because a small edit was made, a status changed or this cleanup progressed. Use the existing relevant document and commit history when they are sufficient. Create a separate artifact only for a distinct need that cannot be met there.
- Keep actual human decisions attributable, with their date and scope. Record a decision once and link to it where necessary; do not invent acceptance or multiply records of the same approval.
- Distinguish editorial simplification from a change to required behavior. Preserve requirement IDs, validation IDs, status meanings, contract fields, authority, identity, retry rules and acceptance conditions unless their change has been explicitly approved.
- Before consolidating or removing a file, account for its unique decisions, evidence and incoming links. Preserve access to necessary history. Do not rewrite dated results, earlier failures or historical build evidence as if later knowledge had existed at the time.
- Keep detailed test inputs and technical measurements with tests and manifests. Describe their purpose and evidence limits in documentation without repeating their contents in multiple progress reports.
- Use plain language. State what works, what was checked, what remains uncertain and what decision is needed. Add detail when it helps the reader act or assess a claim.

This changes how current documentation is maintained. It does not change the product's requirements for immutable records or permit altering historical test results.

## Keep changes within the approved scope

Read what each authorization actually permits. A decision may authorize several steps; do not invent an extra gate between them. Conversely, approval of one work item does not authorize adjacent capability unless the decision includes it. A design acceptance is implementation permission only when its scope says so, and it is never evidence that the implementation has passed.

Make small, coherent changes. Avoid unrelated refactoring or abstractions introduced only to make a test easier. Keep unavailable capability explicitly unavailable, and describe planned behavior as planned.

Agents may analyze, propose, implement authorized work and record decisions that humans have actually made. They must not independently accept requirements, grant implementation permission, close work items or phases, accept increments or products, qualify models/configuration, disposition findings, approve testware or authorize confidential-data use. Use the applicable human authority for those decisions.

## Verify behavior and preserve evidence

Derive expected outcomes from accepted contracts before observing the implementation. Identify the observable boundary, suitable test level and relevant negative or failure cases. A test must distinguish the behavior claimed; copying observed behavior into an expectation does not create an independent oracle.

When a meaningful failure occurs, preserve it, reproduce it and distinguish a product defect from a test/harness problem, environment problem, contract conflict, unavailable capability or expected refusal. Apply the smallest justified correction, rerun the focused check and original scenario, and satisfy the applicable regression gate. Do not weaken an assertion, fixture or governing rule to make a test pass.

Keep claims proportional to the evidence:

- Traceability and a prepared test inventory do not prove implementation.
- Checks of fixture files and setup do not prove product behavior; skipped placeholders are not passing product tests.
- Portable checks do not establish native Windows controls, and local execution does not establish readiness for confidential data.
- A passing test is not human acceptance. Coverage alone is not an acceptance argument; self-review is not independent assurance.
- A completed run, zero findings or a valid model response does not prove good testware, complete coverage or semantic correctness.

Report the environment, scope, observations and remaining limits where relevant. Preserve material failures and their corrections; a later pass does not erase an earlier failure. A recommendation or provisional effort estimate stays provisional until the applicable decision or evidence changes it.

## Preserve product boundaries

Do not automatically treat abstention, an unavailable capability or a negative status as a defect. Distinguish missing evidence, policy denial, an unstarted check, interrupted work, technical failure and a blocked whole run. Use the accepted status contracts rather than flattening these situations into one generic error.

Use only deliberately supplied project material in product review logic. Agent access to repository information does not authorize feeding that information to the product. Supplied URLs, paths, references and command text remain data unless an accepted operation explicitly permits their use.

Do not infer authorship from style, accountability from a job title, approval from an imported label, business truth from model confidence, or permission from available credentials. Model output is untrusted and must pass the applicable deterministic, policy, qualification and human controls. A model cannot qualify itself, obtain extra context on its own, create human authority, turn a suggestion into source truth, repair source testware silently or use unauthorized external discovery as a fallback.

When required authority, policy, qualification or protection cannot be established, preserve that uncertainty and prevent the prohibited operation. Do not cross the laboratory/confidential-data boundary without the required authorization and evidence.

## Stop only at a concrete unresolved boundary

Pause the affected work when the governing rule or expected outcome is materially unclear, the change exceeds authorization, a required design decision is missing, or continuation would replace human authority, weaken an accepted contract, cross a data/protection boundary or erase evidence. Insufficient evidence prevents the stronger claim; it does not prevent reporting what is known or preparing a proposal.

Explain the specific blocker, relevant sources and available options. Ask for the decision needed to continue. Do not turn a routine edit or an already authorized step into another approval process.

## Finish and hand off

Inspect the diff, check links and confirm that current claims match the evidence. Run checks appropriate to the change and satisfy any applicable verification gate. A documentation-only edit does not itself require rerunning unrelated product tests.

Report what changed, why, how it was checked and any material remaining limitation. Name any human decision still required. Agent completion and green tests do not themselves close a work item or establish product acceptance.

### Commit cadence

Use small, coherent commits for completed work. On active workdays, publish ready changes daily or several times during the day within the existing publication authorization. Keep related documentation aligned when it is part of the approved scope; during the current cleanup, respect the one-file approval process. A commit does not require a separate progress document.
