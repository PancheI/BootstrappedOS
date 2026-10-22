import React from "react";
import { AbsoluteFill, useCurrentFrame } from "remotion";
import { Audio } from "@remotion/media";
import { staticFile } from "remotion";
import { FONT, T, type Shot } from "./core";
import { G1_SHOTS } from "./shots/G1";
import { G2_SHOTS } from "./shots/G2";
import { G3_SHOTS } from "./shots/G3";
import { G4_SHOTS } from "./shots/G4";
import { getRemoteFile } from "./audio";

import { FRAMES } from "./core";
export { FPS as REMAKE_FPS } from "./core";

/**
 * Timeline edits, in REF frames. Keep remake/audio/timeline.py and remake/tools/stretches.json equal to these.
 * STRETCHES (e.g. "stay longer on a screen the viewer must read"): REF [S0, S1] plays EXT frames longer
 *   (EXT < 0 = faster), and everything after it shifts by EXT.
 * CUTS ("too long", "we say this twice"): REF [C0, C1] is removed, and everything after it shifts back.
 * Keep every EXT and every cut length a whole number of music beats (60 * fps / BPM * n frames; at 144 BPM and
 * 60 fps one beat is 25 frames), so the music stays on its grid.
 * "RemakeLocked" keeps the REF-locked timeline for the compare and sync tools.
 */
export const STRETCHES: { S0: number; S1: number; EXT: number }[] = [
	// e.g. { S0: 300, S1: 360, EXT: 100 }, // hold 4 beats on a screen the viewer must read
];
export const CUTS: { C0: number; C1: number }[] = [
	// e.g. { C0: 1200, C1: 1599 }, // remove 16 beats the story doesn't need
];
const TOTAL_EXT = STRETCHES.reduce((a, s) => a + s.EXT, 0);
const TOTAL_CUT = CUTS.reduce((a, c) => a + (c.C1 - c.C0 + 1), 0);
export const REMAKE_FRAMES = FRAMES + TOTAL_EXT - TOTAL_CUT;
export const REMAKE_LOCKED_FRAMES = FRAMES;

type Edit = { kind: "s"; a: number; b: number; ext: number } | { kind: "c"; a: number; b: number };
const EDITS: Edit[] = [
	...STRETCHES.map((s) => ({ kind: "s" as const, a: s.S0, b: s.S1, ext: s.EXT })),
	...CUTS.map((c) => ({ kind: "c" as const, a: c.C0, b: c.C1 })),
].sort((x, y) => x.a - y.a);

/** Output frame -> REF-timeline frame. Applies stretches and cuts in REF order (same as timeline.py). */
export const toRef = (F: number) => {
	let shift = 0;
	for (const e of EDITS) {
		if (e.kind === "s") {
			const o0 = e.a + shift, o1 = e.b + shift + e.ext;
			if (F <= o0) return F - shift;
			if (F <= o1) return e.a + ((F - o0) * (e.b - e.a)) / (e.b - e.a + e.ext);
			shift += e.ext;
		} else {
			if (F < e.a + shift) return F - shift;
			shift -= e.b - e.a + 1;
		}
	}
	return F - shift;
};

const SHOTS: Shot[] = [...G1_SHOTS, ...G2_SHOTS, ...G3_SHOTS, ...G4_SHOTS].sort((a, b) => a.f0 - b.f0);

/** Routes global frame F to every shot whose [f0, f1] contains it (overlaps render in registry order). */
export const Remake: React.FC<{ muted?: boolean; locked?: boolean }> = ({ muted, locked }) => {
	const out = useCurrentFrame();
	const F = locked ? out : toRef(out);
	const live = SHOTS.filter((s) => F >= s.f0 && F <= s.f1);
	return (
		<AbsoluteFill style={{ background: T.white, fontFamily: FONT, color: T.ink, overflow: "hidden" }}>
			{live.map((s) => <AbsoluteFill key={s.id}>{s.render(F - s.f0, F)}</AbsoluteFill>)}
			{!muted && getRemoteFile() && <Audio src={staticFile(getRemoteFile()!)} />}
		</AbsoluteFill>
	);
};
