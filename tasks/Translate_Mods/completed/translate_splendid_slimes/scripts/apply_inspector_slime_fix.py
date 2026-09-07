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

updates = {
    "info.splendid_slimes.slime_inspector": "Анализ состояния слайма",
    "info.splendid_slimes.slime_inspector.all_good": "Ваш слайм весело хлюпает и абсолютно доволен!"
}

# 1. Update translations/mods/splendid_slimes.json
with open(LOCAL_MOD_JSON, 'r', encoding='utf-8') as f:
    local_data = json.load(f)

for k, v in updates.items():
    local_data[k] = v

with open(LOCAL_MOD_JSON, 'w', encoding='utf-8') as f:
    json.dump(local_data, f, ensure_ascii=False, indent=2)
print(f"✅ Обновлён {LOCAL_MOD_JSON}")

# 2. Update game ru_ru.json
with open(GAME_MOD_JSON, 'r', encoding='utf-8') as f:
    game_data = json.load(f)

for k, v in updates.items():
    game_data[k] = v

with open(GAME_MOD_JSON, 'w', encoding='utf-8') as f:
    json.dump(game_data, f, ensure_ascii=False, indent=2)
print(f"✅ Записано в файл игры: {GAME_MOD_JSON}")

# 3. Synchronize new_translate.md
if os.path.exists(NEW_TRANSLATE_MD):
    with open(NEW_TRANSLATE_MD, 'r', encoding='utf-8') as f:
        md = f.read()

    for k, v in updates.items():
        pattern = re.compile(rf'"{re.escape(k)}":\s*".*?"')
        md = pattern.sub(f'"{k}": "{v}"', md)

    with open(NEW_TRANSLATE_MD, 'w', encoding='utf-8') as f:
        f.write(md)
    print(f"✅ Обновлён {NEW_TRANSLATE_MD}")

