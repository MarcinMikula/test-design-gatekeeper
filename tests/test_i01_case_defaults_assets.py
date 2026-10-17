"""Check TC-I01-028 sources and fixed expectations, without applying defaults."""

import hashlib
import json
from pathlib import Path

import pytest


FIXTURES = Path(__file__).parent / 'fixtures/i01'
MANIFEST = json.loads((FIXTURES / 'case-defaults/manifest.json').read_bytes())
CASES = MANIFEST['cases']
DECLARATIONS = {
    'origin': ('HUMAN_AUTHORED', 'HUMAN_CONTROLLED_AI_ASSISTED'),
    'accountability': (
        {'actor_ref': 'qa-default-demo', 'accepted': True},
        {'actor_ref': 'qa-explicit-demo', 'accepted': True},
    ),
}


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
    assert len(doc['content']['test_cases']) == 2 and len(doc['content']['basis_elements']) == 1


@pytest.mark.parametrize('case', CASES, ids=lambda c: c['id'])
def test_absent_and_explicit_cases_preserve_unrelated_baseline_content(case):
    content = _decode((FIXTURES / case['file']).read_bytes())['content']
    base = _decode((FIXTURES / 'base-01.json').read_bytes())['content']
    field = case['field']
    default, explicit = DECLARATIONS[field]
    assert default != explicit
    assert set(content) == {'scope', 'basis_elements', 'case_defaults', 'test_cases'}
    assert content['scope'] == base['scope']
    assert content['basis_elements'] == base['basis_elements']
    assert content['case_defaults'] == {field: default}
    for index, label in enumerate(('ABSENT', 'EXPLICIT')):
        expected = dict(base['test_cases'][0])
        expected['source_id'] = f'TC-{field.upper()}-{label}'
        if index == 0:
            expected.pop(field, None)
        else:
            expected[field] = explicit
        assert content['test_cases'][index] == expected
    # Structural declarations are valid; accepted=true does not prove human authority.
    if field == 'accountability':
        for declaration in (default, explicit):
            assert set(declaration) == {'actor_ref', 'accepted'}
            assert isinstance(declaration['actor_ref'], str) and declaration['actor_ref']
            assert declaration['accepted'] is True


@pytest.mark.parametrize('case', CASES, ids=lambda c: c['id'])
def test_locations_keep_supplied_presence_separate_from_expected_effective_values(case):
    raw = (FIXTURES / case['file']).read_bytes()
    content = _decode(raw)['content']
    field = case['field']
    default, explicit = DECLARATIONS[field]
    default_pointer = f'/content/case_defaults/{field}'
    defaults_span = case['defaults_object_span']
    assert _decode(_slice(raw, defaults_span)) == content['case_defaults']
    assert case['default']['source_pointer'] == default_pointer
    assert case['default']['supplied_value'] == default
    assert _field_at(raw, case['default']['value_span'], defaults_span, field) == default
    assert case['default_scope_pointer'] == '/content/test_cases'
    expected_items = case['tc_expectations']
    assert len(expected_items) == 2
    assert expected_items[0]['record_span']['end_byte'] < expected_items[1]['record_span']['start_byte']
    for index, item in enumerate(expected_items):
        tc = content['test_cases'][index]
        record_pointer = f'/content/test_cases/{index}'
        assert item['record_pointer'] == record_pointer
        assert item['field_pointer'] == f'{record_pointer}/{field}'
        assert item['source_id'] == tc['source_id']
        assert _decode(_slice(raw, item['record_span'])) == tc
    absent, supplied = expected_items
    assert field not in content['test_cases'][0]
    assert absent['supplied_presence'] == 'ABSENT' and absent['default_applied'] is True
    assert 'supplied_value' not in absent and 'value_span' not in absent
    assert absent['effective_value'] == default
    assert absent['effective_source_pointer'] == default_pointer
    assert supplied['supplied_presence'] == 'VALUE' and supplied['default_applied'] is False
    assert supplied['supplied_value'] == supplied['effective_value'] == explicit
    assert supplied['effective_source_pointer'] == supplied['field_pointer']
    assert _field_at(raw, supplied['value_span'], supplied['record_span'], field) == explicit


def test_manifest_matches_the_inventory_and_capture_boundary():
    ids = ['TC-I01-028.01', 'TC-I01-028.02']
    assert [c['id'] for c in CASES] == ids
    assert [c['field'] for c in CASES] == ['origin', 'accountability']
    assert [c['file'] for c in CASES] == [f'case-defaults/{i}.json' for i in ids]
    assert {p.name for p in (FIXTURES / 'case-defaults').glob('TC-*.json')} == {i + '.json' for i in ids}
    assert MANIFEST['control'] == {'id': 'BASE-01', 'file': 'base-01.json'}
    assert MANIFEST['levels'] == ['U', 'I'] and MANIFEST['evidence'] == ['E1', 'E2']
    assert MANIFEST['conditions'] == ['TCND-I01-07']
    assert MANIFEST['oracles'] == ['OR-I01-AUTH-003', 'OR-I01-AUTH-004']
    assert MANIFEST['expected_full_capture'] == {
        'outcome': 'CAPTURED', 'new_package_version': True, 'source_bytes_unchanged': True,
        'native_tc_count': 2, 'minimum': 'NOT_EVALUATED',
        'minimum_reason': 'MINIMUM_CHECK_NOT_ENABLED_IN_I01', 'review_performed': False,
        'declarations_grant_authority': False, 'accountable_adoption_inferred': False,
    }
