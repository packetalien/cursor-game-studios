#!/usr/bin/env python3
"""
Nightly (or ad-hoc) studio audit: health check + metrics + contamination scan.

Exit code follows studio-health-check (1 if health fails). Contamination
violations print to stderr but do not change exit code unless --strict.

Usage:
  python scripts/nightly-studio-audit.py
  python scripts/nightly-studio-audit.py --strict
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Patterns built without embedding banned literals in this source file.
_T_TABLETOP = "".join(map(chr, (71, 85, 82, 80, 83)))
_T_ALT_STUDIO = "Osi" + "ris" + "Forge"
_T_CITY_ANCHOR = "Alex" + "andria"
_T_MEME_FILE = "quant" + "um" + "_" + "pl" + "aid"

FORBIDDEN = [
    re.compile(rf"\b{re.escape(_T_TABLETOP)}\b", re.I),
    re.compile(re.escape(_T_ALT_STUDIO), re.I),
    re.compile(re.escape(_T_CITY_ANCHOR), re.I),
    re.compile(re.escape(_T_MEME_FILE), re.I),
]
SKIP = {"_upstream", ".git", "__pycache__", ".pytest_cache", "node_modules", "tests"}
TEXT_EXT = {".md", ".mdc", ".yaml", ".yml", ".json", ".py", ".txt", ".sh"}


def _scan_text_files() -> list[Path]:
    out: list[Path] = []
    for p in ROOT.rglob("*"):
        if not p.is_file():
            continue
        if any(x in p.parts for x in SKIP):
            continue
        if p.suffix.lower() in TEXT_EXT:
            out.append(p)
    return out


def contamination(strict: bool) -> int:
    hits = 0
    for p in _scan_text_files():
        try:
            t = p.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for pat in FORBIDDEN:
            if pat.search(t):
                print(f"CONTAMINATION pattern in {p.relative_to(ROOT)}", file=sys.stderr)
                hits += 1
    if hits and strict:
        return 1
    if hits:
        print(f"audit: contamination hits={hits} (non-strict)", file=sys.stderr)
    else:
        print("audit: contamination scan clean")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--strict",
        action="store_true",
        help="Fail if contamination patterns found",
    )
    args = ap.parse_args()

    r = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "studio-health-check.py"), "--require-phase2-mark"],
        cwd=str(ROOT),
    )
    if r.returncode != 0:
        return r.returncode

    subprocess.run([sys.executable, str(ROOT / "scripts" / "studio-metrics.py")], cwd=str(ROOT))

    c = contamination(args.strict)
    if c != 0:
        return c
    print("nightly-studio-audit: complete")
    return 0


if __name__ == "__main__":
    sys.exit(main())
