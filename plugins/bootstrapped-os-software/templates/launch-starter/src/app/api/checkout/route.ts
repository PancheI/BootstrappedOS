import { NextResponse } from "next/server";
import { createCheckout, paymentsReady } from "@/lib/agentaos";
import { siteUrl } from "@/lib/site";

// The plan comes from the browser as a key only; the price always comes from src/config/pricing.json.
export async function POST(req: Request) {
  const { plan } = (await req.json().catch(() => ({}))) as { plan?: unknown };
  if (typeof plan !== "string") return NextResponse.json({ error: "Pick a plan." }, { status: 400 });
  if (!paymentsReady()) return NextResponse.json({ error: "Payments aren't switched on yet." }, { status: 503 });

  // AgentaOS takes https return addresses only. Without one (localhost) the buyer stays on the checkout's own
  // success page. In production NEXT_PUBLIC_SITE_URL must be your https address, or buyers never reach /thanks.
  const site = siteUrl();
  const successUrl = site.startsWith("https://") ? `${site}/thanks` : undefined;
  if (!successUrl && process.env.NODE_ENV === "production") {
    console.error("[checkout] set NEXT_PUBLIC_SITE_URL to your https address: buyers can't reach /thanks");
  }

  try {
    const url = await createCheckout(plan, successUrl);
    return NextResponse.json({ url });
  } catch (e) {
    console.error("[checkout]", e);
    return NextResponse.json({ error: "The checkout didn't open. Try again in a moment." }, { status: 500 });
  }
}
