# Learnings

Lessons from decisions, reviews and observed failures in Test Design Gatekeeper. This journal explains what changed our understanding and what to carry into later work. It is not a second specification or an acceptance record. [README.md](README.md) describes current capability; the linked source records preserve detailed evidence and decisions. The [earlier journal][earlier-journal] remains available in Git history.

## Concept and requirements: fluent output still needs evidence

An LLM can plausibly identify missing test conditions while inventing business rules, assuming a technique applies or treating its own interpretation as confirmed. This risk shaped the proposed hybrid approach: deterministic checks where explicit rules support them, bounded model assistance for interpretation, inspectable evidence and human decisions. The usefulness of that approach remains to be demonstrated by product evaluation.

The human review boundary matters just as much. TDG reviews the deliberately supplied package; it does not search for missing context or silently edit the source test cases. Reporting an issue, accepting that issue, editing a test and formally approving testware are separate responsibilities. Identified human accountability permits controlled AI-assisted testware without requiring every word to have been typed by a human.

**Carry forward:** a convincing explanation is a proposal to examine. Keep the evidence, uncertainty and responsible human visible. Missing input can justify withholding a conclusion.

Sources: [Project Charter][charter] and [RA-01][ra01].

## Requirements analysis: separate questions need separate answers

Automation does not establish white-box testing, and a manual test is not automatically black-box. Test level, type, design basis and execution mode must be assessed separately. Similarly, scope, technique applicability, sufficient evidence, a reported finding and result availability answer different questions.

**Carry forward:** avoid a convenient label or single PASS/FAIL value that erases these distinctions. Use the [glossary](CONTEXT.md) for orientation and the governing [classification][ra04] and [result contracts][ra05] for the rules.

## Requirements closure: traceability is not working software

The accepted requirements baseline contained **249 requirements, 169 validation obligations and 424 inspected direct relations**. These counts describe the specification and its traceability. A requirement could be accepted, traced and allocated while still unimplemented and untested.

**Carry forward:** report specification work, implemented behavior, executed verification and human acceptance as separate facts. A traceability count is not a product-completion percentage.

Source: [requirements review and phase-gate record][ra-baseline].

## SAD-04 review: repeated descriptions can contradict an existing contract

The integrated review found two significant problems in SAD-02: a table mixed processing states with assessment outcomes and misdescribed result availability; a native JSON example used an incompatible envelope. Concrete examples were especially risky because later implementation could copy them.

RA-09's corrected baseline had already been accepted on **21 September 2026**, before the **23 September SAD-02** document. The earlier version of this journal incorrectly described RA-09 as a later accepted contract. The example contradicted an existing rule. That chronology matters when diagnosing why document layers drifted.

The review added correction notices while retaining the original text. This preserved history, but left readers to reconcile the old example with its correction. The October cleanup revisits that maintenance approach.

**Carry forward:** check examples directly against their governing contract. Put approved corrections into the active description and keep earlier text accessible in history. A resolved documentation finding is not evidence that the corresponding runtime behavior has been tested.

Sources: [SAD-04 findings][sad-review], [RA-09 acceptance][ra09-review] and [SAD-02][sad02].

## I-01 planning: an estimate remains a hypothesis

The initial I-01 estimate was **40–62 hours**. The Owner challenged it because testing alone might require comparable effort. It was retained as an uncertain forecast, not an approved budget, deadline or reason to reduce necessary testing. W02 was chosen as the first reassessment point.

**Carry forward:** revisit an estimate as concrete work reveals its cost. Include test preparation, execution, diagnosis and human review. The later [W02 forecast][effort] is also provisional; actual human effort remains unreported, so it cannot establish estimation accuracy.

Source: [SAD-04 review and effort reservation][sad-review].

## W01: expose only the capability that exists

The foundation build provided `version`, `capabilities` and controlled empty-store `init`. Package processing stayed explicitly unavailable. This avoided fake receipts, packages, review runs or findings that could make the CLI appear more complete than it was.

**Carry forward:** describe demonstrated capability directly. A foundation is useful engineering work, but it does not demonstrate the usefulness of test-case review.

Source: [W01 implementation and verification][w01].

## W01 verification: the target platform exposed a real defect

| Recorded run | Result | What it established |
| --- | --- | --- |
| Initial portable development run | 44 passed, 4 skipped | The four Windows tests had not run. |
| First native Windows run | 47 passed, 1 failed, 0 skipped | A directory held by the guard could still be renamed. |
| After the guard correction | Focused test passed; full Windows regression: 48 passed | The original scenario and regression passed after the change. |
| Corrected `0.1.0.dev2` on the target platform | 48 passed, 0 failed, 0 skipped | Verification of the identified corrected W01 build. |

The initial guard requested only `FILE_READ_ATTRIBUTES` while omitting `FILE_SHARE_DELETE`. A focused Windows experiment showed that the smallest tested access combination preventing rename was `FILE_LIST_DIRECTORY | FILE_READ_ATTRIBUTES`. Wider access combinations also worked; the detailed comparison remains in the source record.

**Carry forward:** portable success cannot establish platform-specific controls. Least privilege means the minimum authority that actually performs the required protection. Preserve the first meaningful failure and its diagnosis after a fix: they show that the test could detect the defect. The failing `0.1.0.dev1` observation and corrected `0.1.0.dev2` remain distinguishable.

Source: [W01 evidence, diagnosis and access-mask comparison][w01].

## PR #3: byte identity makes line endings part of verification

PR review identified that Windows Git line-ending conversion could change artifact bytes without an obvious textual difference. The repository introduced `* text=auto eol=lf`, then rechecked the accepted SAD-04 artifact identities.

**Carry forward:** when evidence depends on byte-level hashes, verify the actual bytes and control relevant checkout transformations. A visually identical file may have a different digest.

Source: [W01 closure and PR #3 correction evidence][w01-closure].

## W01 closure: the tested build and a later decision have different dates

Build `0.1.0.dev2` was verified with `W01_VERIFIED_CLOSURE_PENDING` in its capability manifest. The Owner closed W01 on **29 September 2026** and authorized W02. Editing the executable merely to display `W01_CLOSED` would have changed the tested artifact.

**Carry forward:** retain the identified tested build. Record the later decision with its real date and scope, and explain current status in current documentation. W01 closure did not accept the whole I-01 increment.

Source: [W01 closure decision][w01-closure].

## PR #3 and W01: useful self-review still has an independence limit

Technical self-review found documentation and evidence gaps, and corrections were made before closure. The earlier journal records that PR #3 had neither an independent reviewer nor GitHub CI status checks at that time. The Owner accepted W01 within the solo, AI-assisted project model.

**Carry forward:** describe what the review actually checked and who performed it. Its findings are useful, but calling it a review does not make it independent assurance. Stronger claims need the evidence appropriate to those claims.

Sources: [W01 closure review boundary][w01-closure] and the [earlier journal's self-review entry][earlier-journal].

## Start of W02: define expectations before observing implementation

The agreed sequence put synthetic inputs, receipt/identity expectations and the detailed test inventory before native JSON capture implementation. The intention was to derive expected behavior from accepted contracts rather than copy observed implementation behavior into tests.

This was a methodological choice, not a measured improvement. Fixture checks establish properties of prepared data and setup; they do not establish importer behavior. At the October pause, the latest preparation record reported **238 passing asset checks and 164 skipped product-test placeholders** on Linux/Python 3.12. The corresponding importer behavior and target-platform checks of those materials remained unverified.

**Carry forward:** keep independent expected outcomes, and distinguish preparation from execution. Reassess the amount and sequence of preparation when its cost delays a useful product experiment.

Sources: [W02 expected-behavior basis][w02-design], [test inventory][w02-inventory] and [last preparation record before the pause][w02-last].

## 18–19 October 2026: a written warning did not prevent documentation growth

An earlier entry in this journal already warned that formality was useful only when it prevented a concrete mistake. It identified document-growth risk and advised against duplicate summaries and ceremonial records. We did not turn that warning into a sufficiently effective working practice.

At the pause, the repository contained **80 Markdown files**, including successive document versions and sixteen W02-C preparation reports. Definitions and status descriptions were repeated across layers. Corrections were added beside retained conflicting text, and later acceptance records were needed to interpret old preparation labels. This increased the effort needed to find the applicable rule.

The review work had also found real defects, and all four SAD activities were part of the earlier plan. The audit therefore did not establish that every document or requirement was invented. It established duplication, drift and excessive process around a product whose usefulness had still not been evaluated. The assistant should have challenged this cost earlier; simplifying individual sentences had not addressed the structure.

The Owner paused development and TC-I01-033. Cleanup began with README, agent instructions and the glossary, with one proposed file explained in Polish and approved before publication. Project documentation remains in English. Approved agent guidance now favors updating current text and preserving history over creating a new file for every status change.

**Carry forward:** a lesson is useful when it changes the next decision. Give each active document a distinct purpose, maintain a rule in its governing source, and preserve necessary history without forcing readers through successive corrections. Record a new lesson when evidence changes our understanding, not after every routine step.

After cleanup, the implementation sequence still needs an explicit decision so a small useful review can be evaluated sooner. Documentation cleanup alone does not demonstrate product value, validate the effort estimate or resume development.

Sources: [repository at the pause][pause-tree], [earlier design allocation][ra-baseline], [current project status](README.md) and [approved agent guidance](AGENTS.md).

## Adding or revisiting a lesson

Use this existing journal when a decision, failure or observation materially changes product understanding, test strategy, architecture, evidence or working practice. State what happened, what supports the conclusion, what changed and what remains uncertain. Link detailed evidence instead of copying it. Routine commits, spelling fixes and ordinary passing checks do not need entries. When later evidence changes a lesson, identify the earlier view and explain the change; preserve the underlying historical record.

[charter]: docs/governance/test-design-gatekeeper-project-charter-v0.4.md
[ra01]: docs/requirements-analysis/test-design-gatekeeper-ra-01-stakeholders-actors-authority-v0.3.md
[ra04]: docs/requirements-analysis/test-design-gatekeeper-ra-04-scope-qualification-classification-boundaries-v0.2.md
[ra05]: docs/requirements-analysis/ra-05/test-design-gatekeeper-ra-05-findings-dispositions-persistence-v0.2.md
[ra-baseline]: docs/requirements-analysis/ra-10/test-design-gatekeeper-requirements-analysis-readiness-v0.2.md
[sad-review]: docs/reviews/test-design-gatekeeper-sad-04-review-record-v0.1.md
[ra09-review]: docs/requirements-analysis/ra-09/test-design-gatekeeper-ra-09-focused-static-review-v0.2.md
[sad02]: docs/solution-design/test-design-gatekeeper-sad-02-data-identity-contracts-v0.1.md
[effort]: docs/implementation/i01-w02-test-inventory.md#7-effort-reassessment
[w01]: docs/implementation/i01-w01-foundation.md
[w01-closure]: docs/implementation/i01-w01-closure.md
[w02-design]: docs/implementation/i01-w02-test-design.md
[w02-inventory]: docs/implementation/i01-w02-test-inventory.md
[w02-last]: docs/implementation/i01-w02c-imported-claims-fixtures.md
[pause-tree]: https://github.com/MarcinMikula/test-design-gatekeeper/tree/19948de4cb79b49904980ba335692752f291d3dd
[earlier-journal]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/19948de4cb79b49904980ba335692752f291d3dd/LEARNINGS.md
