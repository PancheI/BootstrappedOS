import type { Metadata } from "next";
import { Manrope, Space_Grotesk } from "next/font/google";
import type { ReactNode } from "react";
import { Analytics } from "@/lib/analytics";
import { product, siteUrl } from "@/lib/site";
import "./globals.css";

const body = Manrope({ subsets: ["latin"], variable: "--font-body" });
const head = Space_Grotesk({ subsets: ["latin"], variable: "--font-head" });

export const metadata: Metadata = {
  metadataBase: new URL(siteUrl()),
  title: `${product.name}: ${product.tagline}`,
  description: product.promise,
  alternates: { canonical: "/" },
  openGraph: { title: product.name, description: product.tagline, type: "website" },
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en" className={`${body.variable} ${head.variable}`}>
      <body>
        <Analytics>{children}</Analytics>
      </body>
    </html>
  );
}
