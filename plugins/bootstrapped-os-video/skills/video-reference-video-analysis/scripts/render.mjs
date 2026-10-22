// Remotion frame renderer for the remake. One browser, many frames.
//   node <tools>/render.mjs <OUTDIR> stills <f,f,...|a-b>      → OUTDIR/o<F>.jpg
//   node <tools>/render.mjs <OUTDIR> compare <f,f,...>         → stills + OUTDIR/compare.jpg (REF left | ours right, labelled, diff score)
//   node <tools>/render.mjs <OUTDIR> full <f0> <f1>            → OUTDIR/seq/o<F>.jpg for every frame
// Bundles src/index.ts into OUTDIR/bundle each call unless NOBUNDLE=1. ≤15 frames per stills/compare call.
import { createRequire } from "module";
import fs from "fs";
import path from "path";
import { execFileSync } from "child_process";
// Run from your Remotion project root (or set PROJECT_ROOT). compare.py is looked up next to this file.
const here = path.dirname(new URL(import.meta.url).pathname);
const root = path.resolve(process.env.PROJECT_ROOT || process.cwd());
const req = createRequire(fs.realpathSync(path.join(root, "node_modules/@remotion/cli/package.json")));
const { bundle } = req("@remotion/bundler");
const { renderStill, selectComposition, openBrowser, renderFrames } = req("@remotion/renderer");
const [OUT, mode, a, b] = process.argv.slice(2);
if (!OUT || !mode) { console.error("usage: render.mjs OUTDIR stills|compare|full frames"); process.exit(1); }
fs.mkdirSync(OUT, { recursive: true });
const parse = (s) => s.includes("-") && !s.includes(",") ? (() => { const [x, y] = s.split("-").map(Number); return Array.from({ length: y - x + 1 }, (_, i) => x + i); })() : s.split(",").map(Number);
const bdir = path.resolve(OUT, "bundle");
let serveUrl = bdir;
if (process.env.NOBUNDLE !== "1" || !fs.existsSync(bdir)) serveUrl = await bundle({ entryPoint: path.join(root, "src/index.ts"), outDir: bdir, publicDir: path.join(root, "public"), onProgress: () => {} });
const browser = await openBrowser("chrome");
const composition = await selectComposition({ serveUrl, id: process.env.COMP || "RemakeLocked", puppeteerInstance: browser, logLevel: "error" });
if (mode === "full") {
	const f0 = +a, f1 = +b; const seq = path.join(OUT, "seq"); fs.mkdirSync(seq, { recursive: true });
	await renderFrames({ serveUrl, composition, puppeteerInstance: browser, frameRange: [f0, f1], imageFormat: "jpeg", jpegQuality: 92, outputDir: seq, concurrency: 3, logLevel: "error", onStart: () => {}, onFrameUpdate: () => {}, onError: (e) => console.log("ERR:", e.message) });
	console.log("full", f0, f1, "→", seq);
} else {
	const frames = parse(a);
	if (frames.length > 15) console.log("WARN: >15 frames per call");
	for (const F of frames) {
		await renderStill({ serveUrl, composition, frame: F, output: path.join(OUT, `o${F}.jpg`), imageFormat: "jpeg", jpegQuality: 92, puppeteerInstance: browser, logLevel: "error", onBrowserLog: (l) => l.type === "error" && console.log("page:", l.text) });
		console.log("still", F);
	}
	if (mode === "compare") execFileSync("python3", [path.join(here, "compare.py"), OUT, ...frames.map(String)], { stdio: "inherit" });
}
await browser.close({ silent: true });
