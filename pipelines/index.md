# Production pipelines — Cursor Game Studios

> **Work in progress.** Executable truth lives in your game repo, CI, and engine.
> These documents are **orchestration contracts**: who participates, what skills
> gate progress, and how you know you are done.

## Pipeline catalog

| ID | Document | One-line purpose |
|----|----------|------------------|
| `concept-to-gdd` | [concept-to-gdd-pipeline.md](concept-to-gdd-pipeline.md) | Idea → pillars → GDD backbone |
| `vertical-slice` | [vertical-slice-pipeline.md](vertical-slice-pipeline.md) | Playable slice with quality gates |
| `multi-agent-level` | [multi-agent-level-pipeline.md](multi-agent-level-pipeline.md) | World + level + TA swarm |
| `ci-agent-review` | [ci-agent-review-pipeline.md](ci-agent-review-pipeline.md) | Automation + human/agent review |
| `asset-pipeline` | [asset-pipeline.md](asset-pipeline.md) | Import → validate → ship-ready |
| `unreal-pcg` | [unreal-pcg-pipeline.md](unreal-pcg-pipeline.md) | PCG graphs + validation loops |
| `world-partition` | [world-partition-pipeline.md](world-partition-pipeline.md) | Streaming + bounds + load |
| `build-deploy` | [build-deployment-pipeline.md](build-deployment-pipeline.md) | Package, sign, release |
| `automated-testing` | [automated-testing-pipeline.md](automated-testing-pipeline.md) | Tests + soak + evidence |

## Automation

- `python scripts/studio-health-check.py` — structure + pipeline presence
- `python scripts/pipeline-runner.py <id>` — print ordered checklist
- `python scripts/studio-metrics.py` — JSON snapshot of repo shape
- `python scripts/nightly-studio-audit.py` — health + metrics + contamination scan

## Related docs

- [Advanced orchestration](../docs/advanced-orchestration.md)
- [Orchestration patterns](../docs/orchestration-patterns.md)
- [Phase 3 chapter](../03-phase-03-advanced-orchestration-production-pipelines.md)
