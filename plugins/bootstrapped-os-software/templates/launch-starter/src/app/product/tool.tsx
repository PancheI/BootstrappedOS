"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import { track } from "@/lib/analytics";
import { money, pricing } from "@/lib/site";

const fmt = (n: number) => new Intl.NumberFormat("en", { maximumFractionDigits: 0 }).format(n);
const perMonth = `${pricing.currency}/mo`;

export function Tool() {
  const [price, setPrice] = useState(19);
  const [costs, setCosts] = useState(150);
  const [goal, setGoal] = useState(1000);
  const [used, setUsed] = useState(false);

  useEffect(() => {
    if (!used) return;
    const t = setTimeout(() => track("product_used", { price, costs }), 800);
    return () => clearTimeout(t);
  }, [price, costs, used]);

  const breakEven = price > 0 ? Math.ceil(costs / price) : 0;
  const toGoal = price > 0 ? Math.ceil(goal / price) : 0;
  const yearly = Math.round(price * 10);
  const field = (label: string, value: number, set: (n: number) => void, suffix: string) => (
    <label className="flex flex-col gap-1.5 text-sm font-semibold">
      {label}
      <span className="flex items-center gap-2">
        <input type="number" min={0} value={value} onChange={(e) => { setUsed(true); set(Number(e.target.value) || 0); }} className="h-12 w-full rounded-xl border border-line px-4 text-base font-normal outline-none focus:border-accent" />
        <span className="text-soft">{suffix}</span>
      </span>
    </label>
  );

  return (
    <div className="flex flex-col gap-8">
      <div className="grid gap-4 sm:grid-cols-3">
        {field("Your price", price, setPrice, perMonth)}
        {field("Your costs", costs, setCosts, perMonth)}
        {field("Your goal", goal, setGoal, perMonth)}
      </div>
      <div className="grid gap-4 sm:grid-cols-3">
        <Result big={fmt(breakEven)} label="buyers cover your costs" />
        <Result big={fmt(toGoal)} label={`buyers reach ${money(goal)} a month`} />
        <Result big={money(yearly)} label="a yearly plan at 10 months' price, paid up front" />
      </div>
      <p className="text-sm text-soft">Arithmetic only: price × buyers. It says nothing about whether they&apos;ll buy; that&apos;s what the first conversations are for.</p>
      <Link href="/#pricing" className="self-start rounded-full bg-accent px-6 py-3 font-semibold text-accent-ink no-underline">Get the full check →</Link>
    </div>
  );
}

function Result({ big, label }: { big: string; label: string }) {
  return (
    <div className="rounded-2xl border border-line p-5">
      <p className="font-display text-4xl font-bold">{big}</p>
      <p className="mt-1 text-sm text-soft">{label}</p>
    </div>
  );
}
