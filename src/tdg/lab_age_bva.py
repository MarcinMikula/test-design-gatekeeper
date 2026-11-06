"""Compare declared age inputs with one operator-confirmed integer interval."""

from decimal import Decimal, InvalidOperation
import hashlib
import json

from tdg.capabilities import CONTRACT_VERSION


MAX_LAB_PACKAGE_BYTES = 64 * 1024


class LabInputError(ValueError):
    """An input rejection with a diagnostic safe to display."""


def lab_integer(token: str) -> int:
    if len(token) > 128:
        raise ValueError("Numeric token exceeds the laboratory limit")
    return int(token)


def _unique_members(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Duplicate JSON member")
        result[key] = value
    return result


def _reject_nonfinite(token: str) -> None:
    raise ValueError("Non-finite JSON number")


def _decode_content(raw: bytes) -> dict:
    if len(raw) > MAX_LAB_PACKAGE_BYTES:
        raise LabInputError("LAB_PACKAGE_TOO_LARGE")
    try:
        document = json.loads(
            raw.decode("utf-8"), object_pairs_hook=_unique_members,
            parse_int=lab_integer, parse_float=Decimal, parse_constant=_reject_nonfinite,
        )
    except (ValueError, RecursionError, InvalidOperation) as error:
        raise LabInputError("INVALID_LAB_PACKAGE_JSON") from error
    if (
        not isinstance(document, dict)
        or document.keys() != {"document_type", "contract_version", "content"}
        or document["document_type"] != "review_package_input"
        or document["contract_version"] != CONTRACT_VERSION
        or not isinstance(document["content"], dict)
    ):
        raise LabInputError("INVALID_LAB_PACKAGE_ENVELOPE")
    return document["content"]


def _nonblank_text(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _ungradable(report: dict, reason: str, *locations: str) -> dict:
    return {**report, "outcome": "UNGRADABLE", "reason": reason, "unresolved_locations": list(locations)}


def assess_age_boundaries(raw: bytes, *, basis_id: str, actor_ref: str, minimum: int, maximum: int) -> dict:
    """Assess the declared inputs of the explicitly linked cases in one lab submission."""
    content = _decode_content(raw)
    report = {
        "experiment": "lab-age-bva-v1",
        "classification": "synthetic",
        "criterion": "TWO_VALUE_BVA_INTEGER_AGE",
        "input_sha256": hashlib.sha256(raw).hexdigest(),
        "basis_id": basis_id,
        "operator_interpretation": {"actor_ref": actor_ref, "inclusive_age_interval": [minimum, maximum]},
    }
    scope = content.get("scope")
    if not isinstance(scope, dict) or not _nonblank_text(scope.get("description")):
        return _ungradable(report, "SCOPE_NOT_SUPPLIED", "/content/scope/description")

    source_locations = [
        f"/content/{field}" for field in ("tc_sources", "supporting_sources")
        if field in content and content[field] != []
    ]
    if source_locations:
        return _ungradable(report, "UNRESOLVED_SOURCE_BINDINGS", *source_locations)

    basis = content.get("basis_elements")
    if not isinstance(basis, list):
        return _ungradable(report, "BASIS_NOT_SUPPLIED", "/content/basis_elements")
    matches = [
        index for index, element in enumerate(basis)
        if isinstance(element, dict) and element.get("source_id") == basis_id
    ]
    if not matches:
        return _ungradable(report, "BASIS_NOT_SUPPLIED", "/content/basis_elements")
    if len(matches) > 1:
        return _ungradable(report, "BASIS_AMBIGUOUS", *(f"/content/basis_elements/{i}" for i in matches))
    index = matches[0]
    basis_locator = f"/content/basis_elements/{index}/text"
    if not _nonblank_text(basis[index].get("text")):
        return _ungradable(report, "BASIS_TEXT_MISSING", basis_locator)
    report["basis_locator"] = basis_locator

    cases = content.get("test_cases")
    if not isinstance(cases, list) or not cases:
        return _ungradable(report, "CASE_EVIDENCE_NOT_SUPPLIED", "/content/test_cases")

    observations = []
    unresolved = []
    excluded = []
    for index, case in enumerate(cases):
        location = f"/content/test_cases/{index}"
        if not isinstance(case, dict):
            unresolved.append(location)
            continue
        refs = case.get("basis_refs")
        if not isinstance(refs, list) or any(not _nonblank_text(ref) for ref in refs):
            unresolved.append(f"{location}/basis_refs")
            continue
        if basis_id not in refs:
            excluded.append(location)
            continue
        test_data = case.get("test_data")
        age = test_data.get("age") if isinstance(test_data, dict) else None
        if type(age) is not int:
            unresolved.append(f"{location}/test_data/age")
            continue
        source_id = case.get("source_id")
        observations.append({
            "case_id": source_id if _nonblank_text(source_id) else None,
            "age": age,
            "locator": f"{location}/test_data/age",
        })

    targets = sorted({minimum - 1, minimum, maximum, maximum + 1})
    report.update(target_ages=targets, case_age_inputs=observations, excluded_cases=excluded)
    if unresolved:
        return _ungradable(report, "AGE_EVIDENCE_UNRESOLVED", *unresolved)
    if not observations:
        return _ungradable(report, "NO_LINKED_AGE_CASES", "/content/test_cases")

    observed_ages = {item["age"] for item in observations}
    return {**report, "outcome": "ASSESSED", "missing_ages": [age for age in targets if age not in observed_ages]}
