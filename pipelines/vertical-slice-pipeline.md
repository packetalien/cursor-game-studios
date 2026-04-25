# Pipeline: Full game vertical slice

> **Work in progress.** Delivers one thin playable column: core loop, one level
> slice, minimal UI, one audio pass, buildable artifact.

## Participation map

| Track | Lead agent | Specialists |
|-------|------------|-------------|
| Code | `lead-programmer` | `gameplay-programmer`, engine cluster |
| World | `level-designer` | `world-builder`, `technical-artist` |
| UX | `ux-designer` | `ui-programmer` |
| Audio | `audio-director` | `sound-designer` |
| QA | `qa-lead` | `qa-tester`, `performance-analyst` |
| Ship | `producer` | `release-manager` |

## Skill sequence

| Order | Skill id | Gate |
|------:|----------|------|
| 1 | `story-readiness` | Slice story approved |
| 2 | `dev-story` | Implementation + tests |
| 3 | `smoke-check` | Green locally |
| 4 | `playtest-report` | Human playtest notes |
| 5 | `perf-profile` | Budget recorded |
| 6 | `gate-check` | Phase transition OK |

## MCP requirements

| MCP (optional) | Use |
|----------------|-----|
| Engine / editor | **Single-writer** mutation queue for BP/asset changes |
| CI | Artifact build + test job |
| VCS | Release branch discipline |

## Success criteria

- Slice runs on target config without blocking defects.
- Acceptance criteria from story are demonstrably met.
- Performance snapshot attached (even if “good enough”).

## Failure criteria

- Flaky tests waived without owner + deadline.
- Undefined ownership on shared files (merge storm).

## Monitoring

- Build time trend; test flakiness rate; crash count from playtests.

## Rollback

- Revert to last green tag; freeze feature adds until slice stable.

## Evolution (Phase 4+)

- Attach crash symbolication step for packaged builds.
- Add soak test gate for overnight automation.
