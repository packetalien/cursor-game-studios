# Phase 04 — Unreal Engine 5.5+ native integration & procedural mastery

> **Work in progress — use at your own risk.** Phase 4 is the studio’s **native
> engine covenant**: documentation, pipelines, and skills that assume Unreal
> 5.5+ workflows—**MCP as conductor**, not chaos gremlin.

**Version:** 0.4.0  
**Phase:** 4 — Unreal native + PCG + World Partition + advanced rendering

---

## Table of contents

1. [Executive summary](#executive-summary)
2. [What Phase 4 adds](#what-phase-4-adds)
3. [Twelve Unreal-native role profiles](#twelve-unreal-native-role-profiles)
4. [Unreal MCP complexity matrix](#unreal-mcp-complexity-matrix)
5. [PCG quality gates (charter)](#pcg-quality-gates-charter)
6. [World Partition performance tiers](#world-partition-performance-tiers)
7. [Rendering cost vs quality heuristics](#rendering-cost-vs-quality-heuristics)
8. [Nanite workflow spine](#nanite-workflow-spine)
9. [Lumen & reflections trade space](#lumen--reflections-trade-space)
10. [Chaos physics & replication discipline](#chaos-physics--replication-discipline)
11. [Virtual Shadow Maps policy grid](#virtual-shadow-maps-policy-grid)
12. [Material & shader automation ledger](#material--shader-automation-ledger)
13. [Live Link pattern matrix](#live-link-pattern-matrix)
14. [Automation ROI (Phase 4)](#automation-roi-phase-4)
15. [Sensory covenant — engine midnight](#sensory-covenant--engine-midnight)
16. [Graveyard quotes — engine programmer edition](#graveyard-quotes--engine-programmer-edition)
17. [Fifteen Unreal production workflow seeds](#fifteen-unreal-production-workflow-seeds)
18. [Evolution hooks (Phase 5+)](#evolution-hooks-phase-5)
19. [Index](#index)
20. [Glossary](#glossary)
21. [Index of tables](#index-of-tables)

---

## Executive summary

Phase 4 turns Cursor Game Studios into a **first-class Unreal lane**: `unreal/`
documentation for MCP, agents, Live Link, PCG, World Partition, and rendering
tech; **five** additional pipelines; **three** PCG specialist skills; optional
`StudioUnrealMetrics.json` probing via `scripts/unreal-mcp-health.py`; and
health checks that verify the Unreal doc tree exists. We are no longer *using*
Unreal as a guest OS—we are **negotiating with it as a roommate who pays rent in
triangles**.

---

## What Phase 4 adds

| Layer | Location | Purpose |
|-------|----------|---------|
| Unreal doctrine | `unreal/` + this chapter | MCP, agents, streaming, GI, PCG |
| PCG mastery | `unreal/pcg-mastery/` | Rules, gates, specialist roster |
| World Partition | `unreal/world-partition/` | Orchestration + streaming + debug |
| Rendering tech | `unreal/rendering-tech/` | Nanite, Lumen, Chaos, VSM, materials |
| Pipelines | `pipelines/*` (five new) | Executable contracts for engine lanes |
| Skills | `.cursor/skills/pcg/*` | Biome, dungeon, city PCG playbooks |
| Automation | `unreal-mcp-health.py`, health check extensions | Optional project metrics |

---

## Twelve Unreal-native role profiles

### R01 — Nanite Optimization Specialist

**Charter:** Convert heroic meshes into **streaming citizens** with material
discipline. Owns Nanite eligibility matrices and fallback LOD policy.  
**Mission:** keep triangle talk honest—**geometry is cheap until shading says otherwise**.  
**Primary tools:** `nanite-optimization-pipeline.md`, TA material audits, capture passes.  
**Success looks like:** documented per-class Nanite vs fallback with receipts.  
**Graveyard line:** “We optimized the mesh; the material laughed in GPU.”

### R02 — PCG Architect

**Charter:** Graph modularity, seed governance, and merge-safe subgraph
boundaries. Speaks fluent “**not one megagraph**.”  
**Mission:** make procedural graphs **reviewable** like code, not like weather.  
**Primary tools:** `pcg-asset-generation-pipeline.md`, `pcg-rule-systems.md`, exports folder policy.  
**Success looks like:** deterministic seeds, bisectable diffs, bounded regen cost.  
**Graveyard line:** “The graph is fine; the merge conflict is performing interpretive dance.”

### R03 — World Partition Engineer

**Charter:** Cell tiers, data layers, streaming sources, and **boundary hitch
autopsies**. Refuses Default-layer hoarding on principle.  
**Mission:** turn open worlds into **predictable load choreography**.  
**Primary tools:** `world-partition-streaming-pipeline.md`, streaming visualization, soak logs.  
**Success looks like:** named tiers, hitch maps with cell ids, rollback levers.  
**Graveyard line:** “It streams perfectly—except when players exist.”

### R04 — Lumen Lighting Director

**Charter:** Interior leak triage, reflection honesty, and exposure lock before
lookdev spirals into religious war.  
**Mission:** keep GI readable under motion and **emotionally stable** under iteration.  
**Primary tools:** `lumen-lighting-pipeline.md`, reference exposure locks, still captures.  
**Success looks like:** signed-off probe/reflection budgets per biome.  
**Graveyard line:** “The bounce light is not gaslighting you—the leak is.”

### R05 — Virtual Shadow Map Custodian

**Charter:** Cache policy per platform; argues with the sun until frame time
stops screaming.  
**Mission:** align shadow cost with **SKU reality**, not demo reel dreams.  
**Primary tools:** VSM policy grid, platform overrides, perf captures at noon and dusk.  
**Success looks like:** documented cache sizing + worst-case stills per SKU.  
**Graveyard line:** “Shadows remember. Especially the shortcuts.”

### R06 — Chaos Physics Tuner

**Charter:** Debris budgets, sleep policies, and **network authority** for
things that explode socially.  
**Mission:** make destruction **exciting in single-player and survivable online**.  
**Primary tools:** `chaos-destruction-pipeline.md`, replication traces, soak stability.  
**Success looks like:** bounded debris, deterministic repro slices, net-safe wakes.  
**Graveyard line:** “Physics sleeps—guilt does not.”

### R07 — Live Link Operator

**Charter:** Heartbeats, log tails, bounded JSON snapshots—**telemetry without
stalking**.  
**Mission:** give agents **truth from runtime** without drowning them in bytes.  
**Primary tools:** `live-link-patterns.md`, optional `StudioUnrealMetrics.json`, log tail L1.  
**Success looks like:** stable cadence, bounded payloads, human-readable summaries.  
**Graveyard line:** “If your heartbeat file is larger than the save game, you built telemetry wrong.”

### R08 — Material Graph Auditor

**Charter:** Master material strategy, permutation caps, and “**no snowflake
windows**” enforcement.  
**Mission:** stop shader permutations from becoming **a second repo**.  
**Primary tools:** master material families, lintable parameter naming, TA sign-off tables.  
**Success looks like:** permutation caps enforced in reviews, not in prayers.  
**Graveyard line:** “Every unique window is a tiny invoice to the GPU.”

### R09 — Blueprint Compile Firefighter

**Charter:** Serialization of compiles; breaks up parallel MCP mutations like a
bouncer at a compile club.  
**Mission:** keep editor automation from becoming **compile storm performance art**.  
**Primary tools:** single-writer queues, MCP mutation logs, staged applies.  
**Success looks like:** zero parallel writes on the same graph without a named mutex story.  
**Graveyard line:** “The Blueprint compiled once—then never stopped.”

### R10 — C++ Subsystems Wrangler

**Charter:** GameInstance / WorldSubsystem seams, deterministic init order, and
**no ctor drama** at 2am.  
**Mission:** keep native boundaries **boring**, because boring ships.  
**Primary tools:** subsystem maps, init order ADRs, narrow unit tests where feasible.  
**Success looks like:** documented ownership for cross-world services.  
**Graveyard line:** “If init order is folklore, your crash is mythology.”

### R11 — PCG QA Sampler

**Charter:** Stratified cell sampling, golden seeds, and proofs that **navmesh
is not optional folklore**.  
**Mission:** treat procedural output like **inventory**, not ambience.  
**Primary tools:** `pcg-quality-gates.md`, sampling scripts, golden-seed tables.  
**Success looks like:** failing builds when gates flap, not when vibes flap.  
**Graveyard line:** “PCG said it connected; navmesh filed for divorce.”

### R12 — Runtime Performance Coroner

**Charter:** `stat` rituals, hitch timelines, and postmortems that name the
**actual guilty cell**, not “the build machine hates us.”  
**Mission:** convert spikes into **named suspects** with evidence chains.  
**Primary tools:** perf captures, streaming overlays, correlation notes in `STATUS.md` or issues.  
**Success looks like:** postmortems that cite coordinates, not astrology.  
**Graveyard line:** “The hitch was at a boundary—shocking, like gravity.”

---

## Unreal MCP complexity matrix

| Surface | MCP value | Parallelism risk | Mitigation |
|---------|-----------|------------------|------------|
| Asset queries | High | Low | Read-only burst OK |
| Blueprint read | High | Low | Cache exports |
| Blueprint write | High | **Severe** | Single-writer queue |
| PCG graph write | High | **Severe** | Per-graph mutex |
| Console `stat` | Medium | Medium | Throttle frequency |
| Cook / package | High | Medium | CI isolation |

---

## PCG quality gates (charter)

| Gate id | Intent | Example signal |
|---------|--------|----------------|
| G-PCG-01 | Zero tolerated overlaps in sample | Spatial query report |
| G-PCG-02 | Nav coverage | Walkable % |
| G-PCG-03 | Instance budget | Per-cell cap |
| G-PCG-04 | Dungeon connectivity | BFS proof |
| G-PCG-05 | HLOD friendliness | Cluster variance |

---

## World Partition performance tiers

| Tier | Cell mood | Typical content |
|------|-----------|-----------------|
| T0 | Paranoid density | Urban cores |
| T1 | Pragmatic | Mixed biomes |
| T2 | Stoic sprawl | Wilderness + sparse POI |

---

## Rendering cost vs quality heuristics

| Axis | Cheap lie | Expensive truth |
|------|-----------|-----------------|
| GI | “We’ll fix in grade” | Leaks always find you |
| Reflections | SSR only whispers | Spec fights back |
| Shadows | Ignore cache | Memory sends regards |
| Foliage | Instance everything | Overdraw laughs |

---

## Nanite workflow spine

| Step | Owner | Output |
|------|-------|--------|
| N1 eligibility | TA | Mesh class matrix |
| N2 materials | TA | Complexity table |
| N3 hotspots | Perf | Capture stills |
| N4 fallback | TD | Platform policy |

---

## Lumen & reflections trade space

| Choice | Wins | Tax |
|--------|------|-----|
| High interior probes | Cozy corners | Memory |
| Aggressive spec | Bling | Noise + GPU |
| Locked exposure | Consistency | Art time |

---

## Chaos physics & replication discipline

| Concern | Policy |
|---------|--------|
| Debris | Hard count |
| Sleep | Aggressive kindness |
| Ownership | Written, not vibes |
| QA | Deterministic seeds first |

---

## Virtual Shadow maps policy grid

| Scenario | Default | Escape hatch |
|----------|---------|----------------|
| Open world sun | VSM bias | Platform override doc |
| Dense Nanite | Verify interaction | ADR required |

---

## Material & shader automation ledger

| Automation | Target |
|--------------|--------|
| Param lint | Naming drift |
| Tier variants | Look consistency |
| Subgraph reuse | Permutation explosion |

---

## Live Link pattern matrix

| Pattern | Transport | Cadence |
|---------|-----------|---------|
| L1 log tail | File | Event / low Hz |
| L2 heartbeat JSON | File | 1–5 Hz |
| L3 command queue | JSONL | Human-gated |

---

## Automation ROI (Phase 4)

| Investment | Payoff | Risk |
|------------|--------|------|
| `unreal-mcp-health.py` | Early “metrics missing” signal | Env misuse |
| Unreal doc tree checks | Prevents doc rot | None meaningful |
| PCG skills | Faster briefing | Over-invocation |

---

## Sensory covenant — engine midnight

You will hear the **hum of Nanite streaming** like a distant choir of GPUs
praying for mercy. You will see the **glow of Lumen** spill across geo that
should not be that generous at three in the morning. You will feel the **click**
of a clean PCG node alignment—brief holiness before the next merge conflict.
You will taste the metallic dread of a **two-gigabyte level load** and pretend
it is “almost done.” This covenant binds **sensation to discipline**: if it
felt spiritual and fixed nothing, you were decorating, not shipping.

---

## Graveyard quotes — engine programmer edition

> “We don’t have bugs—we have emergent narrative in the crash reporter.”

> “If your PCG seed changes every compile, QA will haunt you politely.”

> “Nanite forgives your mesh; your material graph does not.”

> “Lumen is not your therapist—it will expose every leak in your life and level.”

> “World Partition cells are roommates. Two writers in one cell is a horror film.”

> “Chaos sleeps until you ship—then it throws a party in the physics thread.”

> “Virtual shadow maps remember every shortcut you took at noon.”

> “Live Link telemetry is love letters from runtime—read them before they divorce you.”

> “A Blueprint compile storm is nature’s way of saying ‘serialize your MCP’.”

> “If your HLOD looks like modern art, players will interpret it as a bug.”

> “Console commands are spells—powerful, easy to misuse, and oddly permanent.”

> “Two gigabytes of level data is not ‘content richness’—it is a threat.”

> “Determinism is a romance language; ‘random vibes’ is not.”

> “The editor forgives nothing at 3am except your delusions.”

> “We are not importing Unreal—we are **becoming** the crash symbol.”

---

## Fifteen Unreal production workflow seeds

1. **Nanite pass Friday:** baseline `stat` stills → material triage → ADR.  
2. **Lumen leak hunt:** lock exposure → bisect probe density → capture repro cell.  
3. **PCG golden seeds:** pick three seeds; freeze exports in PR.  
4. **Dungeon BFS proof:** automated sampler prints counterexample module id.  
5. **City instancing audit:** histogram kits; kill snowflake facades.  
6. **WP boundary soak:** overnight traverse with log tail L1.  
7. **Chaos net replay:** single-player first; then replicate smallest slice.  
8. **Material permutation cap:** TA signs max variant count per family.  
9. **Subsystem init order map:** C++ owner writes one-page sequence diagram.  
10. **Blueprint mutex drill:** two agents plan; one applies MCP writes.  
11. **VSM cache policy per SKU:** table in SECURITY-adjacent perf appendix.  
12. **PCG nav hole repair:** secondary fill pass with documented entropy.  
13. **Streaming JSON heartbeat:** optional `StudioUnrealMetrics.json` contract.  
14. **Nanite fallback drill:** disable Nanite on hero set; verify readability.  
15. **Postmortem cell naming:** every hitch gets a cell id, not a vibe.

---

## Evolution hooks (Phase 5+)

- Typed MCP tool schemas per command family with timeouts.  
- CI still captures for Lumen/Nanite diffs.  
- PCG cell sampler integrated with `pcg-asset-generation-pipeline.md`.

---

## Index

- **Agents × Unreal:** `unreal/unreal-agent-capabilities.md`  
- **MCP policy:** `unreal/unreal-mcp-integration.md`  
- **Live Link:** `unreal/live-link-patterns.md`  
- **PCG:** `unreal/pcg-mastery/`  
- **World Partition:** `unreal/world-partition/`  
- **Rendering:** `unreal/rendering-tech/`  
- **Pipelines:** `pipelines/index.md`  
- **Optional metrics:** `scripts/unreal-mcp-health.py`

---

## Glossary

| Term | Meaning |
|------|---------|
| MCP | Model Context Protocol bridges for editor automation |
| PCG | Procedural Content Generation graphs in Unreal |
| WP | World Partition cell streaming |
| VSM | Virtual Shadow Maps |
| HLOD | Hierarchical Level of Detail |
| GI | Global illumination (Lumen domain) |

---

## Index of tables

| Table | Section |
|-------|---------|
| What Phase 4 adds | [What Phase 4 adds](#what-phase-4-adds) |
| MCP complexity | [Unreal MCP complexity matrix](#unreal-mcp-complexity-matrix) |
| PCG gates | [PCG quality gates (charter)](#pcg-quality-gates-charter) |
| WP tiers | [World Partition performance tiers](#world-partition-performance-tiers) |
| Cost vs quality | [Rendering cost vs quality heuristics](#rendering-cost-vs-quality-heuristics) |
| Nanite spine | [Nanite workflow spine](#nanite-workflow-spine) |
| Lumen trades | [Lumen & reflections trade space](#lumen--reflections-trade-space) |
| Chaos policy | [Chaos physics & replication discipline](#chaos-physics--replication-discipline) |
| VSM grid | [Virtual Shadow maps policy grid](#virtual-shadow-maps-policy-grid) |
| Materials ledger | [Material & shader automation ledger](#material--shader-automation-ledger) |
| Live Link | [Live Link pattern matrix](#live-link-pattern-matrix) |
| Automation ROI | [Automation ROI (Phase 4)](#automation-roi-phase-4) |
