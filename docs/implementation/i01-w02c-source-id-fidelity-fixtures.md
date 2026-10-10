# I-01 / W02-C — Source-ID fidelity fixtures

Prepared and checked 2026-10-10 (Europe/Warsaw).
Source pin: `main` at `1a3414137c478178888632e282340c35335dab9a`.
Status: **four variants prepared; product observations remain unbound**.

This slice materializes TC-I01-024 from the accepted
[W02-B inventory](i01-w02-test-inventory.md), using OR-I01-FID-003 in the
[W02 oracle basis](i01-w02-test-design.md): RA09-REQ-006 and RA09-VAL-003/006,
conditions TCND-I01-01/06, levels U/I and evidence E1/E2. The governing
[RA-09 §3.3 and §4.1](../requirements-analysis/ra-09/test-design-gatekeeper-ra-09-data-representations-import-export-contracts-v0.2.md)
requires retained source fidelity and separate identities for independent items.

## Data and distinguishing witnesses

Each file duplicates the BASE-01 TC and replaces only the two source IDs.
All other supplied content, including the single basis element and its references,
remains logically unchanged. Files use literal UTF-8, without BOM; escaped JSON
versus literal Unicode syntax is separately covered by TC-I01-002.

| Variant | Ordered source strings | Lossy transformation demonstrated only by the asset check |
| --- | --- | --- |
| TC-I01-024.01 | `001`, `1` | Integer conversion removes leading zeros |
| TC-I01-024.02 | `TC-A`, `tc-a` | Case folding conflates distinct strings |
| TC-I01-024.03 | ` TC-A\t`, `TC-A` | Trimming removes leading space and trailing tab; `\t` denotes the decoded tab |
| TC-I01-024.04 | `TC-é`, `TC-é` | NFC normalization conflates U+00E9 with U+0065 U+0301 |

The [manifest](../../tests/fixtures/i01/source-id-fidelity/manifest.json)
records exact sizes, SHA-256, ordered strings, code points and original JSON
Pointers. Each document has 37 JSON values, maximum container depth 6,
maximum decoded text/member-name length 154 UTF-8 bytes, two TC and one basis
element. Other resource limits remain below their accepted bounds.

The pair in each file differs before its illustrated transformation and becomes
equal after it. Thus retaining only a normalized representation cannot satisfy the
oracle. These in-memory counterexamples do not transform the actual fixtures,
implement TDG or prove product defect detection.

## Product binding boundary

Under eligible Windows x64 / CPython 3.13 laboratory conditions, with synthetic
input, a fresh operation identity, healthy isolated initialized store and effective
containment, the complete path expects CAPTURED, unchanged original bytes and
coherent projection/receipt. Minimum remains NOT_EVALUATED with
MINIMUM_CHECK_NOT_ENABLED_IN_I01; no substantive review is performed.

Bind the [eight product skeletons](../../tests/test_i01_source_id_fidelity_pending.py)
to actual component and capture behavior. Observe both ordered strings and code
points at `/content/test_cases/0/source_id` and `/content/test_cases/1/source_id`.
Preserve both independent records and their actual TDG-generated identities,
with projection-to-original artifact/pointer bindings. For I-level checks,
inspect retained bytes, identities, values, links and receipt using an independent
store connection after commit/reopen. Test-generated IDs or decoding the fixture
alone cannot prove these outcomes. No new matching policy or diagnostic code is
introduced by this slice.

## Preparation evidence and handoff

The [asset checks](../../tests/test_i01_source_id_fidelity_assets.py) independently
check the pair recipes, exact bytes/digests, unique JSON members, resource measures,
unchanged baseline content and distinguishing lossy-transform witnesses.
First focused execution: 13 passed, eight skipped; two pytest iterator-deprecation
warnings were corrected by materializing parametrization lists. No test failed.
Combined execution afterward: **153 passed, 108 skipped**, with no warnings,
on Linux / CPython 3.12.14 using cached pytest 9.1.1 modules. TDG was not installed
or executed under 3.12. This is asset evidence, not product execution or native
Windows/Python 3.13 qualification. Existing fixtures and accepted snapshots remain
unchanged; no product regression is claimed.

Target command after environment preparation:

~~~powershell
.\.venv\Scripts\python.exe -m pytest -q -rs tests/test_i01_source_id_fidelity_assets.py tests/test_i01_source_id_fidelity_pending.py
~~~

Eight families now materialize BASE-01 plus 52 variants across fourteen case rows
and two valid controls. These exposed synthetic inputs and solo AI-assisted checks
remain development evidence. Effort is unreported; the forecast stays provisional.
W02 remains open; no W03 GO or I-01 acceptance is claimed.

Next small slice: TC-I01-025 — unknown nested content, malformed test_cases member,
and title-only TC (three variants).
