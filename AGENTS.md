# Cursor Game Studios — agent architecture

> **Work in progress — use at your own risk.** Verify collaboration rules against
> your team’s policies before relying on them for production decisions.

**Cursor Game Studios** is a **Cursor-native structural port** of
[Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios)
(MIT, Donchitos). This file orients humans and Cursor agents.

Indie and mid-scale game development coordinated through **49** specialized
subagent definitions under `.cursor/agents/`.

## Technology stack

- **Engine**: [CHOOSE: Godot 4 / Unity / Unreal Engine 5.5+]
- **Language**: [CHOOSE: GDScript / C# / C++ / Blueprint]
- **Version control**: Git
- **Build system**: [SPECIFY after choosing engine]
- **Asset pipeline**: [SPECIFY after choosing engine]

## Project structure

See `.cursor/docs/directory-structure.md`.

## Engine version reference

See `docs/engine-reference/README.md`.

## Technical preferences

See `.cursor/docs/technical-preferences.md`.

## Coordination rules

See `.cursor/docs/coordination-rules.md`.

## Collaboration protocol

**User-driven collaboration, not autonomous execution.**  
Flow: **Question → Options → Decision → Draft → Approval**

See `docs/COLLABORATIVE-DESIGN-PRINCIPLE.md`.

## First session

Use **`.cursor/skills/start/SKILL.md`** for guided onboarding.

## Coding standards

See `.cursor/docs/coding-standards.md`.

## Context management

See `.cursor/docs/context-management.md`.

## Cursor integration

- **Subagents**: `.cursor/agents/{directors,leads,specialists}/`
- **Skills**: `.cursor/skills/<skill-id>/SKILL.md`
- **Rules**: `.cursor/rules/*.mdc`
- **MCP** (optional): attach editor, tracker, or CI servers deliberately; avoid
  over-wiring every tool into every subagent.
