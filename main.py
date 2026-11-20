#!/usr/bin/env python3
"""Entry for make.fun news-image-20261120: sum up 20 November 2026 world
news in one image.

The poster (entry.png, 1024x1024, drawn with PIL from the day's wire
reports) sits beside this file. The program copies it byte-for-byte to
the output path: no network, no re-encoding, so two runs are identical.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import sys
from pathlib import Path


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        print(f"error: {source} not found", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(source, target)
    # Byte-for-byte copy: the output must be exactly the poster we ship.
    if target.stat().st_size != source.stat().st_size:
        print("error: copied file size differs from source", file=sys.stderr)
        return 1
    print(f"wrote {target} ({target.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
