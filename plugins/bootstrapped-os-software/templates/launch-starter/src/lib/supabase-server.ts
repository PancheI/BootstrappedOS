import "server-only";
import { createServerClient } from "@supabase/ssr";
import { cookies } from "next/headers";

/** Sign-in needs the project URL and the publishable key (Project settings -> API Keys). Both are safe to expose; the secret key is never used here. */
export function missingAuthEnv(): string[] {
  return ["SUPABASE_URL", "SUPABASE_PUBLISHABLE_KEY"].filter((k) => !process.env[k]);
}

export function authReady(): boolean {
  return missingAuthEnv().length === 0;
}

/** Acts as the signed-in visitor (their session lives in cookies), so row level security applies. Use in pages, server actions and route handlers. */
export async function authClient() {
  const store = await cookies();
  return createServerClient(process.env.SUPABASE_URL!, process.env.SUPABASE_PUBLISHABLE_KEY!, {
    cookies: {
      getAll: () => store.getAll(),
      setAll: (list) => {
        // Pages can't write cookies; the proxy refreshes the session for them.
        try {
          list.forEach(({ name, value, options }) => store.set(name, value, options));
        } catch {}
      },
    },
  });
}

/** The signed-in visitor, or null. getClaims checks the token's signature; never trust getSession on the server. */
export async function currentUser(): Promise<{ id: string; email: string } | null> {
  await cookies(); // reading cookies keeps the calling page per-visit, even when env is missing at build time
  if (!authReady()) return null;
  const { data } = await (await authClient()).auth.getClaims();
  const claims = data?.claims;
  return claims ? { id: claims.sub, email: String(claims.email ?? "") } : null;
}
