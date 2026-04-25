# Changelog

> **Work in progress.** Entries describe the Cursor-native port; upstream remains
> the conceptual source of truth for counts and roles.

All notable changes to **Cursor Game Studios** are documented here.

## [Unreleased]

### Fixed

- **Unittest discovery on Python 3.11+ / Windows:** add `tests/__init__.py` and
  refactor tests as `unittest.TestCase` subclasses so discovery matches pytest.
  Document **`-s tests -t tests`** (not `-t .` with `-s tests`, which triggers
  CPython’s “Start directory is not importable” check when `__init__.py` is
  missing). Add `scripts/run-unittest.py` with absolute paths for Dropbox / any cwd.

### Added

- **Phase 4 — Unreal Engine 5.5+ native integration & procedural mastery:**
  chapter `04-phase-04-unreal-native-integration-procedural-mastery.md`; `unreal/`
  documentation tree (MCP, agent capabilities, Live Link, PCG mastery, World
  Partition, rendering tech); five new pipelines (`nanite-optimization`,
  `lumen-lighting`, `chaos-destruction`, `pcg-asset-generation`,
  `world-partition-streaming`); three PCG specialist skills under
  `.cursor/skills/pcg/`; `scripts/unreal-mcp-health.py`; health check extensions
  for Unreal docs + skill/pipeline counts; `studio-metrics.py` includes `unreal/`
  in byte estimate; `nightly-studio-audit.py` invokes Unreal health probe;
  `tests/test_phase3_pipelines.py` extended for Phase 4 paths.
- **Phase 1 — Foundation:** structural port of Donchitos/Claude-Code-Game-Studios
  (49 agents, 72 skills, 12 `.mdc` rules including integrity rule);
  `scripts/generate-cursor-game-studios.py`; `tests/test_port_integrity.py`;
  legal and governance files; `01-phase-01-cursor-native-studio-foundation.md`;
  public `docs/` mirror from upstream reference material.
- **Phase 2 — Agent and skill deepening:** idempotent append blocks for all 49
  agents and 72 skills (`<!-- PHASE2_DEEPENING_BEGIN -->`); `skills/` reference
  tree (category-indexed companions); `docs/studio-operating-doctrine.md`,
  `docs/orchestration-patterns.md`, `docs/agent-skill-affinity-matrix.md`;
  `02-phase-02-agent-skill-deepening.md`; `scripts/phase2-deepen.py`;
  `docs/index.md` links to Phase 2 docs and `skills/index.md`.
- **Phase 3 — Orchestration + pipelines + automation:** chapter
  `03-phase-03-advanced-orchestration-production-pipelines.md`;
  `docs/advanced-orchestration.md`; `pipelines/` (nine pipeline definitions +
  index); scripts `studio-health-check.py`, `pipeline-runner.py`,
  `studio-metrics.py`, `nightly-studio-audit.py`; `tests/test_phase3_pipelines.py`.

### Changed

- `ROADMAP.md` phase table realigned through Phase 4 completion and Phases 5–10 targets.
- `README.md`, `TASKLIST.md`, `STATUS.md`, `MANIFEST.md`, `docs/index.md`,
  `CONTRIBUTING.md`, `SECURITY.md` updated for Phase 3–4 navigation, Unreal lane
  links, and optional metrics hygiene notes.

## Attribution

Upstream: [Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) (MIT, Donchitos).
