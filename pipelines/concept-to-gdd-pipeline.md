# Pipeline: Concept → GDD

> **Work in progress.** Transforms a raw concept into a reviewable GDD spine
> with explicit acceptance hooks.

## Participation map

| Role | Agent (primary) | Consults |
|------|-----------------|----------|
| Vision | `creative-director` | `producer` |
| Mechanics | `game-designer` | `systems-designer` |
| Space | `level-designer` | `world-builder` |
| UX | `ux-designer` | `accessibility-specialist` |
| Narrative | `narrative-director` | `writer` |

## Skill sequence

| Order | Skill id | Gate |
|------:|----------|------|
| 1 | `brainstorm` | Idea captured |
| 2 | `map-systems` | Systems index exists |
| 3 | `design-system` | Pillars + loops defined |
| 4 | `quick-design` OR full GDD template | Doc skeleton approved |
| 5 | `design-review` | Sign-off recorded |

## MCP requirements

| MCP (optional) | Use |
|----------------|-----|
| VCS | Branch + PR for GDD changes |
| Issue tracker | Epic/story links to doc sections |
| None required | Pipeline is valid filesystem-only |

## Success criteria

- GDD contains required sections per `design-docs` rule scope.
- Traceability: each major mechanic links to a system entry.
- Human EP approval logged (comment or PR approval).

## Failure criteria

- Missing acceptance criteria for core loops.
- Contradictions between pillars and detailed rules unresolved.

## Monitoring

- Weekly diff size on `design/gdd/**` (spikes imply thrash).
- Review turnaround time (SLA set by team).

## Rollback

- Tag GDD revision before major rewrites; restore from VCS tag.

## Evolution (Phase 4+)

- Auto-validate GDD section checklist in CI.
- Optional schema export for tools ingestion.
