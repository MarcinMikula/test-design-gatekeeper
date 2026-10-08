"""W02-C placeholders with the levels accepted for TC-I01-011 through 015.

No real product boundary is bound here. Keep each skip until its assertions and
observations are implemented; fail guards prohibit an accidentally empty PASS.
See docs/implementation/i01-w02c-envelope-fixtures.md for exact binding work.
"""

import json
from pathlib import Path

import pytest


_MANIFEST = Path(__file__).parent / "fixtures/i01/envelope/manifest.json"
CASES = json.loads(_MANIFEST.read_bytes())["cases"]


@pytest.mark.parametrize("case", CASES, ids=lambda case: case["id"])
@pytest.mark.skip(reason="W02-C: real envelope component and diagnostic bindings unavailable")
def test_envelope_component(case):
    """U: envelope routing/validation only; no durable-capture conclusion."""
    pytest.fail(f"Bind actual envelope checks for {case['id']} before enabling")


@pytest.mark.parametrize("case", [c for c in CASES if "I" in c["levels"]], ids=lambda c: c["id"])
@pytest.mark.skip(reason="W02-C: actual capture/store and content-preservation observations unbound")
def test_envelope_capture(case):
    """I: original/projection/receipt, preservation and independent store reads."""
    pytest.fail(f"Bind real capture and durable observations for {case['id']} before enabling")


@pytest.mark.parametrize("case", [c for c in CASES if "C" in c["levels"]], ids=lambda c: c["id"])
@pytest.mark.skip(reason="W02-C: import CLI unavailable; exit/result and durable-effect checks unbound")
def test_envelope_cli(case):
    """C: installed entry point, bounded output/exit and actual durable effects."""
    pytest.fail(f"Bind real CLI and store assertions for {case['id']} before enabling")
