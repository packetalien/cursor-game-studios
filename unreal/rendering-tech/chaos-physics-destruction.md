# Chaos physics & destruction

> **Work in progress.** Chaos delivers **cinematic collapse** and **deterministic nightmares**.

## Design rules

| Rule | Rationale |
|------|-----------|
| Bounded debris counts | perf + replication |
| Sleep policy | idle rubble should shut up |
| Network authority | who owns the explosion |

## Pipeline

`pipelines/chaos-destruction-pipeline.md`

## Debug

- Record **single-player** repro before blaming netcode.  
- Capture **GC clusters** if debris spawns infinitely — **someone loved that loop too much**.
