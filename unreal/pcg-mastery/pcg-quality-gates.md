# PCG quality gates

> **Work in progress.** Automated validation for procedural output.

## Gate table

| Gate id | Metric | Threshold (example) |
|---------|--------|---------------------|
| G-PCG-01 | Overlap violations | 0 in sample N cells |
| G-PCG-02 | Navmesh coverage | ≥ 98% walkable |
| G-PCG-03 | Instance budget / cell | ≤ policy |
| G-PCG-04 | Connectivity (dungeons) | BFS from spawn |
| G-PCG-05 | HLOD friendliness | cluster variance score |

## Sampling strategy

- Stratified sample across **World Partition** cells (not only origin).
- Nightlies increase sample count; PRs use smaller N for speed.

## Artifacts

- `pcg_validation_report.json` per run (attach to CI).

## Escalation

If gates flap: freeze graph, bisect last PCG commit, add regression cell.
