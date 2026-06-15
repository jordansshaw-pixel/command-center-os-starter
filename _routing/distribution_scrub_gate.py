#!/usr/bin/env python3
"""Distribution scrub gate.

Maintainer-only denylist gate for the canonical template repo. Fails (exit
non-zero) if any operator-identifying data, venture/client name, private infra
URL, local machine path, or Transformers IP role name reappears in the tree.

This is intentionally NOT part of the end-user gate suite (run_gates.py): the
denylist is tuned to the upstream author's data, so wiring it into the template
members receive would fail their CI on legitimate content (e.g. a member named
"Jordan", or a doc that uses the word "caliber"). It runs only on the canonical
repo via .github/workflows/distribution-scrub.yml, and standalone for maintainers:

    python _routing/distribution_scrub_gate.py            # scan (default)
    python _routing/distribution_scrub_gate.py --self-test # verify the gate itself

The lowercase `atx_` / uppercase `ATX_` engine namespace (code identifiers and
`atx_*.py` / `atx-*.yml` filenames) is intentionally allowed and NOT flagged.
"""
from __future__ import annotations

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEXT_EXT = {".md", ".json", ".py", ".js", ".ps1", ".sh", ".bat", ".yml", ".yaml", ".txt", ".html"}

# Files that legitimately contain denylist tokens: this gate's own source, build-time
# migration scripts, and the maintainer scrub workflow (whose repo-name guard must name
# the canonical upstream repo, i.e. the owner login).
def _skip_file(name: str) -> bool:
    return (
        name.startswith("_migration_")
        or name == "distribution_scrub_gate.py"
        or name == "distribution-scrub.yml"
    )

# Case-insensitive substring patterns (unambiguous, safe as substrings).
SUBSTRING = [
    "jordan", "jshaw", "jordansshaw",
    "caliberg", "cliefnotes", "lgaipro", "hokulani", "safetycall",
    "solutionsfactory", "lookingglass", "atx-env-vault",
    "atx command center", "seatac",
]
# Word-boundary patterns (short or substring-prone tokens).
BOUNDED = [
    "ecma", "cga", "lgw", "base44", "caliber", "skool",
    # Transformers IP role names:
    "optimus", "ultra magnus", "ultra-magnus", "teletraan", "kup", "rewind",
    "prowl", "ironhide", "jazz", "perceptor", "trailbreaker", "skids",
    "wheeljack", "ratchet", "strongarm", "bumblebee", "hound", "blaster",
]
# Local machine paths (any username) — a real leak vector regardless of who built it.
# Scoped to user-home roots so generic placeholder paths (e.g. C:\path\to\...) are not flagged.
PATH_REGEX = [
    ("<windows-user-path>", re.compile(r"[A-Za-z]:\\Users\\[^\\/\s\"'<>|]+", re.IGNORECASE)),
    ("<unix-home-path>", re.compile(r"/(?:home|Users)/[A-Za-z0-9._-]+", re.IGNORECASE)),
]

def build_patterns():
    pats = [(t, re.compile(re.escape(t), re.IGNORECASE)) for t in SUBSTRING]
    pats += [(t, re.compile(r"\b" + re.escape(t) + r"\b", re.IGNORECASE)) for t in BOUNDED]
    pats += PATH_REGEX
    return pats

def scan() -> int:
    pats = build_patterns()
    hits = []
    for dp, dirs, fns in os.walk(ROOT):
        # exact-component skips (so .github / .githooks ARE scanned)
        dirs[:] = [d for d in dirs if d not in (".git", "__pycache__", "node_modules", ".wrangler")]
        for fn in fns:
            ext = os.path.splitext(fn)[1].lower()
            # Scan known text extensions AND extensionless files (shell hooks like
            # .githooks/pre-commit, LICENSE, .gitignore). Binary reads are skipped below.
            if _skip_file(fn) or not (ext in TEXT_EXT or ext == ""):
                continue
            p = os.path.join(dp, fn)
            try:
                lines = open(p, encoding="utf-8").read().splitlines()
            except (UnicodeDecodeError, OSError):
                continue
            for i, line in enumerate(lines, 1):
                for token, rx in pats:
                    if rx.search(line):
                        rel = os.path.relpath(p, ROOT).replace("\\", "/")
                        hits.append((rel, i, token, line.strip()[:120]))
    if hits:
        print(f"distribution scrub gate: FAIL ({len(hits)} forbidden token(s) found)", file=sys.stderr)
        for rel, i, token, snippet in hits[:80]:
            print(f"  {rel}:{i}  [{token}]  {snippet}", file=sys.stderr)
        if len(hits) > 80:
            print(f"  ... and {len(hits) - 80} more", file=sys.stderr)
        return 1
    print("distribution scrub gate: pass (no forbidden tokens)")
    return 0

def self_test() -> int:
    pats = build_patterns()
    def flagged(text: str) -> bool:
        return any(rx.search(text) for _t, rx in pats)
    # known-bad must flag
    for bad in ["Jordan Shaw", "CaliberGrowthAgency", "Optimus Prime", " Kup ", "ECMA website",
                r"C:\Users\Coco\Command Center", "/home/alice/repo", "/Users/dev/project"]:
        if not flagged(bad):
            print(f"FAIL scrub-gate self-test: missed '{bad}'", file=sys.stderr)
            return 1
    # known-good must NOT flag (engine namespace + placeholders + safe words/paths)
    for good in ["atx_hook_runner.py", "ATX_ROOT", "backup lookup markup", "the operator",
                 "Command Center OS", "Steward Conductor Keeper", "ECMAScript",
                 r"C:\path\to\command-center-os", "_examples/sample-project/.env.local"]:
        if flagged(good):
            print(f"FAIL scrub-gate self-test: false positive on '{good}'", file=sys.stderr)
            return 1
    print("PASS distribution scrub gate self-test")
    return 0

def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if "--self-test" in argv:
        return self_test()
    return scan()

if __name__ == "__main__":
    raise SystemExit(main())
