"""Phase 3 — pipelines and automation scripts exist."""
from __future__ import annotations

import subprocess
import sys
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
]


def test_pipeline_files_present():
    pdir = ROOT / "pipelines"
    for name in EXPECTED:
        assert (pdir / name).is_file(), f"missing {name}"
    assert (pdir / "index.md").is_file()


def test_phase3_chapter_and_advanced_orchestration():
    assert (ROOT / "03-phase-03-advanced-orchestration-production-pipelines.md").is_file()
    assert (ROOT / "docs" / "advanced-orchestration.md").is_file()


def test_automation_scripts_exist():
    for name in (
        "studio-health-check.py",
        "pipeline-runner.py",
        "studio-metrics.py",
        "nightly-studio-audit.py",
    ):
        assert (ROOT / "scripts" / name).is_file()


def test_studio_health_check_exits_zero():
    r = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "studio-health-check.py"), "--require-phase2-mark"],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
    )
    assert r.returncode == 0, r.stdout + r.stderr
