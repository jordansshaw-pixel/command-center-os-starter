# fw-nextjs.md — Next.js-Specific Rules

> Load alongside `02-code-quality.md` and `lang-typescript.md` for any Next.js project.
> Assumes App Router (Next.js 13+). If using Pages Router, note the deviation in `AGENTS.md`.

---

## App Router Fundamentals

- **Default to Server Components.** Only add `'use client'` when the component needs browser APIs, event handlers, or React state/effects.
- **Never add `'use client'` to a layout or a page component unless absolutely required.** Push client boundaries as deep into the tree as possible.
- **Co-locate `'use client'` components in their own files.** A server component imports a client component — not the other way around.

  _Why: Every `'use client'` boundary adds to the client bundle. Server components are free. The default should be server._

---

## Data Fetching

- **Fetch data in Server Components, not in `useEffect`.** `useEffect` data fetching is a pattern from Pages Router. In App Router, it's the wrong tool.
- **Use `async/await` directly in Server Components:**
  ```tsx
  // Good — in a Server Component
  export default async function Page() {
    const data = await fetchSomething()
    return <div>{data.title}</div>
  }
  ```
- **Use React `cache()` to deduplicate expensive fetches that are called from multiple Server Components in the same render.**
- **Pass data down as props to Client Components.** Do not fetch inside Client Components unless you're using a library like SWR or React Query for client-side revalidation.

---

## Route Handlers (API Routes)

- **Route Handlers live in `app/api/[route]/route.ts`.** One file per route, named `route.ts`.
- **Export named functions for each HTTP method:** `GET`, `POST`, `PATCH`, `DELETE`.
- **All Route Handlers must follow the 50ms rule from `06-api-standards.md`.** Long operations use the async job pattern.
- **Auth check is the first thing in every non-public Route Handler.** Before any business logic:
  ```ts
  const session = await getServerSession()
  if (!session) return NextResponse.json({ error: 'Unauthorized' }, { status: 401 })
  ```

---

## Server Actions

- **Use Server Actions for form mutations, not API routes.** Server Actions are the App Router way to handle form submissions.
- **Validate all Server Action inputs with Zod** before touching the database.
- **Server Actions must be defined in files marked `'use server'`** or inline with the `'use server'` directive.
- **Never expose sensitive data in Server Action return values.** Only return what the client needs.

---

## Caching and Revalidation

- **Understand the caching layers:** fetch cache → router cache → full route cache. Know which one you're dealing with before debugging a stale data issue.
- **Use `revalidatePath()` or `revalidateTag()` after mutations.** Do not rely on manual cache busting.
- **Tag fetches that need targeted revalidation:**
  ```ts
  fetch('/api/posts', { next: { tags: ['posts'] } })
  // After mutation:
  revalidateTag('posts')
  ```

---

## File and Folder Conventions

```
app/
├── layout.tsx              ← root layout (Server Component)
├── page.tsx                ← home route
├── (auth)/                 ← route group (no URL segment)
│   ├── login/page.tsx
│   └── signup/page.tsx
├── dashboard/
│   ├── layout.tsx          ← nested layout
│   └── page.tsx
└── api/
    └── webhooks/
        └── stripe/
            └── route.ts    ← Route Handler

components/
├── ui/                     ← shadcn/ui components (copy-pasted, you own them)
└── [feature]/              ← feature-specific components

lib/
├── db.ts                   ← database client
├── auth.ts                 ← auth helpers
└── utils.ts                ← shared utilities
```

- **Route groups `(folder)` do not add to the URL.** Use them to share layouts without affecting the URL structure.
- **Parallel routes `@folder` and intercepted routes `(.)folder`** are powerful but complex — document them in `AGENTS.md` when used.

---

## Metadata and SEO

- **Export a `metadata` object or `generateMetadata` function from every `page.tsx`.** Do not leave pages with default or empty metadata.
  ```ts
  export const metadata: Metadata = {
    title: 'Page Title',
    description: 'Specific description for this page.',
  }
  ```

---

## Environment Variables

- **Server-only variables have no prefix.** `DATABASE_URL`, `STRIPE_SECRET_KEY`
- **Client-accessible variables are prefixed `NEXT_PUBLIC_`.** `NEXT_PUBLIC_SUPABASE_URL`
- **Never put secrets in `NEXT_PUBLIC_` variables.** They are embedded in the client bundle.
- **Access `NEXT_PUBLIC_` variables at the component level, not in a shared server utility that might be imported server-side only.**

---

## Performance

- **Use `next/image` for all images.** No raw `<img>` tags. `next/image` handles lazy loading, format optimization, and size constraints.
- **Use `next/font` for fonts.** Never load fonts from a CDN via a `<link>` tag in the layout.
- **Use `next/link` for internal navigation.** No `<a href>` for internal routes.
- **Analyze bundle size before shipping:** `ANALYZE=true next build`

---

## → Where to Go Next

App Router structure in place and Server/Client boundary defined?
→ Return to `02-code-quality.md` and continue feature implementation

Building API endpoints in Route Handlers?
→ Load `06-api-standards.md` — the 50ms rule and async job pattern apply here

Integrating Supabase for database and auth?
→ Load `stack-supabase.md`

Implementing auth (Clerk or similar)?
→ Load `proc-auth-setup.md`

Ready to deploy?
→ Load `proc-deployment.md`
