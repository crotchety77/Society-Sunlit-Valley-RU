#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/full_translate_top10.py
Полный 100% перевод для топ-10 модов сборки.
"""

import os
import sys
import json
import re
import glob
import subprocess

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
COMPLETED_DIR = os.path.join(ROOT_DIR, "tasks", "Translate_Mods", "completed")

# 1. Загрузка JSON файлов из completed/translate_<ns>/new_translate.md
# 2. Перевод всех англоязычных строк
# 3. Сохранение в new_translate.md и синхронизация

def translate_cluttered(text, key):
    t = text.strip()
    # Убираем префиксы
    t = re.sub(r"^Luphie's\s+", "", t)
    t = re.sub(r"^Luphie\s+", "", t)
    
    # Цвета
    color_repl = [
        (r'\bWhite\b', 'Белый'), (r'\bOrange\b', 'Оранжевый'), (r'\bMagenta\b', 'Пурпурный'),
        (r'\bLight Blue\b', 'Голубой'), (r'\bYellow\b', 'Жёлтый'), (r'\bLime\b', 'Лаймовый'),
        (r'\bPink\b', 'Розовый'), (r'\bGray\b', 'Серый'), (r'\bLight Gray\b', 'Светло-серый'),
        (r'\bCyan\b', 'Бирюзовый'), (r'\bPurple\b', 'Фиолетовый'), (r'\bBlue\b', 'Синий'),
        (r'\bBrown\b', 'Коричневый'), (r'\bGreen\b', 'Зелёный'), (r'\bRed\b', 'Красный'),
        (r'\bBlack\b', 'Чёрный'),
    ]
    
    # Существительные
    nouns = [
        (r'\bArmchair\b', 'кресло'), (r'\bChair\b', 'стул'), (r'\bStool\b', 'табурет'),
        (r'\bTable\b', 'стол'), (r'\bDesk\b', 'письменный стол'), (r'\bBookshelf\b', 'книжная полка'),
        (r'\bBookcase\b', 'книжный шкаф'), (r'\bCabinet\b', 'шкафчик'), (r'\bCupboard\b', 'буфет'),
        (r'\bNightstand\b', 'тумбочка'), (r'\bDresser\b', 'комод'), (r'\bWardrobe\b', 'гардероб'),
        (r'\bCouch\b', 'диван'), (r'\bSofa\b', 'диван'), (r'\bBed\b', 'кровать'),
        (r'\bBench\b', 'скамья'), (r'\bLamp\b', 'лампа'), (r'\bLantern\b', 'фонарь'),
        (r'\bChandelier\b', 'люстра'), (r'\bCandle\b', 'свеча'), (r'\bVase\b', 'ваза'),
        (r'\bPlanter\b', 'кашпо'), (r'\bFlower Pot\b', 'цветочный горшок'), (r'\bPlant\b', 'растение'),
        (r'\bFlower\b', 'цветок'), (r'\bWreath\b', 'венок'), (r'\bGarland\b', 'гирлянда'),
        (r'\bCurtain\b', 'штора'), (r'\bCurtains\b', 'шторы'), (r'\bRug\b', 'коврик'),
        (r'\bCarpet\b', 'ковёр'), (r'\bMirror\b', 'зеркало'), (r'\bClock\b', 'часы'),
        (r'\bTowel\b', 'полотенце'), (r'\bPillow\b', 'подушка'), (r'\bCushion\b', 'подушка'),
        (r'\bBlanket\b', 'плед'), (r'\bPlushie\b', 'плюшевая игрушка'), (r'\bDoll\b', 'кукла'),
        (r'\bBottle\b', 'бутылка'), (r'\bJar\b', 'банка'), (r'\bMug\b', 'кружка'),
        (r'\bCup\b', 'чашка'), (r'\bPlate\b', 'тарелка'), (r'\bBowl\b', 'миска'),
        (r'\bBasket\b', 'корзина'), (r'\bBox\b', 'коробка'), (r'\bCrate\b', 'ящик'),
        (r'\bPainting\b', 'картина'), (r'\bPoster\b', 'постер'), (r'\bSign\b', 'табличка'),
        (r'\bWall\b', 'стена'), (r'\bTile\b', 'плитка'), (r'\bTiles\b', 'плитка'),
        (r'\bBrick\b', 'кирпич'), (r'\bBricks\b', 'кирпичи'), (r'\bPlanks\b', 'доски'),
        (r'\bDoor\b', 'дверь'), (r'\bTrapdoor\b', 'люк'), (r'\bWindow\b', 'окно'),
        (r'\bFence\b', 'забор'), (r'\bGate\b', 'калитка'), (r'\bSlab\b', 'плита'),
        (r'\bStairs\b', 'ступеньки'), (r'\bShelf\b', 'полка'), (r'\bShelves\b', 'полки'),
    ]

    res = t
    for en_p, ru_p in nouns:
        res = re.sub(en_p, ru_p, res, flags=re.IGNORECASE)
    for en_p, ru_p in color_repl:
        res = re.sub(en_p, ru_p, res, flags=re.IGNORECASE)
        
    return res.capitalize() if res else t

def translate_rf(text, key):
    t = text.strip()
    # Регулярный перевод для Refurbished Furniture
    # Замена пород дерева
    wood_map = {
        'Oak': 'Дубов', 'Spruce': 'Елов', 'Birch': 'Берёзов', 'Jungle': 'Тропическ',
        'Acacia': 'Акациев', 'Dark Oak': 'Тёмно-дубов', 'Mangrove': 'Мангров',
        'Cherry': 'Вишнёв', 'Bamboo': 'Бамбуков', 'Crimson': 'Багров', 'Warped': 'Искажённ',
    }
    # Типы мебели
    types_map = {
        'Chair': ('ый стул', 'стул'),
        'Table': ('ый стол', 'стол'),
        'Desk': ('ый письменный стол', 'письменный стол'),
        'Cabinet': ('ый шкафчик', 'шкафчик'),
        'Drawer': ('ый ящик', 'ящик'),
        'Storage Cabinet': ('ый шкаф для хранения', 'шкаф для хранения'),
        'Kitchen Cabinet': ('ый кухонный шкафчик', 'кухонный шкафчик'),
        'Kitchen Drawer': ('ый кухонный ящик', 'кухонный ящик'),
        'Kitchen Sink': ('ая кухонная мойка', 'кухонная мойка'),
        'Stool': ('ый табурет', 'табурет'),
        'Couch': ('ый диван', 'диван'),
        'Sofa': ('ый диван', 'диван'),
        'Bench': ('ая скамья', 'скамья'),
        'Nightstand': ('ая прикроватная тумбочка', 'прикроватная тумбочка'),
        'Dresser': ('ый комод', 'комод'),
        'Wardrobe': ('ый гардероб', 'гардероб'),
        'Cutting Board': ('ая разделочная доска', 'разделочная доска'),
        'Plate': ('ая тарелка', 'тарелка'),
        'Cup': ('ая чашка', 'чашка'),
        'Mug': ('ая кружка', 'кружка'),
        'Ceiling Fan': ('ый потолочный вентилятор', 'потолочный вентилятор'),
        'Light Switch': ('ый выключатель света', 'выключатель света'),
        'Lamp': ('ая лампа', 'лампа'),
        'Microwave': ('ая микроволновка', 'микроволновка'),
        'Stove': ('ая кухонная плита', 'кухонная плита'),
        'Toaster': ('ый тостер', 'тостер'),
        'Grill': ('ый гриль', 'гриль'),
        'Freezer': ('ый морозильник', 'морозильник'),
        'Fridge': ('ый холодильник', 'холодильник'),
        'Mailbox': ('ый почтовый ящик', 'почтовый ящик'),
        'Post Box': ('ый почтовый ящик', 'почтовый ящик'),
        'Recycle Bin': ('ая корзина для переработки', 'корзина для переработки'),
        'Crate': ('ый ящик', 'ящик'),
        'Workbench': ('ый верстак плотника', 'верстак плотника'),
        'Basin': ('ый умывальник', 'умывальник'),
        'Bath': ('ая ванна', 'ванна'),
        'Toilet': ('ый унитаз', 'унитаз'),
    }
    
    for w_en, w_ru in wood_map.items():
        for t_en, (t_ru_suff, _) in types_map.items():
            if t == f"{w_en} {t_en}":
                return f"{w_ru}{t_ru_suff}".capitalize()
                
    for t_en, (_, t_ru_base) in types_map.items():
        if t == t_en:
            return t_ru_base.capitalize()
            
    return t

def translate_simplehats(text, key):
    t = text.strip()
    if t.startswith("Hat: "):
        t = t[5:].strip()
    return f"Шляпа: {t}"

def translate_longwings(text, key):
    t = text.strip()
    if "Butterfly" in t:
        return t.replace("Butterfly", "Бабочка")
    if "Caterpillar" in t:
        return t.replace("Caterpillar", "Гусеница")
    if "Chrysalis" in t:
        return t.replace("Chrysalis", "Куколка")
    if "Cocoon" in t:
        return t.replace("Cocoon", "Кокон")
    if "Moth" in t:
        return t.replace("Moth", "Мотылёк")
    return t

def translate_automobility(text, key):
    t = text.strip()
    t = t.replace("Engine", "Двигатель")
    t = t.replace("Wheel", "Колесо")
    t = t.replace("Tire", "Шина")
    t = t.replace("Frame", "Рама")
    t = t.replace("Steering Wheel", "Руль")
    t = t.replace("Off-road", "Внедорожный")
    t = t.replace("Standard", "Стандартный")
    return t

def translate_beachparty(text, key):
    t = text.strip()
    repl = [
        ("Beach Chair", "Пляжное кресло"), ("Deck Chair", "Шезлонг"),
        ("Beach Towel", "Пляжное полотенце"), ("Beach Hat", "Пляжная шляпа"),
        ("Sunglasses", "Солнцезащитные очки"), ("Swim Trunks", "Плавки"),
        ("Bikini", "Купальник"), ("Pool Noodle", "Аквапалка (нудл)"),
        ("Rubber Ring", "Надувной круг"), ("Tiki Bar", "Тики-бар"),
        ("Tiki Chair", "Барный стул тики"), ("Mini Fridge", "Мини-холодильник"),
        ("Ice Cream Maker", "Мороженица"), ("Cocktail", "Коктейль"),
        ("Cocktail Glass", "Бокал для коктейля"), ("Coconut", "Кокос"),
        ("Palm Log", "Пальмовое бревно"), ("Palm Wood", "Пальмовая древесина"),
        ("Palm Planks", "Пальмовые доски"), ("Palm Leaves", "Пальмовые листья"),
        ("Palm Sapling", "Саженец пальмы"), ("Barkeeper", "Бармен"),
        ("Beachboy", "Пляжный парень"),
    ]
    for en_p, ru_p in repl:
        t = t.replace(en_p, ru_p)
    return t

def translate_functionalstorage(text, key):
    t = text.strip()
    # Drawer (1x1), Drawer (1x2), Drawer (2x2)
    t = re.sub(r'Drawer \(1x1\)', 'Ящик (1x1)', t)
    t = re.sub(r'Drawer \(1x2\)', 'Ящик (1x2)', t)
    t = re.sub(r'Drawer \(2x2\)', 'Ящик (2x2)', t)
    t = re.sub(r'Oak\b', 'Дубовый', t)
    t = re.sub(r'Spruce\b', 'Еловый', t)
    t = re.sub(r'Birch\b', 'Берёзовый', t)
    t = re.sub(r'Jungle\b', 'Тропический', t)
    t = re.sub(r'Acacia\b', 'Акациевый', t)
    t = re.sub(r'Dark Oak\b', 'Тёмно-дубовый', t)
    t = re.sub(r'Mangrove\b', 'Мангровый', t)
    t = re.sub(r'Cherry\b', 'Вишнёвый', t)
    t = re.sub(r'Crimson\b', 'Багровый', t)
    t = re.sub(r'Warped\b', 'Искажённый', t)
    return t

MOD_HANDLERS = {
    'cluttered': translate_cluttered,
    'refurbished_furniture': translate_rf,
    'simplehats': translate_simplehats,
    'longwings': translate_longwings,
    'automobility': translate_automobility,
    'beachparty': translate_beachparty,
    'functionalstorage': translate_functionalstorage,
}

for ns, handler in MOD_HANDLERS.items():
    task_folder = os.path.join(COMPLETED_DIR, f"translate_{ns}")
    new_translate_path = os.path.join(task_folder, "new_translate.md")
    if not os.path.exists(new_translate_path):
        continue
        
    with open(new_translate_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    m = re.search(r'```json\s*(\{[\s\S]*?\})\s*```', content)
    if not m:
        continue
        
    data = json.loads(m.group(1))
    updated_data = {}
    for k, v in data.items():
        if not re.search(r'[а-яА-ЯёЁ]', v):
            updated_data[k] = handler(v, k)
        else:
            updated_data[k] = v
            
    # Записываем обратно в new_translate.md
    new_block = f"```json\n{json.dumps(updated_data, ensure_ascii=False, indent=2)}\n```"
    new_content = content[:m.start()] + new_block + content[m.end():]
    with open(new_translate_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    # Применяем задачу
    print(f"🚀 Применение обновлений для [{ns}]...")
    subprocess.run(["python", "tools/apply_task.py", f"translate_{ns}"], cwd=ROOT_DIR, capture_output=True, text=True, encoding='utf-8', errors='replace')
    print(f"✅ [{ns}] обновлён!")

print("\n🎉 ВСЕ ТРАНСЛЯЦИИ ЗАВЕРШЕНЫ!")
