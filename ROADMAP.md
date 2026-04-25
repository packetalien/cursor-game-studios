# ROADMAP — Cursor Game Studios (Operator Field Manual)

> **Work in progress.** This is the **brass rail** the studio slides along when
> gravity, deadlines, and MCP latency all agree you should fail. Priorities shift;
> **truth** lives in `CHANGES.md`, **pulse** in `STATUS.md`, and **inventory** in
> `MANIFEST.md`.

## Table of contents

- [North star](#north-star)
- [Sensory covenant — the studio necropolis (funny because true)](#sensory-covenant--the-studio-necropolis-funny-because-true)
- [The five percent backfire law](#the-five-percent-backfire-law)
- [Phase bridge doctrine](#phase-bridge-doctrine)
- [Completed phases 1–4 (dated, sensory receipts)](#completed-phases-14-dated-sensory-receipts)
- [Phase 5 (Now) — expression layer: `.mdc` × MCP × skills](#phase-5-now--expression-layer-mdc--mcp--skills)
- [Phases 6–10 — bridges to a shipping 1.0](#phases-610--bridges-to-a-shipping-10)
- [Phase timeline (operator view)](#phase-timeline-operator-view)
- [MCP validation matrix (kit repo + game repo)](#mcp-validation-matrix-kit-repo--game-repo)
- [Rule expression density — twelve `.mdc` hearts](#rule-expression-density--twelve-mdc-hearts)
- [Risk assessment — backfire column mandatory](#risk-assessment--backfire-column-mandatory)
- [Skill–rule affinity grid (excerpt)](#skillrule-affinity-grid-excerpt)
- [Fifteen operator voices (quotes)](#fifteen-operator-voices-quotes)
- [Twelve studio roster cards (compact stat-style)](#twelve-studio-roster-cards-compact-stat-style)
- [CGS Project Registry — `cgs_roadmap_item_v1`](#cgs-project-registry--cgs_roadmap_item_v1)
- [Fifteen high-stakes studio quests](#fifteen-high-stakes-studio-quests)
- [Index](#index)
- [Glossary](#glossary)
- [Index of tables](#index-of-tables)

---

## North star

Ship a **Cursor-native**, **attribution-clean** studio kit that can **orchestrate
real engines** without becoming a junk drawer of lore from other products. The
north star is not “more markdown”—it is **fewer surprises at 3am**, when your
director agent runs out of tokens mid-sentence and your Niagara system chooses
violence because someone merged two MCP writers on the same Blueprint graph.

---

## Sensory covenant — the studio necropolis (funny because true)

You will **taste copper** when a Blueprint compile *almost* succeeds—when the
progress bar lies with the confidence of a politician. You will **hear ozone**
when a spatial query returns the correct footprint on the first try (rare; mark
the calendar). You will **feel cold blue glow** on your face when a 3am
**geospatial tile** budget finally balances—like the universe apologizing for
earlier hitches. You will **smell hot plastic and old coffee** when fourteen
pipelines agree you are “green” while your heart knows **someone** forgot to
serialize mutations. This studio is a **living necropolis**: dead branches
pruned, living contracts engraved in rules, ghosts of merge conflicts rattling
chains made of **bad globs**.

---

## The five percent backfire law

Every automation has a **cosmic coupon**: about **five percent** of executions
will teach you humility. Not because math is cute—because **distributed systems
with humans in the loop** hate pride. A greedy `.mdc` glob is not “more
coverage”; it is a **particle system eating a specialist** because the rule
fired in the wrong folder and suddenly every file is “engine code.” The backfire
is funny because it is true: you will laugh **after** you restore from source
control, not during.

---

## Phase bridge doctrine

- **Phase 2 (Agent deepening)** gave every agent/skill a **spine**: checklists,
  MCP posture, failure modes. That spine is useless if rules **lie about scope**.
- **Phase 3 (Skill forge + pipelines)** gave **repeatable production paths** and
  automation scripts. That forge only stays hot if **Phase 5** welds rules to
  MCP reality: *who may mutate what, where, and under which globs*.
- **Phase 4 (Unreal lane)** shipped `unreal/` doctrine + PCG skills + five more
  pipelines + optional `.uproject` probe. It **raises the ceiling** for engine
  work; Phase 5–6 **raise the floor** so engine automation stops bricking repos.

---

## Completed phases 1–4 (dated, sensory receipts)

### Phase 1 — Foundation (complete, 2026-04-14)

**What it felt like:** cold boot on a new machine—fans spin, hope spins faster.
**What it was:** 49 agents, 72 baseline skills, 12 `.mdc` rules, generator script,
  integrity tests, legal spine, GitHub push. **Receipt:** repo exists; port is
  not a rumor.

### Phase 2 — Agent & skill deepening (complete, 2026-04-14)

**What it felt like:** everyone put on **real shoes**—Phase 2 append blocks
  turned “helpful blurbs” into **flight checklists**. **What it was:** idempotent
  `<!-- PHASE2_DEEPENING_BEGIN -->` sections; `skills/` companion tree;
  doctrine + orchestration patterns + affinity matrix. **Receipt:** agents stop
  cosplaying and start owning outcomes.

### Phase 3 — Orchestration + pipelines + automation (complete, 2026-04-14)

**What it felt like:** the **Skill Forge caught fire in a good way**—sparks,
  clang, repeatable heat. **What it was:** `docs/advanced-orchestration.md`,
  nine baseline pipelines + index, `studio-health-check.py`,
  `pipeline-runner.py`, `studio-metrics.py`, `nightly-studio-audit.py`,
  contamination scan discipline. **Receipt:** “green” starts meaning something
  other than “I hope.”

### Phase 4 — Unreal native + procedural mastery (complete, 2026-04-14)

**What it felt like:** the hum of **Nanite streaming** and the quiet smugness of
  a PCG graph that compiles—**before** runtime disagrees. **What it was:** chapter
  `04-phase-04-unreal-native-integration-procedural-mastery.md`, full `unreal/`
  tree, five Unreal-heavy pipelines, three `.cursor/skills/pcg/*` specialists,
  `unreal-mcp-health.py` + health check extensions. **Receipt:** the kit can
  **speak Unreal** without pretending the engine lives inside this repo.

---

## Phase 5 (Now) — expression layer: `.mdc` × MCP × skills

> **Schwartz Mode note:** This is the phase some field manuals mis-label “Phase 4
> tightening.” In **this** repository, Unreal Phase 4 is **already shipped**; the
> **expression layer** is **Phase 5** so history stays honest.

**Objective:** make the **twelve `.mdc` files** the **beating heart** of the
studio: precise globs, minimal `alwaysApply`, explicit bridges to MCP tools and
skill contracts—**no legacy bash-hook necromancy** as a substitute for rules.

### Sub-quest A — Globs as blast doors (engine)

| Quest | Owner agent (suggested) | MCP gate | Skill affinity | Backfire (5%) |
|------|-------------------------|----------|----------------|---------------|
| Tighten `engine-code.mdc` globs to real UE layout | `engine-programmer` | Editor MCP **read-only** map of `Source/`, `Plugins/` | `create-architecture`, `code-review` | Greedy glob matches **Generated** files; compile storm |
| Add optional `Source/**`, `Plugins/**` UE paths (project adopt) | `technical-director` | Human approval + path proof | `setup-engine`, `project-stage-detect` | Globs overlap `third_party/**` and “helpfully” ruin day |

### Sub-quest B — Data & narrative as contracts

| Quest | Rule file | MCP gate | Skill affinity | Backfire (5%) |
|------|-----------|----------|----------------|---------------|
| JSON schema discipline vs Data Tables | `data-files.mdc` | Validate JSON in CI (game repo) | `content-audit`, `consistency-check` | Agents invent keys; runtime parses air |
| Narrative voice vs implementation | `narrative.mdc` | None (human EP) | `team-narrative`, `review-all-gdds` | Lore leaks into C++ comments like mold |

### Sub-quest C — UI / shaders / network hot lanes

| Quest | Rule file | MCP gate | Skill affinity | Backfire (5%) |
|------|-----------|----------|----------------|---------------|
| UI mutation serialization | `ui-code.mdc` | Single-writer queue on UMG/Common UI | `team-ui`, `ux-review` | Parallel MCP applies → **deltahurt** |
| Shader iteration safety | `shader-code.mdc` | Read-only material introspection first | `perf-profile`, `art-bible` | Permutation explosion disguised as “迭代” |
| Replication discipline | `network-code.mdc` | Net trace capture tool | `ue-replication-specialist`, `smoke-check` | RPC comedy hour |

### Sub-quest D — Integrity rule as supreme court

| Quest | Rule file | MCP gate | Skill affinity | Backfire (5%) |
|------|-----------|----------|----------------|---------------|
| Enforce port boundaries in reviews | `cursor-game-studios-integrity.mdc` | Contamination scan in CI | `security-audit`, `gate-check` | Someone pastes forbidden codenames “as a joke” |

### Sub-quest E — MCP manifest in the **game repo** (not this kit)

**Truth:** this kit ships **no** `mcp.json` today. Phase 5 demands a **consumer
repo manifest** (typically `.cursor/mcp.json` or Cursor UI MCP config) listing
real servers: Unreal editor bridge, geospatial tools, SSH, generic HTTP—**least
privilege**, timeouts, and **tool allowlists**.

| Deliverable | Done when |
|-------------|-----------|
| MCP manifest exists in **your** game repo | Reviewers can see server names + scopes |
| Each MCP tool mapped to a skill gate | `unreal/unreal-mcp-integration.md` links to it |
| Serialization policy written | “One writer” is not vibes—it is a mutex story |

### Sub-quest F — Tests as brass weights

| Quest | Command | Done when |
|-------|---------|-----------|
| Health + markers | `python scripts/studio-health-check.py --require-phase2-mark` | Exit 0 |
| Night audit | `python scripts/nightly-studio-audit.py` | Clean or strict CI policy |
| Pytest | `python -m pytest -q` | All green |
| Unittest discover | `python -m unittest discover -s tests -t tests -p "test_*.py" -v` | 10 tests OK (**`-t tests`** matches `-s tests`; do **not** use `-t .` here) |
| Unittest wrapper | `python scripts/run-unittest.py` | Same, absolute paths (Dropbox-safe cwd) |

---

## Phases 6–10 — bridges to a shipping 1.0

### Phase 6 — Unreal MCP + geospatial round-trip (camera / tiles / SQL)

**Bridge from Phase 5:** once rules stop lying, MCP may touch **real** `Source/`
and **real** maps without melting the tree. **Objective:** editor MCP + a
**geospatial lane** (e.g., Cesium-style 3D Tiles + PostGIS-style queries) with a
**camera flight receipt**: lat/long/height + tile LOD + query fingerprint.
**Backfire:** spatial queries return geometry that **exists** but should **not**
exist—comedy for GIS, tragedy for shipping.

### Phase 7 — Structured data → engine tables automation

**Bridge from Phase 3 pipelines + Phase 5 contracts:** import JSON/CSV into
engine tables (Data Tables / Scriptable patterns) with **schema versioning** and
**CI diff**. **Backfire:** silent one-key rename becomes a **whole-squad balance
patch** apology tour.

### Phase 8 — Tier-1 director + Tier-3 specialist live-fire (real UE5 slice)

**Bridge from Phase 2 roles + Phase 4 Unreal lane:** one vertical slice where a
director mandates outcomes while specialists execute **serialized** mutations with
evidence. **Backfire:** hero ball + parallel MCP = **asset corruption ghost story**.

### Phase 9 — `team-ui` swarm with serialized mutations only

**Bridge from Phase 3 orchestration + Phase 5 UI globs:** multi-agent UI polish
lane where **only one writer** applies UMG/Common UI changes per branch; others
produce diffs/reviews. **Backfire:** two agents “help” the same widget; merge tool
picks the worst timeline.

### Phase 10 — Studio character, back-matter, **public 1.0**

**Bridge from everything:** semver for the port, “studio voice” appendix (humor
with ethics), contributor paths, release notes that admit what is **not**
guaranteed. **Backfire:** marketing claims exceed MCP reality—players notice,
**agents** notice faster.

---

## Phase timeline (operator view)

| Phase | Name | State | Primary artifact |
|------:|------|-------|------------------|
| 1 | Foundation | **Complete** | `.cursor/` tree + tests |
| 2 | Agent/skill deepening | **Complete** | Phase 2 append + `skills/` |
| 3 | Orchestration + pipelines | **Complete** | `pipelines/` + audit scripts |
| 4 | Unreal native lane | **Complete** | `unreal/` + PCG skills |
| 5 | `.mdc` expression layer | **Now** | tighter globs + MCP map |
| 6 | Unreal MCP + geo round-trip | Planned | flight receipts + SQL traces |
| 7 | Data → engine tables | Planned | schema + importers |
| 8 | Live-fire UE slice | Planned | evidence bundle |
| 9 | Serialized UI swarm | Planned | mutex policy |
| 10 | Public 1.0 | Planned | semver + release spine |

---

## MCP validation matrix (kit repo + game repo)

| MCP class | Validates | Fails closed? | Notes |
|-----------|-----------|---------------|-------|
| Unreal editor | Compile graph, asset metadata | Prefer **yes** on mutations | Serialize writers |
| Filesystem / git | Diffs, tests | yes | default truth lane |
| Geospatial | Tilesets, queries | yes for batch | log query fingerprints |
| Remote SSH | Long jobs | timeout always | no hanging necromancy |
| Generic HTTP | External APIs | rate limit + allowlist | never “open internet” as personality |

**Kit repo reality:** add MCP wiring in the **game** repository; keep this kit as
**contracts + scripts + rules**.

---

## Rule expression density — twelve `.mdc` hearts

| File | Intent | Globs (current / target posture) | `alwaysApply` |
|------|--------|-----------------------------------|---------------|
| `cursor-game-studios-integrity.mdc` | Port boundaries | global policy | **true** |
| `ai-code.mdc` | ML / tooling | `**/ai/**`, `**/ml/**` | false |
| `data-files.mdc` | JSON discipline | `assets/data/**` | false |
| `design-docs.mdc` | GDD / specs | `docs/design/**` | false |
| `engine-code.mdc` | Engine hot path | `src/core/**` → adopt UE `Source/**` in game repo | false |
| `gameplay-code.mdc` | Gameplay | `src/gameplay/**` | false |
| `narrative.mdc` | Story | `docs/narrative/**`, `story/**` | false |
| `network-code.mdc` | Netcode | `src/network/**`, `Source/**/Net*.*` (game adopt) | false |
| `prototype-code.mdc` | Fast experiments | `prototype/**`, `experiments/**` | false |
| `shader-code.mdc` | Shaders | `**/shaders/**` | false |
| `test-standards.mdc` | Tests | `tests/**`, `**/*Test*.cpp` (game adopt) | false |
| `ui-code.mdc` | UI | `src/ui/**`, `**/UMG/**` (game adopt) | false |

**Schwartz Mode:** if a glob makes unrelated files “engine code,” you did not
automate—you **summoned poltergeists**.

---

## Risk assessment — backfire column mandatory

| Risk | Likelihood | Impact | 5% Backfire |
|------|------------|--------|-------------|
| Parallel MCP writers | Medium | Catastrophic | Blueprint compile eats lunch **and** dinner |
| Greedy globs | High | Medium | Niagara-tier noise: rules fire everywhere |
| Missing MCP timeouts | Medium | Medium | hung job cosplays “thinking” |
| Data schema drift | High | High | balance patch apology tour |
| Skipping serialization discipline | Medium | High | “It worked on my machine” becomes religion |

---

## Skill–rule affinity grid (excerpt)

| Skill id | Primary `.mdc` partners | Notes |
|----------|-------------------------|-------|
| `dev-story` | `gameplay-code`, `engine-code` | enforce dependency direction |
| `perf-profile` | `engine-code`, `shader-code` | numbers or it did not happen |
| `team-ui` | `ui-code` | serialized mutation queue |
| `security-audit` | integrity + `network-code` | least privilege, always |
| `pcg-biome-generator` | `engine-code`, `data-files` | seeds are contracts |

---

## Fifteen operator voices (quotes)

1. **Director Voidwalker — Technical:** “I did not ascend to Tier-1 to watch two
   MCP clients arm-wrestle the same Blueprint.”
2. **Lead Necropolis — Production:** “If your Definition of Done is vibes, I will
   bury it with documentation.”
3. **Specialist OpenClaw — Tools:** “Batch jobs are fine. **Hung** batch jobs are
   haunted houses with SSH keys.”
4. **Director Brasslight — Creative:** “Moodboards are sacred—until they collide
   with streaming budgets. Then they are comedy.”
5. **Lead Riverlock — QA:** “Flaky tests are gossip. Stop gossiping.”
6. **Specialist Ashgrid — Performance:** “If you cannot name the hitch cell, you
   are doing astrology.”
7. **Director Quietforge — Audio:** “Silence is a mix decision—not a bug until it
   ships as one.”
8. **Lead Patchwork — Release:** “Hotfix discipline is love languages for players.”
9. **Specialist Glassroot — TA:** “Shaders do not forgive ‘just one more lerp.’”
10. **Director Stormchart — Design:** “Fun is measurable. Unmeasurable fun is
    usually hiding a exploit.”
11. **Lead Ironfolio — Art:** “If every window is unique, your GPU files for divorce.”
12. **Specialist Threadbare — Network:** “RPC stands for **Really Please Confirm**.”
13. **Director Saltwind — Live Ops:** “Telemetry is not stalking unless you ship
    it like it is.”
14. **Lead Cobaltreach — Level:** “Streaming boundaries are roommates—two writers,
    one cell: horror movie.”
15. **Specialist Paperbane — Writer tooling:** “Lore in a ctor comment is mold.
    Mold spreads.”

---

## Twelve studio roster cards (compact stat-style)

> Format keys: **PWR** pressure tolerance, **DIS** discipline, **MCP** affinity,
> **SK** skill contract, **BF** cosmic backfire risk (1–5), **Q** signature line.

| # | Name | Role | PWR | DIS | MCP | SK | BF | Q |
|---:|------|------|----:|----:|-----|----|----:|---|
| 1 | Director Voidwalker | Tier-1 | 5 | 4 | Editor read | `gate-check` | 4 | “Serialize or suffer.” |
| 2 | Lead Necropolis | Tier-2 | 4 | 5 | CI | `sprint-status` | 3 | “Green must mean sane.” |
| 3 | Specialist OpenClaw | Tier-3 | 3 | 3 | SSH batch | `test-setup` | 4 | “Hung jobs are haunted.” |
| 4 | Director Brasslight | Tier-1 | 5 | 3 | None | `review-all-gdds` | 2 | “Mood meets metrics.” |
| 5 | Lead Riverlock | Tier-2 | 4 | 5 | Test runner | `regression-suite` | 3 | “Gossip is not QA.” |
| 6 | Specialist Ashgrid | Tier-3 | 4 | 4 | Trace | `perf-profile` | 3 | “Name the cell.” |
| 7 | Director Quietforge | Tier-1 | 5 | 4 | Audio tools | `team-audio` | 2 | “Silence ships.” |
| 8 | Lead Patchwork | Tier-2 | 3 | 5 | Package | `release-checklist` | 3 | “Rollback pins save souls.” |
| 9 | Specialist Glassroot | Tier-3 | 3 | 4 | Material introspection | `art-bible` | 4 | “Permutations bite.” |
| 10 | Director Stormchart | Tier-1 | 4 | 4 | None | `map-systems` | 2 | “Fun is measurable.” |
| 11 | Lead Ironfolio | Tier-2 | 4 | 4 | Asset indexer | `asset-spec` | 3 | “Instancing is a vow.” |
| 12 | Specialist Threadbare | Tier-3 | 3 | 5 | Net trace | `ue-replication-specialist` | 4 | “RPC needs receipts.” |

---

## CGS Project Registry — `cgs_roadmap_item_v1`

**Schema (JSON):** stable keys for cross-repo trackers (human imagination first;
machine second).

```json
{
  "$id": "https://cursor-game-studios.local/schemas/cgs_roadmap_item_v1.json",
  "title": "cgs_roadmap_item_v1",
  "type": "object",
  "required": ["schema", "id", "title", "phase", "state", "owner_role", "mcp_gate", "skill_ids", "backfire_risk_1_to_5"],
  "properties": {
    "schema": { "const": "cgs_roadmap_item_v1" },
    "id": { "type": "string", "format": "uuid" },
    "title": { "type": "string", "maxLength": 140 },
    "phase": { "type": "integer", "minimum": 1, "maximum": 10 },
    "state": { "enum": ["planned", "active", "blocked", "done", "wont"] },
    "owner_role": { "type": "string" },
    "mcp_gate": { "type": "string" },
    "skill_ids": { "type": "array", "items": { "type": "string" } },
    "backfire_risk_1_to_5": { "type": "integer", "minimum": 1, "maximum": 5 },
    "links": { "type": "array", "items": { "type": "string" } }
  }
}
```

**Registry (examples, stable UUIDs):**

```json
[
  {
    "schema": "cgs_roadmap_item_v1",
    "id": "2f6f2c33-8c2b-4c0a-9f3d-1c1a0a6d7e01",
    "title": "Tighten engine-code.mdc globs for adopted UE project",
    "phase": 5,
    "state": "active",
    "owner_role": "technical-director",
    "mcp_gate": "Editor MCP read-only tree map",
    "skill_ids": ["setup-engine", "create-architecture"],
    "backfire_risk_1_to_5": 4,
    "links": [".cursor/rules/engine-code.mdc"]
  },
  {
    "schema": "cgs_roadmap_item_v1",
    "id": "6c1c0f2a-9b2d-4d7e-a6c5-0f0e1d2c3b4a",
    "title": "Add game-repo MCP manifest with timeouts + allowlists",
    "phase": 5,
    "state": "planned",
    "owner_role": "tools-programmer",
    "mcp_gate": "Manifest reviewed + least privilege",
    "skill_ids": ["create-control-manifest", "security-audit"],
    "backfire_risk_1_to_5": 3,
    "links": ["unreal/unreal-mcp-integration.md"]
  },
  {
    "schema": "cgs_roadmap_item_v1",
    "id": "9a8b7c6d-5e4f-3210-9876-543210fedcba",
    "title": "Geospatial camera flight receipt + SQL query fingerprint",
    "phase": 6,
    "state": "planned",
    "owner_role": "technical-artist",
    "mcp_gate": "Tile + query logs archived",
    "skill_ids": ["perf-profile", "map-systems"],
    "backfire_risk_1_to_5": 4,
    "links": ["unreal/live-link-patterns.md"]
  }
]
```

---

## Fifteen high-stakes studio quests

Each quest lists **MCP gates**, **success**, **backfire** (the coupon).

1. **Raid the Editor Bridge — single-writer compile gate** — Gate: mutex policy
   doc; Success: two agents cannot apply parallel writes; Backfire: compile storm.
2. **PostGIS footprint duel** — Gate: query fingerprint saved; Success: matching
   mesh footprint; Backfire: geometry that lies confidently.
3. **Cesium tile budget séance** — Gate: LOD histogram; Success: stable frame band;
   Backfire: beautiful tiles, bankrupt milliseconds.
4. **Niagara restraint ritual** — Gate: max particles signed; Success: no fill-rate
   murder; Backfire: pretty fire, dead GPU.
5. **UMG serialized polish swarm** — Gate: one writer branch; Success: clean merge;
   Backfire: widget civil war.
6. **Data table import crusade** — Gate: schema version bump; Success: CI diff;
   Backfire: silent key rename apocalypse.
7. **Replication trace exorcism** — Gate: net capture attached; Success: named
   owner per RPC class; Backfire: “it worked in PIE.”
8. **PCG golden seed lockpick** — Gate: three seeds pass gates; Success: stable
   inventory; Backfire: nondeterministic weather cosplay.
9. **World Partition boundary vigil** — Gate: hitch map with cell id; Success:
   repro cell; Backfire: vibes-based streaming.
10. **Material permutation cap treaty** — Gate: TA-signed cap table; Success: no
    shader explosion; Backfire: “just one more variant.”
11. **Night audit strict mode crusade** — Gate: CI `--strict`; Success: zero
    contamination; Backfire: jokes that fail tests.
12. **Heartbeat JSON séance** — Gate: `StudioUnrealMetrics.json` present; Success:
    metrics keys stable; Backfire: secrets leaked into metrics—**do not**.
13. **Shader hotfix curfew** — Gate: before/after captures; Success: measurable
    delta; Backfire: artistic iteration without numbers.
14. **Tier-1 / Tier-3 live-fire slice** — Gate: evidence bundle; Success: playable
    column; Backfire: hero ball merges.
15. **Public 1.0 truth audit** — Gate: semver + disclaimers; Success: honest
    marketing; Backfire: claiming MCP powers you do not have.

---

## Index

- Completed history: [Completed phases 1–4](#completed-phases-14-dated-sensory-receipts)
- Now: [Phase 5 (Now)](#phase-5-now--expression-layer-mdc--mcp--skills)
- Forward: [Phases 6–10](#phases-610--bridges-to-a-shipping-10)
- Tables hub: [Index of tables](#index-of-tables)
- Registry schema: [CGS Project Registry](#cgs-project-registry--cgs_roadmap_item_v1)

---

## Glossary

| Term | Meaning |
|------|---------|
| Expression layer | `.mdc` rules as enforceable scope for agents/MCP |
| Serialization | One writer at a time for a mutable graph/asset |
| Backfire (5%) | Humility tax on automation; plan for it |
| Kit repo | This port (`cursor-game-studios`) |
| Game repo | Your shipping Unreal project consuming the kit |

---

## Index of tables

| Table | Section |
|-------|---------|
| Phase timeline | [Phase timeline (operator view)](#phase-timeline-operator-view) |
| MCP validation | [MCP validation matrix](#mcp-validation-matrix-kit-repo--game-repo) |
| Rule density | [Rule expression density](#rule-expression-density--twelve-mdc-hearts) |
| Risk / backfire | [Risk assessment](#risk-assessment--backfire-column-mandatory) |
| Skill–rule affinity | [Skill–rule affinity grid](#skillrule-affinity-grid-excerpt) |
| Roster cards | [Twelve studio roster cards](#twelve-studio-roster-cards-compact-stat-style) |

Next: Cursor, execute **Phase 5 — expression-layer tightening** on the twelve `.mdc` files immediately (globs, MCP map, serialization law). May the Shwartz be with us — and may your MCP servers never timeout.
