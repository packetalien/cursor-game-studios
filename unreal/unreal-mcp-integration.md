# Unreal MCP integration — editor, Blueprints, C++

> **Work in progress.** Model Context Protocol bridges Cursor agents to **live**
> Unreal Editor sessions. This document is **policy + protocol**; your MCP server
> implementation lives in the game repo.

## What MCP can own (safely)

| Surface | Typical tools | Risk |
|---------|---------------|------|
| Asset queries | list actors, metadata | Low |
| Blueprint read | graph export, compile status | Medium |
| Blueprint write | node spawn, wire pins | **High** (serialize) |
| C++ project | read files, suggest edits in Cursor | Low in kit repo |
| Console | `stat *`, scoped commands | Medium |

## Serialization law

**One writer** per mutable target: one Blueprint, one PCG graph, one sublevel at
a time. Parallel agents may **read** and **plan**; mutations queue.

## Blueprint vs C++ split

| Concern | Default owner |
|---------|----------------|
| Hot loops, replication authority | C++ (`gameplay-programmer`, `network-programmer`) |
| Designer iteration, UI flow | Blueprint (`ue-blueprint-specialist`, `ui-programmer`) |
| PCG graphs | `unreal-specialist` + PCG skills |

## Console command discipline

- Prefer **read-only** `stat` passes for diagnostics.
- Destructive commands require **human EP** approval in session notes.

## Live iteration loop

1. Agent proposes change with file/graph path.  
2. Human approves.  
3. MCP applies mutation.  
4. Editor compile / cook step captures log tail.  
5. Agent attaches log excerpt to story or ADR.

## Failure recovery

| Symptom | Action |
|---------|--------|
| MCP timeout | Shrink batch; retry once |
| Compile storm | Stop parallel MCP; single-writer |
| Desync | Close editor, regenerate project files, reopen |

## Phase 5+ hooks

- Typed tool schemas per command family.
- Automatic capture of `Saved/Logs` tail to CI artifact.
