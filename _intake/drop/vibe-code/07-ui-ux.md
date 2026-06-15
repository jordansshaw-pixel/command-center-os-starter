# 07 — UI/UX & Copy Standards

> Load this file when building or reviewing frontend components and user-facing copy.

---

## Visual Design Rules

- **No emojis in the UI.** Not in buttons, headings, labels, or notifications. Zero.
- **No glassmorphism.** No gratuitous gradients. No purple-dominant palettes.
- **Use a spacing scale and stick to it.** Example: 4 / 8 / 12 / 16 / 24 / 32 / 48px. Do not use arbitrary values.
- **One font family maximum.** Two if the project requires distinct heading and body treatments. Never more.
- **Sufficient contrast required.** Text must pass WCAG AA contrast ratio against its background. Test both light and dark themes if the project supports them.

  _Why: Inconsistent spacing and low contrast are the most common reasons a UI "feels off" even when individual components look fine._

---

## State Requirements

Every async operation and every component that can fail must have both:

- **A loading state** — spinner, skeleton, or progress indicator. Never leave the user looking at a blank or frozen screen.
- **An error state** — visible, user-facing, and actionable. Not just `console.error`. The user must be able to see what happened and know what to do next.

  _Why: Users interpret no feedback as broken. Silent failures are the worst UX — the user doesn't know what happened and has no path to recover._

---

## Copy Rules

- **Every word earns its place.** If you can cut a word without losing meaning, cut it.
- **No placeholder copy in committed code.** No "Lorem ipsum," "Your amazing feature," "TODO: add copy here."
- **No AI-sounding filler phrases.** Ban list: leverage, streamline, empower, cutting-edge, revolutionary, seamless, robust solution, take it to the next level, unlock your potential, game-changer.
- **CTAs must be specific.** Not "Get Started" — "Start Free Trial," "Book a Demo," "Download the Report." The user must know exactly what clicking will do.
- **No fabricated social proof.** No invented testimonials, inflated user counts, or made-up case studies. If real proof doesn't exist, the section doesn't exist.
- **No em-dash overuse.** One per page maximum. Restructure the sentence instead.

  _Why: Vague copy and fake social proof erode trust the moment a user looks closely._

---

## Copy Tone

Copy should be direct, specific, and human. It should sound like a competent person wrote it, not like a marketing generator. When in doubt: shorter, plainer, more specific.

---

## → Where to Go Next

Frontend components built?
→ Load `05-testing.md` — write at least one integration test that simulates a user going through the full UI flow

Performance concerns (slow renders, large bundle)?
→ Load `08-performance.md`

Copy and UI complete and reviewed?
→ Load `10-checkpoints.md` — run the done checklist before committing
