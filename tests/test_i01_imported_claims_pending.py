"""TC-I01-032 awaits actual identity, authority/history observers and capture services."""

import json
from pathlib import Path

import pytest

MANIFEST = json.loads((Path(__file__).parent / 'fixtures/i01/imported-claims/manifest.json').read_bytes())


@pytest.mark.parametrize('case', MANIFEST['cases'], ids=lambda c: c['id'])
@pytest.mark.skip(reason='W02-C: real projection, generated identity and trusted-effect observers not connected')
def test_imported_claim_is_not_a_trusted_identity_or_decision(case):
    """U: retain the located claim; observe real identity/context routing and no trusted promotion."""
    pytest.fail(f"Bind actual mapping/identity boundaries, calibrated effect observers and source-versus-authority checks for {case['id']} before enabling")


@pytest.mark.parametrize('case', MANIFEST['cases'], ids=lambda c: c['id'])
@pytest.mark.skip(reason='W02-C: actual capture, prior-history setup, E3 observers and independent store checks not connected')
def test_capture_preserves_claims_without_restoring_trusted_history(case):
    """I: new generated identities, honest receipt, no inferred decisions and unchanged prior records."""
    pytest.fail(f"Bind real capture, prior BASE-01 records, positive observer controls and reopened-store identity/history checks for {case['id']} before enabling")
