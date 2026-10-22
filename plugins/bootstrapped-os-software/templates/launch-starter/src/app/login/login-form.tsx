"use client";

import { useActionState } from "react";
import { login, type LoginState } from "./actions";

const input = "h-12 rounded-full border border-line px-5 text-base outline-none focus:border-accent";
const button = "h-12 rounded-full bg-ink px-5 font-semibold text-white disabled:opacity-60";

export function LoginForm() {
  const [state, action, busy] = useActionState<LoginState, FormData>(login, { step: "email" });

  return (
    <form action={action} className="flex flex-col gap-3">
      {state.step === "email" ? (
        <>
          <label htmlFor="email" className="text-sm font-semibold">Your email</label>
          <input id="email" name="email" type="email" required autoComplete="email" placeholder="you@email.com" className={input} />
          <button type="submit" disabled={busy} className={button}>{busy ? "Sending…" : "Email me a sign-in code"}</button>
        </>
      ) : (
        <>
          <p className="text-soft">We sent a link and a code to <strong className="text-ink">{state.email}</strong>. Click the link, or type the code here.</p>
          <label htmlFor="code" className="text-sm font-semibold">Code</label>
          <input id="code" name="code" inputMode="numeric" autoComplete="one-time-code" required placeholder="123456" className={`${input} tracking-widest`} />
          <button type="submit" disabled={busy} className={button}>{busy ? "Checking…" : "Sign in"}</button>
        </>
      )}
      {state.error && <p role="alert" className="text-sm text-red-700">{state.error}</p>}
    </form>
  );
}
