# Cursor Game Studios

> **Work in progress — use at your own risk.** This repository is a **high-fidelity,
> Cursor-native structural port** of
> [Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios)
> (MIT, **Donchitos**). It is not affiliated with unrelated engines, products, or
> codenames beyond what you explicitly add to your own game project.

**Cursor Game Studios** ships the same studio shape as upstream—**49** agent
definitions, **75** semantic skills, and **12** `.mdc` rules (eleven path-scoped
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
python scripts/phase2-deepen.py
pytest
```

If you refresh `docs/` from upstream, preserve **`docs/index.md`** (merge manually
if needed).

## Tests

From the **repository root** (the folder that contains `tests/`):

```bash
pip install pytest
python -m pytest -q
```

Stdlib **unittest** discovery (Python 3.11+ needs `-t .` so the `tests` package
is importable; `tests/__init__.py` is included for that):

```bash
python -m unittest discover -s tests -p "test_*.py" -v -t .
```

PowerShell (same intent):

```powershell
python -m unittest discover -s tests -p "test_*.py" -v -t .
```

## Phase 3 — Orchestration & pipelines

- **Charter:** `03-phase-03-advanced-orchestration-production-pipelines.md`
- **Advanced orchestration:** `docs/advanced-orchestration.md`
- **Pipelines:** `pipelines/index.md` (Phase 3 baseline + Phase 4 Unreal lanes)
- **Automation:**

```bash
python scripts/studio-health-check.py --require-phase2-mark
python scripts/pipeline-runner.py --list
python scripts/pipeline-runner.py vertical-slice
python scripts/studio-metrics.py
python scripts/nightly-studio-audit.py
python scripts/unreal-mcp-health.py
```

## Phase 4 — Unreal 5.5+ native integration

- **Charter:** `04-phase-04-unreal-native-integration-procedural-mastery.md`
- **Unreal lane:** `unreal/index.md` (MCP, Live Link, PCG, World Partition, rendering)
- **New pipelines:** Nanite, Lumen, Chaos, PCG asset generation, WP streaming (see `pipelines/index.md`)
- **PCG skills:** `.cursor/skills/pcg/pcg-*/SKILL.md`
- **Optional game metrics:** set `CURSOR_UNREAL_UPROJECT` to an absolute `.uproject` path;
  game repo may emit `Saved/StudioUnrealMetrics.json` for `unreal-mcp-health.py`

## License

See **`LICENSE`** (MIT with upstream attribution).

## Disclaimer

See **`DISCLAIMER.md`**.
