import os
import sys
import json
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

GAME_DIR = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\config\ftbquests\quests\chapters'

chapters = ['iii__advanced_farming.snbt', 'longwings.snbt', 'ii__building_up_the_farm.snbt', 'fish_tank.snbt', 'fishing.snbt', 'iv__prismatic_farming.snbt']

for ch in chapters:
    fp = os.path.join(GAME_DIR, ch)
    if os.path.exists(fp):
        with open(fp, 'r', encoding='utf-8') as fh:
            txt = fh.read()
        print(f"\n=================== Chapter: {ch} ===================")
        blocks = txt.split('{\n\t\t\t')
        for b in blocks[1:]:
            qid_m = re.search(r'id:\s*\"([0-9A-Fa-f]+)\"', b)
            qid = qid_m.group(1) if qid_m else 'UNKNOWN'
            title_m = re.search(r'title:\s*\"([^\"]+)\"', b)
            title = title_m.group(1) if title_m else ''
            dm = re.search(r'description:\s*\[([\s\S]*?)\]', b)
            if dm:
                raw_d = dm.group(1)
                lines = re.findall(r'\"((?:\\\"|[^\"])*)\"', raw_d)
                has_pagebreak = any('pagebreak' in l for l in lines)
                has_raw_text = any(not l.startswith('{') and l != '' for l in lines)
                if has_pagebreak or has_raw_text or 'butterfly' in b.lower() or 'pond' in b.lower() or 'longwings' in b.lower() or 'бабочк' in b.lower() or 'пруд' in b.lower():
                    print(f"  QID: {qid} | Title: {title}")
                    print(f"    Lines ({len(lines)}):")
                    for l in lines:
                        print(f"      - {l}")
