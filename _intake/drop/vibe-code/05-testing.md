# 05 — Testing Standards

> Load this file when implementing features or running a test pass.

---

## Definition of "Tested"

A feature is tested when you can state all of the following:

- **What the test does** (the action being simulated)
- **What input it takes** (the specific data or user action)
- **What output it expects** (the exact assertion)

"I clicked it and it seemed to work" is not tested. That is manual observation, and it does not survive refactoring.

---

## Required Coverage per Feature

- **At least one integration test per feature.** Simulate a user going through the full flow end-to-end.
- **Happy path AND failure path.** What happens when: the API returns an error, the user submits an empty form, the network is down, the input is malformed?
- **Test error states explicitly.** Do not assume they work because the happy path works.

  _Why: Error handling is the difference between a crash and a graceful fallback. Users will hit every failure mode you don't test._

---

## Before Integrating Risky Features

- **Test in a standalone project first.** Build a minimal prototype that proves the concept works in isolation before touching the main codebase.
- **Download reference implementations when available.** If an API or library has example projects, verify they work before writing your integration.

  _Why: It's cheaper to throw away a standalone prototype than to untangle a failed integration from a live codebase._

---

## Test File Convention

- Test files live next to the code they test: `component.ts` → `component.test.ts`
- Test names describe the scenario: `"returns 401 when token is expired"`, not `"test auth"`
- Each test tests one thing. If a test has multiple unrelated assertions, split it.

---

## Running Tests

Tests must pass before any merge to `main`. If tests are failing:

1. Do not merge
2. Do not disable the failing test
3. Fix the code or update the test with a documented reason

  _Why: A disabled test is a lie in the test suite. It says "this works" when it doesn't._

---

## → Where to Go Next

Tests written and passing?
→ Load `10-checkpoints.md` — run the full "done" checklist before committing

Tests failing due to a bug (not a wrong test)?
→ Load `04-debugging.md`

Tests passing but you haven't run a security review yet?
→ Load `03-security.md` before merging
