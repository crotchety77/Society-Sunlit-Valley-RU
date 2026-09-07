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

# Let's inspect every single quest across all 30 chapters for {@pagebreak} in SNBT, ru_ru or en_us
all_pb_quests = []

for f in sorted(os.listdir(GAME_DIR)):
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
                
                # Check pagebreaks in SNBT
                pb_snbt = sum(1 for l in lines if '{@pagebreak}' in l)
                
                clean_hex = qid.lstrip('0')
                full_hex = qid.zfill(16)
                
                ru_descs = [v for k, v in ru.items() if (f'quest{clean_hex}.description' in k or f'quest{full_hex}.description' in k) and '{@pagebreak}' in v]
                en_descs = [v for k, v in en.items() if (f'quest{clean_hex}.description' in k or f'quest{full_hex}.description' in k) and '{@pagebreak}' in v]
                
                if pb_snbt > 0 or len(ru_descs) > 0 or len(en_descs) > 0:
                    title = ""
                    for k in [f'ftbquests.chapter.{f[:-5]}.quest{qid}.title', f'ftbquests.chapter.{f[:-5]}.quest{clean_hex}.title']:
                        if k in ru:
                            title = ru[k]
                            break
                        if k in en:
                            title = en[k]
                            break
                    if not title:
                        tm = re.search(r'title:\s*\"([^\"]+)\"', b)
                        title = tm.group(1) if tm else qid
                        
                    all_pb_quests.append({
                        'file': f,
                        'qid': qid,
                        'title': title,
                        'pb_snbt': pb_snbt,
                        'lines': lines
                    })

print(f"Всего квестов с {{@pagebreak}}: {len(all_pb_quests)}")
for q in all_pb_quests:
    print(f"\n[{q['file']}] QID: {q['qid']} | «{q['title']}» (Разрывов страниц в SNBT: {q['pb_snbt']})")
    for l in q['lines']:
        print(f"   - {l}")
