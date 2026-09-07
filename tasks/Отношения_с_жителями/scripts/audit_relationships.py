# -*- coding: utf-8 -*-
"""
Скрипт аудита отношений с жителями, наград за 5 сердец и предпочтений в подарках
для сборки Society: Sunlit Valley.
"""
import os
import json
import glob

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
GAME_KUBEJS = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs"
TASK_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# 1. Загрузка всех словарей переводов для красивого отображения названий предметов
lang_dict = {}

# Загружаем из локального проекта
for fpath in glob.glob(os.path.join(PROJECT_ROOT, "translations", "**", "*.json"), recursive=True):
    try:
        with open(fpath, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, dict):
                lang_dict.update(data)
    except Exception as e:
        pass

# Загружаем из игровых ассетов
for fpath in glob.glob(os.path.join(GAME_KUBEJS, "assets", "*", "lang", "ru_ru.json")):
    try:
        with open(fpath, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, dict):
                lang_dict.update(data)
    except Exception as e:
        pass

# Загружаем сырые дампы
raw_ru = os.path.join(PROJECT_ROOT, "game_data", "raw_lang", "ru_ru.json")
if os.path.exists(raw_ru):
    with open(raw_ru, "r", encoding="utf-8") as f:
        lang_dict.update(json.load(f))

# Ручной маппинг для предметов и тегов, если нет в словарях
MANUAL_NAMES = {
    "#minecraft:flowers": "Любые цветы (#minecraft:flowers)",
    "#forge:raw_meat": "Любое сырое мясо (#forge:raw_meat)",
    "#minecraft:fishes": "Любая рыба (#minecraft:fishes)",
    "#society:mineral": "Любые минералы (#society:mineral)",
    "#society:dish": "Любые готовые блюда (#society:dish)",
    "#society:farmer_product": "Любая продукция фермы (#society:farmer_product)",
    "#forge:raw_materials": "Любые сырые руды / материалы (#forge:raw_materials)",
    "#gamediscs:game_discs": "Любые игровые диски (#gamediscs:game_discs)",
    "#society:raw_logs": "Любая необработанная древесина / брёвна (#society:raw_logs)",
    "#vinery:red_wine": "Любое красное вино (#vinery:red_wine)",
    "#vinery:white_wine": "Любое белое вино (#vinery:white_wine)",
    "#society:clothing": "Любая одежда (#society:clothing)",
    "#society:eldritch": "Предметы потусторонней магии / древности (#society:eldritch)",
    "#etcetera:sweaters": "Любые свитера (#etcetera:sweaters)",
    "#etcetera:hats": "Любые шляпы (#etcetera:hats)",
    "#forge:gems": "Любые драгоценные камни (#forge:gems)",
    "#society:pristine_mineral": "Безупречные минералы (#society:pristine_mineral)",
    "minecraft:rabbit_foot": "Кроличья лапка",
    "minecraft:totem_of_undying": "Тотем бессмертия",
    "minecraft:heart_of_the_sea": "Сердце моря",
    "minecraft:nautilus_shell": "Раковина наутилуса",
    "minecraft:echo_shard": "Осколок эха",
    "minecraft:dragon_head": "Голова дракона",
    "minecraft:dragon_egg": "Яйцо дракона",
    "minecraft:nether_star": "Звезда Незера",
    "minecraft:poisonous_potato": "Ядовитый картофель",
    "minecraft:pufferfish": "Иглобрюх",
    "minecraft:warped_fungus": "Искажённый гриб",
    "minecraft:crimson_fungus": "Багровый гриб",
    "minecraft:popped_chorus_fruit": "Приготовленный плод хоруса",
    "#minecraft:decorated_pot_sherds": "Любые глиняные черепки (#minecraft:decorated_pot_sherds)",
    "trials:heavy_core": "Тяжёлый сердечник (Heavy Core)",
    "trials:ominous_bottle": "Зловещий флакон (Ominous Bottle)",
    "trials:trial_key": "Ключ испытаний",
    "trials:trial_key_ominous": "Зловещий ключ испытаний",
    "snuffles:frosty_fluff": "Морозный пух",
    "botania:black_lotus": "Чёрный лотос",
    "crittersandcompanions:clam": "Моллюск",
    "crittersandcompanions:dragonfly_wing": "Крыло стрекозы",
    "unusualfishmod:cooked_aero_mono_stick": "Жареная рыба-моно на палочке",
    "meadow:goat_cheese_block": "Блок козьего сыра",
    "meadow:piece_of_goat_cheese": "Кусочек козьего сыра",
    "windswept:lavender": "Лаванда",
    "windswept:goat_stew": "Рагу из козлятины",
    "windswept:elder_feather": "Перо старейшины",
    "windswept:holly_berries": "Ягоды падуба",
    "bakery:hazelnut_ella": "Ореховая паста",
    "pamhc2trees:hazelnutitem": "Фундук",
    "pamhc2trees:roastedhazelnutitem": "Жареный фундук",
    "candlelight:beef_wellington": "Говядина «Веллингтон»",
    "wildernature:bison_horn": "Рог бизона",
    "veggiesdelight:rice_and_vegetables": "Рис с овощами",
    "autumnity:foul_berries": "Вонючие ягоды",
    "crabbersdelight:jar_of_pickles": "Банка солений",
    "crabbersdelight:sea_pickle_juice": "Сок морского огурца",
    "crabbersdelight:pearl": "Жемчужина",
    "crabbersdelight:pearl_block": "Блок жемчуга",
    "crabbersdelight:kelp_shake": "Коктейль из ламинарии",
    "aquaculture:tin_can": "Консервная банка",
    "aquaculture:box": "Рыболовная коробка",
    "netherdepthsupgrade:lava_pufferfish": "Лавовый иглобрюх",
    "netherdepthsupgrade:eyeball_fish": "Рыба-глаз",
    "netherdepthsupgrade:bonefish": "Рыба-кость",
    "netherdepthsupgrade:wither_bonefish": "Иссушающая рыба-кость",
    "farmersdelight:rotten_tomato": "Гнилой помидор",
    "farmersdelight:straw": "Солома",
    "farmersdelight:nether_salad": "Незеритовый салат",
    "vintagedelight:deluxe_granola_bar": "Гранола-батончик «Делюкс»",
    "vintagedelight:chocolate_nut_granola_bar": "Шоколадно-ореховый батончик",
    "vintagedelight:fruity_granola_bar": "Фруктовый батончик",
    "vintagedelight:century_egg": "Столетнее яйцо",
    "vintagedelight:ghost_charcoal": "Призрачный уголь",
    "vinery:jellie_wine": "Желейное вино",
    "vinery:straw_hat": "Соломенная шляпа",
    "vinery:rotten_cherry": "Гнилая вишня",
    "quark:dragon_scale": "Чешуя дракона",
    "quark:diamond_heart": "Алмазное сердце",
    "herbalbrews:oolong_tea": "Чай Улун",
    "herbalbrews:cinnamon_coffee": "Кофе с корицей",
    "herbalbrews:hazelnut_coffee": "Ореховый кофе",
    "herbalbrews:coffee": "Классический кофе",
    "herbalbrews:milk_coffee": "Кофе с молоком",
    "herbalbrews:witch_hat": "Шляпа ведьмы",
    "atmospheric:candied_orange_slices": "Засахаренные дольки апельсина",
    "atmospheric:carmine_husk": "Карминовая шелуха",
    "beachparty:palm_log": "Пальмовое бревно",
    "snowpig:frozen_ham": "Замороженная ветчина",
    "snowpig:frozen_porkchop": "Замороженная свинина",
    "twigs:bamboo_thatch": "Бамбуковая соломка",
    "automobility:dash_panel": "Панель ускорения",
    "untitledduckmod:goose_foot": "Лапка гуся",
    "untitledduckmod:duck_feather": "Утиное перо",
    "supplementaries:candy": "Конфета",
    "supplementaries:antique_ink": "Антикварные чернила",
    "create:honeyed_apple": "Яблоко в меду",
    "create:experience_block": "Блок опыта",
    "create:experience_nugget": "Самородок опыта",
}

def get_item_name(item_id):
    if item_id in MANUAL_NAMES:
        return MANUAL_NAMES[item_id]
    
    # Пытаемся найти по ключам локализации
    pure_id = item_id.split(":")[-1] if ":" in item_id else item_id
    namespace = item_id.split(":")[0] if ":" in item_id else "minecraft"
    
    candidate_keys = [
        f"item.{namespace}.{pure_id}",
        f"block.{namespace}.{pure_id}",
        f"entity.{namespace}.{pure_id}",
        f"society.item.{pure_id}",
        f"society.{pure_id}",
        item_id
    ]
    
    for k in candidate_keys:
        if k in lang_dict:
            return lang_dict[k]
            
    return item_id

def format_item(item_id):
    name = get_item_name(item_id)
    if name != item_id:
        return f"**{name}** (`{item_id}`)"
    return f"`{item_id}`"

# База данных жителей
VILLAGERS = [
    {
        "id": "banker",
        "name": "Кэролайн",
        "role": "Банкир",
        "icon": "🪙",
        "color": "#FFD700",
        "reward_5_heart": "📚 Книга навыков **«Искусство экономить»** (`society:slouching_towards_artistry`) — *Ремесленные воронки экономят Искрокамень при сборе.*",
        "alt_reward": "2x Путеводный камень (`waystones:waystone`) — если книга уже прочитана.",
        "loved": ["society:legendary_ink", "wildernature:bison_horn", "candlelight:beef_wellington", "society:aged_goat_cheese_block", "meadow:goat_cheese_block"],
        "liked": ["society:truffle_oil", "meadow:piece_of_goat_cheese", "society:mystic_syrup", "windswept:goat_stew", "society:ancient_vespertine"],
        "neutral": ["#society:dish"],
        "disliked": ["#society:farmer_product"],
        "hated": ["society:energy_drink", "supplementaries:candy"],
    },
    {
        "id": "market",
        "name": "Леон",
        "role": "Торговец с рынка",
        "icon": "🥕",
        "color": "#55FF55",
        "reward_5_heart": "📚 Книга навыков **«Круглый год фермерства»** (`society:universal_methods_of_farming`) — *Рынок продаёт семена всех сезонов круглый год.*",
        "alt_reward": "16x Семян искропада (`society:sparkpod_seed`) — если книга уже прочитана.",
        "loved": ["#vinery:red_wine", "society:glitched_vhs", "windswept:elder_feather", "society:latte", "society:tubasmoke_carton", "society:ancient_vespertine"],
        "liked": ["society:tubasmoke_stick", "society:energy_drink", "supplementaries:antique_ink", "herbalbrews:coffee", "untitledduckmod:duck_feather"],
        "neutral": [],
        "disliked": [],
        "hated": ["herbalbrews:milk_coffee", "society:death_liquid"],
    },
    {
        "id": "librarian",
        "name": "Вероника",
        "role": "Библиотекарь",
        "icon": "📖",
        "color": "#FF55FF",
        "reward_5_heart": "📚 Книга навыков **«Долговая яма»** (`society:debt_caverns`) — *Обморок в Пещере Черепа в 6:00 не начисляет штраф и больничный долг.*",
        "alt_reward": "Оберег Дивы (`botania:diva_charm`) + Кольцо маны (`botania:mana_ring` с 500k маны) — если книга уже прочитана.",
        "loved": ["#society:clothing"],
        "liked": ["supplementaries:antique_ink", "#society:dish", "society:prismatic_shard", "herbalbrews:oolong_tea", "society:sunlit_pearl", "vinery:jellie_wine", "society:bowl_of_soul"],
        "neutral": ["minecraft:rabbit_foot", "crabbersdelight:pearl_block"],
        "disliked": ["#vinery:red_wine", "#vinery:white_wine"],
        "hated": ["society:tubasmoke_stick", "society:tubasmoke_carton"],
    },
    {
        "id": "blacksmith",
        "name": "Эйден",
        "role": "Кузнец",
        "icon": "🔨",
        "color": "#FF5555",
        "reward_5_heart": "🔨 **Молот Эйдена** (`justhammers:iron_hammer`) с чарами *Эффективность V* и *Удача III*.",
        "alt_reward": "—",
        "loved": ["society:ember_crystal_cluster", "crittersandcompanions:dragonfly_wing", "windswept:lavender", "herbalbrews:hazelnut_coffee", "bakery:hazelnut_ella"],
        "liked": ["#minecraft:flowers", "#forge:raw_materials", "pamhc2trees:hazelnutitem", "pamhc2trees:roastedhazelnutitem"],
        "neutral": [],
        "disliked": [],
        "hated": [],
    },
    {
        "id": "carpenter",
        "name": "Эйс",
        "role": "Плотник",
        "icon": "🪓",
        "color": "#E69A58",
        "reward_5_heart": "📜 Чертеж **Блокопедия** (`portable_blueprints:worn_blueprint` Blockapedia by Ace) — мгновенная постройка справочной библиотеки блоков.",
        "alt_reward": "—",
        "loved": ["#gamediscs:game_discs", "society:steamy_gadget", "society:mossberry_stew", "trials:heavy_core", "vintagedelight:deluxe_granola_bar"],
        "liked": ["vintagedelight:chocolate_nut_granola_bar", "vintagedelight:fruity_granola_bar", "vinery:straw_hat", "society:mossberry", "create:honeyed_apple"],
        "neutral": ["#society:raw_logs"],
        "disliked": [],
        "hated": [],
    },
    {
        "id": "fisher",
        "name": "Харуна",
        "role": "Рыбак",
        "icon": "🎣",
        "color": "#55FFFF",
        "reward_5_heart": "💎 **Сердце Нептуния** (`society:heart_of_neptunium`) — редчайший артефакт морских глубин.",
        "alt_reward": "—",
        "loved": ["unusualfishmod:cooked_aero_mono_stick", "society:princess_hairbrush", "vintagedelight:century_egg", "society:aquamagical_dust", "society:heart_of_neptunium", "minecraft:heart_of_the_sea"],
        "liked": ["#minecraft:fishes", "minecraft:nautilus_shell", "minecraft:echo_shard", "crittersandcompanions:clam", "botania:black_lotus", "#minecraft:decorated_pot_sherds"],
        "neutral": [],
        "disliked": ["crabbersdelight:pearl_block"],
        "hated": [],
    },
    {
        "id": "shepherd",
        "name": "Мария",
        "role": "Пастух",
        "icon": "🐑",
        "color": "#FFAA00",
        "reward_5_heart": "🐧 2x **Яйцо призыва пингвина** (`2x wildernature:penguin_spawn_egg`) — эксклюзивный питомец.",
        "alt_reward": "—",
        "loved": ["society:mossberry", "society:spider_silk", "society:mocha", "society:dirty_chai", "society:merino_wool"],
        "liked": ["herbalbrews:cinnamon_coffee", "society:cranberry", "society:boysenberry", "society:crystalberry", "society:salmonberry"],
        "neutral": [],
        "disliked": ["#society:mineral"],
        "hated": ["#minecraft:flowers", "#forge:raw_meat", "minecraft:rabbit_foot", "#minecraft:fishes"],
    },
    {
        "id": "witch",
        "name": "Эвелин",
        "role": "Ведьма",
        "icon": "🔮",
        "color": "#C055FF",
        "reward_5_heart": "🤖 **Автоматическая гладилка** (`society:auto_petter`) — автоматически гладит животных в загоне каждый день.",
        "alt_reward": "—",
        "loved": ["#society:eldritch", "society:energy_drink", "society:pink_energy_drink", "society:white_energy_drink", "society:mana_energy_drink", "society:latte", "society:mocha", "society:bowl_of_soul", "herbalbrews:milk_coffee", "herbalbrews:hazelnut_coffee"],
        "liked": ["#society:mineral", "#minecraft:flowers", "herbalbrews:coffee", "society:espresso", "society:dirty_chai", "society:death_liquid"],
        "neutral": ["#society:farmer_product"],
        "disliked": ["society:truffle_tea"],
        "hated": ["#minecraft:fishes", "herbalbrews:witch_hat"],
    },
    {
        "id": "trader",
        "name": "Карлос",
        "role": "Странствующий торговец",
        "icon": "🧳",
        "color": "#55AAFF",
        "reward_5_heart": "👕 **Доступ к коллекции одежды** (стадия `trader_clothing`) — разблокирует продажу уникальных нарядов и аксессуаров.",
        "alt_reward": "—",
        "loved": ["society:star_coquito", "society:starcardi", "society:truffle_tea", "veggiesdelight:rice_and_vegetables", "society:chicken_tortilla_soup"],
        "liked": ["snuffles:frosty_fluff", "#society:mineral", "#society:dish", "society:prismatic_shard", "minecraft:rabbit_foot", "society:sunlit_pearl", "crabbersdelight:pearl_block"],
        "neutral": [],
        "disliked": ["#society:clothing"],
        "hated": ["society:gnome", "society:spider_silk"],
    },
    {
        "id": "wise_oak",
        "name": "Мудрый Дуб",
        "role": "Древнее древо",
        "icon": "🌳",
        "color": "#2E8B57",
        "reward_5_heart": "🛒 **Открытие тайного магазина Мудрого Дуба** (`openshop wise_oak`) — уникальные товары за Рога бизона и реликвии.",
        "alt_reward": "—",
        "loved": [],
        "liked": [],
        "neutral": [],
        "disliked": [],
        "hated": [],
    }
]

UNIVERSAL_LOVED = [
    "society:prismatic_shard",
    "minecraft:rabbit_foot",
    "herbalbrews:oolong_tea",
    "society:sunlit_pearl",
    "vinery:jellie_wine",
    "society:gnome",
    "society:bowl_of_soul",
    "crabbersdelight:pearl_block"
]

UNIVERSAL_LIKED = [
    "#etcetera:sweaters",
    "#etcetera:hats",
    "#society:mineral",
    "#forge:gems",
    "#society:pristine_mineral",
    "minecraft:totem_of_undying",
    "atmospheric:candied_orange_slices",
    "quark:diamond_heart",
    "society:mossberry",
    "society:mossberry_stew",
    "crabbersdelight:pearl",
    "society:furniture_box",
    "society:ancient_cookie"
]

UNIVERSAL_DISLIKED = [
    "#society:raw_logs",
    "create:experience_block",
    "create:experience_nugget",
    "snowpig:frozen_ham",
    "society:oil",
    "snowpig:frozen_porkchop",
    "twigs:bamboo_thatch",
    "automobility:dash_panel",
    "netherdepthsupgrade:bonefish",
    "netherdepthsupgrade:wither_bonefish",
    "society:magma_geode",
    "society:omni_geode",
    "society:frozen_geode",
    "society:battery",
    "society:oak_resin",
    "society:pine_tar",
    "beachparty:palm_log",
    "atmospheric:carmine_husk",
    "untitledduckmod:goose_foot",
    "society:geode",
    "aquaculture:box",
    "vintagedelight:ghost_charcoal",
    "trials:trial_key_ominous",
    "trials:trial_key",
    "farmersdelight:nether_salad",
    "vintagedelight:century_egg",
    "crabbersdelight:kelp_shake",
    "society:sturdy_bamboo_block"
]

UNIVERSAL_HATED = [
    "crabbersdelight:jar_of_pickles",
    "windswept:holly_berries",
    "crabbersdelight:sea_pickle_juice",
    "netherdepthsupgrade:lava_pufferfish",
    "netherdepthsupgrade:eyeball_fish",
    "minecraft:pufferfish",
    "autumnity:foul_berries",
    "society:supreme_mayonnaise",
    "society:wraptor_mayonnaise",
    "society:large_duck_mayonnaise",
    "society:turtle_mayonnaise",
    "society:large_mayonnaise",
    "society:mayonnaise",
    "society:penguin_mayonnaise",
    "society:birt_mayonnaise",
    "society:cruncher_mayonnaise",
    "society:parrot_mayonnaise",
    "society:turkey_mayonnaise",
    "minecraft:warped_fungus",
    "society:coconut_oil",
    "farmersdelight:rotten_tomato",
    "minecraft:poisonous_potato",
    "aquaculture:tin_can",
    "society:dried_tubabacco_leaf",
    "minecraft:nether_star",
    "society:tubabacco_leaf",
    "society:large_turkey_mayonnaise",
    "society:petrified_mayonnaise",
    "society:flamingo_mayonnaise",
    "society:duck_mayonnaise",
    "society:goose_mayonnaise",
    "society:large_goose_mayonnaise",
    "society:golden_mayonnaise",
    "society:dragon_mayonnaise",
    "society:sniffer_mayonnaise",
    "society:springling_mayonnaise",
    "farmersdelight:straw",
    "trials:ominous_bottle",
    "minecraft:echo_shard",
    "society:living_flesh",
    "minecraft:popped_chorus_fruit",
    "society:large_galliraptor_mayonnaise",
    "society:galliraptor_mayonnaise",
    "minecraft:dragon_head",
    "minecraft:dragon_egg",
    "vinery:rotten_cherry",
    "minecraft:crimson_fungus",
    "quark:dragon_scale",
    "society:mini_oni_eye",
    "society:rubber",
    "society:sap"
]

def generate_preferences_md():
    md = []
    md.append("# 👥 Справочник отношений и предпочтений жителей (Society: Sunlit Valley)\n")
    md.append("> **Назначение:** Единая структурированная база данных по всем NPC, системе очков дружбы, кулдаунам, универсальным подаркам и уникальным наградам за ♥5 сердец.\n")
    md.append("---\n")
    
    md.append("## ⚙️ 1. Механика и математика дружбы\n")
    md.append("- **Шкала дружбы:** от `0` до `500` очков (ровно **5 сердец**, 1 сердце = `100` очков).")
    md.append("- **Старт отношений:** первый диалог даёт сразу `+5` очков.")
    md.append("- **Ежедневный разговор:** `+5` очков в день (*Мудрый Дуб даёт +20 очков*).")
    md.append("- **Периодичность подарков:** подарок можно вручать **1 раз в 4 игровых дня** (`Shift + ПКМ` с предметом из тега `#society:villager_gift` в руке).")
    md.append("- **Очки за категории подарков:**")
    md.append("  - 💖 **Любимый (Loved):** `+40` очков *(почти пол-сердца!)*")
    md.append("  - 👍 **Нравится (Liked):** `+25` очков *(четверть сердца)*")
    md.append("  - 😐 **Нейтральный (Neutral):** `+10` очков")
    md.append("  - 👎 **Не нравится (Disliked):** `-15` очков")
    md.append("  - 💔 **Ненавистный (Hated):** `-30` очков")
    md.append("- **Особые правила:**")
    md.append("  - 🌳 **Мудрый Дуб (`wise_oak`):** подарки не принимает. Дружба растёт только от ежедневных разговоров (+20 в день). **ВНИМАНИЕ:** если поставить на дуб кранчик (`society:tapper` / `society:auto_tapper`), дружба мгновенно сбрасывается в `0`!\n")
    md.append("---\n")
    
    md.append("## 🏆 2. Аудит наград: Награды за уровень дружбы (♥1 .. ♥5)\n")
    md.append("По результатам аудита исходного кода KubeJS (`server_scripts/npcs/npcInteraction.js`):")
    md.append("- **Уровни 1, 2, 3, 4 сердца:** материальные предметы **не выдаются**. По мере роста сердец открываются новые уникальные ветки диалогов (`chatter_friendship1` ... `chatter_friendship4`).")
    md.append("- **Уровень 5 сердец (500 очков):** каждый житель дарит **эксклюзивную награду высшей ценности** (Книги навыков, легендарные инструменты, спавнеры, чертежи или доступ к скрытым магазинам/одежде).\n")
    
    md.append("### 🌟 ТОП-3 жителя с Книгами Навыков (Рекомендуются к приоритетной прокачке!):")
    md.append("1. 🪙 **Банкир (Кэролайн)** $\\rightarrow$ 📚 Книга **«Искусство экономить»** *(Ремесленные воронки экономят Искрокамень при сборе)*.")
    md.append("2. 🥕 **Торговец с рынка (Леон)** $\\rightarrow$ 📚 Книга **«Круглый год фермерства»** *(Семена всех сезонов доступны круглый год)*.")
    md.append("3. 📖 **Библиотекарь (Вероника)** $\\rightarrow$ 📚 Книга **«Долговая яма»** *(Обморок в Пещере Черепа не начисляет штраф и долг)*.\n")
    md.append("---\n")
    
    md.append("## 📋 3. Персональные карточки жителей и предпочтения\n")
    
    for v in VILLAGERS:
        md.append(f"### {v['icon']} {v['role']} — {v['name']} (`{v['id']}`)")
        md.append(f"- **Цвет в интерфейсе:** `{v['color']}`")
        md.append(f"- **🎁 Награда за ♥5 сердец (500 очков):** {v['reward_5_heart']}")
        if v['alt_reward'] != "—":
            md.append(f"- **🔄 Альтернативная награда (если перк изучен):** {v['alt_reward']}")
        
        if v['id'] == "wise_oak":
            md.append("- *Мудрый Дуб не принимает обычные подарки. Прокачивается только ежедневными беседами.*\n")
            continue
            
        md.append("- **💖 Любимые подарки (+40):**")
        if v['loved']:
            for it in v['loved']:
                md.append(f"  - {format_item(it)}")
        else:
            md.append("  - *(Только универсальные)*")
            
        md.append("- **👍 Нравятся (+25):**")
        if v['liked']:
            for it in v['liked']:
                md.append(f"  - {format_item(it)}")
        else:
            md.append("  - *(Только универсальные)*")
            
        if v['neutral']:
            md.append("- **😐 Нейтральные исключения (+10):**")
            for it in v['neutral']:
                md.append(f"  - {format_item(it)}")
                
        if v['disliked']:
            md.append("- **👎 Не нравятся (-15):**")
            for it in v['disliked']:
                md.append(f"  - {format_item(it)}")
                
        if v['hated']:
            md.append("- **💔 Ненавидит (-30):**")
            for it in v['hated']:
                md.append(f"  - {format_item(it)}")
                
        md.append("")
        
    md.append("---\n")
    md.append("## 🌍 4. Универсальные подарки (Universal Gifts)\n")
    md.append("Эти правила применяются ко всем жителям, если предмет не переопределён в их персональном списке выше.\n")
    
    md.append("### 💖 Универсально Любимые (+40 для всех):")
    for it in UNIVERSAL_LOVED:
        md.append(f"- {format_item(it)}")
    md.append("")
    
    md.append("### 👍 Универсально Нравятся (+25 для всех):")
    for it in UNIVERSAL_LIKED:
        md.append(f"- {format_item(it)}")
    md.append("")
    
    md.append("### 👎 Универсально Не нравятся (-15 для всех):")
    for it in UNIVERSAL_DISLIKED:
        md.append(f"- {format_item(it)}")
    md.append("")
    
    md.append("### 💔 Универсально Ненавистные (-30 для всех):")
    for it in UNIVERSAL_HATED:
        md.append(f"- {format_item(it)}")
    md.append("")
    
    md.append("---\n")
    md.append("## 🗺️ 5. Интеграция с FTB Quests и поиск информации в игре\n")
    md.append("1. **Вкладка «Жители» в FTB Quests (`villagers.snbt`):**")
    md.append("   - Содержит карточки на каждого жителя (открываются по получению приглашения `society:invitation`).")
    md.append("   - Рекомендуется добавить информацию о любимых подарках прямо в описание карточек жителей в `ru_ru.json` (`ftbquestlocalizer`).")
    md.append("2. **Где разместить информацию об универсальных подарках?**")
    md.append("   - Лучшее место — вступительный квест ветки «Жители» (`Getting Started / Villagers`), либо в тултип предмета `society:face_note` («Отношения с жителями»), который всегда под рукой у игрока.\n")
    
    content = "\n".join(md)
    target_file = os.path.join(TASK_DIR, "Список_Предпочтений.md")
    with open(target_file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Успешно сохранен: {target_file}")
    
    audit_target = os.path.join(TASK_DIR, "audit_results.md")
    with open(audit_target, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Успешно сохранен: {audit_target}")

if __name__ == "__main__":
    generate_preferences_md()
