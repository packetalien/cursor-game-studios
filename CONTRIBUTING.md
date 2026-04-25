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
3. Run `pytest`.
4. Append `CHANGES.md` under `[Unreleased]`.

## Rules style

- Prefer concise `.mdc` rules with explicit `globs`.
- Use `alwaysApply: true` sparingly (integrity rule + true global invariants only).
