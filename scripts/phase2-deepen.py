#!/usr/bin/env python3
"""
Phase 2 — append structured deepening blocks to all agents and skills.

Idempotent: skips files that already contain PHASE2_DEEPENING_BEGIN.

Usage:
  python scripts/phase2-deepen.py
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKER = "<!-- PHASE2_DEEPENING_BEGIN -->"


def _parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---"):
        return {}, text
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        return {}, text
    fm_lines = m.group(1).splitlines()
    body = text[m.end() :]
    meta: dict[str, str] = {}
    for line in fm_lines:
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        meta[k.strip()] = v.strip().strip('"')
    return meta, body


def _skill_category(skill_id: str) -> str:
    s = skill_id.lower()
    if s in {"start", "help", "adopt", "onboard", "setup-engine", "project-stage-detect"}:
        return "onboarding"
    if s.startswith("team-"):
        return "orchestration"
    if s.startswith("qa-") or s in {"smoke-check", "soak-test", "regression-suite", "test-setup", "test-helpers", "test-flakiness", "test-evidence-review", "skill-test", "skill-improve"}:
        return "quality"
    if s in {
        "release-checklist",
        "launch-checklist",
        "changelog",
        "patch-notes",
        "hotfix",
        "day-one-patch",
    }:
        return "release"
    if s.startswith("design") or s in {
        "brainstorm",
        "map-systems",
        "quick-design",
        "art-bible",
        "asset-spec",
        "asset-audit",
        "ux-design",
        "ux-review",
        "review-all-gdds",
        "propagate-design-change",
    }:
        return "design"
    if s.startswith("architecture") or s in {
        "create-architecture",
        "create-control-manifest",
        "dev-story",
        "code-review",
        "tech-debt",
        "security-audit",
        "perf-profile",
    }:
        return "engineering"
    if s in {
        "create-epics",
        "create-stories",
        "sprint-plan",
        "sprint-status",
        "story-readiness",
        "story-done",
        "estimate",
        "milestone-review",
        "retrospective",
        "gate-check",
        "scope-check",
    }:
        return "production"
    if s in {
        "bug-report",
        "bug-triage",
        "balance-check",
        "content-audit",
        "consistency-check",
        "playtest-report",
        "reverse-document",
    }:
        return "analysis"
    if s in {"localize", "prototype"}:
        return "content"
    return "studio-wide"


def _agent_human_title(stem: str) -> str:
    return stem.replace("-", " ").title()


def deepen_agent(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if MARKER in text:
        return False
    meta, body = _parse_frontmatter(text)
    name = meta.get("name", path.stem)
    title = _agent_human_title(path.stem)
    block = f"""

{MARKER}
## Phase 2 — Agent deepening (Cursor Game Studios)

### Mission amplification (`{name}`)

You own **{title}** as a first-class studio role—not a costume. Your mission is to
compress weeks of avoidable thrash into **decisions with receipts**: explicit
assumptions, explicit trade-offs, and explicit next actions.

### Core responsibilities (Phase 2+)

- Translate vague intent into **checkable** outcomes (artifacts, tests, or
  reviewable diffs).
- Keep your domain **bounded**: consult laterally, escalate vertically, never
  silently annex another lead’s charter.
- Prefer **small batch** changes that can be reviewed without a archaeology team.

### MCP orchestration stance (optional tooling)

Use MCP **only** when it reduces risk or time-to-verify—not when it increases
ambient magic. Typical patterns:

| MCP class | When it helps | When it hurts |
|-----------|---------------|----------------|
| **Editor / engine** | Deterministic repro, measured iteration | Parallel mutating calls, “mystery compile” races |
| **VCS / review** | Traceability, blame, diff discipline | Drive-by comments without owners |
| **CI / build** | Objective pass/fail gates | Flaky checks that train everyone to ignore red |

Default posture: **filesystem + terminal + diffs** are truth; MCP is an
accelerator you must be able to **disable** and still ship.

### Collaboration patterns

- **Directors → Leads:** mandate outcomes + constraints; never micromanage method
  unless risk is existential.
- **Leads → Specialists:** split work into **independently verifiable** slices.
- **Specialists → Leads:** return **done** or **blocked** with evidence; no
  “almost done” as a personality trait.

### Anti-patterns and failure modes

- **Hero ball:** one agent tries to own architecture, implementation, QA, and
  narrative tone in a single breath.
- **Ghost handoffs:** “someone should…” without a named owner and deadline.
- **Tool worship:** MCP calls that replace thinking; you should still be able to
  explain *why* a change is safe.

### Phase 2+ evolution hooks

- Tighten **Definition of Done** per milestone (what evidence closes a task).
- Add **engine-specific** checklists (UE5.5+ when applicable) without hard-wiring
  secrets or vendor lock-in prose.
- Increase **parallelism** only where artifacts do not contend (research vs
  single-writer mutation queues).

---
*Deepening appended by `scripts/phase2-deepen.py` — preserves upstream body above.*
"""
    path.write_text(text.rstrip() + block, encoding="utf-8")
    return True


def deepen_skill(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if MARKER in text:
        return False
    meta, _body = _parse_frontmatter(text)
    name = meta.get("name", path.parent.name)
    sid = path.parent.name
    block = f"""

{MARKER}
## Phase 2 — Skill deepening (Cursor Game Studios)

### Rich procedural spine (`{name}`)

Treat this skill as a **flight checklist**, not a vibe. Each invocation should
end with: **inputs read → actions taken → artifacts produced → risks noted**.

### Spawn template (copy/paste starter)

```text
You are executing the Cursor Game Studios skill `{sid}`.

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
"""
    path.write_text(text.rstrip() + block, encoding="utf-8")
    return True


def write_skill_reference_tree() -> tuple[int, int]:
    """Create skills/<category>/<id>.md companion pages."""
    base = ROOT / "skills"
    if base.exists():
        for p in base.rglob("*.md"):
            p.unlink()
        for d in sorted([x for x in base.iterdir() if x.is_dir()], reverse=True):
            try:
                d.rmdir()
            except OSError:
                pass
    count = 0
    cats: set[str] = set()
    skills_root = ROOT / ".cursor" / "skills"
    for skill_md in sorted(skills_root.glob("*/SKILL.md")):
        sid = skill_md.parent.name
        cat = _skill_category(sid)
        cats.add(cat)
        dest_dir = base / cat
        dest_dir.mkdir(parents=True, exist_ok=True)
        rel_skill = f"../../.cursor/skills/{sid}/SKILL.md"
        content = f"""# Skill reference — `{sid}`

> **Category:** `{cat}`  
> **Canonical playbook:** [{rel_skill}]({rel_skill})

This file is a **Phase 2 companion**: stable navigation, category browsing, and
space for future long-form exemplars without destabilizing the canonical
`SKILL.md`.

## Quick orientation

- Start from the canonical `SKILL.md` for procedural truth.
- Use this page when you want **repo navigation** and **studio-wide** context.

## Suggested pairing

Pair with the **Agent–Skill Affinity Matrix** in `docs/agent-skill-affinity-matrix.md`.

## Work in progress

Exemplars and engine-specific expansions may land here in later phases.
"""
        (dest_dir / f"{sid}.md").write_text(content, encoding="utf-8")
        count += 1
    index = base / "index.md"
    lines = [
        "# Cursor Game Studios — `skills/` reference tree",
        "",
        "> **Work in progress.** Canonical procedures live under `.cursor/skills/`.",
        "",
        "## Categories",
        "",
    ]
    for c in sorted(cats):
        lines.append(f"- [`{c}/`]({c}/)")
    lines += ["", "## All skills", ""]
    for skill_md in sorted(skills_root.glob("*/SKILL.md")):
        sid = skill_md.parent.name
        cat = _skill_category(sid)
        lines.append(f"- [`{cat}/{sid}.md`]({cat}/{sid}.md)")
    index.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return count, len(cats)


def main() -> None:
    agents = sorted((ROOT / ".cursor" / "agents").rglob("*.md"))
    skills = sorted((ROOT / ".cursor" / "skills").glob("*/SKILL.md"))
    ac = sum(1 for p in agents if deepen_agent(p))
    sc = sum(1 for p in skills if deepen_skill(p))
    ref_n, ref_cats = write_skill_reference_tree()
    print(f"agents_updated={ac}/{len(agents)} skills_updated={sc}/{len(skills)}")
    print(f"skills_reference_pages={ref_n} categories={ref_cats}")


if __name__ == "__main__":
    main()
