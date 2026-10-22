import "server-only";
import { createClient } from "@supabase/supabase-js";

export function storageReady(): boolean {
  return Boolean(process.env.SUPABASE_URL && process.env.SUPABASE_SECRET_KEY);
}

/** Server-only client with the secret key. Never import this into a client component. */
export function db() {
  return createClient(process.env.SUPABASE_URL!, process.env.SUPABASE_SECRET_KEY!, { auth: { persistSession: false } });
}
