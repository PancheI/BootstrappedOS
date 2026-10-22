"use client";

import { useState, type FormEvent } from "react";
import { track } from "@/lib/analytics";

export function Waitlist({ label = "Join the waitlist" }: { label?: string }) {
  const [state, setState] = useState<"idle" | "busy" | "done" | "error">("idle");
  const [message, setMessage] = useState("");

  async function submit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    const email = new FormData(e.currentTarget).get("email");
    setState("busy");
    try {
      const res = await fetch("/api/waitlist", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ email }) });
      const data = (await res.json().catch(() => ({}))) as { error?: string };
      if (res.ok) {
        track("waitlist_joined");
        setState("done");
        return;
      }
      setState("error");
      setMessage(data.error || "That didn't work. Try again.");
    } catch {
      // No connection: show a message instead of leaving the button on "Joining…".
      setState("error");
      setMessage("That didn't go through. Check your connection and try again.");
    }
  }

  if (state === "done") return <p className="font-semibold">You&apos;re on the list. One email when it&apos;s ready, no spam.</p>;
  return (
    <form onSubmit={submit} className="flex w-full max-w-md flex-col gap-2 sm:flex-row">
      <label htmlFor="email" className="sr-only">Email</label>
      <input id="email" name="email" type="email" required placeholder="you@email.com" className="h-12 flex-1 rounded-full border border-line px-5 text-base outline-none focus:border-accent" />
      <button type="submit" disabled={state === "busy"} className="h-12 rounded-full bg-ink px-5 font-semibold text-white disabled:opacity-60">
        {state === "busy" ? "Joining…" : label}
      </button>
      {state === "error" && <p role="alert" className="text-sm text-red-700 sm:basis-full">{message}</p>}
    </form>
  );
}
