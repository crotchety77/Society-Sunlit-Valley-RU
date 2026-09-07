#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

ROOT_DIR = r"c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода"
LOCAL_MOD_JSON = os.path.join(ROOT_DIR, "translations", "mods", "splendid_slimes.json")
GAME_MOD_JSON = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\splendid_slimes\lang\ru_ru.json"
NEW_TRANSLATE_MD = os.path.join(ROOT_DIR, "tasks", "Translate_Mods", "translate_splendid_slimes", "new_translate.md")

# 1. Read JSON block directly from new_translate.md
with open(NEW_TRANSLATE_MD, 'r', encoding='utf-8') as f:
    md = f.read()

# Extract JSON from markdown
json_match = re.search(r'```json\s*([\s\S]*?)\s*```', md)
if not json_match:
    print("❌ Не найден блок JSON в new_translate.md!")
    sys.exit(1)

parsed_json = json.loads(json_match.group(1))
print(f"📖 Успешно считано {len(parsed_json)} ключей из new_translate.md")

# Ensure item.splendid_slimes.plort is formatted consistently as "Плорт (%s)" if breeds are full names like "Песчаный Слайм"
# If parsed_json has "item.splendid_slimes.plort": "%s плорт", it would produce "Песчаный Слайм плорт".
# Let's check how individual plorts are written: "item.splendid_slimes.dusty_plort": "Плорт (Песчаный Слайм)"
if parsed_json.get("item.splendid_slimes.plort") == "%s плорт":
    parsed_json["item.splendid_slimes.plort"] = "Плорт (%s)"

# 2. Write to translations/mods/splendid_slimes.json
with open(LOCAL_MOD_JSON, 'w', encoding='utf-8') as f:
    json.dump(parsed_json, f, ensure_ascii=False, indent=2)
print(f"✅ Обновлён {LOCAL_MOD_JSON}")

# 3. Write directly to game ru_ru.json
with open(GAME_MOD_JSON, 'w', encoding='utf-8') as f:
    json.dump(parsed_json, f, ensure_ascii=False, indent=2)
print(f"✅ Записано в файл игры: {GAME_MOD_JSON}")

