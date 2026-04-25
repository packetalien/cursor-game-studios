# Pipeline: CI/CD + agent review

> **Work in progress.** Combines objective CI gates with structured agent review
> so “green” still means “sane.”

## Participation map

| Role | Agent |
|------|-------|
| Automation owner | `devops-engineer` |
| Code quality | `lead-programmer` |
| Security pass | `security-engineer` |
| QA evidence | `qa-lead` |

## Skill sequence

| Order | Skill id | Gate |
|------:|----------|------|
| 1 | `qa-plan` | Test plan tied to stories |
| 2 | `code-review` | Human/agent review checklist |
| 3 | `security-audit` | For networked or privileged code |
| 4 | `regression-suite` | CI execution |
| 5 | `gate-check` | Release lane |

## MCP requirements

| MCP (optional) | Use |
|----------------|-----|
| CI server | Workflow dispatch, artifacts |
| VCS | Required checks on `main` |

## Success criteria

- CI green on required checks; review comments resolved or explicitly deferred.
- Security audit notes archived for multiplayer changes.

## Failure criteria

- Red builds merged via admin override without postmortem.
- Secrets in logs or artifacts.

## Monitoring

- Mean time to green; flaky test list; queue depth.

## Rollback

- Revert merge; disable bad workflow with incident note.

## Evolution (Phase 4+)

- SARIF ingestion for static analysis.
- Bot-opened review threads with agent summaries.
