#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/translate_batch_top10.py
Модуль для генерации точных переводов для 10 модов:
1. cluttered
2. refurbished_furniture
3. dramaticdoors
4. simplehats
5. longwings
6. automobility
7. pamhc2trees
8. paraglider
9. beachparty
10. functionalstorage
"""

import re
import json

# ==========================================================
# 1. CLUTTERED
# ==========================================================
def translate_cluttered_key(k, v):
    if v.startswith("TODO: "):
        v = v[6:].strip()
    
    # Tooltips & UI
    if k == "itemGroup.cluttered_tab" or k == "creativetab.cluttered_tab":
        return "Cluttered: Блоки"
    if k == "creativetab.cluttered_furniture_tab":
        return "Cluttered: Мебель и декор"
    if k == "cluttered.storage":
        return "Хранилище"
    if k == "cluttered.fridge":
        return "Холодильник"
    if k == "cluttered.box":
        return "Картонная коробка"
    if k == "cluttered.hand_drill.tooltip":
        return "Используется для смены деталей на определённых блоках.\n§6Shift + ПКМ§7 для вращения блоков.\n§8Текстура: EyeSeeDee§r"
    if k == "cluttered.bouncymushroom.tooltip":
        return "Он пружинит!"
    if k == "cluttered.eye_block.tooltip":
        return "Смотреть в упор неприлично..."
    if k == "cluttered.garland.tooltip":
        return "Можно перемещать влево и вправо с помощью ручной дрели"
    if k == "cluttered.bracket.tooltip":
        return "Можно размещать на заборах"
    if k == "cluttered.polaroid_camera.tooltip":
        return "Попробуйте вставить бумагу!"

    if k.startswith("painting.cluttered."):
        if k.endswith(".author"):
            return v
        p_map = {
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
        return p_map.get(v, v)

    # Ивовое дерево
    if "willow" in k:
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
        if v in w_map:
            return w_map[v]

    # Обработка префикса Luphie's
    name = v
    if name.startswith("Luphie's "):
        name = name[len("Luphie's "):]
    elif name.startswith("Luphie "):
        name = name[len("Luphie "):]

    # Прямые соответствия популярных предметов Cluttered
    direct_cluttered = {
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
        "Hand Drill": "Ручная дрель",
        "Polaroid Camera": "Камера Polaroid",
        "Bouncy Mushroom": "Прыгучий гриб",
        "Glowing Bouncy Mushroom": "Светящийся прыгучий гриб",
    }
    
    if name in direct_cluttered:
        return direct_cluttered[name]
        
    return name


# ==========================================================
# 2. REFURBISHED FURNITURE
# ==========================================================
def translate_refurbished_furniture_key(k, v):
    if v.startswith("TODO: "):
        v = v[6:].strip()
    
    # Регулярные шаблоны для MrCrayfish Refurbished Furniture
    if k.startswith("container.refurbished_furniture."):
        c_map = {
            "freezer": "Морозильник",
            "fridge": "Холодильник",
            "storage_cabinet": "Шкафчик для хранения",
            "kitchen_cabinet": "Кухонный шкафчик",
            "kitchen_drawer": "Кухонный ящик",
            "desk": "Письменный стол",
            "cutting_board": "Разделочная доска",
            "microwave": "Микроволновка",
            "stove": "Кухонная плита",
            "toaster": "Тостер",
            "grill": "Гриль",
            "crate": "Ящик",
            "post_box": "Почтовый ящик",
            "recycle_bin": "Корзина для переработки",
            "mail_box": "Почтовый ящик",
            "workbench": "Верстак плотника",
        }
        for sub, ru in c_map.items():
            if sub in k:
                return ru

    if k.startswith("gui.refurbished_furniture."):
        g_map = {
            "power": "Питание",
            "temperature": "Температура",
            "cooking": "Приготовление",
            "toast": "Поджарить",
            "bake": "Запечь",
            "freeze": "Заморозить",
            "link": "Связать",
            "unlink": "Отвязать",
            "clear": "Очистить",
            "lock": "Заблокировать",
            "unlock": "Разблокировать",
            "open": "Открыть",
            "close": "Закрыть",
        }
        for sub, ru in g_map.items():
            if sub in k:
                return ru

    return v


# ==========================================================
# 3. DRAMATIC DOORS
# ==========================================================
def translate_dramaticdoors_key(k, v):
    if v.startswith("TODO: "):
        v = v[6:].strip()
        
    # Двери и калитки
    # Short <Name> Door -> Низкая <Имя> дверь
    # Tall <Name> Door -> Высокая <Имя> дверь
    # Tall <Name> Fence Gate -> Высокая <Имя> калитка
    # Short <Name> Fence Gate -> Низкая <Имя> калитка
    
    # Парсим структуру
    is_tall = "Tall " in v or k.startswith("block.dramaticdoors.tall_")
    is_short = "Short " in v or k.startswith("block.dramaticdoors.short_")
    is_gate = "Fence Gate" in v or "fence_gate" in k
    
    # Извлекаем основу имени
    base = v.replace("Short ", "").replace("Tall ", "").replace(" Fence Gate", "").replace(" Door", "").strip()
    
    # Склонения древесины / материалов
    adj_map = {
        "Oak": "дубовая",
        "Spruce": "еловая",
        "Birch": "берёзовая",
        "Jungle": "тропическая",
        "Acacia": "акациевая",
        "Dark Oak": "тёмно-дубовая",
        "Mangrove": "мангровая",
        "Cherry": "вишнёвая",
        "Bamboo": "бамбуковая",
        "Crimson": "багровая",
        "Warped": "искажённая",
        "Iron": "железная",
        "Glass": "стеклянная",
        "Pale Oak": "бледно-дубовая",
        "Copper": "медная",
        "Exposed Copper": "потускневшая медная",
        "Weathered Copper": "состаренная медная",
        "Oxidized Copper": "окисленная медная",
        "Waxed Copper": "вощёная медная",
        "Waxed Exposed Copper": "вощёная потускневшая медная",
        "Waxed Weathered Copper": "вощёная состаренная медная",
        "Waxed Oxidized Copper": "вощёная окисленная медная",
        "Maple": "кленовая",
        "Pine": "сосновая",
        "Fir": "пихтовая",
        "Redwood": "секвойевая",
        "Willow": "ивовая",
        "Cypress": "кипарисовая",
        "Ebony": "эбеновая",
        "Mahogany": "красного дерева",
        "Palm": "пальмовая",
        "Jacaranda": "жакарандовая",
        "Aspen": "осиновая",
        "Baobab": "баобабовая",
        "Sakura": "сакуровая",
        "Larch": "лиственничная",
        "Alder": "ольховая",
        "Cedar": "кедровая",
        "Walnut": "ореховая",
        "Chestnut": "каштановая",
    }
    
    # Род для калитки (женский: калитка) и двери (женский: дверь)
    fem_adj = adj_map.get(base, f"{base}")
    if is_gate:
        prefix = "Высокая" if is_tall else ("Низкая" if is_short else "")
        return f"{prefix} {fem_adj} калитка".strip()
    else:
        prefix = "Высокая" if is_tall else ("Низкая" if is_short else "")
        return f"{prefix} {fem_adj} дверь".strip()


# ==========================================================
# 4. SIMPLE HATS
# ==========================================================
def translate_simplehats_key(k, v):
    if v.startswith("TODO: "):
        v = v[6:].strip()
        
    hat_dict = {
        "itemGroup.simplehats": "Simple Hats (Шляпы и аксессуары)",
        "item.simplehats.hatbag_common": "Обычный мешок со шляпой",
        "item.simplehats.hatbag_uncommon": "Необычный мешок со шляпой",
        "item.simplehats.hatbag_rare": "Редкий мешок со шляпой",
        "item.simplehats.hatbag_epic": "Эпический мешок со шляпой",
        "item.simplehats.hatbag_legendary": "Легендарный мешок со шляпой",
        "item.simplehats.hatbag_easter": "Пасхальный мешок со шляпой",
        "item.simplehats.hatbag_summer": "Летний мешок со шляпой",
        "item.simplehats.hatbag_halloween": "Хэллоуинский мешок со шляпой",
        "item.simplehats.hatbag_festive": "Праздничный мешок со шляпой",
        "item.simplehats.hat_scraps": "Обрывки шляпы",
        "item.simplehats.hat_scraps_easter": "Пасхальные обрывки шляпы",
        "item.simplehats.hat_scraps_summer": "Летние обрывки шляпы",
        "item.simplehats.hat_scraps_halloween": "Хэллоуинские обрывки шляпы",
        "item.simplehats.hat_scraps_festive": "Праздничные обрывки шляпы",
        "item.simplehats.special": "Особая шляпа",
    }
    if k in hat_dict:
        return hat_dict[k]
        
    return v


# ==========================================================
# 5. LONGWINGS
# ==========================================================
def translate_longwings_key(k, v):
    if v.startswith("TODO: "):
        v = v[6:].strip()
        
    lw_dict = {
        "itemGroup.longwings": "Longwings (Бабочки и шелкопряды)",
        "item.longwings.butterfly_net": "Сачок для бабочек",
        "item.longwings.caterpillar": "Гусеница",
        "item.longwings.chrysalis": "Куколка",
        "item.longwings.silk_thread": "Шёлковая нить",
        "item.longwings.silk_fabric": "Шёлковая ткань",
        "item.longwings.butterfly_display": "Рамка для бабочек",
        "item.longwings.magnifying_glass": "Лупа",
        "item.longwings.field_guide": "Полевой определитель бабочек",
    }
    if k in lw_dict:
        return lw_dict[k]
        
    return v


# ==========================================================
# 6. AUTOMOBILITY
# ==========================================================
def translate_automobility_key(k, v):
    if v.startswith("TODO: "):
        v = v[6:].strip()
        
    auto_dict = {
        "itemGroup.automobility": "Automobility (Автомобили и транспорт)",
        "item.automobility.crowbar": "Монтировка",
        "item.automobility.wrench": "Гаечный ключ",
        "item.automobility.automobile": "Автомобиль",
        "block.automobility.auto_mechanic_table": "Стол автомеханика",
        "block.automobility.sloped_dash_panel": "Наклонная панель приборов",
        "block.automobility.steep_sloped_dash_panel": "Крутая панель приборов",
        "block.automobility.grass_off_road": "Грунтовая дорога (трава)",
        "block.automobility.dirt_off_road": "Грунтовая дорога (земля)",
        "block.automobility.sand_off_road": "Песчаная дорога",
        "category.automobility": "Automobility",
        "key.automobility.accelerate": "Газ / Ускорение",
        "key.automobility.brake": "Тормоз / Задний ход",
        "key.automobility.steer_left": "Поворот влево",
        "key.automobility.steer_right": "Поворот вправо",
        "key.automobility.drift": "Дрифт",
        "key.automobility.horn": "Клаксон",
    }
    if k in auto_dict:
        return auto_dict[k]
        
    return v


# ==========================================================
# 7. PAMHC2TREES
# ==========================================================
def translate_pamhc2trees_key(k, v):
    if v.startswith("TODO: "):
        v = v[6:].strip()
        
    # Pam's HarvestCraft 2 Trees
    tree_fruits = {
        "apple": "яблочн",
        "banana": "бананов",
        "cherry": "вишнёв",
        "lemon": "лимонн",
        "lime": "лаймов",
        "orange": "апельсинов",
        "peach": "персиков",
        "pear": "грушев",
        "plum": "сливов",
        "avocado": "авокадов",
        "coconut": "кокосов",
        "mango": "мангов",
        "apricot": "абрикосов",
        "fig": "инжирн",
        "grapefruit": "грейпфрутов",
        "papaya": "папайев",
        "persimmon": "хурмов",
        "pomegranate": "гранатов",
        "almond": "миндальн",
        "cashew": "кешью",
        "chestnut": "каштанов",
        "hazelnut": "фундучн",
        "pecan": "пеканов",
        "pistachio": "фисташков",
        "walnut": "орехов",
        "cinnamon": "коричн",
        "maple": "кленов",
        "nutmeg": "мускатн",
        "peppercorn": "перечн",
        "vanilla": "ванильн",
        "breadfruit": "хлебн",
        "guava": "гуавов",
        "jackfruit": "джекфрутов",
        "lychee": "личи",
        "passionfruit": "маракуйев",
        "rambutan": "рамбутанов",
        "tamarind": "тамариндов",
        "dragonfruit": "питахайев",
        "durian": "дурианов",
        "starfruit": "карамбол",
    }
    for sub, ru in tree_fruits.items():
        if sub in k:
            if "sapling" in k:
                return f"Саженец {ru}ого дерева"
            if "item" in k:
                return f"{v}"
                
    return v


# ==========================================================
# 8. PARAGLIDER
# ==========================================================
def translate_paraglider_key(k, v):
    if v.startswith("TODO: "):
        v = v[6:].strip()
        
    para_dict = {
        "itemGroup.paraglider": "Paraglider (Парапланы)",
        "item.paraglider.paraglider": "Параплан",
        "item.paraglider.deku_leaf": "Лист Деку",
        "item.paraglider.heart_container": "Сосуд сердца",
        "item.paraglider.stamina_vessel": "Сосуд выносливости",
        "item.paraglider.spirit_orb": "Сфера духа",
        "item.paraglider.anti_vessel": "Анти-сосуд",
        "item.paraglider.essence": "Эссенция",
        "block.paraglider.goddess_statue": "Статуя Богини",
        "block.paraglider.kakariko_goddess_statue": "Статуя Богини Какарико",
        "block.paraglider.goron_goddess_statue": "Статуя Богини Горонов",
        "block.paraglider.rito_goddess_statue": "Статуя Богини Рито",
        "block.paraglider.horned_statue": "Рогатая статуя",
        "stat.paraglider.stamina": "Запас выносливости",
    }
    if k in para_dict:
        return para_dict[k]
        
    return v


# ==========================================================
# 9. BEACHPARTY
# ==========================================================
def translate_beachparty_key(k, v):
    if v.startswith("TODO: "):
        v = v[6:].strip()
        
    beach_dict = {
        "itemGroup.beachparty": "Beachparty (Пляжный отдых)",
        "item.beachparty.coconut": "Кокос",
        "item.beachparty.coconut_open": "Расколотый кокос",
        "item.beachparty.palm_log": "Пальмовое бревно",
        "item.beachparty.palm_wood": "Пальмовая древесина",
        "item.beachparty.palm_planks": "Пальмовые доски",
        "item.beachparty.palm_leaves": "Пальмовые листья",
        "item.beachparty.palm_sapling": "Саженец пальмы",
        "item.beachparty.deck_chair": "Шезлонг",
        "item.beachparty.beach_chair": "Пляжное кресло",
        "item.beachparty.beach_towel": "Пляжное полотенце",
        "item.beachparty.beach_hat": "Пляжная шляпа",
        "item.beachparty.sunglasses": "Солнцезащитные очки",
        "item.beachparty.swim_trunks": "Плавки",
        "item.beachparty.bikini": "Купальник",
        "item.beachparty.pool_noodle": "Аквапалка (нудл)",
        "item.beachparty.rubber_ring": "Надувной круг",
        "item.beachparty.tiki_bar": "Тики-бар",
        "item.beachparty.tiki_chair": "Барный стул тики",
        "item.beachparty.mini_fridge": "Мини-холодильник",
        "item.beachparty.ice_cream_maker": "Мороженица",
        "item.beachparty.cocktail": "Коктейль",
        "item.beachparty.cocktail_glass": "Бокал для коктейля",
        "item.beachparty.coconut_cocktail": "Кокосовый коктейль",
        "item.beachparty.sweetberry_icecream": "Мороженое из сладких ягод",
        "item.beachparty.chocolate_icecream": "Шоколадное мороженое",
        "item.beachparty.vanilla_icecream": "Ванильное мороженое",
        "item.beachparty.coconut_icecream": "Кокосовое мороженое",
        "item.beachparty.melon_icecream": "Арбузное мороженое",
        "item.beachparty.icecream_cone": "Вафельный рожок",
    }
    if k in beach_dict:
        return beach_dict[k]
        
    return v


# ==========================================================
# 10. FUNCTIONAL STORAGE
# ==========================================================
def translate_functionalstorage_key(k, v):
    if v.startswith("TODO: "):
        v = v[6:].strip()
        
    fs_dict = {
        "itemGroup.functionalstorage": "Functional Storage (Ящики и хранилища)",
        "block.functionalstorage.storage_controller": "Контроллер ящиков",
        "block.functionalstorage.controller_extension": "Расширитель контроллера",
        "block.functionalstorage.armory_cabinet": "Оружейный шкаф",
        "block.functionalstorage.framed_storage_controller": "Каркасный контроллер ящиков",
        "block.functionalstorage.framed_controller_extension": "Каркасный расширитель контроллера",
        "block.functionalstorage.compacting_drawer": "Сжимающий ящик",
        "block.functionalstorage.simple_compacting_drawer": "Простой сжимающий ящик",
        "block.functionalstorage.framed_compacting_drawer": "Каркасный сжимающий ящик",
        "block.functionalstorage.framed_simple_compacting_drawer": "Каркасный простой сжимающий ящик",
        "block.functionalstorage.ender_drawer": "Эндер-ящик",
        "item.functionalstorage.linking_tool": "Инструмент связывания",
        "item.functionalstorage.configuration_tool": "Инструмент настройки",
        "item.functionalstorage.copper_upgrade": "Медное улучшение хранилища",
        "item.functionalstorage.gold_upgrade": "Золотое улучшение хранилища",
        "item.functionalstorage.diamond_upgrade": "Алмазное улучшение хранилища",
        "item.functionalstorage.netherite_upgrade": "Незеритовое улучшение хранилища",
        "item.functionalstorage.iron_downgrade": "Железное понижение хранилища (1 стак)",
        "item.functionalstorage.void_upgrade": "Улучшение аннигиляции (Void)",
        "item.functionalstorage.collector_upgrade": "Улучшение сборщика предметов",
        "item.functionalstorage.puller_upgrade": "Улучшение втягивания предметов",
        "item.functionalstorage.pusher_upgrade": "Улучшение выталкивания предметов",
        "item.functionalstorage.redstone_upgrade": "Редстоун-улучшение",
        "gui.functionalstorage.item": "Предмет:",
        "gui.functionalstorage.amount": "Количество:",
        "gui.functionalstorage.max": "Максимум:",
        "gui.functionalstorage.mode": "Режим:",
        "gui.functionalstorage.linked": "Связано:",
    }
    if k in fs_dict:
        return fs_dict[k]
        
    return v
