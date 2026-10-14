# I-01 / W02-C — Step representation fixtures

Prepared and first checked 2026-10-09; combined verification and publication
slice 2026-10-10 (Europe/Warsaw).
Source pin: `main` at `8cdcb8f05db2d2f02a952b8f3bd4ef9d3fae8a89`.
Status: **three variants prepared; tests of TDG behavior still need to be connected to the implementation**.

Reading this record: *fixtures* are prepared input files and test setup.
*Asset checks* verify those files. *Product skeletons* are placeholders for tests
of TDG itself; they are skipped until connected to the implementation.
The dated results below describe the state at that point in the project.
Wording clarified on 2026-10-14; recorded results and decisions are unchanged.

This document records the test data prepared for TC-I01-022 from the accepted
[W02-B inventory](i01-w02-test-inventory.md). The
[manifest](../../tests/fixtures/i01/step-representation/manifest.json) records
source sizes/digests and value spans, expected supplied steps, occurrence counts,
numbering, expectation locators, U/I levels and E1/E2 obligations. These are test
observations, not a new product schema or executable-step model.

## Inputs and distinguishing observations

Only the `steps` value changes from [BASE-01](../../tests/fixtures/i01/base-01.json).
All surrounding bytes and other TC dimensions stay unchanged; in particular,
there is no supplied TC-level `expected_result` member.

| Variant | Supplied representation | Required observation |
| --- | --- | --- |
| TC-I01-022.01 | One narrative string with two numbered actions and two expectation lines | Preserve one text value, its three line breaks and indentation; no invented structured/executable actions |
| TC-I01-022.02 | Ordered array: enter age 30, then submit registration | Retain two distinct steps in source order and their nested `expected_result` values/locations |
| TC-I01-022.03 | Three array entries numbered `"02"`, `"02"`, `"01"`; the first two objects are identical | Retain all three occurrences and supplied numbers in array order; no deduplication, sorting or renumbering |

The narrative's line breaks are escaped in JSON and decoded as three LF
characters. Its expectation prose stays in the narrative. In the two array
variants, expectations remain attributable to each step's source location.
They are not invented as a supplied TC-level expected result.

The source member `number` is a fixture convention for supplied numbering,
not a newly mandatory schema field or permission to guess a mapping alias.
Whether mapped directly or retained as located source content, those values
must not be silently dropped or used to reorder the steps. Equal array members
have separate source positions even when all their supplied values match.

Files are respectively 1012, 1152 and 1360 bytes, with 21, 27 and 33 JSON values.
The narrative input has maximum container depth 5; both arrays have depth 6.
All retain maximum decoded text/member-name size 154 UTF-8 bytes, one TC and one
basis element, below the other accepted limits. No additional control file is
introduced. Raw spans include the narrative quotes/escapes or the complete array
layout; these are fixture coordinates, not a mandated product API.

## Oracles and binding boundary

Trace: TCND-I01-01/06; OR-I01-FID-002 in the
[W02 oracle basis](i01-w02-test-design.md); RA09-REQ-006/007 and RA09-VAL-006,
with RA03-REQ-006/022 upstream. Governing clauses are
[RA-09 §3.2–3.3](../requirements-analysis/ra-09/test-design-gatekeeper-ra-09-data-representations-import-export-contracts-v0.2.md)
and [SAD-04 §6.1](../solution-design/test-design-gatekeeper-sad-04-integrated-review-increment-plan-v0.2.md).

Every controlled complete path expects CAPTURED with coherent retained original,
projection and receipt; a new version reference appears only after commit.
Minimum remains NOT_EVALUATED with MINIMUM_CHECK_NOT_ENABLED_IN_I01, and no
substantive review is performed. Source representation, order, repetition,
numbering and nested expectations survive without repair or invented actions.
The context remains eligible Windows x64 / CPython 3.13 laboratory operation,
a fresh operation ID, healthy isolated store and effective containment.

[Product skeletons](../../tests/test_i01_step_representation_pending.py) contain
three U and three I placeholders with explicit skips and fail guards. Before
enabling them, bind actual representation/occurrence/source observations and the
real capture service. Verify retained bytes, projection/source references and
receipt through a separate store connection after commit/reopen, preserving
prior immutable records. Check each duplicate position separately; compare
ordered arrays rather than sets. A whole-source digest alone cannot prove that
the projection preserves step order, and capture success alone cannot prove
that an absent TC-level expected result was not invented.

<a id="preparation-evidence-and-handoff"></a>

## What was checked and what remains to do

[Asset checks](../../tests/test_i01_step_representation_assets.py) verify exact
bytes, independent resource measures, the isolated steps replacement, fixed
expected content and source spans. Additional observations distinguish narrative
lines from array entries, nested expectation positions, reversed arrays and
deduplicated/sorted/renumbered in-memory witnesses. No TDG parser or store supplies
the expected values, and source fixtures are not rewritten by the checks.

The first focused run on 2026-10-09 passed: **11 new asset checks; six product
skeletons skipped**. Combined verification on 2026-10-10 across all six families:
**129 passed; 96 skipped**, on Linux x86_64 / CPython 3.12.14 with cached pytest
9.1.1 modules. TDG was not installed or run under 3.12. Target Windows/Python 3.13
verification and product E2 observations remain pending; product regression was
not rerun for this change to test data and test placeholders. Existing assets and accepted snapshots stay
unchanged.

On a prepared target environment:

~~~powershell
.\.venv\Scripts\python.exe -m pytest -q -rs tests/test_i01_step_representation_assets.py tests/test_i01_step_representation_pending.py
~~~

At the time of this record, the prepared files included the baseline example
`BASE-01` and 46 input variants for twelve test cases (TC-I01-011–022).
This covers group B and TC-I01-021–022 in group C.
Two additional valid files serve as comparison examples.
The complete plan contains 72 test cases with 208 input variants, so more
test data remain to be prepared. These counts describe files prepared, not
tests passed by TDG. One input variant can be used by several automated checks,
so the number of pytest results differs from the number of input variants.

These files contain synthetic examples used while developing TDG. Because they
are already available to the author, they are not a separate, previously unseen
set for acceptance testing. The checks recorded here were performed by the
author with AI assistance. They do not count as an independent human review.

No record of human time spent was provided for this work. The estimate of
remaining work is still provisional and will be checked against actual effort.
Preparing these files does not finish W02 (test preparation), authorize W03
(the next work item), or mean that I-01 (the first product increment) has been
accepted.

Next planned task at the time of this record: TC-I01-023, repeated source identifiers on separate TC or
basis elements and the resulting ambiguous reference.
