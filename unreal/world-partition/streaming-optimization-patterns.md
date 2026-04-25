# Streaming optimization patterns

> **Work in progress.**

## Patterns

| Pattern | Description |
|---------|-------------|
| Predictive preload | Trigger loads ahead of player vector |
| HLOD stairway | coarse → fine as distance drops |
| Async physics wake | delay Chaos until cell stable |

## Metrics

| Metric | Healthy |
|--------|---------|
| Streaming in-flight | bounded queue |
| Time blocked on load | < frame budget spike policy |

## Debug ritual

1. `stat streaming` (or project equivalent).  
2. Visualize streaming sources.  
3. Correlate hitches with cell boundaries — **the guilt is usually spatial**.
