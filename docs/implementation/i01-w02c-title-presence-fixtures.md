# I-01 / W02-C — Title presence and type fixtures

Prepared and checked 2026-10-09 (Europe/Warsaw).
Source pin: `main` at `35e9ae1cce9debc1b11258ed6b96cf4b67119061`.
Status: **seven variants prepared; product assertions remain unbound**.

This slice materializes TC-I01-021 from the accepted
[W02-B inventory](i01-w02-test-inventory.md). The
[manifest](../../tests/fixtures/i01/title-presence/manifest.json) records exact
source bytes/digests, title presence or raw lexeme/span, resource measurements,
fixed expected observations and U/I evidence bindings. Only the title changes;
scope, basis, actions, expected result, age and other BASE-01 content stay intact.

## Inputs and fixed expectations

| Variant | Supplied title | Expected presence |
| --- | --- | --- |
| TC-I01-021.01 | Member absent | ABSENT |
| TC-I01-021.02 | JSON `null` | NULL |
| TC-I01-021.03 | Empty string `""` | EMPTY |
| TC-I01-021.04 | String containing space, tab, CR, LF, space | WHITESPACE_ONLY |
| TC-I01-021.05 | `"Register a customer aged 30"` | VALUE |
| TC-I01-021.06 | Integer `0` | TYPE_MISMATCH |
| TC-I01-021.07 | Empty array `[]` | TYPE_MISMATCH |

The states follow [RA-09 §3.3](../requirements-analysis/ra-09/test-design-gatekeeper-ra-09-data-representations-import-export-contracts-v0.2.md):
absence, explicit null, type mismatch, then empty/whitespace/value of the intended
type. An empty array is the wrong type for a text-only title. JSON null, empty
text, zero and an empty array are all falsy in Python, but do not have the same
accepted presence observation. No product classifier is implemented here.

Whitespace is encoded as `" \t\r\n "` in the source and decodes to five exact
characters. It is neither an empty string nor permission to trim the source.
The VALUE file deliberately equals [BASE-01](../../tests/fixtures/i01/base-01.json)
byte-for-byte; its distinct fixture ID identifies an inventory variant, not new
source content. No additional control file is introduced.

Files are 1003–1051 bytes. The absent-title input has 23 JSON values; the other
six have 24. All have container depth 6, maximum decoded text/member-name size
154 UTF-8 bytes, one TC and one basis element, below the other accepted limits.
The only numbers are the small supplied age and, in variant .06, title zero.

## Capture and source-reference boundary

All seven controlled complete paths expect CAPTURED, including deficient titles.
The governing [SAD-04 §6.1](../solution-design/test-design-gatekeeper-sad-04-integrated-review-increment-plan-v0.2.md)
does not reject capturable content for editorial incompleteness. Original bytes,
presence/type deficiencies and applicable issues remain inspectable; TDG does
not fill an absent title, replace null, stringify a number or turn an array into
empty text. Minimum stays NOT_EVALUATED with MINIMUM_CHECK_NOT_ENABLED_IN_I01;
no substantive review or TC approval is produced.

These outcomes assume the accepted eligible Windows x64 / CPython 3.13 laboratory
context, fresh operation identity, healthy isolated schema-1 store and effective
containment. A component observation alone does not establish durable capture.

For a present member, the source locator resolves to the supplied title within
the exact retained artifact. For ABSENT, evidence identifies the containing TC
at `/content/test_cases/0` and the missing-field observation. The manifest's
target `/content/test_cases/0/title` is not a claim that a missing value exists:
variant .01 has no raw title lexeme or value span. In contrast, variant .02 has
the four-byte token `null` and a real span. Presence remains separate from mapping
status; this slice invents no per-variant MAPPED/UNMAPPED result or issue code.

Trace: TCND-I01-06; OR-I01-FID-001/004 in the
[W02 oracle basis](i01-w02-test-design.md); RA09-REQ-006/007/012,
RA09-VAL-003/006, RA-09 §3.3 and SAD-04 §6.1. The inventory allocates U + I and
E1/E2. [Product skeletons](../../tests/test_i01_title_presence_pending.py) provide
seven U and seven I placeholders with explicit skips and fail guards. Enabling
them requires actual presence/source/mapping observations and real capture plus
separate store inspection after commit/reopen: original bytes, deficiencies,
source boundaries, projection and receipt must agree; prior immutable records
must remain unchanged. Generic success or capture alone cannot prove the state.

## Preparation evidence and handoff

[Asset checks](../../tests/test_i01_title_presence_assets.py) validate exact
bytes, valid envelope, independent resource measures, isolated title changes,
raw spans versus absence, fixed recipe/state mapping and the distinguishing
null/falsy/whitespace/control observations. They do not call TDG or treat Python
truthiness as the product oracle.

The first focused run passed: **19 new asset checks; 14 product skeletons
skipped**. All five families together: **118 passed; 90 skipped** on Linux
x86_64 / CPython 3.12.14 with cached pytest 9.1.1 modules. TDG was not installed
or run under 3.12. Target Windows/Python 3.13 verification and actual product
E2 observations remain pending; product regression was not rerun for this
asset-only change. Existing assets and accepted snapshots are unchanged.

On a prepared target environment:

~~~powershell
.\.venv\Scripts\python.exe -m pytest -q -rs tests/test_i01_title_presence_assets.py tests/test_i01_title_presence_pending.py
~~~

BASE-01 plus 43 named variants across eleven case rows and two valid controls
are materialized. These are all group-B variants plus TC-I01-021 in group C,
not completed product verification or the whole 72-row / 208-variant inventory.
Pytest item totals and inventory-variant counts measure different things.
The exposed synthetic corpus and solo AI-assisted checks are development
evidence, not held-out acceptance or independent assurance. Effort is unreported;
the forecast remains provisional.

Next small slice: TC-I01-022, narrative/structured/repeated steps with their
order, numbering and nested expected results preserved. W02 remains open;
no W03 GO or I-01 acceptance is claimed.
