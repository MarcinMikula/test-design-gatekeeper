# I-01 / W02-C — Links and instructions stay as data

Prepared and checked on 2026-10-17 (Europe/Warsaw).
Starting repository version: `main` at `35565b5d0b74ebccaa6e36bf91640c8945f4d048`.
Status: **five input files prepared; ten tests of TDG still need to be connected to the implementation**.

This work prepares TC-I01-031 from the accepted
[test inventory](i01-w02-test-inventory.md). A file may contain a link, a path or
text that looks like a command. Importing the file must preserve that text
without opening the link, reading another file or running the command.

## Prepared examples

Each input starts from [BASE-01](../../tests/fixtures/i01/base-01.json) and adds
one string inside `content.supplementary_content`. The test case, scope, basis,
source IDs, steps, age, expected result and origin remain unchanged.

| Variant | Added content | File bytes |
| --- | --- | ---: |
| TC-I01-031.01 | An HTTPS URL under `url`, with marker `TC031-URL-MARKER` | 1141 |
| TC-I01-031.02 | A synthetic Windows file path under `path`, with marker `TC031-PATH-MARKER` | 1146 |
| TC-I01-031.03 | A `$ref` member pointing to an HTTPS schema address, with marker `TC031-REF-MARKER` | 1154 |
| TC-I01-031.04 | Issue key `TDG031-404` under `issue_key` | 1121 |
| TC-I01-031.05 | `cmd.exe /c echo TC031-EXEC-MARKER` under `instruction` | 1146 |

The URLs use the synthetic host `tdg.invalid`. The Windows path is
`C:\TDG-Synthetic\TC031-PATH-MARKER.txt`; it does not identify a user's file.
The last string would only print a marker if deliberately run, but the fixture
preparation and data checks do not execute it. No referenced resource was opened
or created for these checks.

Each file contains one native test case, one basis element and 26 JSON values,
with a maximum container depth of six. All five use valid UTF-8 JSON without a
BOM or duplicate members and stay below the accepted resource limits. The
[manifest](../../tests/fixtures/i01/inert-content/manifest.json) records exact
sizes, SHA-256 digests, source pointers and byte ranges for the added content.

## Expected result

Under the complete controlled import path, each file should produce `CAPTURED`
and a new package-version reference. The operation selects only that JSON file.
Its embedded references must not add sources, supply missing business evidence,
change the selected schema or trigger an issue-tracker lookup.

TDG must preserve the original bytes and added string with its source location,
mapping status and applicable issues. The `$ref` is a member of the supplied
content, not permission to download or register a schema. Schemas still come
from the approved local registry selected by the native contract and version.

I-01's minimum remains `NOT_EVALUATED`, with reason
`MINIMUM_CHECK_NOT_ENABLED_IN_I01`, and review is not performed. These outcomes
assume the approved Windows x64 / CPython 3.13 laboratory setup, synthetic-data
permission, a fresh operation ID, a healthy isolated store and effective
admission and containment controls.

The governing oracle is OR-I01-FID-008 in the
[W02 test design](i01-w02-test-design.md), covering TCND-I01-08 and 16.
The source rules are RA03-REQ-005, RA09-REQ-003/005/023 and RA08-REQ-010;
validation routes include RA09-VAL-002/013 and RA08-VAL-004/007.
See [RA-08 §§4.2 and 6.2](../requirements-analysis/ra-08/test-design-gatekeeper-ra-08-confidentiality-security-privacy-v0.2.md),
[RA-09 §§3.1, 3.3 and 3.4](../requirements-analysis/ra-09/test-design-gatekeeper-ra-09-data-representations-import-export-contracts-v0.2.md)
and [SAD-04 §§6.1–6.2, 7.1 and 9](../solution-design/test-design-gatekeeper-sad-04-integrated-review-increment-plan-v0.2.md).
This example covers the bounded I-01 behavior, not every obligation in those
requirements.

## What was checked

The [13 checks of the input data and setup](../../tests/test_i01_inert_content_assets.py)
passed. They verify the exact bytes, intended changes from BASE-01, resource
measurements, source locations, five distinct stimulus forms and markers, and
consistency with the accepted inventory. URL and path checks inspect strings;
they do not resolve a host or open the indicated file. The focused run had no
failures or warnings.

Across all fifteen groups of test data, **225 checks passed and 154 product-test
placeholders were skipped**. The combined check used a fresh checkout of the
staged files with Git's automatic line-ending conversion enabled. All JSON
fixture bytes remained unchanged, as required by `.gitattributes`.

The checks ran on Linux x86_64 / CPython 3.12.14 with cached pytest 9.1.1 modules.
TDG was not installed or run under that Python version. Verification on the
target Windows/Python 3.13 environment and tests of TDG's actual handling remain
to be done. Product regression tests were not run for this change to test data
and test placeholders.

## What the product tests still need

The [ten product-test placeholders](../../tests/test_i01_inert_content_pending.py)
have explicit skips and fail guards. Five will test the component boundary;
five will exercise import and real storage. The manifest describes the required
operation trace (E3) and safe diagnostic observations (E4), but those observers
and their controls have not yet run against TDG.

For every variant, observe attempts to open a referenced file, resolve a source
or remote schema, use the network, or execute supplied code or a shell command.
Observe both the parent and parser worker, before a system guard can deny the
action. A missing file, DNS error or blocked connection does not establish that
TDG made no attempt. A blocked forbidden attempt still fails this case.

First prove that each observer detects a harmless controlled probe. Use an
isolated disposable file, a controlled local endpoint or intercepted attempt,
resolver probes and a harmless execution probe. Keep probe observations separate
from the actual case, and never use the source strings as instructions for
setting up those probes. An observer that was not shown to work cannot support
a claim of no attempts.

The operation is allowed to read its explicitly selected input, approved local
configuration and schemas, runtime files and store. It also needs its configured
parser worker. Record those expected activities separately so they are not
mistaken for actions caused by the payload. A legitimate parser-worker start
does not authorize another process requested by the supplied command.

Capture bounded routine stdout, stderr and logs. They must not echo the source
value or its marker, including escaped representations. Prove the marker check
works using a separate test buffer. Deliberate authorized source inspection is
a different surface: it may show retained content safely, with escaping and
output bounds, without automatically opening links or executing text. Do not
create a second raw-payload archive in diagnostic logs.

After capture, reopen the store through a separate connection. Check the exact
source, added content, one-file inventory, mapping identity, issues and receipt.
Prior immutable records must remain unchanged. These assertions must use TDG's
actual observations; a no-op replacement importer would not test the boundary.
Record any observer blind spots. This laboratory test does not establish the
separate protected operating profile or prove that every possible network path
has been excluded.

Once the target environment is prepared, run:

~~~powershell
.\.venv\Scripts\python.exe -m pytest -q -rs tests/test_i01_inert_content_assets.py tests/test_i01_inert_content_pending.py
~~~

## Progress and next step

Prepared data now include BASE-01, 76 input variants for 21 test cases
(TC-I01-011–031) and two valid comparison files. The full plan contains 72 cases
with 208 variants.

These synthetic examples are already visible to the author and cannot later be
described as previously unseen acceptance data. The checks were performed with
AI assistance and do not count as an independent human review. No record of human
time spent was provided; the effort estimate remains provisional.

W02 (test preparation) is still in progress. Starting W03 and accepting the whole
I-01 increment require separate decisions. The next planned task is TC-I01-032:
supplied identifiers, roles, approvals, statuses and qualification claims must
remain declarations without restoring trusted history or creating authority.
