"""Check TC-I01-031 source data without following references or executing text."""

import hashlib
import json
from pathlib import Path, PureWindowsPath
from urllib.parse import urlsplit

import pytest


FIXTURES = Path(__file__).parent / 'fixtures/i01'
MANIFEST = json.loads((FIXTURES / 'inert-content/manifest.json').read_bytes())
CASES = MANIFEST['cases']
SPECS = (
    ('url', 'url', 'https://tdg.invalid/TC031-URL-MARKER', 'TC031-URL-MARKER'),
    ('local_path', 'path', r'C:\TDG-Synthetic\TC031-PATH-MARKER.txt', 'TC031-PATH-MARKER'),
    ('schema_reference', '$ref', 'https://tdg.invalid/TC031-REF-MARKER.schema.json', 'TC031-REF-MARKER'),
    ('issue_key', 'issue_key', 'TDG031-404', 'TDG031-404'),
    ('instruction', 'instruction', 'cmd.exe /c echo TC031-EXEC-MARKER', 'TC031-EXEC-MARKER'),
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
    assert (depth, nodes, longest) == (6, 26, 154)
    assert len(raw) < 1_048_576 and depth < 32 and nodes < 20_000 and longest < 65_536
    assert len(doc['content']['test_cases']) == len(doc['content']['basis_elements']) == 1


@pytest.mark.parametrize('index,case', list(enumerate(CASES)), ids=[c['id'] for c in CASES])
def test_only_the_intended_string_is_added_and_its_exact_location_is_recorded(index, case):
    kind, field, value, marker = SPECS[index]
    raw = (FIXTURES / case['file']).read_bytes()
    doc = _decode(raw)
    expected = _decode((FIXTURES / 'base-01.json').read_bytes())
    expected['content']['supplementary_content'] = {field: value}
    assert doc == expected
    assert case['kind'] == kind and case['field'] == field
    assert case['supplied_value'] == case['expected_retained_value'] == value
    assert case['leakage_marker'] == marker and raw.count(marker.encode()) == 1
    assert case['content_pointer'] == '/content'
    assert case['container_pointer'] == '/content/supplementary_content'
    assert case['source_pointer'] == f'/content/supplementary_content/{field}'
    content_span, container_span, value_span = case['content_span'], case['container_span'], case['value_span']
    assert _decode(_slice(raw, content_span)) == doc['content']
    assert _decode(_slice(raw, container_span)) == {field: value}
    assert content_span['start_byte'] < container_span['start_byte'] < container_span['end_byte'] < content_span['end_byte']
    assert raw[content_span['start_byte']:container_span['start_byte']].endswith(b'\n    "supplementary_content": ')
    assert container_span['start_byte'] < value_span['start_byte'] < value_span['end_byte'] < container_span['end_byte']
    assert raw[container_span['start_byte']:value_span['start_byte']].endswith(b'\n      ' + json.dumps(field).encode() + b': ')
    assert _slice(raw, value_span) == json.dumps(value).encode()
    assert _decode(_slice(raw, value_span)) == value
    assert case['expected_inventory'] == {'selected_source_count': 1, 'extra_source_count': 0}


def test_stimulus_forms_and_markers_are_distinct_synthetic_strings():
    markers = [c['leakage_marker'] for c in CASES]
    assert len(set(markers)) == len(CASES) == 5
    base_raw = (FIXTURES / 'base-01.json').read_bytes()
    for case in CASES:
        raw = (FIXTURES / case['file']).read_bytes()
        assert isinstance(case['supplied_value'], str)
        assert case['leakage_marker'].encode() not in base_raw
        assert all(m == case['leakage_marker'] or m.encode() not in raw for m in markers)
    for index in (0, 2):
        parsed = urlsplit(CASES[index]['supplied_value'])
        assert parsed.scheme == 'https' and parsed.hostname == 'tdg.invalid'
        assert parsed.username is None and parsed.password is None
    path = PureWindowsPath(CASES[1]['supplied_value'])
    assert path.is_absolute() and path.drive == 'C:' and '..' not in path.parts
    assert CASES[2]['field'] == '$ref'
    assert CASES[3]['supplied_value'] == 'TDG031-404'
    assert CASES[4]['supplied_value'] == 'cmd.exe /c echo TC031-EXEC-MARKER'


def test_observation_plan_covers_attempts_and_routine_diagnostics():
    observers = ['supplied_reference_file_open', 'supplied_reference_resolution',
                 'remote_schema_resolution', 'network', 'payload_code_or_shell_execution']
    plan = MANIFEST['observation_plan']
    assert plan['status'] == 'PENDING_PRODUCT_BINDING'
    assert plan['e3_observers'] == observers
    assert MANIFEST['expected_forbidden_attempts'] == dict.fromkeys(observers, 0)
    assert plan['e4_sinks'] == ['routine_stdout', 'routine_stderr', 'routine_logs']
    assert plan['expected_routine_marker_occurrences'] == 0
    assert plan['observer_positive_control']['required'] is True
    for key in ('attempt_boundary', 'allowed_baseline', 'during_capture', 'after_capture',
                'diagnostic_checks', 'binding_rule'):
        assert isinstance(plan[key], str) and plan[key].strip()
    assert plan['observer_positive_control']['method'].strip()


def test_manifest_matches_inventory_and_single_source_capture_expectations():
    ids = [f'TC-I01-031.{n:02}' for n in range(1, 6)]
    assert [c['id'] for c in CASES] == ids
    assert [c['file'] for c in CASES] == [f'inert-content/{name}.json' for name in ids]
    assert {p.name for p in (FIXTURES / 'inert-content').glob('TC-*.json')} == {name + '.json' for name in ids}
    assert MANIFEST['base_control'] == {'id': 'BASE-01', 'file': 'base-01.json'}
    assert MANIFEST['levels'] == ['U', 'I'] and MANIFEST['evidence'] == ['E1', 'E3', 'E4']
    assert MANIFEST['conditions'] == ['TCND-I01-08', 'TCND-I01-16']
    assert MANIFEST['oracles'] == ['OR-I01-FID-008']
    setup = MANIFEST['operation_setup']
    assert setup['operator_ref'] == 'qa-demo' and setup['profile'] == 'laboratory'
    assert setup['classification'] == 'synthetic' and setup['purpose'] == 'lab-development'
    assert setup['references_are_selected_inputs'] is False
    assert MANIFEST['expected_full_capture'] == {
        'outcome': 'CAPTURED', 'new_package_version': True, 'source_bytes_unchanged': True,
        'native_tc_count': 1, 'selected_source_count': 1, 'minimum': 'NOT_EVALUATED',
        'minimum_reason': 'MINIMUM_CHECK_NOT_ENABLED_IN_I01', 'review_performed': False,
        'references_become_substantive_evidence': False, 'schema_selection_unchanged': True,
    }
