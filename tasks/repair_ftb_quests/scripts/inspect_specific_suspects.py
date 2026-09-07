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

check_qids = [
    '263CCA4D2EAF2629', # Бабочки (Butterfly Breeding)
    '17C8B0197B8636E7', # Пчелы / Фермерство
    '3DE36C9FBCB58800', # Бабочки / Растения
    '632578AFE8A0D12D', # Слизни (Splendid Slimes)
    '3E08F21BA8F69499', # Подарки жителям (Gift Giving)
    '41C453E806763C4F', # Улучшения машин
    '18490F31FFAB134E', # Для владельцев серверов
    '6FE9F992ACD90629', # Рыбный пруд (Farming Fish)
]

for qid in check_qids:
    clean = qid.lstrip('0')
    print(f"\n=======================================================")
    print(f"CHECKING QID: {qid}")
    
    # Find in SNBT
    snbt_found = False
    for f in os.listdir(GAME_DIR):
        if f.endswith('.snbt'):
            fp = os.path.join(GAME_DIR, f)
            with open(fp, 'r', encoding='utf-8') as fh:
                txt = fh.read()
            if qid.lower() in txt.lower():
                snbt_found = True
                print(f"  Located in chapter file: {f}")
                # Print description block
                idx = txt.lower().find(qid.lower())
                sub = txt[max(0, idx-100):min(len(txt), idx+600)]
                dm = re.search(r'description:\s*\[([\s\S]*?)\]', sub)
                if dm:
                    print("  SNBT description block:")
                    for line in dm.group(1).strip().split('\n'):
                        print(f"    {line}")
                break
    if not snbt_found:
        print("  ❌ NOT FOUND IN ANY SNBT FILE!")
        
    print("  [EN keys]:")
    for k in sorted(en):
        if qid.lower() in k.lower() or (clean and clean.lower() in k.lower()):
            print(f"    {k}: {en[k]}")
    print("  [RU keys]:")
    for k in sorted(ru):
        if qid.lower() in k.lower() or (clean and clean.lower() in k.lower()):
            print(f"    {k}: {ru[k]}")
