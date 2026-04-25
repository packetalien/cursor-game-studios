# PCG rule systems — deterministic + AI-assisted

> **Work in progress.** PCG is **rules with teeth**. AI proposes; rules enforce.

## Rule layers

| Layer | Example rule |
|-------|----------------|
| Spatial | min spacing, slope mask, waterline |
| Semantic | biome tag compatibility |
| Performance | max instances per cell |
| Narrative | landmark density caps |

## AI-assisted workflow

1. Human defines **hard constraints** (tables in ADR).  
2. Agent proposes PCG graph deltas.  
3. `pcg-quality-gates` pipeline validates output.  
4. Merge only if gates pass.

## Versioning

- Export PCG graph JSON to `Content/PCG/Exports/` on merge.
- Diff exports in PR when graphs change.

## Failure taxonomy

| Class | Fix |
|-------|-----|
| Overlap | tighten spacing / collision |
| Holes | fill pass or secondary scatter |
| Cost spike | LOD bias, instanced static mesh swap |
