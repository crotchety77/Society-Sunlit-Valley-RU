import json
import os
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

GAME_DIR = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley"
KUBEJS_DIR = os.path.join(GAME_DIR, "kubejs")
SHOP_FILE = os.path.join(KUBEJS_DIR, "data", "society_trading", "shops", "librarian.json")

# Extract translation from game jar files or assets
import zipfile

def extract_mod_lang(mod_jar_pattern):
    import glob
    mods_dir = os.path.join(GAME_DIR, "mods")
    matches = glob.glob(os.path.join(mods_dir, f"*{mod_jar_pattern}*.jar"))
    res = {}
    for jar_path in matches:
        try:
            with zipfile.ZipFile(jar_path, 'r') as z:
                for filename in ['assets/' + mod_jar_pattern + '/lang/ru_ru.json', 'assets/' + mod_jar_pattern + '/lang/en_us.json']:
                    if filename in z.namelist():
                        data = json.loads(z.read(filename).decode('utf-8'))
                        res.update(data)
        except Exception as e:
            pass
    return res

with open(SHOP_FILE, "r", encoding="utf-8") as f:
    shop_data = json.load(f)

trades = shop_data.get("trades", [])

# Load all kubejs assets
assets_dir = os.path.join(KUBEJS_DIR, "assets")
kubejs_langs = {}
if os.path.exists(assets_dir):
    for ns in os.listdir(assets_dir):
        p = os.path.join(assets_dir, ns, "lang", "ru_ru.json")
        if os.path.exists(p):
            try:
                kubejs_langs[ns] = json.load(open(p, encoding='utf-8'))
            except Exception:
                pass

print(f"Total trades: {len(trades)}")
for i, t in enumerate(trades, 1):
    offer = t.get("offer", {})
    item_id = offer.get("item", "")
    cost = t.get("numismatics_cost", 0)
    
    ns, path = item_id.split(":") if ":" in item_id else ("minecraft", item_id)
    
    # 1. Kubejs lang
    k_lang = kubejs_langs.get(ns, {})
    name = k_lang.get(f"item.{ns}.{path}") or k_lang.get(f"block.{ns}.{path}")
    
    # 2. If not found, check mod jar
    if not name:
        jar_lang = extract_mod_lang(ns)
        name = jar_lang.get(f"item.{ns}.{path}") or jar_lang.get(f"block.{ns}.{path}") or jar_lang.get(f"item.minecraft.{path}")
    
    print(f"#{i:02d} | {item_id:<55} | Name: {str(name):<35} | Cost: {cost}")
