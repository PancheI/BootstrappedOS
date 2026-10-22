import { Frame } from "@/components/frame";
import { product } from "@/lib/site";

export const metadata = { title: "Privacy" };

// A plain starting point, not legal advice. Check it against your country's rules before you sell.
export default function Privacy() {
  const { company, email, country } = product.legal;
  return (
    <Frame>
      <article className="mx-auto flex max-w-2xl flex-col gap-4 px-5 py-16 text-[15px] leading-relaxed">
        <h1 className="font-display text-3xl font-bold">Privacy</h1>
        <p>{product.name} is run by {company} ({country}). Contact: <a href={`mailto:${email}`}>{email}</a>.</p>
        <h2 className="pt-2 text-lg font-bold">What we collect</h2>
        <p>Your email, if you join the waitlist or buy. Payment details are handled by our payment provider (merchant of record) and never reach us. Anonymous usage analytics (pages viewed, buttons clicked) to improve the product. It uses no cookies and stores nothing in your browser, and it isn&apos;t linked to your email.</p>
        <h2 className="pt-2 text-lg font-bold">Why</h2>
        <p>To deliver what you bought, send the emails you asked for, and see which parts of the site work.</p>
        <h2 className="pt-2 text-lg font-bold">Your rights</h2>
        <p>Ask us any time to see, correct or delete your data: email <a href={`mailto:${email}`}>{email}</a>. Every email has an unsubscribe link.</p>
      </article>
    </Frame>
  );
}
