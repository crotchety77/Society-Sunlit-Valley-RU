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
    en = json.load(f)
with open(RU_PATH, 'r', encoding='utf-8') as f:
    ru = json.load(f)

# Let's search all quests containing pagebreak in SNBT across all chapters
print("=== All Quests with {@pagebreak} in SNBT ===")
for f in os.listdir(GAME_DIR):
    if f.endswith('.snbt'):
        fp = os.path.join(GAME_DIR, f)
        with open(fp, 'r', encoding='utf-8') as fh:
            txt = fh.read()
            
        blocks = txt.split('{\n\t\t\t')
        for b in blocks[1:]:
            qid_m = re.search(r'id:\s*\"([0-9A-Fa-f]+)\"', b)
            qid = qid_m.group(1) if qid_m else ''
            
            dm = re.search(r'description:\s*\[([\s\S]*?)\]', b)
            if dm:
                raw_d = dm.group(1)
                lines = re.findall(r'\"((?:\\\"|[^\"])*)\"', raw_d)
                
                # Check for pagebreak or fish pond / fishing / butterfly in this block
                has_pb = any('pagebreak' in l for l in lines)
                has_pond = 'pond' in raw_d.lower() or 'пруд' in raw_d.lower() or 'fish' in raw_d.lower() or 'рыб' in raw_d.lower()
                
                if has_pb or has_pond:
                    # Title
                    title = ""
                    for k in [f"ftbquests.chapter.{f[:-5]}.quest{qid}.title", f"ftbquests.chapter.{f[:-5]}.quest{qid.lstrip('0')}.title"]:
                        if k in ru:
                            title = ru[k]
                            break
                        if k in en:
                            title = en[k]
                            break
                    if not title:
                        tm = re.search(r'title:\s*\"([^\"]+)\"', b)
                        title = tm.group(1) if tm else qid
                    
                    print(f"\n[{f}] QID: {qid} | «{title}» (has_pb={has_pb})")
                    print("  SNBT lines:")
                    for l in lines:
                        print(f"    - {l}")
                    print("  EN keys:")
                    for k in sorted(en):
                        if qid.lower() in k.lower() or (qid.lstrip('0') and qid.lstrip('0').lower() in k.lower()):
                            print(f"    {k}: {en[k]}")
                    print("  RU keys:")
                    for k in sorted(ru):
                        if qid.lower() in k.lower() or (qid.lstrip('0') and qid.lstrip('0').lower() in k.lower()):
                            print(f"    {k}: {ru[k]}")
