# Lumen — global illumination & reflections

> **Work in progress.** Lumen is beautiful until it is **a profiler crime scene**.

## Scenes

| Scene type | Notes |
|------------|-------|
| Interiors | probe density vs leak |
| Exteriors | skylight vs sun dominance |
| Mirrors | reflection budget honesty |

## Workflow

1. Lock **reference exposure** before tuning GI.  
2. Iterate **one axis** at a time (diffuse vs spec).  
3. Capture before/after stills for ADR.

## Pipeline

`pipelines/lumen-lighting-pipeline.md`

## 3am covenant

You will swear the bounce light moved on its own. **It did.** Sleep anyway.
