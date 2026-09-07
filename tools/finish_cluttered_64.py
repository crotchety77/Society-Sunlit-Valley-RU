#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/finish_cluttered_64.py
Переводит последние 64 ключа в Cluttered, доводя перевод до 100%.
"""

import os
import sys
import json
import re
import subprocess

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TASK_DIR = os.path.join(ROOT_DIR, "tasks", "Translate_Mods", "01_cluttered")
new_translate_path = os.path.join(TASK_DIR, "new_translate.md")

with open(new_translate_path, "r", encoding="utf-8") as f:
    content = f.read()

m = re.search(r'```json\s*(\{[\s\S]*?\})\s*```', content)
data = json.loads(m.group(1))

EXACT_64 = {
    "block.cluttered.crabapple_sapling": "Саженец дикой яблони",
    "block.cluttered.fluorescent_maple_sapling": "Саженец люминесцентного клёна",
    "block.cluttered.fluorescent_maple_leaves": "Листья люминесцентного клёна",
    "block.cluttered.flowering_fluorescent_maple_leaves": "Цветущие листья люминесцентного клёна",
    "block.cluttered.fluorescent_maple_log": "Бревно люминесцентного клёна",
    "block.cluttered.fluorescent_maple_wood": "Древесина люминесцентного клёна",
    "block.cluttered.stripped_fluorescent_maple_log": "Обтёсанное бревно люминесцентного клёна",
    "block.cluttered.stripped_fluorescent_maple_wood": "Обтёсанная древесина люминесцентного клёна",
    "block.cluttered.fluorescent_maple_button": "Кнопка из люминесцентного клёна",
    "block.cluttered.fly_agaric": "Красный мухомор",
    "block.cluttered.deep_chalcedony_slab": "Плита из глубинного халцедона",
    "block.cluttered.textile_block_stone": "Каменный тканевый блок",
    "block.cluttered.wooden_victorian_bracket_bow": "Деревянный викторианский кронштейн с бантом",
    "block.cluttered.wooden_victorian_bracket_star": "Деревянный викторианский кронштейн со звездой",
    "block.cluttered.gingerbread_bricks_corner": "Пряничный боковой бордюр",
    "block.cluttered.wooden_canterbury_panel": "Деревянная панель «Кентербери»",
    "block.cluttered.wooden_atlantic_panel": "Деревянная панель «Атлантика»",
    "block.cluttered.wooden_alexandria_panel": "Деревянная панель «Александрия»",
    "block.cluttered.wooden_augustine_panel": "Деревянная панель «Августин»",
    "block.cluttered.wicker_block": "Плетёный блок",
    "block.cluttered.chiseled_gold_block": "Резной золотой блок",
    "block.cluttered.eye_block": "Смотрящий блок",
    "block.cluttered.bunny_book_ends": "Подставки для книг «Кролики»",
    "block.cluttered.cat_mugs_cluttered": "Кружки «Котики»",
    "block.cluttered.mushroom_jars": "Баночки с грибами",
    "block.cluttered.paper_pile": "Стопка бумаг",
    "block.cluttered.hanging_plant_pot_grass": "Подвесной горшок с травой",
    "block.cluttered.drying_herbs": "Сушёные травы",
    "block.cluttered.hanging_cloth": "Подвешенная ткань",
    "block.cluttered.animated_flag_rainbow": "Радужный флаг",
    "block.cluttered.animated_flag_lesbian": "Флаг заката",
    "block.cluttered.animated_flag_bisexual": "Розово-синий флаг",
    "block.cluttered.animated_flag_pansexual": "Трёхцветный яркий флаг",
    "block.cluttered.animated_flag_asexual": "Чёрно-фиолетовый флаг",
    "block.cluttered.animated_flag_transgender": "Пастельный трёхцветный флаг",
    "block.cluttered.animated_flag_nonbinary": "Жёлто-белый флаг",
    "block.cluttered.row_of_small_books": "Ряд небольших книг",
    "block.cluttered.traditional_radio": "Традиционный радиоприёмник",
    "block.cluttered.stars_pendant": "Подвеска со звёздами",
    "block.cluttered.moon_pendant": "Подвеска с луной",
    "block.cluttered.caged_bulb": "Лампа в металлической клетке",
    "block.cluttered.bulletin_board_cluttered": "Заполненная доска объявлений",
    "block.cluttered.lovely_love_seat_basic": "Уютный двухместный диванчик",
    "block.cluttered.sweetheart_baking_set_ingredients": "Ингредиенты для выпечки",
    "block.cluttered.jam_jars": "Баночки с вареньем",
    "block.cluttered.brass_key": "Латунный ключ",
    "block.cluttered.card_index": "Картотека",
    "block.cluttered.heavenly_ornamental_array": "Небесная декоративная композиция",
    "block.cluttered.salt_pepper_shakers": "Солонка и перечница",
    "block.cluttered.fabric_bolts": "Рулоны ткани",
    "block.cluttered.stack_of_books": "Стопка книг",
    "block.cluttered.stack_of_books_tall": "Высокая стопка книг",
    "block.cluttered.wine_bottle_rack": "Винная полка",
    "block.cluttered.wine_bottles": "Бутылки вина",
    "block.cluttered.vial_stand": "Подставка для колб",
    "block.cluttered.pineapple": "Декоративный ананас",
    "block.cluttered.pok_ta_pok_hoop": "Кольцо пок-та-пок",
    "block.cluttered.pok_ta_pok_hoop_snakes": "Змеиное кольцо пок-та-пок",
    "block.cluttered.sewing_clutter": "Набор для рукоделия",
    "block.cluttered.rito_wooden_books": "Книги народа Рито",
    "block.cluttered.office_supplies_a": "Канцелярские принадлежности (набор A)",
    "block.cluttered.office_supplies_b": "Канцелярские принадлежности (набор B)",
    "block.cluttered.tarrytown_stove": "Печь Тарритауна",
    "block.cluttered.seltzer_cans": "Баночки с газировкой",
}

for k, v in EXACT_64.items():
    data[k] = v

new_block = f"```json\n{json.dumps(data, ensure_ascii=False, indent=2)}\n```"
new_content = content[:m.start()] + new_block + content[m.end():]
with open(new_translate_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("🚀 Синхронизация 100% перевода Cluttered...")
subprocess.run(["python", "tools/apply_task.py", "01_cluttered"], cwd=ROOT_DIR, capture_output=True, text=True, encoding='utf-8', errors='replace')
print("🎉 100% ПЕРЕВОД Cluttered ПРИМЕНЁН!")
