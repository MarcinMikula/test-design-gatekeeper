"""Check TC-I01-025 input files; these tests do not run TDG's importer."""

import copy
import hashlib
import json
from pathlib import Path

import pytest


FIXTURES = Path(__file__).parent / 'fixtures/i01'
MANIFEST = json.loads((FIXTURES / 'deficient-content/manifest.json').read_bytes())
CASES = MANIFEST['cases']
EXTENSION = {'details': {'marker': 'KEEP-NESTED-025', 'values': [0, False, None, '']}}
POINTERS = ['/content/vendor_extension', '/content/test_cases', '/content/test_cases/0']


def _unique_members(pairs):
    result = {}
    for key, value in pairs:
        assert key not in result, f'Duplicate JSON member: {key!r}'
        result[key] = value
    return result


def _reject_non_integer(token):
    raise AssertionError(f'Unexpected numeric syntax in fixture: {token!r}')


def _decode(raw):
    assert not raw.startswith(b'\xef\xbb\xbf')
    numeric_tokens = []

    def integer(token):
        numeric_tokens.append(token)
        assert len(token) <= 128
        return int(token)

    result = json.loads(raw.decode('utf-8', errors='strict'),
                        object_pairs_hook=_unique_members, parse_int=integer,
                        parse_float=_reject_non_integer, parse_constant=_reject_non_integer)
    assert all(token in ('0', '30') for token in numeric_tokens)
    return result


def _measure(value, parent_depth=0):
    if not isinstance(value, (dict, list)):
        return parent_depth, 1, len(value.encode('utf-8')) if isinstance(value, str) else 0
    depth = parent_depth + 1
    nodes = 1
    text = max((len(key.encode('utf-8')) for key in value), default=0) if isinstance(value, dict) else 0
    children = value.values() if isinstance(value, dict) else value
    maximum_depth = depth
    for child in children:
        child_depth, child_nodes, child_text = _measure(child, depth)
        maximum_depth = max(maximum_depth, child_depth)
        nodes += child_nodes
        text = max(text, child_text)
    return maximum_depth, nodes, text


def _document(case):
    return _decode((FIXTURES / case['file']).read_bytes())


@pytest.mark.parametrize('case', CASES, ids=lambda c: c['id'])
def test_exact_bytes_valid_envelope_and_resource_bounds(case):
    raw = (FIXTURES / case['file']).read_bytes()
    doc = _decode(raw)
    depth, nodes, text = _measure(doc)
    tc = doc['content']['test_cases']
    assert set(doc) == {'document_type', 'contract_version', 'content'}
    assert doc['document_type'] == 'review_package_input' and doc['contract_version'] == '1.0'
    assert type(doc['content']) is dict
    assert case['measurements'] == {
        'byte_length': len(raw), 'sha256': hashlib.sha256(raw).hexdigest(),
        'container_depth': depth, 'value_nodes': nodes, 'max_decoded_text_bytes': text,
        'tc_array_entries': len(tc) if isinstance(tc, list) else None,
        'basis_array_entries': len(doc['content']['basis_elements']),
    }
    assert len(raw) < 1_048_576 and depth < 32 and nodes < 20_000 and text < 65_536
    assert len(doc['content']['basis_elements']) == 1
    assert not isinstance(tc, list) or len(tc) == 1


@pytest.mark.parametrize('index,case', list(enumerate(CASES)), ids=[c['id'] for c in CASES])
def test_each_input_changes_only_the_planned_content(index, case):
    base_raw = (FIXTURES / 'base-01.json').read_bytes()
    base = _decode(base_raw)
    expected = copy.deepcopy(base)
    if index == 0:
        expected['content']['vendor_extension'] = EXTENSION
    elif index == 1:
        expected['content']['test_cases'] = expected['content']['test_cases'][0]
    else:
        expected['content']['test_cases'] = [{'title': base['content']['test_cases'][0]['title']}]
    doc = _document(case)
    # Compare serialized types too: Python alone considers 0 equal to False.
    assert json.dumps(doc, sort_keys=True) == json.dumps(expected, sort_keys=True)
    restored = copy.deepcopy(doc)
    if index == 0:
        del restored['content']['vendor_extension']
    elif index == 1:
        restored['content']['test_cases'] = [restored['content']['test_cases']]
    else:
        restored['content']['test_cases'][0] = copy.deepcopy(base['content']['test_cases'][0])
    assert restored == base
    assert (json.dumps(restored, indent=2) + '\n').encode() == base_raw


@pytest.mark.parametrize('index,case', list(enumerate(CASES)), ids=[c['id'] for c in CASES])
def test_manifest_locates_the_supplied_value_in_the_original_bytes(index, case):
    raw = (FIXTURES / case['file']).read_bytes()
    doc = _decode(raw)
    pointer = POINTERS[index]
    assert case['source_pointer'] == pointer
    value = doc
    for part in pointer.strip('/').split('/'):
        value = value[int(part)] if isinstance(value, list) else value[part]
    span = case['value_span']
    start, end = span['start_byte'], span['end_byte']
    assert 0 <= start < end < len(raw)
    prefix = [b'    "vendor_extension": ', b'    "test_cases": ', b'    "test_cases": [\n      '][index]
    assert raw.count(prefix) == 1 and start == raw.index(prefix) + len(prefix)
    assert raw[start:end].startswith(b'{') and raw[start:end].endswith(b'}')
    decoded = _decode(raw[start:end])
    assert json.dumps(decoded, sort_keys=True) == json.dumps(value, sort_keys=True)
    assert json.dumps(value, sort_keys=True) == json.dumps(case['source_value'], sort_keys=True)


def test_unknown_nested_content_has_distinguishable_falsy_values_and_marker():
    details = _document(CASES[0])['content']['vendor_extension']['details']
    assert details['marker'] == 'KEEP-NESTED-025'
    assert [type(v) for v in details['values']] == [int, bool, type(None), str]
    assert details['values'] == [0, False, None, '']
    assert all(not v for v in details['values'])
    assert [v for v in details['values'] if v] == []  # Dropping falsy values loses four supplied entries.
    assert CASES[0]['expected_component']['mapping_state'] == 'UNMAPPED'


def test_malformed_member_is_an_object_not_an_empty_or_singleton_array():
    tc = _document(CASES[1])['content']['test_cases']
    assert type(tc) is dict and tc
    assert tc == _decode((FIXTURES / 'base-01.json').read_bytes())['content']['test_cases'][0]
    assert json.dumps(tc) != json.dumps([tc]) and json.dumps(tc) != '[]'
    assert CASES[1]['measurements']['tc_array_entries'] is None
    assert CASES[1]['expected_component']['presence_state'] == 'TYPE_MISMATCH'


def test_title_only_case_has_absent_fields_rather_than_null_or_filled_values():
    case = CASES[2]
    item = _document(case)['content']['test_cases'][0]
    assert item == {'title': 'Register a customer aged 30'}
    absent = ['source_id', 'preconditions', 'steps', 'test_data', 'origin', 'basis_refs']
    assert case['absent_fields'] == absent
    assert case['absent_field_evidence_pointer'] == '/content/test_cases/0'
    assert all(key not in item for key in absent)
    assert item != {**item, 'steps': None}
    assert item != {**item, 'steps': []}
    assert 'expected_result' not in item


def test_manifest_keeps_three_variants_and_the_i01_capture_boundary():
    ids = [f'TC-I01-025.{n:02}' for n in range(1, 4)]
    assert [c['id'] for c in CASES] == ids
    assert [c['file'] for c in CASES] == [f'deficient-content/{i}.json' for i in ids]
    assert {p.name for p in (FIXTURES / 'deficient-content').glob('TC-*.json')} == {i + '.json' for i in ids}
    assert MANIFEST['oracles'] == ['OR-I01-FID-004', 'OR-I01-ENV-007']
    assert MANIFEST['conditions'] == ['TCND-I01-06', 'TCND-I01-15']
    assert MANIFEST['levels'] == ['U', 'I'] and MANIFEST['evidence'] == ['E1', 'E2']
    assert MANIFEST['expected_full_capture'] == {
        'outcome': 'CAPTURED', 'new_package_version': True,
        'source_bytes_unchanged': True, 'source_deficiencies_visible': True,
        'minimum': 'NOT_EVALUATED', 'minimum_reason': 'MINIMUM_CHECK_NOT_ENABLED_IN_I01',
        'review_performed': False,
    }
    assert all(c['expected_component']['retain_raw_value_and_source_location']
               and c['expected_component']['visible_issue_or_limitation']
               and c['expected_component']['no_content_repair'] for c in CASES)
