# I-01 / W02-C — Numeric lexeme and text retention fixtures

Prepared and checked 2026-10-09 (Europe/Warsaw).
Source pin: `main` at `1e2a637e54a891be4c078759d695f8f2893b4f24`.
Status: **four variants prepared; product assertions remain unbound**.

This slice materializes TC-I01-019–020 from the Owner-accepted
[W02-B inventory](i01-w02-test-inventory.md). The
[manifest](../../tests/fixtures/i01/numeric-retention/manifest.json) records
exact bytes/digests, source lexemes and locations, independent expected outcomes,
U/I levels, E1/E2 obligations and requirement/validation traces. Its observation
fields are test metadata, not new product schema fields or issue codes.

## Inputs and distinguishing observations

All four files add only `test_data.n` to the existing BASE-01. The supplied
registration age, scope, test basis and TC remain unchanged. This is a capture
fidelity probe, not an additional business rule or TC-quality assessment.

| Variant | Exact source value at `/content/test_cases/0/test_data/n` | Required distinction |
| --- | --- | --- |
| TC-I01-019.01 | `9007199254740993` | Retain the 16-character numeric lexeme; `9007199254740992` is not the supplied value |
| TC-I01-019.02 | `0.1000000000000000000001` | Retain the 24-character numeric lexeme; `0.1` changes its exact value |
| TC-I01-019.03 | `-0` | Preserve the original two-character lexeme even though numeric comparison with zero can be equal |
| TC-I01-020 | JSON string containing `1` followed by 128 zeros | Preserve 129 text characters as a string; the 128-character numeric-token limit does not apply to this value |

Files are respectively 1084, 1092, 1070 and 1199 bytes. Each has container depth
6, 25 JSON values, maximum decoded text/member-name size 154 UTF-8 bytes, one TC
and one basis element. All other input/count/text bounds remain below their
limits. Numeric lexemes are 16, 24 and 2 characters, not over-limit numbers.

No additional control files are introduced. The checks reuse
[BASE-01](../../tests/fixtures/i01/base-01.json),
[the n=0 control](../../tests/fixtures/i01/syntax/control-number-zero.json) and
[TC-I01-018.03](../../tests/fixtures/i01/numeric-token/TC-I01-018.03.json).
The last is a rejection contrast: removing only the two quotes from TC-I01-020
produces the exact existing 129-character numeric-token input. It is not a
positive capture control. In-memory changed-value witnesses for the first two
numbers establish that the fixture checks distinguish numeric loss; the zero
control establishes lexical loss without a numeric-value difference.

Byte spans in the manifest are zero-based UTF-8 offsets with an exclusive end;
the string span includes its quotes. These are fixture-observer coordinates,
not a requirement for the future product to expose byte offsets. A product
source reference must bind its locator to the exact retained artifact.

## Oracles and product binding

The governing sources are [RA-09 §3.3 and §4.1](../requirements-analysis/ra-09/test-design-gatekeeper-ra-09-data-representations-import-export-contracts-v0.2.md),
[SAD-04 §6.1/§9](../solution-design/test-design-gatekeeper-sad-04-integrated-review-increment-plan-v0.2.md),
the [numeric-limit addendum](../solution-design/test-design-gatekeeper-sad-04-i01-numeric-token-limit-addendum-v0.1.md)
and OR-I01-SYN-005 / FID-003 / SYN-004 in the
[W02 oracle basis](i01-w02-test-design.md). Trace reaches TCND-I01-05/06/10,
RA09-REQ-004/006/016 and RA09-VAL-003/006 as allocated per case in the manifest.

Every controlled complete path expects CAPTURED with coherent retained source,
projection and receipt, a new version reference only after commit, minimum
NOT_EVALUATED with MINIMUM_CHECK_NOT_ENABLED_IN_I01, and no substantive review.
This assumes the accepted eligible Windows x64 / CPython 3.13 laboratory context,
fresh operation identity, healthy isolated store and effective containment.
Passing a component limit check alone cannot establish capture success.

For TC-I01-019, exact source bytes and the numeric lexeme/location must survive.
Use an exact projection where supported; otherwise expose the affected
projection limitation with a resolvable retained lexeme reference. A generic
warning, rounded number claimed as source, missing original, or false token-size
violation is not acceptable. SAD-04 prohibits source numeric conversion through
binary floating point. No particular numeric runtime class is chosen here.
For `-0`, numeric equality with zero does not establish lexical fidelity; the
contract does not require one particular signed-zero encoding in the derived
projection. The original `-0` must remain identifiable independently.

TC-I01-020 must remain text, with its exact decoded value and source reference;
there is no implicit numeric conversion or numeric-token rejection. Its numeric
counterpart retains the separately accepted REJECTED/exit-2 expectation.

[Product skeletons](../../tests/test_i01_numeric_retention_pending.py) contain
four U and four I placeholders, with explicit skips and fail guards. Before
enabling them:

- bind actual component results and original/projection locator observations;
  choose assertions for the supported projection representation from its design,
  not from observed output; test an explicit limitation at its precise boundary;
- distinguish numeric and text tokens, and prove no numeric coercion or loss is
  hidden by value equality, display formatting or a generic issue;
- invoke the real capture service and inspect retained originals, digests,
  projection/limitation references, generated identities and receipt through a
  separate store connection after commit and reopen; verify prior immutable
  records remain unchanged;
- keep E1 asset checks distinct from the unexecuted E2 product/storage evidence.

This slice adds no CLI case beyond the inventory's U + I allocation, changes no
product module and does not enable import.

## Preparation evidence and handoff

[Asset checks](../../tests/test_i01_numeric_retention_assets.py) use a tagged
numeric-lexeme observer and exact rational comparisons only for these small
synthetic inputs. They are independent of TDG's implementation and never rewrite
the original fixture files. They check exact sizes/digests, resource measures,
the isolated mutation and locator, loss witnesses, text-versus-number contrast
and the accepted case/level/oracle mapping.

The first focused run passed: **13 new asset checks; eight product skeletons
skipped**. Across all four families: **99 passed; 76 skipped** on Linux x86_64 /
CPython 3.12.14 with cached pytest 9.1.1 modules. TDG was not installed or run
under 3.12. Target Windows/Python 3.13 verification remains pending. This was
test-asset verification, not product regression, parser qualification or capture
execution. Existing assets, dependency pins and accepted snapshots are unchanged.

On a prepared target environment, the focused command is:

~~~powershell
.\.venv\Scripts\python.exe -m pytest -q -rs tests/test_i01_numeric_retention_assets.py tests/test_i01_numeric_retention_pending.py
~~~

BASE-01 plus 36 variants across ten case rows and two additional valid controls
are now materialized. This supplies assets and unbound skeletons for all listed
group-B variants (TC-I01-011–020); it does not execute or accept those product
cases, complete W02, or cover the whole 72-row / 208-variant inventory.
The data are exposed development material, not held-out acceptance evidence;
author checking remains solo AI-assisted. Effort is unreported and the forecast
remains provisional.

Next small slice: TC-I01-021, the seven title-presence/type variants in group C.
W02 remains open; no W03 GO or I-01 acceptance is claimed.
