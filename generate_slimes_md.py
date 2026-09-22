import os, json

slimes_dir = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\data\splendid_slimes\slimes'
if not os.path.exists(slimes_dir):
    slimes_dir = r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\game_data\data\splendid_slimes\slimes'

ru_lang_path = r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\translations\mods\splendid_slimes.json'
with open(ru_lang_path, 'r', encoding='utf-8') as f:
    ru_lang = json.load(f)

# Mod items ru lang
all_ru = {}
for root, dirs, files in os.walk(r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\translations'):
    for file in files:
        if file.endswith('.json'):
            try:
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    all_ru.update(json.load(f))
            except:
                pass

for root, dirs, files in os.walk(r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets'):
    for file in files:
        if file == 'ru_ru.json':
            try:
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    all_ru.update(json.load(f))
            except:
                pass

# Manual item names mapping for precision
item_name_overrides = {
    "minecraft:golden_carrot": "Золотая морковь",
    "society:fire_opal": "Огненный опал",
    "autumnity:cooked_turkey": "Жареная индейка",
    "society:large_sheep_milk": "Большое овечье молоко",
    "untitledduckmod:cooked_duck": "Жареная утка",
    "untitledduckmod:duck": "Утка",
    "netherdepthsupgrade:bonefish": "Рыба-костянка",
    "minecraft:stray": "Зимогор",
    "trials:bogged": "Заболоченный",
    "minecraft:amethyst_shard": "Осколок аметиста",
    "society:bell_pepper_preserves": "Консервированный сладкий перец",
    "vinery:jungle_grapes_red": "Красный виноград джунглей",
    "vintagedelight:pickle": "Солёный огурец",
    "oreganized:lead_ingot": "Свинцовый слиток",
    "society:tubasmoke_stick": "Сигарета тубадыма",
    "society:dried_shimmering_mushrooms": "Сушёные мерцающие грибы",
    "minecraft:purple_bed": "Фиолетовая кровать",
    "aquaculture:boulti": "Бульти",
    "unusualfishmod:raw_sneep_snorp": "Сырой снип-снорп",
    "minecraft:chicken": "Курица / Сырая курятина",
    "minecraft:chorus_flower": "Цветок хоруса",
    "farm_and_charm:strawberry": "Клубника",
    "society:smoked_spindlefish": "Копчёная веретеновидка",
    "atmospheric:orange": "Апельсин",
    "veggiesdelight:garlic": "Чеснок",
    "pamhc2trees:bananaitem": "Банан",
    "buzzier_bees:crystallized_honey_block": "Блок кристаллизованного мёда"
}

def get_item_ru_name(item_id):
    if item_id in item_name_overrides:
        return item_name_overrides[item_id]
    parts = item_id.split(':')
    ns = parts[0]
    path = parts[1]
    keys = [
        f'item.{ns}.{path}',
        f'block.{ns}.{path}',
        f'entity.{ns}.{path}'
    ]
    for k in keys:
        if k in all_ru:
            return all_ru[k]
    return item_id

en_names_map = {
    'all_seeing': 'All-Seeing',
    'bear': 'Bear (Barney)',
    'bitwise': 'Bitwise',
    'blazing': 'Blazing',
    'bony': 'Bony',
    'boomcat': 'Boomcat',
    'dusty': 'Dusty',
    'ender': 'Ender',
    'gold': 'Gold',
    'juicy': 'Juicy',
    'luminous': 'Luminous',
    'mechanic': 'Mechanic',
    'minty': 'Minty (Ender Dragon)',
    'orby': 'Orby',
    'phantom': 'Phantom',
    'prisma': 'Prisma',
    'puddle': 'Puddle',
    'rotting': 'Rotting',
    'shulking': 'Shulking',
    'slimy': 'Slimy (Pink)',
    'sparkcat': 'Sparkcat',
    'sweet': 'Sweet',
    'webby': 'Webby',
    'weeping': 'Weeping'
}

slimes = []
for f in sorted(os.listdir(slimes_dir)):
    if f.endswith('.json'):
        p = os.path.join(slimes_dir, f)
        with open(p, 'r', encoding='utf-8') as fp:
            data = json.load(fp)
            breed = data.get('breed', f.replace('.json',''))
            
            ru_name = ru_lang.get(f'slime.splendid_slimes.{breed}', breed.capitalize())
            en_name = en_names_map.get(breed, breed.capitalize())
            ru_diet = ru_lang.get(f'diet.splendid_slimes.{breed}', '')
            
            foods_list = []
            for item in data.get('foods', []):
                if 'tag' in item:
                    foods_list.append(f"#{item['tag']}")
                elif 'item' in item:
                    foods_list.append(item['item'])
            
            fav_food = data.get('favorite_food', {})
            fav_food_str = ''
            if 'item' in fav_food:
                fav_id = fav_food['item']
                fav_name = get_item_ru_name(fav_id)
                fav_food_str = f"{fav_name} (`{fav_id}`)"
            
            fav_entity = data.get('favorite_entity', None)
            fav_entity_str = ''
            if fav_entity:
                if isinstance(fav_entity, str):
                    ent_name = get_item_ru_name(fav_entity)
                    fav_entity_str = f"{ent_name} (`{fav_entity}`)"
                elif isinstance(fav_entity, dict) and 'entity' in fav_entity:
                    ent_id = fav_entity['entity']
                    ent_name = get_item_ru_name(ent_id)
                    fav_entity_str = f"{ent_name} (`{ent_id}`)"
            
            slimes.append({
                'breed': breed,
                'ru_name': ru_name,
                'en_name': en_name,
                'ru_diet': ru_diet,
                'foods': foods_list,
                'fav_food': fav_food_str,
                'fav_entity': fav_entity_str,
                'traits': data.get('traits', [])
            })

out_md = '# Аудит слаймов сборки (Splendid Slimes + Custom Breeds)\n\n'
out_md += 'В сборке представлено **24 породы слаймов** (включая 5 кастомных пород от автора сборки: `bear`, `dusty`, `juicy`, `mechanic`, `sparkcat`).\n'
out_md += 'Все диеты и любимая еда переопределены автором сборки под экосистему модов Sunlit Valley.\n\n'
out_md += '| № | Слайм (RU) | Name (EN) | ID породы | Категория диеты (Теги / Предметы) | Любимая еда (Favorite Food / ID) | Любимый моб (если есть) |\n'
out_md += '|---|---|---|---|---|---|---|\n'

for i, s in enumerate(slimes, 1):
    foods_formatted = '<br>'.join([f'`{f}`' for f in s['foods']])
    fav = s['fav_food'] if s['fav_food'] else '—'
    ent = s['fav_entity'] if s['fav_entity'] else '—'
    out_md += f'| {i} | **{s["ru_name"]}** | {s["en_name"]} | `splendid_slimes:{s["breed"]}` | **{s["ru_diet"]}**<br>{foods_formatted} | {fav} | {ent} |\n'

out_md += '\n---\n\n## Подробный список по каждому слайму (ID, Теги, Любимая еда)\n\n'

for i, s in enumerate(slimes, 1):
    out_md += f'### {i}. {s["ru_name"]} ({s["en_name"]})\n'
    out_md += f'- **ID породы:** `splendid_slimes:{s["breed"]}`\n'
    out_md += f'- **Категория диеты:** {s["ru_diet"]}\n'
    out_md += f'- **Теги / Список принимаемой еды:**\n'
    for f in s['foods']:
        out_md += f'  - `{f}`\n'
    if s['fav_food']:
        out_md += f'- **Любимая еда:** {s["fav_food"]}\n'
    if s['fav_entity']:
        out_md += f'- **Любимая добыча / сущность:** {s["fav_entity"]}\n'
    if s['traits']:
        traits_str = ', '.join([f'`{t}`' for t in s['traits']])
        out_md += f'- **Черты (Traits):** {traits_str}\n'
    out_md += '\n'

out_path = r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\docs\SLIMES_DIETS_AUDIT.md'
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(out_md)

print('Successfully written to', out_path)
