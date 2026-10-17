# I-01 / W02-C — Preserve explicit declarations when defaults exist

Prepared and checked on 2026-10-17 (Europe/Warsaw).
Starting repository version: `main` at `e38a8165f7a45a2e3cf3a72a7b53a3b6ba72cb67`.
Status: **six input files prepared; twelve tests of TDG still need to be connected to the implementation**.

This work prepares TC-I01-029 from the accepted
[test inventory](i01-w02-test-inventory.md). A default can fill a missing field,
but it must not replace a value that was actually supplied. This includes values
that are empty, invalid, unresolved or negative.

## Prepared examples

Each file starts from [BASE-01](../../tests/fixtures/i01/base-01.json), adds
`case_defaults` and changes one declaration in its single test case. The
scope, basis, source ID, steps, age and expected result stay the same.

The first five files provide `HUMAN_AUTHORED` as the default origin. The sixth
provides `actor_ref: qa-default-demo` and `accepted: true` as the default
accountability declaration.

| Variant | Value supplied for the individual case | Presence to preserve | File bytes |
| --- | --- | --- | ---: |
| TC-I01-029.01 | `origin: null` | `NULL` | 1102 |
| TC-I01-029.02 | `origin: ""` | `EMPTY` | 1100 |
| TC-I01-029.03 | `origin: "UNKNOWN"` | `VALUE` | 1107 |
| TC-I01-029.04 | `origin: []` | `TYPE_MISMATCH` | 1100 |
| TC-I01-029.05 | `origin: "written by QA engineer"` | `VALUE` | 1122 |
| TC-I01-029.06 | Accountability object with `actor_ref: qa-default-demo` and `accepted: false` | `VALUE` | 1289 |

All six target fields are present. In every example, the original declaration
must remain and the default must not be applied.

An empty array is the wrong type for the text-only origin field, even though it
contains no entries. It must not be reported as an empty text value. Likewise,
`false` is an explicit Boolean declaration, not a missing accountability field.

The negative accountability example uses the same actor reference in the
default and the individual case. Only `accepted` differs, so replacing
`false` with `true` cannot be hidden by an unrelated actor change. The name is
synthetic, and neither Boolean value grants a role or proves human adoption.

Each file contains one native test case and one basis element. The first five
have 26 JSON values; the accountability example has 31. All have a maximum
container depth of six, use valid UTF-8 JSON without a BOM or duplicate members,
and stay below the accepted resource limits.

## Expected preservation and import results

`UNKNOWN` remains a recognized origin literal with code `UNKNOWN`.
The free-text phrase remains `UNMAPPED` under a selected mapping that has no
agreed entry or alias for it. Its reference to a job title must not establish
authorship, AI involvement or accountable adoption.

Null, empty text and a mistyped array do not establish a canonical origin code.
Their original values, presence and applicable mapping issues must remain
visible. The [manifest](../../tests/fixtures/i01/default-preservation/manifest.json)
records these observations separately; it does not invent a runtime mapping
enum for an invalid field or require a particular null/missing field shape in
TDG's output. Conflicting declarations must remain visible without replacing
the supplied value.

The manifest records exact sizes, SHA-256 digests, source pointers and byte
ranges for both defaults and individual declarations. The supplied JSON null
has actual source bytes: `null`. It is not an absent field. The final variant
also locates the exact `false` token inside the accountability object.

The existing [TC-I01-028 examples](i01-w02c-case-defaults-fixtures.md) provide
comparison cases where the same fields are absent and the same defaults do
apply. They are reused without adding new comparison files. Together, these
inputs distinguish a missing field from an explicit value that must be kept.

On the complete controlled import path, each new file should produce
`CAPTURED` and a new package-version reference. These expectations assume the
approved Windows x64 / CPython 3.13 laboratory setup, synthetic-data permission,
a fresh operation ID, a healthy isolated store and effective containment.

I-01 does not decide whether the package meets the minimum conditions for review.
The receipt must retain `NOT_EVALUATED` with reason
`MINIMUM_CHECK_NOT_ENABLED_IN_I01`, and no review is performed. The defaults
must not create positive eligibility, attributable human adoption or authority.

The expected behavior comes from OR-I01-AUTH-004/005 and TCND-I01-07 in the
[W02 test design](i01-w02-test-design.md), traced to RA09-REQ-008/024 and
RA09-VAL-007/008. The detailed rules are
[RA-09 §§3.1–3.3 and 4.2](../requirements-analysis/ra-09/test-design-gatekeeper-ra-09-data-representations-import-export-contracts-v0.2.md).
[SAD-04 §§6.1–6.2](../solution-design/test-design-gatekeeper-sad-04-integrated-review-increment-plan-v0.2.md)
defines the corresponding I-01 mapping and capture-only status boundary.

## What was checked

The [14 checks of the input files](../../tests/test_i01_default_preservation_assets.py)
passed. They verify exact bytes, the envelope, resource measurements, the intended
changes from BASE-01, all recorded source locations and the six fixed expected
observations. They also compare the default values with the existing absent-field
controls and distinguish a Boolean `false` from numeric or textual substitutes.
The focused run had no failures or warnings.

Across all thirteen groups of test data, **206 checks passed and 142 product-test
placeholders were skipped**. The combined check used a fresh checkout of the
staged files with Git's automatic line-ending conversion enabled. All JSON
fixture bytes remained unchanged, as required by `.gitattributes`.

The checks ran on Linux x86_64 / CPython 3.12.14 with cached pytest 9.1.1 modules.
TDG was not installed or run under that Python version. Verification on the
target Windows/Python 3.13 environment and tests of TDG's actual default handling
remain to be done. Product regression tests were not run for this change to test
data and test placeholders.

The [twelve product-test placeholders](../../tests/test_i01_default_preservation_pending.py)
have explicit skips and fail guards. Six will test the mapping component; six
will test import and storage. Before enabling them, bind the actual versioned
mapping and inspect TDG's preserved values, source locations, presence, origin
resolution, visible issues and decision not to apply the default.

Integration tests must reopen the store and inspect it through a separate
database connection. Original bytes, retained declarations, identities,
provenance and receipt must agree; previous immutable records must remain
unchanged. A replacement mapper written inside the tests would not establish
TDG's behavior.

Once the target environment is prepared, run:

~~~powershell
.\.venv\Scripts\python.exe -m pytest -q -rs tests/test_i01_default_preservation_assets.py tests/test_i01_default_preservation_pending.py
~~~

## Progress and next step

Prepared data now include BASE-01, 70 input variants for 19 test cases
(TC-I01-011–029) and two valid comparison files. The full plan contains 72 cases
with 208 variants.

These synthetic examples are already visible to the author and cannot later be
described as previously unseen acceptance data. The checks were performed with
AI assistance and do not count as an independent human review. No record of human
time spent was provided; the effort estimate remains provisional.

W02 (test preparation) is still in progress. Starting W03 and accepting the whole
I-01 increment require separate decisions. The next planned task is TC-I01-030:
a supplied `accepted: true`, actor reference and role claim must not create
human authority that is absent from the trusted operation context.
