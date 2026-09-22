import json
import sys
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

shop_file = r'G:\curseforge\minecraft\Instances\Society Sunlit Cobblemon\kubejs\data\society_trading\shops\ball_boutique.json'
with open(shop_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

print("=== BALL BOUTIQUE SHOP METADATA ===")
print(f"Shop ID: {data.get('shop_id')}")
print(f"Name Key: {data.get('name')}")
print(f"Texture: {data.get('texture')}")
print(f"Stage Required: {data.get('stage_required')}")
print(f"Seasons Required: {data.get('seasons_required')}")
print(f"Selector Weight: {data.get('selector_weight')}")

print("\n=== PERMANENT TRADES ===")
for idx, t in enumerate(data.get('trades', [])):
    offer = t.get('offer', {})
    req = t.get('request', {})
    cost = t.get('numismatics_cost')
    limit = t.get('limit')
    stage = t.get('stage_required')
    print(f"  [{idx+1}] Offer: {offer.get('count', 1)}x {offer.get('item')} | Cost: {cost:,} ({req.get('count')}x {req.get('item')}) | Limit: {limit} | Stage: {stage}")

r_sets = data.get('random_sets', [])
print(f"\n=== RANDOM SETS COUNT: {len(r_sets)} ===")

for s_idx, rs in enumerate(r_sets):
    r_style = rs.get('random_style')
    r_count = rs.get('rolled_count')
    trades = rs.get('trades', [])
    print(f"\n--- Random Set {s_idx}: random_style='{r_style}', rolled_count={r_count}, total_trades={len(trades)} ---")
    
    # Analyze trades inside this set
    items_by_type = defaultdict(lambda: defaultdict(list))
    for t in trades:
        offer = t.get('offer', {})
        item = offer.get('item')
        nbt_str = offer.get('nbt', '{}')
        try:
            nbt = json.loads(nbt_str)
        except:
            nbt = {}
        ctype = nbt.get('type', 'none')
        qfood = nbt.get('quality_food', {})
        quality = qfood.get('quality', 0) if isinstance(qfood, dict) else 0
        items_by_type[item][(ctype, quality)].append(t)
    
    for item_id, variants in sorted(items_by_type.items()):
        print(f"  Item: {item_id} ({len(variants)} type/quality variants)")
        # Show sample variants
        for (ctype, quality), tlist in sorted(variants.items())[:10]:
            t = tlist[0]
            cost = t.get('numismatics_cost')
            req = t.get('request', {})
            req2 = t.get('second_request', {})
            limit = t.get('limit')
            tid = t.get('trade_id')
            req2_str = f" + {req2.get('count')}x {req2.get('item')}" if req2.get('item') else ""
            print(f"    - Type: '{ctype}', Quality: {quality} | Cost: {cost:,} ({req.get('count')}x {req.get('item')}{req2_str}) | Limit: {limit} | ID: {tid}")
        if len(variants) > 10:
            print(f"    ... and {len(variants) - 10} more variants")
