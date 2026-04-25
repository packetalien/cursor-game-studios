#!/usr/bin/env python3
"""
Emit lightweight JSON metrics about the studio repository shape.

Usage:
  python scripts/studio-metrics.py
  python scripts/studio-metrics.py --out metrics.json
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _count_bytes() -> int:
    total = 0
    roots = [ROOT / ".cursor", ROOT / "docs", ROOT / "pipelines", ROOT / "skills", ROOT / "scripts"]
    for base in roots:
        if not base.is_dir():
            continue
        for p in base.rglob("*"):
            if p.is_file():
                try:
                    total += p.stat().st_size
                except OSError:
                    pass
    return total


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, help="Write JSON to this path")
    args = ap.parse_args()

    agents = list((ROOT / ".cursor" / "agents").rglob("*.md"))
    skills = list((ROOT / ".cursor" / "skills").rglob("SKILL.md"))
    rules = list((ROOT / ".cursor" / "rules").glob("*.mdc"))
    pipelines = list((ROOT / "pipelines").glob("*.md"))
    pipelines = [p for p in pipelines if p.name != "index.md"]

    data = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "counts": {
            "agents": len(agents),
            "skills": len(skills),
            "rules": len(rules),
            "pipeline_definitions": len(pipelines),
        },
        "approx_total_bytes_excluding_git": _count_bytes(),
    }
    text = json.dumps(data, indent=2)
    if args.out:
        args.out.write_text(text, encoding="utf-8")
        print("wrote", args.out)
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
