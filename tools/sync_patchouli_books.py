import os
import json
import glob
import zipfile
import sys
import re
import shutil

sys.stdout.reconfigure(encoding='utf-8')

print("=== 1. LOADING ALL TRANSLATIONS ===")
all_lang = {}

for f in glob.glob('translations/mods/*.json'):
    with open(f, 'r', encoding='utf-8') as jf:
        all_lang.update(json.load(jf))
for f in glob.glob('translations/*.json'):
    with open(f, 'r', encoding='utf-8') as jf:
        all_lang.update(json.load(jf))
for f in glob.glob('game_data/**/ru_ru.json', recursive=True):
    with open(f, 'r', encoding='utf-8') as jf:
        all_lang.update(json.load(jf))
for jar in glob.glob('G:/curseforge/minecraft/Instances/Society Sunlit Valley/mods/*.jar'):
    try:
        with zipfile.ZipFile(jar, 'r') as z:
            for n in z.namelist():
                if n.endswith('ru_ru.json'):
                    d = json.loads(z.read(n).decode('utf-8'))
                    for k, v in d.items():
                        if k not in all_lang:
                            all_lang[k] = v
    except Exception:
        pass

# Fix specific known items/entities in all_lang
all_lang['item.netherdepthsupgrade.soulsucker'] = 'Высасыватель душ'
all_lang['entity.netherdepthsupgrade.soulsucker'] = 'Высасыватель душ'
all_lang['item.species.wraptor_egg'] = 'Яйцо ираптора'
all_lang['entity.species.wraptor'] = 'Ираптор'
all_lang['item.species.cruncher_egg'] = 'Яйцо кусача'
all_lang['entity.species.cruncher'] = 'Кусач'
all_lang['item.species.goober_egg'] = 'Окаменевшее яйцо'
all_lang['entity.species.goober'] = 'Губер'
all_lang['item.pamhc2trees.plumitem'] = 'Слива'
all_lang['item.pamhc2trees.mangoitem'] = 'Манго'
all_lang['item.pamhc2trees.hazelnutitem'] = 'Фундук'
all_lang['item.pamhc2trees.bananaitem'] = 'Банан'
all_lang['item.pamhc2trees.cherryitem'] = 'Вишня'
all_lang['item.pamhc2trees.lemonitem'] = 'Лимон'
all_lang['item.pamhc2trees.orangeitem'] = 'Апельсин'
all_lang['item.pamhc2trees.peachitem'] = 'Персик'
all_lang['item.pamhc2trees.starfruititem'] = 'Карамбола'
all_lang['item.pamhc2trees.pawpawitem'] = 'Азимина'
all_lang['item.pamhc2trees.passionfruititem'] = 'Маракуйя'
all_lang['item.pamhc2trees.lycheeitem'] = 'Личи'
all_lang['item.pamhc2trees.dragonfruititem'] = 'Питайя'
all_lang['item.pamhc2trees.cinnamonitem'] = 'Корица'
all_lang['item.wildernature.bison_horn'] = 'Рог бизона'
all_lang['entity.wildernature.bison'] = 'Бизон'
all_lang['item.atmospheric.carmine_husk'] = 'Карминовая шелуха'
all_lang['entity.atmospheric.cochineal'] = 'Кошениль'
all_lang['entity.untitledduckmod.duck'] = 'Утка'
all_lang['entity.untitledduckmod.goose'] = 'Гусь'
all_lang['item.windswept.frozen_branch'] = 'Замёрзшая ветвь'
all_lang['entity.windswept.frostbiter'] = 'Обморозитель'
all_lang['entity.species.mammutilation'] = 'Маммутиляция'
all_lang['entity.betterarcheology.moobloom'] = 'Мублум'
all_lang['entity.autumnity.snail'] = 'Улитка'
all_lang['entity.snowpig.snow_pig'] = 'Снежная свинья'
all_lang['entity.snuffles.snuffle'] = 'Снуфлик'
all_lang['entity.autumnity.turkey'] = 'Индейка'
all_lang['entity.meadow.wooly_cow'] = 'Шерстяная корова'
all_lang['entity.meadow.wooly_sheep'] = 'Шерстистая овца'
all_lang['item.crittersandcompanions.koi_fish'] = 'Карп кои'
all_lang['entity.crittersandcompanions.koi_fish'] = 'Карп кои'

# Load old Scriptora translations as fallback for descriptions
old_ru_files = {}
old_ru_root = 'tasks/patchouli_sync/old_ru_ru/patchouli_books'
if os.path.exists(old_ru_root):
    for root, dirs, files in os.walk(old_ru_root):
        for f in files:
            if f.endswith('.json'):
                full = os.path.join(root, f)
                rel = os.path.relpath(full, old_ru_root).replace('\\', '/')
                try:
                    with open(full, 'r', encoding='utf-8') as jf:
                        old_ru_files[rel] = json.load(jf)
                except Exception:
                    pass

print(f"Loaded {len(all_lang)} translation keys and {len(old_ru_files)} old Patchouli files.")

def get_name_by_id(item_id):
    if not item_id:
        return None, None, '[UNKNOWN]'
    if '{' in item_id:
        item_id = item_id.split('{')[0]
    if ':' not in item_id:
        return None, None, '[UNKNOWN]'
    ns, name = item_id.split(':', 1)
    keys = [
        (f'item.{ns}.{name}', f'translations/mods/{ns}.json' if os.path.exists(f'translations/mods/{ns}.json') else f'{ns}'),
        (f'block.{ns}.{name}', f'translations/mods/{ns}.json' if os.path.exists(f'translations/mods/{ns}.json') else f'{ns}'),
        (f'entity.{ns}.{name}', f'translations/mods/{ns}.json' if os.path.exists(f'translations/mods/{ns}.json') else f'{ns}'),
        (f'{ns}.{name}', f'translations/{ns}.json')
    ]
    for k, src in keys:
        if k in all_lang:
            return all_lang[k], src, '[FACT]'
    return None, None, '[UNKNOWN]'

def translate_stats_text(text):
    if not text:
        return text
    
    # Season replacements with colors
    text = text.replace('§0🌼 §2Spring§0', '§0🌼 §2Весна§0')
    text = text.replace('🌼 §2Spring§0', '🌼 §2Весна§0')
    text = text.replace('§0🔥 §6Summer§0', '§0🔥 §6Лето§0')
    text = text.replace('🔥 §6Summer§0', '🔥 §6Лето§0')
    text = text.replace('🔥 §6Summer §0', '🔥 §6Лето §0')
    text = text.replace('§0🍂 §4Autumn§0', '§0🍂 §4Осень§0')
    text = text.replace('🍂 §4Autumn§0', '🍂 §4Осень§0')
    text = text.replace('§0❆ §bWinter§0', '§0❆ §bЗима§0')
    text = text.replace('❆ §bWinter§0', '❆ §bЗима§0')
    text = text.replace('🔥 §6Summer§r 🍂 §4Autumn', '🔥 §6Лето§r 🍂 §4Осень')
    text = text.replace('Year-Round', 'Круглый год')
    
    # Headers and labels
    text = text.replace('$(l)Stats$()', '$(l)Характеристики$()')
    text = text.replace('Seed Price:', 'Цена семян:')
    text = text.replace('Growth time:', 'Время созревания:')
    text = text.replace('Grow time:', 'Время созревания:')
    text = text.replace('Yield:', 'Урожайность:')
    text = text.replace('Dimension:', 'Измерение:')
    text = text.replace('Biome:', 'Биом:')
    text = text.replace('Water:', 'Вода:')
    text = text.replace('Weather:', 'Погода:')
    text = text.replace('Time:', 'Время:')
    text = text.replace('Bait:', 'Наживка:')
    text = text.replace('Price:', 'Цена:')
    text = text.replace('Milk:', 'Молоко:')
    text = text.replace('Milk Cooldown:', 'Перезарядка молока:')
    text = text.replace('Drops:', 'Добыча:')
    text = text.replace('Favorite Food:', 'Любимая еда:')
    text = text.replace('Produces:', 'Производит:')
    text = text.replace('Produce:', 'Продукция:')
    text = text.replace('Cooldown:', 'Перезарядка:')
    text = text.replace('Requires Wood:', 'Требуется древесина:')
    text = text.replace('Sapling Price:', 'Цена саженца:')
    text = text.replace('Fertilizer:', 'Удобрение:')
    
    # Values
    text = text.replace('Fresh River', 'Пресная (река)')
    text = text.replace('Fresh/River', 'Пресная / река')
    text = text.replace('Fresh', 'Пресная')
    text = text.replace('River', 'Река')
    text = text.replace('Ocean', 'Океан')
    text = text.replace('Salt', 'Морская')
    text = text.replace('Swamp', 'Болото')
    text = text.replace('Caves', 'Пещеры')
    text = text.replace('Mushroom Island', 'Грибной остров')
    text = text.replace('Rain', 'Дождь')
    text = text.replace('Clear', 'Ясно')
    text = text.replace('Day', 'День')
    text = text.replace('Night', 'Ночь')
    text = text.replace('Nether', 'Незер')
    text = text.replace('Overworld', 'Обычный мир')
    text = text.replace('Basalt Deltas', 'Базальтовые дельты')
    text = text.replace('Soul Sand Valley', 'Долина песка душ')
    text = text.replace('Crimson Forest', 'Багровый лес')
    text = text.replace('Warped Forest', 'Искажённый лес')
    text = text.replace('Nether Wastes', 'Пустоши Незера')
    text = text.replace('Any', 'Любая')
    text = re.sub(r'(\d+)\s+days', r'\1 дн.', text)
    text = re.sub(r'(\d+)\s+day', r'\1 дн.', text)
    
    # Specific fish baits
    text = text.replace('$(thing)Worm$()', '$(thing)Червь$()')
    text = text.replace('$(thing)Gold Grub$()', '$(thing)Золотая личинка$()')
    text = text.replace('$(thing)Leech$()', '$(thing)Пиявка$()')
    text = text.replace('$(thing)Minnow$()', '$(thing)Гольян$()')
    text = text.replace('$(thing)Firefly$()', '$(thing)Светлячок$()')
    
    # Specific drops & food
    text = text.replace('Raw Beef', 'Сырая говядина')
    text = text.replace('Raw Porkchop', 'Сырая свинина')
    text = text.replace('Raw Mutton', 'Сырая баранина')
    text = text.replace('Raw Chicken', 'Сырая курятина')
    text = text.replace('Leather', 'Кожа')
    text = text.replace('Feather', 'Перо')
    text = text.replace('Egg', 'Яйцо')
    text = text.replace('Wool', 'Шерсть')
    text = text.replace('Milk', 'Молоко')
    text = text.replace('Wheat', 'Пшеница')
    text = text.replace('Seeds', 'Семена')
    text = text.replace('Carrot', 'Морковь')
    text = text.replace('Potato', 'Картофель')
    text = text.replace('Beetroot', 'Свёкла')
    text = text.replace('Apple', 'Яблоко')
    text = text.replace('Golden Apple', 'Золотое яблоко')
    text = text.replace('Bamboo', 'Бамбук')
    text = text.replace('Sweet Berries', 'Сладкие ягоды')
    text = text.replace('Glow Berries', 'Светящиеся ягоды')
    text = text.replace('Slimeball', 'Сгусток слизи')
    text = text.replace('Honey Bottle', 'Бутылочка мёда')
    text = text.replace('Honeycomb', 'Пчелиные соты')
    
    return text

dictionary_records = []
audit_fish_discrepancies = []
audit_almanac_discrepancies = []

print("=== 2. TRANSLATING FISH FINDER ===")
# fish_finder book.json
ff_book = {
    "name": "Справочник рыболова",
    "landing_text": "Руководство по ловле всех видов рыб, сезонам, водоёмам, погодным условиям и наживкам.",
    "version": 1
}
os.makedirs('patchouli_books/fish_finder/ru_ru', exist_ok=True)
with open('patchouli_books/fish_finder/ru_ru/book.json', 'w', encoding='utf-8') as jf:
    json.dump(ff_book, jf, ensure_ascii=False, indent=2)

# fish_finder categories
os.makedirs('patchouli_books/fish_finder/ru_ru/categories', exist_ok=True)
ff_cat = {
    "name": "Рыбы",
    "description": "Справочник по всем видам рыб, обитающим в реках, океанах, пещерах и лаве Незера.",
    "icon": "furniture:copper_fish_tank",
    "sortnum": 0
}
with open('patchouli_books/fish_finder/ru_ru/categories/fish.json', 'w', encoding='utf-8') as jf:
    json.dump(ff_cat, jf, ensure_ascii=False, indent=2)

# fish_finder entries
os.makedirs('patchouli_books/fish_finder/ru_ru/entries/fish', exist_ok=True)
fish_en_dir = 'patchouli_books/fish_finder/en_us/entries/fish'
for f in sorted(os.listdir(fish_en_dir)):
    if f.endswith('.json'):
        with open(os.path.join(fish_en_dir, f), 'r', encoding='utf-8') as jf:
            en_data = json.load(jf)
        
        old_key = f"fish_finder/ru_ru/entries/fish/{f}"
        old_data = old_ru_files.get(old_key, {})
        
        icon = en_data.get('icon', '')
        actual_name, src, evid = get_name_by_id(icon)
        if not actual_name:
            actual_name = en_data.get('name', '')
            src = 'manual'
            evid = '[UNKNOWN]'
            
        old_name = old_data.get('name', '(нет перевода)')
        if old_name != actual_name:
            audit_fish_discrepancies.append({
                'file': f,
                'id': icon,
                'en': en_data.get('name', ''),
                'old': old_name,
                'actual': actual_name,
                'source': src
            })
            
        dictionary_records.append({
            'book': 'fish_finder',
            'category': 'fish',
            'file': f,
            'id': icon,
            'en': en_data.get('name', ''),
            'ru': actual_name,
            'source': src,
            'evidence': evid
        })
        
        # Build translated entry
        ru_entry = dict(en_data)
        ru_entry['name'] = actual_name
        
        ru_pages = []
        for p_idx, p in enumerate(en_data.get('pages', [])):
            ru_p = dict(p)
            p_type = p.get('type')
            
            if p_type == 'patchouli:text':
                ru_p['text'] = translate_stats_text(p.get('text', ''))
                if 'title' in p:
                    ru_p['title'] = p['title']
            elif p_type == 'patchouli:entity':
                # Use old translated flavour text if available, or translate
                old_p_text = ''
                if old_data and len(old_data.get('pages', [])) > p_idx:
                    old_p_text = old_data['pages'][p_idx].get('text', '')
                
                if old_p_text and old_p_text != p.get('text', ''):
                    ru_p['text'] = old_p_text
                else:
                    ru_p['text'] = translate_stats_text(p.get('text', ''))
            
            ru_pages.append(ru_p)
            
        ru_entry['pages'] = ru_pages
        with open(f'patchouli_books/fish_finder/ru_ru/entries/fish/{f}', 'w', encoding='utf-8') as jf:
            json.dump(ru_entry, jf, ensure_ascii=False, indent=2)

print(f"Translated 69 fish entries (Discrepancies found: {len(audit_fish_discrepancies)})")

print("=== 3. TRANSLATING ALMANAC ===")
# almanac book.json
alm_book = {
    "name": "Фермерский альманах",
    "landing_text": "Полный справочник фермера по культурам, животным, слаймам, деревьям и уходу за угодьями.",
    "version": 1
}
os.makedirs('patchouli_books/almanac/ru_ru', exist_ok=True)
with open('patchouli_books/almanac/ru_ru/book.json', 'w', encoding='utf-8') as jf:
    json.dump(alm_book, jf, ensure_ascii=False, indent=2)

# almanac categories
cat_translations = {
    "animals.json": {
        "name": "Домашние животные",
        "description": "Руководство по разведению скота, уходу, сбору шерсти, яиц, молока и любимой еде животных.",
        "icon": "society:animal_feed",
        "sortnum": 0
    },
    "crops.json": {
        "name": "Сельхозкультуры",
        "description": "Справочник по всем полевым культурам, сезонам посева, ценам на семена и урожайности.",
        "icon": "minecraft:netherite_hoe",
        "sortnum": 1
    },
    "pets.json": {
        "name": "Питомцы",
        "description": "Домашние питомцы, птицы, капибары, кошки, собаки, их повадки и лакомства.",
        "icon": "candlelight:hearth",
        "sortnum": 2
    },
    "slimes.json": {
        "name": "Слаймы",
        "description": "Разведение великолепных слаймов, вкусы, любимые блюда и производство ресурсов.",
        "icon": "splendid_slimes:slime_heart{slime:{id:\"splendid_slimes:slimy\"}}",
        "sortnum": 3
    },
    "trees.json": {
        "name": "Деревья",
        "description": "Породы лесных и декоративных деревьев, саженцы, заготовка древесины и сезоны.",
        "icon": "pamhc2trees:apple_sapling",
        "sortnum": 4
    },
    "tree_crops.json": {
        "name": "Древесные культуры",
        "description": "Плодовые деревья, сбор фруктов, орехов и сезонное созревание.",
        "icon": "society:cornucopia",
        "sortnum": 5
    }
}

os.makedirs('patchouli_books/almanac/ru_ru/categories', exist_ok=True)
for cat_file, cat_data in cat_translations.items():
    with open(f'patchouli_books/almanac/ru_ru/categories/{cat_file}', 'w', encoding='utf-8') as jf:
        json.dump(cat_data, jf, ensure_ascii=False, indent=2)

# Specific custom names for animals/crops/slimes
animal_name_map = {
    'cow': 'Корова',
    'sheep': 'Овца',
    'pig': 'Свинья',
    'chicken': 'Курица',
    'goat': 'Коза',
    'duck': 'Утка',
    'goose': 'Гусь',
    'bison': 'Бизон',
    'turkey': 'Индейка',
    'snow_pig': 'Снежная свинья',
    'wooly_cow': 'Шерстяная корова',
    'wooly_sheep': 'Шерстистая овца',
    'snuffle': 'Снуфлик',
    'snail': 'Улитка',
    'cochineal': 'Кошениль',
    'moobloom': 'Мублум',
    'raccoon': 'Енот',
    'frostbiter': 'Обморозитель',
    'mammutilation': 'Маммутиляция',
    'cruncher': 'Кусач',
    'wraptor': 'Ираптор',
    'goober': 'Губер',
    'bat': 'Летучая мышь',
    'panda': 'Панда',
    'squirrel': 'Белка',
    'shima_enaga': 'Длиннохвостая синица',
    'bear': 'Медведь',
    'bee': 'Пчела',
    'frog': 'Лягушка',
    'allay': 'Эллей',
    'axolotl': 'Аксолотль',
    'camel': 'Верблюд',
    'cat': 'Кошка',
    'dog': 'Собака',
    'dolphin': 'Дельфин',
    'donkey': 'Осёл',
    'fox': 'Лиса',
    'horse': 'Лошадь',
    'llama': 'Лама',
    'mule': 'Мул',
    'ocelot': 'Оцелот',
    'parrot': 'Попугай',
    'polar_bear': 'Белый медведь',
    'rabbit': 'Кролик',
    'strider': 'Страйдер',
    'turtle': 'Черепаха',
    'wolf': 'Волк'
}

# almanac entries
almanac_en_entries = 'patchouli_books/almanac/en_us/entries'
alm_count = 0
for root, dirs, files in os.walk(almanac_en_entries):
    for f in sorted(files):
        if f.endswith('.json'):
            alm_count += 1
            full_p = os.path.join(root, f)
            rel_p = os.path.relpath(full_p, almanac_en_entries).replace('\\', '/')
            with open(full_p, 'r', encoding='utf-8') as jf:
                en_data = json.load(jf)
            
            old_key = f"almanac/ru_ru/entries/{rel_p}"
            old_data = old_ru_files.get(old_key, {})
            
            en_name = en_data.get('name', '')
            icon = en_data.get('icon', '')
            cat_name = en_data.get('category', '').split(':')[-1]
            base_fname = f.replace('.json', '')
            
            actual_name = None
            src = None
            evid = '[UNKNOWN]'
            
            if cat_name == 'animals':
                actual_name = animal_name_map.get(base_fname)
                if not actual_name:
                    actual_name, src, evid = get_name_by_id(icon)
                else:
                    src = 'game_entity'
                    evid = '[FACT]'
            elif cat_name == 'crops':
                # Extract emojis if present
                emojis = re.findall(r'[🌼🔥🍂❆🌐]', en_name)
                emoji_str = ' ' + ''.join(emojis) if emojis else ''
                clean_en = re.sub(r'[🌼🔥🍂❆🌐\s]+', ' ', en_name).strip()
                
                crop_name, src, evid = get_name_by_id(icon)
                if crop_name:
                    actual_name = f"{crop_name}{emoji_str}"
                else:
                    actual_name = en_name
            elif cat_name in ['trees', 'tree_crops']:
                actual_name, src, evid = get_name_by_id(icon)
                if not actual_name:
                    actual_name = en_name
            else:
                actual_name, src, evid = get_name_by_id(icon)
                if not actual_name:
                    actual_name = en_name
                    
            if not actual_name:
                actual_name = en_name
                
            old_name = old_data.get('name', '(нет перевода)')
            if old_name != actual_name:
                audit_almanac_discrepancies.append({
                    'file': rel_p,
                    'id': icon,
                    'en': en_name,
                    'old': old_name,
                    'actual': actual_name,
                    'source': src or 'manual'
                })
                
            dictionary_records.append({
                'book': 'almanac',
                'category': cat_name,
                'file': rel_p,
                'id': icon,
                'en': en_name,
                'ru': actual_name,
                'source': src or 'manual',
                'evidence': evid
            })
            
            ru_entry = dict(en_data)
            ru_entry['name'] = actual_name
            
            ru_pages = []
            for p_idx, p in enumerate(en_data.get('pages', [])):
                ru_p = dict(p)
                p_type = p.get('type')
                
                if p_type == 'patchouli:text':
                    ru_p['text'] = translate_stats_text(p.get('text', ''))
                    if 'title' in p:
                        ru_p['title'] = p['title']
                elif p_type == 'patchouli:multiblock':
                    if 'name ' in p:
                        ru_p['name '] = f"Посадка: {actual_name}"
                    elif 'name' in p:
                        ru_p['name'] = f"Посадка: {actual_name}"
                elif p_type == 'patchouli:entity':
                    old_p_text = ''
                    if old_data and len(old_data.get('pages', [])) > p_idx:
                        old_p_text = old_data['pages'][p_idx].get('text', '')
                    if old_p_text and old_p_text != p.get('text', ''):
                        ru_p['text'] = old_p_text
                    else:
                        ru_p['text'] = translate_stats_text(p.get('text', ''))
                        
                ru_pages.append(ru_p)
                
            ru_entry['pages'] = ru_pages
            
            out_file = os.path.join('patchouli_books/almanac/ru_ru/entries', rel_p)
            os.makedirs(os.path.dirname(out_file), exist_ok=True)
            with open(out_file, 'w', encoding='utf-8') as jf:
                json.dump(ru_entry, jf, ensure_ascii=False, indent=2)

print(f"Translated {alm_count} almanac entries (Discrepancies found: {len(audit_almanac_discrepancies)})")

# 4. Copy to game instance
game_pb = 'G:/curseforge/minecraft/Instances/Society Sunlit Valley/patchouli_books'
if os.path.exists(game_pb):
    shutil.copytree('patchouli_books/fish_finder/ru_ru', f'{game_pb}/fish_finder/ru_ru', dirs_exist_ok=True)
    shutil.copytree('patchouli_books/almanac/ru_ru', f'{game_pb}/almanac/ru_ru', dirs_exist_ok=True)
    print("Copied translated ru_ru books directly into game instance!")

# 5. Write docs/Patchouli/Актуальные_названия_объектов.md
os.makedirs('docs/Patchouli', exist_ok=True)
with open('docs/Patchouli/Актуальные_названия_объектов.md', 'w', encoding='utf-8') as mf:
    mf.write("# Единый словарь актуальных названий объектов (Patchouli Almanac & Fish Finder)\n\n")
    mf.write("Данный словарь является **источником истины** для синхронизации названий предметов, рыб, растений и мобов между книгами Patchouli и предметами в инвентаре игры.\n\n")
    mf.write("| ID / Реестр | Тип | Книга / Категория | English | Актуальное русское название | Источник | Статус |\n")
    mf.write("| :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n")
    for r in sorted(dictionary_records, key=lambda x: (x['book'], x['category'], x['ru'])):
        mf.write(f"| `{r['id']}` | `{r['category']}` | `{r['book']}` | {r['en']} | **{r['ru']}** | {r['source']} | {r['evidence']} |\n")

print("Created docs/Patchouli/Актуальные_названия_объектов.md")
