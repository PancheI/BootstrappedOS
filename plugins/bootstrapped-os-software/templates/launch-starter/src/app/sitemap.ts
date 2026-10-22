import type { MetadataRoute } from "next";
import { siteUrl } from "@/lib/site";

export default function sitemap(): MetadataRoute.Sitemap {
  const now = new Date();
  return ["", "/product", "/privacy", "/terms"].map((p) => ({ url: `${siteUrl()}${p}`, lastModified: now }));
}
