# I-01 / W02-C — Required JSON fields, types and versions

Prepared and checked 2026-10-08 (Europe/Warsaw).
Source pin: `main` at `e1ff0d7a9114f3092fc10ac4734e27cdce7ea380`.

These 19 inputs cover TC-I01-011–015 from the [accepted inventory](i01-w02-test-inventory.md)
and reuse the unchanged [BASE-01](../../tests/fixtures/i01/base-01.json). They test
the outer JSON structure: required fields, their types, supported document kind
and contract version, extra fields and empty `content`.

The input files are prepared; tests of TDG's behavior still need to be connected
to the implementation. Results below describe the 2026-10-08 checks. Development
and further test-data preparation are currently paused; [README.md](../../README.md)
gives the current project status.

## Prepared cases and oracles

The [manifest](../../tests/fixtures/i01/envelope/manifest.json) lists each input
file, size, hash and resource measurements. It also records the source inventory,
planned test levels, expected results and full-capture prerequisites. Its fields
describe tests; they do not define a new TDG interface or runtime issue codes.

| Case / variants | Change from BASE-01 | Expected controlled result | Planned levels |
| --- | --- | --- | --- |
| TC-I01-011.01–.03 | Remove document_type, contract_version or content, in that order | REJECTED; no guessed defaults or package/reference; CLI 2 | U + C |
| TC-I01-012.01–.02 | Add the same synthetic_marker at root, then inside content | Root: REJECTED. Inside content: CAPTURED with exact marker, source location and mapping state visible | U + I |
| TC-I01-013.01–.09 | document_type null/integer; contract_version null/number; content null/array/string; whole document array/string scalar | REJECTED; no type coercion; CLI 2 | U + C |
| TC-I01-014.01–.04 | Kind review_export, review_package_snapshot, unknown-kind; then version string 999.0 | REJECTED; no migration, restore or version fallback; CLI 2 | U + C |
| TC-I01-015 | Supported envelope with content={} | CAPTURED; absent scope/basis/TC visible; minimum NOT_EVALUATED; CLI 0 | U + I + C |

The single-variant TC-I01-015 keeps its unsuffixed ID. Other suffixes follow the
accepted inventory order. Wrong-type version 1.0 is a JSON number; unsupported
version "999.0" remains a string. The whole-document array contains BASE-01;
the scalar is the string "synthetic scalar". These instantiate the accepted
partitions without extending their scope.

All 19 files are strict UTF-8 JSON without duplicate members or a BOM. Their
deliberate defect, where present, concerns the envelope. Raw size, numeric-token
length, text size, depth, node and candidate-item bounds do not compete with that
stimulus. Existing fixture-tree attributes preserve exact bytes during checkout.
Both unknown-field fixtures carry W02C_UNKNOWN_MARKER_012; the retained content
location is `/content/synthetic_marker`. No marker is an operational instruction.

Capture expectations require the accepted laboratory context and all remaining
admission, worker-containment and healthy-store prerequisites. Envelope
eligibility alone does not prove capture. Every complete path keeps minimum
NOT_EVALUATED and performs no review. Empty content is not an envelope rejection
or a claim that the core minimum is MET/NOT_MET.

Trace follows W02-B: TCND-I01-04/06/08/15; OR-I01-ENV-001–007 and RCP-004 in the
[W02 oracle basis](i01-w02-test-design.md); RA09-REQ-001/003/006/012/013/015/020/021,
RA09-VAL-002/003/011 and
[SAD-04 Sections 6.1–6.2](../solution-design/test-design-gatekeeper-sad-04-integrated-review-increment-plan-v0.2.md#61-native-input-and-mechanical-projection).
These links identify the expected behavior, not executed evidence of requirement
fulfilment.

## Checks, skeletons and remaining bindings

[Input checks](../../tests/test_i01_envelope_assets.py) verify file digests,
sizes and resource measurements, the precise mutation with all other supplied
values unchanged, unique stable IDs, variant order, planned levels and expected
partitions. They use Python's JSON decoder with duplicate/encoding checks and
exact decimal decoding, not a TDG parser or TDG-produced expected results.

The [39 product-test placeholders](../../tests/test_i01_envelope_pending.py) cover
19 component, 3 integration and 17 CLI tests, following the accepted case levels.
They are skipped with explicit reasons. A fail guard prevents an empty PASS if a
skip is removed before real assertions are supplied.

| Boundary | Binding required before product execution |
| --- | --- |
| U | Actual local envelope routing/validation and affected-location diagnostics; assert no coercion, defaulting or fallback. A component result does not establish a receipt or store effect. |
| I | Real capture, effective containment and separate SQLite inspection: coherent original/projection/inventory/receipt and post-commit reference for the two capturable variants; no new package/reference for root-marker rejection. Check unknown marker location/mapping and missing dimensions of empty content. |
| C | Installed entry point, bounded stdout/stderr, delivered exit code and independent durable-effect checks for the 17 allocated variants. Preserve prior history; no fabricated successful receipt or package after rejection. |

The tests still need to use the actual receipt/projection fields and issue codes,
and run with verified observation tools on the target environment. Bind the accepted minimum reason on capture and
verify no fabricated review. Safe rejection-retention and storage-failure rules
still apply. Prepared E1 assets do not supply product E2/E4 evidence. Preserve the
first meaningful product failure rather than changing the oracle to match it.

<a id="verification-and-handoff"></a>

## What was checked and what remains to do

Focused execution on 2026-10-08: **40 new asset checks passed; 39 new product
skeletons skipped**. Including the numeric family: **49 passed, 48 skipped**.
The host was Linux x86_64 / CPython 3.12.14 with cached pytest 9.1.1 modules.
These are portable asset checks only. TDG was not installed or run under 3.12;
Windows x64 / CPython 3.13 qualification remains pending for these assets.
Product source/dependency pins and the earlier numeric artifacts are unchanged;
the product regression was not rerun for this change to test data and test placeholders.

With the normal target environment already prepared:

```powershell
.\.venv\Scripts\python.exe -m pytest -q -rs tests/test_i01_envelope_assets.py tests/test_i01_envelope_pending.py tests/test_i01_numeric_assets.py tests/test_i01_numeric_pending.py
```

At that date, the envelope and numeric groups together comprised `BASE-01` and
22 input variants for six cases (TC-I01-011–015 and TC-I01-018). One input can be
used by several checks. The pytest totals above count checks and skipped
placeholders; they do not establish passed TDG cases.

These synthetic development inputs are already known to the author and cannot
serve as previously unseen acceptance data. The author performed the checks
with AI assistance. They do not count as an independent human review.

Human time spent was not reported. [Inventory Section 7](i01-w02-test-inventory.md#7-effort-reassessment)
retains the provisional forecast and reassessment requirements. Preparing these
files and checking them did not close W02, authorize W03 or accept I-01.
