"""Check TC-I01-026 files and fixed expectations; do not implement TDG's mapper."""

import hashlib
import json
from pathlib import Path
import re

import pytest


FIXTURES = Path(__file__).parent / 'fixtures/i01'
MANIFEST = json.loads((FIXTURES / 'origin-literals/manifest.json').read_bytes())
CASES = MANIFEST['cases']
ORIGINS = ('HUMAN_AUTHORED', 'HUMAN_CONTROLLED_AI_ASSISTED',
           'WITHOUT_ACCOUNTABLE_ADOPTION', 'OTHER', 'UNKNOWN')
PATTERN = rb'^        "origin": (?P<token>"[A-Z_]+"),\n'


def _unique_members(pairs):
    result = {}
    for key, value in pairs:
        assert key not in result, f'Duplicate JSON member: {key!r}'
        result[key] = value
    return result


def _unexpected_number(token):
    raise AssertionError(f'Unexpected numeric token: {token!r}')


def _decode(raw):
    assert not raw.startswith(b'\xef\xbb\xbf')
    return json.loads(raw.decode('utf-8', errors='strict'), object_pairs_hook=_unique_members,
                      parse_float=_unexpected_number, parse_constant=_unexpected_number)


def _measure(value, parent_depth=0):
    if not isinstance(value, (dict, list)):
        return parent_depth, 1, len(value.encode()) if isinstance(value, str) else 0
    depth, nodes = parent_depth + 1, 1
    text = max((len(k.encode()) for k in value), default=0) if isinstance(value, dict) else 0
    maximum_depth = depth
    for child in value.values() if isinstance(value, dict) else value:
        child_depth, child_nodes, child_text = _measure(child, depth)
        maximum_depth = max(maximum_depth, child_depth)
        nodes += child_nodes
        text = max(text, child_text)
    return maximum_depth, nodes, text


@pytest.mark.parametrize('case', CASES, ids=lambda c: c['id'])
def test_exact_source_bytes_envelope_and_resource_measures(case):
    raw = (FIXTURES / case['file']).read_bytes()
    doc = _decode(raw)
    depth, nodes, text = _measure(doc)
    assert set(doc) == {'document_type', 'contract_version', 'content'}
    assert doc['document_type'] == 'review_package_input' and doc['contract_version'] == '1.0'
    assert case['measurements'] == {
        'byte_length': len(raw), 'sha256': hashlib.sha256(raw).hexdigest(),
        'container_depth': depth, 'value_nodes': nodes, 'max_decoded_text_bytes': text,
        'tc_array_entries': len(doc['content']['test_cases']),
        'basis_array_entries': len(doc['content']['basis_elements']),
    }
    assert len(raw) < 1_048_576 and depth < 32 and nodes < 20_000 and text < 65_536
    assert len(doc['content']['test_cases']) == len(doc['content']['basis_elements']) == 1


@pytest.mark.parametrize('index,case', list(enumerate(CASES)), ids=[c['id'] for c in CASES])
def test_only_origin_changes_and_the_original_value_is_located(index, case):
    raw = (FIXTURES / case['file']).read_bytes()
    base_raw = (FIXTURES / 'base-01.json').read_bytes()
    matches = list(re.finditer(PATTERN, raw, re.MULTILINE))
    base_matches = list(re.finditer(PATTERN, base_raw, re.MULTILINE))
    assert len(matches) == len(base_matches) == 1
    match, base_match = matches[0], base_matches[0]
    assert match.group('token') == json.dumps(ORIGINS[index]).encode('ascii')
    assert raw[:match.start('token')] + raw[match.end('token'):] == base_raw[:base_match.start('token')] + base_raw[base_match.end('token'):]
    assert case['value_span'] == {'start_byte': match.start('token'), 'end_byte': match.end('token')}
    assert case['source_pointer'] == '/content/test_cases/0/origin'
    doc, base = _decode(raw), _decode(base_raw)
    tc = doc['content']['test_cases'][0]
    assert tc['origin'] == ORIGINS[index] == case['supplied_origin'] == case['expected_origin_code']
    assert case['expected_presence'] == 'VALUE' and case['expected_mapping'] == 'MAPPED'
    assert case['expected_accountability_presence'] == 'ABSENT'
    assert 'accountability' not in tc and 'case_defaults' not in doc['content']
    tc['origin'] = base['content']['test_cases'][0]['origin']
    assert doc == base


def test_human_authored_variant_reuses_exact_baseline_bytes():
    assert (FIXTURES / CASES[0]['file']).read_bytes() == (FIXTURES / 'base-01.json').read_bytes()
    assert MANIFEST['control']['identical_variant'] == CASES[0]['id']


def test_unknown_is_a_recognized_literal_and_no_declared_origin_supplies_accountability():
    assert [c['supplied_origin'] for c in CASES] == list(ORIGINS)
    assert len({c['expected_origin_code'] for c in CASES}) == 5
    assert CASES[-1]['expected_origin_code'] == 'UNKNOWN'
    assert CASES[-1]['expected_mapping'] == 'MAPPED'
    # All five sources have the same absent accountability; none is an adoption record.
    for case in CASES:
        tc = _decode((FIXTURES / case['file']).read_bytes())['content']['test_cases'][0]
        assert 'accountability' not in tc
        assert tc['steps'][0]['expected_result'] == 'Registration is accepted.'


def test_manifest_matches_inventory_and_keeps_review_minimum_disabled():
    ids = [f'TC-I01-026.{i:02}' for i in range(1, 6)]
    assert [c['id'] for c in CASES] == ids
    assert [c['file'] for c in CASES] == [f'origin-literals/{i}.json' for i in ids]
    assert {p.name for p in (FIXTURES / 'origin-literals').glob('TC-*.json')} == {i + '.json' for i in ids}
    assert MANIFEST['levels'] == ['U', 'I'] and MANIFEST['evidence'] == ['E1', 'E2']
    assert MANIFEST['oracles'] == ['OR-I01-AUTH-001', 'OR-I01-RCP-004']
    assert MANIFEST['conditions'] == ['TCND-I01-07', 'TCND-I01-15']
    assert MANIFEST['expected_full_capture'] == {
        'outcome': 'CAPTURED', 'new_package_version': True,
        'source_bytes_unchanged': True, 'minimum': 'NOT_EVALUATED',
        'minimum_reason': 'MINIMUM_CHECK_NOT_ENABLED_IN_I01', 'review_performed': False,
        'origin_declaration_grants_authority': False, 'accountability_created_from_origin': False,
    }
