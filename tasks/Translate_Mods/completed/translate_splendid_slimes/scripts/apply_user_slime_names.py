#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Применение утверждённых пользователем имён 24 пород слаймов
"""

import os
import sys
import json

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

TASKS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
ROOT_DIR = os.path.abspath(os.path.join(TASKS_DIR, ".."))
GAME_DIR = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs"
GAME_SPLENDID_RU = os.path.join(GAME_DIR, "assets", "splendid_slimes", "lang", "ru_ru.json")
GAME_SOCIETY_RU = os.path.join(GAME_DIR, "assets", "society", "lang", "ru_ru.json")
LOCAL_SPLENDID_JSON = os.path.join(ROOT_DIR, "translations", "mods", "splendid_slimes.json")
NEW_TRANSLATE_MD = os.path.join(TASKS_DIR, "translate_splendid_slimes", "new_translate.md")
GLOSSARY_MD = os.path.join(ROOT_DIR, "glossary.md")



# 24 утверждённых породы
SLIMES = {
    "all_seeing": "Всевидящий Слайм",
    "bear": "Барни Слайм",
    "bitwise": "Редстоун Слайм",
    "blazing": "Ифритовый Слайм",
    "bony": "Костяной Слайм",
    "boomcat": "Кот-Бум Слайм",
    "dusty": "Песчаный Слайм",
    "ender": "Эндер Слайм",
    "gold": "Золото-рудный Слайм",
    "juicy": "Джусик Слайм",
    "luminous": "Светящийся Слайм",
    "mechanic": "Криэйт Слайм",
    "minty": "Дракон Слайм",
    "orby": "Экспертикус Слайм",
    "phantom": "Фантом Слайм",
    "prisma": "Призмариновый Слайм",
    "puddle": "Бездноглаз Слайм",
    "rotting": "Гниющий Слайм",
    "shulking": "Шалкерный Слайм",
    "slimy": "Розовый слайм",
    "sparkcat": "Искро-Кот Слайм",
    "sweet": "Карамельный Слайм",
    "webby": "Паучок Слайм",
    "weeping": "Плакса Слайм"
}

# 1. Load current translation
with open(LOCAL_SPLENDID_JSON, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 2. Update breed names, plorts, hearts, jars, blocks, entities
for code, name in SLIMES.items():
    data[f"slime.splendid_slimes.{code}"] = name
    data[f"entity.splendid_slimes.{code}_slime"] = name
    data[f"item.splendid_slimes.{code}_plort"] = f"Плорт ({name})"
    data[f"item.splendid_slimes.{code}_slime_heart"] = f"Сердце ({name})"
    data[f"item.splendid_slimes.jarred_{code}_slime"] = f"{name} в банке"
    data[f"block.splendid_slimes.{code}_slime_block"] = f"Слаймовый блок ({name})"

# Ensure custom slimes have descriptions and diets
data["slime.splendid_slimes.dusty.info"] = "Обитает в тенистых пещерах под пустынями, путая и сбивая с толку путников."
data["diet.splendid_slimes.dusty"] = "Кости и останки"

data["slime.splendid_slimes.bear.info"] = "Его плорты используются для создания мягких одеял, погружающих слаймоводов в сладкий сон."
data["diet.splendid_slimes.bear"] = "Мёд и сладости"

data["slime.splendid_slimes.sparkcat.info"] = "Дальний родственник Кота-Бума, переполненный искрящейся энергией. Не способен стать Ларго!"
data["diet.splendid_slimes.sparkcat"] = "Копчёная рыба"

data["slime.splendid_slimes.mechanic.info"] = "Обожает механизмы и шестерни, но пока слишком мал, чтобы крутить их в одиночку."
data["diet.splendid_slimes.mechanic"] = "Металлические слитки и камни"

# 3. Save to local and game
with open(LOCAL_SPLENDID_JSON, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f"✅ Обновлён локальный translations/mods/splendid_slimes.json ({len(data)} ключей)")

with open(GAME_SPLENDID_RU, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f"✅ Записано напрямую в игру: {GAME_SPLENDID_RU}")

# 4. Update new_translate.md
with open(NEW_TRANSLATE_MD, 'r', encoding='utf-8') as f:
    md = f.read()

# Replace JSON block
json_start = md.find("```json\n")
if json_start != -1:
    header = md[:json_start]
    # Update text in header
    slime_list_str = ", ".join([f"*{name}*" for name in SLIMES.values()])
    header = header.replace(
        "*Всевидящий*, *Медвежий*, *Битовый*, *Огненный*, *Костяной*, *Кот-бум*, *Пыльный*, *Эндер*, *Золотой*, *Сочный*, *Светящийся*, *Механический*, *Мятный*, *Сферический*, *Фантомный*, *Призмариновый*, *Слизень-лужица*, *Гниющий*, *Шалкеровый*, *Классический*, *Искрокот*, *Сладкий*, *Паутинный*, *Плачущий*.",
        slime_list_str + "."
    )
    new_md = header + "```json\n" + json.dumps(data, ensure_ascii=False, indent=2) + "\n```\n"
    with open(NEW_TRANSLATE_MD, 'w', encoding='utf-8') as f:
        f.write(new_md)
    print("✅ Обновлён new_translate.md")

print("\n🎉 Все 24 породы слаймов успешно обновлены по новому списку!")
