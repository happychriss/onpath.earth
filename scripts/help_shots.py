#!/usr/bin/env python3
"""Turn the app screenshots (PNG) into the help pages' pictures (assets/help/*.webp).

Usage: python3 scripts/help_shots.py <folder> [<folder> …]
Looks up every source file named in help_shots.IMAGES in the given folders (also in their subfolders; a later
folder wins when a name appears twice) and writes 540 × 1200 WebP files. Pictures whose PNG is not found are
reported and left as they are. Needs Pillow.
"""
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from help_shots import IMAGES, WIDTH, HEIGHT, files  # noqa: E402

if len(sys.argv) < 2:
    raise SystemExit(__doc__)
found = {}
for folder in sys.argv[1:]:
    for png in sorted(Path(folder).rglob('*.png')):
        found[png.name] = png
out = ROOT / 'assets' / 'help'
out.mkdir(parents=True, exist_ok=True)
missing = []
for name, (de_src, en_src, *_) in IMAGES.items():
    de_file, en_file = files(name)
    for src, dest in ((de_src, de_file), (en_src, en_file)):
        if not src:
            continue
        if src not in found:
            missing.append(src)
            continue
        im = Image.open(found[src]).convert('RGB').resize((WIDTH, HEIGHT), Image.LANCZOS)
        im.save(out / dest, 'WEBP', quality=78, method=6)
print(f'{len(list(out.glob("*.webp")))} pictures in assets/help/')
if missing:
    print('Not found (left as they are):', ', '.join(sorted(set(missing))))
