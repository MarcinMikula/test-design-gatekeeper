"""U/I skeletons for TC-I01-021; no product assertions are bound yet.

See docs/implementation/i01-w02c-title-presence-fixtures.md. The accepted
presence states must be observed from TDG; passing fixture checks cannot
establish classification, preserved deficiencies or durable capture.
"""

import json
from pathlib import Path

import pytest


_MANIFEST = Path(__file__).parent / "fixtures/i01/title-presence/manifest.json"
CASES = json.loads(_MANIFEST.read_bytes())["cases"]


@pytest.mark.parametrize("case", CASES, ids=lambda c: c["id"])
@pytest.mark.skip(reason="W02-C: real title presence, mapping and source-boundary observations unbound")
def test_title_presence_component(case):
    """U: observe the accepted state, retained value/absence and no coercion."""
    pytest.fail(f"Bind actual presence/source assertions for {case['id']} before enabling")


@pytest.mark.parametrize("case", CASES, ids=lambda c: c["id"])
@pytest.mark.skip(reason="W02-C: capture service, containment and independent store checks unbound")
def test_title_presence_capture(case):
    """I: CAPTURED despite deficiency; inspect original/projection/receipt after reopen."""
    pytest.fail(f"Bind actual capture/store assertions for {case['id']} before enabling")
