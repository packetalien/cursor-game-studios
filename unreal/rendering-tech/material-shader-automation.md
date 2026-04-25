# Material & shader automation

> **Work in progress.** Materials are **graphs**; graphs are **debt** unless governed.

## Automation targets

| Target | Automation |
|--------|------------|
| Parameter naming | lint via convention doc |
| Quality tiers | master material variants |
| Permutation explosion | MF library + shared subgraphs |

## MCP angle

- Read-only: export parameter metadata for dashboards.
- Writes: **serialized**; never parallel-compile storm.

## Pipeline tie-in

Nanite + Lumen pipelines reference material complexity gates.
