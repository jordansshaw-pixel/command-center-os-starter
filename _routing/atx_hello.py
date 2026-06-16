#!/usr/bin/env python3
"""Emit the deterministic the OS hello entrance response."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ENTRY_SOURCES = [
    "CLAUDE.md",
    "CONTEXT.md",
    "ROUTING.md",
    "_memory/MEMORY-ROUTER.md",
    "_handoffs/README.md",
]
DEFAULT_FOCUS = "stabilize the current the OS build before expanding new lanes"
PROMPT = "What should enter the OS now: root work, a project lane, or an intake item?"


def extract_current_focus() -> str:
    context_path = ROOT / "CONTEXT.md"
    if not context_path.exists():
        return DEFAULT_FOCUS
    lines = context_path.read_text(encoding="utf-8").splitlines()
    in_block = False
    for line in lines:
        stripped = line.strip()
        if stripped == "```text" and not in_block:
            in_block = True
            continue
        if in_block and stripped == "```":
            in_block = False
            continue
        if in_block and "Stabilize the current the OS build" in stripped:
            return stripped.rstrip(".")
    return DEFAULT_FOCUS


def response_packet() -> dict[str, str | list[str]]:
    return {
        "status": "the OS entrance loaded",
        "workspace": str(ROOT),
        "default_scope": "root unless the operator names a project, folder, or file",
        "entry_sources": ENTRY_SOURCES,
        "current_focus": extract_current_focus(),
        "prompt": PROMPT,
    }


def render_text(packet: dict[str, str | list[str]]) -> str:
    sources = ", ".join(str(source) for source in packet["entry_sources"])
    return "\n".join(
        [
            f"{packet['status']}.",
            f"Workspace: {packet['workspace']}",
            f"Default scope: {packet['default_scope']}.",
            f"Entry sources: {sources}.",
            f"Current focus: {packet['current_focus']}.",
            str(packet["prompt"]),
            "",
        ]
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Emit the OS hello entrance response.")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    packet = response_packet()
    if args.format == "json":
        print(json.dumps(packet, indent=2))
    else:
        print(render_text(packet), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
