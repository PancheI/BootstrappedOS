import type { MetadataRoute } from "next";
import { siteUrl } from "@/lib/site";

export default function robots(): MetadataRoute.Robots {
  return { rules: [{ userAgent: "*", allow: "/", disallow: ["/api/", "/thanks", "/app", "/login", "/auth/"] }], sitemap: `${siteUrl()}/sitemap.xml` };
}
