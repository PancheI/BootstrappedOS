// Read-only: shows what's left before live payments. It never submits anything.
// Verification (your legal details) and the payout account are done by you in the AgentaOS dashboard.
import { AgentaOS } from "@agentaos/pay";

const key = process.env.AGENTAOS_API_KEY;
if (!key) {
  console.error("Set AGENTAOS_API_KEY in .env.local first (a test key starts with sk_test_).");
  process.exit(1);
}

const r = await new AgentaOS(key).goLive.get().catch((e) => {
  console.error(`Couldn't read your go-live status: ${e.message}`);
  process.exit(1);
});
const tick = (ok) => (ok ? "[x]" : "[ ]");
const verify = {
  unverified: "not submitted yet: fill it in the AgentaOS dashboard",
  in_review: "submitted, being reviewed",
  on_hold: `on hold${r.heldReason ? `: ${r.heldReason}` : ""}`,
  verified: "verified",
  rejected: `rejected${r.rejectReason ? `: ${r.rejectReason}` : ""}${r.cooldownUntil ? ` (you can resubmit after ${r.cooldownUntil.slice(0, 10)})` : ""}`,
}[r.verifyState] ?? r.verifyState;

console.log(`Go-live check (${r.progress.done} of ${r.progress.total} done)\n`);
console.log(`${tick(r.triedIt)} Tried it: a test product and a test payment`);
console.log(`${tick(r.verifyState === "verified")} Verification: ${verify}`);
console.log(`${tick(r.hasPayoutAccount)} Payout account: ${r.hasPayoutAccount ? "added" : "add one in the AgentaOS dashboard"}`);
if (r.rfi) {
  console.log(`[ ] Open questions from AgentaOS (asked ${r.rfi.askedAt.slice(0, 10)}): ${r.rfi.question}`);
  for (const item of r.rfi.items) console.log(`    - ${item.text}`);
} else {
  console.log("[x] Open questions: none");
}
console.log(`${tick(r.canGoLive)} Can go live: ${r.canGoLive ? "yes. Put the live key in, then: npm run plans -- --yes --live" : "not yet"}`);
if (r.milestones.firstLivePaymentAt) console.log(`\nLive payments so far: ${r.milestones.livePaymentCount}`);
