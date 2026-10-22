/**
 * Remake engine: a frame-locked remake of REF (remake/ref/reference.mp4, 1920×1080 @ 60fps; set FRAMES from SPEC.md).
 * Every shot renders as a PURE function of the global frame F: no timers, no Date, no Math.random, no CSS
 * transitions/animations. Shots register { id, f0, f1, render(lf, F) } and <Remake> routes F to them.
 *
 * Shared API (shots import only from here — ask the lead for changes, never edit this file from a shot group):
 *   FPS W H FRAMES           constants
 *   T                        your brand tokens, from knowledge/brand/brief.md (palette swap table in SPEC.md)
 *   FONT                     your brand font from knowledge/brand/brief.md (Poppins is only a placeholder), weights 400/500/600/700
 *   E.*                      easings (linear, inOut, out, in, outBack, expoOut, expoIn, expoInOut, bezier)
 *   kf(F, keys, ease?)       keyframes [[frame, value], ...] with per-segment easing (ease or ease[] per segment)
 *   samples(F, f0, arr)      linearly interpolate a measured per-frame array starting at frame f0 (clamped)
 *   clamp01, lerp, mix
 *   <Camera scale tx ty origin blur rot>  2D camera wrapper (translate then scale around origin)
 *   <GridBg ox oy tint cells> the 160px grid background with tinted cells (ox/oy = pan offset in px)
 *   <Cursor x y press>       arrow cursor, tip at (x,y); press 0..1 scales per ref press curve
 *   <Ripple x y t color>     click ripple, t 0..1
 *   <Logo size fill>         your brand mark (ICON) as a mask, so any fill/gradient works
 *   <Wordmark size>          mark + BRAND_NAME in FONT
 *   <Reveal text lf at ...>  per-character text reveal (fade + rise + blur), matches ref "typing-ish" reveals
 *   Avatar(seed)             AI portrait from public/remake/faces/ if you add some (FACES > 0), else an initials disc
 *   hash(n)                  seeded deterministic hash 0..1
 *   R(name)                  staticFile for your real UI screens (public/assets/brand/screens/<name>.png)
 */
import React from "react";
import { Easing, Img, staticFile } from "remotion";
// Placeholder: swap Poppins for the font in knowledge/brand/brief.md.
import { loadFont } from "@remotion/google-fonts/Poppins";

export const FPS = 60;
export const W = 1920;
export const H = 1080;
export const FRAMES = 2100; // REF frame count from SPEC.md (2100 = the 35 s example in timeline.py)

export const { fontFamily: FONT } = loadFont("normal", { weights: ["400", "500", "600", "700"], subsets: ["latin"] });

/* Palette: your brand from knowledge/brand/brief.md (the brand stage), mapped onto REF's roles.
 * Measure REF's colours into SPEC.md's swap table, then set each role here. Keep REF's LIGHTNESS per role.
 * The values below are neutral placeholders. */
export const T = {
	ink: "#12182C", // text
	white: "#FFFFFF", // background
	gridLine: "rgba(18,24,44,0.035)",
	gridCell: "rgba(18,24,44,0.03)",
	platform: "#1D6FE0", // a generic social-platform UI colour (no other brand's logo or name)
	platformText: "#1A66CF",
	brand: "#4F46E5", // your primary colour
	brand2: "#14B8D4", // your second colour
	brandGrad: "linear-gradient(90deg, #4F46E5 0%, #2F7FE3 55%, #14B8D4 100%)",
	tintA: "#E6E4FB", // light tint of brand
	tintB: "#DDF3F8", // light tint of brand2
	tintMid: "#EEF0FC",
	red: "#E5484D", // semantic red stays (errors, notifications)
	green: "#16A34A",
	muted: "#8A90A2",
	card: "#FFFFFF",
	cardShadow: "0 18px 50px rgba(18,24,44,0.10), 0 2px 6px rgba(18,24,44,0.06)",
};

/* Your brand: put your real icon and product screenshots in public/assets/brand/. Never redraw the logo. */
export const BRAND_NAME = "YourBrand";
export const ICON_ASPECT = 1; // icon height / width
export const R = (name: string) => staticFile(`assets/brand/screens/${name}.png`);
export const ICON = staticFile("assets/brand/icon.png");

/* ─── math ─── */
export const clamp01 = (x: number) => Math.max(0, Math.min(1, x));
export const lerp = (a: number, b: number, t: number) => a + (b - a) * t;
export const mix = (F: number, f0: number, f1: number) => clamp01((F - f0) / (f1 - f0));
export const hash = (n: number) => { const s = Math.sin(n * 127.1 + 311.7) * 43758.5453; return s - Math.floor(s); };

export const E = {
	linear: (t: number) => t,
	inOut: Easing.bezier(0.45, 0, 0.55, 1),
	out: Easing.bezier(0.22, 1, 0.36, 1),
	in: Easing.bezier(0.55, 0, 1, 0.45),
	outBack: Easing.bezier(0.34, 1.56, 0.64, 1),
	expoOut: Easing.bezier(0.16, 1, 0.3, 1),
	expoIn: Easing.bezier(0.7, 0, 0.84, 0),
	expoInOut: Easing.bezier(0.87, 0, 0.13, 1),
	bezier: Easing.bezier,
};
type Ease = (t: number) => number;

/** Keyframes: kf(F, [[f,v],...], ease | ease[]) — value held outside the range. */
export function kf(F: number, keys: [number, number][], ease: Ease | Ease[] = E.inOut): number {
	if (F <= keys[0][0]) return keys[0][1];
	for (let i = 1; i < keys.length; i++) {
		if (F <= keys[i][0]) {
			const [fa, va] = keys[i - 1], [fb, vb] = keys[i];
			const e = Array.isArray(ease) ? ease[i - 1] ?? E.inOut : ease;
			return lerp(va, vb, e(clamp01((F - fa) / (fb - fa))));
		}
	}
	return keys[keys.length - 1][1];
}

/** Measured per-frame track: arr[i] is the value at frame f0+i. Fractional F interpolates, outside clamps. */
export function samples(F: number, f0: number, arr: number[]): number {
	const i = F - f0;
	if (i <= 0) return arr[0];
	if (i >= arr.length - 1) return arr[arr.length - 1];
	const k = Math.floor(i);
	return lerp(arr[k], arr[k + 1], i - k);
}

/* ─── components ─── */
export const Camera: React.FC<{ scale?: number; tx?: number; ty?: number; rot?: number; origin?: [number, number]; blur?: number; children: React.ReactNode; style?: React.CSSProperties }> = ({ scale = 1, tx = 0, ty = 0, rot = 0, origin = [W / 2, H / 2], blur = 0, children, style }) => (
	<div style={{ position: "absolute", left: 0, top: 0, width: W, height: H, transformOrigin: `${origin[0]}px ${origin[1]}px`, transform: `translate(${tx}px, ${ty}px) scale(${scale}) rotate(${rot}deg)`, filter: blur > 0.05 ? `blur(${blur}px)` : undefined, ...style }}>{children}</div>
);

/** Background grid, measured from REF f0: 160px cells, lines at x = 140 + 160k, y = 138 + 160k (before pan). */
export const GridBg: React.FC<{ ox?: number; oy?: number; base?: string; tint?: number; cells?: [number, number, number][]; scale?: number }> = ({ ox = 0, oy = 0, base = T.white, tint = 1, cells = DEFAULT_CELLS, scale = 1 }) => {
	const C = 160 * scale;
	const x0 = ((((140 * scale + ox) % C) + C) % C) - C, y0 = ((((138 * scale + oy) % C) + C) % C) - C;
	const lines: React.ReactNode[] = [];
	for (let x = x0; x < W + C; x += C) lines.push(<div key={"x" + x} style={{ position: "absolute", left: x, top: 0, width: 2, height: H, background: T.gridLine }} />);
	for (let y = y0; y < H + C; y += C) lines.push(<div key={"y" + y} style={{ position: "absolute", left: 0, top: y, width: W, height: 2, background: T.gridLine }} />);
	return (
		<div style={{ position: "absolute", inset: 0, background: base, overflow: "hidden" }}>
			{cells.map(([cx, cy, a], i) => {
				const x = 140 * scale + ox + (cx - 1) * C, y = 138 * scale + oy + (cy - 1) * C;
				return <div key={i} style={{ position: "absolute", left: x, top: y, width: C, height: C, background: `rgba(18,24,44,${0.028 * a * tint})` }} />;
			})}
			{lines}
		</div>
	);
};
// [col,row,alpha] in grid units relative to the line at x=140,y=138 (col 0 = the cell left of it). Measured from REF f0.
const DEFAULT_CELLS: [number, number, number][] = [[4, 0, 1], [0, 1, 0.9], [6, 1, 0.5], [8, 0, 0.6], [9, 0, 1], [6, 2, 0.5], [9, 2, 0.6], [-1, 3, 0.5], [10, 3, 0.5], [3, 4, 1], [7, 4, 1], [1, 5, 0.6], [7, 5, 1], [8, 5, 1]];

/** Arrow cursor; tip at (x,y). press 0..1 → scale 1..0.86 (REF press curve). */
export const Cursor: React.FC<{ x: number; y: number; press?: number; size?: number; color?: string }> = ({ x, y, press = 0, size = 30, color = T.ink }) => (
	<svg width={size} height={size * 1.2} viewBox="0 0 20 24" style={{ position: "absolute", left: x - size * 0.1, top: y - size * 0.05, transformOrigin: "10% 5%", transform: `scale(${1 - 0.14 * press})`, filter: "drop-shadow(0 3px 5px rgba(0,0,0,.22))", zIndex: 1000 }}>
		<path d="M2 1 L2 19 L6.6 14.8 L9.6 21.8 L12.6 20.5 L9.6 13.6 L16 13.6 Z" fill={color} stroke="#fff" strokeWidth={1.4} strokeLinejoin="round" />
	</svg>
);
/** The REF also uses an outline "send" style paper-plane cursor in places — shots draw it themselves when needed. */

export const Ripple: React.FC<{ x: number; y: number; t: number; color?: string; r?: number }> = ({ x, y, t, color = T.brand, r = 60 }) => {
	if (t <= 0 || t >= 1) return null;
	const k = E.out(t);
	return <div style={{ position: "absolute", left: x - r * k, top: y - r * k, width: 2 * r * k, height: 2 * r * k, borderRadius: "50%", border: `3px solid ${color}`, opacity: 1 - t }} />;
};

/** Brand mark as a mask — pass fill as a colour or gradient. */
export const Logo: React.FC<{ size: number; fill?: string; style?: React.CSSProperties }> = ({ size, fill, style }) =>
	fill ? (
		<div style={{ width: size, height: size * ICON_ASPECT, background: fill, WebkitMaskImage: `url(${ICON})`, maskImage: `url(${ICON})`, WebkitMaskSize: "contain", maskSize: "contain", WebkitMaskRepeat: "no-repeat", maskRepeat: "no-repeat", ...style }} />
	) : (
		<Img src={ICON} style={{ width: size, height: size * ICON_ASPECT, display: "block", ...style }} />
	);

export const Wordmark: React.FC<{ size: number; color?: string; gap?: number }> = ({ size, color = T.ink, gap }) => (
	<div style={{ display: "flex", alignItems: "center", gap: gap ?? size * 0.22 }}>
		<Logo size={size} />
		<span style={{ fontFamily: FONT, fontWeight: 600, fontSize: size * 0.9, letterSpacing: "0.02em", color, lineHeight: 1 }}>{BRAND_NAME}</span>
	</div>
);

/**
 * Per-word/char reveal. at = local frame the first unit starts; step = frames between units; dur = frames per unit.
 * mode "char" | "word". Each unit fades from 0, rises `rise` px and unblurs `blur` px.
 */
export const Reveal: React.FC<{ text: string; lf: number; at: number; step?: number; dur?: number; mode?: "char" | "word"; rise?: number; blur?: number; style?: React.CSSProperties; unitStyle?: (i: number) => React.CSSProperties | undefined }> = ({ text, lf, at, step = 2, dur = 14, mode = "word", rise = 16, blur = 6, style, unitStyle }) => {
	const units = mode === "char" ? [...text] : text.split(/(\s+)/);
	let k = 0;
	return (
		<span style={{ whiteSpace: "pre", ...style }}>
			{units.map((u, i) => {
				if (/^\s+$/.test(u)) return <span key={i}>{u}</span>;
				const t = E.out(clamp01((lf - at - k * step) / dur));
				k++;
				return <span key={i} style={{ display: "inline-block", opacity: t, transform: `translateY(${(1 - t) * rise}px)`, filter: t < 1 && blur ? `blur(${(1 - t) * blur}px)` : undefined, ...unitStyle?.(i) }}>{u}</span>;
			})}
		</span>
	);
};

const AV_COLORS = ["#F4D6C8", "#D6E4F4", "#E1D8F5", "#D5F0E1", "#F6E6C4", "#F5D5DF", "#D2EEF2", "#E6E6E6"];
const AV_INK = ["#9A4F2E", "#2E5A9A", "#5B3FA0", "#2E7A50", "#8A6412", "#9A2E55", "#1E7482", "#555"];
const INITIALS = ["JM", "AR", "SK", "LT", "DP", "NB", "EC", "RV", "OW", "MF", "HG", "TY", "KL", "BS", "CN", "ZA"];
/** Avatar: an AI-generated portrait (people who do not exist) from public/remake/faces/f00.jpg … f<NN>.jpg, deterministic per seed.
 *  No portraits ship with this template: add your own (generated or licensed for commercial use), then set FACES.
 *  With FACES = 0, or `initials`, it draws an initials disc. */
export const FACES = 0;
/** Face index → gender, for picking a portrait that fits a name: m = man, w = woman (one letter per face). */
export const FACE_GENDER = "";
export const face = (seed: number, idx?: number) => staticFile(`remake/faces/f${String(idx ?? Math.floor(hash(seed) * FACES)).padStart(2, "0")}.jpg`);
export const Avatar: React.FC<{ seed: number; size: number; style?: React.CSSProperties; initials?: boolean; faceIdx?: number }> = ({ seed, size, style, initials, faceIdx }) => {
	if (!initials && FACES > 0)
		return <Img src={face(seed, faceIdx)} style={{ width: size, height: size, borderRadius: "50%", objectFit: "cover", flexShrink: 0, display: "block", ...style }} />;
	const i = Math.floor(hash(seed) * AV_COLORS.length), j = Math.floor(hash(seed + 7) * INITIALS.length);
	return <div style={{ width: size, height: size, borderRadius: "50%", background: AV_COLORS[i], color: AV_INK[i], fontFamily: FONT, fontWeight: 600, fontSize: size * 0.38, display: "flex", alignItems: "center", justifyContent: "center", flexShrink: 0, ...style }}>{INITIALS[j]}</div>;
};

/* ─── shot registry ─── */
export type Shot = { id: string; f0: number; f1: number; render: (lf: number, F: number) => React.ReactNode };
