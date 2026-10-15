# I-01 / W02-C — Incomplete and unfamiliar content

Prepared and first checked on 2026-10-14 (Europe/Warsaw).
Final verification completed on 2026-10-15.
Starting repository version: `main` at `74fa190c08e2b19149d6948eb53340f6fe2b48f8`.
Status: **three input files prepared; six tests of TDG still need to be connected to the implementation**.

This work prepares TC-I01-025 from the accepted
[test inventory](i01-w02-test-inventory.md). It checks a distinction that matters
to import: a document can have the correct outer JSON structure while containing
incomplete or unfamiliar test data. Under the accepted safety conditions, TDG
should preserve that content and make its problems visible.

## Prepared examples

All three files start from [BASE-01](../../tests/fixtures/i01/base-01.json).
The document type, contract version, scope and test basis stay the same.
Each file changes one part of `content`.

| Variant | Input | Expected behavior when TDG is tested |
| --- | --- | --- |
| TC-I01-025.01 | A new `vendor_extension` object contains a nested marker and the values `0`, `false`, `null` and `""`. | Keep the unfamiliar subtree, its source location and its `UNMAPPED` status. Preserve the values even though they are all false in a Boolean check; expose the applicable issue or limitation. |
| TC-I01-025.02 | `test_cases` contains a single TC object instead of an array. | Keep the supplied object as a raw, located value and report `TYPE_MISMATCH`. Do not silently wrap it in an array or replace it with an empty one. |
| TC-I01-025.03 | The TC array contains one object with only a title. | Keep the record and its missing fields visible. Do not add an ID, steps, expected results, nulls or defaults that were not supplied. |

The [manifest](../../tests/fixtures/i01/deficient-content/manifest.json) records
each file's exact size and SHA-256 digest, the relevant JSON Pointer and the byte
range containing its value. Missing fields in the title-only example have no
value bytes; the containing TC at `/content/test_cases/0` is the evidence of absence.
In the malformed example, the count of TC array entries is recorded as unavailable
(`null` in this test metadata), because the source contains no TC array. This is
not the same as an empty array containing zero entries.

| Variant | File bytes | JSON values | Maximum container depth |
| --- | ---: | ---: | ---: |
| TC-I01-025.01 | 1237 | 32 | 6 |
| TC-I01-025.02 | 1003 | 23 | 5 |
| TC-I01-025.03 | 583 | 13 | 4 |

All files use valid UTF-8 JSON without duplicate members or a BOM. Their other
sizes and counts stay below the accepted limits. BASE-01 provides the comparison
input; no additional control file is needed.

## Expected import results

For each example, the complete import path should return `CAPTURED` and a new
package-version reference after a successful commit. Original bytes, source
locations, visible issues and the preserved content must agree with the receipt.
These expectations assume the approved Windows x64 / CPython 3.13 laboratory
setup, synthetic-data permission, a fresh operation ID, a healthy isolated store
and effective containment.

Import success does not mean that a TC is ready for review. In I-01, the minimum
check is disabled: its result must remain `NOT_EVALUATED`, with reason
`MINIMUM_CHECK_NOT_ENABLED_IN_I01`, and no review is performed. In particular,
the title-only input must not cause the importer to invent a `MET` or `NOT_MET`
review-minimum verdict. It records the supplied content and its deficiencies.

The expected behavior comes from OR-I01-FID-004 and OR-I01-ENV-007 in the
[W02 test design](i01-w02-test-design.md), covering TCND-I01-06/15;
RA09-REQ-006/012, RA03-REQ-025 and RA09-VAL-002/003. The detailed contracts are
[RA-09 §§3.1–3.3](../requirements-analysis/ra-09/test-design-gatekeeper-ra-09-data-representations-import-export-contracts-v0.2.md)
and [SAD-04 §§6.1–6.2](../solution-design/test-design-gatekeeper-sad-04-integrated-review-increment-plan-v0.2.md).

## What was checked

The [13 checks of the input files](../../tests/test_i01_deficient_content_assets.py)
passed. They verify the exact bytes, valid envelope, size limits, intended changes
from BASE-01, original locations and the differences between missing, empty and
mistyped data. They also check that the manifest preserves the accepted import
expectations. The first focused run had no failures or warnings.

Across all nine groups of test data, **166 checks passed and 114 product-test
placeholders were skipped**. These checks ran on Linux x86_64 / CPython 3.12.14
with cached pytest 9.1.1 modules. TDG was not installed or run under that Python
version. Tests of import behavior and verification on Windows/Python 3.13 still
need to be done; these results only check the prepared materials. Product
regression tests were not run for this change to test data and test placeholders.

The [six new product-test placeholders](../../tests/test_i01_deficient_content_pending.py)
have explicit skips and fail guards. Removing a skip without adding assertions
will fail the test. Three are unit tests of content projection, source locations
and issues. Three are integration tests of import and storage. Before enabling
them, connect them to TDG's real output and issue fields; diagnostic code names
remain to be bound to the implementation, rather than invented in these files.

The integration tests must inspect committed originals, projection, inventory,
issues, identities and receipt through a separate database connection after
reopening the store. They must also verify that previous immutable records were
not changed. If safe field projection is impossible, check the retained raw
subtree or trustworthy opaque boundary and the visible limitation. Reading the
fixture itself does not prove that TDG saved it correctly.

Once the target environment is prepared, run:

~~~powershell
.\.venv\Scripts\python.exe -m pytest -q -rs tests/test_i01_deficient_content_assets.py tests/test_i01_deficient_content_pending.py
~~~

## Progress and next step

Prepared data now include BASE-01, 55 input variants for 15 test cases
(TC-I01-011–025) and two valid comparison files. The full plan contains 72 cases
with 208 variants, so more input files and product tests remain to be prepared.

These are synthetic examples used during development. They are already visible
to the author and cannot later be described as previously unseen acceptance data.
The checks recorded here were performed with AI assistance and do not count as an
independent human review. No record of human time spent was provided; the effort
estimate remains provisional.

W02 (test preparation) is still in progress. Finishing these files does not
authorize W03 or accept the whole I-01 product increment. The next planned task
is TC-I01-026: five supplied origin values, preserved and mapped without granting
human authority or making an eligibility decision.
