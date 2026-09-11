import json
import os
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

GAME_DIR = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley"
KUBEJS_DIR = os.path.join(GAME_DIR, "kubejs")
SHOP_FILE = os.path.join(KUBEJS_DIR, "data", "society_trading", "shops", "book_fair.json")

# Load society ru_ru
society_ru = json.load(open(os.path.join(KUBEJS_DIR, "assets", "society", "lang", "ru_ru.json"), encoding='utf-8'))
society_skills_ru = json.load(open(os.path.join(KUBEJS_DIR, "assets", "society_skills", "lang", "ru_ru.json"), encoding='utf-8'))

with open(SHOP_FILE, "r", encoding="utf-8") as f:
    shop_data = json.load(f)

trades = shop_data.get("trades", [])

print(f"Total trades: {len(trades)}")
for i, t in enumerate(trades, 1):
    offer = t.get("offer", {})
    item_id = offer.get("item", "")
    cost = t.get("numismatics_cost", 0)
    stage = t.get("stage_required")
    seasons = t.get("seasons_required")
    
    ns, path = item_id.split(":") if ":" in item_id else ("minecraft", item_id)
    name = society_ru.get(f"item.{ns}.{path}") or society_ru.get(f"item.society.{path}") or "???"
    desc = society_ru.get(f"item.{ns}.{path}.description") or society_ru.get(f"item.society.{path}.description") or ""
    
    season_str = f"Сезон: {', '.join(seasons)}" if seasons else "Любой сезон"
    lock_str = f"🔒 [Мастерство: {stage}]" if stage else "🔓 [Доступно на ярмарке]"
    
    print(f"#{i:02d} | {name} (`{item_id}`)")
    print(f"     Доступность: {lock_str} | {season_str} | Цена: {cost} ●")
    print(f"     Описание: {desc}")
    print()
