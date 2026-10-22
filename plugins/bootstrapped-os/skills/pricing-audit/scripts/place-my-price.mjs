#!/usr/bin/env node
// Place one founder's price against the market benchmarks. Node 20+, no dependencies.
//
//   node place-my-price.mjs --price 19 --model subscription --interval month --mrr 0 \
//        [--yearly yes|no] [--trial none|free|card] [--benchmarks <file.json>]
//
// The normal path: no benchmarks file. The script prints the arithmetic it can do on the
// founder's own price and says "live precedents only"; the audit backs each check with
// public pricing pages read that day. The benchmark figures live in the Bootstrapped core
// (members): the agent saves the core's `evidence` answer (topic: pricing) as JSON and
// passes it with --benchmarks. With it, the script prints market facts only, each with its
// n and "correlation only". It never tells the founder what to charge.
import { existsSync, readFileSync } from "node:fs";

const USAGE = `Usage: node place-my-price.mjs --price <number> --model subscription|one-time|lifetime|credits|usage
       --interval month|year|once --mrr <monthly revenue now, USD> [--yearly yes|no] [--trial none|free|card]
       [--benchmarks <file.json>]   optional: the core's pricing evidence saved as JSON (members)
Without --benchmarks the script uses live precedents only. That is the normal path.`;
const GAP = 10; // percentage points; smaller gaps are reported as "no clear gap"

function parseArgs(argv) {
  const a = {};
  if (argv.length === 0 || argv.includes("--help") || argv.includes("-h")) return null;
  for (let i = 0; i < argv.length; i += 2) {
    if (!argv[i]?.startsWith("--")) throw new Error(`Unexpected argument: ${argv[i]}`);
    a[argv[i].slice(2)] = argv[i + 1];
  }
  const price = Number(a.price), mrr = Number(a.mrr);
  if (!(price > 0)) throw new Error("--price must be a number above 0");
  if (!(mrr >= 0)) throw new Error("--mrr must be 0 or more");
  const model = a.model ?? "subscription";
  const interval = a.interval ?? (["one-time", "lifetime"].includes(model) ? "once" : "month");
  if (!["subscription", "one-time", "lifetime", "credits", "usage"].includes(model)) throw new Error(`Unknown --model ${model}`);
  if (!["month", "year", "once"].includes(interval)) throw new Error(`Unknown --interval ${interval}`);
  if (a.yearly && !["yes", "no"].includes(a.yearly)) throw new Error("--yearly is yes or no");
  if (a.trial && !["none", "free", "card"].includes(a.trial)) throw new Error("--trial is none, free or card");
  return { price, mrr, model, interval, yearly: a.yearly, trial: a.trial, benchmarks: a.benchmarks };
}

const BANDS = ["$0", "under $200", "$200-999", "$1k-5k", "$5k+"];
const bandOf = (m) => (m <= 0 ? 0 : m < 200 ? 1 : m < 1000 ? 2 : m < 5000 ? 3 : 4);
const PRICE_BANDS = ["under $10", "$10-19", "$20-49", "$50+"];
const priceBandOf = (x) => (x < 10 ? 0 : x < 20 ? 1 : x < 50 ? 2 : 3);
const ok = (cell) => cell && !cell.suppressed && cell.n != null;
const usd = (x) => `$${Number.isInteger(x) ? x : x.toFixed(2)}`;
const tag = (n) => `(n = ${n}, correlation only)`;

// Percentile of `x` within a stored quantile set {p10, p20, ..., median, ..., p90}.
function percentileOf(cell, x) {
  const pts = Object.entries(cell).filter(([k]) => /^p\d+$|^median$/.test(k))
    .map(([k, v]) => [k === "median" ? 50 : Number(k.slice(1)), v]).sort((a, b) => a[0] - b[0]);
  const [lo, hi] = [pts[0], pts[pts.length - 1]];
  if (x < lo[1]) return `below the ${lo[0]}th percentile`;
  if (x > hi[1]) return `above the ${hi[0]}th percentile`;
  const equal = pts.filter(([, v]) => v === x).map(([p]) => p);
  if (equal.length > 1) return `between the ${equal[0]}th and ${equal[equal.length - 1]}th percentile (many sit exactly here)`;
  if (equal.length === 1) return `at about the ${equal[0]}th percentile`;
  for (let i = 1; i < pts.length; i++) {
    const [p0, v0] = pts[i - 1], [p1, v1] = pts[i];
    if (x >= v0 && x <= v1) return `at about the ${Math.round(p0 + ((x - v0) / (v1 - v0)) * (p1 - p0))}th percentile`;
  }
  return "inside the range";
}

function compareLine(label, mine, next, myBand, nextBand, founderHas) {
  if (!ok(mine) || !ok(next)) return `- ${label}: not enough data at one of the two stages (n < 20).`;
  const gap = next.pct - mine.pct;
  const you = founderHas == null ? "" : founderHas ? " Yours: yes." : " Yours: no.";
  const nums = `${next.pct}% at ${nextBand} vs ${mine.pct}% at ${myBand} (n = ${next.n} / ${mine.n}, correlation only)`;
  if (Math.abs(gap) < GAP) return `- ${label}: no clear gap, ${nums}. The data doesn't point either way.${you}`;
  return `- ${label}: ${gap > 0 ? "more" : "less"} common one stage up, ${nums}.${you}`;
}

function main() {
  let a;
  try { a = parseArgs(process.argv.slice(2)); } catch (e) { console.error(`${e.message}\n${USAGE}`); process.exit(1); }
  if (a === null) { console.log(USAGE); process.exit(0); }
  const recurringPrice = a.interval !== "once";
  const perMonth = a.interval === "year" ? a.price / 12 : a.price;
  if (!a.benchmarks) {
    const lines = ["Live precedents only (no benchmarks file; the market figures are in the Bootstrapped core for members)."];
    if (a.mrr < 1000) {
      if (recurringPrice) lines.push(`- $1,000 a month at ${usd(+perMonth.toFixed(2))}/month = ${Math.ceil(1000 / perMonth)} paying subscribers (arithmetic).`);
      else lines.push(`- $1,000 a month at ${usd(a.price)} each = ${Math.ceil(1000 / a.price)} sales every month (arithmetic).`);
    }
    lines.push("- Back checks 2, 4, 5 and 6 with public pricing pages read today, dated.");
    console.log(lines.join("\n"));
    process.exit(0);
  }
  if (!existsSync(a.benchmarks)) { console.error(`No file at ${a.benchmarks}. Save the core's pricing evidence there first, or run without --benchmarks.`); process.exit(1); }
  const file = a.benchmarks;
  const B = JSON.parse(readFileSync(file, "utf8"));
  const cells = B.revenue_bands.cells;
  const bi = bandOf(a.mrr), ni = Math.min(bi + 1, BANDS.length - 1);
  const mine = cells[bi], next = cells[ni];
  const recurring = a.interval !== "once";
  const monthly = a.interval === "year" ? a.price / 12 : a.price;
  const out = [];

  out.push(`Where your price sits. Market data built ${B.dataset_built.slice(0, 10)} from ${B.sources[0].label}.`);
  out.push(`Market facts, not advice: founders who show revenue are not all founders, and earners are older. Prices compared as USD list prices.`, "");
  out.push(`- Your stage: ${mine.band} a month. ${mine.startups_in_band} listed startups sit here ${tag(mine.startups_in_band)}.`);
  const target = ni === bi ? "your own stage" : `the next stage up (${next.band})`;

  // Price placement against earners one band up.
  if (recurring && (a.model === "subscription" || a.model === "credits" || a.model === "usage")) {
    const ep = next.entry_monthly_price_usd;
    const per = a.interval === "year" ? ` (${usd(a.price)}/year = ${usd(+monthly.toFixed(2))}/month)` : "";
    if (ok(ep)) out.push(`- Your entry price${per} is ${percentileOf(ep, monthly)} of cheapest monthly prices among products at ${target}; their median is ${usd(ep.median)} ${tag(ep.n)}.`);
    else out.push(`- Entry price at ${target}: not enough walked pricing pages (n < 20).`);
    const ps = next.price_per_subscriber_usd_month;
    if (ok(ps)) {
      const where = monthly < ps.p25 ? "below the middle half" : monthly > ps.p75 ? "above the middle half" : "inside the middle half";
      out.push(`- What subscribers actually pay at ${target}: median ${usd(ps.median)} a month each, middle half ${usd(ps.p25)}-${usd(ps.p75)}. Your ${usd(+monthly.toFixed(2))} is ${where} ${tag(ps.n)}.`);
    }
    const pb = B.entry_price_bands.cells[priceBandOf(monthly)];
    const all = B.entry_price_bands.cells.filter((c) => ok(c.share_earning)).map((c) => c.share_earning.pct);
    if (ok(pb.share_earning)) {
      const spread = Math.max(...all) - Math.min(...all);
      const flat = spread < GAP ? ` Across all price bands it runs ${Math.min(...all)}-${Math.max(...all)}%, so a lower price doesn't go with more founders earning.` : "";
      const rev = ok(pb.monthly_revenue_of_earners_usd) ? ` Those earning at this price make a median ${usd(pb.monthly_revenue_of_earners_usd.median)} a month (n = ${pb.monthly_revenue_of_earners_usd.n}).` : "";
      out.push(`- Products starting at ${pb.band}: ${pb.share_earning.pct}% earn something ${tag(pb.share_earning.n)}.${flat}${rev}`);
    }
  } else {
    out.push(`- Price placement is only computed for recurring prices; the walked sample has too few one-time prices per stage.`);
  }

  // What is more or less common one stage up.
  if (ni !== bi) {
    out.push("", `What products one stage up (${next.band}) do differently from ${mine.band}:`);
    out.push(compareLine("Yearly plan", mine.share_offering_yearly, next.share_offering_yearly, mine.band, next.band, a.yearly ? a.yearly === "yes" : null));
    out.push(compareLine("Card up front on the trial", mine.share_card_up_front_trial, next.share_card_up_front_trial, mine.band, next.band, a.trial ? a.trial === "card" : null));
    out.push(compareLine("Any trial", mine.share_any_trial, next.share_any_trial, mine.band, next.band, a.trial ? a.trial !== "none" : null));
    out.push(compareLine("Free tier", mine.share_with_free_tier, next.share_with_free_tier, mine.band, next.band, null));
    out.push(compareLine("Subscription", mine.share_subscription, next.share_subscription, mine.band, next.band, a.model === "subscription"));
    out.push(compareLine("One-time or lifetime only", mine.share_one_time_or_lifetime_only, next.share_one_time_or_lifetime_only, mine.band, next.band, ["one-time", "lifetime"].includes(a.model)));
  }

  // $1,000 a month at this price.
  const c = B.charges_per_1000_month;
  out.push("");
  if (a.mrr >= 1000) { /* already past a $1,000 month: the line would say nothing */ }
  else if (recurring) out.push(`- $1,000 a month at ${usd(+monthly.toFixed(2))}/month = ${Math.ceil(1000 / monthly)} paying subscribers (arithmetic). Real $1,000 months took a median of ${c.charges.median} charges, middle half ${c.charges.p25}-${c.charges.p75} ${tag(c.months)}.`);
  else out.push(`- $1,000 a month at ${usd(a.price)} each = ${Math.ceil(1000 / a.price)} sales every month (arithmetic). Real $1,000 months took a median of ${c.charges.median} charges ${tag(c.months)}.`);

  // Timing, for the stage they are at.
  if (bi === 0 && ok(B.time_to_first_sale)) {
    const t = B.time_to_first_sale;
    out.push(`- First sale: ${t.within_30_days_pct}% made it within a month of founding, ${t.within_90_days_pct}% within three, ${t.within_365_days_pct}% within a year ${tag(t.n)}. Slow is common, not a verdict.`);
  } else if (bi < 3 && B.first_sale_to_1000_month) {
    const f = B.first_sale_to_1000_month, r = f.of_those_reaching;
    out.push(`- After a first sale, ${f.reached_1k_month_pct}% reached a $1,000 month (n = ${f.n})${ok(r) ? `; those that did took a median of ${r.median_months_after_first_sale} months, ${r.within_6_months_pct}% within 6 (n = ${r.n})` : ""}. Correlation only.`);
  }
  const pc = B.price_changes_after_launch;
  if (ok(pc) && ok(pc.changed_entry_price)) out.push(`- Changing price is normal: ${pc.changed_entry_price.pct}% of public launches changed their entry price within about ${pc.median_days_between_walks} days, ${pc.changed_any_pricing_field.pct}% changed some part of their pricing ${tag(pc.n)}.`);

  console.log(out.join("\n"));
}

main();
