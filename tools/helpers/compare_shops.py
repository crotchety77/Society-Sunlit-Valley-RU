import os, json, sys

sys.stdout.reconfigure(encoding='utf-8')

kubejs_dir = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs'

print('=== 1. WANDERER (SHOP) ===')
w_file = os.path.join(kubejs_dir, 'data/society_trading/shops/wanderer.json')
if os.path.exists(w_file):
    w_data = json.load(open(w_file, 'r', encoding='utf-8'))
    for t in w_data.get('trades', []):
        print(t)

print('\n=== 2. TRADER (NPC SHOP) ===')
t_file = os.path.join(kubejs_dir, 'data/society_trading/shops/trader.json')
if os.path.exists(t_file):
    t_data = json.load(open(t_file, 'r', encoding='utf-8'))
    for t in t_data.get('trades', []):
        print(t)

print('\n=== 3. BOOK FAIR (LIBRARIAN 27-28 число) ===')
bf_file = os.path.join(kubejs_dir, 'data/society_trading/shops/book_fair.json')
if os.path.exists(bf_file):
    bf = json.load(open(bf_file, 'r', encoding='utf-8'))
    for t in bf.get('trades', []):
        offer = t.get('offer', {}).get('item')
        req = t.get('request', {})
        stage = t.get('stage_required', '')
        print(f"Offer: {offer} | Cost: {req.get('count')}x {req.get('item')} | Req Stage: {stage}")
