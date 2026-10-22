import { NextResponse } from "next/server";
import { db, storageReady } from "@/lib/supabase";

export async function POST(req: Request) {
  const { email } = (await req.json().catch(() => ({}))) as { email?: unknown };
  const clean = typeof email === "string" ? email.trim().toLowerCase().slice(0, 200) : "";
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(clean)) return NextResponse.json({ error: "That email doesn't look right." }, { status: 400 });
  if (!storageReady()) {
    console.warn("[waitlist] SUPABASE_URL / SUPABASE_SECRET_KEY not set; email not stored");
    return NextResponse.json({ error: "The waitlist isn't switched on yet." }, { status: 503 });
  }
  const { error } = await db().from("waitlist").upsert({ email: clean }, { onConflict: "email", ignoreDuplicates: true });
  if (error) {
    console.error("[waitlist]", error.message);
    return NextResponse.json({ error: "That didn't work. Try again in a moment." }, { status: 500 });
  }
  return NextResponse.json({ ok: true });
}
