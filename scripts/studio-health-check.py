#!/usr/bin/env python3
"""
Studio structure health check: agent/skill/rule counts, pipeline presence,
and Unreal doc tree (`unreal/`).

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
    "nanite-optimization-pipeline.md",
    "lumen-lighting-pipeline.md",
    "chaos-destruction-pipeline.md",
    "pcg-asset-generation-pipeline.md",
    "world-partition-streaming-pipeline.md",
]
EXPECTED_UNREAL_DOCS = [
    "unreal/index.md",
    "unreal/unreal-mcp-integration.md",
    "unreal/unreal-agent-capabilities.md",
    "unreal/live-link-patterns.md",
    "unreal/pcg-mastery/pcg-rule-systems.md",
    "unreal/pcg-mastery/pcg-quality-gates.md",
    "unreal/pcg-mastery/pcg-agent-specialists.md",
    "unreal/world-partition/world-partition-orchestration.md",
    "unreal/world-partition/streaming-optimization-patterns.md",
    "unreal/world-partition/large-world-debugging.md",
    "unreal/rendering-tech/nanite-optimization-workflows.md",
    "unreal/rendering-tech/lumen-gi-reflections.md",
    "unreal/rendering-tech/chaos-physics-destruction.md",
    "unreal/rendering-tech/virtual-shadow-maps.md",
    "unreal/rendering-tech/material-shader-automation.md",
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
    if len(skills) != 75:
        errs.append(f"skills: expected 75, got {len(skills)}")
    if len(rules) != 12:
        errs.append(f"rules: expected 12, got {len(rules)}")

    pdir = ROOT / "pipelines"
    for name in EXPECTED_PIPELINES:
        p = pdir / name
        if not p.is_file():
            errs.append(f"missing pipeline: pipelines/{name}")

    for rel in EXPECTED_UNREAL_DOCS:
        u = ROOT / rel
        if not u.is_file():
            errs.append(f"missing unreal doc: {rel}")

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
        f"unreal_docs={len(EXPECTED_UNREAL_DOCS)}",
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
