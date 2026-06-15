# Route Card: Operator Onboarding

Status: active runtime card
Edition: Community / distributable starter

## Trigger

First run, or any time `_operator/OPERATOR-TRUTHS.md` / `OPERATOR-VOICE.md` are still empty scaffolds,
or `_memory/SESSION-BOOT-STATE.md` still shows the fresh-install open loop. Detect this before
substantial work and route here first.

## Load Next

- `_operator/OPERATOR-TRUTHS.md`
- `_operator/OPERATOR-VOICE.md`
- `_operator/OPERATOR-APPROVAL-STANDARD.md`
- `_agents/keeper/doctrine/memory-relevance.md`
- `_governance/brand-guardian.md` (only if a truth/proof boundary comes up during the interview)

## Required Roles

Conductor (sequence the interview), Keeper (decide what becomes durable memory), Steward / Brand
Guardian (label truth/approval state). Voice captures expression preferences.

## Interview

Ask the operator, one cluster at a time, and write confirmed answers into the named files:

1. **Identity** → `OPERATOR-TRUTHS.md`: name/handle to use, role, and what they build.
2. **Ventures & clients** → `OPERATOR-TRUTHS.md`: capture each venture/client lane as a name (and a one-
   line intent). Root records only the lane. The full **venture harness** — the venture's own memory,
   routing, connectivity, governance, and stage spine — is installed into the venture's folder by the
   agent when the venture is created, via `routes/project-scaffold.md`. Do not put venture working data
   in root.
3. **Standards & non-negotiables** → `OPERATOR-TRUTHS.md`: quality bars and hard rules.
4. **Boundaries** → `OPERATOR-TRUTHS.md` + `_connectivity/`: do-not-touch zones, live-system limits.
5. **Voice** → `OPERATOR-VOICE.md`: cadence, words that build/erode trust, how to be challenged.
6. **Approval posture** → confirm or adjust `OPERATOR-APPROVAL-STANDARD.md` defaults.

Label every captured truth with its approval state (user-confirmed, source-confirmed, inferred,
provisional). Do not invent operator truths; ask.

## Output

- Populated `_operator/OPERATOR-TRUTHS.md` and `OPERATOR-VOICE.md`.
- Rewritten `_memory/SESSION-BOOT-STATE.md` reflecting real current state (remove the first-run loop).
- A first decision-log entry in `_memory/decision-log.md` recording that onboarding completed.
- Handoff to the normal `ROUTE-INDEX` cards.

## Stop Conditions

Do not store secrets or credentials in `_operator/` or memory. Do not generalize a single answer into
universal law without confirmation. Do not skip onboarding and guess the operator's identity.

## Next

After onboarding, classify real work through the smallest matching card in `ROUTE-INDEX.md`. Suggest
proving one route end-to-end on the sample project in `_examples/` before adding live projects.
