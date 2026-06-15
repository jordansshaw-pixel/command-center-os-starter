# proc-auth-setup.md — Auth Implementation Process

> Load this file when implementing authentication from scratch on a new project.
> Assumes Clerk as the default provider per `tech-stack.md`.
> If using a different provider, note the deviation in `AGENTS.md` and adapt accordingly.

---

## Before Writing Any Auth Code

Auth is the highest-risk part of any application. Before touching a line:

1. **Confirm the provider in `AGENTS.md`.** Default is Clerk. If the project uses Supabase Auth or another provider, the specific implementation details differ — but the rules below apply to all of them.
2. **Confirm which routes are public and which are protected.** Write this list down in `AGENTS.md` before implementation. Do not leave it implicit.
3. **Confirm what user data needs to sync to your own database.** Clerk stores identity. Your DB stores everything else (profile data, preferences, org-specific data). Define the sync boundary explicitly.

---

## Clerk Setup (Default)

### Installation
```bash
npm install @clerk/nextjs        # Next.js
npm install @clerk/expo          # React Native / Expo
```

### Environment Variables
```
# Required — server and client
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=pk_...
CLERK_SECRET_KEY=sk_...

# Optional — custom redirect paths
NEXT_PUBLIC_CLERK_SIGN_IN_URL=/sign-in
NEXT_PUBLIC_CLERK_SIGN_UP_URL=/sign-up
NEXT_PUBLIC_CLERK_AFTER_SIGN_IN_URL=/dashboard
NEXT_PUBLIC_CLERK_AFTER_SIGN_UP_URL=/dashboard
```

Add all to `.env.example` with no values before implementation.

### Middleware (Next.js)
```ts
// middleware.ts — at project root
import { clerkMiddleware, createRouteMatcher } from '@clerk/nextjs/server'

const isPublicRoute = createRouteMatcher([
  '/',
  '/sign-in(.*)',
  '/sign-up(.*)',
  '/api/webhooks(.*)',   // webhooks must be public — they come from Clerk's servers
])

export default clerkMiddleware((auth, req) => {
  if (!isPublicRoute(req)) auth().protect()
})

export const config = {
  matcher: ['/((?!_next|[^?]*\\.(?:html?|css|js(?!on)|jpe?g|webp|png|gif|svg|ttf|woff2?|ico|csv|docx?|xlsx?|zip|webmanifest)).*)', '/(api|trpc)(.*)'],
}
```

**Every route is protected by default. Public routes are the explicit exception list.**

---

## User Sync to Database

When a user signs up or updates their profile in Clerk, sync to your database via Clerk webhooks:

1. **Create a webhook endpoint:** `app/api/webhooks/clerk/route.ts`
2. **Verify the webhook signature** before processing. Do not trust unverified webhook payloads.
3. **Handle these events at minimum:**
   - `user.created` → create a row in your `users` table
   - `user.updated` → update name, email, avatar in your `users` table
   - `user.deleted` → soft delete or hard delete per your data policy
4. **Store the Clerk `userId` as the foreign key** in all your tables. Do not use Clerk's email as the identifier — emails change.

```ts
// app/api/webhooks/clerk/route.ts
import { Webhook } from 'svix'
import { headers } from 'next/headers'

export async function POST(req: Request) {
  const WEBHOOK_SECRET = process.env.CLERK_WEBHOOK_SECRET
  if (!WEBHOOK_SECRET) throw new Error('CLERK_WEBHOOK_SECRET not set')

  const headerPayload = headers()
  const svix_id = headerPayload.get('svix-id')
  const svix_timestamp = headerPayload.get('svix-timestamp')
  const svix_signature = headerPayload.get('svix-signature')

  if (!svix_id || !svix_timestamp || !svix_signature) {
    return new Response('Missing svix headers', { status: 400 })
  }

  const payload = await req.json()
  const body = JSON.stringify(payload)
  const wh = new Webhook(WEBHOOK_SECRET)

  let evt
  try {
    evt = wh.verify(body, { 'svix-id': svix_id, 'svix-timestamp': svix_timestamp, 'svix-signature': svix_signature })
  } catch {
    return new Response('Invalid signature', { status: 400 })
  }

  // Handle evt.type === 'user.created', 'user.updated', 'user.deleted'
  // ...

  return new Response('OK', { status: 200 })
}
```

---

## Protecting Routes and Data

### Server Components
```ts
import { auth } from '@clerk/nextjs/server'

export default async function ProtectedPage() {
  const { userId } = auth()
  if (!userId) redirect('/sign-in')
  // ...
}
```

### Route Handlers
```ts
import { auth } from '@clerk/nextjs/server'

export async function GET() {
  const { userId } = auth()
  if (!userId) return NextResponse.json({ error: 'Unauthorized' }, { status: 401 })
  // Always derive userId from auth(), never from request params
}
```

### Database Queries
- **Always filter by `userId` from the auth session, not from a request parameter.** A user must never be able to access another user's data by manipulating a URL or request body.
- If using Supabase, pair Clerk auth with RLS policies. See `stack-supabase.md` for the Clerk + Supabase JWT pattern.

---

## Testing Auth

- **Test with two separate accounts.** Confirm that Account A cannot access Account B's data.
- **Test the unauthenticated state.** What happens when a token expires mid-session? The user should be redirected to sign-in, not shown an error screen or raw data.
- **Test webhook delivery.** Use the Clerk dashboard's webhook testing tool to fire test events. Confirm your handler processes them correctly.

---

## Auth Checklist (Before Shipping)

- [ ] All protected routes are in middleware — no route relies solely on client-side auth checks
- [ ] Webhook endpoint verifies signature before processing
- [ ] `user.created`, `user.updated`, `user.deleted` events all handled
- [ ] All DB queries filter by `userId` from server session (not from request)
- [ ] Tested with two accounts — Account A cannot access Account B's data
- [ ] Unauthenticated state tested — expired session redirects cleanly
- [ ] `CLERK_WEBHOOK_SECRET` in `.env.example`

---

## → Where to Go Next

Auth implemented and checklist passed?
→ Load `03-security.md` — run the full security checklist before continuing

Using Supabase as the database?
→ Load `stack-supabase.md` — the Clerk + Supabase JWT integration requires specific RLS setup

Ready to move on to feature implementation?
→ Return to `02-code-quality.md`
