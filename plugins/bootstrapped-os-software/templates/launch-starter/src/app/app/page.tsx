import Link from "next/link";
import { redirect } from "next/navigation";
import { Frame } from "@/components/frame";
import { currentUser } from "@/lib/supabase-server";
import { signOut } from "../login/actions";

export const metadata = { title: "Your account", robots: { index: false } };

// The signed-in area. The real check happens here, on the server, on every visit.
export default async function App() {
  const user = await currentUser();
  if (!user) redirect("/login");
  return (
    <Frame>
      <section className="mx-auto flex max-w-xl flex-col gap-6 px-5 py-24">
        <h1 className="font-display text-4xl font-bold">You&apos;re signed in</h1>
        <p className="text-soft">Signed in as <strong className="text-ink">{user.email}</strong></p>
        <div className="rounded-2xl border border-line p-6">
          <h2 className="font-display text-lg font-bold">Your plan</h2>
          {/* Next step: read the plan from AgentaOS (see the payments-agentaos skill). Until then, everyone signed in can use the product. */}
          <p className="text-soft">Your plan and receipts show here soon. Receipts are also in your email.</p>
        </div>
        <div className="flex flex-wrap items-center gap-4">
          <Link href="/product" className="rounded-full bg-accent px-6 py-3 font-semibold text-accent-ink no-underline">Open the product →</Link>
          <form action={signOut}>
            <button type="submit" className="text-sm underline">Sign out</button>
          </form>
        </div>
      </section>
    </Frame>
  );
}
