# Test Design Gatekeeper

## SAD04-I01-NUM-001 — I-01 numeric-token limit decision

**Accepted decision record.** The rule is incorporated into [SAD-04 Section 6.1][current]. This file preserves the human decision and its scope.

| Field | Recorded state |
| --- | --- |
| Decision ID | SAD04-I01-NUM-001 |
| Decision date | 2026-10-03 (Europe/Warsaw) |
| Original record prepared | 2026-10-04 (Europe/Warsaw) |
| Status | ACCEPTED — explicit Project Owner decision |
| Trigger | [W02 Section 9.5][trigger] |

## Decision and acceptance evidence

The Owner accepted rejection of an otherwise valid native JSON input when the bounded input check detects a numeric token longer than 128 characters: `REJECTED`, CLI exit `2`, no new package version/reference and minimum `NOT_EVALUATED`. The diagnostic identifies the limit and safe affected location without exposing raw numeric content or an unnecessary host path.

The Owner confirmed on 2026-10-03:

> tak potwierdzam, idzmy dalej

The decision resolved W02 Section 9.5's numeric-outcome question. It did not accept the W02-B inventory, close W02, authorize confidential input or establish executed product evidence. Its scope is the numeric-token bound; outcomes for other limits and operational failures remain governed by their own rules.

## Current rule and history

Read [SAD-04 Section 6.1][current] for the full rule, including 127/128-character boundary handling, source fidelity and rejection-receipt persistence failure; Sections 8 and 9 retain the CLI and resource contracts.

The [original addendum snapshot][original] preserves the full earlier wording, outcome table and publication context. Recorded historical hashes refer to that snapshot. This cleanup changes neither the accepted outcome nor the limit.

[current]: test-design-gatekeeper-sad-04-integrated-review-increment-plan-v0.2.md#61-native-input-and-mechanical-projection
[trigger]: ../implementation/i01-w02-test-design.md#95-numeric-token-limit-accepted-outcome-mapping
[original]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/6bf96d9748c1d4faae049786feb8c49397f4c659/docs/solution-design/test-design-gatekeeper-sad-04-i01-numeric-token-limit-addendum-v0.1.md
