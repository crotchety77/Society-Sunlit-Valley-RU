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

qid = '632578AFE8A0D12D'
print(f"=== QID {qid} ===")
for k in sorted(en):
    if qid.lower() in k.lower():
        print(f"EN: {k} -> {en[k]}")
for k in sorted(ru):
    if qid.lower() in k.lower():
        print(f"RU: {k} -> {ru[k]}")

# Find in SNBT
for f in os.listdir(GAME_DIR):
    if f.endswith('.snbt'):
        fp = os.path.join(GAME_DIR, f)
        with open(fp, 'r', encoding='utf-8') as fh:
            txt = fh.read()
        if qid.lower() in txt.lower():
            print(f"Found in {f}:")
            idx = txt.lower().find(qid.lower())
            print(txt[max(0, idx-50):min(len(txt), idx+400)])
