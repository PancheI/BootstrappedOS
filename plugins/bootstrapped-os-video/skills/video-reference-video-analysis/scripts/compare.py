"""compare.py OUTDIR f f f ... → OUTDIR/compare.jpg: per row REF | OURS | |diff|, labelled with frame and mean-abs-diff.
Also OUTDIR/compare_<F>.jpg full-res REF|OURS pairs for close inspection."""
import sys, os
import numpy as np
from PIL import Image, ImageDraw
# project root = PROJECT_ROOT or the current directory (run from your Remotion project root)
root = os.environ.get("PROJECT_ROOT", os.getcwd())
# multi-reference: REF=A → remake/ref/A/ (default remake/ref/); REF_DIR overrides the whole path
REFDIR = os.environ.get("REF_DIR") or (os.path.join(root, "remake", "ref", os.environ["REF"]) if os.environ.get("REF") else os.path.join(root, "remake", "ref"))
out = sys.argv[1]; frames = [int(x) for x in sys.argv[2:]]
rows = []; W, Hh = 640, 360
for F in frames:
    ref = Image.open(f"{REFDIR}/full/f{F:04d}.jpg").convert("RGB")
    ours = Image.open(f"{out}/o{F}.jpg").convert("RGB").resize(ref.size)
    a, b = np.asarray(ref).astype(np.int16), np.asarray(ours).astype(np.int16)
    d = np.abs(a - b).mean()
    pair = Image.new("RGB", (ref.width * 2, ref.height)); pair.paste(ref, (0, 0)); pair.paste(ours, (ref.width, 0)); pair.save(f"{out}/compare_{F}.jpg", quality=88)
    dif = Image.fromarray(np.clip(np.abs(a - b).mean(2) * 3, 0, 255).astype(np.uint8)).convert("RGB")
    row = Image.new("RGB", (W * 3, Hh + 22), "white"); dr = ImageDraw.Draw(row)
    for i, im in enumerate((ref, ours, dif)): row.paste(im.resize((W, Hh)), (i * W, 22))
    dr.text((6, 5), f"F{F}  t={F/60:.2f}s  REF | OURS | diff   mean-abs-diff={d:.1f}", fill="black")
    rows.append(row); print(f"F{F} diff {d:.1f}")
sheet = Image.new("RGB", (W * 3, sum(r.height for r in rows)), "white"); y = 0
for r in rows: sheet.paste(r, (0, y)); y += r.height
sheet.save(f"{out}/compare.jpg", quality=85); print("→", f"{out}/compare.jpg")
