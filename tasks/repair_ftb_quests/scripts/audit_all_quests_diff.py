import os
import sys
import json
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
GAME_DIR = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\config\ftbquests\quests\chapters'
EN_PATH = os.path.join(REPO_ROOT, 'translations', 'ftbquests', 'en_us.json')
RU_PATH = os.path.join(REPO_ROOT, 'translations', 'ftbquests', 'ru_ru.json')

with open(EN_PATH, 'r', encoding='utf-8') as f:
    en_json = json.load(f)

with open(RU_PATH, 'r', encoding='utf-8') as f:
    ru_json = json.load(f)

# Group all keys by their logical base prefix:
# e.g. "ftbquests.chapter.<chap>.quest<ID>"
def group_quest_keys(data):
    grouped = {}
    for k, v in data.items():
        # Match quest key prefix
        m = re.match(r'^(ftbquests\.chapter\.[^.]+\.quest[0-9A-Fa-f]+)\.(.*)$', k)
        if m:
            prefix = m.group(1)
            field = m.group(2)
            grouped.setdefault(prefix, {})[field] = (k, v)
        else:
            # Check other patterns if any
            m2 = re.match(r'^(ftbquestlocalizer\.quest\.[0-9A-Fa-f]+)\.(.*)$', k)
            if m2:
                prefix = m2.group(1)
                field = m2.group(2)
                grouped.setdefault(prefix, {})[field] = (k, v)
    return grouped

en_grouped = group_quest_keys(en_json)
ru_grouped = group_quest_keys(ru_json)

all_prefixes = sorted(list(set(list(en_grouped.keys()) + list(ru_grouped.keys()))))

print(f"Всего квестов в базе локализации: {len(all_prefixes)}")

mismatched_quests = []
clean_quests = []

for pfx in all_prefixes:
    en_fields = en_grouped.get(pfx, {})
    ru_fields = ru_grouped.get(pfx, {})
    
    # Get descriptions
    en_desc = {k: v for k, v in en_fields.items() if k.startswith('description')}
    ru_desc = {k: v for k, v in ru_fields.items() if k.startswith('description')}
    
    # Extract titles
    title_ru = ru_fields.get('title', ('', ''))[1]
    title_en = en_fields.get('title', ('', ''))[1]
    title = title_ru or title_en or pfx
    
    # Differences check:
    diffs = []
    
    if len(en_desc) != len(ru_desc):
        diffs.append(f"Количество строк description: EN={len(en_desc)}, RU={len(ru_desc)}")
        
    # Check key-by-key
    for k in ru_desc:
        if k not in en_desc:
            diffs.append(f"Ключ '{k}' есть в RU, но отсутствует в EN")
    for k in en_desc:
        if k not in ru_desc:
            diffs.append(f"Ключ '{k}' есть в EN, но отсутствует в RU")
            
    # Check pagebreak count
    en_pb = sum(1 for k, (_, v) in en_desc.items() if '{@pagebreak}' in v)
    ru_pb = sum(1 for k, (_, v) in ru_desc.items() if '{@pagebreak}' in v)
    if en_pb != ru_pb:
        diffs.append(f"Количество {{@pagebreak}}: EN={en_pb}, RU={ru_pb}")

    if diffs:
        mismatched_quests.append({
            'prefix': pfx,
            'title': title,
            'diffs': diffs,
            'en_desc': en_desc,
            'ru_desc': ru_desc
        })
    else:
        clean_quests.append({
            'prefix': pfx,
            'title': title,
            'desc_count': len(ru_desc)
        })

print(f"Найдено квестов с несоответствиями: {len(mismatched_quests)}")
print(f"Найдено квестов с полной совместимостью: {len(clean_quests)}")

for item in mismatched_quests:
    print("=" * 70)
    print(f"Квест: '{item['title']}' ({item['prefix']})")
    for d in item['diffs']:
        print(f"  ❌ {d}")
    print("  [EN]:")
    for k in sorted(item['en_desc']):
        print(f"    {k}: {item['en_desc'][k][1]}")
    print("  [RU]:")
    for k in sorted(item['ru_desc']):
        print(f"    {k}: {item['ru_desc'][k][1]}")
