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

# Ключи, в которых оставляем "слизень":
# block.splendid_slimes.slime_feeder -> Кормушка для слизней
# block.splendid_slimes.slime_incubator -> Инкубатор слизней
# block.splendid_slimes.corral_block -> Блок загона для слизней
# item.splendid_slimes.default_heart -> Сердце слизня
# info.splendid_slimes.slime_heart -> Поместите в инкубатор для выведения слизня

# Во всех остальных ключах переводим на "слайм":
slime_replacements = {
    "block.splendid_slimes.slime_spawner": "Рассадник слаймов",
    "block.splendid_slimes.slime_spawner.slime_count": "Количество слаймов: %s",
    "config.jade.plugin_splendid_slimes.splendid_slime": "Слаймы Splendid Slimes",
    "key.categories.splendid_slimes": "Великолепные слаймы",
    "info.splendid_slimes.slime_inspector.suffocating": "Слайм задыхается! Ему не хватает воздуха!",
    "info.splendid_slimes.slime_inspector.crowded": "В загоне слишком тесно! Слайму нужно больше пространства.",
    "info.splendid_slimes.slime_inspector.aquatic_failure": "Водный слайм страдает без воды!",
    "info.splendid_slimes.slime_inspector.diverse_failure": "Слайму одиноко! Ему нужны соседи других пород.",
    "info.splendid_slimes.slime_inspector.not_happy": "Ваш слайм крайне недоволен условиями жизни...",
    "itemGroup.splendid_slimes": "«Великолепные слаймы»",
    "slime.splendid_slimes.blazing.info": "Эти слаймы холодны на ощупь и черпают всё своё тепло исключительно из окружающей среды.",
    "slime.splendid_slimes.boomcat.info": "Самый популярный домашний слайм. Также главный виновник разбитых мензурок и посуды.",
    "slime.splendid_slimes.gold.info": "Эти слаймы всем сердцем тоскуют по глубоким золотым шахтам...",
    "slime.splendid_slimes.phantom.info": "Счастливые слаймы часто забирают плохие сны у тех, кто спит рядом с ними.",
    "slime.splendid_slimes.prisma.info": "Более упругий родственник слайма-лужицы, неравнодушный к ярким морским цветам.",
    "slime.splendid_slimes.shulking.info": "Приручённых шалкеровых слаймов часто используют спасатели для подъёма завалов.",
    "slime.splendid_slimes.slimy.info": "Самый базовый и дружелюбный слайм. Идеален для начинающих слаймоводов!",
    "trait.splendid_slimes.largoless.info": "Не может превратиться в Ларго. Его плорты не создают гибридов из других слаймов.",
    "trait.splendid_slimes.diverse.info": "Расстраивается, если рядом с ним нет как минимум 3 уникальных видов других слаймов.",
    "splendid_slimes.advancement.obtain_corral.title": "Загон для слаймов",
    "splendid_slimes.advancement.obtain_corral.description": "Используйте блоки загона, чтобы удерживать слаймов",
    "splendid_slimes.advancement.obtain_incubator.title": "Рождение слайма",
    "splendid_slimes.advancement.obtain_incubator.description": "Создайте инкубатор, чтобы вырастить слайма из сердца",
    "splendid_slimes.advancement.obtain_plort.description": "Покормите слайма и соберите плорт",
    "splendid_slimes.advancement.obtain_press.description": "Создайте пресс плортов, чтобы спрессовать сердце слайма",
    "splendid_slimes.advancement.obtain_feeder.description": "Создайте кормушку для автоматического кормления слаймов со сложным рационом",
    "splendid_slimes.advancement.root.title": "Великолепные слаймы",
    "splendid_slimes.advancement.root.description": "Разведение слаймов ради ценных ресурсов!",
    "jei.splendid_slimes.category.slime_info": "Информация о слаймах",
    "jei.splendid_slimes.category.slime_incubating": "Инкубация слаймов",
    "jei.splendid_slimes.category.slime_traits": "Черты слаймов",
    "jei.splendid_slimes.category.slime_traits.none": "У слайма нет особых черт"
}

# 1. Update translations/mods/splendid_slimes.json
with open(LOCAL_MOD_JSON, 'r', encoding='utf-8') as f:
    local_data = json.load(f)

for k, v in slime_replacements.items():
    local_data[k] = v

with open(LOCAL_MOD_JSON, 'w', encoding='utf-8') as f:
    json.dump(local_data, f, ensure_ascii=False, indent=2)
print(f"✅ Обновлён {LOCAL_MOD_JSON}")

# 2. Update game ru_ru.json
with open(GAME_MOD_JSON, 'r', encoding='utf-8') as f:
    game_data = json.load(f)

for k, v in slime_replacements.items():
    game_data[k] = v

with open(GAME_MOD_JSON, 'w', encoding='utf-8') as f:
    json.dump(game_data, f, ensure_ascii=False, indent=2)
print(f"✅ Записано в файл игры: {GAME_MOD_JSON}")

# 3. Synchronize new_translate.md
if os.path.exists(NEW_TRANSLATE_MD):
    with open(NEW_TRANSLATE_MD, 'r', encoding='utf-8') as f:
        md = f.read()

    for k, v in slime_replacements.items():
        pattern = re.compile(rf'"{re.escape(k)}":\s*".*?"')
        md = pattern.sub(f'"{k}": "{v}"', md)

    with open(NEW_TRANSLATE_MD, 'w', encoding='utf-8') as f:
        f.write(md)
    print(f"✅ Обновлён {NEW_TRANSLATE_MD}")
