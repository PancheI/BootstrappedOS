"use client";

import { useState } from "react";
import { track } from "@/lib/analytics";
import { money, per, pricing } from "@/lib/site";

export function Pricing() {
  const [busy, setBusy] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  async function buy(key: string) {
    setBusy(key);
    setError(null);
    track("checkout_clicked", { plan: key });
    try {
      const res = await fetch("/api/checkout", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ plan: key }) });
      const data = (await res.json()) as { url?: string; error?: string };
      if (!res.ok || !data.url) throw new Error(data.error || "The checkout didn't open.");
      window.location.assign(data.url);
    } catch (e) {
      track("checkout_failed", { plan: key });
      setError(e instanceof Error ? e.message : "The checkout didn't open.");
      setBusy(null);
    }
  }

  return (
    <div>
      <div className={`grid gap-4 ${pricing.plans.length > 1 ? "sm:grid-cols-2" : ""}`}>
        {pricing.plans.map((p) => (
          <div key={p.key} className={`flex flex-col gap-4 rounded-2xl border p-6 ${p.highlight ? "border-accent ring-1 ring-accent" : "border-line"}`}>
            <div className="flex items-baseline justify-between gap-3">
              <h3 className="font-display text-lg font-bold">{p.name}</h3>
              {p.highlight && <span className="rounded-full bg-accent px-2.5 py-0.5 text-xs font-semibold text-accent-ink">Most picked</span>}
            </div>
            <p className="font-display text-4xl font-bold">
              {money(p.price)} <span className="text-base font-medium text-soft">{per(p)}</span>
            </p>
            {p.trialDays ? <p className="text-sm text-soft">{p.trialDays} days free, then {money(p.price)} {per(p)}</p> : null}
            <ul className="flex flex-col gap-2 text-[15px]">
              {p.features.map((f) => (
                <li key={f} className="flex gap-2"><span aria-hidden className="text-accent">✓</span>{f}</li>
              ))}
            </ul>
            <button
              type="button"
              onClick={() => buy(p.key)}
              disabled={busy !== null}
              className={`mt-auto h-12 rounded-full px-5 font-semibold transition active:scale-[.98] disabled:opacity-60 ${p.highlight ? "bg-accent text-accent-ink" : "border border-ink"}`}
            >
              {busy === p.key ? "Opening checkout…" : `Get ${p.name.toLowerCase()}`}
            </button>
          </div>
        ))}
      </div>
      {error && <p role="alert" className="mt-4 text-sm text-red-700">{error}</p>}
      <p className="mt-4 text-sm text-soft">Secure checkout. VAT and receipts handled. Cancel any time.</p>
    </div>
  );
}
