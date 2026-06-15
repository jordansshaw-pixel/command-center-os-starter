# Phase 1 Gate-Hardening Reference

> **Classification: root technical reference evidence. NOT authority.**
> the operator reclassified this intake item on 2026-06-13 as a durable reference for
> future clarity on how and why the Phase 1 live-system gate upgrade was built.
> This file is evidence only. It is not a contract, standard, route card,
> doctrine, decision, memory source, or authorization to build. The authoritative
> implementation state remains in the committed gate files, route cards,
> handoffs, and memory entries that record the completed work.

---

Date staged: 2026-06-13
Staged by: Owner request
Subject: Item 3 (live-system completeness gate) build kickoff — reference copy

The text below is a copy of the Codex kickoff prompt prepared for Item 3. It is
reproduced here solely as Owner reference. It is NOT authorization to build, and
nothing in the OS should act on it. Authorization, routing, and memory remain the
Owner's to direct separately.

---

## Item 3 — Live-System Completeness Gate (kickoff prompt, reference only)

Load the OS runtime Tier 0 first, per AGENTS.md: CLAUDE.md, CONTEXT.md,
_memory/SESSION-BOOT-STATE.md, _routing/runtime/ROUTING-KERNEL.md,
_routing/runtime/ROUTE-INDEX.md, _memory/runtime/MEMORY-KERNEL.md,
_memory/runtime/LOAD-INDEX.md. Then classify through routes/live-system.md AND
routes/role-engagement.md, and load the Warden boundary lens, because this
builds and wires a gate on the live-system boundary. This is the highest-risk
Phase 1 item.

Scope: implement Item 3 from
_handoffs/phase-1-gate-hardening-build-handoff.md, with the operator decisions
below. Items 1, 2, and 2.5 are complete. This is the LAST Phase 1 item.

OPERATOR DECISIONS RESOLVED (build to these, do not re-ask):
- Packet format: JSON. Parse with the Python standard-library json module ONLY.
  Do NOT add pyyaml or any third-party dependency — this must preserve the Item
  2.5 portability contract (the OS gates depend on Python >=3.10 and nothing else).
  The JSON choice is scoped to THIS gate only; do NOT introduce any global
  'JSON for rules' convention or record one.
- Scope: build the gate AND wire it into routes/live-system.md in this pass.

NON-NEGOTIABLE SAFETY PROPERTY (this is the whole point of the item):
The gate validates that a live-system packet is COMPLETE and INTERNALLY
CONSISTENT. It MUST NEVER be treated as APPROVAL. A passing gate means 'this
packet has all required fields and they are consistent' — it does NOT mean the
action is authorized. Warden hard stops and explicit the operator approval remain
mandatory and sit DOWNSTREAM of the gate, unchanged. If any code, output string,
comment, or route-card wording could let a reader interpret gate-pass as
authorization, that is a build failure. The gate's only outputs are: eligible
(yes/no) + a list of blockers/missing fields. It never emits anything resembling
'approved' or 'cleared to proceed'.

CANONICAL FIELD SOURCE:
The required fields are defined in _connectivity/live-system-risk-rules.md under
'Required Live-System Packet'. Use THAT list as the source of truth (System,
Scope, Requested action, Current source, Owner, Permission class, Risk score,
Approval required, Approval status, Credential handling, Rollback path, Blocked
actions, Allowed safe actions, Next action). Note: routes/live-system.md
currently names a SHORTER paraphrase in its Output line — do NOT validate against
the route card's short list; validate against the full standard. If the two
drift, the gate should treat live-system-risk-rules.md as authoritative.

BUILD — in dependency order:

1. Create _routing/atx_live_system_gate.py, mirroring the structure and
   conventions of _routing/atx_fast_lane_gate.py (same argparse style, same
   exit-code convention: 0 = eligible/complete, 2 = blocked):
   - Accept a live-system packet as a JSON file path (e.g. --packet path.json)
     or JSON on stdin.
   - Parse with stdlib json only.
   - Verify EVERY required field from live-system-risk-rules.md is present and
     non-empty.
   - Consistency checks (presence/form only, NOT judgment): if Approval status
     indicates approved, then Approval required, Owner, and Rollback path must be
     present and non-empty; Risk score must be an integer 0-4; if Risk score is
     4, scope-down/blocked-actions handling must be present. Define an explicit
     allowed set for Approval status (e.g. blocked, pending, approved) and reject
     unknown values.
   - On success: print a result object with eligible: yes plus the validated
     field summary. On failure: eligible: no plus named blockers. NEVER print
     anything that reads as approval.
   - Exit 0 if complete+consistent, 2 otherwise.
   - Include --self-test covering: complete approved packet (eligible), missing
     Rollback path (blocked), approved status with empty Owner (blocked), Risk 4
     with no scope-down (blocked), unknown Approval status value (blocked),
     malformed JSON (blocked with a clear parse error, not a traceback).
   - The gate MUST NOT perform, trigger, or authorize any live-system action. It
     only reads and validates a packet file.

2. Add the new gate to the canonical runner _routing/run_gates.py so its
   --self-test runs alongside the others (extend the CHECKS table; update the
   self-test count guard if present). Do NOT change the other checks.

3. Wire into _routing/runtime/routes/live-system.md — as a PRECONDITION, not a
   permission:
   - Add the gate to 'Load Next' / reference it in the card.
   - State explicitly in the card: a FAILED gate is a hard stop (incomplete
     packet cannot proceed); a PASSED gate ONLY advances the work to the existing
     Warden + the operator approval step — it does NOT authorize the action and is
     NOT approval. Use wording that makes gate-pass a filter, never a green light.
   - Do NOT change the card's existing Required Roles, Stop Conditions (risk 4
     until scoped, the operator approval required), or escalation. Add the gate as an
     additional early completeness check, leave all human/Warden authority
     intact.

Acceptance test (report results explicitly):
- python _routing/atx_live_system_gate.py --self-test prints PASS and covers
  every case above.
- A hand-written complete approved packet validates (eligible: yes). Removing
  each single required field in turn produces a block naming that field.
- An approved-status packet with an empty Owner or missing Rollback path BLOCKS.
- Risk score 4 with no scope-down handling BLOCKS.
- Unknown Approval status value BLOCKS.
- Malformed JSON BLOCKS with a readable error (no raw traceback).
- run_gates.py --self-test still passes with the new check included.
- Grep the gate source and the route-card edit for the strings
  'approved'/'authorize'/'cleared': confirm none of them are emitted as a gate
  verdict or implied by the wiring. Report what you found.
- The pre-commit hook passes on this clean change (normal commit). Report any
  --no-verify use.

Stop conditions / MUST NOT:
- MUST NOT let the gate perform, trigger, or authorize any live-system action.
- MUST NOT treat or word a passing gate as approval anywhere in code, output,
  comments, or the route card.
- MUST NOT add pyyaml or any third-party dependency; stdlib json only.
- MUST NOT introduce or record any global 'JSON for rules / YAML for skills'
  convention. JSON is scoped to this gate.
- MUST NOT change the substance of live-system-risk-rules.md rules, the route
  card's existing Required Roles / Stop Conditions / escalation, or any other
  gate's logic.
- MUST NOT touch live systems, credentials, or push. Pushing is the operator's
  action.
- MUST NOT add any bypass other than native git --no-verify.

Finalize: return a build-time-review output block (Trigger / Required lenses —
MUST include Warden and Theorist / Operating architecture / Boundary architecture
/ Risk / Signal / Build route / Memory impact / Next action). List all
changed/created files. Confirm every acceptance result, especially the grep for
approval-implying language. Record through _memory/MEMORY-ROUTER.md: the new
live-system completeness gate, its JSON format (scoped to this gate), and the
explicit non-authority property (gate-pass is never approval). Then STOP — this
completes Phase 1; do not begin Phase 2.

---

End of Owner reference material. Nothing above is system build authorization.
