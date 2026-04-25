# PCG agent specialists

> **Work in progress.** Specialist **skills** extend base agents.

## Specialist roster

| Specialist | Skill id | Focus |
|------------|----------|-------|
| Biome Generator | `pcg-biome-generator` | species masks, sustainability |
| Dungeon Architect | `pcg-dungeon-architect` | modular connectivity |
| City Builder | `pcg-city-builder` | blockout, HLOD-aware massing |

## Base agent pairing

| Base | Why |
|------|-----|
| `unreal-specialist` | graph ownership, engine limits |
| `technical-artist` | lookdev + performance trade-offs |
| `level-designer` | playability, encounter flow |

## Handoff protocol

1. Level designer defines **play volumes** and choke points.  
2. PCG specialist proposes graph.  
3. TA signs performance budget.  
4. QA runs `pcg-asset-generation-pipeline` sample.
