# Pipeline: Multi-agent level generation

> **Work in progress.** Coordinates world-building, level design, TA, and perf
> without parallel-writer collisions.

## Participation map

| Wave | Agents |
|------|--------|
| W1 — Layout | `level-designer`, `world-builder` |
| W2 — Visual target | `art-director`, `technical-artist` |
| W3 — Implementation | `unreal-specialist` (or engine cluster) |
| W4 — Validation | `performance-analyst`, `qa-tester` |

## Skill sequence

| Order | Skill id | Notes |
|------:|----------|-------|
| 1 | `team-level` | Orchestrated handoff doc |
| 2 | `asset-spec` | Naming + LOD budgets |
| 3 | `dev-story` | Data-driven placement / streaming hooks |
| 4 | `perf-profile` | Streaming + overdraw |
| 5 | `smoke-check` | Load + traverse |

## MCP requirements

| MCP (optional) | Rule |
|----------------|------|
| Editor automation | **Serialized** graph edits |
| Asset indexer | Validate naming conventions |

## Success criteria

- Level loads within agreed memory/time budget.
- Ownership matrix: one writer per contested asset class at a time.

## Failure criteria

- Concurrent edits to same map data without lock.
- Perf regression without recorded baseline.

## Monitoring

- Heatmaps for actor counts; streaming hitches count.

## Rollback

- Revert map data; keep layout doc as source of truth.

## Evolution (Phase 4+)

- Procedural validation scripts for actor bounds.
- Nightly load test in CI.
