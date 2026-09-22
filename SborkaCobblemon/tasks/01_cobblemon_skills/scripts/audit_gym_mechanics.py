import sys
import zipfile
import json
import os
import glob
import re
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

jar_path = r'G:\curseforge\minecraft\Instances\Society Sunlit Cobblemon\mods\rctmod-forge-1.20.1-0.12.1-beta.jar'
kubejs_trainers = r'G:\curseforge\minecraft\Instances\Society Sunlit Cobblemon\kubejs\data\rctmod\trainers'

jar_trainers = {}
if os.path.exists(jar_path):
    with zipfile.ZipFile(jar_path, 'r') as z:
        for name in z.namelist():
            if name.startswith('data/rctmod/trainers/') and name.endswith('.json'):
                t_id = os.path.basename(name)[:-5]
                try:
                    jar_trainers[t_id] = json.loads(z.read(name).decode('utf-8'))
                except Exception as e:
                    pass

k_trainers = {}
if os.path.exists(kubejs_trainers):
    for f in glob.glob(os.path.join(kubejs_trainers, '*.json')):
        t_id = os.path.basename(f)[:-5]
        with open(f, 'r', encoding='utf-8') as fh:
            try:
                k_trainers[t_id] = json.load(fh)
            except Exception as e:
                pass

def get_trainer(t_id):
    if t_id in k_trainers:
        return k_trainers[t_id], 'kubejs'
    if t_id in jar_trainers:
        return jar_trainers[t_id], 'jar'
    return None, 'none'

# Parse cobblemonGymUtils.js
gym_utils_path = r'G:\curseforge\minecraft\Instances\Society Sunlit Cobblemon\kubejs\startup_scripts\cobblemon\cobblemonGymUtils.js'
with open(gym_utils_path, 'r', encoding='utf-8') as f:
    code = f.read()

# Let's extract the exact lines of trainerBuckets
lines = code.splitlines()
buckets = {}
cur_tier = None
cur_list = []
in_map = False

for line in lines:
    if "const trainerBuckets = new Map([" in line:
        in_map = True
        continue
    if in_map and "]);" in line:
        if cur_tier is not None:
            buckets[cur_tier] = cur_list
        in_map = False
        break
    if in_map:
        m_tier = re.match(r'^\s*(\d+),?\s*$', line)
        if m_tier:
            if cur_tier is not None:
                buckets[cur_tier] = cur_list
            cur_tier = int(m_tier.group(1))
            cur_list = []
            continue
        m_str = re.findall(r'["\']([^"\']+)["\']', line)
        if m_str and cur_tier is not None:
            for s in m_str:
                if s not in [']', '[']:
                    cur_list.append(s)

def parse_array(var_name):
    m = re.search(rf'const {var_name} = \[([\s\S]*?)\]', code)
    if m:
        return re.findall(r'["\']([^"\']+)["\']', m.group(1))
    return []

elite_easy = parse_array('eliteModeEasy')
elite_hard = parse_array('eliteModeHard')
league_bosses = parse_array('leagueBosses')
tier9_bosses = parse_array('tier9Bosses')

def analyze_group(name, t_list):
    total = len(t_list)
    missing = []
    team_sizes = []
    levels = []
    ai_levels = []
    iv_counts = defaultdict(int)
    ev_counts = 0
    held_item_counts = 0
    legendaries = []

    for t_id in t_list:
        t, src = get_trainer(t_id)
        if not t:
            missing.append(t_id)
            continue
        team = t.get('team', [])
        team_sizes.append(len(team))
        ai = t.get('aiLevel', 0)
        ai_levels.append(ai)
        for mon in team:
            lvl = mon.get('level', 1)
            levels.append(lvl)
            if mon.get('heldItem'):
                held_item_counts += 1
            if mon.get('evs') and any(mon.get('evs').values()):
                ev_counts += 1
            ivs = mon.get('ivs', {})
            perfect_ivs = sum(1 for v in ivs.values() if v >= 31)
            iv_counts[perfect_ivs] += 1
            species = mon.get('species', '')
            if species in ['cobblemon:mewtwo', 'cobblemon:zapdos', 'cobblemon:articuno', 'cobblemon:moltres', 'cobblemon:raikou', 'cobblemon:entei', 'cobblemon:suicune', 'cobblemon:lugia', 'cobblemon:ho_oh', 'cobblemon:celebi', 'cobblemon:kyogre', 'cobblemon:groudon', 'cobblemon:rayquaza', 'cobblemon:dialga', 'cobblemon:palkia', 'cobblemon:giratina', 'cobblemon:arceus']:
                legendaries.append((t_id, species))

    min_sz = min(team_sizes) if team_sizes else 0
    max_sz = max(team_sizes) if team_sizes else 0
    min_lvl = min(levels) if levels else 0
    max_lvl = max(levels) if levels else 0
    min_ai = min(ai_levels) if ai_levels else 0
    max_ai = max(ai_levels) if ai_levels else 0

    print(f"{name:28} | Count: {total:2} | TeamSize: {min_sz}-{max_sz} (avg {sum(team_sizes)/len(team_sizes):.1f}) | Levels: {min_lvl:2}-{max_lvl:3} (avg {sum(levels)/len(levels):.1f}) | AI: {min_ai}-{max_ai} | EV: {(ev_counts/len(levels)*100 if levels else 0):3.0f}% | 6IV: {(iv_counts[6]/len(levels)*100 if levels else 0):3.0f}%")

print("=== STANDARD GYM TIERS (10 - 95) ===")
for b in sorted(buckets.keys()):
    analyze_group(f"Tier {b}", buckets[b])

print("\n=== UPGRADED / ELITE GYM ===")
analyze_group("Elite Mode Easy (75%)", elite_easy)
analyze_group("Elite Mode Hard (25%)", elite_hard)

print("\n=== LEAGUE BOSSES ===")
for tier in range(1, 9):
    tier_bosses = [f"league_{b}{tier}" for b in league_bosses]
    analyze_group(f"League Boss Tier {tier}", tier_bosses)

analyze_group("League Boss Tier 9 (Elite)", [f"league_{b}9" for b in tier9_bosses])
