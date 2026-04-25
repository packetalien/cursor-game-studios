#!/usr/bin/env python3
"""
Studio structure health check: agent/skill/rule counts + pipeline presence.

Exit 0 if healthy, 1 otherwise.

Usage:
  python scripts/studio-health-check.py [--require-phase2-mark]
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_PIPELINES = [
    "concept-to-gdd-pipeline.md",
    "vertical-slice-pipeline.md",
    "multi-agent-level-pipeline.md",
    "ci-agent-review-pipeline.md",
    "asset-pipeline.md",
    "unreal-pcg-pipeline.md",
    "world-partition-pipeline.md",
    "build-deployment-pipeline.md",
    "automated-testing-pipeline.md",
]
MARKER = "<!-- PHASE2_DEEPENING_BEGIN -->"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--require-phase2-mark",
        action="store_true",
        help="Require PHASE2 deepening marker in every agent and skill file",
    )
    args = ap.parse_args()
    errs: list[str] = []

    agents = list((ROOT / ".cursor" / "agents").rglob("*.md"))
    skills = list((ROOT / ".cursor" / "skills").rglob("SKILL.md"))
    rules = list((ROOT / ".cursor" / "rules").glob("*.mdc"))
    if len(agents) != 49:
        errs.append(f"agents: expected 49, got {len(agents)}")
    if len(skills) != 72:
        errs.append(f"skills: expected 72, got {len(skills)}")
    if len(rules) != 12:
        errs.append(f"rules: expected 12, got {len(rules)}")

    pdir = ROOT / "pipelines"
    for name in EXPECTED_PIPELINES:
        p = pdir / name
        if not p.is_file():
            errs.append(f"missing pipeline: pipelines/{name}")

    if args.require_phase2_mark:
        for f in agents + skills:
            t = f.read_text(encoding="utf-8")
            if MARKER not in t:
                errs.append(f"missing Phase2 marker: {f.relative_to(ROOT)}")

    if errs:
        print("studio-health-check FAILED:")
        for e in errs:
            print(" -", e)
        return 1
    print(
        "studio-health-check OK:",
        f"agents={len(agents)} skills={len(skills)} rules={len(rules)}",
        f"pipelines={len(EXPECTED_PIPELINES)}",
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
