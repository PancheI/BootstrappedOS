import type { EmailOtpType } from "@supabase/supabase-js";
import { NextResponse, type NextRequest } from "next/server";
import { authClient, authReady } from "@/lib/supabase-server";

// The link in the sign-in email lands here. Supabase's default email sends ?code=...;
// a custom email template can send ?token_hash=...&type=email instead. Both work.
export async function GET(request: NextRequest) {
  const url = request.nextUrl;
  const next = url.searchParams.get("next") ?? "/app";
  const safeNext = next.startsWith("/") && !next.startsWith("//") ? next : "/app"; // never redirect off-site
  if (authReady()) {
    const supabase = await authClient();
    const code = url.searchParams.get("code");
    const tokenHash = url.searchParams.get("token_hash");
    const type = url.searchParams.get("type") as EmailOtpType | null;
    const { error } = code
      ? await supabase.auth.exchangeCodeForSession(code)
      : tokenHash && type
        ? await supabase.auth.verifyOtp({ token_hash: tokenHash, type })
        : { error: new Error("no code in link") };
    if (!error) return NextResponse.redirect(new URL(safeNext, url.origin));
    console.warn("[auth/callback]", error.message);
  }
  return NextResponse.redirect(new URL("/login?error=link", url.origin));
}
