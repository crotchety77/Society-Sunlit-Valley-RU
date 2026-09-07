import json
import os
import sys

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", ".."))
TASK_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
EN_PATH = os.path.join(TASK_DIR, "en_us_all.json")
RU_MOD_PATH = os.path.join(ROOT_DIR, "translations", "mods", "refurbished_furniture.json")

with open(EN_PATH, "r", encoding="utf-8") as f:
    en = json.load(f)

ru = {}
if os.path.exists(RU_MOD_PATH):
    with open(RU_MOD_PATH, "r", encoding="utf-8") as f:
        ru = json.load(f)

print(f"Total EN keys: {len(en)}")
print(f"Total RU keys: {len(ru)}")

missing = {k: v for k, v in en.items() if k not in ru}
print(f"Missing keys: {len(missing)}")

# Find any keys where ru translation is identical to en or contains English placeholders
untranslated = {}
for k, v in en.items():
    if k in ru:
        ru_val = ru[k]
        if ru_val.strip().lower() == v.strip().lower() and not v.isdigit() and len(v) > 3 and "{" not in v:
            untranslated[k] = (v, ru_val)
        elif "Drawer" in ru_val or "was sliced" in ru_val or "Тропическый" in ru_val or "Dark Дубовый" in ru_val:
            untranslated[k] = (v, ru_val)

print(f"Untranslated / problematic keys: {len(untranslated)}")

for k in list(missing.keys())[:15]:
    print(f"  [MISSING] {k}: {missing[k]}")

for k in list(untranslated.keys())[:15]:
    print(f"  [PROBLEM] {k}: {untranslated[k][0]} -> {untranslated[k][1]}")
