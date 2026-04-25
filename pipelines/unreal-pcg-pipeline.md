# Pipeline: Unreal PCG (procedural content graphs)

> **Work in progress.** PCG graphs, deterministic seeds, validation, and perf.

## Participation map

| Role | Agent |
|------|-------|
| PCG owner | `unreal-specialist` |
| World | `world-builder` |
| Perf | `performance-analyst` |
| QA | `qa-tester` |

## Skill sequence

| Order | Skill id | Gate |
|------:|----------|------|
| 1 | `create-architecture` | PCG ownership + data interfaces |
| 2 | `dev-story` | Graph + supporting native/BP glue |
| 3 | `perf-profile` | Regeneration cost |
| 4 | `smoke-check` | Determinism spot-check |

## MCP requirements

| MCP (optional) | Rule |
|----------------|------|
| Editor | Serialize graph compiles; no parallel cooks on same graph |

## Success criteria

- Regeneration stable across seeds documented in ADR.
- Cook warnings under agreed threshold.

## Failure criteria

- Nondeterministic output without documented entropy source.
- PCG edits during active multiplayer test (race).

## Monitoring

- Cook time; regeneration frame spikes.

## Rollback

- Disable PCG layer; revert to baked static fallback.

## Evolution (Phase 4+)

- Golden-seed snapshot tests in CI harness.
