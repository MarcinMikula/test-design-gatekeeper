"""Validate synthetic input witnesses, not TDG fidelity or capture behavior."""
import copy
import hashlib
import json
from pathlib import Path
import unicodedata

import pytest

F = Path(__file__).parent / 'fixtures/i01'
M = json.loads((F / 'source-id-fidelity/manifest.json').read_bytes())
CASES = M['cases']
PAIRS = [('001', '1'), ('TC-A', 'tc-a'), (' TC-A\t', 'TC-A'), ('TC-\u00e9', 'TC-e\u0301')]


def unique(pairs):
    result = {}
    for k, v in pairs:
        assert k not in result
        result[k] = v
    return result


def measure(v, depth=0):
    if isinstance(v, (dict, list)):
        children = list(v.values()) if isinstance(v, dict) else v
        values = [measure(c, depth + 1) for c in children]
        keys = [len(k.encode()) for k in v] if isinstance(v, dict) else []
        return (max([depth + 1] + [x[0] for x in values]),
                1 + sum(x[1] for x in values), max([0] + keys + [x[2] for x in values]))
    return depth, 1, len(v.encode()) if isinstance(v, str) else 0


@pytest.mark.parametrize('case', CASES, ids=lambda c: c['id'])
def test_exact_bytes_valid_json_and_resource_bounds(case):
    raw = (F / case['file']).read_bytes()
    assert not raw.startswith(b'\xef\xbb\xbf')
    doc = json.loads(raw.decode('utf-8'), object_pairs_hook=unique)
    assert len(raw) == case['byte_length'] and hashlib.sha256(raw).hexdigest() == case['sha256']
    assert measure(doc) == (6, 37, 154)
    assert len(raw) < 1_048_576
    assert len(doc['content']['test_cases']) == 2
    assert len(doc['content']['basis_elements']) == 1


@pytest.mark.parametrize('index,case', list(enumerate(CASES)), ids=[c['id'] for c in CASES])
def test_only_two_source_ids_differ_from_duplicated_baseline(index, case):
    doc = json.loads((F / case['file']).read_bytes())
    base = json.loads((F / 'base-01.json').read_bytes())
    expected = copy.deepcopy(base)
    expected['content']['test_cases'] *= 2
    expected['content']['test_cases'] = [dict(tc, source_id=s)
                                       for tc, s in zip(expected['content']['test_cases'], PAIRS[index])]
    assert doc == expected
    assert case['source_ids'] == list(PAIRS[index])
    assert case['code_points'] == [[ord(c) for c in s] for s in PAIRS[index]]
    assert case['source_pointers'] == ['/content/test_cases/0/source_id', '/content/test_cases/1/source_id']


@pytest.mark.parametrize('index,case', list(enumerate(CASES)), ids=[c['id'] for c in CASES])
def test_lossy_transform_witness_would_conflate_distinct_supplied_strings(index, case):
    ids = [tc['source_id'] for tc in json.loads((F / case['file']).read_bytes())['content']['test_cases']]
    transform = [int, str.casefold, str.strip, lambda s: unicodedata.normalize('NFC', s)][index]
    assert all(isinstance(s, str) for s in ids)
    assert ids[0] != ids[1] and ids[0].encode() != ids[1].encode()
    assert transform(ids[0]) == transform(ids[1])
    assert len(set(ids)) == 2 and len({transform(s) for s in ids}) == 1


def test_manifest_inventory_and_oracle_boundary():
    assert [c['id'] for c in CASES] == [f'TC-I01-024.{n:02}' for n in range(1, 5)]
    assert {p.name for p in (F / 'source-id-fidelity').glob('TC-*.json')} == {c['id'] + '.json' for c in CASES}
    assert M['oracles'] == ['OR-I01-FID-003']
    assert M['levels'] == ['U', 'I'] and M['evidence'] == ['E1', 'E2']
    assert M['expected_full_capture']['outcome'] == 'CAPTURED'
    assert M['expected_full_capture']['minimum'] == 'NOT_EVALUATED'
