"""TC-I01-028 product tests wait for TDG's defaulting and capture components."""

import json
from pathlib import Path

import pytest

CASES = json.loads((Path(__file__).parent / 'fixtures/i01/case-defaults/manifest.json').read_bytes())['cases']


@pytest.mark.parametrize('case', CASES, ids=lambda c: c['id'])
@pytest.mark.skip(reason='W02-C: actual scoped defaults, source presence and effective-value observations not connected')
def test_case_defaults_component(case):
    """U: default only the absent field; retain the explicit value and both source locations."""
    pytest.fail(f"Connect the real mapping, scope and supplied/effective-value checks for {case['id']} before enabling")


@pytest.mark.parametrize('case', CASES, ids=lambda c: c['id'])
@pytest.mark.skip(reason='W02-C: real capture, receipt and independent reopened-store checks not connected')
def test_case_defaults_capture(case):
    """I: retain two TC, original bytes and default provenance; infer no authority or review verdict."""
    pytest.fail(f"Connect the actual capture, provenance, receipt and immutable-store checks for {case['id']} before enabling")
