# Unreal agent capabilities matrix

> **Work in progress.** Maps **existing** studio agents to Unreal surfaces. This
> is a **capability charter**, not a promise that every MCP exists on your desk.

## Directors (tier 1)

| Agent | Unreal authority |
|-------|------------------|
| `technical-director` | Rendering architecture, networking model, engine risk |
| `creative-director` | Visual target, mood, player fantasy vs GPU budget |
| `producer` | Milestones, build cadence, trade-off arbitration |

## Leads (tier 2)

| Agent | Unreal authority |
|-------|------------------|
| `lead-programmer` | Module boundaries, build graph, code review gates |
| `art-director` | Material lookdev budgets, asset spec |
| `qa-lead` | Test harness in editor + CI, crash triage |
| `release-manager` | Packaging profiles, platforms |

## Unreal cluster (specialists)

| Agent | Primary Unreal surfaces |
|-------|-------------------------|
| `unreal-specialist` | Overall UE5.5+ patterns, subsystems |
| `ue-gas-specialist` | Gameplay Ability System |
| `ue-blueprint-specialist` | Blueprint graphs, replication in BP |
| `ue-replication-specialist` | Net ownership, RPC policy |
| `ue-umg-specialist` | UMG / Common UI |
| `technical-artist` | Shaders, PCG, Nanite/Lumen tuning |
| `performance-analyst` | `stat`, traces, load budgets |
| `level-designer` | World Partition, streaming volumes |

## PCG extension skills (Phase 4)

| Skill id | Role |
|----------|------|
| `pcg-biome-generator` | Ecosystem scatter, masks, sustainability |
| `pcg-dungeon-architect` | Modular grid, connectivity proofs |
| `pcg-city-builder` | Blockout facades, HLOD-aware instancing |

## Read-only vs mutate

| Mode | Agents |
|------|--------|
| Read-mostly | `qa-tester`, `writer` (lore), `analytics-engineer` |
| Mutate | `unreal-specialist`, UE subs, `tools-programmer` (with queue) |
