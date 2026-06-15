# 04 — Debugging Protocol

> Load this file when a feature or fix is not working and multiple attempts have failed.
> This is a human-executed protocol, not a set of instructions for the AI to follow mid-task.

---

## The Core Principle

Debugging is a discrete phase. It is not interleaved with feature implementation. When something is broken, stop building and switch into debug mode with a clear, isolated prompt.

---

## Step 1: Isolate Before You Fix

Before attempting another fix, answer these questions in writing:

1. What exact behavior is observed? (Not "it's broken" — what specifically happens?)
2. What behavior is expected?
3. What is the smallest reproduction case? Can this be tested in isolation, outside the main codebase?
4. What has already been tried? What did each attempt change?

Do not write another fix until you can answer all four.

  _Why: Most failed debugging attempts fail because the problem is not yet understood. Writing the answers forces clarity._

---

## Step 2: The 3-Attempt Reset Rule

**This is a human-executed rule, not an AI instruction.**

If the AI has made 3 or more attempts at fixing the same issue and the code is getting more complex with each attempt:

1. **Stop.** Do not prompt again.
2. Run `git reset --hard <last-good-commit-hash>` to return to a clean, known-working state.
3. Identify the last commit hash where the feature worked: `git log --oneline`
4. Re-approach with a single, specific prompt that includes:
   - The exact error message or unexpected behavior
   - The relevant file(s) and function(s) only
   - What you know the cause is NOT (eliminating dead ends from prior attempts)
   - The specific thing you need changed

  _Why: Language models accumulate context from previous attempts. Failed fixes add noise that degrades the quality of subsequent attempts. A clean state and a precise prompt almost always outperforms a sixth attempt on a dirty codebase._

---

## Step 3: Isolation Test

For complex bugs:

1. Create a standalone file or minimal project that reproduces the issue
2. Test the specific behavior in isolation, with no other dependencies
3. Fix the isolated case first
4. Then bring the fix back into the main codebase

  _Why: Complex systems have complex interactions. Isolation removes noise so you can find the signal._

---

## What the AI Output Should Look Like During Debugging

When the AI is in debug mode, its output should include:

- The specific thing it identified as wrong
- The specific change it made and why
- What to observe to confirm the fix worked

If an AI response during debugging includes phrases like "I've also improved..." or "I also refactored..." — discard the output and re-prompt with explicit scope constraints. The debug prompt should specify: "Only fix X. Do not touch anything else."

---

## Common Failure Modes to Check First

- Environment variable missing or incorrect value
- Import path wrong or circular
- Wrong async/await pattern (missing `await`, not handling rejection)
- Type mismatch caught only at runtime
- Cache not invalidated after a schema or config change
- RLS policy blocking a query silently

---

## → Where to Go Next

Bug is isolated and fixed, and you've reset to a clean git state?
→ Load `01-git-and-versioning.md` — commit the fix with a proper `fix(<scope>):` message

Fix required changes to API behavior or response shape?
→ Also load `06-api-standards.md` to confirm the fix still meets the response contract

Fix introduced new logic that needs tests?
→ Load `05-testing.md`

Issue turned out to be architectural (not a one-line fix)?
→ Stop. Flag it for the human orchestrator. Do not architect a solution mid-debug.
