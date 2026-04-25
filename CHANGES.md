# Changelog

> **Work in progress.** Entries describe the Cursor-native port; upstream remains
> the conceptual source of truth for counts and roles.

All notable changes to **Cursor Game Studios** are documented here.

## [Unreleased]

### Added

- **Phase 1 — Foundation:** structural port of Donchitos/Claude-Code-Game-Studios
  (49 agents, 72 skills, 12 `.mdc` rules including integrity rule);
  `scripts/generate-cursor-game-studios.py`; `tests/test_port_integrity.py`;
  legal and governance files; `01-phase-01-cursor-native-studio-foundation.md`;
  public `docs/` mirror from upstream reference material.
- **Phase 2 — Agent and skill deepening:** idempotent append blocks for all 49
  agents and 72 skills (`<!-- PHASE2_DEEPENING_BEGIN -->`); `skills/` reference
  tree (nine categories); `docs/studio-operating-doctrine.md`,
  `docs/orchestration-patterns.md`, `docs/agent-skill-affinity-matrix.md`;
  `02-phase-02-agent-skill-deepening.md`; `scripts/phase2-deepen.py`;
  `docs/index.md` links to Phase 2 docs and `skills/index.md`.

### Changed

- `ROADMAP.md` phase table realigned to Phase 1–2 completion and future work.

## Attribution

Upstream: [Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) (MIT, Donchitos).
