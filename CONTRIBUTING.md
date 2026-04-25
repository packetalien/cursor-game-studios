# Contributing

> **Work in progress.**

## Principles

- Preserve **upstream attribution** for
  [Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios)
  (MIT, Donchitos).
- Keep this repository a **clean structural port**—avoid importing unrelated
  product codenames, tabletop mechanics, or meme filenames into the core kit.

## Workflow

1. Clone upstream to `_upstream/` (or pass `--upstream`).
2. Run `python scripts/generate-cursor-game-studios.py`.
3. Run `python scripts/phase2-deepen.py` to (re)apply Phase 2 appendices idempotently
   and refresh the `skills/` companion tree.
4. Run `pytest`.
5. Append `CHANGES.md` under `[Unreleased]`.

## Rules style

- Prefer concise `.mdc` rules with explicit `globs`.
- Use `alwaysApply: true` sparingly (integrity rule + true global invariants only).
