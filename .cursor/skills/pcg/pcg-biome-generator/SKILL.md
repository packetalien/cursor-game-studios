---
name: pcg-biome-generator
description: "Procedural biomes in Unreal 5.5+: species masks, sustainability budgets, and PCG graphs that survive perf review."
user-invocable: true
allowed-tools: Read, Glob, Grep, Write, Bash, Task
---

# PCG Biome Generator

You design **living scatter** that respects slope, soil fiction, and GPU reality.

## Preconditions

- World Partition cell policy named (tier + size).
- Instance budget per cell documented in ADR or `asset-spec`.

## Procedure

1. **Masks:** height/slope/wetness inputs declared; no mystery weights.
2. **Species layers:** separate graphs or subgraphs per layer; merge with explicit ordering.
3. **Sustainability:** regeneration cost measured; cap regen frequency for in-editor work.
4. **Handoff:** export graph snapshot path; link `pcg-asset-generation-pipeline`.

## Outputs

- PCG graph change list with seed table appendix.
- Risk notes: overlap classes, nav holes, wind animation cost.

## Pairing

- `unreal-specialist` — engine limits.
- `technical-artist` — look vs instance density.
- `level-designer` — encounter readability through foliage.

## Anti-patterns

- One megagraph that **eats souls** and merge conflicts.
- “Random is fine” when QA needs **repro**.

<!-- PHASE2_DEEPENING_BEGIN -->
## Phase 2 — Skill deepening (Cursor Game Studios)

### Rich procedural spine (`pcg-biome-generator`)

Treat this skill as a **flight checklist**, not a vibe. Each invocation should
end with: **inputs read → actions taken → artifacts produced → risks noted**.

### Spawn template (copy/paste starter)

```text
You are executing the Cursor Game Studios skill `pcg-biome-generator`.

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
