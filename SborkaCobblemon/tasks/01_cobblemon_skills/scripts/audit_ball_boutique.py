import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

shop_file = r'G:\curseforge\minecraft\Instances\Society Sunlit Cobblemon\kubejs\data\society_trading\shops\ball_boutique.json'
with open(shop_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Shop ID: {data.get('shop_id')}")
print(f"Name Key: {data.get('name')}")
print(f"Stage Required: {data.get('stage_required')}")
print(f"Seasons Required: {data.get('seasons_required')}")
print(f"Selector Weight: {data.get('selector_weight')}")

trades = data.get('trades', [])
print(f"\nTotal Top-Level Trades/Groups: {len(trades)}")

for idx, trade in enumerate(trades):
    if 'trades' in trade:
        # Group of trades
        group_id = trade.get('group_id', trade.get('trade_id', f'group_{idx}'))
        sub_trades = trade.get('trades', [])
        print(f"\n--- Group {idx}: {group_id} (Count: {len(sub_trades)}) ---")
        for s_idx, st in enumerate(sub_trades):
            offer = st.get('offer', {})
            req = st.get('request', {})
            req2 = st.get('second_request', {})
            cost = st.get('numismatics_cost')
            limit = st.get('limit')
            tid = st.get('trade_id')
            stage = st.get('stage_required')
            nbt = offer.get('nbt', '')
            item = offer.get('item')
            count = offer.get('count', 1)
            print(f"  [{s_idx+1}] {item} x{count} (nbt={nbt}) | Price: {cost} ({req.get('item')} x{req.get('count')}) | Extra: {req2.get('item')} x{req2.get('count')} | Limit: {limit} | Stage: {stage} | ID: {tid}")
    else:
        offer = trade.get('offer', {})
        req = trade.get('request', {})
        req2 = trade.get('second_request', {})
        cost = trade.get('numismatics_cost')
        limit = trade.get('limit')
        tid = trade.get('trade_id')
        stage = trade.get('stage_required')
        nbt = offer.get('nbt', '')
        item = offer.get('item')
        count = offer.get('count', 1)
        print(f"[{idx+1}] {item} x{count} (nbt={nbt}) | Price: {cost} ({req.get('item')} x{req.get('count')}) | Extra: {req2.get('item')} x{req2.get('count')} | Limit: {limit} | Stage: {stage} | ID: {tid}")
