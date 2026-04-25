# STATUS — Cursor Game Studios

> **Work in progress.**

## Current status

**On track — Phase 3 delivered.** Phases 1–2 plus **production orchestration**:
`docs/advanced-orchestration.md`, nine `pipelines/` definitions, and automation
scripts (health check, pipeline runner, metrics, nightly audit).

## Key metrics

| Metric | Value |
|--------|------:|
| Agent definitions | 49 (each with Phase 2 deepening block) |
| Skills | 72 (each with Phase 2 deepening block) |
| Rules (`.mdc`) | 12 |
| Skill companion pages (`skills/`) | 72 + index |
| Pipeline definitions (`pipelines/`) | 9 + index |
| Automation scripts | 4 (`studio-health-check`, `pipeline-runner`, `studio-metrics`, `nightly-studio-audit`) |

## Recent updates

| Date | Note |
|------|------|
| 2026-04-14 | Phase 1 scaffold committed to workspace folder |
| 2026-04-14 | Phase 2 — agent/skill deepening + studio docs |
| 2026-04-14 | Phase 3 — pipelines + advanced orchestration + automation |

## Known issues

- Legacy bash hooks are **reference-only** under `legacy/upstream-claude-hooks/`.
- Regeneration expects `_upstream/` or `--upstream` path to Donchitos repo.
