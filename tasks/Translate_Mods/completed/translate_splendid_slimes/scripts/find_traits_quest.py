#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import glob
import json
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

ROOT_DIR = r"c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода"
RU_PATH = os.path.join(ROOT_DIR, "translations", "ftbquests", "ru_ru.json")
EN_PATH = os.path.join(ROOT_DIR, "translations", "ftbquests", "en_us.json")

ru = json.load(open(RU_PATH, 'r', encoding='utf-8'))
en = json.load(open(EN_PATH, 'r', encoding='utf-8'))

print("=== Поиск в FTB Quests (traits, черты, великолепный слизень) ===")
for k, v in ru.items():
    v_str = str(v).lower()
    if 'черт' in v_str or 'великолепн' in v_str or 'trait' in str(en.get(k, '')).lower():
        if 'slime' in str(en.get(k, '')).lower() or 'слиз' in v_str or 'слайм' in v_str:
            print(f"[{k}]")
            print(f"   EN: {en.get(k)}")
            print(f"   RU: {v}")
            print()

CHAPTERS_DIR = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\config\ftbquests\quests\chapters"
for p in glob.glob(os.path.join(CHAPTERS_DIR, "*.snbt")):
    chap = os.path.basename(p).replace(".snbt", "")
    content = open(p, 'r', encoding='utf-8', errors='ignore').read()
    if 'trait' in content.lower():
        print(f"Match 'trait' in chapter: {chap}")
        for m in re.finditer(r'id:\s*"([0-9A-Fa-f]{16})"', content):
            qid = m.group(1)
            ctx = content[max(0, m.start()-50):min(len(content), m.end()+800)]
            if 'trait' in ctx.lower() or 'inspector' in ctx.lower():
                print(f"   Quest ID: {qid}")
                for k in ru:
                    if f"quest{qid}" in k:
                        print(f"      {k} -> EN: {en.get(k)} | RU: {ru.get(k)}")
