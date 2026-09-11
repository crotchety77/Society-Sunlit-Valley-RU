import json
import os
import sys
import zipfile
import glob

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

GAME_DIR = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley"
KUBEJS_DIR = os.path.join(GAME_DIR, "kubejs")
SHOP_FILE = os.path.join(KUBEJS_DIR, "data", "society_trading", "shops", "librarian.json")
MODS_DIR = os.path.join(GAME_DIR, "mods")

# Extract all ru_ru from jar files
jar_ru = {}
for j in glob.glob(os.path.join(MODS_DIR, "*.jar")):
    try:
        with zipfile.ZipFile(j, 'r') as z:
            for f in z.namelist():
                if f.startswith("assets/") and f.endswith("/lang/ru_ru.json"):
                    ns = f.split("/")[1]
                    data = json.loads(z.read(f).decode('utf-8'))
                    if ns not in jar_ru:
                        jar_ru[ns] = {}
                    jar_ru[ns].update(data)
    except Exception:
        pass

# KubeJS lang overrides
kubejs_ru = {}
assets_dir = os.path.join(KUBEJS_DIR, "assets")
if os.path.exists(assets_dir):
    for ns in os.listdir(assets_dir):
        p = os.path.join(assets_dir, ns, "lang", "ru_ru.json")
        if os.path.exists(p):
            try:
                kubejs_ru[ns] = json.load(open(p, encoding='utf-8'))
            except Exception:
                pass

with open(SHOP_FILE, "r", encoding="utf-8") as f:
    shop_data = json.load(f)

trades = shop_data.get("trades", [])

# Builtin minecraft ru_ru
vanilla_ru = {
    "minecraft:name_tag": "Бирка",
    "minecraft:book": "Книга",
    "create:wrench": "Гаечный ключ",
}

print(f"Total trades: {len(trades)}")
for i, t in enumerate(trades, 1):
    offer = t.get("offer", {})
    item_id = offer.get("item", "")
    cost = t.get("numismatics_cost", 0)
    stage = t.get("stage_required", None)
    
    ns, path = item_id.split(":") if ":" in item_id else ("minecraft", item_id)
    
    name = (
        kubejs_ru.get(ns, {}).get(f"item.{ns}.{path}") or
        kubejs_ru.get(ns, {}).get(f"block.{ns}.{path}") or
        jar_ru.get(ns, {}).get(f"item.{ns}.{path}") or
        jar_ru.get(ns, {}).get(f"block.{ns}.{path}") or
        vanilla_ru.get(item_id) or
        "???"
    )
    
    lock_badge = f"🔒 [Мастерство: {stage}]" if stage else "🔓 [Доступно сразу]"
    print(f"#{i:02d} | {lock_badge:<30} | {item_id:<55} | {name:<40} | Cost: {cost}")
