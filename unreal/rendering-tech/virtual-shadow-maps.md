# Virtual Shadow Maps (VSM)

> **Work in progress.** Shadows at scale: **generous until they are not**.

## When VSM shines

- Large open worlds with dynamic sun.
- Dense Nanite scenes with coherent shadow direction.

## Watchouts

| Issue | Mitigation |
|-------|------------|
| Cache pressure | cache size policy per platform |
| Nanite interaction | verify cascades vs VSM choice |

## Handoff

TA owns shadow policy; `performance-analyst` validates worst-case passes.
