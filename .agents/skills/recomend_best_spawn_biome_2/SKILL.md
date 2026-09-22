---
name: recomend_best_spawn_biome_2
description: Determine the mathematically and practically best biome for finding and catching a Pokémon in Cobblemon using the current build's actual spawn pool, biome tags, species/evolution data, bucket probabilities, and verified spawner mechanics. Separates theoretical target-selection probability from practical hunting conditions and never invents spawn mechanics or probabilities.
---

# Skill: `recomend_best_spawn_biome_2`

## Описание
Данный навык предназначен для альтернативной модели расчёта и подбора оптимального биома для поимки покемонов.

## Скрипты
- `scripts/` — директория для пользовательских Python скриптов и вспомогательных инструментов.

## Goal

Determine where a Pokémon is best searched for in the **current Cobblemon build**.

The analysis MUST produce two separate conclusions:

1. **Mathematical Best**

   * Highest theoretical probability of selecting the target during the verified spawn-selection process.
   * Based only on confirmed spawn data and confirmed spawner mechanics.

2. **Practical Best**

   * Best real-world hunting location after considering conditions that affect successful spawning and ease of hunting.
   * Includes entity-cap pressure, terrain, visibility, spawn-position availability, despawn/clearing convenience, and navigation.
   * Must NOT be converted into an artificial numerical score unless a quantitative model is explicitly proven.

Never merge these into a single score.

---

# 1. Evidence Policy

Every important statement MUST be classified.

### `[FACT]`

Directly confirmed by the current build:

* Cobblemon/backport JAR bytecode/decompiled code.
* Current `spawn_pool_world` JSON.
* Current biome tag JSON.
* Current species/evolution JSON.
* Current Cobblemon configuration.
* Current mod configuration.

### `[CALCULATED]`

Direct mathematical result derived only from confirmed facts.

Examples:

* bucket probability;
* total matching weight;
* target share inside a bucket;
* theoretical target-selection probability.

### `[INFERENCE]`

Reasonable practical conclusion derived from confirmed facts.

Examples:

* open terrain is easier to inspect;
* a cave requires more clearing;
* a biome has more potential non-target spawns.

### `[UNKNOWN]`

The available code/data does not prove the relationship strongly enough to calculate it.

Examples:

* exact spawn-per-minute rate;
* exact mob-cap filling speed;
* exact effect of despawn timing;
* exact probability of finding a free spawn position;
* exact effect of another mod on spawning.

Never silently convert `[UNKNOWN]` into `[INFERENCE]` or `[FACT]`.

---

# 2. Source Priority

Use evidence in this order:

1. Current Cobblemon/backport JAR.
2. Current `data/cobblemon/spawn_pool_world/*.json`.
3. Current `data/cobblemon/tags/worldgen/biome/*.json`.
4. Current Cobblemon/backport configuration.
5. Current `data/cobblemon/species/*.json`.
6. Other current modpack data.
7. External documentation only when current local data is insufficient.

Do NOT silently use another Cobblemon version.

If external documentation describes another version, mark it:

`[VERSION MISMATCH]`

---

# 3. Verified Spawner Architecture

The current build uses a hierarchical selection model.

The conceptual pipeline is:

```text
Spawner Tick
    │
    ├── World Prospecting / Entity Cap
    │
    ▼
chooseBucket()
    │
    ├── Common
    ├── Uncommon
    ├── Rare
    └── Ultra-Rare
    │
    ▼
Selected Bucket
    │
    ├── All other buckets excluded
    │
    ▼
SpawnDetail / Context Filtering
    │
    ├── biome
    ├── biome tags
    ├── Y range
    ├── light
    ├── sky light
    ├── weather
    ├── moon phase
    ├── blocks
    ├── fluid
    ├── submerged
    ├── grounded
    └── other confirmed conditions
    │
    ▼
Matching Entries in Selected Bucket
    │
    ▼
Weight / Percentage Selection
    │
    ▼
Target Selected
    │
    ▼
Separate actual-spawn pipeline
```

The exact ordering MUST follow the current code if bytecode inspection establishes a different order.

Do not claim that bucket probability is affected by the number or weights of Pokémon in another bucket unless the code proves it.

---

# 4. Bucket Probability

If bucket selection uses fixed bucket weights:

```text
P(Bucket) =
    BucketWeight /
    Sum(AllBucketWeights)
```

For the currently verified configuration:

```text
Common       = 93.8%
Uncommon     = 5.0%
Rare         = 1.0%
Ultra-Rare   = 0.2%

Total        = 100.0%
```

Therefore:

```text
P(Common)     = 0.938
P(Uncommon)   = 0.050
P(Rare)       = 0.010
P(Ultra-Rare) = 0.002
```

These values are `[FACT]` only if confirmed from the current build's configuration/code.

---

# 5. Intra-Bucket Selection

After a bucket is selected, entries from other buckets do NOT participate in the denominator.

For a weight-based target:

```text
P(Target | Bucket, Context) =
    TargetWeight /
    Sum(MatchingEntryWeights in SelectedBucket)
```

Only entries satisfying the current context participate.

For example:

```text
Rare bucket:

Target = 10
Other matching Rare entries = 5 + 15

Total matching Rare weight = 30

Target share = 10 / 30
             = 33.33%
```

A Pokémon from Common does not add its weight to this denominator.

---

# 6. Theoretical Target-Selection Probability

For a weight-based target:

```text
P(Target selected) =
    P(Bucket) ×
    P(Target | Bucket, Context)
```

This means the theoretical probability that one complete execution of the verified selection model:

```text
chooseBucket()
→
context filtering
→
intra-bucket selection
```

selects the target.

It does NOT mean:

* actual probability of an entity appearing in the world;
* Pokémon per minute;
* Pokémon per spawn attempt;
* average time to encounter;
* probability of a successful spawn position.

Do not report those quantities unless the full pipeline is mathematically modeled from confirmed code.

---

# 7. Percentage-Based Entries

Some spawn entries may use `percentage` instead of `weight`.

Do NOT automatically convert:

```text
percentage → weight
```

unless the current code explicitly proves that relationship.

If the exact selection semantics of percentage entries are not established:

```text
Target Share = UNKNOWN
Target Selection Probability = UNKNOWN
```

The report MUST explain that the entry is percentage-based and that its exact interaction with bucket selection/weight selection has not been proven.

---

# 8. Context Filtering

Every spawn entry must be evaluated against its actual conditions.

At minimum inspect:

* biome;
* biome tags;
* anti-biome conditions;
* bucket;
* weight;
* percentage;
* min/max Y;
* min/max sky light;
* min/max block light;
* weather;
* moon phase;
* time;
* fluid;
* submerged;
* grounded;
* required blocks;
* forbidden blocks;
* other conditions present in the current spawn JSON.

Do not approximate a condition if the exact data is available.

---

# 9. Biome Tags

Biome tags MUST be resolved from actual tag files.

Do NOT use string heuristics such as:

```text
"if 'mountain' in biome name → mountain"
"if 'forest' in biome name → forest"
```

unless the result is explicitly marked `[INFERENCE]`.

For example:

```text
#cobblemon:is_mountain
```

must be resolved through:

```text
data/cobblemon/tags/worldgen/biome/
```

and the Minecraft/modded biome tag structure.

The Python analyzer should resolve:

```text
direct biome IDs
+
biome tags
+
nested tag references
+
optional/required tag semantics
```

according to the actual data format.

---

## 9.1 Real Biome Registry & Phantom Mod Filtering

`[FACT]` The modpack **Society Sunlit Cobblemon** contains **ONLY** the following worldgen biomes:
1. **Vanilla Minecraft 1.20.1 biomes** (`minecraft:*`).
2. **Installed Mod Biomes:**
   * **Atmospheric:** `aspen_parkland`, `dunes`, `flourishing_dunes`, `petrified_dunes`, `rocky_dunes`, `grimwoods`, `hot_springs`, `kousa_jungle`, `laurel_forest`, `rainforest`, `rainforest_basin`, `sparse_rainforest`, `sparse_rainforest_basin`, `scrubland`, `snowy_scrubland`, `spiny_thicket`.
   * **Autumnity:** `maple_forest`, `pumpkin_fields`.
   * **Windswept:** `chestnut_forest`, `snowy_chestnut_forest`, `flowering_savanna`, `lavender_fields`, `lavender_hills`, `pine_barrens`, `snowy_pine_barrens`, `tundra`.
   * **Quark:** `glimmering_weald`.

`[PROHIBITION]`
**Never recommend biomes from missing mods:**
* `terralith:*` (Terralith is NOT installed).
* `biomesoplenty:*` (Biomes O' Plenty is NOT installed).
* `wythers:*` (Wythers is NOT installed).

Cobblemon tags include these mods as optional references (`required: false`). Any resolved tag MUST be filtered against the verified installed biomes list before producing tables or recommendations.

---


# 10. Evolution Line Analysis

Analyze the complete evolution line.

For every relevant stage determine separately:

```text
Direct Wild Spawn [FACT]
Acquisition Route [FACT]
Spawn Bucket [FACT]
Spawn Weight / Percentage [FACT]
Spawn Conditions [FACT]
```

The evolution chain itself is factual.

Example:

```text
Gible → Gabite → Garchomp
```

is:

```text
[FACT] Evolution Route
```

But:

```text
Recommended Acquisition Stage: Gible
```

is:

```text
[CALCULATED]
```

and requires an actual comparison.

Do NOT assume:

* final evolutions rarely spawn;
* first stages are always better;
* evolution is always preferable to direct spawning;
* direct spawning is always preferable to evolution.

The current spawn data decides this.

---

# 11. Direct Wild Spawn vs Acquisition Route

For the requested target, determine:

### Direct Wild Spawn

Can the requested Pokémon itself spawn in the wild?

```text
YES [FACT]
NO [FACT]
UNKNOWN [UNKNOWN]
```

### Acquisition Route

If relevant:

```text
Previous Stage
    ↓
Next Stage
    ↓
Target
```

Then compare the available routes.

The final report may state:

```text
Direct Wild Spawn: AVAILABLE
Recommended Acquisition Stage: ...
```

or:

```text
Direct Wild Spawn: NOT AVAILABLE
Recommended Acquisition Stage: ...
```

The recommendation must be based on actual data.

---

# 12. Common Pool Pressure

Common Pool Pressure is a **practical diagnostic**, not a mathematical penalty.

The analyzer may report:

```text
Common Matching Entries
Common Weight Sum
Qualitative Common Pressure
```

But:

```text
W_Common =
    Sum(Matching Common Weights)
```

MUST NOT be inserted into:

```text
P(Target selected)
```

as a penalty coefficient.

Do not calculate:

```text
TargetProbability × CommonPressure
```

or similar artificial formulas.

---

## 12.1 Why Common Pressure Matters

If the actual spawner performs an entity-cap check, nearby Pokémon can occupy the available cap.

Therefore Common Pokémon can affect practical hunting conditions indirectly.

The causal chain is:

```text
Common spawns
    ↓
Entities occupy cap
    ↓
Entity-cap check may reject future spawning
    ↓
Fewer successful spawn opportunities
```

This is a practical mechanism.

It does NOT mean:

```text
Common weight reduces Rare bucket probability
```

The two concepts must remain separate.

---

## 12.2 Pressure Classification

Use only:

```text
Low
Medium
High
Unknown
```

Optionally explain the reason.

Examples:

```text
High — many matching Common entries + difficult terrain clearing
Medium — several Common entries but manageable terrain
Low — few matching Common entries and easy clearing
Unknown — insufficient evidence
```

Do NOT automatically classify:

```text
Cave = High
Mountain = Low
Plains = Low
Forest = Medium
```

The classification must be based on actual current data and observable practical conditions.

---

# 13. Entity Cap

If the current code confirms an entity-cap check:

```text
Nearby Pokemon count >= maxAllowed
→ spawning attempt is blocked
```

report this as `[FACT]`.

Do not calculate:

```text
cap filling speed
```

unless all required variables and spawn/despawn timing are known.

Do not claim:

```text
"Biome X gives 2× more spawns"
```

without a verified quantitative model.

---

# 14. Practical Hunting Factors

The Practical Best analysis may consider:

* entity-cap pressure;
* number of matching Common entries;
* terrain openness;
* visibility;
* spawn-position availability;
* cave clearing requirements;
* water navigation;
* verticality;
* foliage;
* ability to inspect the entire area;
* ease of despawning/clearing unwanted Pokémon;
* accessibility;
* required Y level;
* required light;
* required weather/time;
* required blocks;
* whether the player can realistically maintain the required conditions.

These are separate from theoretical selection probability.

Use descriptive reasoning, not an arbitrary score.

---

# 15. Mathematical Best

Mathematical Best is determined only from calculated selection probability.

For each valid biome/context:

```text
P(Target selected)
```

must be calculated where possible.

The Mathematical Best is the biome/context with the highest verified value.

If values are equal:

```text
Tie
```

If probability cannot be calculated because the target uses unsupported percentage mechanics:

```text
Mathematical Best = UNKNOWN
```

Do not replace UNKNOWN with a practical judgment.

---

# 16. Practical Best

Practical Best is determined separately.

The analysis should consider:

```text
Mathematical opportunity
+
Common Pressure
+
Spawn-context difficulty
+
Terrain/accessibility
+
Visibility
+
Entity-cap management
```

but must not combine these into a numerical score unless such a model is explicitly requested and justified.

The report should explain *why* a biome is practically preferable.

---

# 17. Required Analyzer Output

The Python analyzer should provide machine-readable information sufficient for the Agent to reason about the result.

Recommended structure:

```text
Target
Evolution Line

Stage
Direct Wild Spawn
Acquisition Route

Biome
Context
Bucket

Bucket Probability
Matching Entry Count

Target Weight
Target Percentage

Matching Bucket Weight
Target Share
Theoretical Target Selection Probability

Common Matching Count
Common Weight Sum
Common Pressure

Hard Conditions
Practical Factors

Evidence
```

---

# 18. Required Human Report

The final response should contain:

## 1. Target and Evolution Line

```text
Target:
Evolution Line:
Direct Wild Spawn:
Acquisition Route:
```

## 2. Spawn Mechanics

Explain:

* bucket;
* bucket probability;
* target weight/percentage;
* matching competitors;
* target share;
* theoretical target-selection probability.

## 3. Biome Comparison

Use:

| Biome | Context | Bucket | Matching Entries | Target Share | P(Target selected) | Common Pressure | Practical Factors |
| ----- | ------- | ------ | ---------------: | -----------: | -----------------: | --------------- | ----------------- |

Do not rank rows by practical convenience unless clearly labeled.

## 4. Mathematical Best

State:

```text
Mathematical Best:
Reason:
```

The reason must use calculated selection probability.

## 5. Practical Best

State:

```text
Practical Best:
Reason:
```

The reason must use practical factors.

## 6. Acquisition Recommendation

If direct wild spawning is unavailable or inferior after comparison:

```text
Recommended Acquisition Stage:
```

Otherwise explicitly say that direct wild spawning remains an available route.

## 7. Hunting Instructions

Include:

* Nature's Compass query;
* biome/context;
* Y level if relevant;
* light/weather/time requirements;
* terrain recommendations;
* entity-cap management;
* despawn/clearing advice.

Never invent commands.

---

# 19. Nature's Compass

When the recommended biome is known, provide the corresponding Nature's Compass search.

Example:

```text
Nature's Compass → Search for <Biome Name>
```

If the biome is a tag-based condition rather than a single biome, explain that multiple biomes may qualify.

Do not claim a biome is valid merely because its name looks compatible with a tag.

---

# 20. Python Analyzer Contract

The analyzer:

```text
.agents/skills/recommend_spawn_biome/scripts/calculate_best_spawn_biome.py
```

must be responsible for:

1. Loading current JAR data.
2. Loading local KubeJS spawn overrides.
3. Loading species/evolution data.
4. Loading biome tag data.
5. Resolving biome tags.
6. Building the evolution line.
7. Finding direct wild spawn entries.
8. Evaluating spawn conditions.
9. Grouping matching entries by bucket.
10. Calculating bucket probability.
11. Calculating intra-bucket weight share.
12. Calculating theoretical target-selection probability.
13. Separating weight and percentage mechanics.
14. Reporting Common Pool Pressure only as a diagnostic.
15. Never inventing practical probability multipliers.

---

# 21. Important Python Rules

The script MUST NOT contain heuristic biome classification such as:

```python
if "forest" in biome_id:
```

for determining whether a spawn condition is satisfied.

It MUST resolve actual biome tags.

The script MUST NOT contain:

```python
target_probability *= common_pressure
```

or equivalent.

The script MUST NOT claim:

```text
spawn frequency
spawn per minute
time to encounter
```

unless the complete mathematical model is verified.

The script MUST NOT silently treat:

```text
percentage
```

as:

```text
weight
```

---

# 22. Unit Tests

The analyzer should contain tests for at least:

### Test 1 — Bucket Independence

If Common changes while Rare remains unchanged:

```text
P(Rare)
```

must remain unchanged.

Example:

```text
Common pool:
50 entries, total weight 500

Rare pool:
Target weight 10

versus:

Common pool:
1 entry, total weight 10

Rare pool:
Target weight 10
```

Expected:

```text
P(Rare) = 1%
```

in both cases.

---

### Test 2 — Inactive Competitor

If a Rare competitor does not satisfy the current biome/context:

```text
Rare:
Target = 10
Competitor = 5
```

then:

```text
Target Share = 10 / 15 = 66.67%
```

when both match.

If competitor is inactive:

```text
Target Share = 10 / 10 = 100%
```

---

### Test 3 — Different Buckets Do Not Enter Denominator

Example:

```text
Common:
A = 100

Rare:
Target = 10
Competitor = 10
```

Expected Rare denominator:

```text
10 + 10 = 20
```

not:

```text
100 + 10 + 10 = 120
```

---

### Test 4 — Bucket Probability

Verify:

```text
Common = 0.938
Uncommon = 0.05
Rare = 0.01
Ultra-Rare = 0.002
```

when the configured bucket weights are:

```text
93.8 / 5.0 / 1.0 / 0.2
```

---

### Test 5 — Target Selection Probability

Example:

```text
Rare bucket = 1%

Target weight = 10
Competitor weight = 10
```

Then:

```text
P(Target | Rare) = 10 / 20 = 50%

P(Target selected) =
1% × 50%
= 0.5%
```

---

### Test 6 — Percentage Is Not Weight

A percentage-based entry must not silently enter the weight denominator.

Expected result:

```text
Target Share = UNKNOWN
```

unless the current code explicitly proves its relationship to weight selection.

---

# 23. Failure Conditions

Return an explicit error/UNKNOWN state when:

* target species does not exist;
* current JAR cannot be found;
* spawn pool cannot be loaded;
* biome tag data is unavailable;
* spawn condition cannot be resolved;
* percentage mechanics are unknown;
* multiple incompatible versions are detected.

Do not guess.

---

# 24. Final Principle

The analyzer answers two different questions:

### Mathematical

> "Given the verified spawner selection algorithm, where does the target have the highest theoretical chance of being selected?"

### Practical

> "Where is it easiest/most reliable to actually hunt the target given entity-cap pressure, terrain, conditions, visibility, and spawn management?"

These questions must never be collapsed into one number.

The final answer must preserve the distinction:

```text
Mathematical Best
        ≠
Practical Best
```

unless both happen to point to the same biome independently.
