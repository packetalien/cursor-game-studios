---
name: perf-profile
description: "Structured performance profiling workflow. Identifies bottlenecks, measures against budgets, and generates optimization recommendations with priority rankings."
argument-hint: "[system-name or 'full']"
user-invocable: true
agent: performance-analyst
allowed-tools: Read, Glob, Grep, Bash
---

## Phase 1: Determine Scope

Read the argument:

- System name → focus profiling on that specific system
- `full` → run a comprehensive profile across all systems

---

## Phase 2: Load Performance Budgets

Check for existing performance targets in design docs or CLAUDE.md:

- Target FPS (e.g., 60fps = 16.67ms frame budget)
- Memory budget (total and per-system)
- Load time targets
- Draw call budgets
- Network bandwidth limits (if multiplayer)

---

## Phase 3: Analyze Codebase

**CPU Profiling Targets:**
- `_process()` / `Update()` / `Tick()` functions — list all and estimate cost
- Nested loops over large collections
- String operations in hot paths
- Allocation patterns in per-frame code
- Unoptimized search/sort over game entities
- Expensive physics queries (raycasts, overlaps) every frame

**Memory Profiling Targets:**
- Large data structures and their growth patterns
- Texture/asset memory footprint estimates
- Object pool vs instantiate/destroy patterns
- Leaked references (objects that should be freed but aren't)
- Cache sizes and eviction policies

**Rendering Targets (if applicable):**
- Draw call estimates
- Overdraw from overlapping transparent objects
- Shader complexity
- Unoptimized particle systems
- Missing LODs or occlusion culling

**I/O Targets:**
- Save/load performance
- Asset loading patterns (sync vs async)
- Network message frequency and size

---

## Phase 4: Generate Profiling Report

```markdown
## Performance Profile: [System or Full]
Generated: [Date]

### Performance Budgets
| Metric | Budget | Estimated Current | Status |
|--------|--------|-------------------|--------|
| Frame time | [16.67ms] | [estimate] | [OK/WARNING/OVER] |
| Memory | [target] | [estimate] | [OK/WARNING/OVER] |
| Load time | [target] | [estimate] | [OK/WARNING/OVER] |
| Draw calls | [target] | [estimate] | [OK/WARNING/OVER] |

### Hotspots Identified
| # | Location | Issue | Estimated Impact | Fix Effort |
|---|----------|-------|------------------|------------|

### Optimization Recommendations (Priority Order)
1. **[Title]** — [Description]
   - Location: [file:line]
   - Expected gain: [estimate]
   - Risk: [Low/Med/High]
   - Approach: [How to implement]

### Quick Wins (< 1 hour each)
- [Simple optimization 1]

### Requires Investigation
- [Area that needs actual runtime profiling to confirm impact]
```

Output the report with a summary: top 3 hotspots, estimated headroom vs budget, and recommended next action.

---

## Phase 5: Scope and Timeline Decision

Activate this phase only if any hotspot has Fix Effort rated M or L.

Present significant-effort items and ask the user to choose for each:

- **A) Implement the optimization** (proceed with fix now or schedule it)
- **B) Reduce feature scope** (run `/scope-check [feature]` to analyze trade-offs)
- **C) Accept the performance hit and defer to Polish phase** (log as known issue)
- **D) Escalate to technical-director for an architectural decision** (run `/architecture-decision`)

If multiple items are deferred to Polish (choice C), record them under `### Deferred to Polish`.

This skill is read-only — no files are written. Verdict: **COMPLETE** — performance profile generated.

---

## Phase 6: Next Steps

- If bottlenecks require architectural change: run `/architecture-decision`.
- If scope reduction is needed: run `/scope-check [feature]`.
- To schedule optimizations: run `/sprint-plan update`.

### Rules
- Never optimize without measuring first — gut feelings about performance are unreliable
- Recommendations must include estimated impact — "make it faster" is not actionable
- Profile on target hardware, not just development machines
- Static analysis (this skill) identifies candidates; runtime profiling confirms

<!-- PHASE2_DEEPENING_BEGIN -->
## Phase 2 — Skill deepening (Cursor Game Studios)

### Rich procedural spine (`perf-profile`)

Treat this skill as a **flight checklist**, not a vibe. Each invocation should
end with: **inputs read → actions taken → artifacts produced → risks noted**.

### Spawn template (copy/paste starter)

```text
You are executing the Cursor Game Studios skill `perf-profile`.

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
