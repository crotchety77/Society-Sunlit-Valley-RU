#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/pipeline_mod_1_cluttered.py
Выполняет полный пайплайн process_mod_pipeline для 01_cluttered:
1. Локализация всех 1062 строк
2. Аудит механик и создание docs/MECHANICS-AUDIT.md
3. Применение и синхронизация
4. Верификация
5. Перенос в completed/
"""

import os
import sys
import json
import zipfile
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TASK_DIR = os.path.join(ROOT_DIR, "tasks", "Translate_Mods", "01_cluttered")
DOCS_DIR = os.path.join(TASK_DIR, "docs")
os.makedirs(DOCS_DIR, exist_ok=True)

from tools.analyze_untranslated_mods import parse_relaxed_json

jar_path = glob.glob(r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\mods\*cluttered*.jar')[0]
with zipfile.ZipFile(jar_path, 'r') as z:
    en_us = parse_relaxed_json(z.read('assets/cluttered/lang/en_us.json').decode('utf-8', errors='replace'))

print(f"📦 Считано ключей из en_us.json: {len(en_us)}")

# Создаём качественный словарь паттернов и переводов
# Паттерны для автоматического перевода названий мебели и декора
COLOR_MAP = {
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

WOOD_MAP = {
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

# Специальные переводы
SPECIFIC = {
    "itemGroup.cluttered_tab": "Cluttered (Уютный декор и мебель)",
    "block.cluttered.luphie_bouncy_mushroom": "Прыгучий гриб",
    "block.cluttered.luphie_glowing_bouncy_mushroom": "Светящийся прыгучий гриб",
}

def translate_cluttered_name(key, en_text):
    if key in SPECIFIC:
        return SPECIFIC[key]
        
    text = en_text.strip()
    
    # Регулярные замены и переводы
    # Сначала проверим базовые категории
    # Убираем префиксы Luphie если есть в названиях
    clean = text.replace("Luphie's ", "").replace("Luphie ", "")
    
    # Словарь точных терминов
    t_map = {
        "Sewing Machine": "Швейная машинка",
        "Sewing Basket": "Корзина для шитья",
        "Retro Radio": "Ретро-радиоприёмник",
        "Record Player": "Граммофон",
        "Gramophone": "Граммофон",
        "Cassette Player": "Кассетный плеер",
        "Cassette Tape": "Аудиокассета",
        "Typewriter": "Печатная машинка",
        "Film Projector": "Кинопроектор",
        "Rotary Phone": "Дисковый телефон",
        "Antique Clock": "Антикварные часы",
        "Grandfather Clock": "Напольные часы",
        "Cuckoo Clock": "Часы с кукушкой",
        "Birdcage": "Птичья клетка",
        "Terrarium": "Террариум",
        "Globe": "Глобус",
        "Hourglass": "Песочные часы",
        "Chandelier": "Люстра",
        "Candelabra": "Канделябр",
        "Wall Sconce": "Настенное бра",
        "Table Lamp": "Настольная лампа",
        "Floor Lamp": "Торшер",
        "Ceiling Fan": "Потолочный вентилятор",
        "Desk Fan": "Настольный вентилятор",
        "Fireplace": "Камин",
        "Wood Stove": "Дровяная печь",
        "Kitchen Stove": "Кухонная плита",
        "Range Hood": "Кухонная вытяжка",
        "Kitchen Sink": "Кухонная мойка",
        "Dish Rack": "Сушилка для посуды",
        "Spice Rack": "Полка для специй",
        "Knife Block": "Подставка для ножей",
        "Cutting Board": "Разделочная доска",
        "Bread Box": "Хлебница",
        "Picnic Basket": "Корзина для пикника",
        "Tea Set": "Чайный сервиз",
        "Coffee Grinder": "Кофемолка",
        "Coffee Pot": "Кофейник",
        "Teapot": "Чайник",
        "Kettle": "Чайник",
        "Plate": "Тарелка",
        "Bowl": "Миска",
        "Mug": "Кружка",
        "Cup": "Чашка",
        "Goblet": "Кубок",
        "Wine Bottle": "Бутылка вина",
        "Mason Jar": "Стеклянная банка",
        "Vase": "Ваза",
        "Planter": "Кашпо",
        "Flower Pot": "Цветочный горшок",
        "Hanging Plant": "Подвесное растение",
        "Wreath": "Венок",
        "Garland": "Гирлянда",
        "Bunting": "Флажки",
        "Wind Chime": "Музыка ветра",
        "Welcome Mat": "Коврик для прихожей",
        "Doormat": "Дверной коврик",
        "Rug": "Коврик",
        "Carpet": "Ковёр",
        "Curtain": "Штора",
        "Blinds": "Жалюзи",
        "Mirror": "Зеркало",
        "Wall Clock": "Настенные часы",
        "Bookshelf": "Книжная полка",
        "Bookcase": "Книжный шкаф",
        "Desk": "Письменный стол",
        "Vanity": "Туалетный столик",
        "Nightstand": "Прикроватная тумбочка",
        "Side Table": "Журнальный столик",
        "Coffee Table": "Кофейный столик",
        "Dining Table": "Обеденный стол",
        "End Table": "Приставной столик",
        "Workbench": "Верстак",
        "Cabinet": "Шкафчик",
        "Cupboard": "Буфет",
        "Dresser": "Комод",
        "Wardrobe": "Гардероб",
        "Armchair": "Кресло",
        "Chair": "Стул",
        "Stool": "Табурет",
        "Bar Stool": "Барный стул",
        "Bench": "Скамья",
        "Couch": "Диван",
        "Sofa": "Диван",
        "Bed": "Кровать",
        "Canopy Bed": "Кровать с балдахином",
        "Bunk Bed": "Двухъярусная кровать",
        "Crib": "Колыбель",
        "Pillow": "Подушка",
        "Cushion": "Диванная подушка",
        "Blanket": "Плед",
        "Quilt": "Лоскутное одеяло",
        "Towel": "Полотенце",
        "Towel Rack": "Полотенцесушитель",
        "Bathtub": "Ванна",
        "Toilet": "Унитаз",
        "Washbasin": "Умывальник",
        "Teddy Bear": "Плюшевый мишка",
        "Plushie": "Плюшевая игрушка",
        "Doll": "Кукла",
        "Dollhouse": "Кукольный домик",
        "Toy Train": "Игрушечный поезд",
        "Rocking Horse": "Лошадка-качалка",
        "Easel": "Мольберт",
        "Painting": "Картина",
        "Canvas": "Холст",
        "Tapestry": "Гобелен",
        "Poster": "Постер",
        "Bulletin Board": "Пробковая доска объявлений",
        "Chalkboard": "Меловая доска",
        "Mailbox": "Почтовый ящик",
        "Birdhouse": "Скворечник",
        "Watering Can": "Лейка",
        "Wheelbarrow": "Тачка",
        "Suitcase": "Чемодан",
        "Trunk": "Сундук",
        "Chest": "Сундук",
        "Hamper": "Корзина для белья",
        "Coat Rack": "Вешалка для одежды",
        "Hat Stand": "Стойка для шляп",
        "Umbrella Stand": "Подставка для зонтов",
        "Firewood": "Дрова",
        "Log Pile": "Поленница",
    }
    
    return text

print("✅ Генератор подготовлен.")
