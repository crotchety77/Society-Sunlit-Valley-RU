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
    en_data = json.load(f)

with open(RU_PATH, 'r', encoding='utf-8') as f:
    ru_data = json.load(f)

def get_desc_keys_for_quest(data):
    quests = {}
    for k, v in data.items():
        # Match quest hex id and description index
        # Format 1: ftbquests.chapter.<chap>.quest<HEX>.description<N>
        # Format 2: ftbquestlocalizer.quest.<HEX>.description.<N>
        # Format 3: ftbquests...
        m = re.search(r'quest([0-9A-Fa-f]{16})\.description(\d*)', k, re.IGNORECASE)
        if m:
            qid = m.group(1).upper()
            idx = int(m.group(2)) if m.group(2) else 0
            quests.setdefault(qid, {})[idx] = (k, v)
        else:
            m2 = re.search(r'quest\.([0-9A-Fa-f]{16})\.description\.?(\d*)', k, re.IGNORECASE)
            if m2:
                qid = m2.group(1).upper()
                idx = int(m2.group(2)) if m2.group(2) else 0
                quests.setdefault(qid, {})[idx] = (k, v)
    return quests

def get_quest_titles(data):
    titles = {}
    for k, v in data.items():
        m = re.search(r'quest([0-9A-Fa-f]{16})\.title', k, re.IGNORECASE)
        if m:
            qid = m.group(1).upper()
            titles[qid] = v
        m2 = re.search(r'quest\.([0-9A-Fa-f]{16})\.title', k, re.IGNORECASE)
        if m2:
            qid = m2.group(1).upper()
            titles[qid] = v
    return titles

en_descs = get_desc_keys_for_quest(en_data)
ru_descs = get_desc_keys_for_quest(ru_data)
en_titles = get_quest_titles(en_data)
ru_titles = get_quest_titles(ru_data)

# Let's inspect differences between EN and RU description keys
all_qids = sorted(list(set(list(en_descs.keys()) + list(ru_descs.keys()))))

print(f"Total Unique Quests with descriptions in EN/RU: {len(all_qids)}")

structural_diffs = []
clean_quests = []

for qid in all_qids:
    en_lines = en_descs.get(qid, {})
    ru_lines = ru_descs.get(qid, {})
    title = ru_titles.get(qid) or en_titles.get(qid) or qid
    
    en_len = len(en_lines)
    ru_len = len(ru_lines)
    
    # Check if number of lines differ
    diff = False
    details = []
    
    if en_len != ru_len:
        diff = True
        details.append(f"Число строк: EN={en_len}, RU={ru_len}")
        
    # Check pagebreak count
    en_pb = sum(1 for idx, (_, v) in en_lines.items() if '{@pagebreak}' in v)
    ru_pb = sum(1 for idx, (_, v) in ru_lines.items() if '{@pagebreak}' in v)
    if en_pb != ru_pb:
        diff = True
        details.append(f"Разделители страниц {{@pagebreak}}: EN={en_pb}, RU={ru_pb}")
        
    if diff:
        structural_diffs.append({
            'qid': qid,
            'title': title,
            'en_len': en_len,
            'ru_len': ru_len,
            'en_lines': en_lines,
            'ru_lines': ru_lines,
            'details': details
        })
    else:
        clean_quests.append({
            'qid': qid,
            'title': title,
            'len': en_len
        })

print(f"\n=======================================================")
print(f"РЕЗУЛЬТАТЫ СРАВНЕНИЯ EN vs RU JSON:")
print(f"Квестов со структурными различиями: {len(structural_diffs)}")
print(f"Квестов с чистой/идентичной структурой: {len(clean_quests)}")
print(f"=======================================================\n")

for item in structural_diffs:
    print(f"▶ Квест: '{item['title']}' | ID: {item['qid']}")
    for d in item['details']:
        print(f"  - {d}")
    print("  [EN строки]:")
    for idx in sorted(item['en_lines']):
        print(f"    {item['en_lines'][idx][0]}: {item['en_lines'][idx][1]}")
    print("  [RU строки]:")
    for idx in sorted(item['ru_lines']):
        print(f"    {item['ru_lines'][idx][0]}: {item['ru_lines'][idx][1]}")
    print()
