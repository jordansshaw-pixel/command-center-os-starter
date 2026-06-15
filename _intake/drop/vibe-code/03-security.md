# 03 — Security

> Load this file during implementation, code review, and before any deployment.

---

## Secrets and Credentials

- **Never commit API keys, secrets, tokens, or credentials.** Use environment variables via `.env` files. Ensure `.env` is in `.gitignore`.
- **Store a `.env.example`** with all required variable names but no values. Keep it updated as new variables are added.
- **Never log sensitive data.** No API keys, tokens, passwords, session IDs, or PII in `console.log`, server logs, or any logging output.

  _Why: A single committed secret can be scraped from git history even after deletion. Logs are often stored in plain text and accessible to anyone with server access._

---

## Input Validation

- **Validate all user input server-side.** Always. Without exception.
- **Client-side validation is a UX convenience, not a security gate.** Never treat it as one.
- **Sanitize inputs before using them in queries, templates, or shell commands.** Never interpolate raw user input.

  _Why: Any client-side validation can be bypassed. The server is the only trusted surface._

---

## Database

- **Enable Row-Level Security (RLS) on every database table.** No exceptions.
- **Every table with user data must have RLS policies** that scope reads and writes to the authenticated user's own data.
- **Review RLS policies explicitly** before shipping any table. Do not assume it works — test it with a second user account.

  _Why: Without RLS, any authenticated user can potentially read or modify any row. RLS is the last line of defense against data leakage._

---

## Transport

- **Use HTTPS for all external API calls.** No HTTP, ever.
- **Do not disable SSL verification** in any environment, including local development.

---

## Dependencies

- **Run `npm audit` (or equivalent) regularly.** Do not ignore critical or high-severity vulnerabilities.
- **Before installing a new dependency, check:** Is it actively maintained? Does it have known vulnerabilities? Can this be built in-house in under 50 lines?

---

## Pre-Deploy Security Checklist

- [ ] No secrets in committed files (`git log --all -S "secret_value"` if unsure)
- [ ] `.env` is in `.gitignore`
- [ ] `.env.example` is complete and up to date
- [ ] RLS enabled and tested on all tables
- [ ] All user inputs validated server-side
- [ ] `npm audit` run with no critical issues outstanding

---

## → Where to Go Next

Pre-deploy checklist fully passed?
→ Load `10-checkpoints.md` — run the full "done" checklist before shipping

Security issues found (exposed secrets, missing RLS, validation gaps)?
→ Fix them now. Do not continue feature work until the checklist is clean.

Still in the implementation phase?
→ Return to `02-code-quality.md` and continue building
