# Live Link & bidirectional patterns

> **Work in progress.** “Live Link” here means **continuous feedback** between a
> running Unreal instance and Cursor—not only the LiveLink animation plugin.

## Pattern L1 — Log tail subscription

**Flow:** Editor writes `Saved/Logs` → tailer MCP tool → agent summarizes.  
**Use:** overnight soak, smoke repro.

## Pattern L2 — Structured heartbeat JSON

**Flow:** lightweight game module writes `Saved/StudioHeartbeat.json` (fps,
streaming loads, PCG regen ms) on a timer → MCP read → `studio-metrics`-style
dashboard in CI.

## Pattern L3 — Command queue file

**Flow:** agent writes `Intermediate/StudioCommandQueue.jsonl` → game/editor
plugin consumes and ACKs → avoids direct socket chaos.

## Anti-patterns

| Bad | Good |
|-----|------|
| Polling editor 60 Hz | Event-driven or 1–5 Hz |
| Giant JSON blobs | Bounded samples + rolling window |

## Security

- Treat heartbeat files as **untrusted** if repo is shared.
- Never embed secrets in command queue.
