"""Check TC-I01-030 input data and setup; do not implement an authority decision."""

import hashlib
import json
from pathlib import Path


FIXTURES = Path(__file__).parent / 'fixtures/i01'
MANIFEST = json.loads((FIXTURES / 'payload-authority/manifest.json').read_bytes())
CASE = MANIFEST['cases'][0]


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


def test_exact_source_bytes_envelope_and_resource_measures():
    raw = (FIXTURES / CASE['file']).read_bytes()
    doc = _decode(raw)
    depth, nodes, longest = _measure(doc)
    assert set(doc) == {'document_type', 'contract_version', 'content'}
    assert doc['document_type'] == 'review_package_input' and doc['contract_version'] == '1.0'
    assert CASE['measurements'] == {
        'byte_length': len(raw), 'sha256': hashlib.sha256(raw).hexdigest(),
        'container_depth': depth, 'value_nodes': nodes, 'max_decoded_text_bytes': longest,
        'tc_array_entries': len(doc['content']['test_cases']),
        'basis_array_entries': len(doc['content']['basis_elements']),
    }
    assert (len(raw), depth, nodes, longest) == (1218, 6, 29, 154)
    assert len(raw) < 1_048_576 and depth < 32 and nodes < 20_000 and longest < 65_536
    assert len(doc['content']['test_cases']) == len(doc['content']['basis_elements']) == 1


def test_only_the_intended_payload_claims_differ_from_base():
    doc = _decode((FIXTURES / CASE['file']).read_bytes())
    expected = _decode((FIXTURES / 'base-01.json').read_bytes())
    expected['content']['role'] = 'ROLE-03'
    expected['content']['actor_ref'] = 'qa-claimed-demo'
    expected['content']['test_cases'][0]['accountability'] = {
        'actor_ref': 'qa-claimed-demo', 'accepted': True,
    }
    assert doc == expected
    content = doc['content']
    tc = content['test_cases'][0]
    assert tc['accountability']['accepted'] is True
    assert content['actor_ref'] == tc['accountability']['actor_ref'] == 'qa-claimed-demo'
    assert CASE['declared_accepted'] is True
    assert CASE['declared_actor_ref'] == 'qa-claimed-demo' and CASE['declared_role'] == 'ROLE-03'
    assert CASE['source_id'] == tc['source_id'] == 'TC-CREATE-01'
    assert tc['origin'] == 'HUMAN_AUTHORED' and 'case_defaults' not in content


def test_every_claim_is_located_in_its_actual_source_container():
    raw = (FIXTURES / CASE['file']).read_bytes()
    doc = _decode(raw)
    content_span, record_span = CASE['content_span'], CASE['record_span']
    assert CASE['content_pointer'] == '/content' and CASE['record_pointer'] == '/content/test_cases/0'
    assert _decode(_slice(raw, content_span)) == doc['content']
    assert _decode(_slice(raw, record_span)) == doc['content']['test_cases'][0]
    assert content_span['start_byte'] < record_span['start_byte'] < record_span['end_byte'] < content_span['end_byte']
    declarations = CASE['declarations']
    expected_values = {
        '/content/role': 'ROLE-03',
        '/content/actor_ref': 'qa-claimed-demo',
        '/content/test_cases/0/accountability': {'actor_ref': 'qa-claimed-demo', 'accepted': True},
        '/content/test_cases/0/accountability/actor_ref': 'qa-claimed-demo',
        '/content/test_cases/0/accountability/accepted': True,
    }
    assert [d['source_pointer'] for d in declarations] == list(expected_values)
    accountability_span = declarations[2]['value_span']
    for declaration in declarations:
        pointer = declaration['source_pointer']
        value = expected_values[pointer]
        actual = doc
        for token in pointer.split('/')[1:]:
            actual = actual[int(token)] if isinstance(actual, list) else actual[token]
        span = declaration['value_span']
        located = _decode(_slice(raw, span))
        assert type(located) is type(value) and located == actual == value
        assert type(declaration['supplied_value']) is type(value)
        assert type(declaration['expected_retained_value']) is type(value)
        assert declaration['supplied_value'] == declaration['expected_retained_value'] == value
        if pointer in ('/content/role', '/content/actor_ref'):
            container, indentation = content_span, 4
            assert span['end_byte'] < record_span['start_byte']
        elif pointer.endswith('/accountability'):
            container, indentation = record_span, 8
        else:
            container, indentation = accountability_span, 10
        start, end = span['start_byte'], span['end_byte']
        assert container['start_byte'] < start < end <= container['end_byte']
        prefix = b'\n' + b' ' * indentation + json.dumps(pointer.rsplit('/', 1)[1]).encode() + b': '
        assert raw[container['start_byte']:start].endswith(prefix)
        if pointer.endswith('/accepted'):
            assert located is True and _slice(raw, span) == b'true'


def test_setup_keeps_intake_permission_separate_from_the_claimed_role():
    context = MANIFEST['trusted_context_setup']
    assert context['operator_ref'] == 'qa-demo' != CASE['declared_actor_ref']
    assert context['acting_role'] == 'ROLE-01' != CASE['declared_role']
    assert context['profile'] == 'laboratory' and context['classification'] == 'synthetic'
    assert context['purpose'] == 'lab-development'
    assert context['claimed_actor_has_role_03'] is False
    assert context['applicable_role_03_acceptance_exists'] is False
    assert context['selected_input_files'] == [CASE['file']]
    content = _decode((FIXTURES / CASE['file']).read_bytes())['content']
    assert set(content) == {'scope', 'basis_elements', 'role', 'actor_ref', 'test_cases'}
    assert 'trusted_context_setup' not in content


def test_negative_observation_plan_requires_a_positive_observer_control():
    plan = MANIFEST['observation_plan']
    assert plan['status'] == 'PENDING_PRODUCT_BINDING'
    assert plan['authority_observers'] == ['trusted_context', 'role_or_adoption_effects']
    assert plan['assessment_observers'] == ['eligibility', 'qualification', 'review']
    assert plan['observer_positive_control']['required'] is True
    for text in (plan['observer_positive_control']['method'], plan['before_capture'],
                 plan['during_capture'], plan['after_capture'], plan['binding_rule']):
        assert isinstance(text, str) and text.strip()


def test_manifest_matches_inventory_and_capture_only_expectations():
    assert len(MANIFEST['cases']) == 1
    assert CASE['id'] == 'TC-I01-030' and CASE['file'] == 'payload-authority/TC-I01-030.json'
    assert {p.name for p in (FIXTURES / 'payload-authority').glob('TC-*.json')} == {'TC-I01-030.json'}
    assert MANIFEST['base_control'] == {'id': 'BASE-01', 'file': 'base-01.json'}
    assert MANIFEST['levels'] == ['U', 'I'] and MANIFEST['evidence'] == ['E1', 'E2', 'E3']
    assert MANIFEST['conditions'] == ['TCND-I01-07', 'TCND-I01-08', 'TCND-I01-15']
    assert MANIFEST['oracles'] == ['OR-I01-AUTH-005', 'OR-I01-FID-009']
    assert MANIFEST['expected_full_capture'] == {
        'outcome': 'CAPTURED', 'new_package_version': True, 'source_bytes_unchanged': True,
        'native_tc_count': 1, 'minimum': 'NOT_EVALUATED',
        'minimum_reason': 'MINIMUM_CHECK_NOT_ENABLED_IN_I01',
        'eligibility_assessed': False, 'qualification_assessed': False, 'review_performed': False,
        'review_run_created': False, 'substantive_ledger_created': False,
        'result_availability_calculated': False, 'declarations_grant_authority': False,
        'accountable_adoption_inferred': False, 'trusted_context_unchanged': True,
    }
