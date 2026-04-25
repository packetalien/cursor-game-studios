# SECURITY

> **Work in progress.** This document describes expectations for reporting issues
> in a **prompt-and-rules repository**, not a hosted service.

## Reporting a vulnerability

If you believe you have found a **security vulnerability** (for example:
prompt-injection patterns that encourage unsafe commands, or documentation that
pushes users toward secret leakage), please report it responsibly:

- Prefer **private** disclosure to maintainers (GitHub Security Advisories or a
  direct maintainer contact, if available).
- Include reproduction steps, impact, and suggested mitigation.

## Scope and limitations

This repository ships **markdown, YAML, and optional scripts**. It does not
run a networked service. Standard **indemnification**: maintainers are not
insurers of your production environment; you remain responsible for builds,
releases, secrets, and multiplayer security.

## Dependency notes

Optional dev dependency: `pytest`. Pin versions under your own supply-chain
policy if required.

## Optional Unreal metrics (`StudioUnrealMetrics.json`)

If your **game repository** emits performance snapshots for local automation,
treat that JSON as **sensitive-ish operational data**: it can reveal project
structure and timing. Do **not** place secrets, tokens, or player identifiers in
metrics files; keep them build-local or redacted in CI artifacts.

## Audit history

| Date | Summary |
|------|---------|
| 2026-04-14 | Initial SECURITY.md for Phase 1 |
| 2026-04-14 | Phase 4 — documented optional Unreal metrics hygiene |
