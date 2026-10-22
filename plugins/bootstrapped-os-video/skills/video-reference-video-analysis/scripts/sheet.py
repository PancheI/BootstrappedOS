"""sheet.py SEQDIR OUT.jpg [step] — 1-per-second (default step 60) REF|OURS contact sheet from a full-render seq dir."""
import sys, os, glob
from PIL import Image, ImageDraw
# project root = PROJECT_ROOT or the current directory (run from your Remotion project root)
root = os.environ.get("PROJECT_ROOT", os.getcwd())
# multi-reference: REF=A → remake/ref/A/ (default remake/ref/); REF_DIR overrides the whole path
REFDIR = os.environ.get("REF_DIR") or (os.path.join(root, "remake", "ref", os.environ["REF"]) if os.environ.get("REF") else os.path.join(root, "remake", "ref"))
seq, out = sys.argv[1], sys.argv[2]; step = int(sys.argv[3]) if len(sys.argv) > 3 else 60
files = {int(os.path.basename(p)[1:-4].lstrip("0") or 0): p for p in glob.glob(f"{seq}/*.jpg")}
fr = [F for F in sorted(files) if F % step == 0]
w, h = 480, 270; cols = 4
S = Image.new("RGB", (cols * w * 2, ((len(fr) + cols - 1) // cols) * (h + 18)), "white"); d = ImageDraw.Draw(S)
for i, F in enumerate(fr):
    x, y = (i % cols) * w * 2, (i // cols) * (h + 18)
    S.paste(Image.open(f"{REFDIR}/full/f{F:04d}.jpg").resize((w, h)), (x, y + 18)); S.paste(Image.open(files[F]).resize((w, h)), (x + w, y + 18))
    d.text((x + 4, y + 3), f"F{F} REF | OURS", fill="black")
S.save(out, quality=85); print("→", out)
