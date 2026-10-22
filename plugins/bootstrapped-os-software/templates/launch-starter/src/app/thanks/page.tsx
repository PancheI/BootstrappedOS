import Link from "next/link";
import { Frame } from "@/components/frame";
import { product } from "@/lib/site";

export const metadata = { title: "Thank you", robots: { index: false } };

export default function Thanks() {
  return (
    <Frame>
      <section className="mx-auto flex max-w-xl flex-col gap-4 px-5 py-24">
        <h1 className="font-display text-4xl font-bold">You&apos;re in. Thank you.</h1>
        <p className="text-soft">Your receipt is on its way by email. I read every reply: tell me what made you buy, it helps more than you think.</p>
        <p className="text-soft">{product.founder.name}</p>
        {/* Sign-in uses the same email as the checkout, so the buyer lands in their account. */}
        <Link href="/login" className="self-start rounded-full bg-accent px-6 py-3 font-semibold text-accent-ink no-underline">Sign in to start →</Link>
        <p className="text-sm text-soft">Use the email you paid with. No password: we email you a code.</p>
      </section>
    </Frame>
  );
}
