# 08 — Performance

> Load this file during implementation and before deployment.

---

## Dependencies

- **Before installing a library, ask:** Can this be built in under 50 lines? If yes, build it.
- **Every new dependency is a maintenance burden, a security surface, and a bundle size increase.** Treat installation as a cost, not a shortcut.

---

## Frontend

- **Lazy load heavy components and routes.** The settings page should not load on the homepage.
- **Debounce search inputs and any input that triggers expensive operations.** 300ms is a reasonable default. Do not fire an API call on every keystroke.
- **Optimize images:** compress, serve in WebP, lazy load below-the-fold images.
- **All async operations must have loading and error states.** No unhandled promises. No silent failures.

  _Why: Unhandled promises produce bugs that are nearly impossible to trace. Initial page load speed directly affects user retention._

---

## API Performance

API response time rules live in `06-api-standards.md`. The 50ms ceiling applies to all synchronous endpoints. Long-running tasks must use the async job pattern described there.

---

## What to Measure

Before and after any significant change, verify:

- Lighthouse score on the key pages (aim for 90+ on Performance)
- API response times in the network tab
- Bundle size delta (run `npm run build` and compare)

---

## → Where to Go Next

Performance review complete and numbers are acceptable?
→ Load `10-checkpoints.md` — finalize and commit

API response times failing the 50ms ceiling?
→ Load `06-api-standards.md` — implement the async job pattern

Bundle size or render performance is the issue?
→ Audit lazy loading and dependency usage in this file, then re-measure before committing
