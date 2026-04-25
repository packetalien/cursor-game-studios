#!/usr/bin/env python3
"""
Run unittest discovery with flags that work on Python 3.11+ / Windows / Dropbox.

`unittest discover -s tests -t .` fails because start_dir != top_level_dir, so
CPython requires tests/__init__.py. Using the same directory for both -s and -t
avoids that check; this script passes absolute paths so cwd does not matter.

Usage (from anywhere):
  python scripts/run-unittest.py
  python scripts/run-unittest.py -q
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TESTS = ROOT / "tests"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("-q", "--quiet", action="store_true", help="Single-line summary (verbosity 1)")
    args = ap.parse_args()
    cmd = [
        sys.executable,
        "-m",
        "unittest",
        "discover",
        "-s",
        str(TESTS),
        "-t",
        str(TESTS),
        "-p",
        "test_*.py",
    ]
    if not args.quiet:
        cmd.append("-v")
    return subprocess.call(cmd, cwd=str(ROOT))


if __name__ == "__main__":
    sys.exit(main())
