// Checks src/config/pricing.json, the one file the page, the checkout and `npm run plans` read.
// Run with: npm test
import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";

const pricing = JSON.parse(readFileSync(new URL("../src/config/pricing.json", import.meta.url), "utf8"));

test("currency is a three-letter code", () => {
  assert.match(pricing.currency, /^[A-Z]{3}$/);
});

test("every plan has a unique key, a name and a positive price", () => {
  const keys = pricing.plans.map((p) => p.key);
  assert.equal(new Set(keys).size, keys.length, "two plans share a key");
  for (const plan of pricing.plans) {
    assert.ok(plan.key && plan.name, `plan without key or name: ${JSON.stringify(plan)}`);
    assert.ok(typeof plan.price === "number" && plan.price > 0, `${plan.key}: price must be a number above 0`);
  }
});

test("a subscription has a month or year interval; a one-time plan has none", () => {
  for (const plan of pricing.plans) {
    assert.ok(["one_time", "subscription"].includes(plan.type), `${plan.key}: unknown type ${plan.type}`);
    if (plan.type === "subscription") assert.ok(["month", "year"].includes(plan.interval), `${plan.key}: interval must be month or year`);
    else assert.equal(plan.interval, null, `${plan.key}: a one-time plan has no interval`);
  }
});

test("every plan has a place for its test and live ids", () => {
  for (const plan of pricing.plans) {
    assert.equal(typeof plan.linkId?.test, "string", `${plan.key}: linkId.test missing`);
    assert.equal(typeof plan.linkId?.live, "string", `${plan.key}: linkId.live missing`);
  }
});
