# Test Design Gatekeeper

## SAD-02 — Data, Identity and Contract Boundaries

**Historical entry.** The accepted data, identity and contract design is now maintained in [SAD-04](test-design-gatekeeper-sad-04-integrated-review-increment-plan-v0.2.md). This file keeps the original address usable and points to the current rules and the complete historical record.

## Accepted decisions and original record

The SAD-02 review closed on 2026-09-23 after the Owner accepted Sections 3–14 and SAD-D-004–008: separate logical data domains, immutable identity and lineage, versioned interchange contracts, guarded retries/writes and distinct incomplete outcomes. This closed the logical data, identity and contract activity within B-01. The Owner also clarified that TDG may identify problems and suggest improvements; the human changes the TC, and TDG has no authority to approve, directly modify or repair it.

The [complete SAD-02 snapshot][original] preserves the individual Owner replies, decision rationale, logical records, identity/version tables, lifecycle and serialization examples, failure and recovery rules, requirement/validation references, open decisions and closure record. It also retains the two correction notices added on 2026-09-28. References to the former numbered sections or recorded source hashes refer to that snapshot. Its pending-work statements describe the situation at preparation time.

## Where to read the current rules

The old lifecycle table in Section 7.1 and JSON illustration in Section 8.1 were superseded by the accepted corrections SR-SAD04-F-001 and SR-SAD04-F-002. The corrected contracts are incorporated directly into SAD-04:

| Topic from SAD-02 | Location in SAD-04 |
| --- | --- |
| SAD-D-004–008 | Section 5.1 |
| Native JSON envelope and input boundary | Section 6.1 |
| Capture, assessment, run and availability meanings | Section 6.2 |
| I-01 persistence, identity, retry and recovery | Sections 7.1–7.3 |
| Logical records and independent versions | Section 7.4 |
| Review commits, human history and export consequences | Section 7.5 |
| Remaining design choices and planned verification | Sections 10 and 12 |

The SAD-02 closure was a design decision, with no implementation or confidential-use permission and no executed product-test or independent-review evidence. Later implementation choices and the I-01 gate are recorded in SAD-04. Current development remains paused for documentation cleanup; see [README.md](../../README.md). This consolidation changes no accepted product contract.

[original]: https://github.com/MarcinMikula/test-design-gatekeeper/blob/6bf96d9748c1d4faae049786feb8c49397f4c659/docs/solution-design/test-design-gatekeeper-sad-02-data-identity-contracts-v0.1.md
