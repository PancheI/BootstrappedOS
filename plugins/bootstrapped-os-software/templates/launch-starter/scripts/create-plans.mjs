// Creates the plans in src/config/pricing.json as AgentaOS products and saves each id back right away.
// Dry run by default: it prints what it would create. Add --yes to create them.
// Test keys (sk_test_) create test plans; a live key creates live ones, and asks for --live too.
// Safe to re-run: a plan that already has an id, or already exists in AgentaOS, is skipped.
import { readFileSync, writeFileSync } from "node:fs";
import { AgentaOS } from "@agentaos/pay";

const file = new URL("../src/config/pricing.json", import.meta.url);
const pricing = JSON.parse(readFileSync(file, "utf8"));
const save = () => writeFileSync(file, JSON.stringify(pricing, null, 2) + "\n");
const key = process.env.AGENTAOS_API_KEY;
const yes = process.argv.includes("--yes");
if (!key && yes) {
  console.error("Set AGENTAOS_API_KEY in .env.local first (a test key starts with sk_test_).");
  process.exit(1);
}
const mode = key?.startsWith("sk_live_") ? "live" : "test";
if (mode === "live" && !process.argv.includes("--live")) {
  console.error("That is a LIVE key. Re-run with --yes --live if you really mean to create live plans.");
  process.exit(1);
}
const product = JSON.parse(readFileSync(new URL("../src/config/product.json", import.meta.url), "utf8"));
const site = (process.env.NEXT_PUBLIC_SITE_URL || "").replace(/\/$/, "");
const client = key ? new AgentaOS(key) : null;

// Plans this account already has, by their plan key. Finds a plan created by an earlier run whose id never got saved.
async function existingPlans() {
  const found = new Map();
  if (!client) return found;
  for (let offset = 0; ; offset += 100) {
    const page = await client.paymentLinks.list({ limit: 100, offset });
    for (const link of page.items) {
      if (link.status === "active" && typeof link.metadata?.plan === "string") found.set(link.metadata.plan, link.id);
    }
    if (!page.hasMore) return found;
  }
}

const existing = await existingPlans();
let failed = false;
for (const plan of pricing.plans) {
  if (plan.linkId?.[mode]) { console.log(`= ${plan.key}: already created (${plan.linkId[mode]})`); continue; }
  if (existing.has(plan.key)) {
    plan.linkId = { ...(plan.linkId || {}), [mode]: existing.get(plan.key) };
    if (yes) save();
    console.log(`= ${plan.key}: found in AgentaOS (${existing.get(plan.key)})${yes ? ", id saved" : ""}`);
    continue;
  }
  const params = {
    name: `${product.name} · ${plan.name}`,
    description: plan.features.join(" · "),
    amount: plan.price, // in currency units (19 = $19), as the AgentaOS SDK expects
    currency: pricing.currency,
    type: plan.type,
    ...(plan.type === "subscription" ? { billingInterval: plan.interval } : {}),
    ...(plan.type === "subscription" && plan.trialDays ? { trialPeriodDays: plan.trialDays } : {}),
    ...(site.startsWith("https://") ? { successUrl: `${site}/thanks` } : {}),
    metadata: { plan: plan.key },
  };
  if (!yes) { console.log(`+ would create (${mode}):`, JSON.stringify(params)); continue; }
  try {
    const link = await client.paymentLinks.create(params);
    plan.linkId = { ...(plan.linkId || {}), [mode]: link.id };
    save();
    console.log(`+ ${plan.key}: created ${link.id} (${mode}), id saved`);
  } catch (e) {
    failed = true;
    console.error(`! ${plan.key}: not created: ${e.message}`);
  }
}
if (!yes) console.log("\nDry run. Re-run with --yes to create these plans.");
else if (failed) { console.error("\nSome plans failed. Fix the error and re-run; saved plans are skipped."); process.exit(1); }
else console.log("Done. The ids are in src/config/pricing.json.");
