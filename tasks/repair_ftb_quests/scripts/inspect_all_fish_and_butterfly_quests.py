import os
import sys
import json
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
EN_PATH = os.path.join(REPO_ROOT, 'translations', 'ftbquests', 'en_us.json')
RU_PATH = os.path.join(REPO_ROOT, 'translations', 'ftbquests', 'ru_ru.json')

with open(EN_PATH, 'r', encoding='utf-8') as f:
    en = json.load(f)
with open(RU_PATH, 'r', encoding='utf-8') as f:
    ru = json.load(f)

# Let's search all quests mentioning fish pond / пруд in ru or en
pond_quests = set()
for k, v in ru.items():
    if ('пруд' in v.lower() or 'рыбн' in v.lower() or 'икр' in v.lower() or 'бабочк' in v.lower()) and 'description' in k:
        m = re.search(r'quest([0-9A-Fa-f]+)', k)
        if m:
            pond_quests.add(m.group(1))

for k, v in en.items():
    if ('pond' in v.lower() or 'fish' in v.lower() or 'butterfly' in v.lower()) and 'description' in k:
        m = re.search(r'quest([0-9A-Fa-f]+)', k)
        if m:
            pond_quests.add(m.group(1))

print(f"Total related quests found: {len(pond_quests)}")
for qid in sorted(pond_quests):
    clean = qid.lstrip('0')
    en_keys = {k: v for k, v in en.items() if (qid.lower() in k.lower() or clean.lower() in k.lower()) and 'description' in k}
    ru_keys = {k: v for k, v in ru.items() if (qid.lower() in k.lower() or clean.lower() in k.lower()) and 'description' in k}
    
    # Check if text length or content differs substantially (e.g. extra instructions added)
    title_ru = [v for k, v in ru.items() if (qid.lower() in k.lower() or clean.lower() in k.lower()) and 'title' in k]
    title = title_ru[0] if title_ru else qid
    
    print(f"\n=======================================================")
    print(f"QID: {qid} | «{title}» | EN lines: {len(en_keys)}, RU lines: {len(ru_keys)}")
    print("  [EN]:")
    for k in sorted(en_keys):
        print(f"    {k}: {en_keys[k]}")
    print("  [RU]:")
    for k in sorted(ru_keys):
        print(f"    {k}: {ru_keys[k]}")
