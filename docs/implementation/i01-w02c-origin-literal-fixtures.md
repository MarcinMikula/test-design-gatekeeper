# I-01 / W02-C — Declared origin of a test case

Prepared and checked on 2026-10-15.
Starting repository version: `main` at `c8f5870f3a6e8894fd82efaffbbd342215c4cfe5`.
Status: **five input variants prepared; ten tests of TDG still need to be connected to the implementation**.

This work prepares TC-I01-026 from the accepted
[test inventory](i01-w02-test-inventory.md). The `origin` field records what the
submitter says about how a test case was created. TDG should preserve each of the
five recognized values and its meaning. That declaration alone does not establish
that an identified person has taken responsibility for the test case.

## Prepared examples

Each file uses [BASE-01](../../tests/fixtures/i01/base-01.json) and changes only
the `origin` value in its single test case. The first variant is an exact copy of
BASE-01, which already declares `HUMAN_AUTHORED`.

| Variant | Supplied value | Meaning of the declaration | File bytes |
| --- | --- | --- | ---: |
| TC-I01-026.01 | `HUMAN_AUTHORED` | A human wrote the test case. | 1051 |
| TC-I01-026.02 | `HUMAN_CONTROLLED_AI_ASSISTED` | A human controlled the work and used AI assistance. | 1065 |
| TC-I01-026.03 | `WITHOUT_ACCOUNTABLE_ADOPTION` | The test case has not been adopted by an accountable human. | 1065 |
| TC-I01-026.04 | `OTHER` | The declared origin is another category. | 1042 |
| TC-I01-026.05 | `UNKNOWN` | The submitter declares that the origin is unknown. | 1044 |

All five values are defined by the contract. With the selected mapping that
implements these definitions, each should retain its original text and receive
the corresponding origin code with status `MAPPED`. In particular, `UNKNOWN`
is a recognized declaration; it must not be confused with an unrecognized text
value, which has status `UNMAPPED`.

None of these inputs supplies `accountability` or `case_defaults`. The importer
must keep that absence visible, including for the two values that describe human
involvement. The labels are part of synthetic test submissions; they do not
describe who actually wrote these fixture files.

The [manifest](../../tests/fixtures/i01/origin-literals/manifest.json) records
exact sizes, SHA-256 digests and the location of each original value at
`/content/test_cases/0/origin`, including its byte range. Each file has 24 JSON
values, a maximum container depth of six, one test case and one basis element.
All use valid UTF-8 JSON without a BOM or duplicate members and stay below the
accepted size and count limits. The scope, test basis, steps and expected result
are unchanged. BASE-01 supplies the comparison input.

## Expected import results

For all five examples, the complete import path should return `CAPTURED` and a
new package-version reference after a successful commit. These expectations
assume the approved Windows x64 / CPython 3.13 laboratory setup, synthetic-data
permission, a fresh operation ID, a healthy isolated store and effective
containment. The declared origin alone does not prevent capture.

I-01 does not decide whether a test case meets the minimum conditions for review.
The receipt must therefore retain `NOT_EVALUATED` with reason
`MINIMUM_CHECK_NOT_ENABLED_IN_I01`, and inspection must say that no review was
performed. Importing a declaration must not grant a human role, create a record
of responsibility or produce an eligibility or approval decision.

The expected behavior comes from OR-I01-AUTH-001 and OR-I01-RCP-004 in the
[W02 test design](i01-w02-test-design.md), covering TCND-I01-07/15. The governing
requirements are RA09-REQ-008, RA03-REQ-021/032/050 and RA09-REQ-013/015/017,
with validation obligation RA09-VAL-007. The detailed contracts are
[RA-09 §4.2](../requirements-analysis/ra-09/test-design-gatekeeper-ra-09-data-representations-import-export-contracts-v0.2.md)
and [SAD-04 §§6.1–6.2](../solution-design/test-design-gatekeeper-sad-04-integrated-review-increment-plan-v0.2.md).

## What was checked

The [13 checks of the input files](../../tests/test_i01_origin_literal_assets.py)
passed. They verify the exact bytes, valid envelope, resource measurements,
original value locations, the five distinct declarations and the absence of
accountability data. They also check that only `origin` changes from BASE-01 and
that the manifest retains the accepted expectations. The focused run had no
failures or warnings.

Across all ten groups of test data, **179 checks passed and 124 product-test
placeholders were skipped**. The combined check used a fresh checkout of the
staged files with Git's automatic line-ending conversion enabled. All JSON
fixture bytes remained unchanged, as required by `.gitattributes`.

These checks ran on Linux x86_64 / CPython 3.12.14 with cached pytest 9.1.1 modules.
TDG was not installed or run under that Python version. Tests of import behavior
and verification on Windows/Python 3.13 still need to be done. The results above
check the prepared materials; they do not establish that TDG imports them
correctly. Product regression tests were not run for this change to test data
and test placeholders.

The [ten new product-test placeholders](../../tests/test_i01_origin_literal_pending.py)
have explicit skips and fail guards: removing a skip without adding the real
checks will fail the test. Five unit tests will check preserved declarations,
their mapped codes, source locations and absent accountability. Five integration
tests will check import, storage and the receipt.

Before enabling them, select and record the actual mapping version that
implements the five contract values. The tests must inspect TDG's output and
the recorded mapping identity, rather than reproduce a mapper inside the test.
Integration checks must reopen the store and use a separate database connection
to inspect committed originals, projection, identities and receipt. They must
verify that accountability remains absent, no authority was inferred and previous
immutable records were not changed. Reading these fixture files alone cannot
establish those outcomes.

Once the target environment is prepared, run:

~~~powershell
.\.venv\Scripts\python.exe -m pytest -q -rs tests/test_i01_origin_literal_assets.py tests/test_i01_origin_literal_pending.py
~~~

## Progress and next step

Prepared data now include BASE-01, 60 input variants for 16 test cases
(TC-I01-011–026) and two valid comparison files. The full plan contains 72 cases
with 208 variants, so more input files and product tests remain to be prepared.

These synthetic examples are already visible to the author and cannot later be
described as previously unseen acceptance data. The checks were performed with
AI assistance and do not count as an independent human review. No record of human
time spent was provided; the effort estimate remains provisional.

W02 (test preparation) is still in progress. Starting W03 and accepting the whole
I-01 increment require separate decisions. The next planned task is TC-I01-027:
preserve two unrecognized origin declarations, including lowercase
`human_authored` when the selected mapping defines no alias for it, without
guessing their meaning.
