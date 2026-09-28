"""Describe actual availability; the design allocation is not a runtime claim."""

import platform
import sqlite3
import sys

from tdg import __version__

CONTRACT_VERSION = "1.0"
STORE_SCHEMA_VERSION = 1
LAB_POLICY_VERSION = "i01-lab-v1"
DISABLED_COMMANDS = ("import", "receipt", "package")


def version_info() -> dict:
    return {
        "tdg": __version__,
        "python": platform.python_version(),
        "python_implementation": platform.python_implementation(),
        "sqlite": sqlite3.sqlite_version,
        "host_os": sys.platform,
        "host_architecture": platform.machine(),
        "supported_product_target": "Windows x64 / CPython 3.13",
        "contract_version": CONTRACT_VERSION,
        "store_schema_version": STORE_SCHEMA_VERSION,
        "selected_lab_policy_version": LAB_POLICY_VERSION,
    }


def capability_manifest() -> dict:
    from tdg.windows_workspace import supported_host

    result = {
        "manifest_version": "1.0",
        "build": __version__,
        "increment": "I-01",
        "implementation_stage": "W01_VERIFIED_CLOSURE_PENDING",
        "enabled_commands": ["version", "capabilities"],
        "disabled_commands": {
            "import": "CAPTURE_AND_PROTECTION_NOT_IMPLEMENTED",
            "receipt": "CAPTURE_NOT_IMPLEMENTED",
            "package": "CAPTURE_NOT_IMPLEMENTED",
        },
        "disabled_capabilities": [
            "native_json_capture",
            "csv",
            "attachments_and_extraction",
            "core_minimum_check",
            "domain_qualification",
            "test_design_review",
            "finding_dispositions",
            "result_export",
            "model_invocation",
            "sealed_processing",
            "tc_repair_or_approval",
        ],
        "data_policy": "PUBLIC_OR_SYNTHETIC_LABORATORY_ONLY",
        "package_processing_enabled": False,
        "target_platform_verification": "W01_WINDOWS_TRIAL_PASSED_2026-09-28",
        "workspace_path_support": "DIRECT_CHILD_OF_LOCALAPPDATA_TDG_LAB_ONLY",
    }
    if supported_host():
        result["enabled_commands"].append("init")
    else:
        result["disabled_commands"]["init"] = "WINDOWS_X64_PYTHON313_REQUIRED"
    return result
