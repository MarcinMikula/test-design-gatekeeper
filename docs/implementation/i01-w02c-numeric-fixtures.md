# I-01 / W02-C — Testing the length limit for JSON numbers

Prepared 2026-10-07; verified/published 2026-10-08 (Europe/Warsaw).
Source pin: `main` at `577e0eef38bf4865f955ddd2d06f4ed6e9e1f4ba`.

These files prepare TC-I01-018 from the [accepted inventory](i01-w02-test-inventory.md):
a JSON number written without quotes is tested just below, at and above the
128-character limit. The three inputs are ready; tests of TDG's behavior still
need to be connected to the implementation.

The results below describe the 2026-10-08 checks. Development and further test-data
preparation are currently paused; [README.md](../../README.md) gives the current
project status.

## Assets and expected outcomes

- [BASE-01](../../tests/fixtures/i01/base-01.json): the shared synthetic
  registration input (`BR-AGE-01`, `TC-CREATE-01`, `HUMAN_AUTHORED`), specified in
  [inventory Section 2](i01-w02-test-inventory.md#2-common-fixture-and-observation-contract).
  Its supplied declarations do not grant human authority or establish an I-01
  business-rule assessment.
- [Manifest](../../tests/fixtures/i01/numeric-token/manifest.json): exact sizes,
  SHA-256 digests, source byte ranges and their offset convention, resource
  measurements and expectations for each test level. Its field names describe
  test data; they do not define a new TDG interface or runtime issue codes.
- [Input checks](../../tests/test_i01_numeric_assets.py): verify the BASE-01
  recipe, file bytes, measurements, controlled change and expected outcomes.
- [Product-test placeholders](../../tests/test_i01_numeric_pending.py): three
  inputs at each of the component, integration and CLI levels. All nine tests
  remain skipped until real assertions are connected. Removing a skip without
  those assertions fails visibly rather than producing an empty PASS.

Each variant adds only `test_data.n` to the TC: unquoted `1` followed by zeros.
The checks also remove that exact byte insertion and recover BASE-01 unchanged.

| Variant | Token characters | Length gate | Complete eligible capture / delivered CLI result |
| --- | ---: | --- | --- |
| TC-I01-018.01 | 127 | Within bound | CAPTURED / 0 |
| TC-I01-018.02 | 128 | Within bound | CAPTURED / 0 |
| TC-I01-018.03 | 129 | Exceeds bound | REJECTED / 2; no new package/reference |

The manifest retains the detailed measurements for BASE-01 and each variant.
Other input limits stay below their thresholds. `.gitattributes` disables text
conversion for this fixture tree so checkout cannot silently change its bytes
or digests.

The full-capture oracle assumes a healthy initialized isolated workspace and the
accepted Windows x64 / CPython 3.13 laboratory context, operator qa-demo,
synthetic classification, lab-development purpose, a fresh operation identity,
and all other admission/containment controls satisfied. A component gate pass
alone cannot establish CAPTURED. All three complete paths retain minimum
NOT_EVALUATED and perform no substantive review.

Trace: TCND-I01-05/10; OR-I01-SYN-004 in the
[W02 oracle basis](i01-w02-test-design.md); RA09-REQ-004/006/016 and RA09-VAL-003.
The current numeric rule is in
[SAD-04 Section 6.1](../solution-design/test-design-gatekeeper-sad-04-integrated-review-increment-plan-v0.2.md#61-native-input-and-mechanical-projection),
with CLI and resource rules in Sections 8 and 9. The
[SAD04-I01-NUM-001 record](https://github.com/MarcinMikula/test-design-gatekeeper/blob/6bf96d9748c1d4faae049786feb8c49397f4c659/docs/solution-design/test-design-gatekeeper-sad-04-i01-numeric-token-limit-addendum-v0.1.md)
preserves the decision. This is one planned case with three input variants.

## Binding still required before product execution

| Level | Required real observation before removing the skip |
| --- | --- |
| U — component | Call the actual bounded numeric-token check; assert within-bound versus excess and the affected source location. Do not infer receipt, persistence or CLI behavior. |
| I — integration | Exercise real capture with effective prerequisites. Inspect actual receipt and a separate SQLite connection: original bytes/digest, exact or explicitly limited located projection, coherent inventory/IDs and committed reference for CAPTURED; no new package/reference for REJECTED. Assert minimum NOT_EVALUATED, the I-01 limitation on capture, and no fabricated review. |
| C — CLI | Invoke the installed import entry point; inspect exit code, bounded stdout/stderr and durable effects. Excess must identify numeric-token limit and safe location without leaking the raw token/host path. Bind the actual issue-code vocabulary; no code is invented here. |

E1 fixture-integrity evidence is prepared. Product E2/E4 evidence, parser/service
entry points, receipt/projection field bindings, diagnostic codes and independent
store observations remain pending. Eligible native containment must be available
before claiming the controlled full path. No adapter or fake service substitutes
for these observations. Retain the first meaningful failure when execution
becomes possible; a contrary product result must not redefine these oracles.

## Verification and limits

On 2026-10-08 the focused selection produced **9 passed, 9 skipped**. The passes
are fixture/manifest checks; the nine skipped tests are placeholders awaiting connections to
TDG. Neither number is an executed TC-I01-018 product result.

The available host was Linux x86_64, CPython 3.12.14, using cached pytest 9.1.1
modules. CPython 3.13 was unavailable; the TDG package was not installed or run
under 3.12. This is portable asset validation only, not supported-runtime or
native Windows qualification. Source code, dependency pins and the qualified
W01 build remain unchanged. The existing product regression was not rerun for
this change to test data and test placeholders.

With the normal project environment already prepared, the focused command on the
target Windows host is:

```powershell
.\.venv\Scripts\python.exe -m pytest -q -rs tests/test_i01_numeric_assets.py tests/test_i01_numeric_pending.py
```

Expected results came from accepted requirements and design before any TDG
import result was observed. These synthetic development inputs are already known
to the author and cannot serve as previously unseen acceptance data. The author
performed the checks with AI assistance. They do not count as an independent
human review.

Human time spent was not reported; conversation duration is not a measure of
human effort. [Inventory Section 7](i01-w02-test-inventory.md#7-effort-reassessment)
retains the provisional forecast and reassessment requirements. Preparing these
files and checking them did not close W02, authorize W03 or accept I-01.
