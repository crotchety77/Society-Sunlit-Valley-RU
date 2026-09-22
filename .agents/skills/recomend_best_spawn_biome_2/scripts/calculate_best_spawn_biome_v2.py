"""
calculate_best_spawn_biome_v2.py

Cobblemon Spawn Biome Analyzer (V2 - Dynamic Biome Discovery & Strict Two-Stage Model)
-------------------------------------------------------------------------------------
Key Improvements:
1. Strict Worldgen Inspection: Discovers all biomes from Vanilla + actual installed mods
   (Atmospheric, Autumnity, Windswept, Quark) and ignores phantom biomes from unloaded mods
   (e.g., Terralith, Biomes O' Plenty, Wythers) even if listed as optional in Cobblemon tags.
2. Complete Two-Stage Model:
   - P(Bucket) = BucketWeight / Sum(AllBucketWeights)
   - P(Target | Bucket, Context) = TargetWeight / Sum(MatchingWeights in Bucket & Context)
   - P(Target selected) = P(Bucket) * P(Target | Bucket, Context)
3. Direct Wild Spawn vs Acquisition Route audit across full evolution chains.
4. Qualitative Common Pressure diagnostic (no artificial probability penalization).
5. Mathematical Best vs Practical Best separation.
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import sys
import zipfile
from collections import defaultdict, deque
from dataclasses import dataclass, field
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple

# Reconfigure console output for UTF-8 safety on Windows
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# ============================================================================
# Configuration
# ============================================================================

BASE_PATH = r"G:\curseforge\minecraft\Instances\Society Sunlit Cobblemon"

BACKPORTED_JAR = os.path.join(
    BASE_PATH,
    "mods",
    "Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar",
)

LOCAL_SPAWN_DIR = os.path.join(
    BASE_PATH,
    "kubejs",
    "data",
    "cobblemon",
    "spawn_pool_world",
)

LOCAL_BIOME_TAG_DIRS = [
    os.path.join(
        BASE_PATH,
        "kubejs",
        "data",
        "cobblemon",
        "tags",
        "worldgen",
        "biome",
    ),
]

BUCKET_RATES: Dict[str, float] = {
    "common": 0.938,
    "uncommon": 0.050,
    "rare": 0.010,
    "ultra-rare": 0.002,
}

BUCKET_ALIASES = {
    "common": "common",
    "uncommon": "uncommon",
    "rare": "rare",
    "ultra-rare": "ultra-rare",
    "ultrarare": "ultra-rare",
    "ultra_rare": "ultra-rare",
    "ultra rare": "ultra-rare",
}

VANILLA_BIOMES: Set[str] = {
    "minecraft:badlands", "minecraft:bamboo_jungle", "minecraft:beach",
    "minecraft:birch_forest", "minecraft:cherry_grove", "minecraft:cold_ocean",
    "minecraft:dark_forest", "minecraft:deep_cold_ocean", "minecraft:deep_dark",
    "minecraft:deep_frozen_ocean", "minecraft:deep_lukewarm_ocean", "minecraft:deep_ocean",
    "minecraft:desert", "minecraft:dripstone_caves", "minecraft:eroded_badlands",
    "minecraft:flower_forest", "minecraft:forest", "minecraft:frozen_ocean",
    "minecraft:frozen_peaks", "minecraft:frozen_river", "minecraft:grove",
    "minecraft:ice_spikes", "minecraft:jagged_peaks", "minecraft:jungle",
    "minecraft:lukewarm_ocean", "minecraft:lush_caves", "minecraft:mangrove_swamp",
    "minecraft:meadow", "minecraft:mushroom_fields", "minecraft:ocean",
    "minecraft:old_growth_birch_forest", "minecraft:old_growth_pine_taiga",
    "minecraft:old_growth_spruce_taiga", "minecraft:plains", "minecraft:river",
    "minecraft:savanna", "minecraft:savanna_plateau", "minecraft:snowy_beach",
    "minecraft:snowy_plains", "minecraft:snowy_slopes", "minecraft:snowy_taiga",
    "minecraft:sparse_jungle", "minecraft:stony_peaks", "minecraft:stony_shore",
    "minecraft:sunflower_plains", "minecraft:swamp", "minecraft:taiga",
    "minecraft:warm_ocean", "minecraft:windswept_forest", "minecraft:windswept_gravelly_hills",
    "minecraft:windswept_hills", "minecraft:windswept_savanna", "minecraft:wooded_badlands",
}

VANILLA_TAGS: Dict[str, List[str]] = {
    "minecraft:is_mountain": [
        "minecraft:meadow", "minecraft:frozen_peaks", "minecraft:jagged_peaks",
        "minecraft:stony_peaks", "minecraft:snowy_slopes", "minecraft:grove", "minecraft:cherry_grove"
    ],
    "minecraft:is_hill": [
        "minecraft:windswept_hills", "minecraft:windswept_gravelly_hills", "minecraft:windswept_forest", "minecraft:windswept_savanna"
    ],
    "minecraft:is_forest": [
        "minecraft:forest", "minecraft:flower_forest", "minecraft:birch_forest",
        "minecraft:old_growth_birch_forest", "minecraft:dark_forest", "minecraft:grove"
    ],
    "minecraft:is_taiga": [
        "minecraft:taiga", "minecraft:snowy_taiga", "minecraft:old_growth_pine_taiga", "minecraft:old_growth_spruce_taiga"
    ],
    "minecraft:is_jungle": [
        "minecraft:jungle", "minecraft:sparse_jungle", "minecraft:bamboo_jungle"
    ],
    "minecraft:is_ocean": [
        "minecraft:ocean", "minecraft:deep_ocean", "minecraft:warm_ocean",
        "minecraft:lukewarm_ocean", "minecraft:deep_lukewarm_ocean", "minecraft:cold_ocean",
        "minecraft:deep_cold_ocean", "minecraft:frozen_ocean", "minecraft:deep_frozen_ocean"
    ],
    "minecraft:is_deep_ocean": [
        "minecraft:deep_ocean", "minecraft:deep_lukewarm_ocean", "minecraft:deep_cold_ocean", "minecraft:deep_frozen_ocean"
    ],
    "minecraft:is_river": [
        "minecraft:river", "minecraft:frozen_river"
    ],
    "minecraft:is_beach": [
        "minecraft:beach", "minecraft:snowy_beach"
    ],
    "minecraft:is_badlands": [
        "minecraft:badlands", "minecraft:eroded_badlands", "minecraft:wooded_badlands"
    ],
    "minecraft:is_nether": [
        "minecraft:nether_wastes", "minecraft:soul_sand_valley", "minecraft:crimson_forest", "minecraft:warped_forest", "minecraft:basalt_deltas"
    ],
    "minecraft:is_end": [
        "minecraft:the_end", "minecraft:small_end_islands", "minecraft:end_midlands", "minecraft:end_highlands", "minecraft:end_barrens"
    ],
    "forge:is_mountain": [
        "#minecraft:is_mountain", "windswept:lavender_hills", "windswept:pine_barrens", "windswept:snowy_pine_barrens"
    ],
    "forge:is_cave": [
        "minecraft:dripstone_caves", "minecraft:lush_caves", "minecraft:deep_dark", "quark:glimmering_weald"
    ]
}


# ============================================================================
# Data Structures
# ============================================================================

@dataclass
class BiomeTag:
    tag_id: str
    values: List[str]
    replace: bool = False
    source: str = ""

@dataclass
class SpawnEntry:
    pokemon: str
    bucket: str
    weight: Optional[float]
    percentage: Optional[float]
    condition: Dict[str, Any]
    anticondition: Dict[str, Any]
    source: str
    raw: Dict[str, Any]

@dataclass
class MatchingEntry:
    pokemon: str
    bucket: str
    weight: Optional[float]
    percentage: Optional[float]
    source: str
    raw: Dict[str, Any]

@dataclass
class SpawnAnalysis:
    pokemon: str
    biome: str
    context: str
    bucket: str
    bucket_probability: Optional[float]
    target_weight: Optional[float]
    target_percentage: Optional[float]
    matching_entries_count: int
    total_matching_weight: Optional[float]
    target_share: Optional[float]
    target_selection_probability: Optional[float]
    common_matching_count: int
    common_weight_sum: Optional[float]
    common_pressure: str
    practical_factors: List[str]
    hard_conditions: Dict[str, Any]
    competitors: List[Tuple[str, Optional[float]]]
    evidence: Dict[str, str] = field(default_factory=dict)

# ============================================================================
# Helpers & Loaders
# ============================================================================

def normalize_id(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip().lower()

def normalize_bucket(value: Any) -> str:
    val = normalize_id(value)
    return BUCKET_ALIASES.get(val, val)

def as_float(value: Any) -> Optional[float]:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None

def unique_preserve_order(values: Iterable[str]) -> List[str]:
    result = []
    seen = set()
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result

def get_installed_biomes() -> Set[str]:
    """Scan vanilla + installed mod JARs to find all real biomes."""
    biomes = set(VANILLA_BIOMES)
    mods_dir = os.path.join(BASE_PATH, "mods")
    if not os.path.isdir(mods_dir):
        return biomes

    for jar_path in glob.glob(os.path.join(mods_dir, "*.jar")):
        try:
            with zipfile.ZipFile(jar_path, "r") as z:
                for name in z.namelist():
                    # data/<namespace>/worldgen/biome/<biome_name>.json
                    parts = name.split("/")
                    if len(parts) == 5 and parts[0] == "data" and parts[2] == "worldgen" and parts[3] == "biome" and parts[4].endswith(".json"):
                        ns = parts[1]
                        bname = parts[4][:-5]
                        biomes.add(f"{ns}:{bname}")
        except Exception:
            pass
    return biomes

def load_data() -> Tuple[Dict[str, Dict[str, Any]], List[SpawnEntry], Dict[str, BiomeTag], Set[str]]:
    species_map: Dict[str, Dict[str, Any]] = {}
    spawn_entries: List[SpawnEntry] = []
    biome_tags: Dict[str, BiomeTag] = {}
    installed_biomes = get_installed_biomes()

    # Initialize standard Vanilla / Forge biome tags
    for tid, vals in VANILLA_TAGS.items():
        biome_tags[tid] = BiomeTag(tag_id=tid, values=vals, replace=False, source="BUILTIN_VANILLA")

    # 1. Load from Backported JAR
    if os.path.exists(BACKPORTED_JAR):
        try:
            with zipfile.ZipFile(BACKPORTED_JAR, "r") as jar:
                for name in jar.namelist():
                    if name.startswith("data/cobblemon/species/") and name.endswith(".json"):
                        try:
                            data = json.loads(jar.read(name).decode("utf-8"))
                            sname = normalize_id(data.get("name") or os.path.basename(name).rsplit(".", 1)[0])
                            if sname:
                                species_map[sname] = data
                        except Exception:
                            pass
                    elif name.startswith("data/cobblemon/spawn_pool_world/") and name.endswith(".json"):
                        try:
                            data = json.loads(jar.read(name).decode("utf-8"))
                            if data.get("enabled", True):
                                for raw in data.get("spawns", []):
                                    if isinstance(raw, dict):
                                        pkmn = normalize_id(raw.get("pokemon"))
                                        if pkmn:
                                            spawn_entries.append(SpawnEntry(
                                                pokemon=pkmn,
                                                bucket=normalize_bucket(raw.get("bucket", "common")),
                                                weight=as_float(raw.get("weight")),
                                                percentage=as_float(raw.get("percentage")),
                                                condition=raw.get("condition") or {},
                                                anticondition=raw.get("anticondition") or {},
                                                source=f"JAR:{name}",
                                                raw=raw
                                            ))
                        except Exception:
                            pass
                    elif name.startswith("data/") and "/tags/worldgen/biome/" in name and name.endswith(".json"):
                        try:
                            data = json.loads(jar.read(name).decode("utf-8"))
                            # extract tag_id
                            parts = name.split("/")
                            ns = parts[1]
                            tname = "/".join(parts[parts.index("biome") + 1:])[:-5]
                            tag_id = f"{ns}:{tname}"
                            biome_tags[tag_id] = BiomeTag(
                                tag_id=tag_id,
                                values=[str(v) if isinstance(v, (str, int, float)) else str(v.get("id", "")) for v in data.get("values", [])],
                                replace=bool(data.get("replace", False)),
                                source=f"JAR:{name}"
                            )
                        except Exception:
                            pass
        except Exception as e:
            print(f"[ERROR] Failed to load JAR data: {e}", file=sys.stderr)

    # 2. Load Local KubeJS overrides
    if os.path.isdir(LOCAL_SPAWN_DIR):
        for p in glob.glob(os.path.join(LOCAL_SPAWN_DIR, "*.json")):
            try:
                with open(p, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if data.get("enabled", True):
                        for raw in data.get("spawns", []):
                            if isinstance(raw, dict):
                                pkmn = normalize_id(raw.get("pokemon"))
                                if pkmn:
                                    spawn_entries.append(SpawnEntry(
                                        pokemon=pkmn,
                                        bucket=normalize_bucket(raw.get("bucket", "common")),
                                        weight=as_float(raw.get("weight")),
                                        percentage=as_float(raw.get("percentage")),
                                        condition=raw.get("condition") or {},
                                        anticondition=raw.get("anticondition") or {},
                                        source=f"LOCAL:{p}",
                                        raw=raw
                                    ))
            except Exception:
                pass

    return species_map, spawn_entries, biome_tags, installed_biomes

# ============================================================================
# Biome Tag Resolver (Filtering Phantom Biomes)
# ============================================================================

class BiomeTagResolver:
    def __init__(self, tags: Dict[str, BiomeTag], installed_biomes: Set[str]):
        self.tags = tags
        self.installed_biomes = installed_biomes
        self._cache: Dict[str, Set[str]] = {}

    def _normalize_tag_id(self, tag_id: str) -> str:
        tag_id = normalize_id(tag_id)
        if tag_id.startswith("#"):
            tag_id = tag_id[1:]
        if ":" not in tag_id:
            tag_id = f"minecraft:{tag_id}"
        return tag_id

    def resolve_tag(self, tag_id: str, stack: Optional[Set[str]] = None) -> Set[str]:
        tag_id = self._normalize_tag_id(tag_id)
        if tag_id in self._cache:
            return set(self._cache[tag_id])

        if stack is None:
            stack = set()
        if tag_id in stack:
            return set()
        stack.add(tag_id)

        tag = self.tags.get(tag_id)
        if not tag:
            self._cache[tag_id] = set()
            return set()

        result: Set[str] = set()
        for raw_value in tag.values:
            val = str(raw_value).strip()
            if not val:
                continue
            if val.startswith("?"):
                val = val[1:]
            
            if val.startswith("#"):
                nested = self._normalize_tag_id(val)
                result.update(self.resolve_tag(nested, stack))
            else:
                norm_biome = normalize_id(val)
                # STRICT AUDIT: Only keep biome if it actually exists in game instance!
                if norm_biome in self.installed_biomes:
                    result.add(norm_biome)

        stack.remove(tag_id)
        self._cache[tag_id] = set(result)
        return result

    def resolve_requirement(self, requirement: Any, biome_id: str) -> bool:
        if not isinstance(requirement, str):
            return False
        val = requirement.strip()
        if not val:
            return False
        if val.startswith("#"):
            tag_id = self._normalize_tag_id(val)
            return normalize_id(biome_id) in self.resolve_tag(tag_id)
        return normalize_id(val) == normalize_id(biome_id)

# ============================================================================
# Evolution & Context Evaluation
# ============================================================================

def get_evolution_chain(target: str, species_map: Dict[str, Dict[str, Any]]) -> List[str]:
    target = normalize_id(target)
    if target not in species_map:
        return [target]

    parents = defaultdict(set)
    children = defaultdict(set)
    for sname, data in species_map.items():
        for evo in data.get("evolutions", []):
            res = normalize_id(evo.get("result"))
            if res:
                children[sname].add(res)
                parents[res].add(sname)

    # find roots
    roots = set()
    queue = deque([target])
    visited = set()
    while queue:
        curr = queue.popleft()
        if curr in visited:
            continue
        visited.add(curr)
        plist = parents.get(curr)
        if not plist:
            roots.add(curr)
        else:
            for p in plist:
                queue.append(p)

    # collect
    chain = []
    visited_nodes = set()
    def dfs(node: str):
        if node in visited_nodes:
            return
        visited_nodes.add(node)
        chain.append(node)
        for ch in sorted(children.get(node, [])):
            dfs(ch)

    for r in sorted(roots):
        dfs(r)

    return unique_preserve_order(chain) if chain else [target]

def classify_context(entry: SpawnEntry) -> str:
    cond = entry.condition
    if cond.get("fluid") is not None or cond.get("submerged") is True:
        return "Submerged / Water"
    max_sky = as_float(cond.get("maxSkyLight"))
    if max_sky is not None and max_sky < 8:
        return "Underground / Cave"
    return "Surface / Land"

def entry_matches_biome(entry: SpawnEntry, biome_id: str, resolver: BiomeTagResolver) -> bool:
    cond_biomes = entry.condition.get("biomes", [])
    anti_biomes = entry.anticondition.get("biomes", [])
    if not isinstance(cond_biomes, list):
        cond_biomes = []
    if not isinstance(anti_biomes, list):
        anti_biomes = []

    for req in anti_biomes:
        if resolver.resolve_requirement(req, biome_id):
            return False
    if not cond_biomes:
        return True
    for req in cond_biomes:
        if resolver.resolve_requirement(req, biome_id):
            return True
    return False

def entry_matches_context(entry: SpawnEntry, context: str) -> bool:
    c = classify_context(entry)
    return c == context

# ============================================================================
# Two-Stage Calculation Engine
# ============================================================================

def analyze_stage_in_biome(
    target: str,
    stage_entry: SpawnEntry,
    biome_id: str,
    context: str,
    all_spawns: List[SpawnEntry],
    resolver: BiomeTagResolver,
) -> Optional[SpawnAnalysis]:
    # 1. Filter all entries in the game that match this biome & context
    matching_grouped: Dict[str, List[MatchingEntry]] = defaultdict(list)
    for entry in all_spawns:
        if entry_matches_biome(entry, biome_id, resolver) and entry_matches_context(entry, context):
            matching_grouped[entry.bucket].append(MatchingEntry(
                pokemon=entry.pokemon,
                bucket=entry.bucket,
                weight=entry.weight,
                percentage=entry.percentage,
                source=entry.source,
                raw=entry.raw
            ))

    bucket_entries = matching_grouped.get(stage_entry.bucket, [])
    p_bucket = BUCKET_RATES.get(stage_entry.bucket)
    
    total_matching_weight = None
    target_share = None
    target_prob = None

    if stage_entry.weight is not None:
        weights = [e.weight for e in bucket_entries if e.weight is not None]
        total_matching_weight = sum(weights)
        if total_matching_weight > 0:
            target_share = stage_entry.weight / total_matching_weight
            if p_bucket is not None:
                target_prob = p_bucket * target_share

    # Common diagnostics
    common_entries = matching_grouped.get("common", [])
    common_weights = [e.weight for e in common_entries if e.weight is not None]
    common_count = len(common_entries)
    common_sum = sum(common_weights)

    if context == "Underground / Cave":
        common_pressure = "High (Cave Mob Cap)"
    elif common_count <= 4 and common_sum <= 50:
        common_pressure = "Low (Sparse/Open)"
    elif common_count >= 12 or common_sum >= 150:
        common_pressure = "High (Dense Pool)"
    else:
        common_pressure = "Medium (Moderate)"

    # Competitors in same bucket
    competitors = [
        (e.pokemon, e.weight)
        for e in bucket_entries
        if e.pokemon != target and e.weight is not None
    ]
    competitors.sort(key=lambda x: x[1] if x[1] is not None else -1, reverse=True)

    # Practical factors
    pract_factors = []
    if context == "Surface / Land":
        pract_factors.append("Open surface, easy 30-60 block despawn cycle")
    elif context == "Underground / Cave":
        pract_factors.append("Cave darkness, requires torching/clearing unlit pockets")
    else:
        pract_factors.append("Water column, swim navigation")

    return SpawnAnalysis(
        pokemon=target,
        biome=biome_id,
        context=context,
        bucket=stage_entry.bucket,
        bucket_probability=p_bucket,
        target_weight=stage_entry.weight,
        target_percentage=stage_entry.percentage,
        matching_entries_count=len(bucket_entries),
        total_matching_weight=total_matching_weight,
        target_share=target_share,
        target_selection_probability=target_prob,
        common_matching_count=common_count,
        common_weight_sum=common_sum,
        common_pressure=common_pressure,
        practical_factors=pract_factors,
        hard_conditions=stage_entry.condition,
        competitors=competitors[:5],
        evidence={
            "bucket": "FACT",
            "selection_prob": "CALCULATED" if target_prob is not None else "UNKNOWN",
            "common_pressure": "INFERENCE"
        }
    )

def run_analysis(target_name: str) -> Dict[str, Any]:
    species_map, spawn_entries, biome_tags, installed_biomes = load_data()
    target = normalize_id(target_name)
    resolver = BiomeTagResolver(biome_tags, installed_biomes)
    evo_chain = get_evolution_chain(target, species_map)

    spawns_by_pkmn = defaultdict(list)
    for e in spawn_entries:
        spawns_by_pkmn[e.pokemon].append(e)

    results_by_stage = {}
    for stage in evo_chain:
        stage_spawns = spawns_by_pkmn.get(stage, [])
        stage_analyses: List[SpawnAnalysis] = []
        
        for entry in stage_spawns:
            ctx = classify_context(entry)
            for biome_id in sorted(installed_biomes):
                if entry_matches_biome(entry, biome_id, resolver):
                    res = analyze_stage_in_biome(stage, entry, biome_id, ctx, spawn_entries, resolver)
                    if res:
                        stage_analyses.append(res)
        
        results_by_stage[stage] = {
            "has_spawns": len(stage_spawns) > 0,
            "spawn_entries_count": len(stage_spawns),
            "analyses": stage_analyses
        }

    return {
        "target": target,
        "evolution_chain": evo_chain,
        "stages": results_by_stage
    }

# ============================================================================
# Output Formatter
# ============================================================================

def print_report(data: Dict[str, Any]):
    target = data["target"]
    evo_chain = data["evolution_chain"]

    print("=" * 135)
    print(f"COBBLEMON V2 AUDIT: {target.upper()} | Evolution Line: {' -> '.join([s.capitalize() for s in evo_chain])}")
    print("=" * 135)

    print("\n🧬 [ACQUISITION ROUTE AUDIT]")
    for stage in evo_chain:
        info = data["stages"][stage]
        status = f"[FACT] Direct Wild Spawn AVAILABLE ({info['spawn_entries_count']} entries)" if info["has_spawns"] else "[FACT] No direct wild spawns"
        print(f"  * {stage.capitalize():<15} -> {status}")

    for stage in evo_chain:
        info = data["stages"][stage]
        analyses: List[SpawnAnalysis] = info["analyses"]
        if not analyses:
            continue

        print("\n" + "=" * 135)
        print(f"STAGE: {stage.upper()} (Analyses in Installed Biomes: {len(analyses)})")
        print("=" * 135)

        # Group by context
        contexts = unique_preserve_order([a.context for a in analyses])
        for ctx in contexts:
            ctx_analyses = [a for a in analyses if a.context == ctx]
            # Deduplicate by biome (keeping highest target_selection_probability)
            best_by_biome: Dict[str, SpawnAnalysis] = {}
            for a in ctx_analyses:
                if a.biome not in best_by_biome or (a.target_selection_probability or 0) > (best_by_biome[a.biome].target_selection_probability or 0):
                    best_by_biome[a.biome] = a

            sorted_analyses = sorted(best_by_biome.values(), key=lambda x: x.target_selection_probability or 0, reverse=True)

            print(f"\n>>> [{ctx}]")
            print(f"{'BIOME':<34} | {'BUCKET':<10} | {'MATCH':<5} | {'SHARE':<10} | {'P(TARGET)':<12} | {'COMMON_PRESS':<20} | {'MAIN COMPETITORS'}")
            print("-" * 135)

            for i, a in enumerate(sorted_analyses[:8], 1):
                share_str = f"{a.target_share * 100:.2f}%" if a.target_share is not None else "UNKNOWN"
                prob_str = f"{a.target_selection_probability * 100:.4f}%" if a.target_selection_probability is not None else "UNKNOWN"
                comp_str = ", ".join([f"{c[0]} ({c[1]})" for c in a.competitors[:2]]) if a.competitors else "None (Single in Bucket!)"
                tag = " [Mathematical Best]" if i == 1 else ""
                print(f"{a.biome:<34} | {a.bucket:<10} | {a.matching_entries_count:<5} | {share_str:<10} | {prob_str:<12} | {a.common_pressure:<20} | {comp_str}{tag}")

def main():
    parser = argparse.ArgumentParser(description="Cobblemon Dynamic Spawn Biome Analyzer V2")
    parser.add_argument("pokemon", nargs="?", default="gible", help="Target Pokémon name")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")
    args = parser.parse_args()

    data = run_analysis(args.pokemon)
    if args.json:
        print(json.dumps(data, indent=2, default=str))
    else:
        print_report(data)

if __name__ == "__main__":
    main()
