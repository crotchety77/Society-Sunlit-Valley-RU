import json
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

shop_file = r'G:\curseforge\minecraft\Instances\Society Sunlit Cobblemon\kubejs\data\society_trading\shops\ball_boutique.json'
with open(shop_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Random Set 0 (TMs) and Random Set 1 (Capsules)
r_sets = data.get('random_sets', [])
capsule_set = r_sets[1]

print(f"Capsule Set Config: random_style='{capsule_set.get('random_style')}', rolled_count={capsule_set.get('rolled_count')}")
trades = capsule_set.get('trades', [])
print(f"Total Capsule Offers: {len(trades)}")

# Let's group and display every single capsule type and its 4 quality variants (0, 1, 2, 3)
capsules_by_type = {}
for t in trades:
    offer = t.get('offer', {})
    nbt_str = offer.get('nbt', '{}')
    try:
        nbt = json.loads(nbt_str)
    except:
        nbt = {}
    ctype = nbt.get('type', 'none')
    qfood = nbt.get('quality_food', {})
    quality = qfood.get('quality', 0) if isinstance(qfood, dict) else 0
    if ctype not in capsules_by_type:
        capsules_by_type[ctype] = {}
    capsules_by_type[ctype][quality] = t

quality_names = {
    0: "Regular (No Quality)",
    1: "Silver (Quality 1)",
    2: "Gold (Quality 2)",
    3: "Iridium (Quality 3)"
}

for ctype in sorted(capsules_by_type.keys()):
    print(f"\n=======================================================")
    print(f"CAPSULE TYPE: '{ctype.upper()}'")
    qdict = capsules_by_type[ctype]
    for q in sorted(qdict.keys()):
        t = qdict[q]
        cost = t.get('numismatics_cost')
        req = t.get('request', {})
        req2 = t.get('second_request', {})
        limit = t.get('limit')
        tid = t.get('trade_id')
        req2_item = req2.get('item', 'None')
        req2_count = req2.get('count', 0)
        print(f"  Quality {q} ({quality_names[q]}):")
        print(f"    - Price (Numismatics): {cost:,} coins ({req.get('count')}x {req.get('item')})")
        print(f"    - Second Required Item: {req2_count}x {req2_item}")
        print(f"    - Purchase Limit: {limit}")
        print(f"    - Trade ID: {tid}")
