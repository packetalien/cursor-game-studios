# Cursor Game Studios

> **Work in progress — use at your own risk.** This repository is a **high-fidelity,
> Cursor-native structural port** of
> [Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios)
> (MIT, **Donchitos**). It is not affiliated with unrelated engines, products, or
> codenames beyond what you explicitly add to your own game project.

**Cursor Game Studios** ships the same studio shape as upstream—**49** agent
definitions, **72** semantic skills, and **12** `.mdc` rules (eleven path-scoped
ports plus one integrity rule)—mapped to Cursor conventions (`.cursor/agents`,
`.cursor/skills`, `.cursor/rules`).

## Create the GitHub repository (you)

This folder is ready to push. On GitHub:

1. **New repository** → name: **`cursor-game-studios`** (public).
2. Do **not** add a README/license on GitHub (this tree already has them).
3. Locally:

```bash
cd cursor-game-studios
git init
git add .
git commit -m "feat: Phase 1 — Cursor-native studio foundation"
git branch -M main
git remote add origin https://github.com/<your-account>/cursor-game-studios.git
git push -u origin main
```

## Quick start

1. Open **`cursor-game-studios`** in **Cursor**.
2. Read **`AGENTS.md`** (work in progress; verify against your pipeline).
3. Start onboarding via **`.cursor/skills/start/SKILL.md`** (semantic equivalent
   of the original `/start` flow).

## Regenerate from upstream

```bash
git clone --depth 1 https://github.com/Donchitos/Claude-Code-Game-Studios.git _upstream
python scripts/generate-cursor-game-studios.py --upstream _upstream
pytest
```

If you refresh `docs/` from upstream, preserve **`docs/index.md`** (merge manually
if needed).

## Tests

```bash
pip install pytest
pytest
```

## License

See **`LICENSE`** (MIT with upstream attribution).

## Disclaimer

See **`DISCLAIMER.md`**.
