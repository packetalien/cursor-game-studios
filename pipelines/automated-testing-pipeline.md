# Pipeline: Automated testing + evidence

> **Work in progress.** Tests are inventory; evidence is currency.

## Participation map

| Role | Agent |
|------|-------|
| QA lead | `qa-lead` |
| Implementers | `gameplay-programmer`, specialists by domain |
| Flake hunter | `qa-tester` |

## Skill sequence

| Order | Skill id | Gate |
|------:|----------|------|
| 1 | `test-setup` | Harness ready |
| 2 | `qa-plan` | Coverage map |
| 3 | `regression-suite` | CI green |
| 4 | `test-evidence-review` | Artifacts attached to stories |
| 5 | `test-flakiness` | Known flakes have owners |

## MCP requirements

| MCP (optional) | Use |
|----------------|-----|
| CI | Parallel test shards |
| Artifact storage | Logs, videos, traces |

## Success criteria

- Each P0 story has linked test evidence.
- Flake budget not exceeded without explicit waiver.

## Failure criteria

- Red ignored as “noise.”
- Tests that cannot fail.

## Monitoring

- Flake rate; duration p95; coverage (if collected).

## Rollback

- Disable offending suite with incident ticket; restore ASAP.

## Evolution (Phase 4+)

- Mutation testing sample for critical modules.
