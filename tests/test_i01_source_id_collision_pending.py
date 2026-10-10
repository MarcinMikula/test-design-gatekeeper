"""U/I skeletons for TC-I01-023; actual identity/link assertions are unbound.

See docs/implementation/i01-w02c-source-id-collision-fixtures.md. A source
candidate observer or generated test UUID is not evidence of TDG identity.
"""

import json
from pathlib import Path

import pytest


_MANIFEST = Path(__file__).parent / "fixtures/i01/source-id-collisions/manifest.json"
CASES = json.loads(_MANIFEST.read_bytes())["cases"]


@pytest.mark.parametrize("case", CASES, ids=lambda c: c["id"])
@pytest.mark.skip(reason="W02-C: real occurrence, duplicate-key and ambiguous-link observations unbound")
def test_source_id_collision_component(case):
    """U: preserve items and supplied keys; expose the collision without guessing links."""
    pytest.fail(f"Bind actual collision/link assertions for {case['id']} before enabling")


@pytest.mark.parametrize("case", CASES, ids=lambda c: c["id"])
@pytest.mark.skip(reason="W02-C: capture service and durable item-identity/source-link checks unbound")
def test_source_id_collision_capture(case):
    """I: verify distinct TDG IDs, original locations, receipt and unresolved links after reopen."""
    pytest.fail(f"Bind actual identity/store assertions for {case['id']} before enabling")
