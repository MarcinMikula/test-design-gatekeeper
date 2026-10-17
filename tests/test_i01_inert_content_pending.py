"""TC-I01-031 awaits real projection, side-effect observers and capture services."""

import json
from pathlib import Path

import pytest

MANIFEST = json.loads((Path(__file__).parent / 'fixtures/i01/inert-content/manifest.json').read_bytes())


@pytest.mark.parametrize('case', MANIFEST['cases'], ids=lambda c: c['id'])
@pytest.mark.skip(reason='W02-C: real projection, resolver/execution observers and safe diagnostic checks not connected')
def test_reference_or_instruction_remains_inert(case):
    """U: retain the located string; observe attempts and safe projections with calibrated observers."""
    pytest.fail(f"Bind real projection, all forbidden-attempt observers, positive controls and E4 checks for {case['id']} before enabling")


@pytest.mark.parametrize('case', MANIFEST['cases'], ids=lambda c: c['id'])
@pytest.mark.skip(reason='W02-C: actual capture, parent/worker E3/E4 observations and independent store checks not connected')
def test_capture_does_not_follow_or_execute_supplied_content(case):
    """I: one selected original; no reference-driven read/fetch/execution, even if an attempt is blocked."""
    pytest.fail(f"Bind real capture, calibrated parent/worker observers, routine diagnostics and reopened-store checks for {case['id']} before enabling")
