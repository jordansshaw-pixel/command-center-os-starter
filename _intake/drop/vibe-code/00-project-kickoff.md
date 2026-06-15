# 00 — Project Kickoff

> Load this file at the start of a new project. Once kickoff is complete, switch to the relevant phase files.

---

## Before Writing Any Code

1. **Confirm a project plan exists.** If it doesn't, create one before touching any code. The plan must include:
   - What is being built and who it's for
   - Core features (in scope) and explicit non-features (out of scope)
   - Tech stack (reference `tech-stack.md`)
   - Build order: which pieces get built first and why

   _Why: Every hour spent clarifying before building saves three hours of untangling after._

2. **Create a project-specific `AGENTS.md`** (or confirm one exists). It must specify:
   - Tech stack details for this project (even if they match `tech-stack.md` defaults — confirm it)
   - Directory structure
   - Naming conventions that deviate from the global rules
   - Any API patterns specific to this codebase

   _Why: Without project-level rules, the agent makes assumptions. Wrong assumptions compound._

3. **Review the plan before building.** Explicitly ask: "What in this plan is too complex for phase 1? What can be deferred?" Cut it before writing a line.

   _Why: The cheapest time to remove scope is before any code exists._

4. **Break the plan into numbered sections.** Each section is a discrete unit of work that ends in a commit. Sections should not depend on unfinished sections.

   _Why: Section-by-section execution produces a checkpointable, rollback-able build history._

---

## Kickoff Checklist (Human Signs Off Before Build Starts)

- [ ] Plan document exists and has been reviewed
- [ ] Out-of-scope items are explicitly listed
- [ ] `AGENTS.md` created and reviewed
- [ ] Tech stack confirmed in `AGENTS.md`
- [ ] Build order defined and makes sense
- [ ] Repo initialized with correct branch structure (`main` protected)
- [ ] `.env.example` created with all required variable names

**Kickoff is complete when all boxes are checked. Not before.**

---

## → Where to Go Next

Kickoff checklist fully signed off?
→ Load `01-git-and-versioning.md` — initialize the repo and branch structure

Stack not yet confirmed?
→ Load `tech-stack.md` first, then return here to complete the checklist

Project has a Python backend?
→ After `01-git-and-versioning.md`, also load `stack-rules/python-standards.md`

Ready to start building the first section?
→ Load `02-code-quality.md` + `06-api-standards.md` (if the section touches any API endpoints)
