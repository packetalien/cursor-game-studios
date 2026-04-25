# TASKLIST — Cursor Game Studios

> **Work in progress.**

## Phase 1 (foundation) — complete

- [x] Generator + `.cursor/` tree + docs + tests + GitHub push

## Phase 2 (agent and skill deepening) — complete

- [x] `phase2-deepen.py` + `skills/` tree + doctrine + affinity matrix + chapter `02`

## Phase 3 (orchestration + pipelines + automation) — complete

- [x] `03-phase-03-advanced-orchestration-production-pipelines.md`
- [x] `docs/advanced-orchestration.md`
- [x] `pipelines/` — nine baseline pipeline definitions + `pipelines/index.md`
- [x] `scripts/studio-health-check.py`
- [x] `scripts/pipeline-runner.py`
- [x] `scripts/studio-metrics.py`
- [x] `scripts/nightly-studio-audit.py`
- [x] `tests/test_phase3_pipelines.py`
- [x] Metadata + `docs/index.md` + `README.md` links

## Phase 4 (Unreal 5.5+ native + procedural mastery) — complete

- [x] `04-phase-04-unreal-native-integration-procedural-mastery.md`
- [x] `unreal/` documentation tree (MCP, agents, Live Link, PCG, WP, rendering)
- [x] Five new Unreal-focused pipelines + `pipelines/index.md` refresh
- [x] Three PCG skills under `.cursor/skills/pcg/`
- [x] `scripts/unreal-mcp-health.py` + health check / nightly audit wiring
- [x] `studio-metrics.py` includes `unreal/` byte estimate
- [x] Tests + metadata (`MANIFEST`, `CHANGES`, `ROADMAP`, `STATUS`, `README`, `docs/index.md`, `CONTRIBUTING`)

## Phase 5+ (next)

- [ ] Typed MCP tool schemas + timeouts for your game repo
- [ ] Emit `Saved/StudioUnrealMetrics.json` from editor hooks (optional)
- [ ] Wire `nightly-studio-audit.py` into CI schedule (optional)
