/**
 * Multi-reference router (template, untested end-to-end — first real use should verify with RemakeLocked<X> compares).
 *
 * EDL = the cut list. Each segment plays reference `ref` frames [f0, f1] starting at output frame out0,
 * optionally slowed by `ext` extra output frames (a whole-beat hold, like STRETCHES in Remake.tsx).
 * Shots declare which reference timeline they live in: { id, ref: "A", f0, f1, render(lf, F) } with f0/f1 in
 * THAT reference's frames. Segments must be contiguous in output time (out0 of next = previous end + 1).
 *
 * Root.tsx:
 *   <Composition id="Remake" component={RemakeMulti} durationInFrames={EDL_FRAMES} fps={60} width={1920} height={1080} />
 *   // one locked comp per reference, for compare/sync tools (COMP=RemakeLockedB REF=B node render.mjs …)
 *   <Composition id="RemakeLockedA" component={RemakeMulti} defaultProps={{ lockedRef: "A", muted: true }} durationInFrames={REF_FRAMES.A} … />
 */
import React from "react";
import { AbsoluteFill, staticFile, useCurrentFrame } from "remotion";
import { Audio } from "@remotion/media";
import { FONT, T } from "./core";
import { getRemoteFile } from "./audio";

export type RefShot = { id: string; ref: string; f0: number; f1: number; render: (lf: number, F: number) => React.ReactNode };
export type Seg = { ref: string; f0: number; f1: number; out0: number; ext?: number };

// ── fill these in from the approved beat-picking table ──
export const EDL: Seg[] = [
	// { ref: "A", f0: 0, f1: 419, out0: 0 },            // spine: opening
	// { ref: "B", f0: 610, f1: 790, out0: 420, ext: 0 }, // donor hook, restyled to A's look
	// { ref: "A", f0: 420, f1: 1311, out0: 601 },
];
export const REF_FRAMES: Record<string, number> = { /* A: 4246, B: 1800 */ };
export const SHOTS: RefShot[] = [ /* ...A_SHOTS, ...B_SHOTS */ ];

const segLen = (s: Seg) => s.f1 - s.f0 + 1 + (s.ext ?? 0);
export const EDL_FRAMES = EDL.reduce((a, s) => Math.max(a, s.out0 + segLen(s)), 0);

/** Output frame → { ref, F } (F fractional inside an ext hold). */
export const toRefEDL = (out: number): { ref: string; F: number } | null => {
	for (const s of EDL) {
		const len = segLen(s);
		if (out >= s.out0 && out < s.out0 + len) {
			const k = out - s.out0;
			const F = s.ext ? s.f0 + (k * (s.f1 - s.f0)) / (len - 1) : s.f0 + k;
			return { ref: s.ref, F };
		}
	}
	return null;
};

export const RemakeMulti: React.FC<{ muted?: boolean; lockedRef?: string }> = ({ muted, lockedRef }) => {
	const out = useCurrentFrame();
	const pos = lockedRef ? { ref: lockedRef, F: out } : toRefEDL(out);
	const live = pos ? SHOTS.filter((s) => s.ref === pos.ref && pos.F >= s.f0 && pos.F <= s.f1).sort((a, b) => a.f0 - b.f0) : [];
	return (
		<AbsoluteFill style={{ background: T.white, fontFamily: FONT, color: T.ink, overflow: "hidden" }}>
			{pos && live.map((s) => <AbsoluteFill key={s.id}>{s.render(pos.F - s.f0, pos.F)}</AbsoluteFill>)}
			{!muted && !lockedRef && getRemoteFile() && <Audio src={staticFile(getRemoteFile()!)} />}
		</AbsoluteFill>
	);
};
