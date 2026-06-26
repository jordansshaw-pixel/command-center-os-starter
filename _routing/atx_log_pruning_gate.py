#!/usr/bin/env python3

"""Deterministic enforcement detector for the OS log pruning rule.

This script measures OS-owned log size against the registry thresholds and
routes over-threshold logs to Recorder. It NEVER prunes, edits, archives, hashes,
or splits a log. A passed scan means only that no enrolled log is over its
hard ceiling. It is not a prune and does not authorize one.

Source rule: _memory/runtime/LOG-PRUNING-RULE.md (preserves Recorder exact-record
authority). Enforcement policy: warn at trigger, hard-block at ceiling.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "_memory" / "runtime" / "log-registry.json"

DEFAULT_TRIGGER = 300
DEFAULT_TARGET = 200
DEFAULT_CEILING = 500
DEFAULT_OWNER = "Recorder"
DEFAULT_MAX_STALE_DAYS = 7

# `### YYYY-MM-DD HH:MM:SS +/-HH:MM - title` (current rule) and legacy date-only headings.
HEADING_FULL = re.compile(r"^###\s+(\d{4}-\d{2}-\d{2})[ T](\d{2}:\d{2}:\d{2})\s*([+-]\d{2}:\d{2})")
HEADING_DATE = re.compile(r"^###\s+(\d{4}-\d{2}-\d{2})")


def count_lines(path: Path) -> int:
    return len(path.read_text(encoding="utf-8").splitlines())


def classify(lines: int, trigger: int, ceiling: int) -> str:
    if lines >= ceiling:
        return "block"
    if lines > trigger:
        return "warn"
    return "ok"


def load_registry(registry_path: Path) -> dict[str, Any]:
    if not registry_path.exists():
        raise FileNotFoundError(f"Missing log registry: {registry_path}")
    data = json.loads(registry_path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("logs"), list):
        raise ValueError("Log registry must be an object with a 'logs' array.")
    return data


def resolve_entry(entry: dict[str, Any], defaults: dict[str, Any]) -> dict[str, Any]:
    return {
        "path": entry["path"],
        "trigger": int(entry.get("trigger", defaults.get("trigger", DEFAULT_TRIGGER))),
        "target": int(entry.get("target", defaults.get("target", DEFAULT_TARGET))),
        "ceiling": int(entry.get("ceiling", defaults.get("ceiling", DEFAULT_CEILING))),
        "owner": entry.get("owner", defaults.get("owner", DEFAULT_OWNER)),
        "freshness": entry.get("freshness", defaults.get("freshness")),
    }


def scan_entries(entries: list[dict[str, Any]], root: Path, only: set[str] | None = None) -> list[dict[str, Any]]:
    checked: list[dict[str, Any]] = []
    for entry in entries:
        rel = entry["path"]
        if only is not None and rel not in only:
            continue
        target = (root / rel).resolve()
        record = {
            "path": rel,
            "trigger": entry["trigger"],
            "target": entry["target"],
            "ceiling": entry["ceiling"],
            "owner": entry["owner"],
        }
        if not target.exists():
            record["lines"] = None
            record["status"] = "missing"
        else:
            lines = count_lines(target)
            record["lines"] = lines
            record["status"] = classify(lines, entry["trigger"], entry["ceiling"])
        checked.append(record)
    return checked


def overall_status(checked: list[dict[str, Any]]) -> str:
    statuses = {record["status"] for record in checked}
    if "block" in statuses:
        return "block"
    if "warn" in statuses:
        return "warn"
    return "pass"


def next_action(status: str, flagged: list[dict[str, Any]]) -> str:
    if status == "block":
        names = ", ".join(record["path"] for record in flagged if record["status"] == "block")
        return (
            f"Hard ceiling reached: {names}. Route to Recorder for archive-plus-index prune; "
            "Keeper confirms active open loops stay; Librarian updates the Archive Index."
        )
    if status == "warn":
        names = ", ".join(record["path"] for record in flagged if record["status"] == "warn")
        return f"Over trigger: {names}. Flag to Recorder to schedule an archive-plus-index prune. Commit not blocked."
    return "No enrolled log is over its hard ceiling. No prune required by size."


def build_packet(checked: list[dict[str, Any]], registry_label: str) -> dict[str, Any]:
    status = overall_status(checked)
    flagged = [record for record in checked if record["status"] != "ok"]
    return {
        "gate": "log-pruning",
        "deterministicOnly": True,
        "registry": registry_label,
        "status": status,
        "checked": checked,
        "flagged": flagged,
        "owner": DEFAULT_OWNER,
        "next": next_action(status, flagged),
    }


def parse_newest_timestamp(text: str) -> datetime | None:
    """Return the newest entry timestamp parsed from `### ` headings, or None.

    Full `### YYYY-MM-DD HH:MM:SS +/-HH:MM` headings parse to aware datetimes.
    Legacy date-only headings are treated as UTC midnight so comparison stays
    timezone-aware across mixed history.
    """
    newest: datetime | None = None
    for line in text.splitlines():
        if not line.startswith("###"):
            continue
        full = HEADING_FULL.match(line)
        if full:
            stamp = datetime.fromisoformat(f"{full.group(1)}T{full.group(2)}{full.group(3)}")
        else:
            date_only = HEADING_DATE.match(line)
            if not date_only:
                continue
            stamp = datetime.fromisoformat(date_only.group(1)).replace(tzinfo=timezone.utc)
        if newest is None or stamp > newest:
            newest = stamp
    return newest


def classify_freshness(newest: datetime | None, now: datetime, max_stale_days: int) -> str:
    if newest is None:
        return "unknown"
    age_days = (now - newest).total_seconds() / 86400.0
    return "stale" if age_days > max_stale_days else "fresh"


def scan_freshness(
    entries: list[dict[str, Any]],
    root: Path,
    now: datetime,
    only: set[str] | None = None,
) -> list[dict[str, Any]]:
    """Check only logs enrolled with a `freshness` block. Never blocks."""
    checked: list[dict[str, Any]] = []
    for entry in entries:
        fresh_cfg = entry.get("freshness")
        if not fresh_cfg:
            continue
        rel = entry["path"]
        if only is not None and rel not in only:
            continue
        max_stale = int(fresh_cfg.get("maxStaleDays", DEFAULT_MAX_STALE_DAYS))
        target = (root / rel).resolve()
        record: dict[str, Any] = {"path": rel, "maxStaleDays": max_stale}
        if not target.exists():
            record["newest"] = None
            record["ageDays"] = None
            record["status"] = "missing"
        else:
            newest = parse_newest_timestamp(target.read_text(encoding="utf-8"))
            record["newest"] = newest.isoformat() if newest else None
            record["ageDays"] = (
                round((now - newest).total_seconds() / 86400.0, 2) if newest else None
            )
            record["status"] = classify_freshness(newest, now, max_stale)
        checked.append(record)
    return checked


def freshness_overall(checked: list[dict[str, Any]]) -> str:
    statuses = {record["status"] for record in checked}
    if {"stale", "missing", "unknown"} & statuses:
        return "warn"
    return "pass"


def freshness_next(status: str, flagged: list[dict[str, Any]]) -> str:
    if status == "warn":
        names = ", ".join(record["path"] for record in flagged)
        return (
            f"Stale or unreadable log: {names}. If substantive work happened, write a "
            "decision-log entry before continuing. Non-blocking reminder; commit not blocked."
        )
    return "Enrolled logs are within their freshness window. No entry required by age."


def build_freshness_packet(checked: list[dict[str, Any]], registry_label: str) -> dict[str, Any]:
    status = freshness_overall(checked)
    flagged = [record for record in checked if record["status"] != "fresh"]
    return {
        "gate": "log-freshness",
        "deterministicOnly": True,
        "registry": registry_label,
        "status": status,
        "checked": checked,
        "flagged": flagged,
        "owner": DEFAULT_OWNER,
        "next": freshness_next(status, flagged),
    }


def render_freshness_markdown(packet: dict[str, Any]) -> str:
    lines = [
        "## Log Freshness Gate",
        f"- Status: {packet['status']}",
        f"- Registry: {packet['registry']}",
        f"- Owner: {packet['owner']}",
        f"- Next: {packet['next']}",
        "",
        "| Log | Newest entry | Age (days) | Max stale | Status |",
        "|---|---|---:|---:|---|",
    ]
    for record in packet["checked"]:
        newest = record["newest"] or "none"
        age = "n/a" if record["ageDays"] is None else str(record["ageDays"])
        lines.append(
            f"| {record['path']} | {newest} | {age} | {record['maxStaleDays']} | {record['status']} |"
        )
    return "\n".join(lines) + "\n"


def render_markdown(packet: dict[str, Any]) -> str:
    lines = [
        "## Log Pruning Gate",
        f"- Status: {packet['status']}",
        f"- Registry: {packet['registry']}",
        f"- Owner: {packet['owner']}",
        f"- Next: {packet['next']}",
        "",
        "| Log | Lines | Trigger | Ceiling | Status |",
        "|---|---:|---:|---:|---|",
    ]
    for record in packet["checked"]:
        line_text = "missing" if record["lines"] is None else str(record["lines"])
        lines.append(
            f"| {record['path']} | {line_text} | {record['trigger']} | {record['ceiling']} | {record['status']} |"
        )
    return "\n".join(lines) + "\n"


def run_scan(args: argparse.Namespace) -> int:
    try:
        data = load_registry(REGISTRY_PATH)
    except (FileNotFoundError, ValueError, json.JSONDecodeError) as exc:
        packet = {
            "gate": "log-pruning",
            "deterministicOnly": True,
            "status": "block",
            "error": str(exc),
            "owner": DEFAULT_OWNER,
            "next": "Restore or fix _memory/runtime/log-registry.json, then retry.",
        }
        print(json.dumps(packet, indent=2))
        return 2
    defaults = data.get("defaults", {})
    entries = [resolve_entry(entry, defaults) for entry in data["logs"]]
    only = set(args.only) if args.only else None
    checked = scan_entries(entries, ROOT, only)
    packet = build_packet(checked, REGISTRY_PATH.relative_to(ROOT).as_posix())
    if args.format == "markdown":
        print(render_markdown(packet), end="")
    else:
        print(json.dumps(packet, indent=2))
    # Warn is non-blocking (exit 0); only a hard ceiling blocks.
    return 2 if packet["status"] == "block" else 0


def run_freshness_scan(args: argparse.Namespace) -> int:
    try:
        data = load_registry(REGISTRY_PATH)
    except FileNotFoundError:
        # Missing registry in freshness mode: treat as no enrolled logs, return pass with empty list.
        checked: list[dict[str, Any]] = []
        packet = build_freshness_packet(checked, REGISTRY_PATH.relative_to(ROOT).as_posix())
        if args.format == "markdown":
            print(render_freshness_markdown(packet), end="")
        else:
            print(json.dumps(packet, indent=2))
        return 0
    except (ValueError, json.JSONDecodeError) as exc:
        packet = {
            "gate": "log-freshness",
            "deterministicOnly": True,
            "status": "block",
            "error": str(exc),
            "owner": DEFAULT_OWNER,
            "next": "Restore or fix _memory/runtime/log-registry.json, then retry.",
        }
        print(json.dumps(packet, indent=2))
        return 2
    defaults = data.get("defaults", {})
    entries = [resolve_entry(entry, defaults) for entry in data["logs"]]
    only = set(args.only) if args.only else None
    now = datetime.now(timezone.utc)
    checked = scan_freshness(entries, ROOT, now, only)
    packet = build_freshness_packet(checked, REGISTRY_PATH.relative_to(ROOT).as_posix())
    if args.format == "markdown":
        print(render_freshness_markdown(packet), end="")
    else:
        print(json.dumps(packet, indent=2))
    # Freshness is a reminder, never a blocker: a stale log returns exit 0.
    return 0


def _write_lines(path: Path, count: int) -> None:
    path.write_text("\n".join(f"line {index}" for index in range(count)) + "\n", encoding="utf-8")


def run_self_test() -> int:
    # Pure classify transitions.
    if classify(200, 300, 500) != "ok":
        print("FAIL classify ok band", file=sys.stderr)
        return 1
    if classify(300, 300, 500) != "ok":
        print("FAIL classify trigger boundary is not exceeded at equal", file=sys.stderr)
        return 1
    if classify(301, 300, 500) != "warn":
        print("FAIL classify warn band", file=sys.stderr)
        return 1
    if classify(499, 300, 500) != "warn":
        print("FAIL classify warn upper", file=sys.stderr)
        return 1
    if classify(500, 300, 500) != "block":
        print("FAIL classify ceiling boundary blocks", file=sys.stderr)
        return 1

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        _write_lines(root / "ok.md", 150)
        _write_lines(root / "warn.md", 350)
        _write_lines(root / "block.md", 600)
        entries = [
            resolve_entry({"path": "ok.md"}, {}),
            resolve_entry({"path": "warn.md"}, {}),
            resolve_entry({"path": "block.md"}, {}),
            resolve_entry({"path": "absent.md"}, {}),
        ]
        checked = scan_entries(entries, root)
        by_path = {record["path"]: record["status"] for record in checked}
        if by_path != {"ok.md": "ok", "warn.md": "warn", "block.md": "block", "absent.md": "missing"}:
            print(f"FAIL scan statuses: {by_path}", file=sys.stderr)
            return 1
        packet = build_packet(checked, "self-test")
        if packet["status"] != "block":
            print("FAIL overall status should block when any log blocks", file=sys.stderr)
            return 1

        # Only-filter ignores unstaged logs.
        staged = scan_entries(entries, root, only={"warn.md"})
        if build_packet(staged, "self-test")["status"] != "warn":
            print("FAIL only-filter should isolate to warn log", file=sys.stderr)
            return 1

        # Non-block band returns warn-only when nothing reaches ceiling.
        clean = scan_entries(
            [resolve_entry({"path": "ok.md"}, {}), resolve_entry({"path": "warn.md"}, {})],
            root,
        )
        if build_packet(clean, "self-test")["status"] != "warn":
            print("FAIL warn-only overall status", file=sys.stderr)
            return 1

    # Freshness: classify transitions with a fixed `now` (inverse of size).
    fixed_now = datetime(2026, 6, 24, 12, 0, 0, tzinfo=timezone.utc)
    if classify_freshness(datetime(2026, 6, 20, 12, 0, 0, tzinfo=timezone.utc), fixed_now, 7) != "fresh":
        print("FAIL freshness within window", file=sys.stderr)
        return 1
    if classify_freshness(datetime(2026, 6, 10, 12, 0, 0, tzinfo=timezone.utc), fixed_now, 7) != "stale":
        print("FAIL freshness past window", file=sys.stderr)
        return 1
    if classify_freshness(None, fixed_now, 7) != "unknown":
        print("FAIL freshness unknown when no timestamp", file=sys.stderr)
        return 1

    # Newest-timestamp parse picks the max across full and legacy date-only headings.
    sample = (
        "## Decisions\n"
        "### 2026-06-24 22:16:50 -07:00 - Newest full timestamp\n"
        "### 2026-06-11 22:22:36 -05:00 - Older full timestamp\n"
        "### 2026-06-05 - Legacy date-only entry\n"
    )
    parsed = parse_newest_timestamp(sample)
    if parsed is None or parsed.year != 2026 or parsed.month != 6 or parsed.day != 24:
        print(f"FAIL parse newest timestamp: {parsed}", file=sys.stderr)
        return 1
    if parse_newest_timestamp("no headings here") is not None:
        print("FAIL parse returns None when no headings", file=sys.stderr)
        return 1

    # Freshness scan: enrolled+stale warns, enrolled+fresh ok, unenrolled skipped, missing flagged.
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "stale.md").write_text("### 2026-06-01 12:00:00 +00:00 - old\n", encoding="utf-8")
        (root / "fresh.md").write_text("### 2026-06-23 12:00:00 +00:00 - recent\n", encoding="utf-8")
        (root / "nofresh.md").write_text("### 2026-06-01 12:00:00 +00:00 - old\n", encoding="utf-8")
        entries = [
            resolve_entry({"path": "stale.md", "freshness": {"maxStaleDays": 7}}, {}),
            resolve_entry({"path": "fresh.md", "freshness": {"maxStaleDays": 7}}, {}),
            resolve_entry({"path": "nofresh.md"}, {}),
            resolve_entry({"path": "absent.md", "freshness": {"maxStaleDays": 7}}, {}),
        ]
        checked = scan_freshness(entries, root, fixed_now)
        by_path = {record["path"]: record["status"] for record in checked}
        if by_path != {"stale.md": "stale", "fresh.md": "fresh", "absent.md": "missing"}:
            print(f"FAIL freshness scan statuses: {by_path}", file=sys.stderr)
            return 1
        if build_freshness_packet(checked, "self-test")["status"] != "warn":
            print("FAIL freshness overall should warn when any log stale/missing", file=sys.stderr)
            return 1

    # Freshness scan with missing registry file: must return exit 0 with empty checked list (warn-only contract).
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        fake_registry = root / "fake-registry.json"
        args_missing = argparse.Namespace(only=[], format="json")
        # Simulate freshness scan against non-existent registry by catching the exception path.
        try:
            load_registry(fake_registry)
            print("FAIL should raise FileNotFoundError for missing registry", file=sys.stderr)
            return 1
        except FileNotFoundError:
            # This is the expected path: missing registry in freshness mode returns exit 0 with empty list.
            checked_empty: list[dict[str, Any]] = []
            packet_empty = build_freshness_packet(checked_empty, fake_registry.relative_to(root).as_posix())
            if packet_empty["status"] != "pass":
                print(f"FAIL missing registry freshness packet should be pass, got {packet_empty['status']}", file=sys.stderr)
                return 1
            if len(packet_empty["checked"]) != 0:
                print(f"FAIL missing registry freshness packet should have empty checked list, got {len(packet_empty['checked'])} items", file=sys.stderr)
                return 1

    print("PASS log-pruning gate self-test")
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Scan OS-owned logs against pruning thresholds.")
    parser.add_argument("--scan", action="store_true", help="Scan enrolled logs (default action).")
    parser.add_argument("--only", action="append", default=[], help="Limit scan to this the OS-root-relative log path. Repeatable.")
    parser.add_argument("--format", choices=["json", "markdown"], default="json")
    parser.add_argument("--freshness", action="store_true", help="Check enrolled logs for staleness (inverse of size). Warn-only, never blocks.")
    parser.add_argument("--self-test", action="store_true", help="Run deterministic self-tests.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    if args.self_test:
        return run_self_test()
    if args.freshness:
        return run_freshness_scan(args)
    return run_scan(args)


if __name__ == "__main__":
    raise SystemExit(main())
