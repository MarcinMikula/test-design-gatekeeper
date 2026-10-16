"""TC-I01-027 component tests wait for TDG's selected origin mapping."""

import json
from pathlib import Path

import pytest

CASES = json.loads((Path(__file__).parent / 'fixtures/i01/origin-unmapped/manifest.json').read_bytes())['cases']


@pytest.mark.parametrize('case', CASES, ids=lambda c: c['id'])
@pytest.mark.skip(reason='W02-C: real mapping version, no-alias setup and origin/source observations not connected')
def test_unmapped_origin_component(case):
    """U: preserve text and location as VALUE/UNMAPPED; infer no origin, adoption or authority."""
    pytest.fail(f"Connect the real mapper, uppercase control and no-alias/source checks for {case['id']} before enabling")
