#!/usr/bin/env python3
"""Frame lamp photos to the GLOSTO AKIS photo standard.

Every product photo is a 1200x1600 (3:4) transparent PNG. The lamp is
centred, 80% of the frame tall, and stands on a floor line 10% up from
the bottom, so all lamps line up in the homepage grid.

Input photos must already be cut out (transparent background).

Usage:
    python3 tools/frame_photos.py ~/Desktop/lamp_04.png ~/Desktop/lamp_04_2.png
    python3 tools/frame_photos.py photo.png --out some/other/dir

Each output keeps the input's file name (as .png) and goes to img/product/
unless --out says otherwise. Name the files lamp_NN.png, lamp_NN_2.png, ...
before running.

Needs Pillow:  pip3 install pillow
"""
import argparse
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    sys.exit("Needs Pillow. Install it with:  pip3 install pillow")

WIDTH, HEIGHT = 1200, 1600
LAMP_HEIGHT = 0.80   # share of frame height the lamp fills
MAX_WIDTH = 0.90     # never let a wide lamp touch the sides
FLOOR = 0.10         # gap under the lamp, share of frame height
ALPHA_MIN = 20       # pixels more opaque than this count as lamp

DEFAULT_OUT = Path(__file__).resolve().parent.parent / "img" / "product"


def frame(src: Path) -> Image.Image:
    im = Image.open(src).convert("RGBA")
    alpha = im.getchannel("A")
    if alpha.getextrema()[0] == 255:
        raise ValueError("has no transparent background, cut the lamp out first")
    bbox = alpha.point(lambda v: 255 if v > ALPHA_MIN else 0).getbbox()
    if bbox is None:
        raise ValueError("is fully transparent")

    lamp = im.crop(bbox)
    scale = min(HEIGHT * LAMP_HEIGHT / lamp.height, WIDTH * MAX_WIDTH / lamp.width)
    w, h = round(lamp.width * scale), round(lamp.height * scale)
    lamp = lamp.resize((w, h), Image.LANCZOS)

    canvas = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    canvas.paste(lamp, ((WIDTH - w) // 2, HEIGHT - round(HEIGHT * FLOOR) - h))
    return canvas


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("photos", nargs="+", type=Path, help="cut-out lamp photos")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT, help="output folder (default: img/product)")
    args = parser.parse_args()

    args.out.mkdir(parents=True, exist_ok=True)
    failed = 0
    for src in args.photos:
        try:
            framed = frame(src)
        except (OSError, ValueError) as err:
            print(f"SKIP  {src}: {err}", file=sys.stderr)
            failed += 1
            continue
        dest = args.out / f"{src.stem}.png"
        framed.save(dest, optimize=True)
        print(f"OK    {src} -> {dest} ({dest.stat().st_size // 1024} KB)")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
