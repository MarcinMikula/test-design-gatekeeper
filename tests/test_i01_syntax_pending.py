"""U/C skeletons for TC-I01-016–017; no TDG product assertions are bound yet.

See docs/implementation/i01-w02c-syntax-fixtures.md. Asset observations from
Python's decoder do not prove the future TDG parser rejects the same sources.
"""

import json
from pathlib import Path

import pytest


_MANIFEST = Path(__file__).parent / "fixtures/i01/syntax/manifest.json"
CASES = json.loads(_MANIFEST.read_bytes())["cases"]


@pytest.mark.parametrize("case", CASES, ids=lambda c: c["id"])
@pytest.mark.skip(reason="W02-C: real syntax/profile and pre-projection observations unbound")
def test_native_syntax_profile_component(case):
    """U: reject the intended cause; qualify observers with valid controls."""
    pytest.fail(f"Bind actual syntax/profile assertions for {case['id']} before enabling")


@pytest.mark.parametrize("case", CASES, ids=lambda c: c["id"])
@pytest.mark.skip(reason="W02-C: import CLI unavailable; receipt/store/diagnostic checks unbound")
def test_native_syntax_profile_cli(case):
    """C: installed command, REJECTED/2, safe cause and no committed package."""
    pytest.fail(f"Bind actual CLI and durable-effect assertions for {case['id']} before enabling")
