"""TC-I01-024 product observations remain unbound; asset PASS is not product evidence."""
import json
from pathlib import Path
import pytest

CASES = json.loads((Path(__file__).parent / 'fixtures/i01/source-id-fidelity/manifest.json').read_bytes())['cases']


@pytest.mark.parametrize('case', CASES, ids=lambda c: c['id'])
@pytest.mark.skip(reason='W02-C: real source-ID projection and locator observations unbound')
def test_source_id_fidelity_component(case):
    """U: exact strings/code points/order at original locators; no coercion or merge."""
    pytest.fail(f"Bind real projection observations for {case['id']} before enabling")


@pytest.mark.parametrize('case', CASES, ids=lambda c: c['id'])
@pytest.mark.skip(reason='W02-C: capture service and durable source-ID observations unbound')
def test_source_id_fidelity_capture(case):
    """I: inspect bytes, two independent item IDs, source values/links and receipt after reopen."""
    pytest.fail(f"Bind actual capture/store observations for {case['id']} before enabling")
