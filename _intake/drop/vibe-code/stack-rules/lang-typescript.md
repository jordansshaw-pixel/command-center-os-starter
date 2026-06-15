# lang-typescript.md — TypeScript-Specific Rules

> Load alongside `02-code-quality.md` for any TypeScript project.
> These rules extend the general quality standards — they do not replace them.
> For React/Next.js projects, also load the relevant framework file.

---

## Compiler Configuration

- **Always use `strict: true` in `tsconfig.json`.** No exceptions. Do not disable individual strict checks to silence errors.
- **`noImplicitAny: true`** must be enabled (included in strict, but confirm it explicitly).
- **`noUncheckedIndexedAccess: true`** — enables safe array/object access. Add this even though it's not in strict by default.
- **`exactOptionalPropertyTypes: true`** — prevents accidentally assigning `undefined` to optional properties. Add this explicitly.

Minimum `tsconfig.json`:
```json
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true
  }
}
```

_Why: The default TypeScript config catches a fraction of real bugs. Strict mode plus these additions catches the ones that actually ship to production._

---

## Types and Interfaces

- **No `any`. Ever.** If a type is genuinely unknown at write time, use `unknown` and narrow it explicitly with a type guard.
- **Prefer `interface` for object shapes, `type` for unions, intersections, and aliases.**
- **Name interfaces and types clearly.** `UserRecord`, `PaymentPayload`, `ApiResponse<T>` — not `IUser`, `IData`, `Obj`.
- **No type assertions (`as SomeType`) without a comment explaining why it's safe.** Blind casting defeats the type system.
- **Use discriminated unions for state modeling:**
  ```ts
  type RequestState<T> =
    | { status: 'idle' }
    | { status: 'loading' }
    | { status: 'success'; data: T }
    | { status: 'error'; error: string }
  ```
  _Why: Discriminated unions make impossible states unrepresentable. No more `data && !loading && !error` conditionals._

---

## Functions

- **All function parameters and return types must be explicitly annotated.** Do not rely on inference for public-facing functions.
- **Async functions must return `Promise<T>` with a concrete `T`.** Not `Promise<any>`, not `Promise<unknown>` unless that's genuinely the only option.
- **Handle all promise rejections.** No floating promises. Use `void` operator intentionally when you're deliberately ignoring the return value, and comment why.

---

## Enums

- **Prefer `const` objects with `as const` over TypeScript `enum`.**
  ```ts
  // Prefer this:
  const Status = { Active: 'active', Inactive: 'inactive' } as const
  type Status = typeof Status[keyof typeof Status]

  // Over this:
  enum Status { Active = 'active', Inactive = 'inactive' }
  ```
  _Why: TypeScript enums have footguns around reverse mapping and tree-shaking. `as const` objects are predictable and compile away cleanly._

---

## Imports

- **Use path aliases instead of relative hell.** Configure `@/` to point to `src/` in `tsconfig.json`.
  ```ts
  // Good
  import { UserService } from '@/services/user'
  // Bad
  import { UserService } from '../../../services/user'
  ```
- **No barrel files (`index.ts` that re-exports everything) in large modules.** They cause circular dependency issues and slow down TypeScript's language server.

---

## Pre-Commit Sequence (TypeScript)

```bash
tsc --noEmit   # type check — must pass clean
eslint .       # lint — no errors, warnings are reviewed
prettier --check .  # formatting — fix with prettier --write . if needed
```

All three must pass before committing. Do not commit with TypeScript errors suppressed via `// @ts-ignore` or `// @ts-expect-error` without a documented reason in the same comment.

---

## → Where to Go Next

TypeScript config in place and type checking passing?
→ Return to `02-code-quality.md` and continue implementation

Building a React/Next.js frontend?
→ Load `fw-nextjs.md`

Building a React Native mobile app?
→ Load `fw-react-native.md`

Type errors you can't resolve cleanly?
→ Load `04-debugging.md` — treat unresolvable type errors as bugs, not warnings to suppress
