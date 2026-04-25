# Pipeline: Asset import → ship-ready

> **Work in progress.** Names, LODs, collisions, source control, and validation.

## Participation map

| Role | Agent |
|------|-------|
| Spec | `art-director` |
| Pipeline TA | `technical-artist` |
| Tools | `tools-programmer` |
| QA evidence | `qa-tester` |

## Skill sequence

| Order | Skill id | Gate |
|------:|----------|------|
| 1 | `asset-spec` | Naming + LOD policy |
| 2 | `asset-audit` | Repo hygiene |
| 3 | `smoke-check` | Import in clean editor session |
| 4 | `content-audit` | Licensing + attribution |

## MCP requirements

| MCP (optional) | Use |
|----------------|-----|
| DCC batch | Headless validation |
| Storage | Large file LFS policy |

## Success criteria

- Assets pass naming + size budgets; manifests generated.

## Failure criteria

- Broken references; missing mips; unapproved third-party assets.

## Monitoring

- Import error rate; cook warnings trend.

## Rollback

- Revert asset commit; restore manifest lock.

## Evolution (Phase 4+)

- Hash-based dedupe; automatic thumbnail diff.
