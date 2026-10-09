# I-01 / W02-C — Syntax and encoding fixture family

Prepared and checked 2026-10-08; publication slice 2026-10-09 (Europe/Warsaw).
Source pin: `main` at `bf696d9eb8f6933976b1a4a3f9f1ce360193dd36`.
Status: **10 negative variants prepared; product assertions remain unbound**.

This slice materializes TC-I01-016–017 from the Owner-accepted
[W02-B inventory](i01-w02-test-inventory.md). The
[manifest](../../tests/fixtures/i01/syntax/manifest.json) records exact raw sizes
and digests, intended defects, valid counterparts, levels and expected outcomes.
Defect labels are test metadata, not product issue codes.

## Inputs and controls

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
RA-09 §3.3 and SAD-04 §6.1. The accepted inventory allocates U + C to all ten
variants, with E1/E3 for duplicates and E1/E2/E4 for the encoding/syntax cases.

[Asset checks](../../tests/test_i01_syntax_assets.py) verify exact bytes, controls,
isolated mutations and observable defect classes using independent test
observers and Python's decoder. Python's permissive handling of some inputs is
not the TDG oracle: BOM and non-finite tokens remain forbidden by the accepted
native profile.

[Product skeletons](../../tests/test_i01_syntax_pending.py) provide 10 U and 10 C
placeholders with explicit skips and fail guards. Before enabling them:

- bind the actual syntax/profile boundary, cause/location assertions and issue
  vocabulary; generic failure is insufficient proof of the intended rejection;
- qualify pre-projection observers with the valid controls; prove duplicates
  are rejected before any lossy accepted projection is constructed;
- bind the installed CLI, bounded diagnostics, receipt and separate SQLite
  inspection; assert no new package or fabricated result, with prior history
  preserved and no raw payload/path leakage.

The current asset observations do not provide those product E2/E3/E4 results.
Neither fixture validation nor a skipped test is product verification.

## Preparation evidence and handoff

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
The product regression was not rerun for this test-asset-only slice.

For this family on a prepared target environment:

~~~powershell
.\.venv\Scripts\python.exe -m pytest -q -rs tests/test_i01_syntax_assets.py tests/test_i01_syntax_pending.py
~~~

Across the three slices, BASE-01 and 32 variants from eight case rows are
materialized, with two additional valid controls. This is not completion of
the 72-row / 208-variant inventory or execution of those product cases.
The assets are exposed development data; author checking remains solo
AI-assisted, not independent assurance. Human effort is unreported and the
forecast remains provisional.

Next small slice: TC-I01-019–020, exact in-bound numeric lexemes and a long
numeric-looking string. W02 remains open; no W03 GO or I-01 acceptance is claimed.
