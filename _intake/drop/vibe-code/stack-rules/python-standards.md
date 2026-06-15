# python-standards.md — Python-Specific Rules

> Load this file alongside `02-code-quality.md` for any Python project.
> These rules extend the general quality standards — they do not replace them.

---

## Type Checking — Pyright Strict Mode

- **All Python code must pass `pyright` in strict mode.** No exceptions.
- **All functions must have explicit type annotations** — parameters and return types.
- **No implicit `Any`.** If a type is genuinely unknown, use `Unknown` or narrow it with a runtime check.
- **Configure pyright in `pyproject.toml`:**

  ```toml
  [tool.pyright]
  typeCheckingMode = "strict"
  ```

  _Why: Python's dynamic typing makes it easy to ship type errors that only appear at runtime. Strict mode catches them at write time — the same principle as `no any` in TypeScript._

---

## Formatting — Black

- **All Python code must be formatted with `black` before committing.**
- Run: `black .`
- Configure in `pyproject.toml`:

  ```toml
  [tool.black]
  line-length = 88
  target-version = ["py311"]
  ```

- **Do not manually format code.** Let black handle it. Do not argue with black's output.

  _Why: Consistent formatting across every file eliminates style debates and makes diffs easier to read. Black is opinionated so you don't have to be._

---

## Import Sorting — isort

- **All imports must be sorted with `isort` before committing.**
- Run: `isort .`
- Configure in `pyproject.toml` to be compatible with black:

  ```toml
  [tool.isort]
  profile = "black"
  ```

- **Import order:** stdlib → third-party → local. Blank line between each group.

  _Why: Sorted imports reduce merge conflicts and make it immediately clear what a module depends on._

---

## Pre-Commit Sequence (Python)

Run in this order before every commit:

```bash
isort .
black .
pyright
```

All three must complete without errors. If pyright fails, fix the type errors before committing.

---

## Python Project Structure

```
project/
├── pyproject.toml        # deps, tool configs (pyright, black, isort)
├── .env                  # secrets (gitignored)
├── .env.example          # variable names, no values
├── src/
│   └── your_package/
│       ├── __init__.py
│       ├── main.py       # entrypoint
│       ├── api/          # route definitions
│       ├── services/     # business logic
│       ├── models/       # data models / schemas
│       └── utils/        # shared utilities
└── tests/
    └── ...               # mirrors src/ structure
```

---

## FastAPI Specifics (when using the default backend stack)

- **Use Pydantic models for all request and response bodies.** No raw dicts.
- **Use dependency injection for auth and DB sessions.** Do not access request state directly in route handlers.
- **Async routes for I/O-bound operations.** Use `async def` for any route that touches the database or an external API.
- **Background tasks for jobs that exceed the 50ms ceiling.** See `06-api-standards.md` for the async job pattern.

---

## → Where to Go Next

Pyright, black, and isort all passing clean?
→ Return to `02-code-quality.md` and continue implementation

Using FastAPI and designing endpoints?
→ Load `06-api-standards.md` — the 50ms ceiling and async job pattern apply here too

Pre-commit checks failing?
→ Run `isort . && black . && pyright` in that order. Fix pyright errors before committing — do not skip or suppress them