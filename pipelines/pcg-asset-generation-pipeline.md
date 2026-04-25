# Pipeline: PCG asset generation

> **Work in progress.** Procedural output must be **inventory**, not weather.

## Participation map

| Role | Agent |
|------|-------|
| PCG | `unreal-specialist` |
| World | `level-designer`, `world-builder` |
| Rules | `technical-artist` |
| QA | `qa-tester` |

## Skill sequence

| Order | Skill id | Gate |
|------:|----------|------|
| 1 | `pcg-biome-generator` *or* `pcg-city-builder` *or* `pcg-dungeon-architect` | Domain pick |
| 2 | `dev-story` | Graph + export path |
| 3 | `perf-profile` | Regeneration frame budget |
| 4 | `regression-suite` | Golden seeds / samples |

## MCP requirements

| MCP (optional) | Rule |
|----------------|------|
| Editor | Single-writer per PCG graph compile |

## Success criteria

- Quality gates in `unreal/pcg-mastery/pcg-quality-gates.md` satisfied for sample set.

## Failure criteria

- Nondeterministic scatter without documented entropy.

## Monitoring

Cook warnings; instance counts per cell.

## Rollback

Disable PCG layer; static fallback mesh set.

## Evolution (Phase 5+)

CI cell sampler with JSON receipts.
