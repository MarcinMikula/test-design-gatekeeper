"""Thin terminal adapter. Disabled commands must have no data-side effects."""

import argparse
import json
import sys

from tdg.capabilities import DISABLED_COMMANDS, LAB_AGE_BVA_COMMAND, capability_manifest, version_info
from tdg.lab_age_bva import MAX_LAB_PACKAGE_BYTES, LabInputError, assess_age_boundaries, lab_integer


class _SafeParser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        # argparse's default includes arbitrary arguments and terminal controls.
        self.exit(2, "INVALID_ARGUMENTS: use tdg --help.\n")


def _run_lab_age_bva(args: argparse.Namespace) -> int:
    if args.classification != "synthetic":
        print("SYNTHETIC_CLASSIFICATION_REQUIRED", file=sys.stderr)
        return 3
    minimum, maximum = args.confirmed_interval
    if not args.actor_ref.strip() or not args.basis_id.strip() or minimum > maximum:
        print("INVALID_LAB_CONTEXT: provide an actor, a basis ID and an ordered interval.", file=sys.stderr)
        return 2
    if sys.stdin.isatty():
        print("LAB_PACKAGE_STDIN_REQUIRED: pipe or redirect one synthetic JSON package.", file=sys.stderr)
        return 2
    try:
        raw = sys.stdin.buffer.read(MAX_LAB_PACKAGE_BYTES + 1)
        result = assess_age_boundaries(
            raw, basis_id=args.basis_id, actor_ref=args.actor_ref, minimum=minimum, maximum=maximum,
        )
    except LabInputError as error:
        print(str(error), file=sys.stderr)
        return 2
    except OSError:
        print("LAB_PACKAGE_READ_FAILED", file=sys.stderr)
        return 4
    except KeyboardInterrupt:
        print("LAB_REVIEW_INTERRUPTED", file=sys.stderr)
        return 130
    print(json.dumps(result, ensure_ascii=True, indent=2))
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = _SafeParser(prog="tdg", allow_abbrev=False)
    parser.description = "Test Design Gatekeeper — workspace foundation and laboratory experiment."
    commands = parser.add_subparsers(dest="command", required=True)
    for name, help_text in (
        ("version", "Show build, runtime and selected contract versions."),
        ("capabilities", "Show enabled commands and unavailable capabilities."),
    ):
        commands.add_parser(name, help=help_text, allow_abbrev=False)
    for name in DISABLED_COMMANDS:
        commands.add_parser(
            name,
            help="Unavailable in this build; see tdg capabilities.",
            allow_abbrev=False,
        )
    initialize = commands.add_parser("init", help="Create an empty laboratory workspace on Windows x64.", allow_abbrev=False)
    initialize.add_argument("--data-dir", help="New directory directly under LOCALAPPDATA/TDG/lab; default is a generated UUID.")
    initialize.add_argument("--profile", required=True)
    initialize.add_argument("--actor-ref", required=True)
    lab = commands.add_parser(
        LAB_AGE_BVA_COMMAND, help="Compare synthetic age test data with two-value BVA targets.",
        description="Read one synthetic JSON package from stdin for a laboratory age BVA check.",
        allow_abbrev=False,
    )
    lab.add_argument("--classification", required=True, help="Declare the input as synthetic.")
    lab.add_argument("--actor-ref", required=True, help="Logical reference of the operator confirming the interpretation.")
    lab.add_argument("--basis-id", required=True, help="Supplied basis source ID for the age rule.")
    lab.add_argument(
        "--confirmed-interval", nargs=2, type=lab_integer, metavar=("MIN", "MAX"), required=True,
        help="Confirmed inclusive integer interval with the adjacent values in the submitted domain.",
    )

    args, remaining = parser.parse_known_args(argv)
    if args.command in DISABLED_COMMANDS:
        # No store import, directory creation or input opening on this path.
        print("CAPABILITY_NOT_ENABLED: see tdg capabilities.", file=sys.stderr)
        return 3
    if remaining:
        parser.error("Unexpected arguments")

    if args.command == LAB_AGE_BVA_COMMAND:
        return _run_lab_age_bva(args)

    if args.command == "init":
        from tdg.storage import StoreError, StoreExistsError
        from tdg.windows_workspace import (
            WorkspaceBusyError, WorkspaceOperationError, WorkspacePolicyError,
            initialize_workspace,
        )

        try:
            metadata, data_dir = initialize_workspace(
                requested=args.data_dir, actor_ref=args.actor_ref, profile=args.profile,
            )
        except (WorkspacePolicyError, StoreExistsError, WorkspaceBusyError,
                WorkspaceOperationError, StoreError) as error:
            code = 3 if isinstance(error, WorkspacePolicyError) else 5 if isinstance(error, StoreExistsError) else 4
            # The service exposes static codes, not native error strings or paths.
            print(str(error), file=sys.stderr)
            return code
        except KeyboardInterrupt:
            print("INITIALIZATION_INTERRUPTED: no success is asserted.", file=sys.stderr)
            return 130
        print(json.dumps({
            "workspace_id": metadata.workspace_id,
            "profile": metadata.profile,
            "schema_version": metadata.schema_version,
            "data_dir": str(data_dir),
            "review_performed": False,
        }, ensure_ascii=True, indent=2))
        return 0

    result = version_info() if args.command == "version" else capability_manifest()
    print(json.dumps(result, ensure_ascii=True, indent=2))
    return 0
