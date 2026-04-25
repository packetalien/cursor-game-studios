# Large-world debugging

> **Work in progress.** When the world is **too large to apologize to**.

## Symptom → suspect

| Symptom | First suspect |
|---------|---------------|
| Stutter on boundary | streaming/HLOD |
| Memory climb | leaked references / duplicate actors |
| Editor crawl | too many loaded cells |

## Minimal repro

- Duplicate **one offending cell** to empty test map.
- Bisect actor layers until hitch vanishes.

## Documentation

- Log repro steps in `STATUS.md` dated entry or issue tracker.

## Human sanity

Sleep. The landscape will still be broken in the morning — **but you will be less broken**.
