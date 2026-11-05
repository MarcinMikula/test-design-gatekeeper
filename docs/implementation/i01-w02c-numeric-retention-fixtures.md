# I-01 / W02-C — Preserving exact numbers and text

Prepared and checked 2026-10-09 (Europe/Warsaw).
Source pin: `main` at `1e2a637e54a891be4c078759d695f8f2893b4f24`.

These four inputs cover TC-I01-019–020 from the [accepted inventory](i01-w02-test-inventory.md).
They specify how TDG must preserve a number's original written form and keep
JSON strings containing digits as text. The files are prepared; tests of TDG's
behavior still need to be connected to the implementation.

The results below describe the 2026-10-09 checks. Development and further test-data
preparation are currently paused; [README.md](../../README.md) gives the current
project status.

The [manifest](../../tests/fixtures/i01/numeric-retention/manifest.json) records
exact sizes and hashes, source values and locations, expected outcomes, U/I test
levels, E1/E2 evidence and requirement links. Its fields describe tests, not a new
TDG data format or runtime issue codes.

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

Exact file sizes and resource measurements remain in the manifest. Each numeric
case is below the 128-character token limit; the other input, count and text
bounds also remain below their limits.

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

The governing rules are in [RA-09 Sections 3.3 and 4.1](../requirements-analysis/ra-09/test-design-gatekeeper-ra-09-data-representations-import-export-contracts-v0.2.md)
and [SAD-04 Sections 6.1 and 9](../solution-design/test-design-gatekeeper-sad-04-integrated-review-increment-plan-v0.2.md#61-native-input-and-mechanical-projection).
The numeric-token rule is incorporated in SAD-04; the
[SAD04-I01-NUM-001 record](../solution-design/test-design-gatekeeper-sad-04-i01-numeric-token-limit-addendum-v0.1.md)
retains the decision. OR-I01-SYN-005 / FID-003 / SYN-004 in the
[W02 oracle basis](i01-w02-test-design.md) specify the expected observations.
Trace reaches TCND-I01-05/06/10, RA09-REQ-004/006/016 and RA09-VAL-003/006 as
allocated per case in the manifest.

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

The [eight product-test placeholders](../../tests/test_i01_numeric_retention_pending.py)
cover four component and four integration tests, with explicit skips and fail
guards. Before enabling them:

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

The test allocation remains U + I, with no additional CLI case. Product code
is unchanged and import remains unavailable.

<a id="preparation-evidence-and-handoff"></a>

## What was checked and what remains to do

[Input checks](../../tests/test_i01_numeric_retention_assets.py) use a tagged
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

At that date, the prepared material comprised `BASE-01` and 36 input variants
for ten cases (TC-I01-011–020), plus two additional valid comparison files.
One input can be used by several checks. The pytest totals above count checks
and skipped placeholders; they do not establish passed TDG cases.

These synthetic development inputs are already known to the author and cannot
serve as previously unseen acceptance data. The author performed the checks
with AI assistance. They do not count as an independent human review.

Human time spent was not reported. [Inventory Section 7](i01-w02-test-inventory.md#7-effort-reassessment)
retains the provisional forecast and reassessment requirements. Preparing these
files and checking them did not close W02, authorize W03 or accept I-01.
