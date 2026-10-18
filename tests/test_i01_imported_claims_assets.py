"""Check TC-I01-032 data and setup without implementing identity or authority rules."""

import hashlib
import json
from pathlib import Path
from uuid import UUID

import pytest


FIXTURES = Path(__file__).parent / 'fixtures/i01'
MANIFEST = json.loads((FIXTURES / 'imported-claims/manifest.json').read_bytes())
CASES = MANIFEST['cases']
SPECS = (
    ('package_id', '11111111-2222-4333-8444-555555555555'),
    ('role', 'ROLE-05'),
    ('approval', 'ACCEPTED'),
    ('status', 'COMPLETED'),
    ('qualification', 'IN_SCOPE'),
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
    assert (depth, nodes, longest) == (6, 25, 154)
    assert len(raw) < 1_048_576 and depth < 32 and nodes < 20_000 and longest < 65_536
    assert len(doc['content']['test_cases']) == len(doc['content']['basis_elements']) == 1


@pytest.mark.parametrize('index,case', list(enumerate(CASES)), ids=[c['id'] for c in CASES])
def test_one_claim_is_added_and_its_exact_source_value_is_located(index, case):
    field, value = SPECS[index]
    raw = (FIXTURES / case['file']).read_bytes()
    doc = _decode(raw)
    expected = _decode((FIXTURES / 'base-01.json').read_bytes())
    expected['content'][field] = value
    assert doc == expected
    assert case['field'] == field and field not in doc
    assert set(doc['content']) & {name for name, _ in SPECS} == {field}
    assert isinstance(doc['content'][field], str)
    assert case['supplied_value'] == case['expected_retained_value'] == value
    assert case['content_pointer'] == '/content' and case['source_pointer'] == f'/content/{field}'
    content_span, value_span = case['content_span'], case['value_span']
    assert _decode(_slice(raw, content_span)) == doc['content']
    assert content_span['start_byte'] < value_span['start_byte'] < value_span['end_byte'] < content_span['end_byte']
    assert raw[content_span['start_byte']:value_span['start_byte']].endswith(b'\n    ' + json.dumps(field).encode() + b': ')
    assert _slice(raw, value_span) == json.dumps(value).encode()
    assert _decode(_slice(raw, value_span)) == value
    assert case['prohibited_promotion'].strip()
    if field == 'package_id':
        assert case['expected_generated_package_identity_differs_from'] == value
    else:
        assert 'expected_generated_package_identity_differs_from' not in case


def test_identity_and_role_setup_cannot_be_satisfied_by_the_source_claims():
    literal = CASES[0]['supplied_value']
    assert str(UUID(literal)) == literal and UUID(literal).version == 4
    setup = MANIFEST['operation_setup']
    assert setup['operator_ref'] == 'qa-demo' and setup['acting_role'] == 'ROLE-01'
    assert setup['acting_role'] != CASES[1]['supplied_value'] == 'ROLE-05'
    assert setup['operator_has_claimed_role_05'] is False and setup['predecessor_selected'] is False
    assert setup['profile'] == 'laboratory' and setup['classification'] == 'synthetic'
    assert setup['purpose'] == 'lab-development'
    assert MANIFEST['prior_store_setup']['supplied_package_uuid_absent'] is True
    assert MANIFEST['prior_store_setup']['method'].strip() and MANIFEST['prior_store_setup']['check'].strip()
    for case in CASES:
        content = _decode((FIXTURES / case['file']).read_bytes())['content']
        assert 'operation_setup' not in content and 'prior_store_setup' not in content


def test_observation_plan_requires_real_effects_and_a_positive_control():
    plan = MANIFEST['observation_plan']
    assert plan['status'] == 'PENDING_PRODUCT_BINDING'
    assert plan['e3_boundaries'] == ['generated_identity', 'trusted_context_and_policy',
                                    'role_or_approval_effects', 'qualification_or_review_activity',
                                    'history_restoration']
    assert plan['observer_positive_control']['required'] is True
    assert plan['observer_positive_control']['method'].strip()
    for key in ('during_capture', 'after_capture', 'source_vs_authority_check',
                'unavailable_capability_check', 'binding_rule'):
        assert isinstance(plan[key], str) and plan[key].strip()


def test_manifest_matches_inventory_and_capture_without_trusted_promotion():
    ids = [f'TC-I01-032.{n:02}' for n in range(1, 6)]
    assert [c['id'] for c in CASES] == ids
    assert [c['file'] for c in CASES] == [f'imported-claims/{name}.json' for name in ids]
    assert {p.name for p in (FIXTURES / 'imported-claims').glob('TC-*.json')} == {name + '.json' for name in ids}
    assert MANIFEST['base_control'] == {'id': 'BASE-01', 'file': 'base-01.json'}
    assert MANIFEST['levels'] == ['U', 'I'] and MANIFEST['evidence'] == ['E1', 'E2', 'E3']
    assert MANIFEST['conditions'] == ['TCND-I01-08', 'TCND-I01-15']
    assert MANIFEST['oracles'] == ['OR-I01-FID-009']
    assert MANIFEST['expected_full_capture'] == {
        'outcome': 'CAPTURED', 'new_package_version': True, 'new_lineage': True,
        'source_bytes_unchanged': True, 'native_tc_count': 1, 'selected_source_count': 1,
        'minimum': 'NOT_EVALUATED', 'minimum_reason': 'MINIMUM_CHECK_NOT_ENABLED_IN_I01',
        'review_performed': False,
    }
    assert MANIFEST['expected_separation'] == {
        'trusted_context_unchanged': True, 'policy_unchanged': True,
        'supplied_identity_restored': False, 'role_granted': False,
        'human_approval_or_disposition_created': False, 'trusted_history_restored': False,
        'eligibility_assessed': False, 'domain_qualification_assessed': False,
        'model_or_configuration_qualified': False,
        'review_run_created_or_restored': False, 'substantive_ledger_created': False,
        'result_availability_calculated': False, 'prior_immutable_records_unchanged': True,
    }
