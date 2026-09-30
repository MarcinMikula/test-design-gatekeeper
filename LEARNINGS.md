# Learnings

Chronological engineering journal for Test Design Gatekeeper.

This file preserves the reasoning, evidence, turning points, and course corrections that changed our understanding of the project.

Current product behavior and normative contracts belong in `README.md`, `docs/governance/`, `docs/requirements-analysis/`, `docs/solution-design/`, `docs/reviews/`, and `docs/implementation/`.

`LEARNINGS.md` is not an authoritative specification and does not replace an accepted requirement, design decision, review record, implementation record, or Owner decision. When this journal and a current governing artifact differ, the governing artifact wins.

The point of this file is different: preserve *why* an important boundary exists, *what evidence changed our thinking*, and *what should not be forgotten when the project moves on*.

---

## Concept lesson â€” persuasive LLM output is not review evidence

**Period:** Concept & Feasibility
**Status:** Established

### Starting point

The project began from a useful but dangerous idea: an LLM can read functional test cases and point out missing coverage, weak expected results, or places where black-box test-design techniques may help.

That is easy to demonstrate conversationally. It is much harder to turn into a review assistant whose output deserves engineering trust.

A fluent answer can still:

- invent a missing business rule;
- assume a technique is applicable without enough evidence;
- confuse test level, test type, technique, and execution mode;
- treat a plausible interpretation as confirmed fact;
- produce a convincing verdict without showing why it is justified.

### Learning

The product cannot be based on unrestricted model judgment.

The useful direction is hybrid:

```text
bounded supplied evidence
-> deterministic controls where reproducible rules exist
-> bounded probabilistic assistance where semantics are needed
-> explicit evidence and limitations
-> human decision
```

The LLM may contribute to analysis. It is not the source of truth merely because its explanation sounds convincing.

### Consequence

TDG evolved into an evidence-grounded review assistant rather than a general "AI test-case reviewer". Qualification, provenance, abstention, deterministic checks, and human authority became product concerns rather than implementation details.

---

## Authority lesson â€” the human owns the testware decision

**Period:** Charter / RA-01
**Status:** Established

### Problem

It was initially easy to describe TDG as a "gatekeeper" and accidentally give the tool more authority than intended.

A tool that reports a problem, a reviewer who accepts that problem, a test author who edits the TC, and an organizational approver are not the same actor.

The same issue appears with AI-assisted testware. The meaningful boundary is not "was every word typed by a human?" but "is an identified human accountable for this testware and its use?"

### Learning

Human accountability is more important than authorship purity.

TDG may:

- identify a gap;
- explain the evidence;
- suggest a direction;
- record a human disposition.

TDG must not:

- approve a test case;
- certify completeness;
- silently repair the source TC;
- infer human acceptance from its own finding;
- represent self-review as independent review.

### Consequence

"Human authority" became a system boundary, not a disclaimer.

The project explicitly separates generated findings from human dispositions and keeps source test-case modification outside TDG. Human-controlled AI-assisted testware may be eligible when accountable human ownership is explicit.

---

## Scope lesson â€” supplied-data-only is a feature, not a limitation to hide

**Period:** Charter / Requirements Analysis
**Status:** Established

### Problem

A review assistant could always appear more capable by searching for additional project context when the submitted package is incomplete.

That creates several problems at once:

- the actual review boundary becomes unclear;
- provenance becomes harder to prove;
- confidential material may be accessed unexpectedly;
- missing information is silently converted into hidden context;
- the user cannot tell what evidence produced a finding.

### Learning

The Review Package boundary should be deliberate and visible.

TDG reviews what the operator deliberately supplies. Missing, contradictory, opaque, or mismatched information remains visible as an evidence limitation.

The correct response to insufficient evidence can be:

```text
cannot assess this dimension safely
```

rather than:

```text
search for more context and guess what the user probably meant
```

### Consequence

TDG does not search an entire project repository, follow arbitrary URLs, or invent unstated business rules to rescue a review. Scope and provenance became explicit parts of the product model.

---

## Classification lesson â€” independent axes must remain independent

**Period:** Requirements Analysis
**Status:** Established

### Problem

Testing terminology can tempt an implementation into convenient shortcuts.

Examples:

```text
automated != white-box
integration != structural
manual != black-box
LLM-generated != automatically out of scope
```

Likewise, whether a test case is in scope, whether a technique is applicable, whether evidence is sufficient, whether a finding exists, and whether a result is available are different questions.

### Learning

Do not compress independent meanings into one label or one PASS/FAIL verdict.

TDG needs separate axes for concepts that can vary independently.

This applies both to testing classification and to TDG's own processing states.

### Consequence

Requirements and later solution design deliberately preserve separate classification, qualification, processing, assessment, availability, and human disposition concepts. A convenient boolean is not allowed to erase those distinctions.

---

## Requirements lesson â€” traceability numbers are not implementation progress

**Period:** Requirements Analysis closure
**Status:** Established

### Evidence

Requirements Analysis closed with:

- 249 accepted requirements;
- 169 validation obligations;
- a bidirectional trace structure;
- 424 inspected direct relations.

That is substantial engineering evidence about the specification.

It is not product execution evidence.

### Learning

A requirement can be:

```text
identified
-> accepted
-> traced
-> allocated
```

and still be:

```text
not implemented
not executed
not validated
```

A large traceability number can create false confidence if it is presented like a coverage score for working software.

### Consequence

TDG keeps requirement allocation, test planning, implementation state, execution evidence, and acceptance as separate facts.

Later documents explicitly say that routing all requirement IDs does not mean that all requirements are implemented or passed.

---

## Static-testing lesson â€” reviewing design can find real defects before code exists

**Period:** SAD-04 integrated review
**Status:** Validated by two design findings

### Evidence

The integrated design review exposed two implementation-relevant contradictions.

First, historical ledger wording mixed processing/run states with substantive assessment outcomes. Implementing the illustrative vocabulary literally would have produced incompatible lifecycle semantics.

Second, an illustrative JSON example in SAD-02 did not match the later accepted RA-09 wire envelope. It was explicitly an example, but it was still dangerous as an implementation template.

### Learning

Documentation defects can be product defects waiting to happen.

Static testing is not "proofreading before the real work". When contracts, identities, status semantics, or interchange formats are involved, finding a contradiction before implementation is cheaper and cleaner than discovering it through data migration or runtime behavior.

### Consequence

The original historical material was retained, corrective notices were added, and the governing contract was made explicit.

The project also gained a practical rule:

```text
historical snapshot
!=
current governing decision
```

Do not rewrite old evidence merely to make the documentation look internally timeless.

---

## Design lesson â€” illustrative examples must never outrank the governing contract

**Period:** SAD-04 review
**Status:** Established

### Problem

Examples are useful because they make abstract contracts understandable.

They are also dangerous because implementation work often begins by copying the most concrete-looking artifact.

### Evidence

The SAD-02 JSON example looked implementation-ready enough to be copied, while RA-09 already defined a different accepted control envelope.

### Learning

Examples need an explicit authority boundary.

When an example and a normative contract disagree, the implementation must follow the normative contract, and the discrepancy must be preserved as a finding rather than "fixed silently" in history.

### Consequence

TDG now treats document precedence and later closure records as part of the engineering model. Retained `PENDING`, `PROPOSED`, or historical candidate wording is interpreted together with the later decision record instead of being rewritten after the fact.

---

## Planning lesson â€” an estimate is a hypothesis, not a quality gate

**Period:** SAD-04 implementation planning
**Status:** Established

### Starting estimate

The first I-01 implementation estimate was 40â€“62 hours.

The Owner explicitly challenged that range and noted that testing alone might consume comparable effort.

### Learning

An early estimate does not become more true because it appears in an accepted document.

For this project, the dangerous failure mode would be:

```text
estimate too small
-> tests look expensive
-> reduce test depth to fit the estimate
```

The correct direction is the opposite:

```text
test inventory becomes concrete
-> actual complexity becomes visible
-> estimate changes
```

### Consequence

The original range is retained as an uncertain planning hypothesis, not a budget, deadline, effort ceiling, or acceptance criterion.

W02 is intentionally the first re-estimation point because detailed fixtures, oracles, test variants, and fault-injection needs should reveal more realistic testing effort.

---

## Increment lesson â€” implement the smallest useful foundation without pretending the product exists

**Period:** I-01 planning / W01
**Status:** Established

### Problem

Once implementation started, it would have been easy to create placeholder commands or partial import behavior and then describe the project as if Review Package processing already existed.

### Learning

Capability exposure must be honest.

W01 needed only the project/runtime foundation, capability manifest, environment pinning, controlled workspace initialization, and empty-store behavior.

Everything else could remain visibly unavailable.

### Consequence

The qualified W01 build exposes:

```text
version
capabilities
init
```

while package-processing paths remain disabled.

The project deliberately avoids creating fake receipts, fake Review Packages, fake review runs, or placeholder findings merely to make the CLI look complete.

---

## Target-platform lesson â€” portable tests cannot prove Windows behavior

**Period:** I01-W01 native qualification
**Status:** Validated

### Evidence

The first portable development run on Linux produced:

```text
44 passed
4 skipped
```

All four skipped tests were native Windows tests.

That result was useful development evidence, but it did not prove the intended Windows directory and writer protections.

The first actual Windows run produced:

```text
47 passed
1 failed
0 skipped
```

The failing test showed that a held directory could still be renamed.

### Learning

A green portable suite cannot substitute for executing platform-specific controls on the platform whose semantics matter.

This matters especially for filesystem sharing, reparse points, mutex behavior, path admission, and other OS-level mechanisms.

### Consequence

Windows became a real qualification boundary rather than a target mentioned in metadata.

The project preserved the native failure and investigated the mechanism instead of treating the Linux result as sufficient evidence.

---

## W01 defect lesson â€” "least privilege" still has to perform the required protection

**Period:** I01-W01 defect diagnosis
**Status:** Validated

### Evidence

The original directory guard requested only:

```text
FILE_READ_ATTRIBUTES
```

while omitting `FILE_SHARE_DELETE`.

The expectation was that the open handle would prevent rename. On the observed Windows host, rename still succeeded.

A focused native experiment compared access masks:

```text
FILE_READ_ATTRIBUTES
-> rename succeeded

FILE_LIST_DIRECTORY | FILE_READ_ATTRIBUTES
-> rename blocked

GENERIC_READ
-> rename blocked

DELETE | FILE_READ_ATTRIBUTES
-> rename blocked
```

### Learning

Choosing the narrowest-looking permission is not automatically correct least privilege.

The useful definition is:

```text
minimum authority that still establishes the required invariant
```

A control that is theoretically narrower but does not enforce the required boundary is not the safer implementation.

### Consequence

The guard was changed to the smallest tested access combination that established the intended behavior:

```text
FILE_LIST_DIRECTORY | FILE_READ_ATTRIBUTES
```

Broader alternatives were not selected merely because they also worked.

---

## Evidence lesson â€” preserve the first real failure after the fix

**Period:** I01-W01 correction and qualification
**Status:** Established and applied

### Problem

After a defect is corrected, it is tempting to leave only the final green result in project documentation.

That produces a cleaner story but weaker engineering evidence.

### Evidence

W01 retained the sequence:

```text
first Windows run
-> 47 passed / 1 failed

focused diagnosis
-> access-mask behavior isolated

correction
-> focused regression passed

full Windows regression
-> 48 passed

qualified dev2
-> 48 passed / 0 failed / 0 skipped
```

### Learning

A later PASS should not erase the RED that justified the change.

The failed run answers:

```text
did the test have power to detect the defect?
```

The corrected run answers:

```text
did the proposed change resolve it?
```

Both matter.

### Consequence

The failing `0.1.0.dev1` observation remains part of W01 evidence, while the corrected implementation received a distinct `0.1.0.dev2` build identity.

---

## Evidence-engineering lesson â€” byte identity makes line endings a control

**Period:** PR #3 review
**Status:** Established

### Problem

TDG records SHA-256 identities for accepted artifacts.

On Windows, ordinary Git line-ending conversion can make two visually identical text files have different bytes.

If artifact identity is defined at byte level, CRLF versus LF is no longer a formatting preference.

### Evidence

PR review identified the risk before W01 closure.

A repository-level `.gitattributes` policy was added:

```text
* text=auto eol=lf
```

The accepted SAD-04 artifact identities were then rechecked against repository bytes.

### Learning

Once byte-level identity becomes evidence, text normalization becomes part of the evidence system.

### Consequence

The repository now controls line endings explicitly so local Windows checkout behavior cannot silently undermine documented artifact hashes.

---

## Governance lesson â€” qualified build state and later human closure are different facts

**Period:** W01 closure
**Status:** Established

### Situation

Qualified build `0.1.0.dev2` was tested while its runtime capability manifest said:

```text
W01_VERIFIED_CLOSURE_PENDING
```

After the technical review findings were corrected, the Owner formally closed W01 and granted GO to W02.

### Temptation

Rebuild or edit the qualified product only to replace the old status string with:

```text
W01_CLOSED
```

That would make the latest executable look tidier, but it would also change the artifact that had already been qualified.

### Learning

Technical qualification and governance decisions have different timelines.

The qualified build should keep the status that was true for that build snapshot. A later Owner decision belongs in a later governance/closure record.

### Consequence

`0.1.0.dev2` remains unchanged as the qualified W01 build.

The current project state is instead recorded by the W01 Owner closure record:

```text
W01 CLOSED
W02 GO GRANTED
I-01 still incomplete
```

A later governance fact does not require rewriting previously qualified evidence.

---

## Review lesson â€” a clean PR is not the same as an independently reviewed product

**Period:** PR #3 / W01 closure
**Status:** Established

### Evidence

PR #3 received a deliberate technical self-review of code, tests, documentation, environment evidence, hashes, and scope boundaries.

That review found real documentation/evidence gaps and resulted in correction commits before closure.

At the same time, the repository had no independent reviewer and no GitHub CI status checks for the PR.

### Learning

Useful self-review evidence should neither be dismissed nor overstated.

The correct claim is not:

```text
nobody independent reviewed it, therefore the evidence is worthless
```

and not:

```text
the PR was reviewed, therefore independent assurance exists
```

The actual evidence boundary matters.

### Consequence

W01 could be closed by the Project Owner within the project's solo, AI-assisted development model while still retaining the explicit limitation that this is not independent assurance.

Future stronger claims may require stronger independence or automated gates, but those should be earned by the claim being made rather than retroactively invented.

---

## Process lesson â€” formality is useful only when it prevents a real mistake

**Period:** Requirements Analysis through W01
**Status:** Emerging project principle

### Observation

TDG became much more formal than the other repositories in the same engineering ecosystem.

It accumulated:

- a controlled Charter;
- ten Requirements Analysis slices;
- traceability and static-review records;
- four solution-design activities;
- explicit Owner gates;
- implementation and closure evidence.

This created documentation cost and an active scope/document-growth risk.

It also prevented or exposed real problems:

- authority ambiguity;
- scope expansion through hidden context;
- mixed classification axes;
- incompatible status vocabulary;
- a conflicting JSON implementation template;
- premature implementation claims;
- platform-specific behavior that portable execution could not prove;
- byte-identity risk from line endings.

### Learning

The lesson is not "more documentation is always better".

The useful rule is:

```text
keep formality where it protects authority, evidence, contracts, scope,
irreversible data semantics, or acceptance claims

remove or avoid formality that only duplicates an existing source
```

### Consequence

TDG should continue to use explicit SDLC/STLC gates where they prevent a concrete failure mode, while resisting duplicate architecture summaries, duplicate requirements, ceremonial review records, or documents created only because another project has them.

This `LEARNINGS.md` follows the same rule: it exists because the formal artifacts record the *current contract* well but do not provide one readable history of *how our understanding changed*.

---

## Current course â€” W02 should define the test oracle before the importer teaches us its answer

**Period:** Start of I01-W02
**Status:** Working principle carried from accepted SAD-04 design

W01 established the project/runtime foundation.

The next authorized work is deliberately test-design-heavy:

```text
synthetic fixtures
+ independent receipt/identity oracles
+ traceable detailed test inventory
```

before native JSON capture implementation proceeds.

The reason is methodological.

If implementation comes first, there is a strong risk of:

```text
write behavior
-> observe behavior
-> encode observed behavior as expected
-> call the test independent
```

W02 is intended to reverse that order:

```text
accepted contract
-> fixture
-> expected observable outcome
-> traceable test
-> later implementation
```

This principle has not yet been validated by W02 execution. It is the governing design discipline for the next work item and should be revisited after W02 to see whether it actually improved defect detection, implementation clarity, and effort estimation.

---

## How to use this journal

Add a new entry when evidence materially changes at least one of these:

- our understanding of the product boundary;
- authority or safety rules;
- architecture or data semantics;
- the meaning of a status or identity;
- the acceptance oracle;
- the strength of a product claim;
- implementation direction;
- test strategy;
- the interpretation of a failure;
- the relationship between design and observed behavior.

Do not add an entry for every commit, typo, refactor, or routine PASS.

A useful learning should answer:

```text
What did we think or risk before?
What evidence changed that?
What did we decide?
What consequence should survive into later work?
```

When a learning later becomes obsolete, do not silently delete history. Mark the newer evidence and explain what superseded the earlier understanding.
