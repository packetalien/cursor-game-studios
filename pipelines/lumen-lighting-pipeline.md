# Pipeline: Lumen lighting

> **Work in progress.** Global illumination until **global confusion**.

## Participation map

| Role | Agent |
|------|-------|
| Look | `art-director` |
| Lighting craft | `technical-artist` |
| Stability | `performance-analyst` |
| Play space | `level-designer` |

## Skill sequence

| Order | Skill id | Gate |
|------:|----------|------|
| 1 | `art-bible` | Reference exposure + mood anchors |
| 2 | `perf-profile` | Interior/exterior worst cells |
| 3 | `playtest-report` | Readability + leak report |
| 4 | `gate-check` | Ship/no-ship on probe/reflection budget |

## MCP requirements

| MCP (optional) | Rule |
|----------------|------|
| Editor | Capture before/after stills to ADR attachments |

## Success criteria

- No undocumented probe density spikes in streaming cells.
- Player-readability checklist signed by AD + LD.

## Failure criteria

- Flicker classified as “lore” instead of **bugs**.

## Monitoring

GPU time; reflection resolution pressure.

## Rollback

Feature-level Lumen scale reduction with tracked ADR.

## Evolution (Phase 5+)

HDR capture harness for regression stills.
