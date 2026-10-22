"use server";

import { redirect } from "next/navigation";
import { authClient, authReady } from "@/lib/supabase-server";
import { siteUrl } from "@/lib/site";

export type LoginState = { step: "email" | "code"; email?: string; error?: string };

/** One form, two steps: no code yet = send one; a code = check it. */
export async function login(state: LoginState, form: FormData): Promise<LoginState> {
  return form.has("code") ? checkCode(state, form) : sendCode(form);
}

/** Step 1: email the visitor a sign-in link and a 6-digit code. New emails get an account. */
async function sendCode(form: FormData): Promise<LoginState> {
  const email = String(form.get("email") ?? "").trim().toLowerCase().slice(0, 200);
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) return { step: "email", error: "That email doesn't look right." };
  if (!authReady()) return { step: "email", error: "Sign-in isn't switched on yet." };
  const { error } = await (await authClient()).auth.signInWithOtp({ email, options: { emailRedirectTo: `${siteUrl()}/auth/callback` } });
  if (error) {
    console.error("[login]", error.message);
    return { step: "email", error: error.status === 429 ? "Too many tries. Wait a minute and try again." : "That didn't work. Try again in a moment." };
  }
  return { step: "code", email };
}

/** Step 2: the code from the email. (The link in the same email signs in through /auth/callback instead.) */
async function checkCode(state: LoginState, form: FormData): Promise<LoginState> {
  const token = String(form.get("code") ?? "").replace(/\s/g, "");
  if (!state.email || !/^\d{6,10}$/.test(token)) return { ...state, error: "Type the code from the email." };
  const { error } = await (await authClient()).auth.verifyOtp({ email: state.email, token, type: "email" });
  if (error) return { ...state, error: "That code didn't work. Check it, or ask for a new one." };
  redirect("/app");
}

export async function signOut() {
  if (authReady()) await (await authClient()).auth.signOut();
  redirect("/");
}
