"""Check TC-I01-029 data; do not implement defaulting or human-accountability rules."""

from copy import deepcopy
import hashlib
import json
from pathlib import Path

import pytest


FIXTURES = Path(__file__).parent / 'fixtures/i01'
MANIFEST = json.loads((FIXTURES / 'default-preservation/manifest.json').read_bytes())
CASES = MANIFEST['cases']
DEFAULT_ACCOUNTABILITY = {'actor_ref': 'qa-default-demo', 'accepted': True}
SPECS = (
    ('origin', None, 'NULL'),
    ('origin', '', 'EMPTY'),
    ('origin', 'UNKNOWN', 'VALUE'),
    ('origin', [], 'TYPE_MISMATCH'),
    ('origin', 'written by QA engineer', 'VALUE'),
    ('accountability', {'actor_ref': 'qa-default-demo', 'accepted': False}, 'VALUE'),
)


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
    longest = max((len(k.encode()) for k in value), default=0) if isinstance(value, dict) else 0
    maximum_depth = depth
    for child in value.values() if isinstance(value, dict) else value:
        child_depth, child_nodes, child_text = _measure(child, depth)
        maximum_depth = max(maximum_depth, child_depth)
        nodes += child_nodes
        longest = max(longest, child_text)
    return maximum_depth, nodes, longest


def _slice(raw, span):
    start, end = span['start_byte'], span['end_byte']
    assert 0 <= start < end <= len(raw)
    return raw[start:end]


def _field_at(raw, span, container_span, field):
    start, end = span['start_byte'], span['end_byte']
    assert container_span['start_byte'] < start < end <= container_span['end_byte']
    assert raw[container_span['start_byte']:start].endswith(json.dumps(field).encode() + b': ')
    return _decode(_slice(raw, span))


@pytest.mark.parametrize('case', CASES, ids=lambda c: c['id'])
def test_exact_source_bytes_envelope_and_resource_measures(case):
    raw = (FIXTURES / case['file']).read_bytes()
    doc = _decode(raw)
    depth, nodes, longest = _measure(doc)
    assert set(doc) == {'document_type', 'contract_version', 'content'}
    assert doc['document_type'] == 'review_package_input' and doc['contract_version'] == '1.0'
    assert case['measurements'] == {
        'byte_length': len(raw), 'sha256': hashlib.sha256(raw).hexdigest(),
        'container_depth': depth, 'value_nodes': nodes, 'max_decoded_text_bytes': longest,
        'tc_array_entries': len(doc['content']['test_cases']),
        'basis_array_entries': len(doc['content']['basis_elements']),
    }
    assert len(raw) < 1_048_576 and depth < 32 and nodes < 20_000 and longest < 65_536
    assert len(doc['content']['test_cases']) == len(doc['content']['basis_elements']) == 1


@pytest.mark.parametrize('index,case', list(enumerate(CASES)), ids=[c['id'] for c in CASES])
def test_explicit_source_values_locations_and_fixed_no_default_expectations(index, case):
    field, supplied, presence = SPECS[index]
    default = 'HUMAN_AUTHORED' if field == 'origin' else DEFAULT_ACCOUNTABILITY
    raw = (FIXTURES / case['file']).read_bytes()
    doc = _decode(raw)
    expected = _decode((FIXTURES / 'base-01.json').read_bytes())
    expected['content']['case_defaults'] = {field: deepcopy(default)}
    expected['content']['test_cases'][0][field] = deepcopy(supplied)
    assert doc == expected
    tc = doc['content']['test_cases'][0]
    assert field in tc and type(tc[field]) is type(supplied)
    assert tc[field] == supplied and supplied != default
    assert case['field'] == field and case['supplied_value'] == supplied
    assert case['expected_retained_value'] == supplied
    assert case['expected_presence'] == presence and case['expected_default_applied'] is False
    assert case['default_scope_pointer'] == '/content/test_cases'
    assert case['default']['source_pointer'] == f'/content/case_defaults/{field}'
    assert case['default']['supplied_value'] == default
    defaults_span = case['defaults_object_span']
    assert _decode(_slice(raw, defaults_span)) == doc['content']['case_defaults']
    assert _field_at(raw, case['default']['value_span'], defaults_span, field) == default
    assert case['record_pointer'] == '/content/test_cases/0'
    assert _decode(_slice(raw, case['record_span'])) == tc
    assert case['source_pointer'] == f'/content/test_cases/0/{field}'
    located = _field_at(raw, case['value_span'], case['record_span'], field)
    assert type(located) is type(supplied) and located == supplied
    if field == 'origin':
        assert 'accountability' not in tc
        resolution = {'canonical_code_established': False}
        if index == 2:
            resolution = {'canonical_code_established': True, 'code': 'UNKNOWN'}
        elif index == 4:
            resolution['unmapped_text'] = True
        assert case['expected_origin_resolution'] == resolution
        if index == 0:
            assert _slice(raw, case['value_span']) == b'null'
        elif index == 1:
            assert _slice(raw, case['value_span']) == b'""'
        elif index == 3:
            assert _slice(raw, case['value_span']) == b'[]'
    else:
        assert tc['origin'] == 'HUMAN_AUTHORED'
        assert tc[field]['actor_ref'] == default['actor_ref'] == 'qa-default-demo'
        assert doc['content']['case_defaults'][field]['accepted'] is True
        assert tc[field]['accepted'] is False and case['expected_accepted'] is False
        assert case['accepted_pointer'] == '/content/test_cases/0/accountability/accepted'
        assert _field_at(raw, case['accepted_span'], case['value_span'], 'accepted') is False
        assert _slice(raw, case['accepted_span']) == b'false'


def test_existing_absent_field_controls_have_the_same_positive_defaults():
    assert MANIFEST['base_control'] == {'id': 'BASE-01', 'file': 'base-01.json'}
    assert MANIFEST['default_controls'] == [
        {'id': 'TC-I01-028.01', 'file': 'case-defaults/TC-I01-028.01.json',
         'field': 'origin', 'absent_case_pointer': '/content/test_cases/0'},
        {'id': 'TC-I01-028.02', 'file': 'case-defaults/TC-I01-028.02.json',
         'field': 'accountability', 'absent_case_pointer': '/content/test_cases/0'},
    ]
    for control in MANIFEST['default_controls']:
        content = _decode((FIXTURES / control['file']).read_bytes())['content']
        field = control['field']
        assert field not in content['test_cases'][0]
        default = 'HUMAN_AUTHORED' if field == 'origin' else DEFAULT_ACCOUNTABILITY
        assert content['case_defaults'][field] == default
        assert all(c['default']['supplied_value'] == default for c in CASES if c['field'] == field)


def test_manifest_matches_inventory_without_inventing_review_or_authority():
    ids = [f'TC-I01-029.{i:02}' for i in range(1, 7)]
    assert [c['id'] for c in CASES] == ids
    assert [c['file'] for c in CASES] == [f'default-preservation/{i}.json' for i in ids]
    assert {p.name for p in (FIXTURES / 'default-preservation').glob('TC-*.json')} == {i + '.json' for i in ids}
    assert MANIFEST['levels'] == ['U', 'I'] and MANIFEST['evidence'] == ['E1', 'E2']
    assert MANIFEST['conditions'] == ['TCND-I01-07']
    assert MANIFEST['oracles'] == ['OR-I01-AUTH-004', 'OR-I01-AUTH-005']
    assert MANIFEST['expected_full_capture'] == {
        'outcome': 'CAPTURED', 'new_package_version': True, 'source_bytes_unchanged': True,
        'native_tc_count': 1, 'minimum': 'NOT_EVALUATED',
        'minimum_reason': 'MINIMUM_CHECK_NOT_ENABLED_IN_I01', 'review_performed': False,
        'declarations_grant_authority': False, 'accountable_adoption_inferred': False,
    }
