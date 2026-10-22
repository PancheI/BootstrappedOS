import type { Metadata } from "next";
import { Frame } from "@/components/frame";
import { Tool } from "./tool";

export const metadata: Metadata = { title: "Try it" };

// The product. /start-from-zero and the software module replace <Tool /> with the real thing;
// the sample below is a working break-even calculator so the demo never shows an empty page.
export default function ProductPage() {
  return (
    <Frame>
      <section className="mx-auto max-w-3xl px-5 py-16">
        <h1 className="font-display text-3xl font-bold sm:text-4xl">Your break-even, in plain numbers</h1>
        <p className="mt-3 text-soft">Your price, your monthly costs: how many buyers you need, and what a yearly plan changes.</p>
        <div className="mt-8"><Tool /></div>
      </section>
    </Frame>
  );
}
