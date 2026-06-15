# 02 — Code Quality Standards

> Load this file during implementation and code review passes.
> For Python-specific quality rules, also load `stack-rules/python-standards.md`.

---

## File and Function Size

- **Files: 300 lines maximum.** If a file exceeds this, split it into logical modules before continuing.
- **Functions: 50 lines maximum.** If a function is longer, extract helper functions with clear, specific names.

  _Why: Large files and long functions are hard for both humans and agents to reason about. They also signal that a module is doing too many things._

---

## Naming

- **Use descriptive names.** `getUserSalesMetrics()` not `getData()`. `isCallActive` not `flag`.
- **Be specific.** If you find yourself naming a variable `temp`, `data`, `info`, or `result`, rename it to describe what it actually contains.
- **Functions should describe what they do.** `parseWebhookPayload()`, `formatCurrencyDisplay()`, `validateEmailAddress()`.

  _Why: Code is read far more often than it's written. Clear names are documentation._

---

## TypeScript

- **No `any` types.** Define proper interfaces and types for everything.
- **No implicit `any`.** Enable `strict` mode in `tsconfig.json`. Do not disable it.
- **Type all function parameters and return values explicitly.**

  _Why: `any` defeats the purpose of TypeScript and hides exactly the bugs TypeScript exists to catch._

---

## Structure

- **DRY — Don't Repeat Yourself.** If the same logic appears in two or more places, extract it into a shared function or module before the third instance exists.
- **One module, one job.** Each module has a single responsibility with a clear interface.
- **External API integrations get their own module.** No inline API calls scattered across the codebase.
- **No hardcoded values.** Use constants, config files, or environment variables. The only acceptable literal strings in logic are things that will never change (e.g., HTTP methods).

---

## Cleanliness

- **No commented-out code in committed files.** Delete it. Git has the history.
- **No dead code.** Functions, variables, and imports that are not used get deleted, not commented out.
- **No placeholder values in committed code.** `"TODO: fill this in"`, `"your_api_key_here"`, and `"Lorem ipsum"` do not get committed. Ever.

  _Why: Commented code confuses everyone who reads it later — nobody knows if it's deprecated, broken, or intentional._

---

## What "Code Quality Pass" Means

A code quality pass is a discrete step, run separately from feature implementation. When doing a code quality pass:

1. Open only the files changed in this feature
2. Check each rule in this file explicitly
3. Do not add new functionality during a quality pass
4. Commit the quality pass separately: `refactor(<scope>): code quality pass`

  _Why: Mixing quality fixes with new features makes both harder to review and harder to roll back._

---

## → Where to Go Next

Implementing a feature that touches the database or auth?
→ Also load `03-security.md`

Implementing a feature with API endpoints?
→ Also load `06-api-standards.md`

Building frontend components?
→ Also load `07-ui-ux.md`

Feature implementation complete?
→ Load `05-testing.md` — write tests before marking anything done

Running a dedicated quality/refactor pass (no new features)?
→ Load `10-checkpoints.md` after this file

Using Python?
→ Also load `stack-rules/python-standards.md`
