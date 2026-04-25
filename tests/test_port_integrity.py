"""Structural checks and contamination bans for Cursor Game Studios."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {"_upstream", ".git", "__pycache__", ".pytest_cache", "node_modules", "tests"}
TEXT_SUFFIXES = {".md", ".mdc", ".yaml", ".yml", ".json", ".py", ".txt", ".sh"}

# Built without embedding banned substrings contiguously in this source file.
_T_ALT_STUDIO = "Osi" + "ris" + "Forge"
_T_TABLETOP = "".join(map(chr, (71, 85, 82, 80, 83)))
_T_CITY_ANCHOR = "Alex" + "andria"
_T_MEME_FILE = "quant" + "um" + "_" + "pl" + "aid"


def _iter_text_files() -> list[Path]:
    out: list[Path] = []
    for p in ROOT.rglob("*"):
        if not p.is_file():
            continue
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        if p.suffix.lower() in TEXT_SUFFIXES:
            out.append(p)
    return out


def test_no_alt_studio_codename():
    hits: list[str] = []
    needle = _T_ALT_STUDIO.lower()
    for p in _iter_text_files():
        rel = str(p.relative_to(ROOT)).replace("\\", "/")
        t = rel.lower()
        if needle in t:
            hits.append(rel)
            continue
        try:
            body = p.read_text(encoding="utf-8").lower()
        except OSError:
            continue
        if needle in body:
            hits.append(rel)
    assert not hits, "Forbidden alt-studio token in: " + ", ".join(hits)


def test_no_tabletop_engine_token():
    pat = re.compile(rf"\b{re.escape(_T_TABLETOP)}\b", re.IGNORECASE)
    hits: list[str] = []
    for p in _iter_text_files():
        try:
            t = p.read_text(encoding="utf-8")
        except OSError:
            continue
        if pat.search(t):
            hits.append(str(p.relative_to(ROOT)))
    assert not hits, "Forbidden tabletop token in: " + ", ".join(hits)


def test_no_city_anchor_substring():
    """Ban a common unrelated lore-engine city anchor substring company-wide."""
    hits: list[str] = []
    needle = _T_CITY_ANCHOR.lower()
    for p in _iter_text_files():
        rel = str(p.relative_to(ROOT)).replace("\\", "/")
        if needle in rel.lower():
            hits.append(rel)
            continue
        try:
            t = p.read_text(encoding="utf-8")
        except OSError:
            continue
        if needle in t.lower():
            hits.append(rel)
    assert not hits, "Forbidden city-anchor substring in: " + ", ".join(hits)


def test_no_meme_filename_token():
    hits: list[str] = []
    needle = _T_MEME_FILE.lower()
    for p in _iter_text_files():
        rel = str(p.relative_to(ROOT)).replace("\\", "/")
        if needle in rel.lower():
            hits.append(rel)
            continue
        try:
            t = p.read_text(encoding="utf-8")
        except OSError:
            continue
        if needle in t.lower():
            hits.append(rel)
    assert not hits, "Forbidden meme filename token in: " + ", ".join(hits)


def test_agent_skill_rule_counts():
    agents = list((ROOT / ".cursor" / "agents").rglob("*.md"))
    skills = list((ROOT / ".cursor" / "skills").rglob("SKILL.md"))
    rules = list((ROOT / ".cursor" / "rules").glob("*.mdc"))
    assert len(agents) == 49
    assert len(skills) == 72
    assert len(rules) == 12
