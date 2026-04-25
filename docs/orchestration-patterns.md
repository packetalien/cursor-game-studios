# Orchestration patterns — Cursor Game Studios

> **Work in progress.** Patterns for handoffs between agents and skills in Cursor.

## Pattern A — Director gate

```text
Creative or Technical Director → decision record → Lead executes → Specialists implement
```

**Use when:** vision, architecture, or cross-department conflict.

**Artifacts:** short written decision; link into story or ADR.

## Pattern B — Lead fan-out

```text
Lead (design/engine/art/QA) → splits epic → spawns parallel specialist tasks → merges with checklist
```

**Use when:** work decomposes cleanly without shared mutable state.

## Pattern C — Single-writer engine loop

```text
Research (parallel OK) → single implementer applies MCP/editor mutations → compile/test → handoff
```

**Use when:** Unreal editor automation or any MCP that mutates live state.

## Pattern D — Skill chain

| Stage | Skill (canonical id) |
|-------|----------------------|
| Ready | `story-readiness` |
| Build | `dev-story` |
| Review | `code-review` |
| Close | `story-done` |

Chains are **documentation contracts**: if you skip a stage, say so explicitly.

## Pattern E — Team swarm (controlled)

Team skills (`team-ui`, `team-combat`, etc.) assume **role-separated outputs**
merged by a lead. Do not let two specialists edit the same file without sequence.

## Anti-patterns

| Anti-pattern | Why it fails |
|--------------|--------------|
| “Everyone edit `GameMode`” | Merge conflicts and blame storms |
| “Ask the model to just know” | Context rot; write it down |
| “Infinite subagents” | Tool saturation and flaky IO |
