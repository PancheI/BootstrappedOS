import product from "@/config/product.json";
import pricing from "@/config/pricing.json";

export { product, pricing };
export type Plan = (typeof pricing.plans)[number];

/** The public address: NEXT_PUBLIC_SITE_URL once you have a domain, else the Vercel URL, else localhost. */
export function siteUrl(): string {
  if (process.env.NEXT_PUBLIC_SITE_URL) return process.env.NEXT_PUBLIC_SITE_URL.replace(/\/$/, "");
  if (process.env.VERCEL_PROJECT_PRODUCTION_URL) return `https://${process.env.VERCEL_PROJECT_PRODUCTION_URL}`;
  if (process.env.VERCEL_URL) return `https://${process.env.VERCEL_URL}`;
  return "http://localhost:3000";
}

export function money(amount: number, currency = pricing.currency): string {
  return new Intl.NumberFormat("en", { style: "currency", currency, maximumFractionDigits: amount % 1 ? 2 : 0 }).format(amount);
}

export function per(plan: Plan): string {
  if (plan.type !== "subscription") return "once";
  return plan.interval === "year" ? "a year" : "a month";
}
