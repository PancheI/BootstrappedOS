"use client";

import Link from "next/link";
import posthog from "posthog-js";
import { useEffect, type ComponentProps, type ReactNode } from "react";

/** The funnel events, one name per step: visit -> CTA -> waitlist or checkout -> paid. The README lists them too. */
export type Event = "cta_clicked" | "product_used" | "waitlist_joined" | "checkout_clicked" | "checkout_failed";

let started = false;

export function Analytics({ children }: { children: ReactNode }) {
  useEffect(() => {
    const key = process.env.NEXT_PUBLIC_POSTHOG_KEY;
    if (!key || started) return;
    posthog.init(key, {
      api_host: process.env.NEXT_PUBLIC_POSTHOG_HOST || "https://eu.i.posthog.com",
      // Cookieless: nothing is stored in the visitor's browser, so no cookie banner is needed.
      // A visitor counts as new on each full page load; that's the trade-off. Match the privacy page if you change it.
      persistence: "memory",
      person_profiles: "identified_only",
    });
    started = true;
  }, []);
  return <>{children}</>;
}

export function track(event: Event, props?: Record<string, string | number>) {
  if (started) posthog.capture(event, props);
}

/** A link that sends `cta_clicked` with its name, so you can see which button people press. */
export function CtaLink({ name, onClick, ...props }: ComponentProps<typeof Link> & { name: string }) {
  return <Link {...props} onClick={(e) => { track("cta_clicked", { name }); onClick?.(e); }} />;
}
