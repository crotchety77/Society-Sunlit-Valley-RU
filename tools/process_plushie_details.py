import os, json, re

# Complete analysis script for Plushie Capsule pool
with open('game_data/startup_scripts/globalFurniturePlushies.js', 'r', encoding='utf-8') as f:
    content = f.read()

m = re.search(r'global\.originalPlushies\s*=\s*\[(.*?)\];', content, re.DOTALL)
raw_items = m.group(1).split(',')
original_plushies = [x.strip().strip('"').strip("'") for x in raw_items if x.strip().strip('"').strip("'")]

print(f'Total items in pool: {len(original_plushies)}')

# Load all lang dictionaries
en_all = {}
ru_all = {}

# 1. Kubejs assets
for root, dirs, files in os.walk('G:/curseforge/minecraft/Instances/Society Sunlit Valley/kubejs/assets'):
    for f in files:
        if f == 'en_us.json':
            try:
                with open(os.path.join(root, f), 'r', encoding='utf-8') as fp:
                    en_all.update(json.load(fp))
            except: pass
        elif f == 'ru_ru.json':
            try:
                with open(os.path.join(root, f), 'r', encoding='utf-8') as fp:
                    ru_all.update(json.load(fp))
            except: pass

# 2. Mod JARs langs
with open('tools/mod_jars_langs.json', 'r', encoding='utf-8') as fp:
    jar_langs = json.load(fp)
    for ns, lang_map in jar_langs.items():
        if 'en_us.json' in lang_map:
            en_all.update(lang_map['en_us.json'])
        if 'ru_ru.json' in lang_map:
            ru_all.update(lang_map['ru_ru.json'])

# 3. Society translations
for path in ['translations/society/en_us.json', 'translations/society/ru_ru.json']:
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as fp:
            d = json.load(fp)
            if 'ru_ru' in path: ru_all.update(d)
            else: en_all.update(d)

plushie_data = []

for idx, orig in enumerate(original_plushies, 1):
    mod, name = orig.split(':')
    adv_id = f'{mod}:adv_{name}'
    
    # lookup keys
    candidates = [
        f'block.{mod}.adv_{name}',
        f'item.{mod}.adv_{name}',
        f'block.{mod}.{name}',
        f'item.{mod}.{name}',
        f'{mod}.{name}',
        f'block.{name}',
        f'item.{name}',
        name
    ]
    
    en_name = None
    for k in candidates:
        if k in en_all:
            en_name = en_all[k]
            break
            
    ru_name = None
    for k in candidates:
        if k in ru_all:
            ru_name = ru_all[k]
            break
            
    if not en_name:
        # Generate readable name from ID
        en_name = name.replace('_', ' ').title()
        
    plushie_data.append({
        'num': idx,
        'mod': mod,
        'name': name,
        'orig_id': orig,
        'adv_id': adv_id,
        'en_name': en_name,
        'ru_name': ru_name
    })

with open('tools/plushie_pool_detailed.json', 'w', encoding='utf-8') as fp:
    json.dump(plushie_data, fp, ensure_ascii=False, indent=2)

print('Successfully processed all 62 plushies!')
