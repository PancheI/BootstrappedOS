import { Frame } from "@/components/frame";
import { Pricing } from "@/components/pricing";
import { Waitlist } from "@/components/waitlist";
import { CtaLink } from "@/lib/analytics";
import { product } from "@/lib/site";

export default function Home() {
  return (
    <Frame>
      <section className="mx-auto flex max-w-5xl flex-col gap-6 px-5 pb-16 pt-16 sm:pt-24">
        <p className="text-sm font-semibold text-accent">For {product.buyer.toLowerCase()}</p>
        <h1 className="max-w-3xl font-display text-4xl font-bold leading-[1.05] tracking-tight sm:text-6xl">{product.tagline}</h1>
        <p className="max-w-2xl text-lg text-soft">{product.promise}</p>
        <div className="flex flex-wrap items-center gap-3">
          <CtaLink name="hero" href="/product" className="inline-flex h-12 items-center rounded-full bg-accent px-6 font-semibold text-accent-ink no-underline">{product.cta} →</CtaLink>
          <CtaLink name="see-pricing" href="#pricing" className="inline-flex h-12 items-center rounded-full border border-ink px-6 font-semibold no-underline">See pricing</CtaLink>
        </div>
      </section>

      <section className="border-t border-line bg-tint">
        <div className="mx-auto max-w-5xl px-5 py-16">
          <h2 className="font-display text-2xl font-bold sm:text-3xl">{product.problem.title}</h2>
          <div className="mt-8 grid gap-4 md:grid-cols-3">
            {product.problem.quotes.map((q) => (
              <figure key={q.text} className="flex flex-col gap-3 rounded-2xl border border-line bg-white p-5">
                <blockquote className="text-[15px] leading-relaxed">“{q.text}”</blockquote>
                <figcaption className="mt-auto text-sm text-soft">
                  <a href={q.url} rel="nofollow noopener" target="_blank">{q.source}</a>
                </figcaption>
              </figure>
            ))}
          </div>
        </div>
      </section>

      <section className="mx-auto max-w-5xl px-5 py-16">
        <h2 className="font-display text-2xl font-bold sm:text-3xl">How it works</h2>
        <ol className="mt-8 grid gap-6 md:grid-cols-3">
          {product.steps.map((s, i) => (
            <li key={s.title} className="flex flex-col gap-2">
              <span className="font-display text-sm font-bold text-accent">0{i + 1}</span>
              <b className="text-lg">{s.title}</b>
              <span className="text-soft">{s.body}</span>
            </li>
          ))}
        </ol>
      </section>

      <section id="pricing" className="border-t border-line">
        <div className="mx-auto max-w-5xl px-5 py-16">
          <h2 className="font-display text-2xl font-bold sm:text-3xl">Pricing</h2>
          <div className="mt-8"><Pricing /></div>
        </div>
      </section>

      <section className="border-t border-line bg-tint">
        <div className="mx-auto grid max-w-5xl gap-10 px-5 py-16 md:grid-cols-2">
          <div>
            <h2 className="font-display text-2xl font-bold sm:text-3xl">Questions</h2>
            <dl className="mt-6 flex flex-col gap-5">
              {product.faq.map((f) => (
                <div key={f.q}><dt className="font-semibold">{f.q}</dt><dd className="mt-1 text-soft">{f.a}</dd></div>
              ))}
            </dl>
          </div>
          <div className="flex flex-col gap-4">
            <h2 className="font-display text-2xl font-bold sm:text-3xl">Not ready yet?</h2>
            <p className="text-soft">Leave your email. One note when there&apos;s something worth your time.</p>
            <Waitlist />
            <p className="text-sm text-soft">{product.founder.name}: {product.founder.line}</p>
          </div>
        </div>
      </section>
    </Frame>
  );
}
