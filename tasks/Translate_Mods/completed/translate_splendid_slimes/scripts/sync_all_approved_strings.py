#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

ROOT_DIR = r"c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода"
P_JSON = os.path.join(ROOT_DIR, "translations", "mods", "splendid_slimes.json")
P_MD = os.path.join(ROOT_DIR, "tasks", "Translate_Mods", "translate_splendid_slimes", "new_translate.md")
GAME_JSON = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\splendid_slimes\lang\ru_ru.json"

with open(P_JSON, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Update all approved final terms
data["item.splendid_slimes.slime_heart"] = "Сердце слизня: %s"
data["item.splendid_slimes.slime_vac"] = "Вакуумный сборщик (Слаймопушка)"
data["item.splendid_slimes.slime_inspector"] = "Анализатор слаймов"
data["item.splendid_slimes.rocket_pod"] = "Капсула для реактивного прыжка"
data["block.splendid_slimes.rocket_pod"] = "Капсула для реактивного прыжка"

with open(P_JSON, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open(GAME_JSON, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open(P_MD, 'r', encoding='utf-8') as f:
    md = f.read()

json_start = md.find('```json\n')
if json_start != -1:
    header = md[:json_start]
    # Synchronize visual section if present
    header = header.replace('Слаймовый вакуумник (Слаймопушка)', 'Вакуумный сборщик (Слаймопушка)')
    header = header.replace('Анализатор слизней', 'Анализатор слаймов')
    header = header.replace('Ракетная грузовая капсула', 'Капсула для реактивного прыжка')
    new_md = header + '```json\n' + json.dumps(data, ensure_ascii=False, indent=2) + '\n```\n'
    with open(P_MD, 'w', encoding='utf-8') as f:
        f.write(new_md)

print("Все файлы успешно синхронизированы!")
