"""Phase 3 — pipelines and automation scripts exist."""
from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = [
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


class TestPhase3Pipelines(unittest.TestCase):
    def test_pipeline_files_present(self) -> None:
        pdir = ROOT / "pipelines"
        for name in EXPECTED:
            self.assertTrue((pdir / name).is_file(), f"missing {name}")
        self.assertTrue((pdir / "index.md").is_file())

    def test_phase3_chapter_and_advanced_orchestration(self) -> None:
        self.assertTrue((ROOT / "03-phase-03-advanced-orchestration-production-pipelines.md").is_file())
        self.assertTrue((ROOT / "docs" / "advanced-orchestration.md").is_file())

    def test_phase4_unreal_chapter_and_tree(self) -> None:
        self.assertTrue((ROOT / "04-phase-04-unreal-native-integration-procedural-mastery.md").is_file())
        self.assertTrue((ROOT / "unreal" / "index.md").is_file())

    def test_automation_scripts_exist(self) -> None:
        for name in (
            "studio-health-check.py",
            "pipeline-runner.py",
            "studio-metrics.py",
            "nightly-studio-audit.py",
            "unreal-mcp-health.py",
            "run-unittest.py",
        ):
            self.assertTrue((ROOT / "scripts" / name).is_file(), f"missing scripts/{name}")

    def test_studio_health_check_exits_zero(self) -> None:
        r = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "studio-health-check.py"), "--require-phase2-mark"],
            cwd=str(ROOT),
            capture_output=True,
            text=True,
        )
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
