# Cloudflare Pages with wrangler (static sites)

The author's landing site is plain HTML: a Python build script, Cloudflare Pages, a few Pages Functions. Vercel stays the default for the Next.js app. This is the setup and the traps he hit.

## Build into `dist/`, deploy only `dist/`
- A build script writes `dist/` with only what Pages serves: the HTML, `css/`, `js/`, `img/`, `functions/`, `_headers`, `_redirects`, `robots.txt`, `sitemap.xml`, `llms.txt`. Never deploy the repo root. The `.git` folder alone is about 1,500 files, and the dashboard upload stops at 1,000.
- **The build refuses bad input.** How the author does it: his `build.py` aborts if a page's content file is under 400 bytes or the home page has no `<h1>`. A truncated file once nearly shipped a blank page; now it can't reach `dist/`.

## Preview, then live
```bash
npx wrangler pages deploy dist --project-name <name> --branch preview   # https://preview.<name>.pages.dev
npx wrangler pages deploy dist --project-name <name> --branch main      # the custom domain
```
- **Always pass `--branch main` for live.** Wrangler labels the upload with your local git branch. If that branch is `master` and the project's production branch is `main`, the upload lands in preview while the domain keeps serving the old site, and nothing tells you.
- **Deploy with wrangler, not the dashboard drag-and-drop**, once you have `functions/`. The drag-and-drop doesn't deploy Functions, so `/api/*` returns 404 after it.
- Preview has no KV or secret bindings unless you add them for the Preview environment, so a sign-up form failing on preview is expected. Secrets: `npx wrangler pages secret put <NAME> --project-name <name>`; the founder pastes the value.
- The project name can't be renamed (the author's carries a typo forever). Pick it carefully.

## Security headers: `_headers` plus a middleware
- `_headers` sets `Strict-Transport-Security`, `X-Frame-Options: SAMEORIGIN`, `X-Content-Type-Options: nosniff`, `Referrer-Policy`, `Permissions-Policy`, `Cross-Origin-Opener-Policy` on `/*`, and `Cache-Control: public, max-age=31536000, immutable` on `/css/*` and `/js/*`. Give non-HTML twins (a `.md` page) an explicit `Content-Type` and a `Link: <...>; rel="canonical"`.
- **`_headers` applies to static files only.** How the author found out: an SEO audit showed that pages built by a Function (`/makers/*`) went out with no security headers at all. The fix is `functions/_middleware.js`, which adds the same header set to any response that's missing them:
```js
const SECURITY = { 'Strict-Transport-Security': 'max-age=31536000; includeSubDomains; preload', /* same as _headers */ };
export async function onRequest({ request, next }) {
  const res = await next();
  if (Object.keys(SECURITY).every((k) => res.headers.has(k))) return res;
  const out = new Response(res.body, res);
  for (const [k, v] of Object.entries(SECURITY)) if (!out.headers.has(k)) out.headers.set(k, v);
  return out;
}
```
- The same middleware handles old domains: hosts in a `MOVED` set get a 301 to the primary domain with path and query kept, so shared `?ref=` links and rankings carry over. Leave `*.pages.dev` alone so previews still work.
- Check after deploy: `curl -sI https://<domain>/` and `curl -sI https://<domain>/<function-page>`. Both must show the header set.

## DNS
- Custom domains on Pages each need a **proxied** CNAME to `<name>.pages.dev`. Wrangler's login has no DNS scope, so the founder adds those in the dashboard and you read them back.
- Domain on Cloudflare DNS, app on Vercel: add exactly the records Vercel shows, set to **DNS only** (grey cloud), so Vercel can issue the certificate.

## Next.js on Cloudflare
Only with a reason (the founder already pays for Workers). It needs the `@opennextjs/cloudflare` adapter, a wrangler config and Worker secrets. Read the current OpenNext docs first; don't work from memory. Pin wrangler to a version at least a week old.
