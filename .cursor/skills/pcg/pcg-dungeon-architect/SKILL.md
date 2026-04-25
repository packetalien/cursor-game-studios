---
name: pcg-dungeon-architect
description: "Modular dungeons via PCG + connectivity proofs: rooms, corridors, and boss arenas that do not gaslight the navmesh."
user-invocable: true
allowed-tools: Read, Glob, Grep, Write, Bash, Task
---

# PCG Dungeon Architect

You turn **grid grammar** into playable space — not a topology haunted house.

## Preconditions

- Module set cataloged (mesh bounds, connector tags).
- Spawn and exit volumes placed by level design.

## Procedure

1. **Graph skeleton:** room sizes → corridor solver → cap variance.
2. **Connectivity proof:** BFS from player spawn; unreachable volume = failure.
3. **Combat pockets:** minimum arena metrics; ceiling height for abilities.
4. **Bake path:** optional static export for shipping slice.

## Outputs

- Connectivity report (pass/fail + counterexample cell coords).
- Module use histogram (detect over-love for one prefab).

## Pairing

- `systems-designer` — encounter pacing hooks.
- `qa-tester` — navmesh coverage sampling.

## Anti-patterns

- Secret one-way doors the designer **did not ask for**.
- PCG that rerolls layout while QA is mid-flight — **rude**.

<!-- PHASE2_DEEPENING_BEGIN -->
## Phase 2 — Skill deepening (Cursor Game Studios)

### Rich procedural spine (`pcg-dungeon-architect`)

Treat this skill as a **flight checklist**, not a vibe. Each invocation should
end with: **inputs read → actions taken → artifacts produced → risks noted**.

### Spawn template (copy/paste starter)

```text
You are executing the Cursor Game Studios skill `pcg-dungeon-architect`.

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
