import os
import sys
import json
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
EN_PATH = os.path.join(REPO_ROOT, 'translations', 'ftbquests', 'en_us.json')
RU_PATH = os.path.join(REPO_ROOT, 'translations', 'ftbquests', 'ru_ru.json')
GAME_DIR = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\config\ftbquests\quests\chapters'

with open(EN_PATH, 'r', encoding='utf-8') as f:
    en = json.load(f)
with open(RU_PATH, 'r', encoding='utf-8') as f:
    ru = json.load(f)

for ch_name in ['fishing.snbt', 'fish_tank.snbt']:
    fpath = os.path.join(GAME_DIR, ch_name)
    with open(fpath, 'r', encoding='utf-8') as f:
        txt = f.read()

    print(f"\n=================== CHAPTER: {ch_name} ===================")
    blocks = txt.split('{\n\t\t\tid: "')
    for b in blocks[1:]:
        qid_m = re.match(r'^([0-9A-Fa-f]+)\"', b)
        qid = qid_m.group(1) if qid_m else ''
        clean = qid.lstrip('0')
        title = ru.get(f'ftbquests.chapter.{ch_name[:-5]}.quest{qid}.title', ru.get(f'ftbquests.chapter.{ch_name[:-5]}.quest{clean}.title', ''))
        
        dm = re.search(r'description:\s*\[([\s\S]*?)\]', b)
        lines = re.findall(r'\"((?:\\\"|[^\"])*)\"', dm.group(1)) if dm else []
        
        print(f"QID: {qid} | «{title}» | Lines in SNBT: {len(lines)}")
        for l in lines:
            print(f"   - {l}")
