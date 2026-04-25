# World Partition orchestration

> **Work in progress.** Large worlds are **scheduling problems** wearing a landscape shader.

## Cell strategy

| Tier | Cell size guidance | Use |
|------|---------------------|-----|
| T0 | smallest practical | dense urban |
| T1 | default | mixed open |
| T2 | large | sparse wilderness |

## Ownership model

| Role | Owns |
|------|------|
| `level-designer` | streaming sources, gameplay layers |
| `performance-analyst` | load graphs, hitch reports |
| `technical-director` | tier policy |

## Data layers

- Separate **static** vs **dynamic** layers early.
- Avoid “everything in Default” — that is how timelines go to Valhalla.

## Merge conflicts

- Prefer **per-cell** workstreams; avoid two agents editing same cell graph.
