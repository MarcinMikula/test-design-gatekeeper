"""TC-I01-030 awaits real declaration/context observations and capture services."""

import json
from pathlib import Path

import pytest

MANIFEST = json.loads((Path(__file__).parent / 'fixtures/i01/payload-authority/manifest.json').read_bytes())


@pytest.mark.parametrize('case', MANIFEST['cases'], ids=lambda c: c['id'])
@pytest.mark.skip(reason='W02-C: real mapping, trusted-context and authority-effect observers not connected')
def test_payload_claims_do_not_become_authority(case):
    """U: retain located declarations; qa-demo/ROLE-01 stays distinct from the payload ROLE-03 claim."""
    pytest.fail(f"Bind real context/effect observers, their harmless positive controls and no-adoption checks for {case['id']} before enabling")


@pytest.mark.parametrize('case', MANIFEST['cases'], ids=lambda c: c['id'])
@pytest.mark.skip(reason='W02-C: real capture, independent reopened-store checks and E3 observers not connected')
def test_payload_claims_capture_without_adoption_or_review(case):
    """I: preserve source and receipt; inspect actual context/effects and independently reopened history."""
    pytest.fail(f"Bind capture, E3 positive controls/trace and separate-store authority/assessment/immutable-record observations for {case['id']} before enabling")
