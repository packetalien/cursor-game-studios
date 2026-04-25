# Pipeline: Chaos destruction

> **Work in progress.** Physics events are **network handshakes** wearing rubble.

## Participation map

| Role | Agent |
|------|-------|
| Simulation | `gameplay-programmer` |
| Networking | `network-programmer`, `ue-replication-specialist` |
| Safety | `performance-analyst` |
| Feel | `technical-artist` |

## Skill sequence

| Order | Skill id | Gate |
|------:|----------|------|
| 1 | `create-architecture` | Authority + debris budgets |
| 2 | `dev-story` | GC-safe spawn paths |
| 3 | `perf-profile` | Wake/sleep + replication cost |
| 4 | `soak-test` | Long-run stability evidence |

## MCP requirements

| MCP (optional) | Rule |
|----------------|------|
| Editor | Serialize destructible edits; no parallel field rewrites |

## Success criteria

- Bounded debris; deterministic enough for QA repro.
- Crash-free soak threshold met.

## Failure criteria

- “Infinite shards” as a **personality**.

## Monitoring

Chaos tick time; net bandwidth spikes.

## Rollback

Disable layer; swap to canned VFX fallback.

## Evolution (Phase 5+)

Record deterministic seeds for CI replay slices.
