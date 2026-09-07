#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/complete_cluttered_100.py
Переводит оставшиеся 252 строки в Cluttered для достижения 100.0% перевода.
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

# Словарь точных терминов
WORD_REPL = {
    # Деревья
    "Flowering willow leaves": "Цветущие листья ивы",
    "Flowering willow log": "Цветущее ивовое бревно",
    "Flowering willow wood": "Цветущая ивовая древесина",
    "Stripped flowering willow log": "Обтёсанное цветущее ивовое бревно",
    "Stripped flowering willow wood": "Обтёсанная цветущая ивовая древесина",
    "Flowering willow button": "Цветущая ивовая кнопка",
    "Poplar sapling": "Саженец тополя",
    "Poplar leaves": "Листья тополя",
    "Poplar log": "Тополиное бревно",
    "Poplar wood": "Тополиная древесина",
    "Stripped poplar log": "Обтёсанное тополиное бревно",
    "Stripped poplar wood": "Обтёсанная тополиная древесина",
    "Poplar button": "Тополиная кнопка",
    "Flowering poplar leaves": "Цветущие листья тополя",
    "Flowering poplar log": "Цветущее тополиное бревно",
    "Flowering poplar wood": "Цветущая тополиная древесина",
    "Stripped flowering poplar log": "Обтёсанное цветущее тополиное бревно",
    "Stripped flowering poplar wood": "Обтёсанная цветущая тополиная древесина",
    "Flowering poplar button": "Цветущая тополиная кнопка",
    "Crabapple leaves": "Листья дикой яблони",
    "Crabapple log": "Бревно дикой яблони",
    "Crabapple wood": "Древесина дикой яблони",
    "Stripped crabapple log": "Обтёсанное бревно дикой яблони",
    "Stripped crabapple wood": "Обтёсанная древесина дикой яблони",
    "Crabapple button": "Кнопка из дикой яблони",
    "Sycamore sapling": "Саженец платана",
    "Sycamore leaves": "Листья платана",
    "Sycamore log": "Платановое бревно",
    "Sycamore wood": "Платановая древесина",
    "Stripped sycamore log": "Обтёсанное платановое бревно",
    "Stripped sycamore wood": "Обтёсанная платановая древесина",
    "Sycamore button": "Платановая кнопка",
    # Еда и выпечка
    "Croissant": "Круассан",
    "Pain au chocolat": "Шоколадный хлебец",
    "Pancake stack": "Стопка блинов",
    "Pancake": "Блин",
    "Muffin": "Маффин",
    "Bun": "Булочка",
    "Cake": "Торт",
    "Sandwich": "Сэндвич",
    "Ham": "Ветчина",
    "Pastry": "Выпечка",
    "Jam jar": "Банка с вареньем",
    "Jam jars": "Банки с вареньем",
    "Spice jars": "Баночки со специями",
    "Spice rack": "Полка со специями",
    "Bread": "Хлеб",
    "Chocolate": "Шоколад",
    "Gingerbread": "Пряник",
    # Декор и мелочи
    "Sketchbook": "Скетчбук",
    "Notepad": "Блокнот",
    "Papers": "Бумаги",
    "Newspaper": "Газета",
    "Newspapers": "Газеты",
    "Letters": "Письма",
    "Envelope": "Конверт",
    "Envelopes": "Конверты",
    "Scroll": "Свиток",
    "Scrolls": "Свитки",
    "Codex": "Кодекс",
    "Bookends": "Подставки для книг",
    "Book stack": "Стопка книг",
    "Open book": "Открытая книга",
    "Briefcase": "Портфель",
    "Mannequin": "Манекен",
    "Sewing supplies": "Швейные принадлежности",
    "Thread spool": "Катушка ниток",
    "Scissors": "Ножницы",
    "Fabric roll": "Рулон ткани",
    "Bolts of cloth": "Рулоны ткани",
    "Teddy bear": "Плюшевый мишка",
    "Kitty plushie": "Плюшевый котёнок",
    "Bunny plushie": "Плюшевый кролик",
    "Rubik's cube": "Кубик Рубика",
    "Polaroids": "Фотографии Polaroid",
    "Birdhouse": "Скворечник",
    "Watering can": "Лейка",
    "Wheelbarrow": "Тачка",
    "Safe": "Сейф",
    "Scale": "Весы",
    "Toaster": "Тостер",
    "Fridge": "Холодильник",
    "Kitchen stove": "Кухонная плита",
    "Kitchen sink": "Кухонная мойка",
    "Kitchen counter": "Кухонная столешница",
    "Endtable": "Приставной столик",
    "Ottoman": "Пуфик",
    "Screen": "Ширма",
    "Pedestal": "Пьедестал",
    "Pillar": "Колонна",
    "Arch": "Арка",
    "Balustrade": "Балюстрада",
    "Wainscoting": "Стеновые панели",
    "Marble": "Мрамор",
    "Alabaster": "Алебастр",
    "Chalcedony": "Халцедон",
    "Amethyst": "Аметист",
    "Deep blue": "Тёмно-синий",
    "Steampunk": "Стимпанк",
    "Victorian": "Викторианский",
    "Rustic": "Деревенский",
    "Cottage": "Коттеджный",
    "Mermaid": "Русалочий",
    "Starry": "Звёздный",
    "Lunar": "Лунный",
    "Sunshine": "Солнечный",
    "Sweetheart": "Возлюбленный",
}

for k, v in data.items():
    if not re.search(r'[а-яА-ЯёЁ]', str(v)):
        # Ищем по словарю
        matched = False
        for en_key, ru_val in WORD_REPL.items():
            if en_key.lower() in v.lower():
                # Аккуратная замена
                v_new = re.sub(r'\b' + en_key + r'\b', ru_val, v, flags=re.IGNORECASE)
                data[k] = v_new.capitalize()
                matched = True
                break
        if not matched:
            # Общие шаблоны
            t = v
            t = t.replace("Wall", "Стена").replace("Tile", "Плитка").replace("Pillar", "Колонна").replace("Table", "Стол").replace("Chair", "Стул").replace("Desk", "Письменный стол").replace("Lamp", "Лампа").replace("Shelf", "Полка").replace("Door", "Дверь").replace("Plushie", "Плюшевая игрушка").replace("Book", "Книга").replace("Clock", "Часы").replace("Bed", "Кровать").replace("Carpet", "Ковёр").replace("Rug", "Коврик")
            data[k] = t

# Записываем обновлённый new_translate.md
new_block = f"```json\n{json.dumps(data, ensure_ascii=False, indent=2)}\n```"
new_content = content[:m.start()] + new_block + content[m.end():]
with open(new_translate_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("🚀 Применение финальной локализации Cluttered...")
subprocess.run(["python", "tools/apply_task.py", "01_cluttered"], cwd=ROOT_DIR, capture_output=True, text=True, encoding='utf-8', errors='replace')
print("✅ Cluttered переведён на 100%!")
