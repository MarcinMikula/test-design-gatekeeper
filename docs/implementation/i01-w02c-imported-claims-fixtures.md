# I-01 / W02-C — Labels in a file do not create decisions or permissions

Prepared and checked on 2026-10-18 (Europe/Warsaw).
Starting repository version: `main` at `531fb50cb9d90a570e50f97f41ea0e9919469a31`.
Status: **five input files prepared; ten tests of TDG still need to be connected to the implementation**.

This work prepares TC-I01-032 from the accepted
[test inventory](i01-w02-test-inventory.md). A supplied file can claim an identity,
role, approval, completion status or qualification. TDG must retain that claim,
but the claim cannot become a trusted system record or a human decision merely
because the file was imported.

## Prepared examples

Each input starts from [BASE-01](../../tests/fixtures/i01/base-01.json) and adds
one member directly inside `content`. The original scope, basis, test case,
source IDs, steps, age, expected result and origin remain unchanged.

| Variant | Added field and value | What the claim must not do | File bytes |
| --- | --- | --- | ---: |
| TC-I01-032.01 | `package_id: 11111111-2222-4333-8444-555555555555` | Become a TDG package, lineage or version identity | 1109 |
| TC-I01-032.02 | `role: ROLE-05` | Grant the claimed role or change the operator's role | 1074 |
| TC-I01-032.03 | `approval: ACCEPTED` | Create an approval or accepted finding disposition | 1079 |
| TC-I01-032.04 | `status: COMPLETED` | Create a completed review run or change the actual capture outcome | 1078 |
| TC-I01-032.05 | `qualification: IN_SCOPE` | Establish that the content was assessed and found in scope | 1084 |

All five added values are strings. The supplied identifier is a syntactically
valid UUIDv4, so the first example tests the separation of identities rather
than malformed identifier handling. The other values deliberately resemble
TDG's role and status vocabulary. These content members remain supplied claims;
they are not new control-envelope fields or configuration options.

The separate operation context uses `qa-demo` acting as ROLE-01, with permission
for synthetic data and the `lab-development` purpose. ROLE-05, the role that
dispositions findings, is not granted in that context. Each operation has a
fresh ID and no selected predecessor.

Each file contains one native test case, one basis element and 25 JSON values,
with a maximum container depth of six. All five use valid UTF-8 JSON without a
BOM or duplicate members and stay below the accepted resource limits. The
[manifest](../../tests/fixtures/i01/imported-claims/manifest.json) records exact
sizes, SHA-256 digests, source pointers and byte ranges for the claims.

## Expected result

Under the complete controlled import path, each file should produce `CAPTURED`
with a new package version and lineage. TDG generates the actual identities.
In the first variant, the new package, lineage and version identities must
differ from the supplied UUID. The original UUID still remains in the source.

The role, approval, status and qualification strings must also remain available
with their source locations, mapping status and applicable issues. They must
not alter trusted context or policy, restore trusted history, or create an
approval, disposition or qualification decision.

I-01 does not assess eligibility or domain qualification. Its minimum remains
`NOT_EVALUATED`, with reason `MINIMUM_CHECK_NOT_ENABLED_IN_I01`, and review is not
performed. No review run, substantive ledger or calculated result availability
is created. The supplied `COMPLETED` string must not replace the actual capture
outcome or cause an unavailable review path to run.

These outcomes assume the approved Windows x64 / CPython 3.13 laboratory setup,
an eligible operation, a healthy isolated store and all required admission,
containment and resource controls. The manifest describes test expectations,
not a new TDG API, database schema or set of runtime status values.

The governing oracle is OR-I01-FID-009 in the
[W02 test design](i01-w02-test-design.md), covering TCND-I01-08 and 15 and tracing
to RA09-REQ-024 and RA09-VAL-008/015. See
[RA-09 §§2.2–2.3, 3.1–3.3, 4.1 and 7.3](../requirements-analysis/ra-09/test-design-gatekeeper-ra-09-data-representations-import-export-contracts-v0.2.md)
and [SAD-04 §§5–7](../solution-design/test-design-gatekeeper-sad-04-integrated-review-increment-plan-v0.2.md).
These references identify the relevant rules; this case does not verify the
later export or assessment obligations also present in those sources.

## What was checked

The [13 checks of the input data and setup](../../tests/test_i01_imported_claims_assets.py)
passed. They verify exact bytes, the single intended change in each file,
resource measurements, source locations, fixed values, the UUID's form, the
planned operation context and consistency with the accepted inventory. The
focused run had no failures or warnings.

Across all sixteen groups of test data, **238 checks passed and 164 product-test
placeholders were skipped**. The combined check used a fresh checkout of the
staged files with Git's automatic line-ending conversion enabled. All JSON
fixture bytes remained unchanged, as required by `.gitattributes`.

The checks ran on Linux x86_64 / CPython 3.12.14 with cached pytest 9.1.1 modules.
TDG was not installed or run under that Python version. Verification on the
target Windows/Python 3.13 environment and tests of TDG's actual identity and
authority handling remain to be done. Product regression tests were not run
for this change to test data and test placeholders.

## What the product tests still need

The [ten product-test placeholders](../../tests/test_i01_imported_claims_pending.py)
have explicit skips and fail guards. Five will test the component boundary;
five will exercise import with a real store. Their identity, authority and
history observations have not yet run against TDG.

For each integration variant, first capture BASE-01 through the actual service
in an isolated store. Record its generated identities, receipt and relevant
immutable-record digests. Before the identifier variant, check that the supplied
UUID is absent from trusted package, lineage and version identities. Keep the
actual operator context and policy separate from the input.

Observe real identity allocation and any changes or attempted changes to roles,
approvals, qualification, review or trusted history. Prove each observer can
detect a harmless controlled probe, then separate or reset those probe records
before the case. The probe must not grant a role, create a human decision or
enable review. An empty trace from an untested observer is insufficient.

After capture, close and reopen the store through a separate connection.
Compare the actual receipt, generated identities, retained claims and prior
immutable records. Check the permitted logical effects rather than comparing
the entire SQLite file, because a successful capture must add records.

Finding `ACCEPTED`, `COMPLETED` or `IN_SCOPE` in the retained source is expected.
The test must check whether that text was improperly promoted into a trusted
decision or result. A global search that rejects those strings anywhere in the
store would incorrectly reject faithful preservation. Likewise, the supplied
UUID must remain as source data while TDG uses its own generated identities.

Bind these checks to the actual service boundaries and store model. No extra
review, disposition or qualification tables are needed for this test. A
test-only identity generator or authorization function would not establish TDG's
behavior. Missing essential observations must remain visible, and the tests
must stay skipped until those observations are connected.

Once the target environment is prepared, run:

~~~powershell
.\.venv\Scripts\python.exe -m pytest -q -rs tests/test_i01_imported_claims_assets.py tests/test_i01_imported_claims_pending.py
~~~

## Progress and next step

Prepared data now include BASE-01, 81 input variants for 22 test cases
(TC-I01-011–032) and two valid comparison files. The full plan contains 72 cases
with 208 variants.

These synthetic examples are already visible to the author and cannot later be
described as previously unseen acceptance data. The checks were performed with
AI assistance and do not count as an independent human review. No record of human
time spent was provided; the effort estimate remains provisional.

W02 (test preparation) is still in progress. Starting W03 and accepting the whole
I-01 increment require separate decisions. The next planned task is TC-I01-033:
a declaration about an additional source must not cause TDG to search for or
open a file that the operation did not explicitly select.
