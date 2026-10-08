# I-01 / W02-C — First numeric-token fixture family

Prepared 2026-10-07; verification/publication slice 2026-10-08 (Europe/Warsaw).
Source pin: `main` at `577e0eef38bf4865f955ddd2d06f4ed6e9e1f4ba`.
Status: **partial W02-C assets prepared; product assertions remain unbound**.

The Owner accepted the whole [W02-B inventory](i01-w02-test-inventory.md) as the
basis for W02-C on 2026-10-07, recorded in
[SR-I01-W02B-001 v0.7](../reviews/test-design-gatekeeper-i01-w02b-review-progress-v0.7.md).
This slice implements its BASE-01 recipe and TC-I01-018's three listed variants.
It does not close W02, start W03 or accept I-01. The accepted inventory and review
record are unchanged.

## Assets and expected outcomes

- [BASE-01](../../tests/fixtures/i01/base-01.json): synthetic registration basis
  BR-AGE-01, integer age 18–120 inclusive, and TC-CREATE-01 submitting age 30;
  narrative preconditions, structured step, nested expected result, HUMAN_AUTHORED
  declaration and basis link. These are supplied synthetic declarations, not
  grants of human authority or an I-01 business-rule assessment.
- [Manifest](../../tests/fixtures/i01/numeric-token/manifest.json): stable IDs,
  fixture paths, SHA-256 digests, byte lengths, tree/text measurements, exact
  numeric-token spans and separately stated component/capture/CLI expectations.
  Its observation names are test metadata, not a new product DTO or issue-code
  contract. Source offsets count UTF-8 bytes from zero, with an exclusive end.
- [Asset checks](../../tests/test_i01_numeric_assets.py): verify exact bytes and
  recipe measurements, the BASE-01 content, the single controlled mutation and
  consistency of the oracle table with the accepted numeric decision.
- [Product skeletons](../../tests/test_i01_numeric_pending.py): three variants at
  each of U, I and C levels, explicitly skipped until real assertions are bound.
  Removing a skip without binding assertions fails visibly; it cannot yield an
  empty PASS.

Each variant adds only `test_data.n` to the TC: unquoted `1` followed by zeros.
The checks also remove that exact byte insertion and recover BASE-01 unchanged.

| Variant | Token characters | Input bytes | Length gate | Complete eligible capture / delivered CLI result |
| --- | ---: | ---: | --- | --- |
| TC-I01-018.01 | 127 | 1195 | Within bound | CAPTURED / 0 |
| TC-I01-018.02 | 128 | 1196 | Within bound | CAPTURED / 0 |
| TC-I01-018.03 | 129 | 1197 | Exceeds bound | REJECTED / 2; no new package/reference |

BASE-01 is 1051 bytes and 24 JSON values; each variant has 25 values. All four
inputs have container depth 6, maximum decoded text/member-name size 154 UTF-8
bytes, one TC and one basis element. Other input bounds remain below their
thresholds. `.gitattributes` disables text conversion for this fixture tree so
checkout cannot silently change the retained bytes/digests.

The full-capture oracle assumes a healthy initialized isolated workspace and the
accepted Windows x64 / CPython 3.13 laboratory context, operator qa-demo,
synthetic classification, lab-development purpose, a fresh operation identity,
and all other admission/containment controls satisfied. A component gate pass
alone cannot establish CAPTURED. All three complete paths retain minimum
NOT_EVALUATED and perform no substantive review.

Trace: TCND-I01-05/10; OR-I01-SYN-004 in the
[W02 oracle basis](i01-w02-test-design.md); RA09-REQ-004/006/016 and RA09-VAL-003;
SAD-04 §§6.1, 8, 9; accepted
[SAD04-I01-NUM-001](../solution-design/test-design-gatekeeper-sad-04-i01-numeric-token-limit-addendum-v0.1.md).
This is one case row / three variants from 72 / 208, not nine completed cases.

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
are fixture/manifest checks; the skips are the nine deliberately unbound product
skeletons. Neither number is an executed TC-I01-018 product result.

The available host was Linux x86_64, CPython 3.12.14, using cached pytest 9.1.1
modules. CPython 3.13 was unavailable; the TDG package was not installed or run
under 3.12. This is portable asset validation only, not supported-runtime or
native Windows qualification. Source code, dependency pins and the qualified
W01 build remain unchanged. The existing product regression was not rerun for
this test-asset-only slice.

With the normal project environment already prepared, the focused command on the
target Windows host is:

```powershell
.\.venv\Scripts\python.exe -m pytest -q -rs tests/test_i01_numeric_assets.py tests/test_i01_numeric_pending.py
```

Expected outcomes were specified from accepted contracts before any product
capture output. This remains solo AI-assisted author checking, not independent
human assurance. All assets are exposed synthetic development data, not a fresh
held-out acceptance corpus.

Next small slice: envelope fixtures TC-I01-011–015. W02 remains open for the
remaining assets, actual bindings, corrections and completion review. The §7
forecast remains provisional; human effort was not reported for this slice and
must not be invented from elapsed chat time. Reassessment still needs observed
effort and the first real persistence/native harness.
