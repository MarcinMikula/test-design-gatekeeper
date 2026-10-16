"""TC-I01-026 product tests wait for the real mapper and capture service."""

import json
from pathlib import Path

import pytest

CASES = json.loads((Path(__file__).parent / 'fixtures/i01/origin-literals/manifest.json').read_bytes())['cases']


@pytest.mark.parametrize('case', CASES, ids=lambda c: c['id'])
@pytest.mark.skip(reason='W02-C: selected mapping version and actual origin/presence/source observations not connected')
def test_origin_literal_component(case):
    """U: preserve each declaration, observe its literal mapping, and keep accountability absent."""
    pytest.fail(f"Connect the real mapping and source checks for {case['id']} before enabling")


@pytest.mark.parametrize('case', CASES, ids=lambda c: c['id'])
@pytest.mark.skip(reason='W02-C: capture service, receipt and independent store observations not connected')
def test_origin_literal_capture(case):
    """I: inspect committed bytes, mapping, receipt and NOT_EVALUATED; no authority or adoption inferred."""
    pytest.fail(f"Connect the actual import/store checks for {case['id']} before enabling")
