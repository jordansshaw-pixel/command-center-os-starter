#!/usr/bin/env python3
"""Canonical the OS gate runner.

This is the real gate entry point. Shell and PowerShell files are launchers
only; they resolve an interpreter and hand execution here.
"""

from __future__ import annotations

import argparse
import sys
from collections.abc import Callable
from pathlib import Path


MIN_PYTHON = (3, 10)
ROOT = Path(__file__).resolve().parents[1]
ROUTING_DIR = ROOT / "_routing"

if str(ROUTING_DIR) not in sys.path:
    sys.path.insert(0, str(ROUTING_DIR))

import atx_fast_lane_gate  # noqa: E402
import atx_hook_runner  # noqa: E402
import atx_live_system_gate  # noqa: E402
import atx_log_pruning_gate  # noqa: E402
import atx_multi_agent_gate  # noqa: E402
import distribution_scrub_gate  # noqa: E402


CheckFn = Callable[[list[str]], int]


CHECKS: tuple[tuple[str, CheckFn, list[str]], ...] = (
    ("atx_fast_lane_gate.py --self-test", atx_fast_lane_gate.main, ["--self-test"]),
    ("atx_multi_agent_gate.py --self-test", atx_multi_agent_gate.main, ["--self-test"]),
    ("atx_hook_runner.py --self-test", atx_hook_runner.main, ["--self-test"]),
    ("atx_multi_agent_gate.py --validate-registry", atx_multi_agent_gate.main, ["--validate-registry"]),
    ("atx_live_system_gate.py --self-test", atx_live_system_gate.main, ["--self-test"]),
    ("atx_log_pruning_gate.py --self-test", atx_log_pruning_gate.main, ["--self-test"]),
    ("distribution_scrub_gate.py --scan", distribution_scrub_gate.main, []),
)


def assert_supported_python() -> None:
    if sys.version_info < MIN_PYTHON:
        version = ".".join(str(part) for part in MIN_PYTHON)
        current = ".".join(str(part) for part in sys.version_info[:3])
        print(
            f"the OS gate runner requires Python >= {version}; current interpreter is {current}.",
            file=sys.stderr,
        )
        raise SystemExit(2)


def run_checks() -> int:
    failed = False
    for name, check_fn, args in CHECKS:
        print(f"Running {name}...")
        try:
            status = check_fn(args)
        except SystemExit as exc:
            status = int(exc.code or 0) if isinstance(exc.code, int) else 1
        except Exception as exc:  # pragma: no cover - defensive runner boundary
            print(f"FAIL {name} ({exc.__class__.__name__}: {exc})", file=sys.stderr)
            failed = True
            continue
        if status == 0:
            print(f"PASS {name}")
        else:
            print(f"FAIL {name} (exit {status})", file=sys.stderr)
            failed = True
    if failed:
        print("the OS gate checks failed.", file=sys.stderr)
        return 2
    print("the OS gate checks passed.")
    return 0


def run_self_test() -> int:
    assert_supported_python()
    if len(CHECKS) != 7:
        print("FAIL gate runner self-test: unexpected check count", file=sys.stderr)
        return 1
    names = [name for name, _check_fn, _args in CHECKS]
    if len(names) != len(set(names)):
        print("FAIL gate runner self-test: duplicate check name", file=sys.stderr)
        return 1
    print("PASS gate runner self-test")
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the OS deterministic gates.")
    parser.add_argument("--self-test", action="store_true", help="Smoke-test the canonical runner.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    assert_supported_python()
    args = parse_args(argv or sys.argv[1:])
    if args.self_test:
        return run_self_test()
    return run_checks()


if __name__ == "__main__":
    raise SystemExit(main())
