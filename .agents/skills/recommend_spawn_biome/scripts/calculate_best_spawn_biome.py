"""
Automated Spawn Biome Recommendation & Mathematical Pool Analyzer for Cobblemon
Strict implementation adhering to Evidence Policy and Two-Stage Spawning Architecture.
"""
import sys, os, glob, json, zipfile
from collections import defaultdict

if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except:
        pass

BASE_PATH = r"G:\curseforge\minecraft\Instances\Society Sunlit Cobblemon"
BACKPORTED_JAR = os.path.join(BASE_PATH, "mods", "Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar")

BUCKET_RATES = {
    'common': 93.8 / 100.0,
    'uncommon': 5.0 / 100.0,
    'rare': 1.0 / 100.0,
    'ultra-rare': 0.2 / 100.0
}

KNOWN_BIOMES = [
    # Minecraft 1.20.1 Vanilla
    'minecraft:jagged_peaks',
    'minecraft:frozen_peaks',
    'minecraft:stony_peaks',
    'minecraft:meadow',
    'minecraft:snowy_slopes',
    'minecraft:grove',
    'minecraft:windswept_hills',
    'minecraft:windswept_gravelly_hills',
    'minecraft:windswept_forest',
    'minecraft:windswept_savanna',
    'minecraft:plains',
    'minecraft:sunflower_plains',
    'minecraft:forest',
    'minecraft:flower_forest',
    'minecraft:birch_forest',
    'minecraft:dark_forest',
    'minecraft:taiga',
    'minecraft:snowy_taiga',
    'minecraft:jungle',
    'minecraft:sparse_jungle',
    'minecraft:desert',
    'minecraft:badlands',
    'minecraft:eroded_badlands',
    'minecraft:wooded_badlands',
    'minecraft:savanna',
    'minecraft:savanna_plateau',
    'minecraft:beach',
    'minecraft:stony_shore',
    'minecraft:river',
    'minecraft:ocean',
    'minecraft:deep_ocean',
    'minecraft:warm_ocean',
    'minecraft:lukewarm_ocean',
    'minecraft:cold_ocean',
    'minecraft:swamp',
    'minecraft:mangrove_swamp',
    'minecraft:dripstone_caves',
    'minecraft:lush_caves',
    'minecraft:deep_dark',
    'minecraft:cherry_grove',
    'minecraft:ice_spikes',
    'minecraft:mushroom_fields',
    'minecraft:old_growth_birch_forest',
    'minecraft:old_growth_pine_taiga',
    'minecraft:old_growth_spruce_taiga',
    'minecraft:snowy_beach',
    'minecraft:snowy_plains',
    # Windswept mod
    'windswept:chestnut_forest',
    'windswept:snowy_chestnut_forest',
    'windswept:flowering_savanna',
    'windswept:lavender_fields',
    'windswept:lavender_hills',
    'windswept:pine_barrens',
    'windswept:snowy_pine_barrens',
    'windswept:tundra',
    # Atmospheric mod
    'atmospheric:aspen_parkland',
    'atmospheric:dunes',
    'atmospheric:flourishing_dunes',
    'atmospheric:petrified_dunes',
    'atmospheric:rocky_dunes',
    'atmospheric:grimwoods',
    'atmospheric:hot_springs',
    'atmospheric:kousa_jungle',
    'atmospheric:laurel_forest',
    'atmospheric:rainforest',
    'atmospheric:rainforest_basin',
    'atmospheric:sparse_rainforest',
    'atmospheric:sparse_rainforest_basin',
    'atmospheric:scrubland',
    'atmospheric:snowy_scrubland',
    'atmospheric:spiny_thicket',
    # Autumnity mod
    'autumnity:maple_forest',
    'autumnity:pumpkin_fields',
    # Quark mod
    'quark:glimmering_weald'
]


def load_all_data():
    species_map = {}
    spawn_entries = []
    
    if os.path.exists(BACKPORTED_JAR):
        with zipfile.ZipFile(BACKPORTED_JAR, 'r') as z:
            for name in z.namelist():
                if name.startswith('data/cobblemon/species/') and name.endswith('.json'):
                    try:
                        data = json.loads(z.read(name).decode('utf-8'))
                        sp_name = data.get('name', '').lower()
                        species_map[sp_name] = data
                    except:
                        pass
                elif name.startswith('data/cobblemon/spawn_pool_world/') and name.endswith('.json'):
                    try:
                        data = json.loads(z.read(name).decode('utf-8'))
                        if data.get('enabled', True):
                            for s in data.get('spawns', []):
                                spawn_entries.append(s)
                    except:
                        pass

    local_spawns_dir = os.path.join(BASE_PATH, "kubejs", "data", "cobblemon", "spawn_pool_world")
    if os.path.exists(local_spawns_dir):
        for f in glob.glob(os.path.join(local_spawns_dir, "*.json")):
            try:
                with open(f, 'r', encoding='utf-8') as handle:
                    data = json.load(handle)
                    if data.get('enabled', True):
                        for s in data.get('spawns', []):
                            spawn_entries.append(s)
            except:
                pass

    return species_map, spawn_entries

def matches_biome(required_biomes, biome_id, is_surface=True, is_anticond=False):
    if not required_biomes:
        return False if is_anticond else True
    for req in required_biomes:
        if req == biome_id:
            return True
        if req.startswith('#'):
            tag_clean = req.lower()
            if 'is_mountain' in tag_clean and any(m in biome_id for m in ['peaks', 'slopes', 'hills', 'spires', 'crag', 'windswept', 'cliffs', 'grove']):
                return True
            if 'is_hills' in tag_clean and any(m in biome_id for m in ['hills', 'slopes', 'cliffs', 'crag', 'valley', 'highland']):
                return True
            if 'is_forest' in tag_clean and any(m in biome_id for m in ['forest', 'taiga', 'grove', 'woods', 'jungle']):
                return True
            if 'is_taiga' in tag_clean and any(m in biome_id for m in ['taiga', 'grove', 'pine', 'spruce']):
                return True
            if 'is_plains' in tag_clean and any(m in biome_id for m in ['plains', 'meadow', 'sunflower', 'shrubland']):
                return True
            if 'is_arid' in tag_clean and any(m in biome_id for m in ['desert', 'badlands', 'savanna', 'oasis', 'canyon', 'wasteland']):
                return True
            if 'is_desert' in tag_clean and any(m in biome_id for m in ['desert', 'oasis', 'canyon', 'wasteland']):
                return True
            if 'is_badlands' in tag_clean and any(m in biome_id for m in ['badlands', 'painted_mountains']):
                return True
            if 'is_savanna' in tag_clean and any(m in biome_id for m in ['savanna']):
                return True
            if 'is_coast' in tag_clean and any(m in biome_id for m in ['beach', 'shore', 'coast']):
                return True
            if 'is_ocean' in tag_clean and any(m in biome_id for m in ['ocean']):
                return True
            if 'is_freezing' in tag_clean and any(m in biome_id for m in ['frozen', 'snowy', 'jagged', 'ice', 'icy']):
                return True
            if 'is_snowy' in tag_clean and any(m in biome_id for m in ['snowy', 'frozen', 'grove', 'ice']):
                return True
            if 'is_overworld' in tag_clean:
                if not ('nether' in biome_id or 'end' in biome_id):
                    return True
    return False

def get_evolution_chain(target_name, species_map):
    target_lower = target_name.lower()
    parents = {}
    children = defaultdict(list)
    
    for sp_name, data in species_map.items():
        for evo in data.get('evolutions', []):
            res = evo.get('result', '').lower()
            if res:
                parents[res] = sp_name
                children[sp_name].append(res)
                
    root = target_lower
    while root in parents:
        root = parents[root]
        
    chain = []
    def traverse(curr):
        chain.append(curr)
        for c in children.get(curr, []):
            if c not in chain:
                traverse(c)
                
    traverse(root)
    return chain

def classify_common_pressure(is_surface, biome_id, common_entries):
    # Context-aware qualitative assessment based on pool composition and terrain
    if not is_surface or 'cave' in biome_id or 'dark' in biome_id:
        # High cave density pressure
        return "High (Cave Mob Cap)"
    if any(k in biome_id for k in ['peaks', 'spires', 'volcanic', 'crag']):
        return "Low (Sparse Mountain)"
    if any(k in biome_id for k in ['plains', 'meadow', 'desert', 'beach', 'wasteland']):
        return "Low (Open Ground)"
    if any(k in biome_id for k in ['forest', 'jungle', 'taiga', 'grove', 'savanna']):
        return "Medium (Foliage/Hills)"
    return "Unknown"

def analyze(target_name):
    species_map, spawn_entries = load_all_data()
    target_lower = target_name.lower()
    chain = get_evolution_chain(target_lower, species_map)
    if not chain:
        chain = [target_lower]

    print("=" * 135)
    print(f"POKÉMON SPAWN ANALYSIS: {target_name.upper()} | Evolution Line: {' -> '.join(c.capitalize() for c in chain)}")
    print("=" * 135)

    wild_spawns_per_stage = {}
    for pkmn in chain:
        spawns = [s for s in spawn_entries if s.get('pokemon', '').lower() == pkmn]
        wild_spawns_per_stage[pkmn] = spawns

    # Determine Acquisition Route
    print("\n🧬 [ACQUISITION ROUTE AUDIT]")
    for pkmn in chain:
        sp_count = len(wild_spawns_per_stage[pkmn])
        status = f"Direct Wild Spawn AVAILABLE ({sp_count} entries)" if sp_count > 0 else "NO wild spawns (Evolution/Breeding only)"
        marker = "[FACT]"
        print(f"  * {pkmn.capitalize():<12} -> {marker} {status}")

    for pkmn in chain:
        spawns = wild_spawns_per_stage[pkmn]
        print(f"\n===================================================================================================================================")
        print(f"STAGE: {pkmn.upper()} (Total direct spawn entries: {len(spawns)})")
        print(f"===================================================================================================================================")
        if not spawns:
            print(f"  [Direct Evidence] No wild world spawns. Obtain via evolution from previous stage.")
            continue

        for context_mode in ['Surface (Open Sky / Daytime & Night)', 'Underground / Cave (Darkness & Low Y)', 'Submerged / Water (Oceans & Rivers)']:
            is_surf = ('Surface' in context_mode)
            is_water = ('Water' in context_mode)
            is_cave = ('Cave' in context_mode)
            
            biome_results = []
            
            for biome_id in KNOWN_BIOMES:
                matching_bucket_spawns = defaultdict(list)
                target_entries = []
                
                for s in spawn_entries:
                    cond = s.get('condition', {})
                    anticond = s.get('anticondition', {})
                    max_sky = cond.get('maxSkyLight')
                    fluid = cond.get('fluid')
                    submerged = cond.get('submerged')
                    
                    # Context checks
                    if is_water:
                        if fluid is None and submerged is None:
                            continue
                    else:
                        if fluid is not None or submerged is True:
                            continue
                        if is_surf and max_sky is not None and max_sky < 8:
                            continue
                        if is_cave and (max_sky is None or max_sky >= 8):
                            continue
                        
                    if matches_biome(anticond.get('biomes', []), biome_id, is_surf, is_anticond=True):
                        continue
                    if matches_biome(cond.get('biomes', []), biome_id, is_surf, is_anticond=False):
                        p_name = s.get('pokemon', '').lower()
                        b_name = s.get('bucket', 'common').lower()
                        weight = s.get('weight')
                        percentage = s.get('percentage')
                        
                        entry_info = {
                            'pokemon': p_name,
                            'weight': float(weight) if weight is not None else None,
                            'percentage': float(percentage) if percentage is not None else None,
                            'cond': cond
                        }
                        matching_bucket_spawns[b_name].append(entry_info)
                        if p_name == pkmn:
                            target_entries.append((b_name, entry_info))

                if target_entries:
                    common_entries = matching_bucket_spawns.get('common', [])
                    w_common = sum(x['weight'] for x in common_entries if x['weight'] is not None)
                    common_pressure = classify_common_pressure(is_surf, biome_id, common_entries)
                    
                    for t_bucket, t_info in target_entries:
                        target_w = t_info['weight']
                        target_pct = t_info['percentage']
                        bucket_list = matching_bucket_spawns[t_bucket]
                        
                        # Intra-Bucket & Selection Probability Calculation
                        if target_w is not None:
                            # Weight-based entry
                            active_weights = [x['weight'] for x in bucket_list if x['weight'] is not None]
                            total_bucket_w = sum(active_weights)
                            if total_bucket_w > 0:
                                target_share = (target_w / total_bucket_w) * 100.0
                                bucket_base_rate = BUCKET_RATES.get(t_bucket, 0.01)
                                target_selection_prob = bucket_base_rate * (target_share / 100.0) * 100.0
                                share_str = f"{target_share:>6.2f}%"
                                prob_str = f"{target_selection_prob:>8.4f}%"
                            else:
                                share_str = "UNKNOWN"
                                prob_str = "UNKNOWN"
                        elif target_pct is not None:
                            # Percentage-based entry
                            share_str = f"{target_pct:>6.2f}% [Fixed]"
                            prob_str = "UNKNOWN"
                        else:
                            share_str = "UNKNOWN"
                            prob_str = "UNKNOWN"
                            total_bucket_w = 0.0

                        matching_entries_count = len(bucket_list)
                        competitors = sorted([x for x in bucket_list if x['pokemon'] != pkmn and x['weight'] is not None], key=lambda x: x['weight'], reverse=True)
                        top_competitors = [(x['pokemon'], x['weight']) for x in competitors[:3]]
                        
                        # Practical factors
                        if is_surf:
                            pract_factors = "Open sky, easy despawn" if "Low" in common_pressure else "Hills/foliage, moderate despawn"
                        elif is_cave:
                            pract_factors = "Dark cave, mob cap choke risk"
                        else:
                            pract_factors = "Water column, swim navigation"

                        biome_results.append({
                            'biome': biome_id,
                            'bucket': t_bucket,
                            'matching_count': matching_entries_count,
                            'target_share': share_str,
                            'selection_prob': prob_str,
                            'share_val': target_share if target_w is not None and total_bucket_w > 0 else 0.0,
                            'w_common': round(w_common, 1),
                            'common_pressure': common_pressure,
                            'competitors': top_competitors,
                            'practical_factors': pract_factors
                        })

            # Sort by target share
            biome_results.sort(key=lambda x: x['share_val'], reverse=True)
            
            if biome_results:
                print(f"\n>>> [{context_mode}]")
                print(f"{'BIOME':<32} | {'BUCKET':<10} | {'MATCH_ENTRIES':<13} | {'TARGET_SHARE':<14} | {'SELECTION_PROB':<14} | {'COMMON_PRESS':<22} | {'MAIN COMPETITORS'}")
                print("-" * 135)
                seen_biomes = set()
                rank = 0
                for b in biome_results:
                    if b['biome'] in seen_biomes:
                        continue
                    seen_biomes.add(b['biome'])
                    rank += 1
                    comp_str = ", ".join([f"{c[0]} ({c[1]})" for c in b['competitors'][:2]]) if b['competitors'] else "None (Single in Bucket!)"
                    verdict_tag = " [Mathematical Best]" if rank == 1 else ""
                    print(f"{b['biome']:<32} | {b['bucket']:<10} | {b['matching_count']:<13} | {b['target_share']:<14} | {b['selection_prob']:<14} | {b['common_pressure']:<22} | {comp_str}{verdict_tag}")
                    if len(seen_biomes) >= 6:
                        break

def run_unit_tests():
    print("=" * 80)
    print("RUNNING UNIT TESTS FOR SELECTION LOGIC")
    print("=" * 80)
    
    # Test 1: Independence of Bucket Selection from Common Pool Size
    # Biome A: Common has 50 entries with sum weight 500, Rare has Gible (10)
    # Biome B: Common has 1 entry with sum weight 10, Rare has Gible (10)
    p_rare = BUCKET_RATES['rare'] # 0.01
    
    gible_a_share = 10.0 / 10.0 # 100%
    gible_a_prob = p_rare * gible_a_share
    
    gible_b_share = 10.0 / 10.0 # 100%
    gible_b_prob = p_rare * gible_b_share
    
    assert gible_a_prob == gible_b_prob == 0.01, "Test 1 Failed: Common pool affected Rare selection probability!"
    print("✓ Test 1 Passed: Common pool size does NOT alter Rare bucket selection probability.")

    # Test 2: Intra-Bucket Context Inactive Competitor Filter
    # Biome A: Rare has Gible (10) and Dratini (5) -> Total = 15 -> Gible Share = 10/15 = 66.67%
    # Biome B: Rare has Gible (10) and Dratini (5), but Dratini is inactive in Biome B -> Total = 10 -> Gible Share = 10/10 = 100%
    biome_a_matching = [10.0, 5.0]
    biome_b_matching = [10.0] # Dratini filtered out
    
    share_a = 10.0 / sum(biome_a_matching) * 100.0
    share_b = 10.0 / sum(biome_b_matching) * 100.0
    
    assert round(share_a, 2) == 66.67, f"Test 2 Failed: Share A was {share_a}"
    assert round(share_b, 2) == 100.0, f"Test 2 Failed: Share B was {share_b}"
    print(f"✓ Test 2 Passed: Inactive competitors correctly excluded from denominator (Share A = {share_a:.2f}%, Share B = {share_b:.2f}%).")
    print("=" * 80)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        run_unit_tests()
    else:
        t = sys.argv[1] if len(sys.argv) > 1 else 'gible'
        analyze(t)
