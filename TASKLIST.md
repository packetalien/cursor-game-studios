# TASKLIST — Cursor Game Studios

> **Work in progress.** This list is the **action layer** for `ROADMAP.md`: what
> humans and agents do **next**, with receipts. Tone: brass, ozone, and the
> quiet knowledge that **five percent** of runs exist purely to humble you.

---

## Done (through Phase 4 — shipped)

- [x] **Phase 1 — Foundation:** generator + `.cursor/` tree + docs + tests + GitHub push (2026-04-14).
- [x] **Phase 2 — Agent & skill deepening:** `phase2-deepen.py`, `skills/` companion tree, doctrine + orchestration + affinity matrix + chapter `02` (2026-04-14).
- [x] **Phase 3 — Skill forge + automation:** `03-phase-03-…`, `docs/advanced-orchestration.md`, nine baseline pipelines + `pipelines/index.md`, `studio-health-check.py`, `pipeline-runner.py`, `studio-metrics.py`, `nightly-studio-audit.py`, `tests/test_phase3_pipelines.py`, metadata (2026-04-14).
- [x] **Phase 4 — Unreal native lane:** `04-phase-04-…`, full `unreal/` tree, five Unreal-heavy pipelines, three `.cursor/skills/pcg/*` skills, `unreal-mcp-health.py`, health check extensions, metrics include `unreal/` (2026-04-14).

---

## Now (Phase 5 — expression layer: `.mdc` × MCP × skills)

> **Schwartz Mode centerpiece:** tighten the **twelve `.mdc` hearts** so globs are
> blast doors—not shotguns. No “bash hook necromancy” as a substitute for scope.

- [ ] **G1 — Engine glob adoption pack (game repo)** — **Owner:** `technical-director` + `engine-programmer`. **MCP gate:** Editor MCP **read-only** directory map of `Source/` + `Plugins/`. **Deliverable:** revised `engine-code.mdc` globs *in a branch* that match **your** UE tree (not fantasy paths). **Test:** `python scripts/studio-health-check.py --require-phase2-mark`. **Backfire (5%):** greedy glob matches generated files → compile storm cosplay.

- [ ] **G2 — UI / shader / network hot-lane review** — **Owner:** `lead-programmer` + `technical-artist`. **MCP gate:** single-writer policy written for UMG/material mutations. **Deliverable:** short ADR in game repo linking `ui-code.mdc` + `shader-code.mdc` + `network-code.mdc` to actual folders. **Test:** `python -m pytest -q`. **Backfire:** parallel MCP applies → widget civil war.

- [ ] **G3 — MCP manifest (consumer repo)** — **Owner:** `tools-programmer`. **MCP gate:** manifest exists with **timeouts + allowlists** (Unreal editor bridge, geospatial tools, SSH, HTTP—pick what you actually run). **Note:** this kit has **no** `mcp.json`; wire MCP in **your** game repo / Cursor project. **Test:** human checklist + `unreal/unreal-mcp-integration.md` cross-links updated in the same PR.

- [ ] **G4 — Integrity + contamination CI** — **Owner:** `security-engineer` + `release-manager`. **MCP gate:** none required; CI runs text scan patterns. **Deliverable:** optional `--strict` nightly in CI. **Test:** `python scripts/nightly-studio-audit.py` locally; CI mirrors policy. **Backfire:** someone “helpfully” pastes forbidden codenames from other products—tests **should** fail.

- [ ] **G5 — Data schema ↔ `data-files.mdc` alignment** — **Owner:** `systems-designer` + `tools-programmer`. **MCP gate:** JSON validation in game CI. **Deliverable:** schema version bump policy for any table-driving JSON. **Test:** game-repo validator + `pytest` here stays green. **Backfire:** silent key rename becomes apology tour.

- [ ] **G6 — Serialization law promotion** — **Owner:** `technical-director`. **MCP gate:** “one writer” table for Blueprint / PCG / UMG targets. **Deliverable:** section in `docs/advanced-orchestration.md` or game ADR; link from `unreal/unreal-mcp-integration.md`. **Test:** review checklist in PR template. **Backfire:** two Tier-3 specialists arm-wrestle the same asset.

- [ ] **G7 — Registry items filed as JSON** — **Owner:** `producer`. **MCP gate:** none. **Deliverable:** at least three `cgs_roadmap_item_v1` objects live in game-repo `docs/` or `assets/data/` **without secrets**. **Test:** human eye + JSON parse. **Backfire:** registry becomes fiction—dates slip, nobody laughs.

---

## Next (Phase 6+ — prioritized backlog, same flavor)

- [ ] **Phase 6 — Geospatial round-trip:** camera flight receipt + SQL/tile query fingerprint + archived logs (**Schwartz note:** if the query lies, the mesh lies louder).
- [ ] **Phase 6 — Unreal MCP hardening:** typed tools, mutex enforcement, crash-log tail tool wiring (timeouts are love).
- [ ] **Phase 7 — Data → engine tables:** import pipeline with CI diff + schema versioning (romantic, until it breaks).
- [ ] **Phase 8 — Live-fire UE slice:** Tier-1 director outcomes + Tier-3 specialist execution with evidence bundle (hero ball is banned).
- [ ] **Phase 9 — Serialized `team-ui` swarm:** one writer per branch; everyone else reviews (merge tool picks worst timeline if you cheat).
- [ ] **Phase 10 — Public 1.0:** semver, disclaimers, studio voice appendix (honest marketing survives contact with players).

---

## Schwartz Mode — centerpiece tasks (do not skip)

| If you skip… | The necropolis sends… |
|----------------|------------------------|
| G1 engine globs | A “helpful” rule that torches `Intermediate/` |
| G3 MCP timeouts | A job that runs until heat death of universe |
| G6 serialization | Two agents proving merge conflicts are a personality |

---

## Quick commands (brass weights)

```bash
python scripts/studio-health-check.py --require-phase2-mark
python scripts/nightly-studio-audit.py
python -m pytest -q
python -m unittest discover -s tests -t tests -p "test_*.py" -v
python scripts/run-unittest.py
```

---

## Clean next pointer

**Next:** pick **G1** or **G3** first—without a manifest and without honest globs,
every later phase is just **expensive fan fiction**.
