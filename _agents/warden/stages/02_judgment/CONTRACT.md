# Warden Judgment Stage

Status: Initial stage contract
Date: 2026-06-05

## Purpose

Decide whether movement is allowed, blocked, or approval-bound.

## Required Checks

- Is this live?
- Is this secret or credential-bearing?
- Is this reversible?
- Has the operator approved the action?
- Does Sentinel score this as critical?

## Output

- Boundary judgment.

## Exit

Move to `03_output`.

