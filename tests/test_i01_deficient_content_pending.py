"""TC-I01-025: connect these tests to TDG before removing the explicit skips."""

import json
from pathlib import Path

import pytest

CASES = json.loads((Path(__file__).parent / 'fixtures/i01/deficient-content/manifest.json').read_bytes())['cases']


@pytest.mark.parametrize('case', CASES, ids=lambda c: c['id'])
@pytest.mark.skip(reason='W02-C: content projection, source locations and visible issues need actual TDG observations')
def test_deficient_content_component(case):
    """U: retain unknown/mistyped values or trustworthy raw boundary; expose deficiencies without repairs."""
    pytest.fail(f"Connect real projection/issue checks for {case['id']} before enabling")


@pytest.mark.parametrize('case', CASES, ids=lambda c: c['id'])
@pytest.mark.skip(reason='W02-C: import service and independent inspection of committed data are not connected')
def test_deficient_content_capture(case):
    """I: inspect original, projection, issues, receipt and NOT_EVALUATED after commit/reopen."""
    pytest.fail(f"Connect actual import/store checks for {case['id']} before enabling")
