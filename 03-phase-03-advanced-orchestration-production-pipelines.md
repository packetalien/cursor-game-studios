# Phase 03 — Advanced orchestration, production pipelines, and studio automation

> **Work in progress — use at your own risk.** Phase 3 turns Cursor Game Studios
> from a **library of excellence** into a **production organism**: orchestration
> contracts, repeatable pipelines, and scripts that tell you when the organism
> has a fever.

**Version:** 0.3.0  
**Phase:** 3 — Orchestration + pipelines + automation

---

## Table of contents

1. [Executive summary](#executive-summary)
2. [What Phase 3 adds](#what-phase-3-adds)
3. [Twelve production workflow profiles](#twelve-production-workflow-profiles)
4. [Orchestration complexity matrix](#orchestration-complexity-matrix)
5. [Pipeline failure taxonomy](#pipeline-failure-taxonomy)
6. [MCP coordination costs](#mcp-coordination-costs)
7. [Automation ROI heuristics](#automation-roi-heuristics)
8. [Sensory covenant — 3am rhythm](#sensory-covenant--3am-rhythm)
9. [Graveyard quotes](#graveyard-quotes)
10. [Fifteen orchestrated workflow seeds](#fifteen-orchestrated-workflow-seeds)
11. [Evolution hooks (Phase 4+)](#evolution-hooks-phase-4)
12. [Index](#index)
13. [Glossary](#glossary)
14. [Index of tables](#index-of-tables)

---

## Executive summary

Phase 3 ships **advanced orchestration doctrine**, **nine production pipelines**
under `pipelines/`, and **automation scripts** that enforce shape: health,
metrics, nightly audit. The studio should feel like a **living system**—not a
folder of vibes—while preserving the **1:1 upstream body** inside each agent
and skill file.

---

## What Phase 3 adds

| Layer | Location | Purpose |
|-------|----------|---------|
| Advanced orchestration | `docs/advanced-orchestration.md` | Directors/leads/specialists coordination |
| Pipelines | `pipelines/*.md` + `pipelines/index.md` | Repeatable production flows |
| Health | `scripts/studio-health-check.py` | Counts + pipeline presence (+ optional Phase2 marker) |
| Runner | `scripts/pipeline-runner.py` | Human/agent checklist printer |
| Metrics | `scripts/studio-metrics.py` | JSON snapshot of repo shape |
| Audit | `scripts/nightly-studio-audit.py` | Health + metrics + contamination scan |

---

## Twelve production workflow profiles

### P1 — Full game vertical slice

**Goal:** One playable column with receipts.  
**Primary pipeline:** `vertical-slice-pipeline.md`  
**Stress:** Single-writer discipline on shared maps.

### P2 — Concept → GDD backbone

**Goal:** Pillars, systems map, GDD skeleton approved.  
**Primary pipeline:** `concept-to-gdd-pipeline.md`

### P3 — Multi-agent level generation

**Goal:** World + level + TA + perf without merge necromancy.  
**Primary pipeline:** `multi-agent-level-pipeline.md`

### P4 — CI/CD + agent review

**Goal:** Green means sane; audits archived.  
**Primary pipeline:** `ci-agent-review-pipeline.md`

### P5 — Asset import → ship-ready

**Goal:** Names, LODs, licenses, cook sanity.  
**Primary pipeline:** `asset-pipeline.md`

### P6 — Unreal PCG loop

**Goal:** Deterministic regeneration with perf gates.  
**Primary pipeline:** `unreal-pcg-pipeline.md`

### P7 — World Partition management

**Goal:** Streaming health + soak evidence.  
**Primary pipeline:** `world-partition-pipeline.md`

### P8 — Build & deployment

**Goal:** Signed artifacts + rollback pins.  
**Primary pipeline:** `build-deployment-pipeline.md`

### P9 — Automated testing + evidence

**Goal:** Tests as inventory; evidence as currency.  
**Primary pipeline:** `automated-testing-pipeline.md`

### P10 — Security release lane

**Goal:** Multiplayer and privileged paths reviewed.  
**Agents:** `security-engineer`, `release-manager`  
**Skills:** `security-audit`, `release-checklist`

### P11 — Live ops patch discipline

**Goal:** Hotfix without folklore.  
**Agents:** `live-ops-designer`, `release-manager`  
**Skills:** `hotfix`, `patch-notes`

### P12 — Narrative content integration

**Goal:** Writer output becomes trackable data.  
**Agents:** `narrative-director`, `writer`, `tools-programmer`  
**Skills:** `team-narrative`, `content-audit`

### Twelve profiles at a glance

| ID | Profile | Primary pipeline / focus |
|----|---------|--------------------------|
| P1 | Vertical slice | `vertical-slice-pipeline.md` |
| P2 | Concept → GDD | `concept-to-gdd-pipeline.md` |
| P3 | Multi-agent level | `multi-agent-level-pipeline.md` |
| P4 | CI + agent review | `ci-agent-review-pipeline.md` |
| P5 | Asset pipeline | `asset-pipeline.md` |
| P6 | Unreal PCG | `unreal-pcg-pipeline.md` |
| P7 | World Partition | `world-partition-pipeline.md` |
| P8 | Build & deploy | `build-deployment-pipeline.md` |
| P9 | Automated testing | `automated-testing-pipeline.md` |
| P10 | Security release | skills + agents (see profile text) |
| P11 | Live ops patch | skills + agents |
| P12 | Narrative integration | skills + agents |

---

## Orchestration complexity matrix

| Class | Parallelism | Serialization | Typical risk |
|-------|---------------|----------------|--------------|
| Research / specs | High | Low | Misalignment |
| Implementation | Medium | Medium | Merge conflicts |
| Editor MCP | Low | **High** | Race corruption |
| CI verification | High | Low | Flake blindness |

---

## Pipeline failure taxonomy

| Code | Meaning | First response |
|------|---------|----------------|
| F1 | Missing owner | Assign named lead |
| F2 | Missing DoD | Run `story-readiness` |
| F3 | Tool timeout | Shrink batch; retry with logs |
| F4 | Flaky test | Quarantine + owner |
| F5 | Scope smuggling | Producer gate |

---

## MCP coordination costs

| Cost | Mitigation |
|------|------------|
| Stdio saturation | Fewer parallel MCP-heavy agents |
| Context noise | MCP only post-design-lock |
| Retry storms | Exponential backoff + circuit breaker |

---

## Automation ROI heuristics

| Signal | Automate |
|--------|----------|
| Same 12-step checklist weekly | Pipeline runner + CI |
| Same grep mistakes | Lint + audit script |
| Same “who owns file?” fight | Ownership matrix in orchestration doc |

---

## Sensory covenant — 3am rhythm

At three in the morning, the **sound** of a healthy studio is boring: a fan
curve, a distant test runner, the soft click of a reviewed merge. The **tension**
is not melodrama—it is a **seven-agent handoff** where everyone knows which wave
writes and which wave reads. The **satisfaction** is a clean automated build: not
because green is rare, but because green **means** something again.

---

## Graveyard quotes

> “We are not insomniacs by accident. We are insomniacs by schedule.”

> “If your pipeline needs heroics, your pipeline is not a pipeline—it is a cult.”

> “The build went green. The coffee stayed brown. We call that equilibrium.”

> “Seven agents in a handoff is not chaos—unless nobody owns the merge.”

> “Your ‘temporary’ hotfix is writing fan letters to the crash reporter.”

> “Automation is trust with receipts.”

> “We do not worship MCP. We meter it.”

> “A flaky test is a ghost in the machine—and ghosts vote in stand-ups.”

> “The organism never sleeps, but humans still must.”

> “If it is not in CI, it is folklore.”

> “Rollback is not defeat. Rollback is choreography.”

> “The profiler does not care about your intentions.”

> “Documentation is not love letters to the future—it is invoices.”

> “Ship the slice. Debate the universe later.”

> “The old tools can rest. We have pipelines now.”

---

## Fifteen orchestrated workflow seeds

Each seed lists **steps** (human/agent), not magic.

### Seed 1 — Cold open studio night

1. Human opens Cursor repo.  
2. Run `python scripts/nightly-studio-audit.py`.  
3. If fail: fix structure; if pass: pick active story.

### Seed 2 — Concept freeze

1. `brainstorm` skill playbook.  
2. Creative director memo: pillars.  
3. Lock `design/gdd` outline PR.

### Seed 3 — Systems map

1. `map-systems`.  
2. Systems designer cross-check dependencies.  
3. ADR stub for risky couplings.

### Seed 4 — Prototype spike

1. Producer caps timebox.  
2. `prototype` under `prototypes/` rules.  
3. `smoke-check` evidence attached.

### Seed 5 — Vertical slice kickoff

1. `story-readiness` on slice story.  
2. Lead programmer ownership matrix.  
3. `dev-story` implementation wave.

### Seed 6 — Seven-agent level wave

1. Read-mostly specs (world + UX + audio).  
2. Serialized Unreal edits (`multi-agent-level` pipeline).  
3. `perf-profile` + `smoke-check`.

### Seed 7 — CI + review merge train

1. `regression-suite` green.  
2. `code-review` + security notes for net code.  
3. Squash merge with linked story IDs.

### Seed 8 — Asset import week

1. `asset-spec` + naming CI.  
2. `asset-audit`.  
3. Cook report archived.

### Seed 9 — PCG hardening sprint

1. `unreal-pcg` pipeline determinism checks.  
2. Perf snapshots per seed set.  
3. ADR update for randomness sources.

### Seed 10 — World Partition soak

1. `world-partition` pipeline load.  
2. `soak-test` overnight.  
3. Hitch budget review with performance analyst.

### Seed 11 — Release candidate

1. `release-checklist`.  
2. `launch-checklist`.  
3. Signed artifacts + checksum manifest.

### Seed 12 — Hotfix war room

1. `hotfix` skill playbook.  
2. Single branch; single owner.  
3. Postmortem stub opened.

### Seed 13 — Narrative integration

1. `team-narrative`.  
2. Tools programmer data ingest plan.  
3. `content-audit` for tone + continuity.

### Seed 14 — Nightly audit cron (conceptual)

1. `nightly-studio-audit.py` in CI schedule.  
2. Publish `metrics.json` artifact.  
3. Alert on health regression.

### Seed 15 — Phase gate

1. `gate-check`.  
2. Directors triad sign-off on open risks.  
3. Update `production/` stage file (per your project convention).

---

## Evolution hooks (Phase 4+)

- Parse pipeline markdown into machine-readable steps for CI.
- Attach real engine project paths in consumer repos (not in this port repo).
- Deeper MCP policy files per environment (dev/stage/prod).

---

## Index

- **Advanced orchestration:** [docs/advanced-orchestration.md](docs/advanced-orchestration.md)
- **Pipelines:** [pipelines/index.md](pipelines/index.md)
- **Automation:** `scripts/studio-health-check.py`, `scripts/nightly-studio-audit.py`

---

## Glossary

| Term | Definition |
|------|------------|
| DoD | Definition of Done |
| MCP | Model Context Protocol tool servers (optional) |
| Pipeline | Repeatable multi-step production contract (`pipelines/`) |
| Serialized mutation | One writer at a time for contested surfaces |
| Wave | Orchestration batch (read vs write) |

---

## Index of tables

| Table | Section |
|-------|---------|
| Phase 3 adds | [What Phase 3 adds](#what-phase-3-adds) |
| Complexity | [Orchestration complexity matrix](#orchestration-complexity-matrix) |
| Failures | [Pipeline failure taxonomy](#pipeline-failure-taxonomy) |
| MCP costs | [MCP coordination costs](#mcp-coordination-costs) |
| ROI | [Automation ROI heuristics](#automation-roi-heuristics) |
| Profiles | [Twelve production workflow profiles](#twelve-production-workflow-profiles) |
| Profile glance | [Twelve profiles at a glance](#twelve-profiles-at-a-glance) |
| Glossary | [Glossary](#glossary) |

---

## Attribution

Upstream: [Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) (MIT, Donchitos).
