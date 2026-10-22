import Link from "next/link";
import type { ReactNode } from "react";
import { product } from "@/lib/site";

export function Frame({ children }: { children: ReactNode }) {
  return (
    <div className="flex min-h-dvh flex-col">
      <header className="border-b border-line">
        <nav className="mx-auto flex max-w-5xl items-center justify-between px-5 py-4">
          <Link href="/" className="font-display text-lg font-bold no-underline">{product.name}</Link>
          <div className="flex items-center gap-5 text-sm">
            <Link href="/product" className="no-underline hover:underline">Try it</Link>
            <Link href="/#pricing" className="no-underline hover:underline">Pricing</Link>
            <Link href="/app" className="no-underline hover:underline">Sign in</Link>
          </div>
        </nav>
      </header>
      <main className="flex-1">{children}</main>
      <footer className="border-t border-line">
        <div className="mx-auto flex max-w-5xl flex-wrap items-center justify-between gap-3 px-5 py-6 text-sm text-soft">
          <span>© {new Date().getFullYear()} {product.legal.company}</span>
          <span className="flex flex-wrap gap-4">
            {product.madeWith && (
              // Credit for the open-source kit this site started from. Set "madeWith": false in product.json to remove it.
              <a href="https://bootstrappedmakers.com/bootstrapped-os?ref=made-with">Made with Bootstrapped OS</a>
            )}
            <Link href="/privacy">Privacy</Link>
            <Link href="/terms">Terms</Link>
            <a href={`mailto:${product.legal.email}`}>Contact</a>
          </span>
        </div>
      </footer>
    </div>
  );
}
