import { Frame } from "@/components/frame";
import { product } from "@/lib/site";

export const metadata = { title: "Terms" };

// A plain starting point, not legal advice. Check it before you sell.
export default function Terms() {
  const { company, email } = product.legal;
  return (
    <Frame>
      <article className="mx-auto flex max-w-2xl flex-col gap-4 px-5 py-16 text-[15px] leading-relaxed">
        <h1 className="font-display text-3xl font-bold">Terms</h1>
        <p>{product.name} is provided by {company}. By buying, you agree to these terms.</p>
        <h2 className="pt-2 text-lg font-bold">Payments</h2>
        <p>Payments are processed by our merchant of record, which also handles VAT and receipts. Subscriptions renew until you cancel; cancelling stops the next renewal and access runs to the end of the period you paid for.</p>
        <h2 className="pt-2 text-lg font-bold">Refunds</h2>
        <p>Not happy in the first 14 days? Email <a href={`mailto:${email}`}>{email}</a> for a full refund.</p>
        <h2 className="pt-2 text-lg font-bold">The service</h2>
        <p>We work hard to keep it running and correct, but it is provided as is. Numbers it shows are arithmetic on what you enter, not financial advice.</p>
      </article>
    </Frame>
  );
}
