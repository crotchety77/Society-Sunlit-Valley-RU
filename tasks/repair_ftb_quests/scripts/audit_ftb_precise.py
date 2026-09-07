import os
import sys
import json
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

GAME_DIR = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\config\ftbquests\quests\chapters'
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
EN_PATH = os.path.join(REPO_ROOT, 'translations', 'ftbquests', 'en_us.json')
RU_PATH = os.path.join(REPO_ROOT, 'translations', 'ftbquests', 'ru_ru.json')

with open(EN_PATH, 'r', encoding='utf-8') as f:
    en_json = json.load(f)

with open(RU_PATH, 'r', encoding='utf-8') as f:
    ru_json = json.load(f)

snbt_files = [f for f in os.listdir(GAME_DIR) if f.endswith('.snbt')]

# Let's parse all SNBT quests precisely
all_quests = []

for fname in sorted(snbt_files):
    fpath = os.path.join(GAME_DIR, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find chapter id
    chap_m = re.search(r'id:\s*\"([0-9A-Fa-f]+)\"', content)
    chapter_id = chap_m.group(1) if chap_m else fname

    # We match each quest object in the SNBT
    # A quest starts with {\n\t\t\t (or similar indentation) and contains id: "HEX"
    # Let's split on `id: "`
    # Better: find all quest id positions and slice
    matches = list(re.finditer(r'id:\s*\"([0-9A-Fa-f]+)\"', content))
    # Filter out task/reward ids (usually quests are top level in quests: [ ... ])
    # In FTB quests, each quest block has id: "HEX", x: ..., y: ...
    # Let's extract quest blocks
    
    # We can also parse SNBT description references directly!
    # Pattern: {ftbquests.chapter.<chap>.quest<ID>.description<N>}
    desc_blocks = list(re.finditer(r'description:\s*\[([\s\S]*?)\]', content))
    for db in desc_blocks:
        block_text = db.group(1)
        # Find quest ID preceding or following this description block
        # Look backwards from db.start() for the nearest quest id or look forward
        snippet = content[max(0, db.start() - 300):min(len(content), db.end() + 300)]
        
        # Find all keys inside description: [ ... ]
        keys_in_desc = re.findall(r'\"\{?([a-zA-Z0-9_\.]+)\}?\"', block_text)
        raw_lines = [l.strip().strip('"') for l in block_text.strip().split('\n') if l.strip()]
        
        # Find quest ID in snippet
        q_id_match = re.search(r'id:\s*\"([0-9A-Fa-f]{15,16})\"', snippet)
        qid = q_id_match.group(1) if q_id_match else "UNKNOWN"
        
        # Find quest title
        title_match = re.search(r'title:\s*\"([^\"]+)\"', snippet)
        title_in_snbt = title_match.group(1) if title_match else ""
        
        all_quests.append({
            'chapter_file': fname,
            'qid': qid,
            'title_in_snbt': title_in_snbt,
            'snbt_raw_lines': raw_lines,
            'snbt_keys': keys_in_desc
        })

print(f"Total quests with descriptions found in SNBT: {len(all_quests)}")

# Now for each quest, check:
# 1. Keys referenced in SNBT
# 2. Values in en_us.json for those keys
# 3. Values in ru_ru.json for those keys
# 4. Any keys in ru_ru.json that exist for this quest but are NOT in SNBT or NOT in EN
# 5. Any structural mismatch

problematic_quests = []
clean_quests = []

for q in all_quests:
    qid = q['qid']
    keys = q['snbt_keys']
    
    # Find all keys in en_json and ru_json for this quest ID (checking both full and stripped hex)
    hex_clean = qid.lstrip('0')
    hex_full = qid.zfill(16)
    
    def find_quest_keys(data):
        found = {}
        for k, v in data.items():
            if f"quest{hex_clean}.description" in k or f"quest{hex_full}.description" in k or f"quest{qid}.description" in k or f"quest.{hex_clean}.description" in k:
                # Extract index
                m = re.search(r'description\.?(\d*)', k)
                idx = int(m.group(1)) if m and m.group(1) else 1
                found[idx] = (k, v)
        return found
        
    en_k = find_quest_keys(en_json)
    ru_k = find_quest_keys(ru_json)
    
    # Let's inspect differences
    issues = []
    
    # Check 1: Key count mismatch between EN and RU
    if len(en_k) != len(ru_k):
        issues.append(f"Количество ключей описания: EN={len(en_k)}, RU={len(ru_k)}")
        
    # Check 2: Extra keys in RU that are not referenced in SNBT
    for idx, (rk, rv) in ru_k.items():
        if rk not in [k.replace('{', '').replace('}', '') for k in keys] and len(keys) > 0:
            # Check if it's missing in SNBT
            if len(en_k) > 0 and idx not in en_k:
                issues.append(f"Ключ {rk} есть в RU, но отсутствует в EN и в структуре SNBT")
                
    # Check 3: Pagebreak mismatch
    en_pb = sum(1 for idx, (_, v) in en_k.items() if '{@pagebreak}' in v)
    ru_pb = sum(1 for idx, (_, v) in ru_k.items() if '{@pagebreak}' in v)
    if en_pb != ru_pb:
        issues.append(f"Разделители страниц {{@pagebreak}}: EN={en_pb}, RU={ru_pb}")
        
    # Get title
    title_ru = ""
    for k, v in ru_json.items():
        if f"quest{hex_clean}.title" in k or f"quest{hex_full}.title" in k or f"quest{qid}.title" in k:
            title_ru = v
            break
    title_en = ""
    for k, v in en_json.items():
        if f"quest{hex_clean}.title" in k or f"quest{hex_full}.title" in k or f"quest{qid}.title" in k:
            title_en = v
            break
    q_title = title_ru or title_en or q['title_in_snbt'] or qid
    
    if issues:
        problematic_quests.append({
            'file': q['chapter_file'],
            'qid': qid,
            'title': q_title,
            'issues': issues,
            'snbt_keys': keys,
            'en_k': en_k,
            'ru_k': ru_k
        })
    else:
        clean_quests.append({
            'file': q['chapter_file'],
            'qid': qid,
            'title': q_title,
            'lines_count': len(ru_k) if ru_k else len(keys)
        })

print(f"\nАудит завершен!")
print(f"Всего проблемных квестов: {len(problematic_quests)}")
print(f"Всего чистых квестов: {len(clean_quests)}")

for pq in problematic_quests:
    print(f"\n=======================================================")
    print(f"Файл: {pq['file']} | ID: {pq['qid']} | Название: {pq['title']}")
    for iss in pq['issues']:
        print(f"  ❌ {iss}")
    print("  SNBT ключи/строки:")
    for sk in pq['snbt_keys']:
        print(f"    - {sk}")
    print("  EN ключи:")
    for idx in sorted(pq['en_k']):
        print(f"    [{idx}] {pq['en_k'][idx][0]}: {pq['en_k'][idx][1]}")
    print("  RU ключи:")
    for idx in sorted(pq['ru_k']):
        print(f"    [{idx}] {pq['ru_k'][idx][0]}: {pq['ru_k'][idx][1]}")
