#!/usr/bin/env python3
"""
Optional Unreal project health probe for automation.

Without CURSOR_UNREAL_UPROJECT set, exits 0 and prints a skip notice (CI-safe).

With CURSOR_UNREAL_UPROJECT=/abs/path/Game.uproject, verifies the file exists.
Optional JSON metrics may be supplied by your game repo at:
  <project>/Saved/StudioUnrealMetrics.json

Usage:
  python scripts/unreal-mcp-health.py
  python scripts/unreal-mcp-health.py --strict
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--strict",
        action="store_true",
        help="Fail if CURSOR_UNREAL_UPROJECT set but file missing or metrics invalid",
    )
    args = ap.parse_args()

    raw = os.environ.get("CURSOR_UNREAL_UPROJECT", "").strip()
    if not raw:
        print("unreal-mcp-health: skip (CURSOR_UNREAL_UPROJECT unset)")
        return 0

    uproj = Path(raw).expanduser()
    if not uproj.is_file():
        msg = f"unreal-mcp-health: uproject not found: {uproj}"
        print(msg, file=sys.stderr)
        return 1

    metrics_path = uproj.parent / "Saved" / "StudioUnrealMetrics.json"
    if metrics_path.is_file():
        try:
            data = json.loads(metrics_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            print(f"unreal-mcp-health: invalid JSON {metrics_path}: {e}", file=sys.stderr)
            return 1 if args.strict else 0
        keys = (
            "nanite_triangles_sample",
            "world_partition_cells_loaded",
            "lumen_probe_sample",
            "chaos_bodies_awake",
        )
        snapshot = {k: data.get(k) for k in keys if isinstance(data, dict)}
        print("unreal-mcp-health: metrics snapshot", json.dumps(snapshot, sort_keys=True))
    else:
        print(
            "unreal-mcp-health: uproject OK; no Saved/StudioUnrealMetrics.json (optional)",
        )

    print("unreal-mcp-health: OK", uproj.name)
    return 0


if __name__ == "__main__":
    sys.exit(main())
