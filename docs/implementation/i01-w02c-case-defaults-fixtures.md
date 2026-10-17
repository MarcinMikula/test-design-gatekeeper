# I-01 / W02-C — Defaults for missing declarations

Prepared and checked on 2026-10-17 (Europe/Warsaw).
Starting repository version: `main` at `cb741adaeecde6f8d1e50c5cd6865e97816c29e2`.
Status: **two input files prepared; four tests of TDG still need to be connected to the implementation**.

This work prepares TC-I01-028 from the accepted
[test inventory](i01-w02-test-inventory.md). A submitter can provide a default
origin or accountability declaration for a set of test cases. TDG should use it
only where the corresponding field is absent. A declaration already supplied
for an individual test case must remain unchanged.

## Prepared examples

Each file starts from [BASE-01](../../tests/fixtures/i01/base-01.json) and contains
two copies of its test case with distinct source IDs. The first omits the field
being tested; the second declares its own value. The scope, basis, steps, age
and expected result stay the same.

| Variant | Default for the native test cases | First test case: field absent | Second test case: field supplied |
| --- | --- | --- | --- |
| TC-I01-028.01 — origin | `HUMAN_AUTHORED` | Use the default origin and retain evidence that the case itself supplied no origin. | Preserve `HUMAN_CONTROLLED_AI_ASSISTED`. |
| TC-I01-028.02 — accountability | `actor_ref: qa-default-demo`, `accepted: true` | Use that default declaration and retain evidence that the case itself supplied no accountability object. | Preserve `actor_ref: qa-explicit-demo`, `accepted: true`. |

The values deliberately differ between the default and the second case. A test
can therefore detect an implementation that applies the default to both cases.
In the origin example, accountability remains absent for both cases. In the
accountability example, both retain BASE-01's explicit `HUMAN_AUTHORED` origin.

The actor names are synthetic. Both accountability objects have the correct
field types, but `accepted: true` is still a supplied declaration. It does not
establish that a person holds the required role or has taken attributable
responsibility for the test case.

| Variant | File bytes | JSON values | Maximum container depth | Native test cases |
| --- | ---: | ---: | ---: | ---: |
| TC-I01-028.01 | 1634 | 38 | 6 | 2 |
| TC-I01-028.02 | 1847 | 44 | 6 | 2 |

Both files contain one basis element, use valid UTF-8 JSON without a BOM or
duplicate members, and stay below the accepted resource limits.

## Expected preservation and import results

The [manifest](../../tests/fixtures/i01/case-defaults/manifest.json) keeps two
questions separate: what was supplied at the individual case, and which
declaration applies after using the scoped default. A missing source field stays
`ABSENT` in that record of supplied content even though an effective value is
available from `case_defaults`.

The expected effective value must point to its actual source: either the
default at `/content/case_defaults/...` or the declaration at the individual
case. The original bytes must not be rewritten to insert the default. The
manifest records exact sizes, SHA-256 digests, pointers and byte ranges for the
defaults and explicit declarations. For an absent field, it records the
containing test case; there is no invented value or byte range for that field.

These defaults apply to the native `test_cases` array. Both examples contain
only native cases and do not exercise propagation across separate sources.
Conflicting declarations must remain visible, even when an effective value can
be identified.

On the complete controlled import path, each file should produce `CAPTURED`,
a new package-version reference and two distinct retained test cases. This
assumes the approved Windows x64 / CPython 3.13 laboratory setup, synthetic-data
permission, a fresh operation ID, a healthy isolated store and effective
containment.

I-01 does not decide whether the captured package meets the minimum for review.
The receipt must retain `NOT_EVALUATED` with reason
`MINIMUM_CHECK_NOT_ENABLED_IN_I01`, and no review is performed. Applying a
default must not grant a role, infer accountable adoption or issue an eligibility
or approval decision.

The expected behavior comes from OR-I01-AUTH-003/004 and TCND-I01-07 in the
[W02 test design](i01-w02-test-design.md), traced to RA09-REQ-008 and
RA09-VAL-007. The detailed rules are
[RA-09 §§3.1–3.3 and 4.2](../requirements-analysis/ra-09/test-design-gatekeeper-ra-09-data-representations-import-export-contracts-v0.2.md).
[SAD-04 §§6.1–6.2](../solution-design/test-design-gatekeeper-sad-04-integrated-review-increment-plan-v0.2.md)
defines I-01's mechanical mapping and capture-only status boundary.

## What was checked

The [seven checks of the input files](../../tests/test_i01_case_defaults_assets.py)
passed. They verify exact bytes, the envelope, resource measurements, the two
intended case structures, all recorded source locations and the fixed expected
values. They distinguish absent fields from explicit declarations and check that
the unrelated BASE-01 content remains unchanged.

Across all twelve groups of test data, **192 checks passed and 130 product-test
placeholders were skipped**. The combined check used a fresh checkout of the
staged files with Git's automatic line-ending conversion enabled. All JSON
fixture bytes remained unchanged, as required by `.gitattributes`.

The checks ran on Linux x86_64 / CPython 3.12.14 with cached pytest 9.1.1 modules.
TDG was not installed or run under that Python version. Verification on the
target Windows/Python 3.13 environment and tests of TDG's actual default handling
remain to be done. Product regression tests were not run for this change to
test data and test placeholders.

The [four product-test placeholders](../../tests/test_i01_case_defaults_pending.py)
have explicit skips and fail guards. Two will test the mapping component; two
will test import and storage. Before enabling them, select and record the actual
mapping version and connect assertions to TDG's real observations of supplied
presence, effective values, scope, source locations and visible conflicts.

Integration tests must reopen the store and inspect it through a separate
database connection. Original bytes, both case identities, declarations, default
provenance and the receipt must agree; previous immutable records must remain
unchanged. Computing expected defaults inside a replacement mapper in the test
would not establish TDG's behavior.

Once the target environment is prepared, run:

~~~powershell
.\.venv\Scripts\python.exe -m pytest -q -rs tests/test_i01_case_defaults_assets.py tests/test_i01_case_defaults_pending.py
~~~

## Preparation correction

The first generator attempt stopped with `AssertionError` at
`raw.count(block) == 1` while locating the `case_defaults` object. Its opening
brace follows a member name on the same line, but the helper expected an object
that started on its own indented line. The first input had been written; the
manifest and second input had not yet been produced.

The temporary generator was corrected to match from the opening brace while
retaining the internal indentation and closing boundary. Both inputs and the
manifest were rebuilt. Independent checks then decoded every recorded byte
range and compared it with the intended value and containing case. The focused
test run passed without failures or warnings. This was a data-preparation defect;
TDG was not executed during the failed attempt.

## Progress and next step

Prepared data now include BASE-01, 64 input variants for 18 test cases
(TC-I01-011–028) and two valid comparison files. The full plan contains 72 cases
with 208 variants.

These synthetic examples are already visible to the author and cannot later be
described as previously unseen acceptance data. The checks were performed with
AI assistance and do not count as an independent human review. No record of human
time spent was provided; the effort estimate remains provisional.

W02 (test preparation) is still in progress. Starting W03 and accepting the whole
I-01 increment require separate decisions. The next planned task is TC-I01-029:
six examples in which explicit null, empty, unknown, mistyped, free-text or
negative declarations must not be replaced by a positive default.
