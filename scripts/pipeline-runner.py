#!/usr/bin/env python3
"""
Print a pipeline checklist from pipelines/*.md (section headers + tables).

Usage:
  python scripts/pipeline-runner.py concept-to-gdd
  python scripts/pipeline-runner.py --list
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ALIASES = {
    "concept-to-gdd": "concept-to-gdd-pipeline.md",
    "vertical-slice": "vertical-slice-pipeline.md",
    "multi-agent-level": "multi-agent-level-pipeline.md",
    "ci-agent-review": "ci-agent-review-pipeline.md",
    "asset": "asset-pipeline.md",
    "unreal-pcg": "unreal-pcg-pipeline.md",
    "world-partition": "world-partition-pipeline.md",
    "world-partition-streaming": "world-partition-streaming-pipeline.md",
    "build-deploy": "build-deployment-pipeline.md",
    "automated-testing": "automated-testing-pipeline.md",
    "nanite-optimization": "nanite-optimization-pipeline.md",
    "lumen-lighting": "lumen-lighting-pipeline.md",
    "chaos-destruction": "chaos-destruction-pipeline.md",
    "pcg-asset-generation": "pcg-asset-generation-pipeline.md",
}


def _resolve(name: str) -> Path | None:
    key = name.strip().lower().removesuffix(".md")
    fname = ALIASES.get(key)
    if not fname:
        fname = key if key.endswith(".md") else f"{key}-pipeline.md"
    p = ROOT / "pipelines" / fname
    return p if p.is_file() else None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("pipeline", nargs="?", help="Pipeline id or alias")
    ap.add_argument("--list", action="store_true", help="List known pipelines")
    args = ap.parse_args()

    if args.list:
        for k in sorted(ALIASES):
            print(k, "->", ALIASES[k])
        return 0
    if not args.pipeline:
        ap.print_help()
        return 2

    path = _resolve(args.pipeline)
    if not path:
        print("Unknown pipeline:", args.pipeline)
        print("Try: python scripts/pipeline-runner.py --list")
        return 1

    text = path.read_text(encoding="utf-8")
    print(f"# Pipeline runner: {path.relative_to(ROOT)}")
    print()
    for line in text.splitlines():
        if line.startswith("#") or line.startswith("|") or line.startswith("---"):
            print(line)
        elif line.startswith("## "):
            print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
