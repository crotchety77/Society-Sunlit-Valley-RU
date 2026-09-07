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

clean_breeds = {
    "slime.splendid_slimes.all_seeing": "Всевидящий",
    "slime.splendid_slimes.bear": "Барни",
    "slime.splendid_slimes.bitwise": "Редстоун",
    "slime.splendid_slimes.blazing": "Ифритовый",
    "slime.splendid_slimes.bony": "Костяной",
    "slime.splendid_slimes.boomcat": "Кот-Бум",
    "slime.splendid_slimes.dusty": "Пыльный",
    "slime.splendid_slimes.ender": "Эндер",
    "slime.splendid_slimes.gold": "Золотой",
    "slime.splendid_slimes.juicy": "Сочный",
    "slime.splendid_slimes.luminous": "Светящийся",
    "slime.splendid_slimes.mechanic": "Механический",
    "slime.splendid_slimes.minty": "Мятный",
    "slime.splendid_slimes.orby": "Орби",
    "slime.splendid_slimes.phantom": "Фантомный",
    "slime.splendid_slimes.prisma": "Призмариновый",
    "slime.splendid_slimes.puddle": "Лужица",
    "slime.splendid_slimes.rotting": "Гнилой",
    "slime.splendid_slimes.shulking": "Шалкеровый",
    "slime.splendid_slimes.slimy": "Розовый",
    "slime.splendid_slimes.sparkcat": "Искро-Кот",
    "slime.splendid_slimes.sweet": "Сладкий",
    "slime.splendid_slimes.webby": "Паутинный",
    "slime.splendid_slimes.weeping": "Плакса",
    
    "item.splendid_slimes.default_plort": "Обычный",
    "item.splendid_slimes.plort": "%s плорт",
    "item.splendid_slimes.slime_heart": "Сердце слизня: %s"
}

# 1. Update translations/mods/splendid_slimes.json
with open(LOCAL_MOD_JSON, 'r', encoding='utf-8') as f:
    mod_data = json.load(f)

for k, v in clean_breeds.items():
    mod_data[k] = v

with open(LOCAL_MOD_JSON, 'w', encoding='utf-8') as f:
    json.dump(mod_data, f, ensure_ascii=False, indent=2)
print(f"✅ Обновлён {LOCAL_MOD_JSON}")

# 2. Update game ru_ru.json
with open(GAME_MOD_JSON, 'r', encoding='utf-8') as f:
    game_data = json.load(f)

for k, v in clean_breeds.items():
    game_data[k] = v

with open(GAME_MOD_JSON, 'w', encoding='utf-8') as f:
    json.dump(game_data, f, ensure_ascii=False, indent=2)
print(f"✅ Записано в файл игры: {GAME_MOD_JSON}")

# 3. Update new_translate.md
if os.path.exists(NEW_TRANSLATE_MD):
    with open(NEW_TRANSLATE_MD, 'r', encoding='utf-8') as f:
        md = f.read()

    # Update JSON block in new_translate.md
    for k, v in clean_breeds.items():
        pattern = re.compile(rf'"{re.escape(k)}":\s*".*?"')
        md = pattern.sub(f'"{k}": "{v}"', md)

    with open(NEW_TRANSLATE_MD, 'w', encoding='utf-8') as f:
        f.write(md)
    print("✅ new_translate.md синхронизирован (Блок 2 JSON)")

