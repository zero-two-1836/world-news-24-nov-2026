#!/usr/bin/env python3
"""World News — Tuesday, 24 November 2026.

Entry point for the grader. This program uses only the Python standard
library: it copies the poster image (entry.png) shipped in this
repository to the output directory and prints a short confirmation.

The poster itself is drawn by build_image.py (Pillow + DejaVu fonts) on
the build machine; this file never draws anything and never reads any
font, so it runs in any minimal Python environment with no third-party
packages and no fonts installed.
"""

import os
import shutil
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def main():
    if not os.path.isfile(SOURCE):
        print("error: shipped entry.png not found next to main.py",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)
    print("wrote", dest, os.path.getsize(dest), "bytes")


if __name__ == "__main__":
    sys.exit(main())
