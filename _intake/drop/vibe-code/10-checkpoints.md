# 10 — Checkpoints & Refactoring

> Load this file when completing a section of the build plan or running a refactor pass.

---

## Checkpoint Protocol

After completing each section of the build plan, stop and run through this sequence:

1. **Does it work end-to-end?** Test the full user flow, not just the piece you just built.
2. **Are error states handled?** What happens when it fails? Is that visible to the user?
3. **Are loading states present?** Does the user know when an async operation is in progress?
4. **Is the code committed?** If not, commit now with a proper Conventional Commit message.
5. **Are docs updated?** If this section changed anything documented in `AGENTS.md` or `README.md`, update them now.

Only after all five are checked does this section count as done.

---

## Definition of "Done"

A feature is done when all of the following are true — not some of them, all of them:

- [ ] Works end-to-end on a real device or environment (not just `localhost:3000`)
- [ ] Error states are implemented and visible to the user
- [ ] Loading states are implemented for every async operation
- [ ] At least one integration test exists and passes
- [ ] Code is committed with a clean git history (no WIP commits, no commented-out code)
- [ ] Docs are updated if anything architectural changed

"Almost done" is not done. "Just needs cleanup" is not done. Done means the checklist is checked.

---

## Refactoring Rules

- **Refactor when it works, not when it's broken.** Once a feature is functional, ask: Is any logic duplicated? Are any files too large? Could this be simpler?
- **Refactor as a discrete pass.** Do not mix refactoring with new feature work. They get separate commits.
- **Refactor commit format:** `refactor(<scope>): <what changed and why>`

  _Why: Refactoring broken code adds complexity. Refactoring working code improves it. Mixing the two makes both impossible to review._

---

## Periodic Refactor Scan

At natural break points (end of a phase, before starting a major new section), scan for:

- Files over 300 lines
- Functions over 50 lines
- Logic that appears in two or more places
- Modules that have grown to do more than one thing

Flag these. Schedule them as refactor tasks in the build plan. Don't fix them during feature work.

---

## → Where to Go Next

Done checklist fully checked?
→ Load `01-git-and-versioning.md` — commit and push with a proper Conventional Commit message, then merge to `main`

Done checklist has unchecked items?
→ Do not proceed. Go back to the relevant file:
- Missing tests → `05-testing.md`
- Missing error/loading states → `07-ui-ux.md`
- Security item unchecked → `03-security.md`
- Docs not updated → `09-documentation.md`

Refactor candidates identified during the scan?
→ Log them in `AGENTS.md` under a `## Refactor Queue` section. Address in the next dedicated refactor pass, not now.
