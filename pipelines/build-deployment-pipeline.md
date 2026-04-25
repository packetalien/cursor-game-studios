# Pipeline: Build & deployment

> **Work in progress.** Packaging, signing, channels, and rollback posture.

## Participation map

| Role | Agent |
|------|-------|
| Release | `release-manager` |
| Automation | `devops-engineer` |
| Security | `security-engineer` |
| Producer | `producer` |

## Skill sequence

| Order | Skill id | Gate |
|------:|----------|------|
| 1 | `release-checklist` | Preconditions |
| 2 | `launch-checklist` | Channel readiness |
| 3 | `changelog` / `patch-notes` | Comms |
| 4 | `hotfix` (if needed) | Controlled repair |

## MCP requirements

| MCP (optional) | Use |
|----------------|-----|
| CI / build farm | UAT or equivalent |
| Secrets store | Never in repo; inject at runtime |

## Success criteria

- Signed artifacts; checksum manifest; rollback version pinned.

## Failure criteria

- Unsigned binaries to public channel.
- Config drift between environments undocumented.

## Monitoring

- Crash-free sessions; download size; update adoption.

## Rollback

- Prior build re-published; feature flags toggled.

## Evolution (Phase 4+)

- Canary cohort automation with health gates.
