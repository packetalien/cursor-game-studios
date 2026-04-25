#!/usr/bin/env python3
"""
Regenerate Cursor Game Studios assets from a Claude-Code-Game-Studios checkout.

Upstream: https://github.com/Donchitos/Claude-Code-Game-Studios

Usage:
  python scripts/generate-cursor-game-studios.py [--upstream PATH]

Default upstream: <repo_root>/_upstream
"""
from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DIRECTORS = frozenset({"creative-director", "technical-director", "producer"})
LEADS = frozenset(
    {
        "game-designer",
        "lead-programmer",
        "art-director",
        "audio-director",
        "narrative-director",
        "qa-lead",
        "release-manager",
        "localization-lead",
    }
)


def tier_folder(stem: str) -> str:
    if stem in DIRECTORS:
        return "directors"
    if stem in LEADS:
        return "leads"
    return "specialists"


def rewrite_paths(text: str) -> str:
    return text.replace(".claude/", ".cursor/")


def port_agents(upstream: Path, out_root: Path) -> int:
    src = upstream / ".claude" / "agents"
    n = 0
    for f in sorted(src.glob("*.md")):
        body = rewrite_paths(f.read_text(encoding="utf-8"))
        dest_dir = out_root / ".cursor" / "agents" / tier_folder(f.stem)
        dest_dir.mkdir(parents=True, exist_ok=True)
        (dest_dir / f.name).write_text(body, encoding="utf-8")
        n += 1
    return n


def port_skills(upstream: Path, out_root: Path) -> int:
    src = upstream / ".claude" / "skills"
    n = 0
    for skill_md in sorted(src.glob("*/SKILL.md")):
        rel = skill_md.relative_to(src)
        dest = out_root / ".cursor" / "skills" / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(rewrite_paths(skill_md.read_text(encoding="utf-8")), encoding="utf-8")
        n += 1
    return n


def _parse_rule_paths(text: str) -> tuple[list[str], str]:
    m = re.match(r"^---\s*\npaths:\s*\n((?:  - .+\n)+)---\s*\n(.*)$", text, re.DOTALL)
    if not m:
        raise ValueError("Unexpected rule format (expected paths: block)")
    paths_block = m.group(1)
    body = m.group(2)
    paths = re.findall(r'^\s*-\s*"([^"]+)"', paths_block, re.MULTILINE)
    return paths, body


def port_rules(upstream: Path, out_root: Path) -> int:
    src = upstream / ".claude" / "rules"
    rules_dir = out_root / ".cursor" / "rules"
    rules_dir.mkdir(parents=True, exist_ok=True)
    n = 0
    for f in sorted(src.glob("*.md")):
        paths, body = _parse_rule_paths(f.read_text(encoding="utf-8"))
        globs = ",".join(paths) if len(paths) > 1 else paths[0]
        title = body.lstrip().split("\n", 1)[0].removeprefix("# ").strip()
        desc = f"Cursor Game Studios: {title}"
        header = (
            "---\n"
            f"description: {desc}\n"
            f"globs: {globs}\n"
            "alwaysApply: false\n"
            "---\n\n"
        )
        (rules_dir / (f.stem + ".mdc")).write_text(header + rewrite_paths(body), encoding="utf-8")
        n += 1
    return n


def write_port_integrity_rule(out_root: Path) -> None:
    path = out_root / ".cursor" / "rules" / "cursor-game-studios-integrity.mdc"
    path.write_text(
        "---\n"
        "description: Cursor Game Studios — port boundaries and attribution\n"
        "alwaysApply: true\n"
        "---\n\n"
        "# Cursor Game Studios — integrity\n\n"
        "- This repository is **Cursor Game Studios**: a **Cursor-native structural port** of "
        "[Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) "
        "(MIT, Donchitos). Preserve upstream attribution when sharing or modifying prompts.\n"
        "- Keep the tree focused on **game development workflows** in Cursor; do not merge "
        "unrelated product codenames, tabletop rule systems, or stray meme filenames into "
        "the core kit.\n"
        "- Prefer **Unreal Engine 5.5+** when the user targets UE (C++ core, Blueprints where "
        "appropriate); use the Godot or Unity specialist set when those engines are in scope.\n"
        "- Subagents: `.cursor/agents/{directors,leads,specialists}/`.\n"
        "- Skills: `.cursor/skills/<skill-id>/SKILL.md`.\n",
        encoding="utf-8",
    )


def port_docs_tree(upstream: Path, out_root: Path) -> int:
    src = upstream / ".claude" / "docs"
    if not src.is_dir():
        return 0
    dest = out_root / ".cursor" / "docs"
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(src, dest)
    n = 0
    for p in dest.rglob("*"):
        if p.is_file() and p.suffix in {".md", ".yaml", ".yml", ".txt"}:
            t = p.read_text(encoding="utf-8")
            p.write_text(rewrite_paths(t), encoding="utf-8")
            n += 1
    return n


def port_statusline(upstream: Path, out_root: Path) -> None:
    src = upstream / ".claude" / "statusline.sh"
    if not src.is_file():
        return
    dest = out_root / ".cursor" / "statusline.sh"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(rewrite_paths(src.read_text(encoding="utf-8")), encoding="utf-8")


def port_hooks_reference(upstream: Path, out_root: Path) -> None:
    src = upstream / ".claude" / "hooks"
    if not src.is_dir():
        return
    dest = out_root / "legacy" / "upstream-claude-hooks"
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(src, dest)
    (dest / "NOTICE.txt").write_text(
        "Legacy upstream hooks (reference only)\n\n"
        "Copied from Claude-Code-Game-Studios .claude/hooks/ for audit visibility. "
        "Cursor Game Studios is Cursor-native: prefer CI, pre-commit, and "
        ".cursor/rules/*.mdc over bash hook parity.\n",
        encoding="utf-8",
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--upstream",
        type=Path,
        default=ROOT / "_upstream",
        help="Path to Donchitos/Claude-Code-Game-Studios checkout",
    )
    args = ap.parse_args()
    upstream = args.upstream.resolve()
    if not (upstream / ".claude").is_dir():
        raise SystemExit(
            f"Missing .claude in upstream: {upstream}\n"
            "git clone --depth 1 "
            "https://github.com/Donchitos/Claude-Code-Game-Studios.git _upstream"
        )

    out_root = ROOT
    a = port_agents(upstream, out_root)
    s = port_skills(upstream, out_root)
    r = port_rules(upstream, out_root)
    write_port_integrity_rule(out_root)
    d = port_docs_tree(upstream, out_root)
    port_statusline(upstream, out_root)
    port_hooks_reference(upstream, out_root)
    print(f"agents={a} skills={s} rules_legacy={r} integrity_rule=1 cursor_internal_docs~={d}")


if __name__ == "__main__":
    main()
