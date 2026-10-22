import "server-only";
import { AgentaOS } from "@agentaos/pay";
import { pricing } from "@/lib/site";

/** Payments through AgentaOS (merchant of record: VAT, receipts and payouts handled). The rest of the site only calls createCheckout. */
export function paymentsReady(): boolean {
  return Boolean(process.env.AGENTAOS_API_KEY);
}

const mode = (): "test" | "live" => (process.env.AGENTAOS_API_KEY?.startsWith("sk_live_") ? "live" : "test");

/** successUrl must be https; leave it out on localhost. */
export async function createCheckout(planKey: string, successUrl?: string): Promise<string> {
  const plan = pricing.plans.find((p) => p.key === planKey);
  if (!plan) throw new Error(`Unknown plan: ${planKey}`);
  const linkId = plan.linkId[mode()];
  if (!linkId) throw new Error(`No ${mode()} plan id for "${planKey}" yet. Run: npm run plans`);
  const client = new AgentaOS(process.env.AGENTAOS_API_KEY!);
  const checkout = await client.checkouts.create({ linkId, ...(successUrl ? { successUrl } : {}), metadata: { plan: plan.key } });
  return checkout.checkoutUrl;
}
