# Pipeline: Nanite optimization

> **Work in progress.** Geometry forgiveness is not a **budget** forgiveness.

## Participation map

| Role | Agent |
|------|-------|
| Rendering owner | `technical-director` |
| Mesh policy | `technical-artist` |
| Perf evidence | `performance-analyst` |
| Content | `world-builder` |

## Skill sequence

| Order | Skill id | Gate |
|------:|----------|------|
| 1 | `asset-spec` | Nanite eligibility + LOD policy |
| 2 | `perf-profile` | Worst-case triangle + overdraw pass |
| 3 | `smoke-check` | Platform matrix spot (where applicable) |
| 4 | `milestone-review` | Sign-off on quality vs cost trade |

## MCP requirements

| MCP (optional) | Rule |
|----------------|------|
| Editor | Read-only mesh stats first; serialize material swaps |

## Success criteria

- Documented Nanite vs fallback path per asset class.
- `stat` evidence archived for baseline and after pass.

## Failure criteria

- Unchecked material complexity on Nanite hero meshes.
- “Fix it in post” disguised as **infinite micro-detail**.

## Monitoring

Streaming clusters; shader permutation count.

## Rollback

Revert asset batch; re-enable authored LODs where needed.

## Evolution (Phase 5+)

Automated diff of Nanite cluster reports in CI.
