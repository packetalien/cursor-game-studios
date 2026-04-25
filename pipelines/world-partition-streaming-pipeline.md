# Pipeline: World Partition streaming

> **Work in progress.** Streaming is **scheduling** with a landscape shader.

## Participation map

| Role | Agent |
|------|-------|
| World | `level-designer` |
| Performance | `performance-analyst` |
| Architecture | `technical-director` |
| Tools | `tools-programmer` |

## Skill sequence

| Order | Skill id | Gate |
|------:|----------|------|
| 1 | `create-architecture` | Cell tier policy + data layers |
| 2 | `map-systems` | Streaming sources + gameplay layers |
| 3 | `perf-profile` | Hitch map at boundaries |
| 4 | `soak-test` | Overnight traverse evidence |

## MCP requirements

| MCP (optional) | Rule |
|----------------|------|
| Editor | Read-mostly cell diagnostics; serialize layout mutations |

## Success criteria

- Documented cell tiers; load graphs within budget.
- Debug playbook in `unreal/world-partition/large-world-debugging.md` linked from ADR.

## Failure criteria

- Default-layer hoarding; mystery hitches “only on Tuesdays”.

## Monitoring

Streaming queue depth; memory high-water marks.

## Rollback

Reduce loaded radius; temporary HLOD aggression.

## Evolution (Phase 5+)

Heartbeat JSON from `unreal/live-link-patterns.md` in CI.
