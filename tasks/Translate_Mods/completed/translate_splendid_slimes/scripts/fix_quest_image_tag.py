#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

ROOT_DIR = r"c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода"
QUESTS_MD = os.path.join(ROOT_DIR, "tasks", "Translate_Mods", "translate_splendid_slimes", "quests_translate.md")
LOCAL_FTB_RU = os.path.join(ROOT_DIR, "translations", "ftbquests", "ru_ru.json")
GAME_FTB_RU = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\ftbquestlocalizer\lang\ru_ru.json"
QUEUE_P3 = os.path.join(ROOT_DIR, "tasks", "FTB_QUESTS_4_1_4", "work_queue", "priority3_partially_translated.md")

clean_desc3 = "Ухаживать за ними проще, чем за скотом, хотя порой они создают куда больше хаоса...\n\nЧтобы определить породу Слайма, воспользуйтесь &6Анализатором слаймов&r!"

# 1. Update quests_translate.md
if os.path.exists(QUESTS_MD):
    with open(QUESTS_MD, 'r', encoding='utf-8') as f:
        md = f.read()
    
    # Replace in visual Block 1
    md = re.sub(
        r'> Чтобы определить породу Слайма, воспользуйтесь.*?&6Анализатором слаймов&r!',
        r'> Чтобы определить породу Слайма, воспользуйтесь &6Анализатором слаймов&r!',
        md
    )
    
    # Replace in JSON Block 2
    md = re.sub(
        r'(\"ftbquests\.chapter\.iii__advanced_farming\.quest632578AFE8A0D12D\.description3\":\s*\").*?(\",)',
        f'\\g<1>{clean_desc3}\\g<2>',
        md
    )
    
    with open(QUESTS_MD, 'w', encoding='utf-8') as f:
        f.write(md)
    print("✅ Обновлён quests_translate.md (убран неподдерживаемый инлайн-тег image)")

# 2. Update translations/ftbquests/ru_ru.json
with open(LOCAL_FTB_RU, 'r', encoding='utf-8') as f:
    ru = json.load(f)
ru["ftbquests.chapter.iii__advanced_farming.quest632578AFE8A0D12D.description3"] = clean_desc3
with open(LOCAL_FTB_RU, 'w', encoding='utf-8') as f:
    json.dump(ru, f, ensure_ascii=False, indent=2)
print(f"✅ Обновлён {LOCAL_FTB_RU}")

# 3. Update game ftbquestlocalizer ru_ru.json
with open(GAME_FTB_RU, 'r', encoding='utf-8') as f:
    game_ru = json.load(f)
game_ru["ftbquests.chapter.iii__advanced_farming.quest632578AFE8A0D12D.description3"] = clean_desc3
with open(GAME_FTB_RU, 'w', encoding='utf-8') as f:
    json.dump(game_ru, f, ensure_ascii=False, indent=2)
print(f"✅ Записано в файл игры: {GAME_FTB_RU}")

# 4. Update priority3_partially_translated.md
if os.path.exists(QUEUE_P3):
    with open(QUEUE_P3, 'r', encoding='utf-8') as f:
        p3 = f.read()
    p3 = re.sub(
        r'(\"ftbquests\.chapter\.iii__advanced_farming\.quest632578AFE8A0D12D\.description3\":\s*\").*?(\")',
        f'\\g<1>{clean_desc3}\\g<2>',
        p3
    )
    with open(QUEUE_P3, 'w', encoding='utf-8') as f:
        f.write(p3)
    print(f"✅ Синхронизирована очередь: {QUEUE_P3}")

