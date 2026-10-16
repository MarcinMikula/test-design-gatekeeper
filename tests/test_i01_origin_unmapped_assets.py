"""Check the TC-I01-027 data and expectations; do not implement TDG's mapper."""

import hashlib
import json
from pathlib import Path
import re

import pytest


FIXTURES = Path(__file__).parent / 'fixtures/i01'
MANIFEST = json.loads((FIXTURES / 'origin-unmapped/manifest.json').read_bytes())
CASES = MANIFEST['cases']
VALUES = ('written by QA engineer', 'human_authored')
ORIGIN_LINE = rb'^        "origin": (?P<token>"[A-Za-z_ ]+"),\n'


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


@pytest.mark.parametrize('case', CASES, ids=lambda c: c['id'])
def test_exact_bytes_envelope_and_resource_measures(case):
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
def test_only_origin_changes_and_its_source_location_is_exact(index, case):
    raw = (FIXTURES / case['file']).read_bytes()
    base_raw = (FIXTURES / 'base-01.json').read_bytes()
    matches = list(re.finditer(ORIGIN_LINE, raw, re.MULTILINE))
    controls = list(re.finditer(ORIGIN_LINE, base_raw, re.MULTILINE))
    assert len(matches) == len(controls) == 1
    match, control = matches[0], controls[0]
    assert match.group('token') == json.dumps(VALUES[index]).encode('ascii')
    assert control.group('token') == b'"HUMAN_AUTHORED"'
    assert raw[:match.start('token')] == base_raw[:control.start('token')]
    assert raw[match.end('token'):] == base_raw[control.end('token'):]
    assert case['value_span'] == {'start_byte': match.start('token'), 'end_byte': match.end('token')}
    assert case['source_pointer'] == '/content/test_cases/0/origin'
    doc, base = _decode(raw), _decode(base_raw)
    tc = doc['content']['test_cases'][0]
    assert tc['origin'] == VALUES[index] == case['supplied_origin']
    assert case['expected_presence'] == 'VALUE' and case['expected_mapping'] == 'UNMAPPED'
    assert case['expected_origin_code'] is None
    assert case['expected_accountability_presence'] == 'ABSENT'
    assert 'accountability' not in tc and 'case_defaults' not in doc['content']
    tc['origin'] = base['content']['test_cases'][0]['origin']
    assert doc == base


def test_lowercase_counterexample_and_uppercase_control_remain_distinct():
    base = _decode((FIXTURES / 'base-01.json').read_bytes())
    canonical = base['content']['test_cases'][0]['origin']
    supplied = [_decode((FIXTURES / c['file']).read_bytes())['content']['test_cases'][0]['origin']
                for c in CASES]
    assert supplied == list(VALUES)
    assert canonical == 'HUMAN_AUTHORED'
    assert supplied[1] != canonical and supplied[1].upper() == canonical
    assert supplied[0] != canonical and 'QA engineer' in supplied[0]
    # These checks describe the inputs. No mapping is performed here.
    assert MANIFEST['control'] == {
        'id': 'BASE-01', 'file': 'base-01.json',
        'source_pointer': '/content/test_cases/0/origin',
        'supplied_origin': 'HUMAN_AUTHORED', 'expected_mapping': 'MAPPED',
        'expected_origin_code': 'HUMAN_AUTHORED',
    }


def test_manifest_keeps_the_inventory_scope_and_mapping_precondition():
    ids = [f'TC-I01-027.{i:02}' for i in range(1, 3)]
    assert [c['id'] for c in CASES] == ids
    assert [c['file'] for c in CASES] == [f'origin-unmapped/{i}.json' for i in ids]
    assert {p.name for p in (FIXTURES / 'origin-unmapped').glob('TC-*.json')} == {i + '.json' for i in ids}
    assert MANIFEST['levels'] == ['U'] and MANIFEST['evidence'] == ['E1', 'E2']
    assert MANIFEST['oracles'] == ['OR-I01-AUTH-002']
    assert MANIFEST['conditions'] == ['TCND-I01-07']
    assert MANIFEST['mapping_precondition']['required_control_mapping'] == {
        'source': 'HUMAN_AUTHORED', 'code': 'HUMAN_AUTHORED',
    }
    assert MANIFEST['mapping_precondition']['unmapped_source_values'] == list(VALUES)
    assert MANIFEST['expected_component'] == {
        'original_text_preserved': True, 'source_location_preserved': True,
        'authorship_inferred': False, 'ai_involvement_inferred': False,
        'accountable_adoption_inferred': False, 'origin_declaration_grants_authority': False,
    }
