# I-01 / W02-C — A claim in a file does not grant a role

Prepared and checked on 2026-10-17 (Europe/Warsaw).
Starting repository version: `main` at `f1bc627c372d0da548489457a7b8197f81194e86`.
Status: **one input file prepared; two tests of TDG still need to be connected to the implementation**.

This work prepares TC-I01-030 from the accepted
[test inventory](i01-w02-test-inventory.md). The file names a person, claims that
they hold ROLE-03 and says they have accepted responsibility for a test case.
TDG must preserve those declarations. The declarations alone cannot establish
that the person holds the role or has made an attributable acceptance decision.

ROLE-03 is the logical role responsible for accepting accountability for and
repairing test cases. ROLE-01 operates intake. The actual operator and authority
come from the trusted context of the operation, outside the imported file.

## Prepared example

The [input file](../../tests/fixtures/i01/payload-authority/TC-I01-030.json)
starts from [BASE-01](../../tests/fixtures/i01/base-01.json). It adds three
declarations and leaves the scope, basis, test-case source ID, steps, age,
expected result and `HUMAN_AUTHORED` origin unchanged.

| Location in the input | Supplied declaration |
| --- | --- |
| `/content/role` | `ROLE-03` |
| `/content/actor_ref` | `qa-claimed-demo` |
| `/content/test_cases/0/accountability` | `actor_ref: qa-claimed-demo`, `accepted: true` |

The role and actor fields inside `content` are supplied claims. They are not
new control-envelope fields or a way to configure TDG's authority. The
accountability value is a JSON Boolean `true`, not a string or number.
All names and test data are synthetic.

The separate test setup uses operator `qa-demo`, acting as ROLE-01, with
permission for synthetic data and the `lab-development` purpose. The claimed
actor `qa-claimed-demo` has no corresponding ROLE-03 authority or applicable
acceptance in that context. The two names deliberately differ so that a test
can detect an implementation that substitutes the person named in the file for
the actual operator.

The file has **1218 bytes**, 29 JSON values, a maximum container depth of six,
one native test case and one basis element. It uses valid UTF-8 JSON without a
BOM or duplicate members and stays below the accepted resource limits.

## Expected result

Under the complete controlled import path, the file should produce `CAPTURED`
and a new package-version reference. The lack of ROLE-03 acceptance does not
prevent faithful capture at this stage. Intake permission and all other
admission, containment and store prerequisites must still hold.

The original bytes and declarations must remain available with their source
locations, mapping status and applicable issues. The receipt must identify the
actual operation context. Import must not change that context, grant the claimed
role or turn `accepted: true` into a human adoption decision.

I-01 does not assess test-case eligibility, domain qualification or the minimum
conditions for review. The minimum remains `NOT_EVALUATED`, with reason
`MINIMUM_CHECK_NOT_ENABLED_IN_I01`. No review run, substantive assessment ledger
or calculated result availability is created. Inspection must say that review
was not performed.

The [manifest](../../tests/fixtures/i01/payload-authority/manifest.json) records
the test setup, exact byte size and SHA-256 digest, source pointers and byte
ranges for all claims. These are test expectations, not a proposed TDG API or
database schema. They do not prescribe an issue code or introduce a new role
management system.

The expected behavior comes from OR-I01-AUTH-005 and OR-I01-FID-009 in the
[W02 test design](i01-w02-test-design.md), covering TCND-I01-07, 08 and 15.
It traces to RA09-REQ-008/024 and RA09-VAL-007/008/015. The detailed rules are
[RA-09 §§2.3, 3.1–3.3 and 4.2](../requirements-analysis/ra-09/test-design-gatekeeper-ra-09-data-representations-import-export-contracts-v0.2.md).
[SAD-04 §§6.1–6.2](../solution-design/test-design-gatekeeper-sad-04-integrated-review-increment-plan-v0.2.md)
defines the I-01 capture and status boundary. These links identify the governing
rules; this example does not establish full fulfilment of those requirements.

## What was checked

The [six checks of the input data and setup](../../tests/test_i01_payload_authority_assets.py)
passed. They verify the exact bytes, intended changes from BASE-01, resource
measurements, locations and values of all claims, separation from the planned
operation context, and consistency with the inventory. The focused run had no
failures or warnings.

Across all fourteen groups of test data, **212 checks passed and 144 product-test
placeholders were skipped**. The combined check used a fresh checkout of the
staged files with Git's automatic line-ending conversion enabled. All JSON
fixture bytes remained unchanged, as required by `.gitattributes`.

The checks ran on Linux x86_64 / CPython 3.12.14 with cached pytest 9.1.1 modules.
TDG was not installed or run under that Python version. Verification on the
target Windows/Python 3.13 environment and tests of TDG's actual authority and
capture behavior remain to be done. Product regression tests were not run for
this change to test data and test placeholders.

## What the product tests still need

The [two product-test placeholders](../../tests/test_i01_payload_authority_pending.py)
have explicit skips and fail guards. One will test the mapping/context boundary;
the other will exercise import with a real disposable store. Both need actual
observations of TDG before they can be enabled.

The inventory requires an operation trace as evidence E3. Before capture, record
the actual context, the absence of the claimed authority and adoption, and the
relevant prior records. Observe any role or adoption effects and any invocation
of eligibility, qualification or review. Exercise each observer with an
identifiable, harmless test probe, then separate or reset those probe records
before the case. An empty trace proves nothing if the observer was never shown
to work. The probe must not grant a role, create adoption or enable review.

After capture, compare the actual context and reopen the store through a
separate connection. Check the retained source, claims, mapping issues,
identities and receipt. Inspect relevant logical records for unintended human
decisions or assessment effects, and confirm that prior immutable records remain
unchanged. Comparing the whole SQLite file would be misleading because a valid
capture must add records.

This observation protocol is prepared, but its observers and positive controls
have not run against TDG. A test-only authorization function or an expected
Boolean in the manifest cannot supply that evidence.

Once the target environment is prepared, run:

~~~powershell
.\.venv\Scripts\python.exe -m pytest -q -rs tests/test_i01_payload_authority_assets.py tests/test_i01_payload_authority_pending.py
~~~

## Progress and next step

Prepared data now include BASE-01, 71 input variants for 20 test cases
(TC-I01-011–030) and two valid comparison files. The full plan contains 72 cases
with 208 variants.

These synthetic examples are already visible to the author and cannot later be
described as previously unseen acceptance data. The checks were performed with
AI assistance and do not count as an independent human review. No record of human
time spent was provided; the effort estimate remains provisional.

W02 (test preparation) is still in progress. Starting W03 and accepting the whole
I-01 increment require separate decisions. The next planned task is TC-I01-031:
URLs, paths, references and instructions inside the supplied content must remain
data, without causing retrieval or execution.
