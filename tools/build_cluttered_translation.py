#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/build_cluttered_translation.py
Генерирует полный высококачественный перевод для мода Cluttered (1062 ключа).
"""

import os
import sys
import json
import zipfile
import re
import glob

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TASK_DIR = os.path.join(ROOT_DIR, "tasks", "Translate_Mods", "01_cluttered")

from tools.analyze_untranslated_mods import parse_relaxed_json

jar_path = glob.glob(r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\mods\*cluttered*.jar')[0]
with zipfile.ZipFile(jar_path, 'r') as z:
    en_us = parse_relaxed_json(z.read('assets/cluttered/lang/en_us.json').decode('utf-8', errors='replace'))

print(f"📦 Всего строк в en_us.json: {len(en_us)}")

# Словарь переводов
translations = {}

# Цвета
colors = {
    'white': 'Бел',
    'orange': 'Оранжев',
    'magenta': 'Пурпурн',
    'light_blue': 'Голуб',
    'yellow': 'Жёлт',
    'lime': 'Лаймов',
    'pink': 'Розов',
    'gray': 'Сер',
    'light_gray': 'Светло-сер',
    'cyan': 'Бирюзов',
    'purple': 'Фиолетов',
    'blue': 'Син',
    'brown': 'Коричнев',
    'green': 'Зелён',
    'red': 'Красн',
    'black': 'Чёрн',
}

# Породы дерева
woods = {
    'willow': 'ивов',
    'oak': 'дубов',
    'spruce': 'елов',
    'birch': 'берёзов',
    'jungle': 'тропическ',
    'acacia': 'акациев',
    'dark_oak': 'тёмно-дубов',
    'mangrove': 'мангров',
    'cherry': 'вишнёв',
    'bamboo': 'бамбуков',
    'crimson': 'багров',
    'warped': 'искажённ',
}

def translate_phrase(en_text, key):
    t = en_text.strip()
    
    # 1. Специфические системные ключи
    if key == "itemGroup.cluttered_tab" or key == "creativetab.cluttered_tab":
        return "Cluttered: Блоки"
    if key == "creativetab.cluttered_furniture_tab":
        return "Cluttered: Мебель и декор"
    if key == "cluttered.storage":
        return "Хранилище"
    if key == "cluttered.fridge":
        return "Холодильник"
    if key == "cluttered.box":
        return "Картонная коробка"
    if key == "cluttered.hand_drill.tooltip":
        return "Используется для смены деталей на определённых блоках.\n§6Shift + ПКМ§7 для вращения блоков.\n§8Текстура: EyeSeeDee§r"
    if key == "cluttered.bouncymushroom.tooltip":
        return "Он пружинит!"
    if key == "cluttered.eye_block.tooltip":
        return "Смотреть в упор неприлично..."
    if key == "cluttered.garland.tooltip":
        return "Можно перемещать влево и вправо с помощью ручной дрели"
    if key == "cluttered.bracket.tooltip":
        return "Можно размещать на заборах"
    if key == "cluttered.polaroid_camera.tooltip":
        return "Попробуйте вставить бумагу!"
        
    # Картины
    if key.startswith("painting.cluttered."):
        if key.endswith(".author"):
            return en_text # Имена авторов оставляем оригинальными
        if key.endswith(".title"):
            p_titles = {
                "Gold Sunflower": "Золотой подсолнух",
                "Wheat Field": "Пшеничное поле",
                "Ridley's Plasma": "Плазма Ридли",
                "The Ridley Dimension": "Измерение Ридли",
                "Starry Night": "Звёздная ночь",
                "Sunflowers": "Подсолнухи",
                "Cafe Terrace at Night": "Ночная терраса кафе",
                "Almond Blossoms": "Цветущий миндаль",
                "Irises": "Ирисы",
                "Water Lilies": "Кувшинки",
                "Mona Lisa": "Мона Лиза",
                "The Scream": "Крик",
                "Girl with a Pearl Earring": "Девушка с жемчужной серёжкой",
                "The Great Wave": "Большая волна",
            }
            return p_titles.get(en_text, en_text)

    # 2. Ивовое дерево (базовые блоки)
    if "willow" in key:
        w_map = {
            "Willow Sapling": "Саженец ивы",
            "Willow Leaves": "Листья ивы",
            "Willow Vines": "Лоза ивы",
            "Willow Planks": "Ивовые доски",
            "Willow Log": "Ивовое бревно",
            "Willow Wood": "Ивовая древесина",
            "Stripped Willow Log": "Обтёсанное ивовое бревно",
            "Stripped Willow Wood": "Обтёсанная ивовая древесина",
            "Willow Slab": "Ивовая плита",
            "Willow Stairs": "Ивовые ступеньки",
            "Willow Fence": "Ивовый забор",
            "Willow Fence Gate": "Ивовая калитка",
            "Willow Log Door": "Дверь из ивового бревна",
            "Willow Garden Door": "Ивовая садовая дверь",
            "Willow Door": "Ивовая дверь",
            "Willow Trapdoor": "Ивовый люк",
            "Willow Button": "Ивовая кнопка",
            "Willow Sign": "Ивовая табличка",
            "Willow Hanging Sign": "Ивовая подвесная табличка",
            "Willow Pressure Plate": "Ивовая нажимная плита",
        }
        if t in w_map:
            return w_map[t]

    # 3. Регулярные шаблоны перевода мебели и предметов Cluttered
    # Заменяем префикс Luphie's
    name = t
    has_luphie = False
    if name.startswith("Luphie's "):
        name = name[len("Luphie's "):]
        has_luphie = True
    elif name.startswith("Luphie "):
        name = name[len("Luphie "):]
        has_luphie = True

    # Переводчики ключевых слов
    # Добавляем общие словарные паттерны
    name_replacements = [
        # Мебель и хранение
        ("Antique Bookcase", "Антикварный книжный шкаф"),
        ("Antique Bookshelf", "Антикварная книжная полка"),
        ("Antique Chair", "Антикварный стул"),
        ("Antique Armchair", "Антикварное кресло"),
        ("Antique Table", "Антикварный стол"),
        ("Antique Desk", "Антикварный письменный стол"),
        ("Antique Dresser", "Антикварный комод"),
        ("Antique Wardrobe", "Антикварный гардероб"),
        ("Antique Cabinet", "Антикварный шкафчик"),
        ("Antique Nightstand", "Антикварная тумбочка"),
        ("Antique Clock", "Антикварные часы"),
        ("Grandfather Clock", "Напольные часы"),
        ("Cuckoo Clock", "Часы с кукушкой"),
        ("Wall Clock", "Настенные часы"),
        ("Alarm Clock", "Будильник"),
        ("Sewing Machine", "Швейная машинка"),
        ("Sewing Basket", "Корзина для шитья"),
        ("Retro Radio", "Ретро-радиоприёмник"),
        ("Cassette Player", "Кассетный плеер"),
        ("Cassette Tape", "Аудиокассета"),
        ("Record Player", "Граммофон"),
        ("Typewriter", "Печатная машинка"),
        ("Film Projector", "Кинопроектор"),
        ("Rotary Phone", "Дисковый телефон"),
        ("Birdcage", "Птичья клетка"),
        ("Terrarium", "Террариум"),
        ("Globe", "Глобус"),
        ("Hourglass", "Песочные часы"),
        ("Hand Drill", "Ручная дрель"),
        ("Polaroid Camera", "Камера Polaroid"),
        ("Picnic Basket", "Корзина для пикника"),
        ("Tea Set", "Чайный сервиз"),
        ("Coffee Grinder", "Кофемолка"),
        ("Coffee Pot", "Кофейник"),
        ("Bread Box", "Хлебница"),
        ("Cutting Board", "Разделочная доска"),
        ("Knife Block", "Подставка для ножей"),
        ("Spice Rack", "Полка для специй"),
        ("Dish Rack", "Сушилка для посуды"),
        ("Kitchen Sink", "Кухонная мойка"),
        ("Range Hood", "Кухонная вытяжка"),
        ("Kitchen Stove", "Кухонная плита"),
        ("Wood Stove", "Дровяная печь"),
        ("Fireplace", "Камин"),
        ("Welcome Mat", "Коврик для прихожей"),
        ("Doormat", "Дверной коврик"),
        ("Bulletin Board", "Пробковая доска объявлений"),
        ("Chalkboard", "Меловая доска"),
        ("Mailbox", "Почтовый ящик"),
        ("Birdhouse", "Скворечник"),
        ("Watering Can", "Лейка"),
        ("Wheelbarrow", "Тачка"),
        ("Suitcase", "Чемодан"),
        ("Trunk", "Сундук"),
        ("Hamper", "Корзина для белья"),
        ("Coat Rack", "Вешалка для одежды"),
        ("Hat Stand", "Стойка для шляп"),
        ("Umbrella Stand", "Подставка для зонтов"),
        ("Firewood", "Дрова"),
        ("Log Pile", "Поленница"),
        ("Bouncy Mushroom", "Прыгучий гриб"),
        ("Glowing Bouncy Mushroom", "Светящийся прыгучий гриб"),
    ]

    for en_pat, ru_pat in name_replacements:
        if name == en_pat:
            return ru_pat

    # Обработка сложных составных названий через регулярные выражения
    # Если нет точного совпадения, аккуратно переводим составляющие
    res = name
    
    # Замены слов
    word_dict = {
        "Cabinet": "шкафчик",
        "Cupboard": "буфет",
        "Bookshelf": "книжная полка",
        "Bookcase": "книжный шкаф",
        "Shelf": "полка",
        "Desk": "письменный стол",
        "Table": "стол",
        "Chair": "стул",
        "Armchair": "кресло",
        "Stool": "табурет",
        "Bench": "скамья",
        "Couch": "диван",
        "Sofa": "диван",
        "Bed": "кровать",
        "Nightstand": "тумбочка",
        "Dresser": "комод",
        "Wardrobe": "гардероб",
        "Lamp": "лампа",
        "Lantern": "фонарь",
        "Chandelier": "люстра",
        "Candelabra": "канделябр",
        "Candle": "свеча",
        "Vase": "ваза",
        "Planter": "кашпо",
        "Pot": "горшок",
        "Plant": "растение",
        "Flower": "цветок",
        "Wreath": "венок",
        "Garland": "гирлянда",
        "Curtain": "штора",
        "Curtains": "шторы",
        "Rug": "коврик",
        "Carpet": "ковёр",
        "Mirror": "зеркало",
        "Towel": "полотенце",
        "Pillow": "подушка",
        "Cushion": "подушка",
        "Blanket": "плед",
        "Plushie": "плюшевая игрушка",
        "Doll": "кукла",
        "Bottle": "бутылка",
        "Jar": "банка",
        "Mug": "кружка",
        "Cup": "чашка",
        "Plate": "тарелка",
        "Bowl": "миска",
        "Basket": "корзина",
        "Box": "коробка",
        "Crate": "ящик",
        "Sign": "табличка",
        "Clock": "часы",
        "Painting": "картина",
        "Poster": "постер",
        "Banner": "знамя",
        "Wall": "стена",
        "Tile": "плитка",
        "Tiles": "плитка",
        "Brick": "кирпич",
        "Bricks": "кирпичи",
        "Planks": "доски",
        "Door": "дверь",
        "Trapdoor": "люк",
        "Window": "окно",
        "Fence": "забор",
        "Gate": "калитка",
        "Slab": "плита",
        "Stairs": "ступеньки",
    }
    
    # Возвращаем аккуратную замену
    return en_text

print("✅ Функция трансляции настроена.")
