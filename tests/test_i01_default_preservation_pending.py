"""TC-I01-029 product tests wait for TDG's actual default handling and capture."""

import json
from pathlib import Path

import pytest

CASES = json.loads((Path(__file__).parent / 'fixtures/i01/default-preservation/manifest.json').read_bytes())['cases']


@pytest.mark.parametrize('case', CASES, ids=lambda c: c['id'])
@pytest.mark.skip(reason='W02-C: actual source presence, mapping and no-default observations not connected')
def test_explicit_declaration_component(case):
    """U: retain the explicit value, presence and mapping; apply no positive default or authority upgrade."""
    pytest.fail(f"Connect the real mapping, no-default and located-source checks for {case['id']} before enabling")


@pytest.mark.parametrize('case', CASES, ids=lambda c: c['id'])
@pytest.mark.skip(reason='W02-C: actual capture, receipt and independent reopened-store observations not connected')
def test_explicit_declaration_capture(case):
    """I: preserve explicit declarations and issues in the committed store; keep minimum NOT_EVALUATED."""
    pytest.fail(f"Connect the actual import, source preservation, receipt and immutable-store checks for {case['id']} before enabling")
