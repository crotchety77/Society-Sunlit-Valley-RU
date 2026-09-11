import os
import re
import json
import zipfile
import glob

# 1. Inspect jar
jar_path = glob.glob(r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\mods\*society_trading*.jar')[0]
with zipfile.ZipFile(jar_path) as z:
    en_jar = json.loads(z.read('assets/society_trading/lang/en_us.json').decode('utf-8'))

print("=== JAR KEYS (assets/society_trading/lang/en_us.json) ===")
for k, v in en_jar.items():
    print(f"{k} => {v}")

# 2. Inspect kubejs/server_scripts/society_trading
game_dir = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\server_scripts\society_trading'
found_keys = set()
for root, dirs, files in os.walk(game_dir):
    for f in files:
        if f.endswith('.js'):
            with open(os.path.join(root, f), 'r', encoding='utf-8') as fl:
                text = fl.read()
                matches = re.findall(r'["\']([a-zA-Z0-9_.-]+\.society_trading\.[a-zA-Z0-9_.-]+)["\']', text)
                found_keys.update(matches)
                matches2 = re.findall(r'["\'](shop\.[a-zA-Z0-9_.-]+)["\']', text)
                found_keys.update(matches2)
                matches3 = re.findall(r'["\'](selector\.[a-zA-Z0-9_.-]+)["\']', text)
                found_keys.update(matches3)

print("\n=== KUBEJS SCRIPT KEYS ===")
for k in sorted(found_keys):
    print(k)

# 3. Check current translations
local_json = r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\translations\buildings\society_trading_building_shop_ru_ru.json'
with open(local_json, 'r', encoding='utf-8') as f:
    local_data = json.load(f)

print("\n=== UNTRANSLATED JAR KEYS ===")
for k, v in en_jar.items():
    if k not in local_data:
        print(f"Missing: {k} = {v}")

print("\n=== UNTRANSLATED KUBEJS KEYS ===")
for k in sorted(found_keys):
    if k not in local_data:
        print(f"Missing: {k}")
