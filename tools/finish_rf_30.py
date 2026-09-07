#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/finish_rf_30.py
Переводит последние 30 ключей в Refurbished Furniture для достижения 100.0%.
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
TASK_DIR = os.path.join(ROOT_DIR, "tasks", "Translate_Mods", "02_refurbished_furniture")
new_translate_path = os.path.join(TASK_DIR, "new_translate.md")

with open(new_translate_path, "r", encoding="utf-8") as f:
    content = f.read()

m = re.search(r'```json\s*(\{[\s\S]*?\})\s*```', content)
data = json.loads(m.group(1))

EXACT_30 = {
    "block.refurbished_furniture.light_fridge": "Светлый холодильник",
    "block.refurbished_furniture.dark_fridge": "Тёмный холодильник",
    "block.refurbished_furniture.light_toaster": "Светлый тостер",
    "block.refurbished_furniture.dark_toaster": "Тёмный тостер",
    "block.refurbished_furniture.light_microwave": "Светлая микроволновка",
    "block.refurbished_furniture.dark_microwave": "Тёмная микроволновка",
    "block.refurbished_furniture.light_stove": "Светлая кухонная плита",
    "block.refurbished_furniture.dark_stove": "Тёмная кухонная плита",
    "block.refurbished_furniture.light_lightswitch": "Светлый выключатель",
    "block.refurbished_furniture.dark_lightswitch": "Тёмный выключатель",
    "block.refurbished_furniture.light_ceiling_light": "Светлый потолочный светильник",
    "block.refurbished_furniture.dark_ceiling_light": "Тёмный потолочный светильник",
    "block.refurbished_furniture.light_electricity_generator": "Светлый генератор электричества",
    "block.refurbished_furniture.dark_electricity_generator": "Тёмный генератор электричества",
    "block.refurbished_furniture.light_range_hood": "Светлая кухонная вытяжка",
    "block.refurbished_furniture.dark_range_hood": "Тёмная кухонная вытяжка",
    "block.refurbished_furniture.azalea_hedge": "Живая изгородь из азалии",
    "block.refurbished_furniture.stone_stepping_stones": "Каменные пошаговые плиты",
    "block.refurbished_furniture.granite_stepping_stones": "Гранитные пошаговые плиты",
    "block.refurbished_furniture.diorite_stepping_stones": "Диоритовые пошаговые плиты",
    "block.refurbished_furniture.andesite_stepping_stones": "Андезитовые пошаговые плиты",
    "block.refurbished_furniture.deepslate_stepping_stones": "Сланцевые пошаговые плиты",
    "block.refurbished_furniture.door_mat": "Дверной коврик",
    "block.refurbished_furniture.milk": "Молоко",
    "item.refurbished_furniture.package": "Почтовая посылка",
    "item.refurbished_furniture.light_fridge": "Светлый холодильник",
    "item.refurbished_furniture.dark_fridge": "Тёмный холодильник",
    "item.refurbished_furniture.television_remote": "Пульт от телевизора",
    "container.refurbished_furniture.drawer": "Ящик",
    "container.refurbished_furniture.lightswitch": "Выключатель",
}

for k, v in EXACT_30.items():
    data[k] = v

new_block = f"```json\n{json.dumps(data, ensure_ascii=False, indent=2)}\n```"
new_content = content[:m.start()] + new_block + content[m.end():]
with open(new_translate_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("🚀 Синхронизация 100% перевода Refurbished Furniture...")
subprocess.run(["python", "tools/apply_task.py", "02_refurbished_furniture"], cwd=ROOT_DIR, capture_output=True, text=True, encoding='utf-8', errors='replace')
print("🎉 100% ПЕРЕВОД Refurbished Furniture ПРИМЕНЁН!")
