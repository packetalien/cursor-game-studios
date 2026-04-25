# MANIFEST

> **Work in progress.** Inventory reflects the working tree.

## Table of contents

- [Attribution](#attribution)
- [Counts](#counts)
- [Directors](#directors)
- [Leads](#leads)
- [Specialists](#specialists)
- [Skills](#skills)
- [Rules](#rules)
- [Phase 2 artifacts](#phase-2-artifacts)
- [Phase 3 artifacts](#phase-3-artifacts)
- [Index](#index)
- [Glossary](#glossary)
- [Index of tables](#index-of-tables)

## Attribution

**Cursor Game Studios** is a Cursor-native structural port of [Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) (MIT, Donchitos).

---

## Counts

| Kind | Count |
|------|------:|
| Agents | 49 |
| Skills | 72 |
| Rules | 12 |

## Directors

- creative-director.md
- producer.md
- technical-director.md

## Leads

- art-director.md
- audio-director.md
- game-designer.md
- lead-programmer.md
- localization-lead.md
- narrative-director.md
- qa-lead.md
- release-manager.md

## Specialists

- accessibility-specialist.md
- ai-programmer.md
- analytics-engineer.md
- community-manager.md
- devops-engineer.md
- economy-designer.md
- engine-programmer.md
- gameplay-programmer.md
- godot-csharp-specialist.md
- godot-gdextension-specialist.md
- godot-gdscript-specialist.md
- godot-shader-specialist.md
- godot-specialist.md
- level-designer.md
- live-ops-designer.md
- network-programmer.md
- performance-analyst.md
- prototyper.md
- qa-tester.md
- security-engineer.md
- sound-designer.md
- systems-designer.md
- technical-artist.md
- tools-programmer.md
- ue-blueprint-specialist.md
- ue-gas-specialist.md
- ue-replication-specialist.md
- ue-umg-specialist.md
- ui-programmer.md
- unity-addressables-specialist.md
- unity-dots-specialist.md
- unity-shader-specialist.md
- unity-specialist.md
- unity-ui-specialist.md
- unreal-specialist.md
- ux-designer.md
- world-builder.md
- writer.md

## Skills

- adopt
- architecture-decision
- architecture-review
- art-bible
- asset-audit
- asset-spec
- balance-check
- brainstorm
- bug-report
- bug-triage
- changelog
- code-review
- consistency-check
- content-audit
- create-architecture
- create-control-manifest
- create-epics
- create-stories
- day-one-patch
- design-review
- design-system
- dev-story
- estimate
- gate-check
- help
- hotfix
- launch-checklist
- localize
- map-systems
- milestone-review
- onboard
- patch-notes
- perf-profile
- playtest-report
- project-stage-detect
- propagate-design-change
- prototype
- qa-plan
- quick-design
- regression-suite
- release-checklist
- retrospective
- reverse-document
- review-all-gdds
- scope-check
- security-audit
- setup-engine
- skill-improve
- skill-test
- smoke-check
- soak-test
- sprint-plan
- sprint-status
- start
- story-done
- story-readiness
- team-audio
- team-combat
- team-level
- team-live-ops
- team-narrative
- team-polish
- team-qa
- team-release
- team-ui
- tech-debt
- test-evidence-review
- test-flakiness
- test-helpers
- test-setup
- ux-design
- ux-review

## Rules

- ai-code.mdc
- cursor-game-studios-integrity.mdc
- data-files.mdc
- design-docs.mdc
- engine-code.mdc
- gameplay-code.mdc
- narrative.mdc
- network-code.mdc
- prototype-code.mdc
- shader-code.mdc
- test-standards.mdc
- ui-code.mdc

## Phase 2 artifacts

| Artifact | Role |
|----------|------|
| `02-phase-02-agent-skill-deepening.md` | Phase 2 charter |
| `scripts/phase2-deepen.py` | Idempotent deepening generator |
| `skills/index.md` | Categorized skill companion index |
| `skills/<category>/*.md` | 72 companion pages |
| `docs/studio-operating-doctrine.md` | Studio philosophy |
| `docs/orchestration-patterns.md` | Handoff patterns |
| `docs/agent-skill-affinity-matrix.md` | Agent ↔ skill heuristics |

All `.cursor/agents/**/*.md` and `.cursor/skills/**/SKILL.md` include a Phase 2
appendix after `<!-- PHASE2_DEEPENING_BEGIN -->`.

## Phase 3 artifacts

| Artifact | Role |
|----------|------|
| `03-phase-03-advanced-orchestration-production-pipelines.md` | Phase 3 charter |
| `docs/advanced-orchestration.md` | Multi-agent orchestration + rhythm |
| `pipelines/index.md` | Pipeline catalog |
| `pipelines/*-pipeline.md` | Nine production pipeline definitions |
| `scripts/studio-health-check.py` | Structure + optional Phase2 marker gate |
| `scripts/pipeline-runner.py` | Pipeline checklist printer |
| `scripts/studio-metrics.py` | JSON metrics snapshot |
| `scripts/nightly-studio-audit.py` | Health + metrics + contamination scan |

## Index

- Agents: [Directors](#directors), [Leads](#leads), [Specialists](#specialists)
- Skills: [Skills](#skills)
- Rules: [Rules](#rules)

## Glossary

| Term | Meaning |
|------|---------|
| Agent | Subagent definition under `.cursor/agents/` |
| Skill | Workflow playbook `SKILL.md` under `.cursor/skills/` |
| Rule | Path-scoped `.mdc` under `.cursor/rules/` |
| Upstream | Donchitos/Claude-Code-Game-Studios |

## Index of tables

| Table | Location |
|-------|----------|
| Counts | [Counts](#counts) |
| Phase 2 | [Phase 2 artifacts](#phase-2-artifacts) |
| Phase 3 | [Phase 3 artifacts](#phase-3-artifacts) |
| Glossary | [Glossary](#glossary) |