# Librarian Judgment Stage

Status: Initial stage contract
Date: 2026-06-05

## Purpose

Decide where knowledge belongs and how it should be found later.

## Required Checks

- What owns this information?
- What file or folder should point to it?
- Is this duplicate, stale, missing, or unindexed?
- What future query should find it?
- Does this belong in Operator Canon, governance, memory, routing, a project file, or only a working output?
- If it touches Operator Canon, is the approval state user-confirmed, source-confirmed, inferred, or provisional?
- If this is a reference file, what is the nearest truth scope where it is true, reusable, and owned?
- What destination does Librarian recommend from the available file evidence before asking the operator?
- Would asking the operator to classify this create unnecessary operator load?
- If this came from `_intake/`, should the action be move, index, hold, or decision packet?
- What is the authority-triad state?
- Does routing belong to Conductor, memory judgment to Keeper, or truth authority to Steward / Brand Guardian before this can close?

## Output

- Placement or index judgment.
- Reference placement packet when the destination is not trivial.
- Authority-triad state for routing, memory judgment, and truth authority.

## Exit

Move to `03_output`.
