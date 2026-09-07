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

# 24 чистых названий пород БЕЗ слова Слайм
pure_breeds = {
    "all_seeing": "Всевидящий",
    "bear": "Барни",
    "bitwise": "Редстоун",
    "blazing": "Ифритовый",
    "bony": "Костяной",
    "boomcat": "Кот-Бум",
    "dusty": "Песчаный",
    "ender": "Эндер",
    "gold": "Золото-рудный",
    "juicy": "Джусик",
    "luminous": "Светящийся",
    "mechanic": "Криэйт",
    "minty": "Дракон",
    "orby": "Экспертикус",
    "phantom": "Фантом",
    "prisma": "Призмариновый",
    "puddle": "Бездноглаз",
    "rotting": "Гниющий",
    "shulking": "Шалкерный",
    "slimy": "Розовый",
    "sparkcat": "Искро-Кот",
    "sweet": "Карамельный",
    "webby": "Паучок",
    "weeping": "Плакса"
}

with open(LOCAL_MOD_JSON, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 1. Update general templates
data["item.splendid_slimes.default_plort"] = "Обычный"
data["item.splendid_slimes.plort"] = "%s плорт"
data["item.splendid_slimes.default_heart"] = "Сердце слизня"
data["item.splendid_slimes.slime_heart"] = "Сердце: %s"
data["item.splendid_slimes.default_slime_item"] = "Слайм в банке"

# 2. Update all breeds and their items
for k, name in pure_breeds.items():
    data[f"slime.splendid_slimes.{k}"] = name
    data[f"item.splendid_slimes.{k}_plort"] = f"{name} плорт"
    data[f"item.splendid_slimes.{k}_slime_heart"] = f"Сердце ({name})"
    data[f"item.splendid_slimes.jarred_{k}_slime"] = f"{name} слайм в банке"
    data[f"block.splendid_slimes.{k}_slime_block"] = f"Слаймовый блок ({name})"
    data[f"entity.splendid_slimes.{k}_slime"] = f"{name} Слайм"

# 3. Write local translations/mods/splendid_slimes.json
with open(LOCAL_MOD_JSON, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f"✅ Обновлён {LOCAL_MOD_JSON}")

# 4. Write game ru_ru.json
with open(GAME_MOD_JSON, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f"✅ Записано в файл игры: {GAME_MOD_JSON}")

# 5. Synchronize new_translate.md
if os.path.exists(NEW_TRANSLATE_MD):
    with open(NEW_TRANSLATE_MD, 'r', encoding='utf-8') as f:
        md = f.read()

    # Replace JSON block in new_translate.md
    json_block = json.dumps(data, ensure_ascii=False, indent=2)
    md = re.sub(r'```json\s*[\s\S]*?\s*```', f'```json\n{json_block}\n```', md)

    with open(NEW_TRANSLATE_MD, 'w', encoding='utf-8') as f:
        f.write(md)
    print(f"✅ Полностью синхронизирован {NEW_TRANSLATE_MD}")

