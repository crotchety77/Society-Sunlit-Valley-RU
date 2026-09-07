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

with open(NEW_TRANSLATE_MD, 'r', encoding='utf-8') as f:
    md = f.read()

# Exact approved breed names mapping
approved_breeds = {
    "slime.splendid_slimes.all_seeing": "Всевидящий Слайм",
    "slime.splendid_slimes.bear": "Барни Слайм",
    "slime.splendid_slimes.bitwise": "Редстоун Слайм",
    "slime.splendid_slimes.blazing": "Ифритовый Слайм",
    "slime.splendid_slimes.bony": "Костяной Слайм",
    "slime.splendid_slimes.boomcat": "Кот-Бум Слайм",
    "slime.splendid_slimes.dusty": "Песчаный Слайм",
    "slime.splendid_slimes.ender": "Эндер Слайм",
    "slime.splendid_slimes.gold": "Золото-рудный Слайм",
    "slime.splendid_slimes.juicy": "Джусик Слайм",
    "slime.splendid_slimes.luminous": "Светящийся Слайм",
    "slime.splendid_slimes.mechanic": "Криэйт Слайм",
    "slime.splendid_slimes.minty": "Дракон Слайм",
    "slime.splendid_slimes.orby": "Экспертикус Слайм",
    "slime.splendid_slimes.phantom": "Фантом Слайм",
    "slime.splendid_slimes.prisma": "Призмариновый Слайм",
    "slime.splendid_slimes.puddle": "Бездноглаз Слайм",
    "slime.splendid_slimes.rotting": "Гниющий Слайм",
    "slime.splendid_slimes.shulking": "Шалкерный Слайм",
    "slime.splendid_slimes.slimy": "Розовый слайм",
    "slime.splendid_slimes.sparkcat": "Искро-Кот Слайм",
    "slime.splendid_slimes.sweet": "Карамельный Слайм",
    "slime.splendid_slimes.webby": "Паучок Слайм",
    "slime.splendid_slimes.weeping": "Плакса Слайм",

    "item.splendid_slimes.default_plort": "Плорт",
    "item.splendid_slimes.default_heart": "Сердце слизня",
    "item.splendid_slimes.default_slime_item": "Слизень в банке",
    "item.splendid_slimes.plort": "Плорт (%s)",
    "item.splendid_slimes.slime_heart": "Сердце (%s)"
}

# 1. Update new_translate.md
for k, v in approved_breeds.items():
    pattern = re.compile(rf'"{re.escape(k)}":\s*".*?"')
    md = pattern.sub(f'"{k}": "{v}"', md)

with open(NEW_TRANSLATE_MD, 'w', encoding='utf-8') as f:
    f.write(md)

# 2. Update local and game json
json_match = re.search(r'```json\s*([\s\S]*?)\s*```', md)
if json_match:
    parsed = json.loads(json_match.group(1))
    for k, v in approved_breeds.items():
        parsed[k] = v

    with open(LOCAL_MOD_JSON, 'w', encoding='utf-8') as f:
        json.dump(parsed, f, ensure_ascii=False, indent=2)
    print(f"✅ Обновлён {LOCAL_MOD_JSON}")

    with open(GAME_MOD_JSON, 'w', encoding='utf-8') as f:
        json.dump(parsed, f, ensure_ascii=False, indent=2)
    print(f"✅ Записано в {GAME_MOD_JSON}")

