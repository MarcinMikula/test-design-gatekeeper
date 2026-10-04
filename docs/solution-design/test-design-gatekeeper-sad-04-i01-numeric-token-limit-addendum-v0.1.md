# Test Design Gatekeeper

## SAD-04 addendum v0.1 — I-01 numeric-token limit outcome

| Field | Recorded state |
| --- | --- |
| Decision ID | SAD04-I01-NUM-001 |
| Decision date | 2026-10-03 (Europe/Warsaw) |
| Record prepared | 2026-10-04 (Europe/Warsaw) |
| Status | ACCEPTED — explicit Project Owner decision |
| Governing baseline | [SAD-04 v0.2](test-design-gatekeeper-sad-04-integrated-review-increment-plan-v0.2.md), Sections 6.1, 8 and 9 |
| Trigger | [W02 §9.5](../implementation/i01-w02-test-design.md#95-numeric-token-limit-accepted-outcome-mapping) |
| Repository before publication | `0dc8d61144e82271839194de1fa7a466bbb4f92b` |

### 1. Decision evidence

The Owner was asked whether a numeric token exceeding the 128-character limit
should produce `REJECTED` and CLI exit `2`. The proposal also stated that no
package version is created, the minimum remains `NOT_EVALUATED`, and diagnostics
identify the limit and affected location without exposing raw content.

The Owner confirmed on 2026-10-03:

> tak potwierdzam, idzmy dalej

This records that concrete decision. It does not accept the W02-B inventory,
close W02, authorize confidential input, or establish executed product evidence.

### 2. Accepted clarification

For an otherwise valid native JSON input, a numeric token longer than 128
characters violates the I-01 input contract. When this violation is detected
during the bounded input check, stop before capture commit and apply:

| Observable | Required result |
| --- | --- |
| Capture outcome | `REJECTED` |
| CLI exit code | `2` |
| Package version/reference | No new package version or committed package reference |
| Core minimum | `NOT_EVALUATED`; no substantive review |
| Diagnostic | Explicit numeric-token limit cause and safe affected location; no raw numeric payload or unnecessary host path |

The existing permission, safe-retention and persistence rules still apply.
A separate inability to persist a rejection receipt must remain visible; this
decision does not fabricate durable history when storage fails.

Tokens of 127 and 128 characters do not violate this length bound. They still
undergo the remaining checks. Do not round, truncate or coerce an over-limit
number to make it fit. An in-bound exact-representation limitation remains a
separate source-fidelity/projection concern under RA-09 §3.3 and SAD-04 §6.1.

### 3. Precedence and scope

Read this addendum with the frozen SAD-04 v0.2 baseline and its accepted closure
record. It supplies the previously unspecified numeric-token outcome/exit pair;
it does not rewrite those historical files or their recorded hashes.

The classification is specific to the numeric-token bound. It does not assign
outcomes to other resource limits, worker timeouts, containment failures or
persistence faults. Their accepted cause/stage rules remain applicable.

W02 §9.5's decision prerequisite is resolved by this record. Implementation and
runtime verification remain future work.
