# I-01 / W02-C — JSON syntax, encoding and duplicate fields

Prepared and checked 2026-10-08; published 2026-10-09 (Europe/Warsaw).
Source pin: `main` at `bf696d9eb8f6933976b1a4a3f9f1ce360193dd36`.

These ten inputs cover TC-I01-016–017 from the [accepted inventory](i01-w02-test-inventory.md).
TDG is expected to reject duplicate fields, encoding errors and syntax forbidden
by its native JSON rules without silently repairing the input. The files are
prepared; tests of TDG's behavior still need to be connected to the implementation.

The checks below describe the work dated above. Development and further test-data
preparation are currently paused; [README.md](../../README.md) gives the current
project status.

## Inputs and controls

The [manifest](../../tests/fixtures/i01/syntax/manifest.json) records exact sizes
and hashes, deliberate defects, valid comparison files, test levels and expected
outcomes. Its defect labels describe the test data; they are not TDG issue codes.

| Variants | Deliberate defect | Intended observation |
| --- | --- | --- |
| TC-I01-016.01–.03 | Duplicate document_type at root; duplicate title inside TC; a and escaped \u0061 inside one test_data object | Native-profile rejection before lossy projection; compare decoded names and retain both occurrences in the test observer |
| TC-I01-017.01 | Leading bytes EF BB BF | Reject the native-profile BOM; no automatic stripping |
| TC-I01-017.02 | One byte FF replacing R in the title | Strict UTF-8 failure at the recorded byte offset; no replacement decoding |
| TC-I01-017.03–.04 | Line comment after the root opening; trailing comma after the last root member | Syntax rejection; no automatic repair |
| TC-I01-017.05–.07 | Unquoted NaN, Infinity, -Infinity in test_data.n | Reject non-JSON numeric tokens; no coercion into null, strings or numbers |

Both duplicate root values are the supported kind, avoiding a competing
unsupported-kind defect. The title values differ. The third duplicate uses two
different source spellings that decode to the same name at
`/content/test_cases/0/test_data`.

The controls reuse [BASE-01](../../tests/fixtures/i01/base-01.json) and add two
public synthetic files: [one with a single a member](../../tests/fixtures/i01/syntax/control-decoded-name.json)
and [one with n=0](../../tests/fixtures/i01/syntax/control-number-zero.json).
They qualify the data/observer setup; they are not additional inventory variants
or evidence of successful TDG capture. Each inverse mutation is checked in
memory against its exact recorded control bytes. Original fixtures are never
rewritten or passed through a serializer by these tests.

Negative files are 1051–1105 bytes. Valid controls have depth 6, 24–25 JSON
values, maximum decoded text/member-name size 154 UTF-8 bytes, one TC and one
basis element. Known mutations add no container nesting or large payload.
Tree/text metrics in the manifest explicitly describe valid controls only;
malformed originals are not silently normalized into a claimed valid tree.
The duplicate observer preserves ordered name/value pairs instead of accepting
a last-value-wins dictionary.

TC-I01-017.02 is intentionally not UTF-8 text. It is stored as exact binary
bytes, and published through a base64 Git blob. Existing fixture-tree
attributes disable checkout text conversion. The BOM and all other source
bytes must also survive checkout unchanged.

## Oracles and binding boundary

All ten controlled negative paths require REJECTED, CLI exit 2 on successful
result delivery, no new package/reference, minimum NOT_EVALUATED and no review.
Prerequisites remain the accepted Windows x64 / CPython 3.13 laboratory context,
eligible operator declarations, healthy isolated store and effective containment.
Safe rejection-retention/storage-failure rules still apply.

Trace: TCND-I01-05; OR-I01-SYN-001–003 in the
[W02 oracle basis](i01-w02-test-design.md); RA09-REQ-004 / RA09-VAL-003;
[RA-09 Section 3.3](../requirements-analysis/ra-09/test-design-gatekeeper-ra-09-data-representations-import-export-contracts-v0.2.md#33-source-fidelity-presence-and-mapping-state)
and [SAD-04 Section 6.1](../solution-design/test-design-gatekeeper-sad-04-integrated-review-increment-plan-v0.2.md#61-native-input-and-mechanical-projection).
The accepted inventory allocates U + C to all ten variants, with E1/E3 for
duplicates and E1/E2/E4 for the encoding/syntax cases.

[Input checks](../../tests/test_i01_syntax_assets.py) verify exact bytes, controls,
isolated mutations and observable defect classes using independent test
observers and Python's decoder. Python's permissive handling of some inputs is
not the TDG oracle: BOM and non-finite tokens remain forbidden by the accepted
native profile.

The [20 product-test placeholders](../../tests/test_i01_syntax_pending.py) cover
10 component and 10 CLI tests, with explicit skips and fail guards. Before
enabling them:

- bind the actual syntax/profile boundary, cause/location assertions and issue
  vocabulary; generic failure is insufficient proof of the intended rejection;
- qualify pre-projection observers with the valid controls; prove duplicates
  are rejected before any lossy accepted projection is constructed;
- bind the installed CLI, bounded diagnostics, receipt and separate SQLite
  inspection; assert no new package or fabricated result, with prior history
  preserved and no raw payload/path leakage.

The current asset observations do not provide those product E2/E3/E4 results.
Neither fixture validation nor a skipped test is product verification.

<a id="preparation-evidence-and-handoff"></a>

## What was checked and what remains to do

The first authoring attempt stopped with an AssertionError at
`raw.count(anchor) == 1`: the comment recipe used `b'{\n'`, which also occurred
inside nested objects. This was an authoring-harness error, not a TDG failure.
The uniqueness guard was retained. The recipe was corrected to verify the
root prefix and insert at byte 2; subsequent checks prove the exact isolated
mutation. No product behavior or accepted oracle was changed.

Focused asset execution: **37 new checks passed; 20 new product skeletons
skipped**. With the earlier numeric and envelope families: **86 passed,
68 skipped** on Linux x86_64 / CPython 3.12.14 with cached pytest 9.1.1 modules.
TDG was not installed or run under 3.12. Target Windows/Python 3.13 verification
remains pending; source/dependency pins and earlier assets remain unchanged.
The product regression was not rerun for this change to test data and test placeholders.

For this family on a prepared target environment:

~~~powershell
.\.venv\Scripts\python.exe -m pytest -q -rs tests/test_i01_syntax_assets.py tests/test_i01_syntax_pending.py
~~~

At that date, the prepared material comprised `BASE-01` and 32 input variants
for eight cases (TC-I01-011–018), plus two additional valid comparison files.
One input can be used by several checks. The pytest totals above count checks
and skipped placeholders; they do not establish passed TDG cases.

These synthetic development inputs are already known to the author and cannot
serve as previously unseen acceptance data. The author performed the checks
with AI assistance. They do not count as an independent human review.

Human time spent was not reported. [Inventory Section 7](i01-w02-test-inventory.md#7-effort-reassessment)
retains the provisional forecast and reassessment requirements. Preparing these
files and checking them did not close W02, authorize W03 or accept I-01.
