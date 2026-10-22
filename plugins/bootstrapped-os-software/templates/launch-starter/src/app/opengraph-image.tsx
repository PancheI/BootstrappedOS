import { ImageResponse } from "next/og";
import { product } from "@/lib/site";

export const size = { width: 1200, height: 630 };
export const contentType = "image/png";
export const alt = product.tagline;

// The link preview for LinkedIn, X and Slack, drawn from the same config as the page.
export default function OG() {
  return new ImageResponse(
    (
      <div style={{ width: "100%", height: "100%", display: "flex", flexDirection: "column", justifyContent: "space-between", padding: 72, background: "#ffffff", color: "#111318" }}>
        <div style={{ fontSize: 34, fontWeight: 700, color: "#4f46e5" }}>{product.name}</div>
        <div style={{ fontSize: 76, fontWeight: 800, lineHeight: 1.05, letterSpacing: -2, maxWidth: 1000 }}>{product.tagline}</div>
        <div style={{ fontSize: 30, color: "#5b6170" }}>{`For ${product.buyer.toLowerCase()}`}</div>
      </div>
    ),
    size,
  );
}
