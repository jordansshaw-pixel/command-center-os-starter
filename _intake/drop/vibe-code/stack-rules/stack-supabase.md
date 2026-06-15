# stack-supabase.md — Supabase-Specific Rules

> Load this file when Supabase is the database and/or auth provider for this project.
> Covers: PostgreSQL via Supabase, Row Level Security, Storage, Realtime, and Clerk + Supabase JWT integration.

---

## Setup

### Environment Variables
```
# Public — safe to expose to the browser
NEXT_PUBLIC_SUPABASE_URL=https://your-project.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJ...

# Server only — never expose to client
SUPABASE_SERVICE_ROLE_KEY=eyJ...
```

- **The `anon` key is safe to expose.** RLS is what limits what anonymous and authenticated users can do — the key alone does nothing.
- **The `service_role` key bypasses RLS entirely.** Never use it client-side. Never commit it. Use it only in server-side admin operations where RLS intentionally does not apply.

### Client Setup
```ts
// lib/supabase/client.ts — browser client (Client Components)
import { createBrowserClient } from '@supabase/ssr'
export const createClient = () =>
  createBrowserClient(process.env.NEXT_PUBLIC_SUPABASE_URL!, process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!)

// lib/supabase/server.ts — server client (Server Components, Route Handlers, Server Actions)
import { createServerClient } from '@supabase/ssr'
import { cookies } from 'next/headers'
export const createClient = () =>
  createServerClient(process.env.NEXT_PUBLIC_SUPABASE_URL!, process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!, {
    cookies: { get: (name) => cookies().get(name)?.value }
  })
```

Use the server client in any server-side context. Use the browser client only in Client Components that need real-time or client-side queries.

---

## Row Level Security (RLS) — Non-Negotiable

- **Enable RLS on every table. No exceptions.** Run this for every new table:
  ```sql
  ALTER TABLE your_table ENABLE ROW LEVEL SECURITY;
  ```
- **Write explicit policies for every operation (SELECT, INSERT, UPDATE, DELETE).** A table with RLS enabled but no policies denies all access to everyone — confirm your policies actually work.
- **Test RLS with two separate user sessions** before shipping any table. Confirm User A cannot read or write User B's rows.

### Standard Policy Patterns

```sql
-- Users can only read their own rows
CREATE POLICY "users_select_own" ON profiles
  FOR SELECT USING (auth.uid() = user_id);

-- Users can only insert rows for themselves
CREATE POLICY "users_insert_own" ON profiles
  FOR INSERT WITH CHECK (auth.uid() = user_id);

-- Users can only update their own rows
CREATE POLICY "users_update_own" ON profiles
  FOR UPDATE USING (auth.uid() = user_id);
```

---

## Clerk + Supabase JWT Integration

When using Clerk as the auth provider with Supabase as the database, you need to pass Clerk's JWT to Supabase so RLS policies can identify the user.

### Setup
1. In Clerk dashboard: Configure a **JWT template** named `supabase` with this claim structure:
   ```json
   { "sub": "{{user.id}}" }
   ```
   Copy the signing key.

2. In Supabase dashboard: Add a **JWT Secret** under Authentication → JWT Settings. Use the signing key from Clerk.

3. Create a Supabase client that uses the Clerk token:
   ```ts
   // lib/supabase/clerk-client.ts
   import { createClient } from '@supabase/supabase-js'
   import { useAuth } from '@clerk/nextjs'

   export function useSupabaseClient() {
     const { getToken } = useAuth()
     return createClient(
       process.env.NEXT_PUBLIC_SUPABASE_URL!,
       process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
       {
         global: {
           fetch: async (url, options = {}) => {
             const clerkToken = await getToken({ template: 'supabase' })
             const headers = new Headers(options?.headers)
             headers.set('Authorization', `Bearer ${clerkToken}`)
             return fetch(url, { ...options, headers })
           }
         }
       }
     )
   }
   ```

4. Update RLS policies to use `auth.jwt() ->> 'sub'` instead of `auth.uid()`:
   ```sql
   CREATE POLICY "clerk_users_select_own" ON profiles
     FOR SELECT USING ((auth.jwt() ->> 'sub') = user_id);
   ```

---

## Schema and Migrations

- **All schema changes go through migration files.** Never modify tables directly in the Supabase dashboard for production — dashboard changes are not tracked in version control.
- **Use the Supabase CLI for migrations:**
  ```bash
  supabase migration new add_profiles_table
  # Edit the generated file in supabase/migrations/
  supabase db push    # apply to linked project
  ```
- **Migration files are committed to the repo.** The `supabase/migrations/` folder is version-controlled.
- **Never rename or delete a migration file** after it has been applied. Create a new migration to reverse or modify it.

---

## Storage

- **Create a separate bucket for each logical group of files.** `avatars`, `documents`, `exports` — not one giant `uploads` bucket.
- **Enable RLS on storage buckets.** A public bucket means anyone with the URL can access the file — only use it for genuinely public assets.
- **Storage RLS policy pattern:**
  ```sql
  -- Users can upload to their own folder only
  CREATE POLICY "user_uploads" ON storage.objects
    FOR INSERT WITH CHECK (bucket_id = 'avatars' AND (storage.foldername(name))[1] = auth.uid()::text);
  ```
- **Store only the file path in your database, not the full URL.** Construct the URL at read time using `supabase.storage.from('bucket').getPublicUrl(path)`.

---

## Realtime

- **Enable Realtime only on tables that need it.** Every table with Realtime enabled adds overhead.
- **Use Realtime for UI updates, not as a substitute for proper API design.** If you're using Realtime to propagate state that could be a regular fetch, use a regular fetch.
- **Unsubscribe from Realtime channels when the component unmounts.** Forgotten subscriptions cause memory leaks and unexpected behavior.
  ```ts
  useEffect(() => {
    const channel = supabase.channel('room').on(...).subscribe()
    return () => { supabase.removeChannel(channel) }
  }, [])
  ```

---

## Supabase Checklist (Before Shipping)

- [ ] RLS enabled on every table
- [ ] RLS policies written and tested for SELECT, INSERT, UPDATE, DELETE on every table
- [ ] Tested with two user accounts — no cross-user data access
- [ ] `service_role` key is server-only and not in any client-side code
- [ ] All schema changes are in migration files, committed to the repo
- [ ] Storage buckets have RLS policies if they contain user-owned files

---

## → Where to Go Next

Supabase configured and RLS tested?
→ Return to `02-code-quality.md` and continue feature implementation

Using Clerk for auth with Supabase?
→ Confirm the JWT integration above is complete before writing any RLS policies

Ready to deploy the Supabase-backed project?
→ Load `proc-deployment.md` — database migrations must be applied as part of the deploy step

RLS policy not behaving as expected?
→ Load `04-debugging.md` — use the Supabase dashboard's RLS policy debugger (Authentication → Policies → Test) to simulate queries as a specific user
