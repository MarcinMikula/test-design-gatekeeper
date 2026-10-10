"""U/I skeletons for TC-I01-022; no product assertions are bound yet.

See docs/implementation/i01-w02c-step-representation-fixtures.md. The fixture
observations do not establish actual TDG projection, source fidelity or storage.
"""

import json
from pathlib import Path

import pytest


_MANIFEST = Path(__file__).parent / "fixtures/i01/step-representation/manifest.json"
CASES = json.loads(_MANIFEST.read_bytes())["cases"]


@pytest.mark.parametrize("case", CASES, ids=lambda c: c["id"])
@pytest.mark.skip(reason="W02-C: real step representation, ordering and source-locator observations unbound")
def test_step_representation_component(case):
    """U: retain narrative/array form, occurrences, numbers and expectation locations."""
    pytest.fail(f"Bind actual steps/source assertions for {case['id']} before enabling")


@pytest.mark.parametrize("case", CASES, ids=lambda c: c["id"])
@pytest.mark.skip(reason="W02-C: capture service, containment and independent store checks unbound")
def test_step_representation_capture(case):
    """I: inspect retained source/projection/receipt and each step occurrence after reopen."""
    pytest.fail(f"Bind actual capture/store assertions for {case['id']} before enabling")
