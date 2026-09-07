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

# Build map of all active quests across 30 chapters in game
snbt_files = sorted([f for f in os.listdir(GAME_DIR) if f.endswith('.snbt')])

active_quests = {}
for sf in snbt_files:
    p = os.path.join(GAME_DIR, sf)
    with open(p, 'r', encoding='utf-8') as f:
        txt = f.read()
        
    # Find all quest blocks
    # Splitting by "id: \""
    for b in txt.split('id: "')[1:]:
        m = re.match(r'^([0-9A-Fa-f]{16})\"', b)
        if not m:
            continue
        qid = m.group(1).upper()
        # Find description block
        dm = re.search(r'description:\s*\[([\s\S]*?)\]', b)
        desc_raw = dm.group(1) if dm else ""
        keys_or_lines = re.findall(r'\"((?:\\\"|[^\"])*)\"', desc_raw)
        
        # Title
        tm = re.search(r'title:\s*\"([^\"]*)\"', b)
        title_snbt = tm.group(1) if tm else ""
        
        active_quests[qid] = {
            'chapter_file': sf,
            'title_snbt': title_snbt,
            'snbt_lines': keys_or_lines
        }

print(f"Total active quests in SNBT chapters: {len(active_quests)}")

# Analyze each active quest for structural integrity
structural_issues = []
clean_active_quests = []

for qid, qdata in sorted(active_quests.items()):
    clean_hex = qid.lstrip('0')
    full_hex = qid.zfill(16)
    
    # Extract EN keys
    en_desc = {}
    for k, v in en_json.items():
        if f"quest{clean_hex}.description" in k or f"quest{full_hex}.description" in k or f"quest{qid}.description" in k:
            m = re.search(r'description\.?(\d*)', k)
            idx = int(m.group(1)) if m and m.group(1) else 1
            en_desc[idx] = (k, v)
            
    # Extract RU keys
    ru_desc = {}
    for k, v in ru_json.items():
        if f"quest{clean_hex}.description" in k or f"quest{full_hex}.description" in k or f"quest{qid}.description" in k:
            m = re.search(r'description\.?(\d*)', k)
            idx = int(m.group(1)) if m and m.group(1) else 1
            ru_desc[idx] = (k, v)
            
    # Quest title
    title_ru = ""
    for k, v in ru_json.items():
        if f"quest{clean_hex}.title" in k or f"quest{full_hex}.title" in k or f"quest{qid}.title" in k:
            title_ru = v
            break
    title_en = ""
    for k, v in en_json.items():
        if f"quest{clean_hex}.title" in k or f"quest{full_hex}.title" in k or f"quest{qid}.title" in k:
            title_en = v
            break
    title = title_ru or title_en or qdata['title_snbt'] or qid
    
    # Filter snbt keys that are actually localization keys (skip empty string dividers "")
    loc_keys_in_snbt = [k for k in qdata['snbt_lines'] if k.startswith('{') and k.endswith('}')]
    raw_lines_in_snbt = [k for k in qdata['snbt_lines'] if not (k.startswith('{') and k.endswith('}')) and k != ""]
    
    issues = []
    
    # 1. Structural mismatch between EN and RU
    if len(en_desc) > 0 and len(ru_desc) > 0 and len(en_desc) != len(ru_desc):
        issues.append(f"Несовпадение количества ключей: EN={len(en_desc)} vs RU={len(ru_desc)}")
        
    # 2. Check if SNBT references keys that don't match EN or RU
    snbt_key_count = len(loc_keys_in_snbt)
    if snbt_key_count > 0 and len(en_desc) > 0 and snbt_key_count != len(en_desc):
        issues.append(f"Количество ключей в SNBT ({snbt_key_count}) отличается от EN ({len(en_desc)})")
        
    # 3. Extra key in RU that is ignored by original SNBT
    if len(ru_desc) > len(en_desc) and len(en_desc) > 0:
        issues.append(f"В RU добавлено {len(ru_desc) - len(en_desc)} лишних абзацев, которые не отобразятся на оригинальной сборке")
        
    # 4. Check for pagebreaks
    en_pb = sum(1 for idx, (_, v) in en_desc.items() if '{@pagebreak}' in v)
    ru_pb = sum(1 for idx, (_, v) in ru_desc.items() if '{@pagebreak}' in v)
    if en_pb != ru_pb:
        issues.append(f"Несовпадение переносов страниц {{@pagebreak}}: EN={en_pb}, RU={ru_pb}")
        
    if issues:
        structural_issues.append({
            'qid': qid,
            'title': title,
            'chapter': qdata['chapter_file'],
            'issues': issues,
            'en_desc': en_desc,
            'ru_desc': ru_desc,
            'snbt_lines': qdata['snbt_lines'],
            'loc_keys_in_snbt': loc_keys_in_snbt,
            'raw_lines_in_snbt': raw_lines_in_snbt
        })
    else:
        clean_active_quests.append({
            'qid': qid,
            'title': title,
            'chapter': qdata['chapter_file'],
            'desc_count': len(ru_desc) if ru_desc else len(en_desc)
        })

print(f"\n==================================================")
print(f"АКТИВНЫЕ КВЕСТЫ СО СТРУКТУРНЫМИ ИЗМЕНЕНИЯМИ: {len(structural_issues)}")
print(f"АКТИВНЫЕ КВЕСТЫ БЕЗ СТРУКТУРНЫХ ПРОБЛЕМ: {len(clean_active_quests)}")
print(f"==================================================\n")

for item in structural_issues:
    print(f"▶ [{item['chapter']}] ID: {item['qid']} | «{item['title']}»")
    for iss in item['issues']:
        print(f"   ⚠️ {iss}")
    print("   [Оригинал EN]:")
    for idx in sorted(item['en_desc']):
        print(f"      {item['en_desc'][idx][0]}: {item['en_desc'][idx][1]}")
    print("   [Наш перевод RU]:")
    for idx in sorted(item['ru_desc']):
        print(f"      {item['ru_desc'][idx][0]}: {item['ru_desc'][idx][1]}")
    print("   [Структура SNBT]:")
    for l in item['snbt_lines']:
        print(f"      - {repr(l)}")
    print()
