import re
import json
import os
import glob

# 1. Parse global.originalPlushies
script_path = os.path.normpath('game_data/startup_scripts/globalFurniturePlushies.js')
with open(script_path, 'r', encoding='utf-8') as f:
    content = f.read()

m = re.search(r'global\.originalPlushies\s*=\s*\[(.*?)\];', content, re.DOTALL)
if not m:
    print('Error: global.originalPlushies not found')
    exit(1)

raw_items = m.group(1).split(',')
original_plushies = []
for item in raw_items:
    clean = item.strip().strip('"').strip("'")
    if clean:
        original_plushies.append(clean)

print(f'Found {len(original_plushies)} items in global.originalPlushies')

# 2. Check if any other items are added to society:plushies tag
tag_scripts = glob.glob('game_data/server_scripts/**/*.js', recursive=True)
tag_items = set()
for s in tag_scripts:
    with open(s, 'r', encoding='utf-8') as f:
        s_content = f.read()
    for line in s_content.splitlines():
        if 'society:plushies' in line and 'e.add(' in line:
            print(f'Tag addition in {os.path.basename(s)}: {line.strip()}')

# 3. Form adv_ IDs
adv_plushies = []
for p in original_plushies:
    mod, name = p.split(':')
    adv_id = f'{mod}:adv_{name}'
    adv_plushies.append((mod, name, p, adv_id))

print(f'Total adv_ plushies generated: {len(adv_plushies)}')

# 4. Load translations to find English & Russian names
lang_dirs = [
    'translations',
    'translations/mods',
    'game_data/assets',
    'G:/curseforge/minecraft/Instances/Society Sunlit Valley/kubejs/assets'
]

# We also check jar files if needed, or mod lang files
ru_dict = {}
en_dict = {}

def load_json(path):
    if os.path.exists(path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f'Error loading {path}: {e}')
    return {}

# Load all available translations
for d in ['translations/society/ru_ru.json', 'translations/society/en_us.json']:
    if os.path.exists(d):
        loaded = load_json(d)
        if 'ru_ru' in d:
            ru_dict.update(loaded)
        else:
            en_dict.update(loaded)

for f in glob.glob('translations/mods/*.json'):
    loaded = load_json(f)
    ru_dict.update(loaded)

for root, dirs, files in os.walk('G:/curseforge/minecraft/Instances/Society Sunlit Valley/kubejs/assets'):
    for file in files:
        if file == 'ru_ru.json':
            ru_dict.update(load_json(os.path.join(root, file)))
        elif file == 'en_us.json':
            en_dict.update(load_json(os.path.join(root, file)))

results = []
for idx, (mod, name, orig_id, adv_id) in enumerate(adv_plushies, 1):
    # possible translation keys:
    # block.mod.adv_name, item.mod.adv_name, block.mod.name, item.mod.name
    keys_to_check = [
        f'block.{mod}.adv_{name}',
        f'item.{mod}.adv_{name}',
        f'block.{mod}.{name}',
        f'item.{mod}.{name}',
        f'{mod}.{name}',
        name
    ]
    
    en_name = None
    ru_name = None
    
    for k in keys_to_check:
        if k in en_dict and not en_name:
            en_name = en_dict[k]
        if k in ru_dict and not ru_name:
            ru_name = ru_dict[k]
            
    results.append({
        'num': idx,
        'mod': mod,
        'name': name,
        'orig_id': orig_id,
        'adv_id': adv_id,
        'en_name': en_name,
        'ru_name': ru_name
    })

print(f'\nSample 10 items:')
for r in results[:10]:
    print(f"{r['num']}. {r['adv_id']} | EN: {r['en_name']} | RU: {r['ru_name']}")

with open('tools/plushie_pool_raw.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print('Saved raw data to tools/plushie_pool_raw.json')
