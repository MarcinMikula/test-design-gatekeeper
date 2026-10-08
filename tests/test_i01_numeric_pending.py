"""Traceable W02-C skeletons: no product assertion is executable yet.

Remove a skip only when that real boundary and its complete observations are
bound. Fail guards prevent a removed decorator from producing an empty PASS.
The companion asset tests do not supply product evidence for these skeletons.
See docs/implementation/i01-w02c-numeric-fixtures.md for the binding checklist.
"""

import json
from pathlib import Path

import pytest


_MANIFEST = Path(__file__).parent / "fixtures/i01/numeric-token/manifest.json"
CASES = json.loads(_MANIFEST.read_bytes())["cases"]


@pytest.mark.parametrize("case", CASES, ids=lambda case: case["id"])
@pytest.mark.skip(reason="W02-C: numeric-token component boundary not implemented/bound")
def test_numeric_token_component(case):
    """U: assert only the length decision, never a durable-capture conclusion."""
    pytest.fail(f"Bind the real component assertion for {case['id']} before enabling")


@pytest.mark.parametrize("case", CASES, ids=lambda case: case["id"])
@pytest.mark.skip(reason="W02-C: capture service, containment and store observations unbound")
def test_numeric_token_capture(case):
    """I: inspect receipt/source/projection and durable effects independently."""
    pytest.fail(f"Bind the real capture/store assertions for {case['id']} before enabling")


@pytest.mark.parametrize("case", CASES, ids=lambda case: case["id"])
@pytest.mark.skip(reason="W02-C: import CLI unavailable; result/exit/diagnostic observations unbound")
def test_numeric_token_cli(case):
    """C: invoke installed entry point and inspect output, exit and real effects."""
    pytest.fail(f"Bind the real CLI assertions for {case['id']} before enabling")
