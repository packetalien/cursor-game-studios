# Pipeline: World Partition & streaming

> **Work in progress.** Cells, data layers, HLOD, streaming sources, validation.

## Participation map

| Role | Agent |
|------|-------|
| World | `world-builder`, `level-designer` |
| Engine | `engine-programmer`, `unreal-specialist` |
| Perf | `performance-analyst` |

## Skill sequence

| Order | Skill id | Gate |
|------:|----------|------|
| 1 | `map-systems` | Streaming model chosen |
| 2 | `create-architecture` | Data layers + authority |
| 3 | `dev-story` | Implementation |
| 4 | `soak-test` | Long-run load |

## MCP requirements

| MCP (optional) | Use |
|----------------|-----|
| Editor | Measure streaming hitches; **single writer** |

## Success criteria

- No runaway streaming sources; bounds validated.
- Soak test report archived.

## Failure criteria

- Circular streaming dependencies.
- Unbounded actor spawn in streamed cells.

## Monitoring

- Hitch histogram; cell memory high-water marks.

## Rollback

- Toggle data layers off; revert to last stable partition layout.

## Evolution (Phase 4+)

- Automated hitch budget in nightly job.
