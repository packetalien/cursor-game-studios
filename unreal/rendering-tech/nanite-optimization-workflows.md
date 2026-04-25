# Nanite optimization workflows

> **Work in progress.** Nanite forgives geometry — **not** your architecture.

## Checklist

| Step | Action |
|------|--------|
| N-01 | Confirm mesh is Nanite-eligible |
| N-02 | Material complexity audit |
| N-03 | Overdraw hotspots via visualization |
| N-04 | Fallback path for non-Nanite platforms |

## Trade-offs

| More quality | Cost |
|--------------|------|
| Dense foliage | shading + visibility |
| Micro-detail | memory |

## Pipeline

Run `pipelines/nanite-optimization-pipeline.md` on milestone builds.

## Graveyard humor

If your triangle count is a phone number, **Nanite will still stream it** — your **frame budget** will not.
