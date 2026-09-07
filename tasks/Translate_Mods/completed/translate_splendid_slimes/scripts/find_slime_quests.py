#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import glob
import re
import json

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

CHAPTERS_DIR = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\config\ftbquests\quests\chapters"
RU_LOCALIZER = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\ftbquestlocalizer\lang\ru_ru.json"
EN_LOCALIZER = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\ftbquestlocalizer\lang\en_us.json"

ru_data = json.load(open(RU_LOCALIZER, 'r', encoding='utf-8'))
en_data = json.load(open(EN_LOCALIZER, 'r', encoding='utf-8'))

keywords = ['splendid_slimes', 'slime_vac', 'plort', 'slime_incubator', 'plort_press', 'plort_rippit', 'rocket_pod', 'slime_inspector', 'slime_ticket', 'largo', 'tarr']

found_quests = {}

for p in glob.glob(os.path.join(CHAPTERS_DIR, '*.snbt')):
    chap = os.path.basename(p).replace('.snbt', '')
    content = open(p, 'r', encoding='utf-8', errors='ignore').read()
    
    # find all quest id positions
    for m in re.finditer(r'id:\s*"([0-9A-Fa-f]{16})"', content):
        qid = m.group(1)
        # get chunk
        start = max(0, m.start() - 100)
        end = min(len(content), m.end() + 1500)
        chunk = content[start:end]
        
        # check if chunk matches keywords
        matches = [kw for kw in keywords if kw in chunk.lower()]
        if matches:
            found_quests[qid] = {
                'chapter': chap,
                'matched_keywords': matches
            }

print(f"Total Quests Found: {len(found_quests)}")
for qid, info in sorted(found_quests.items(), key=lambda x: x[1]['chapter']):
    chap = info['chapter']
    title_key = f"ftbquests.chapter.{chap}.quest{qid}.title"
    title_ru = ru_data.get(title_key, "---")
    title_en = en_data.get(title_key, "---")
    print(f"[{chap}] Quest {qid}:")
    print(f"   EN Title: {title_en}")
    print(f"   RU Title: {title_ru}")
    print(f"   Matches: {info['matched_keywords']}")
    
    # print keys
    keys = [k for k in ru_data if f"quest{qid}" in k]
    for k in sorted(keys):
        print(f"      ▪ {k}:")
        print(f"         EN: {en_data.get(k, '')}")
        print(f"         RU: {ru_data.get(k, '')}")
    print()
