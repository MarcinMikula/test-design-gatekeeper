"""U/I skeletons for TC-I01-019–020; no product assertions are bound yet.

See docs/implementation/i01-w02c-numeric-retention-fixtures.md for the source,
projection and store observation requirements. Asset checks are not evidence
that the current TDG build captures or preserves these values.
"""

import json
from pathlib import Path

import pytest


_MANIFEST = Path(__file__).parent / "fixtures/i01/numeric-retention/manifest.json"
CASES = json.loads(_MANIFEST.read_bytes())["cases"]


@pytest.mark.parametrize("case", CASES, ids=lambda c: c["id"])
@pytest.mark.skip(reason="W02-C: numeric/text projection and source-locator observations unbound")
def test_numeric_text_retention_component(case):
    """U: exact located lexemes, supported/limited projection, no coercion."""
    pytest.fail(f"Bind actual projection/source assertions for {case['id']} before enabling")


@pytest.mark.parametrize("case", CASES, ids=lambda c: c["id"])
@pytest.mark.skip(reason="W02-C: capture service, containment and independent store checks unbound")
def test_numeric_text_retention_capture(case):
    """I: inspect original, projection, source reference and receipt after commit/reopen."""
    pytest.fail(f"Bind actual capture/store assertions for {case['id']} before enabling")
