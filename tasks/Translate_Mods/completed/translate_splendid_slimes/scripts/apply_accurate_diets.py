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

# Точные проверенные рационы всех 24 пород из kubejs/data/splendid_slimes/slimes/
accurate_diets = {
    "diet.splendid_slimes.all_seeing": "Овощи",
    "diet.splendid_slimes.bear": "Мёд и соты",
    "diet.splendid_slimes.bitwise": "Сокровища омни-геод",
    "diet.splendid_slimes.blazing": "Приготовленное мясо",
    "diet.splendid_slimes.bony": "Фермерское молоко",
    "diet.splendid_slimes.boomcat": "Сырое и жареное мясо",
    "diet.splendid_slimes.dusty": "Кости и костяная рыба",
    "diet.splendid_slimes.ender": "Драгоценные камни",
    "diet.splendid_slimes.gold": "Консервация и джемы",
    "diet.splendid_slimes.juicy": "Красный виноград",
    "diet.splendid_slimes.luminous": "Маринованные овощи",
    "diet.splendid_slimes.mechanic": "Металлические слитки",
    "diet.splendid_slimes.minty": "Тубабак и трубки",
    "diet.splendid_slimes.orby": "Сушёные продукты",
    "diet.splendid_slimes.phantom": "Кровати",
    "diet.splendid_slimes.prisma": "Любая рыба",
    "diet.splendid_slimes.puddle": "Любая рыба",
    "diet.splendid_slimes.rotting": "Сырое мясо",
    "diet.splendid_slimes.shulking": "Плоды и цветы хоруса",
    "diet.splendid_slimes.slimy": "Лесные и садовые ягоды",
    "diet.splendid_slimes.sparkcat": "Копчёная рыба",
    "diet.splendid_slimes.sweet": "Фрукты",
    "diet.splendid_slimes.webby": "Овощи",
    "diet.splendid_slimes.weeping": "Древесные фрукты",
    "diet.splendid_slimes.default_diet": "Любая еда"
}

# 1. Update translations/mods/splendid_slimes.json
with open(LOCAL_MOD_JSON, 'r', encoding='utf-8') as f:
    local_data = json.load(f)

for k, v in accurate_diets.items():
    local_data[k] = v

with open(LOCAL_MOD_JSON, 'w', encoding='utf-8') as f:
    json.dump(local_data, f, ensure_ascii=False, indent=2)
print(f"✅ Обновлён {LOCAL_MOD_JSON}")

# 2. Update game ru_ru.json
with open(GAME_MOD_JSON, 'r', encoding='utf-8') as f:
    game_data = json.load(f)

for k, v in accurate_diets.items():
    game_data[k] = v

with open(GAME_MOD_JSON, 'w', encoding='utf-8') as f:
    json.dump(game_data, f, ensure_ascii=False, indent=2)
print(f"✅ Записано в файл игры: {GAME_MOD_JSON}")

# 3. Synchronize new_translate.md
if os.path.exists(NEW_TRANSLATE_MD):
    with open(NEW_TRANSLATE_MD, 'r', encoding='utf-8') as f:
        md = f.read()

    for k, v in accurate_diets.items():
        pattern = re.compile(rf'"{re.escape(k)}":\s*".*?"')
        md = pattern.sub(f'"{k}": "{v}"', md)

    with open(NEW_TRANSLATE_MD, 'w', encoding='utf-8') as f:
        f.write(md)
    print(f"✅ Обновлён {NEW_TRANSLATE_MD}")

