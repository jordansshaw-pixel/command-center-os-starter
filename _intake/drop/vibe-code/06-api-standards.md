# 06 — API Standards

> Load this file when designing or implementing API endpoints.

---

## Response Time Contract

- **All API endpoints must respond within 50ms.** This is a hard ceiling for synchronous responses.
- **If a task takes longer than 50ms, it must be handled asynchronously:**
  1. The endpoint receives the request and enqueues the job
  2. It returns `201 Accepted` immediately with a `job_id`
  3. A separate `/jobs/{job_id}/status` endpoint returns the current state: `queued`, `running`, `completed`, or `failed`
  4. On completion, the status endpoint returns the result or a reference to it

  ```json
  // POST /api/reports/generate → 201
  {
    "job_id": "job_abc123",
    "status": "queued",
    "status_url": "/api/jobs/job_abc123/status"
  }

  // GET /api/jobs/job_abc123/status → 200
  {
    "job_id": "job_abc123",
    "status": "completed",
    "result_url": "/api/reports/rpt_xyz789"
  }
  ```

  _Why: Synchronous endpoints that run long tasks block the connection, cause timeouts in clients, and fail silently under load. The async pattern is explicit, testable, and resilient._

---

## Response Shape

- **All responses use a consistent envelope format.** Define this in `AGENTS.md` for each project. An example pattern:

  ```json
  // Success
  { "data": { ... }, "error": null }

  // Error
  { "data": null, "error": { "code": "VALIDATION_ERROR", "message": "..." } }
  ```

- **Use standard HTTP status codes correctly:**
  - `200` — success, response body contains data
  - `201` — created or accepted (use for async job kickoff)
  - `400` — client error, bad input
  - `401` — unauthenticated
  - `403` — authenticated but unauthorized
  - `404` — resource not found
  - `422` — unprocessable entity (validation failed with valid structure)
  - `500` — server error

- **Never return `200` with an error inside the body.** If it failed, use an appropriate 4xx or 5xx status code.

---

## Input Validation

- **Validate all inputs at the API boundary.** Before any business logic runs, confirm the request shape is correct.
- **Return specific validation errors.** Not "invalid input" — "email is required", "amount must be a positive integer".

---

## Authentication

- **Every endpoint is authenticated by default.** Explicitly mark public endpoints as exceptions in both code and `AGENTS.md`.
- **Do not rely on client-provided user IDs.** Derive the user from the authenticated session/token, not from a request parameter.

---

## Versioning

- **Version your API from day one:** `/api/v1/...`
- **Never make breaking changes to an existing version.** Add a new version instead.
- **Document breaking changes** with a `BREAKING CHANGE:` footer in the commit.

---

## API Documentation

- **Store a local copy of third-party API docs** your project depends on in `/docs/api/`.
- **Document your own endpoints** in a format the agent can reference (OpenAPI spec or markdown, referenced in `AGENTS.md`).

  _Why: Having API docs locally means the agent references the real spec instead of hallucinating endpoints._

---

## → Where to Go Next

API endpoints designed and implemented?
→ Load `05-testing.md` — write tests for the happy path AND the failure path on each endpoint

Endpoint requires auth or touches user data?
→ Load `03-security.md` — confirm RLS, input validation, and auth are in place

API response time is over 50ms?
→ Implement the async job pattern (POST → 201 → GET /status) before continuing. Do not ship a slow synchronous endpoint.
