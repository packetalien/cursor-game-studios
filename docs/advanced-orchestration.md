# Advanced orchestration — Cursor Game Studios

> **Work in progress.** This document turns “many smart prompts” into a **coherent
> machine**: predictable handoffs, explicit authority, and rhythms that survive
> 3am builds.

## Multi-agent handoff protocol (H1)

Every handoff **must** include:

| Field | Content |
|-------|---------|
| **Owner** | Exactly one human or agent name |
| **Artifact** | Path or ticket ID |
| **Definition of Done** | Observable check |
| **Deadline** | Wall-clock or milestone |
| **Escalation** | Who receives blockers |

Without these five, you are not handing off—you are haunting the backlog.

## Supervisor / director pattern (D3)

The **three directors** (`creative-director`, `technical-director`, `producer`)
form a **triad**, not a triangle fight:

| Director | Primary veto | Consults |
|----------|----------------|------------|
| Creative | Player fantasy + tone | Technical on feasibility |
| Technical | Architecture + risk | Producer on schedule |
| Producer | Schedule + scope | Both on trade-offs |

**Leads (8)** own domains. They **do not** overrule directors; they **package**
options for directors when cross-domain conflict exists.

**Specialists (38)** execute. They **escalate** to their lead when:

- Acceptance criteria are ambiguous,
- Another specialist already owns the file,
- MCP/editor mutation would race.

## Conflict resolution and escalation

| Severity | Path | Timebox |
|----------|------|---------|
| L1 | Lead decides within domain | Same session |
| L2 | Two leads disagree | Director triad within 24h |
| L3 | Schedule vs quality existential | Producer + technical + creative joint memo |

**Rule:** If a conflict hides inside a merge request without a decision record,
the conflict wins by accident.

## Studio rhythm (the long session)

| Cadence | Mechanism |
|---------|-----------|
| **Hourly micro-sync** | Human EP checks active story + CI |
| **Daily** | Lead reviews open risks; specialists close loops |
| **Weekly** | Director gate on phase transition (`gate-check`) |
| **Per merge** | Smallest diff that preserves green |

The organism **does sleep**—automation doesn’t replace rest; it replaces **panic**.

## Orchestration examples

### Example A — Concept → GDD → prototype (high level)

1. **Creative director** frames pillars (decision memo).
2. **Game designer** runs `brainstorm` → `map-systems` → `design-system`.
3. **Producer** locks scope for prototype slice.
4. **Prototyper** + **gameplay-programmer** implement under `prototype/` rules.
5. **QA lead** runs `smoke-check` on prototype acceptance.
6. **Technical director** signs ADR if prototype informs architecture.

### Example B — Vertical slice (engineering-heavy)

1. `story-readiness` → **Lead programmer** assigns owners.
2. **Gameplay + UI** specialists implement with **single-writer** on shared maps.
3. `dev-story` closes implementation; `code-review` mandatory.
4. **Performance analyst** attaches `perf-profile` snapshot.
5. **Release manager** verifies `release-checklist` prerequisites for internal build.

### Example C — Seven-agent handoff (controlled swarm)

**Wave 1 (read-mostly):** `world-builder`, `ux-designer`, `sound-designer` produce specs.  
**Wave 2 (single writer):** `unreal-specialist` applies editor mutations sequentially.  
**Wave 3 (verify):** `qa-tester` + `performance-analyst` run `team-level` outcomes.

## Anti-patterns

| Pattern | Fix |
|---------|-----|
| “Everyone in the Blueprint” | File ownership matrix |
| Director micromanaging diffs | Directors own decisions, leads own execution |
| Infinite MCP fan-out | Tool budget per wave |

## Links

- [Production pipelines](../pipelines/index.md)
- [Orchestration patterns](orchestration-patterns.md)
- [Agent–skill affinity matrix](agent-skill-affinity-matrix.md)
