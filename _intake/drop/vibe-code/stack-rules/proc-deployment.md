# proc-deployment.md — Deployment Process

> Load this file when shipping to production for the first time, or when modifying the deployment pipeline.
> Assumes Vercel for frontend and Railway or Fly.io for backend per `tech-stack.md`.
> Document any deviations in `AGENTS.md`.

---

## Before Any Deployment

Run this checklist in full. Do not deploy with unchecked items.

- [ ] All tests pass locally: `npm test` or equivalent
- [ ] TypeScript compiles clean: `tsc --noEmit`
- [ ] No `console.log` statements left in production code paths
- [ ] All environment variables documented in `.env.example`
- [ ] Security checklist from `03-security.md` passed
- [ ] `npm audit` — no critical vulnerabilities
- [ ] Feature branch merged to `main` with a clean commit history
- [ ] Database migrations (if any) reviewed and tested on a staging environment first

---

## Environment Variable Management

- **Never copy `.env` to the server directly.** Set environment variables through the platform's dashboard or CLI.
- **Use separate variable sets for each environment:** `development`, `staging`, `production`. They should not share secrets.
- **Rotate secrets on every new environment setup.** The key you used in development is not the key you use in production.
- **After adding a new variable, update `.env.example` immediately** — before deployment, not after.

---

## Frontend Deployment — Vercel

### First Deploy
```bash
npm install -g vercel
vercel login
vercel --prod    # from project root
```

### Ongoing
- **Vercel auto-deploys from `main` on push** once connected to the repo. Confirm this is configured in the Vercel dashboard.
- **Preview deployments are automatic for all branches.** Use them. Every PR gets a live URL — test on it before merging.
- **Set environment variables in Vercel dashboard** under Project → Settings → Environment Variables. Set separately for Production, Preview, and Development.
- **`NEXT_PUBLIC_` variables must be set in Vercel** — they're embedded at build time, not runtime.

### Build Checks
After each production deploy:
1. Check the Vercel build log for warnings
2. Open the deployed URL — confirm it loads
3. Test the critical user flow end-to-end on production (not just preview)

---

## Backend Deployment — Railway

### First Deploy
1. Create a new project in the Railway dashboard
2. Connect your GitHub repo
3. Set environment variables under Variables tab
4. Railway auto-detects `Dockerfile` or buildpacks. For FastAPI: ensure `Procfile` or start command is set:
   ```
   web: uvicorn src.main:app --host 0.0.0.0 --port $PORT
   ```

### Ongoing
- **Railway auto-deploys from `main` on push.** Confirm this is the intended behavior — for some projects, manual deploy on production is safer.
- **Set a health check endpoint.** Railway will monitor it. If it fails, the deploy is rolled back automatically.
  ```python
  # FastAPI health check
  @app.get("/health")
  async def health():
      return {"status": "ok"}
  ```
- **Review resource usage after each deploy.** Railway shows memory and CPU. An unexpected spike means something is wrong.

### Rollback
If a deploy is bad: Railway dashboard → Deployments → select previous deploy → Redeploy. Takes ~60 seconds.

---

## Database Migrations

- **Never run migrations directly against production without testing on staging first.**
- **Every migration must be reversible.** Write the down migration before the up migration ships.
- **Migrations are run as a deploy step, not manually.** Wire them into your deploy command or Railway start command:
  ```
  alembic upgrade head && uvicorn src.main:app --host 0.0.0.0 --port $PORT
  ```
- **Back up the database before any destructive migration** (column removal, table drop, data transformation).

---

## Post-Deploy Verification

After every production deploy, verify:

1. **Health check endpoint returns 200** — `curl https://your-api.railway.app/health`
2. **Critical user flows work end-to-end** — sign in, core feature, any payment flow
3. **Error tracking shows no new spike** — check Sentry or your logging platform
4. **API response times are within the 50ms ceiling** — spot check in browser network tab

If any of these fail: **roll back immediately**, then debug. Do not leave a broken production deploy running while you investigate.

---

## Monitoring (Minimum Viable)

- **Error tracking:** Sentry (free tier is sufficient for most projects). Set it up before first production deploy, not after the first incident.
- **Uptime monitoring:** BetterUptime or UptimeRobot — monitors your health endpoint and pages you if it goes down.
- **Log access:** Railway and Vercel both expose logs in the dashboard. Know where they are before you need them.

---

## → Where to Go Next

Deploy successful and post-deploy verification passed?
→ You're done. Commit any deploy config changes with `chore(deploy): <what changed>`

Deploy failed?
→ Roll back immediately. Load `04-debugging.md`. Do not debug on a live broken production environment.

First time setting up monitoring?
→ Set up Sentry and UptimeRobot before moving on. Monitoring is not optional for production.

Database migration caused issues?
→ Run the down migration to restore the previous schema. Load `04-debugging.md` to identify the problem before re-attempting.
