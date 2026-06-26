#!/usr/bin/env python3
"""Lightweight Stop-hook reminder. Prints the Finalization Rule template only.

Deliberately does not call atx_hook_runner.py's full multi-agent engagement
packet here -- Stop fires on every turn, and the full packet is too heavy to
print every time. Session-time risk checks already ran via PreToolUse.
"""

from __future__ import annotations

import sys

TEMPLATE = """Command Center OS Finalization Rule -- answer before ending this turn if the work was substantial:
- What did we learn?
- Where was it saved?
- What remains open?
- Which role should pick it up next?

If something remains open and needs the operator's judgment, use the Decision Packet Template
in CLAUDE.md instead of a vague continuation question."""


def main() -> int:
    if "--self-test" in sys.argv:
        print("PASS finalization reminder self-test")
        return 0
    print(TEMPLATE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
