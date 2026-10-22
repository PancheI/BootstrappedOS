#!/usr/bin/env node
// Refuses a pricing-audit page that breaks the author's rules. Node 20+, no dependencies.
//
//   node check-audit.mjs knowledge/checks/2026-10-18-pricing-audit.md --stage zero|paying
//
// The rules the author's audits taught: no score, no projection in the
// headline, no uplift percentage at $0, a tagged roast, models with precedents and break-evens,
// a ranking, a 10-day plan, and an independent review with "What changed after".
// Prints OK, or FAILED with every reason. Exit code 0 / 1.
import { existsSync, readFileSync } from "node:fs";

const [file, ...rest] = process.argv.slice(2);
const stageArg = rest[rest.indexOf("--stage") + 1];
if (!file || !rest.includes("--stage") || !["zero", "paying"].includes(stageArg)) {
  console.error("Usage: node check-audit.mjs <audit.md> --stage zero|paying\n  zero = no paying customers yet; paying = real revenue in the payment tool");
  process.exit(2);
}
if (!existsSync(file)) { console.error(`FAILED: no file ${file}`); process.exit(1); }

const raw = readFileSync(file, "utf8");
const text = raw.replace(/```[\s\S]*?```/g, ""); // code blocks are not the page
const lines = text.split("\n");
const problems = [];
const section = (title) => {
  const i = lines.findIndex((l) => l.toLowerCase().startsWith(`## ${title.toLowerCase()}`));
  if (i < 0) return null;
  const j = lines.findIndex((l, k) => k > i && /^#{1,2} /.test(l));
  return lines.slice(i + 1, j < 0 ? undefined : j).join("\n");
};
const tableRows = (s) => (s ?? "").split("\n").filter((l) => l.trim().startsWith("|") && !/^\|\s*-/.test(l.trim()));

// 1. Template left unfilled.
const holes = text.match(/<[^<>\n]*\s[^<>\n]*>/g) ?? [];
if (holes.length) problems.push(`unfilled placeholders: ${holes.slice(0, 3).join(" ")}`);

// 2. House style.
if (/—|&mdash;/.test(text)) problems.push("em dash");

// 3. No score, no grade (the author: "what do I have to change and why this is relevant").
if (/\b(scores?|scored|scoring|grade [a-f]|out of 100)\b|\/\s?100\b/i.test(text)) problems.push("publishes a score or grade");

// 4. The headline is a verified or arithmetic fact.
const h1 = lines.find((l) => l.startsWith("# ")) ?? "";
if (!h1) problems.push("no headline (# line)");
if (/projection|%/i.test(h1)) problems.push("headline carries a projection or a percentage");

// 5. No uplift percentage before there is revenue.
if (stageArg === "zero" && /\+\s?\d+\s?%|\d+\s?%\s+more\b/i.test(text)) problems.push("percentage uplift at $0 (there is no revenue to take a percentage of)");

// 6. The walk.
const walk = section("What a buyer sees");
if (!walk) problems.push('no "## What a buyer sees" section');
else {
  if (!/\b\d{1,2} (jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\w* 20\d\d\b|\b20\d\d-\d\d-\d\d\b/i.test(walk)) problems.push("the walk has no date");
  if (!/where a buyer gets stuck:/i.test(walk)) problems.push('no "Where a buyer gets stuck:" line');
}

// 7. The roast: every line tagged, plus what the buyer gets back.
const roast = section("Why would anyone pay");
if (!roast) problems.push('no "## Why would anyone pay?" section');
else {
  const bullets = roast.split("\n").filter((l) => /^\s*[-*] /.test(l) && !/what they get back/i.test(l));
  if (bullets.length < 2) problems.push("roast needs 2+ lines");
  if (bullets.some((l) => !/\((verified|arithmetic)\)/i.test(l))) problems.push("every roast line needs (verified) or (arithmetic)");
  const back = roast.split("\n").find((l) => /what they get back/i.test(l));
  if (!back || !(/\((verified|arithmetic)\)/i.test(back) || /no verified basis/i.test(back))) problems.push('"What they get back" missing, or not tagged (arithmetic)/(verified) or "no verified basis"');
  if (!/doing nothing|\bDIY\b|spreadsheet|by hand/i.test(text)) problems.push("no do-nothing / DIY alternative");
}

// 8. Models: 2+, each with a precedent and a works-if.
const ways = section("Ways to charge for it");
const header = tableRows(ways)[0] ?? "";
const models = (header.match(/\b[A-D] ·/g) ?? []).length;
if (models < 2) problems.push(`needs 2+ models in "## Ways to charge for it", found ${models}`);
const precedent = tableRows(ways).find((r) => /who already charges this way|precedent/i.test(r));
if (!precedent || precedent.split("|").slice(2, -1).some((c) => !c.trim())) problems.push("a model has no named precedent");
const numbers = section("The numbers");
const worksIf = tableRows(numbers).slice(1).filter((r) => /works if/i.test(r)).length;
if (!numbers || !/\d/.test(numbers)) problems.push('no "## The numbers" table with figures');
else if (worksIf < models) problems.push(`${models} models but ${worksIf} "works if" lines`);

// 9. Ranked by money, one pick, ten days.
if (!/ranked by money:/i.test(text)) problems.push('no "Ranked by money:" line');
if (!/\|\s*When\s*\|\s*Do this\s*\|/i.test(text)) problems.push("no When | Do this plan");

// 10. At $0: the parking lot, and no paid channels for the first ten.
if (stageArg === "zero") {
  if (!/later, once you have paying customers/i.test(text)) problems.push('no "Later, once you have paying customers" parking lot');
  const paid = lines.filter((l) => /paid ads|affiliate program|featured (directory )?slot/i.test(l) && !/\b(not|never|no|won't|don't|without|isn't)\b/i.test(l));
  if (paid.length) problems.push("recommends paid ads, affiliates or featured slots before the first paying customer");
}

// 11. A private sample (products you reviewed, people who came to you) is not market data.
for (const tell of [/small (software )?products we (could check|reviewed|re-walked)/i, /with no revenue evidence/i, /\bnon-earners\b/i, /asking us to review them/i]) {
  if (tell.test(text)) { problems.push(`quotes a private sample (${tell.source}); use the market lines in evidence-checklist.md`); break; }
}

// 12. The independent review.
const review = file.replace(/\.md$/, "-review.md");
if (!existsSync(review)) problems.push(`no independent review: ${review}`);
else {
  const r = readFileSync(review, "utf8");
  if (/pending fixes/i.test(r) || !/^#+\s*what changed after/im.test(r)) problems.push(`review ${review} has open findings (no "What changed after" section)`);
}

if (problems.length) { console.log("FAILED:\n- " + problems.join("\n- ")); process.exit(1); }
console.log(`OK: ${file} (${models} models, stage ${stageArg})`);
