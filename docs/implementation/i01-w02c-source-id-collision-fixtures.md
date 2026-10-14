# I-01 / W02-C — Source-ID collision fixtures

Prepared and checked 2026-10-10 (Europe/Warsaw).
Source pin: `main` at `c466cca4165a40bb92885d94c2c3ca9d00af9126`.
Status: **two variants prepared; tests of TDG behavior still need to be connected to the implementation**.

Reading this record: *fixtures* are prepared input files and test setup.
*Asset checks* verify those files. *Product skeletons* are placeholders for tests
of TDG itself; they are skipped until connected to the implementation.
The dated results below describe the state at that point in the project.
Wording clarified on 2026-10-14; recorded results and decisions are unchanged.

This document records the test data prepared for TC-I01-023 from the accepted
[W02-B inventory](i01-w02-test-inventory.md). The
[manifest](../../tests/fixtures/i01/source-id-collisions/manifest.json) records
exact source measures, item locations, reference candidates and relational
expectations. These are test observations, not preassigned TDG identities,
resolved internal links or a new product diagnostic catalog.

## Inputs and distinguishing observations

Each input duplicates one complete array item from
[BASE-01](../../tests/fixtures/i01/base-01.json), preserving its bytes and all
other content. Removing only the second item and its separator restores the
exact BASE-01 bytes. No additional control file is introduced.

| Variant | Supplied items | Required observation |
| --- | --- | --- |
| TC-I01-023.01 | Two identical TC objects with `source_id="TC-CREATE-01"`; one basis element | Preserve both TC occurrences and the duplicate key. Each supplied `basis_refs` entry has one candidate at `/content/basis_elements/0`; duplicated TC keys do not introduce basis-link ambiguity. |
| TC-I01-023.02 | One TC; two identical basis elements with `source_id="BR-AGE-01"` | Preserve both basis occurrences. The TC's supplied reference has two candidate positions and remains visibly ambiguous; do not select the first or last match. |

Identical content strengthens the identity probe: distinct array positions
remain distinct source items even when every supplied value matches. A duplicate
`source_id` value across objects is valid JSON and differs from a repeated member
name inside one object, covered separately by TC-I01-016.

Files are respectively 1583 and 1275 bytes, with 37 and 27 JSON values. Both have
maximum container depth 6 and maximum decoded text/member-name size 154 UTF-8
bytes. Counts are two TC / one basis element and one TC / two basis elements.
All remain below the other accepted resource bounds. Manifest byte spans locate
the original items for asset inspection; product references must identify the
retained artifact and the corresponding JSON Pointer.

## Oracles and binding boundary

Trace: TCND-I01-06; OR-I01-FID-007 in the
[W02 oracle basis](i01-w02-test-design.md); RA09-REQ-009, RA03-REQ-014/037 and
RA09-VAL-005/008. Governing clauses are
[RA-09 §3.2 and §4.1](../requirements-analysis/ra-09/test-design-gatekeeper-ra-09-data-representations-import-export-contracts-v0.2.md)
and [SAD-04 §5 / SAD-D-019](../solution-design/test-design-gatekeeper-sad-04-integrated-review-increment-plan-v0.2.md).

On the controlled complete path, each input expects CAPTURED, retained original
bytes, coherent projection/receipt and a new version reference after commit.
Minimum remains NOT_EVALUATED with MINIMUM_CHECK_NOT_ENABLED_IN_I01; no review
is performed. Preconditions remain eligible Windows x64 / CPython 3.13 laboratory
operation, a fresh operation ID, healthy isolated store and effective containment.

The duplicated items require distinct TDG-generated internal IDs with stable
bindings to their separate original locations. Supplied IDs remain unchanged and
the collision stays visible. In .01, a resolved basis link can only target the
single candidate; this does not introduce a rule requiring every unique reference
to be resolved. In .02, both candidates remain represented as an ambiguity,
including when their business text is identical. No source-ID repair, content
merge or guessed referential target is permitted.

[Product skeletons](../../tests/test_i01_source_id_collision_pending.py) contain
two U and two I placeholders with explicit skips and fail guards. Bind U to real
occurrence/collision/link observations. Bind I to the capture service, then inspect
actual generated IDs, retained bytes, source bindings, reference ambiguity and
receipt through a separate store connection after commit/reopen, preserving prior
immutable records. A test-generated UUID or source-only candidate list cannot
prove that TDG created and durably retained distinct identities.

<a id="preparation-evidence-and-handoff"></a>

## What was checked and what remains to do

[Asset checks](../../tests/test_i01_source_id_collision_assets.py) verify exact
bytes/digests, valid JSON, independently measured resource counts, identical
items at separate positions, the inverse mutation and candidate lists. In-memory
unique-key witnesses distinguish collisions from unique IDs; a deliberately lossy
dictionary-by-source-ID witness shows how merging erases an item and can conceal
reference ambiguity. These witnesses do not rewrite fixtures or repair TC.

The first focused run passed **11 new asset checks; four product skeletons
skipped**. Combined verification across all seven families on 2026-10-10:
**140 passed; 100 skipped**, on Linux x86_64 / CPython 3.12.14 with cached pytest
9.1.1 modules. TDG was not installed or run under 3.12. Target Windows/Python 3.13
verification and product E2 observations remain pending; product regression was
not rerun for this change to test data and test placeholders. Existing assets and accepted snapshots stay
unchanged.

On a prepared target environment:

~~~powershell
.\.venv\Scripts\python.exe -m pytest -q -rs tests/test_i01_source_id_collision_assets.py tests/test_i01_source_id_collision_pending.py
~~~

At the time of this record, the prepared files included the baseline example
`BASE-01` and 48 input variants for thirteen test cases (TC-I01-011–023).
This covers group B and TC-I01-021–023 in group C.
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

Next planned task at the time of this record: TC-I01-024, four source-ID fidelity variants covering leading
zeros, case, surrounding whitespace and canonically equivalent but differently
encoded Unicode.
