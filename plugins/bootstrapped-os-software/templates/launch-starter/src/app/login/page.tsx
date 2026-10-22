import { redirect } from "next/navigation";
import { Frame } from "@/components/frame";
import { currentUser, missingAuthEnv } from "@/lib/supabase-server";
import { LoginForm } from "./login-form";

export const metadata = { title: "Sign in", robots: { index: false } };

export default async function Login({ searchParams }: { searchParams: Promise<{ error?: string }> }) {
  if (await currentUser()) redirect("/app");
  const missing = missingAuthEnv();
  const { error } = await searchParams;
  return (
    <Frame>
      <section className="mx-auto flex max-w-md flex-col gap-5 px-5 py-24">
        <h1 className="font-display text-4xl font-bold">Sign in</h1>
        {missing.length ? (
          <p className="rounded-2xl border border-line p-5 text-soft">
            Sign-in isn&apos;t switched on yet. Set {missing.map((k) => <code key={k} className="mx-1">{k}</code>)} in <code>.env.local</code> (Supabase: Project settings → API Keys), then restart.
          </p>
        ) : (
          <>
            {error && <p role="alert" className="text-sm text-red-700">That sign-in link has expired or was already used. Ask for a new one.</p>}
            <LoginForm />
            <p className="text-sm text-soft">No password. Use the email you paid with.</p>
          </>
        )}
      </section>
    </Frame>
  );
}
