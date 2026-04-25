# Agent–skill affinity matrix — Cursor Game Studios

> **Work in progress.** Heuristic pairings: which skills load cleanly after which
> agents, and where to serialize work.

## Skill complexity tiers

| Tier | Meaning | Examples |
|------|---------|----------|
| **T0** | Single-file orientation | `help`, `project-stage-detect` |
| **T1** | Scoped procedural loop | `smoke-check`, `estimate`, `changelog` |
| **T2** | Multi-artifact coordination | `sprint-plan`, `create-stories`, `architecture-decision` |
| **T3** | Cross-domain swarm risk | `team-ui`, `team-combat`, `dev-story` |

## Director × concern matrix

| Director | Vision | Architecture | Production arbitration |
|----------|--------|----------------|-------------------------|
| `creative-director` | Primary | Consult | Primary |
| `technical-director` | Consult | Primary | Primary |
| `producer` | Facilitate | Facilitate | Primary |

## Lead × primary skills

| Lead | First-class skills |
|------|-------------------|
| `game-designer` | `design-system`, `map-systems`, `balance-check` |
| `lead-programmer` | `create-architecture`, `dev-story`, `tech-debt` |
| `art-director` | `art-bible`, `asset-spec`, `ux-review` |
| `audio-director` | `team-audio`, `asset-audit` |
| `narrative-director` | `team-narrative`, `content-audit` |
| `qa-lead` | `qa-plan`, `regression-suite`, `gate-check` |
| `release-manager` | `release-checklist`, `patch-notes`, `hotfix` |
| `localization-lead` | `localize`, `consistency-check` |

## Specialist hot lanes

| Specialist cluster | Hot skills |
|--------------------|------------|
| Unreal + UE subs | `setup-engine`, `dev-story`, `perf-profile` |
| Unity cluster | `setup-engine`, `architecture-review`, `perf-profile` |
| Godot cluster | `setup-engine`, `prototype`, `dev-story` |
| `performance-analyst` | `perf-profile`, `soak-test`, `smoke-check` |
| `security-engineer` | `security-audit`, `gate-check` |

## MCP usage patterns (risk-ranked)

| Pattern | Risk | Mitigation |
|---------|------|------------|
| Read-only repo scan | Low | Default |
| Formatter / linter | Low | CI + local |
| Editor mutation | High | Single-writer queue |
| Remote build farm | Medium | Logs + timeouts |

## Failure modes when pairing

| Symptom | Likely cause | Fix |
|---------|---------------|-----|
| Duplicate logic | Two specialists, one feature | Assign single owner |
| Endless review | Missing acceptance criteria | Run `story-readiness` |
| Flaky “done” | Tests not named in story | Add test section to story template |

## Navigation

- Canonical skills: `.cursor/skills/*/SKILL.md`
- Categorized companions: `skills/index.md`
