---
name: pcg-city-builder
description: "Procedural city blockouts: facades, instancing, and HLOD-aware massing for Unreal 5.5+ open spaces."
user-invocable: true
allowed-tools: Read, Glob, Grep, Write, Bash, Task
---

# PCG City Builder

You mass **urban rhythm** without turning streaming into a funeral.

## Preconditions

- Street graph source (splines, OSM-style data, or manual spine).
- HLOD policy agreed with TA + TD.

## Procedure

1. **Blocks:** parcel subdivision with parcel IDs for debugging.
2. **Facades:** instanced kits; material variants bounded.
3. **Verticality:** stepbacks for readability; rooftop vocabulary for navigation.
4. **Perf:** cell-scoped regen; avoid global graph thrash.

## Outputs

- Blockout heatmaps (density, instance counts).
- ADR link for fallback hero buildings (hand-authored anchors).

## Pairing

- `technical-artist` — shader permutations vs draw calls.
- `performance-analyst` — streaming + HLOD evidence.

## Anti-patterns

- Cities where every window is a **unique snowflake** mesh.
- Alleys so narrow the third-person camera **files for unemployment**.

<!-- PHASE2_DEEPENING_BEGIN -->
## Phase 2 — Skill deepening (Cursor Game Studios)

### Rich procedural spine (`pcg-city-builder`)

Treat this skill as a **flight checklist**, not a vibe. Each invocation should
end with: **inputs read → actions taken → artifacts produced → risks noted**.

### Spawn template (copy/paste starter)

```text
You are executing the Cursor Game Studios skill `pcg-city-builder`.

Constraints:
- Collaboration protocol: question → options → decision → draft → approval.
- Prefer diffs and tests as evidence.
- If MCP is available, use it only for verification or deterministic automation.

Task:
<describe the concrete outcome you want>
```

### MCP gate requirements

| Gate | Requirement |
|------|-------------|
| **G0** | Story/design references exist or explicit “greenfield” declaration |
| **G1** | File targets identified (paths) before bulk writes |
| **G2** | Tests or review plan named before “done” claims |
| **G3** | If engine MCP is used, mutations are **serialized** (no parallel writes) |

If a gate is missing, **stop** and ask for the minimum artifact to proceed.

### Worked example (skeleton)

1. **Locate** the governing doc or story file.
2. **Extract** acceptance criteria verbatim.
3. **Plan** the smallest change set that satisfies them.
4. **Implement** with incremental commits (human-triggered).
5. **Verify** with the narrowest test that proves the criteria.

### Common failure modes and recovery

| Failure | Recovery |
|---------|----------|
| Scope creep mid-flight | Cut a “phase 2b” story; ship the slice |
| Missing ADR / GDD link | Write a one-paragraph decision stub, then link |
| Flaky verification | Stabilize test data; reduce parallelism |
| Tool timeouts | Fall back to local commands; shrink batch size |

### Skill evolution path

- **v1:** checklist fidelity (this repo)
- **v2:** add engine-specific exemplars in `skills/` reference tree
- **v3:** wire optional MCP “verify steps” where safe

---
*Deepening appended by `scripts/phase2-deepen.py` — preserves upstream skill body above.*
