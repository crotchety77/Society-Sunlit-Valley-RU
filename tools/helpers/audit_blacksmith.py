import os
import json

shops_file = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\data\society_trading\shops\blacksmith.json"
ru_society = r"c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\translations\society\ru_ru.json"
en_society = r"c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\translations\society\en_us.json"
tooltips_js = r"c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\game_data\client_scripts\tooltips\addTooltips.js"

with open(ru_society, "r", encoding="utf-8") as f:
    ru_dict = json.load(f)
with open(en_society, "r", encoding="utf-8") as f:
    en_dict = json.load(f)
with open(shops_file, "r", encoding="utf-8") as f:
    shop_data = json.load(f)

print(f"=== АУДИТ ТОВАРОВ КУЗНЕЦА (Blacksmith) ===")
print(f"Всего сделок: {len(shop_data.get('trades', []))}\n")

for idx, trade in enumerate(shop_data.get("trades", []), 1):
    offer = trade.get("offer", {})
    item_id = offer.get("item")
    count = offer.get("count", 1)
    tag = offer.get("tag")
    
    cost_numi = trade.get("numismatics_cost")
    req = trade.get("request", {})
    req_item = req.get("item")
    req_count = req.get("count", 1)
    
    sec_req = trade.get("second_request", {})
    sec_item = sec_req.get("item")
    sec_count = sec_req.get("count", 1)
    
    stage = trade.get("stage_required", "")
    
    print(f"[{idx}] Предмет: {item_id} (x{count})")
    if tag:
        print(f"    NBT Tag: {tag}")
    print(f"    Цена: {cost_numi} монет | Требует: {req_count}x {req_item}" + (f" + {sec_count}x {sec_item}" if sec_item else "") + (f" [Этап: {stage}]" if stage else ""))
