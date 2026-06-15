# fw-react-native.md — React Native-Specific Rules

> Load alongside `02-code-quality.md` and `lang-typescript.md` for any React Native project.
> Assumes Expo (managed or bare workflow). If using bare React Native CLI, note the deviation in `AGENTS.md`.

---

## Expo Conventions

- **Use Expo SDK packages over bare React Native equivalents whenever available.** `expo-camera`, `expo-notifications`, `expo-file-system` — not the raw community alternatives. Expo packages are maintained to work together across SDK versions.
- **Pin the Expo SDK version in `package.json`.** Do not upgrade the SDK mid-feature. SDK upgrades are a discrete task done on a separate branch.
- **Run `npx expo-doctor` before committing.** Fix all reported issues. Do not ship with known compatibility warnings.

---

## Navigation — Expo Router

- **Use Expo Router (file-based routing) for all new projects.** Do not use React Navigation with a manual route config unless the project already uses it and migration isn't feasible — document this in `AGENTS.md`.
- **File structure mirrors URL structure:**
  ```
  app/
  ├── _layout.tsx           ← root layout (Stack, Tab, or Drawer)
  ├── index.tsx             ← home screen (/)
  ├── (tabs)/               ← tab group
  │   ├── _layout.tsx       ← tab bar configuration
  │   ├── home.tsx
  │   └── profile.tsx
  └── modal.tsx             ← modal screen
  ```
- **Use typed routes.** Enable `expo-router`'s typed routes via `"experiments": { "typedRoutes": true }` in `app.json`. This gives type-safe `href` props on `<Link>`.

---

## Platform Differences

- **Never assume behavior is identical on iOS and Android.** Test on both before marking a feature done.
- **Use `Platform.select()` or `Platform.OS` for platform-specific logic.** Do not duplicate entire components for each platform when a conditional is enough.
- **Platform-specific files use the `.ios.tsx` / `.android.tsx` convention** only when the component differs significantly enough that a shared file with conditionals becomes unreadable.
- **Do not use web-only CSS properties** (`box-shadow`, `cursor`, `transition`) without checking RN compatibility. Use `StyleSheet.create()` or the RN equivalent.

---

## Styling

- **Use `StyleSheet.create()` for all styles.** No inline style objects defined inside the render function — they create new objects on every render.
  ```tsx
  // Good
  const styles = StyleSheet.create({ container: { flex: 1, padding: 16 } })
  // Bad
  <View style={{ flex: 1, padding: 16 }}>
  ```
- **Use a consistent spacing scale.** Define it in a `constants/spacing.ts` file and reference it everywhere. Same principle as the web spacing rule in `07-ui-ux.md`.
- **For complex, dynamic styling needs, use NativeWind (Tailwind for React Native)** if the project adopts it. Document this decision in `AGENTS.md`.

---

## Performance

- **Use `FlatList` or `FlashList` for any list with more than ~20 items.** Never use `ScrollView` with `.map()` for long lists — it renders all items at once and causes jank.
- **Memoize expensive components with `React.memo`.** Memoize expensive calculations with `useMemo`. Memoize callbacks passed to child components with `useCallback`.
- **Avoid anonymous functions in JSX props on frequently-rendered components.** They create new references on every render and break memoization.
- **Measure before optimizing.** Use Flipper or React Native DevTools to identify actual bottlenecks. Do not premature-optimize.

---

## State Management

- **Local component state (`useState`) for UI state.** Form inputs, toggle states, modal visibility.
- **Context + `useReducer` for shared feature state** that doesn't need to persist.
- **Zustand or Jotai for global app state** that is accessed widely across screens. Document the choice in `AGENTS.md`.
- **Never store sensitive data in state.** Use `expo-secure-store` for tokens, credentials, or anything that must survive app restart securely.

---

## API and Networking

- **All API calls follow the rules in `06-api-standards.md`.** The 50ms ceiling applies to the server — the client must handle the async job pattern when applicable.
- **Use a centralized API client.** Never call `fetch()` directly from a component. All network calls go through a service layer in `services/`.
- **Handle offline states explicitly.** Use `expo-network` or `@react-native-community/netinfo` to detect connectivity. Show a useful UI state when offline, not a crash.

---

## Permissions

- **Request permissions at the point of need, not on app launch.**
- **Always handle the denied case.** Show a message explaining why the permission is needed and how to enable it in Settings.
- **Declare all required permissions in `app.json`** under `ios.infoPlist` and `android.permissions`. Missing declarations cause App Store / Play Store rejections.

---

## Build and Distribution

- **Use EAS Build for all production builds.** Do not build locally for distribution.
- **Separate build profiles in `eas.json`:** `development`, `preview`, `production`. Never use production credentials for local testing.
- **OTA updates via EAS Update** are for JS/asset changes only. Native code changes require a full build.

---

## → Where to Go Next

Navigation structure in place and platform differences accounted for?
→ Return to `02-code-quality.md` and continue feature implementation

Integrating Supabase for backend?
→ Load `stack-supabase.md`

Implementing auth?
→ Load `proc-auth-setup.md`

Ready to ship a build?
→ Load `proc-deployment.md`

Performance issues (jank, slow list rendering)?
→ Load `08-performance.md` for general principles, then use Flipper to identify specifics before making changes
