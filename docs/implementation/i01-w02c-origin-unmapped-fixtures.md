# I-01 / W02-C — Unrecognized origin declarations

Prepared and checked on 2026-10-16 (Europe/Warsaw).
Starting repository version: `main` at `bafb8537ea48c74293a6f71f443bc18116d925e2`.
Status: **two input files prepared; two tests of TDG still need to be connected to the implementation**.

This work prepares TC-I01-027 from the accepted
[test inventory](i01-w02-test-inventory.md). It checks that TDG keeps an origin
declaration when its meaning has not been agreed, instead of guessing who wrote
the test case or silently changing the text into a recognized code.

## Prepared examples

Each file starts from [BASE-01](../../tests/fixtures/i01/base-01.json) and changes
only the `origin` value in its single test case.

| Variant | Supplied text | Expected behavior when TDG is tested | File bytes |
| --- | --- | --- | ---: |
| TC-I01-027.01 | `written by QA engineer` | Keep the text and mark its meaning `UNMAPPED`. The job title does not establish authorship, AI involvement or accountable human adoption. | 1059 |
| TC-I01-027.02 | `human_authored` | Keep the lowercase spelling and mark its meaning `UNMAPPED` when the selected mapping defines no alias for it. | 1051 |

The selected, versioned mapping must recognize the control value
`HUMAN_AUTHORED` and have no entry or alias for either test value. No human
resolution of their meaning is supplied. This setup matters: a later, explicitly
agreed mapping could recognize additional source values. These tests check that
TDG does not invent such a mapping.

BASE-01 provides the uppercase comparison value. The lowercase input differs
from it only in those letters. The scope, basis, steps and expected result remain
unchanged in both new files. Neither input supplies `accountability` or
`case_defaults`.

The [manifest](../../tests/fixtures/i01/origin-unmapped/manifest.json) records
exact file sizes, SHA-256 digests and the original value location at
`/content/test_cases/0/origin`, including its byte range. Each file has 24 JSON
values, a maximum container depth of six, one test case and one basis element.
Both use valid UTF-8 JSON without a BOM or duplicate members and stay below the
accepted size and count limits.

## Expected mapping results

Both sources contain a non-empty text value, so field presence is `VALUE`.
Their meaning remains `UNMAPPED`. These are separate observations: TDG can
preserve exactly what was supplied while leaving its meaning unresolved.

No canonical origin code should be inferred, including `HUMAN_AUTHORED`,
`OTHER` or `UNKNOWN`. The literal `UNKNOWN` is a separate, recognized
declaration in [TC-I01-026](i01-w02c-origin-literal-fixtures.md). It must not be
substituted for text that the selected mapping does not recognize.

In this manifest, `expected_origin_code: null` records the absence of an
established code. It does not mean that the source contains JSON null, and it
does not prescribe TDG's runtime field representation. The original text,
its source location and its unresolved mapping must remain observable. The
declaration must not create a record of human responsibility or grant a role.

The expected behavior comes from OR-I01-AUTH-002 and TCND-I01-07 in the
[W02 test design](i01-w02-test-design.md), traced to RA09-REQ-008,
RA03-REQ-021 and RA09-VAL-007. The governing rule is
[RA-09 §4.2](../requirements-analysis/ra-09/test-design-gatekeeper-ra-09-data-representations-import-export-contracts-v0.2.md).

## What was checked

The [six checks of the input files](../../tests/test_i01_origin_unmapped_assets.py)
passed. They verify exact bytes, the document envelope, resource measurements,
the original value locations and the intended differences from BASE-01. They
also check that the manifest retains the two expected `UNMAPPED` results and
the required mapping setup. The focused run had no failures or warnings.

Across all eleven groups of test data, **185 checks passed and 126 product-test
placeholders were skipped**. The combined check used a fresh checkout of the
staged files with Git's automatic line-ending conversion enabled. All JSON
fixture bytes remained unchanged, as required by `.gitattributes`.

These checks ran on Linux x86_64 / CPython 3.12.14 with cached pytest 9.1.1 modules.
TDG was not installed or run under that Python version. Verification on the
target Windows/Python 3.13 environment and tests of TDG's actual mapping remain
to be done. Product regression tests were not run for this change to test data
and test placeholders.

The [two product-test placeholders](../../tests/test_i01_origin_unmapped_pending.py)
follow the inventory's unit/component level. Each has an explicit skip and a
fail guard: removing the skip without adding the real checks will fail the test.
Before enabling them, bind the actual mapping version and confirm that it
recognizes the uppercase control but neither test value.

The tests must inspect the real component's preserved text, source location,
presence and mapping result. They must also check that no origin meaning,
accountable adoption or authority was inferred. A replacement mapper written
inside the test would not establish TDG's behavior. Complete import and storage
checks remain covered by other inventory rows.

Once the target environment is prepared, run:

~~~powershell
.\.venv\Scripts\python.exe -m pytest -q -rs tests/test_i01_origin_unmapped_assets.py tests/test_i01_origin_unmapped_pending.py
~~~

## Progress and next step

Prepared data now include BASE-01, 62 input variants for 17 test cases
(TC-I01-011–027) and two valid comparison files. The full plan contains 72 cases
with 208 variants.

These synthetic examples are already visible to the author and cannot later be
described as previously unseen acceptance data. The checks were performed with
AI assistance and do not count as an independent human review. No record of human
time spent was provided; the effort estimate remains provisional.

W02 (test preparation) is still in progress. Starting W03 and accepting the whole
I-01 increment require separate decisions. The next planned task is TC-I01-028:
check how explicit defaults apply to absent origin or accountability fields while
preserving declarations already supplied for an individual test case.
