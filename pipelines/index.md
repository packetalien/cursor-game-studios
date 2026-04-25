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
| `world-partition-streaming` | [world-partition-streaming-pipeline.md](world-partition-streaming-pipeline.md) | WP streaming soak + hitch receipts |
| `nanite-optimization` | [nanite-optimization-pipeline.md](nanite-optimization-pipeline.md) | Nanite eligibility + material discipline |
| `lumen-lighting` | [lumen-lighting-pipeline.md](lumen-lighting-pipeline.md) | GI + reflections with budgets |
| `chaos-destruction` | [chaos-destruction-pipeline.md](chaos-destruction-pipeline.md) | Chaos sim + replication safety |
| `pcg-asset-generation` | [pcg-asset-generation-pipeline.md](pcg-asset-generation-pipeline.md) | PCG outputs as inventory + gates |
| `build-deploy` | [build-deployment-pipeline.md](build-deployment-pipeline.md) | Package, sign, release |
| `automated-testing` | [automated-testing-pipeline.md](automated-testing-pipeline.md) | Tests + soak + evidence |

## Automation

- `python scripts/studio-health-check.py` — structure + pipeline presence + Unreal doc tree (+ optional Phase2 marker)
- `python scripts/pipeline-runner.py <id>` — print ordered checklist
- `python scripts/studio-metrics.py` — JSON snapshot of repo shape
- `python scripts/nightly-studio-audit.py` — health + metrics + optional Unreal metrics probe + contamination scan
- `python scripts/unreal-mcp-health.py` — optional `CURSOR_UNREAL_UPROJECT` + `Saved/StudioUnrealMetrics.json`

## Related docs

- [Advanced orchestration](../docs/advanced-orchestration.md)
- [Orchestration patterns](../docs/orchestration-patterns.md)
- [Phase 3 chapter](../03-phase-03-advanced-orchestration-production-pipelines.md)
- [Phase 4 chapter](../04-phase-04-unreal-native-integration-procedural-mastery.md)
- [Unreal lane index](../unreal/index.md)
