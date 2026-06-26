#!/usr/bin/env python3
"""Command Center OS — interactive installer / operator onboarding.

Run this once after creating your repo from the template:

    python install.py

It asks who you are, what you build (ventures), your standards, boundaries, voice,
and approval posture, then writes your answers into the operator layer:

    _operator/OPERATOR-TRUTHS.md   (your durable truths)
    _operator/OPERATOR-VOICE.md    (how you write/speak)
    _memory/SESSION-BOOT-STATE.md  (current state; first-run loop cleared)
    _memory/decision-log.md        (records that onboarding completed)

No AI agent is required to run this; it is plain Python (stdlib only). You can
re-run it anytime to update your profile, or edit those files by hand.

It never stores secrets. Ventures are recorded as names/intentions only — the full
"venture harness" (a project's own memory, routing, connectivity, governance, and
stage spine) is installed into each venture folder by your AI agent when you create
the venture. See GUIDE.md.
"""
from __future__ import annotations

import os
import pathlib
import sys
from datetime import date

ROOT = os.path.dirname(os.path.abspath(__file__))
TRUTHS = os.path.join(ROOT, "_operator", "OPERATOR-TRUTHS.md")
VOICE = os.path.join(ROOT, "_operator", "OPERATOR-VOICE.md")
BOOT = os.path.join(ROOT, "_memory", "SESSION-BOOT-STATE.md")
DLOG = os.path.join(ROOT, "_memory", "decision-log.md")

FIRST_RUN_BLOCKQUOTE = (
    "> **First run:** the Core Operator Truths table below is intentionally empty except for the universal\n"
    "> system invariants. Run `_routing/runtime/routes/operator-onboarding.md` to add your own truths\n"
    "> (who you are, what you build, your standards, your boundaries). Until then, treat operator-specific\n"
    "> judgment as unknown and ask before assuming.\n\n"
)

# Exact text of .claude/settings.json — kept here so install.py is the single
# setup step and a fresh clone is fully wired without manual file placement.
HOOKS_SETTINGS = """{
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python _routing/atx_hook_runner.py --event context-recovery --request \\"session start boot check\\" --format markdown"
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Bash|Edit|Write|NotebookEdit",
        "hooks": [
          {
            "type": "command",
            "command": "python _routing/atx_pretooluse_adapter.py"
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python _routing/atx_finalization_reminder.py"
          }
        ]
      }
    ]
  }
}
"""

# Exact text of .claude/settings.json -- kept here so install.py is the single
# setup step and a fresh clone is fully wired without manual file placement.
HOOKS_SETTINGS = r"""{
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python _routing/atx_hook_runner.py --event context-recovery --request \"session start boot check\" --format markdown"
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Bash|Edit|Write|NotebookEdit",
        "hooks": [
          {
            "type": "command",
            "command": "python _routing/atx_pretooluse_adapter.py"
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python _routing/atx_finalization_reminder.py"
          }
        ]
      }
    ]
  }
}
"""


# ---------------------------------------------------------------- prompts ----
def ask(prompt: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    try:
        val = input(f"{prompt}{suffix}\n> ").strip()
    except EOFError:
        return default
    return val or default


def ask_list(prompt: str) -> list[str]:
    print(f"\n{prompt}")
    print("(Enter one per line. Press Enter on an empty line to finish.)")
    items: list[str] = []
    while True:
        try:
            line = input("> ").strip()
        except EOFError:
            break
        if not line:
            break
        items.append(line)
    return items


def ask_choice(prompt: str, options: list[str], default_index: int = 0) -> str:
    print(f"\n{prompt}")
    for i, opt in enumerate(options, 1):
        marker = " (default)" if i - 1 == default_index else ""
        print(f"  {i}) {opt}{marker}")
    try:
        raw = input("> ").strip()
    except EOFError:
        raw = ""
    if not raw:
        return options[default_index]
    if raw.isdigit() and 1 <= int(raw) <= len(options):
        return options[int(raw) - 1]
    return raw


# ------------------------------------------------------------ file helpers ----
def read(path: str) -> str:
    return open(path, encoding="utf-8").read()


def write(path: str, text: str) -> None:
    open(path, "w", encoding="utf-8").write(text)


def replace_section(text: str, heading: str, new_body: str) -> str:
    """Replace the body under a `## heading` line (up to the next `## ` or EOF)."""
    lines = text.splitlines()
    out: list[str] = []
    i = 0
    replaced = False
    while i < len(lines):
        out.append(lines[i])
        if lines[i].strip() == heading and not replaced:
            i += 1
            # skip old body until next "## " heading
            while i < len(lines) and not lines[i].startswith("## "):
                i += 1
            out.append("")
            out.extend(new_body.rstrip("\n").splitlines())
            out.append("")
            replaced = True
            continue
        i += 1
    result = "\n".join(out)
    if not result.endswith("\n"):
        result += "\n"
    return result


# ----------------------------------------------------------- hooks helpers ----
def ensure_hooks(root: str) -> bool:
    """Idempotently ensure .claude/settings.json exists with enforcement hooks.

    Returns True if the file was created, False if it already existed (no-op).
    The file is written UTF-8 without BOM. An existing file is never overwritten.
    """
    dot_claude = os.path.join(root, ".claude")
    settings_path = os.path.join(dot_claude, "settings.json")
    if os.path.exists(settings_path):
        return False
    os.makedirs(dot_claude, exist_ok=True)
    pathlib.Path(settings_path).write_bytes(HOOKS_SETTINGS.encode("utf-8"))
    return True


# ------------------------------------------------------------------ build ----
def build_truths_rows(name, role, ventures, standards, boundaries, posture) -> str:
    rows = [
        f"| {name} is the operator and final human authority. | User-confirmed | onboarding |",
        f"| The operator builds: {role}. | User-confirmed | onboarding |",
    ]
    for v in ventures:
        rows.append(f"| Active venture: {v}. | User-confirmed | onboarding |")
    for s in standards:
        rows.append(f"| Standard: {s} | User-confirmed | onboarding |")
    for b in boundaries:
        rows.append(f"| Boundary: {b} | User-confirmed | onboarding |")
    rows.append(f"| Approval posture: {posture} | User-confirmed | onboarding |")
    table = (
        "| Truth | Status | Source |\n"
        "|---|---|---|\n" + "\n".join(rows)
    )
    note = (
        "Ventures are recorded as lanes here. The full **venture harness** (each venture's own memory, "
        "routing, connectivity, governance, and stage spine) is installed into the venture's folder by "
        "your AI agent when you create it — see `GUIDE.md`.\n\n"
    )
    return note + table


def build_voice_body(cadence, trust_build, trust_erode, challenge) -> str:
    return (
        "Captured during onboarding:\n\n"
        f"- Working voice / cadence: {cadence}\n"
        f"- Builds trust: {trust_build}\n"
        f"- Erodes trust: {trust_erode}\n"
        f"- How to challenge / correct me: {challenge}\n\n"
        "Status:\n\n"
        "```text\n"
        "Captured via operator onboarding. Edit freely.\n"
        "```\n"
    )


def build_boot(today, name, ventures, posture) -> str:
    vlines = "\n".join(f"- {v}" for v in ventures) if ventures else "- (none yet)"
    return f"""# Session Boot State

Status: operator onboarded
Date: {today}

## Current Root State

Command Center OS is configured for {name}. Runtime Tier 0 is the default boot path:

1. `CLAUDE.md`
2. `CONTEXT.md`
3. `_memory/SESSION-BOOT-STATE.md`
4. `_routing/runtime/ROUTING-KERNEL.md`
5. `_routing/runtime/ROUTE-INDEX.md`
6. `_memory/runtime/MEMORY-KERNEL.md`
7. `_memory/runtime/LOAD-INDEX.md`

## Standing Facts

- Operator onboarding is complete; `_operator/` carries the operator's truths and voice.
- Approval posture: {posture}
- Sentinel is the mandatory root risk gate and fires on all non-trivial work.

## Venture Lanes

{vlines}

Each venture's operational structure (the venture harness) lives in its own folder, installed by the
agent at creation. Root stores the lane name, not the venture's working data.

## Open Loops

- (none) — add current work here as it starts.

## Next Owner

Conductor owns runtime route selection. Keeper owns memory relevance. Librarian owns pointer hygiene.
"""


# ----------------------------------------------------------- hooks helpers ----
def ensure_hooks(root: str) -> bool:
    """Idempotently ensure .claude/settings.json exists with enforcement hooks.

    Returns True if the file was created, False if it already existed (no-op).
    The file is written UTF-8 without BOM. An existing file is never overwritten.
    """
    dot_claude = os.path.join(root, ".claude")
    settings_path = os.path.join(dot_claude, "settings.json")
    if os.path.exists(settings_path):
        return False
    os.makedirs(dot_claude, exist_ok=True)
    pathlib.Path(settings_path).write_bytes(HOOKS_SETTINGS.encode("utf-8"))
    return True



# ------------------------------------------------------------------- main ----
def already_onboarded() -> bool:
    try:
        return "EMPTY SCAFFOLD" not in read(TRUTHS)
    except OSError:
        return False


def main() -> int:
    print("=" * 64)
    print(" Command Center OS — operator onboarding")
    print("=" * 64)
    print("This records who you are so the system stays aligned with you.")
    print("It never stores secrets. Press Enter to accept a [default].\n")

    if already_onboarded():
        ans = ask("Operator profile already exists. Overwrite it? (y/N)", "N")
        if ans.lower() not in ("y", "yes"):
            print("Aborted. No files changed.")
            return 0

    name = ask("Your name or handle:", "Operator")
    role = ask("In one line, what do you do / build?", "independent operator")
    ventures = ask_list("Your ventures / work lanes (names, optionally 'name - short note'):")
    standards = ask_list("Your standards / non-negotiables:")
    boundaries = ask_list("Your hard boundaries / do-not-touch zones:")

    print("\n--- Voice ---")
    cadence = ask("How would you describe your working voice/cadence?", "direct and specific")
    trust_build = ask("What builds your trust in an answer?", "named sources and clear ownership")
    trust_erode = ask("What erodes your trust?", "vague, confident claims with no source")
    challenge = ask("How do you like to be challenged or corrected?", "directly, with the reason")

    posture = ask_choice(
        "Approval posture — when may the system act on its own?",
        [
            "Act on low-risk reversible work; ask before live systems, money, or credentials",
            "Ask before most changes",
            "More autonomous; act unless high-risk",
        ],
        default_index=0,
    )

    today = date.today().isoformat()

    # OPERATOR-TRUTHS.md
    t = read(TRUTHS)
    t = t.replace(FIRST_RUN_BLOCKQUOTE, "")
    t = t.replace(
        "Status: EMPTY SCAFFOLD — populate during operator onboarding",
        f"Status: populated via operator onboarding ({today})",
    )
    t = replace_section(
        t, "## Operator-Specific Truths",
        build_truths_rows(name, role, ventures, standards, boundaries, posture),
    )
    write(TRUTHS, t)

    # OPERATOR-VOICE.md
    v = read(VOICE)
    v = replace_section(
        v, "## Operator Voice (populate during onboarding)",
        build_voice_body(cadence, trust_build, trust_erode, challenge),
    )
    write(VOICE, v)

    # SESSION-BOOT-STATE.md
    write(BOOT, build_boot(today, name, ventures, posture))

    # decision-log.md
    try:
        log = read(DLOG)
        entry = (
            f"\n## {today} — Operator onboarding completed\n"
            f"Decision: Operator profile set for {name}.\n"
            f"Why: First-run onboarding via install.py.\n"
            f"Source: install.py\n"
            f"Owner: {name}\n"
        )
        marker = "<!-- No decisions recorded yet. Operator onboarding will add the first entries. -->"
        log = log.replace(marker, entry.strip()) if marker in log else log + entry
        write(DLOG, log)
    except OSError:
        pass

    # Ensure .claude/settings.json exists with enforcement hooks
    hooks_created = ensure_hooks(ROOT)

    # Ensure .claude/settings.json exists with enforcement hooks
    hooks_created = ensure_hooks(ROOT)

    print("\n" + "=" * 64)
    print(" Onboarding complete.")
    print("=" * 64)
    print("Updated: _operator/OPERATOR-TRUTHS.md, _operator/OPERATOR-VOICE.md,")
    print("         _memory/SESSION-BOOT-STATE.md, _memory/decision-log.md")
    print("  Enforcement hooks: .claude/settings.json (SessionStart / PreToolUse / Stop)")
    if hooks_created:
        print("  (hooks file was missing — created now)")
    print("\nNext steps:")
    print("  1. Verify the engine:  python _routing/run_gates.py")
    print("  2. Open the repo with your AI agent and say: 'Load Runtime Tier 0, then start.'")
    print("  3. Create your first venture — ask the agent: 'scaffold a venture called <name>'.")
    print("     The agent installs the full venture harness (memory, routing, connectivity,")
    print("     governance, stages) into that venture's folder.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
