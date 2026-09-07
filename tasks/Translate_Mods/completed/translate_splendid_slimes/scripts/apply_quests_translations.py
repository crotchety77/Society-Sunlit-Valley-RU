#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Применение перевода квестов Слаймоводства во все слои проекта:
1. translations/ftbquests/ru_ru.json
2. kubejs/assets/ftbquestlocalizer/lang/ru_ru.json
3. tasks/FTB_QUESTS_4_1_4/work_queue/priority3_partially_translated.md
4. tasks/FTB_QUESTS_4_1_4/registry_quests.json
"""

import os
import sys
import json
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

TASK_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ROOT_DIR = os.path.abspath(os.path.join(TASK_DIR, "..", "..", ".."))
QUESTS_MD = os.path.join(TASK_DIR, "quests_translate.md")

LOCAL_FTB_RU = os.path.join(ROOT_DIR, "translations", "ftbquests", "ru_ru.json")
GAME_FTB_RU = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\ftbquestlocalizer\lang\ru_ru.json"



QUEUE_P3 = os.path.join(ROOT_DIR, "tasks", "FTB_QUESTS_4_1_4", "work_queue", "priority3_partially_translated.md")
REG_JSON = os.path.join(ROOT_DIR, "tasks", "FTB_QUESTS_4_1_4", "registry_quests.json")

# 1. Parse JSON from quests_translate.md
with open(QUESTS_MD, 'r', encoding='utf-8') as f:
    content = f.read()

json_blocks = re.findall(r'```json\s*(\{.*?\})\s*```', content, re.DOTALL)
if not json_blocks:
    print("❌ Не найден JSON блок в quests_translate.md")
    sys.exit(1)

new_keys = json.loads(json_blocks[0])
print(f"📦 Считано {len(new_keys)} ключей квестов из quests_translate.md")

# 2. Update translations/ftbquests/ru_ru.json
with open(LOCAL_FTB_RU, 'r', encoding='utf-8') as f:
    ftb_ru = json.load(f)
ftb_ru.update(new_keys)
with open(LOCAL_FTB_RU, 'w', encoding='utf-8') as f:
    json.dump(ftb_ru, f, ensure_ascii=False, indent=2)
print(f"✅ Обновлён {LOCAL_FTB_RU}")

# 3. Update game ftbquestlocalizer ru_ru.json
with open(GAME_FTB_RU, 'r', encoding='utf-8') as f:
    game_ru = json.load(f)
game_ru.update(new_keys)
with open(GAME_FTB_RU, 'w', encoding='utf-8') as f:
    json.dump(game_ru, f, ensure_ascii=False, indent=2)
print(f"✅ Записано напрямую в игру: {GAME_FTB_RU}")

# 4. Update priority3_partially_translated.md
if os.path.exists(QUEUE_P3):
    with open(QUEUE_P3, 'r', encoding='utf-8') as f:
        p3_content = f.read()
    # Update translated values
    for k, v in new_keys.items():
        if k in p3_content:
            p3_content = re.sub(
                rf'(\"{re.escape(k)}\":\s*\")(.*?)(\")',
                rf'\g<1>{v}\g<3>',
                p3_content
            )
    with open(QUEUE_P3, 'w', encoding='utf-8') as f:
        f.write(p3_content)
    print(f"✅ Синхронизирована очередь: {QUEUE_P3}")

# 5. Update registry_quests.json
if os.path.exists(REG_JSON):
    with open(REG_JSON, 'r', encoding='utf-8') as f:
        reg_data = json.load(f)
    # Check if any quest titles updated
    for qid in ['632578AFE8A0D12D', '41029F073ADDDC2F', '747B28CA5F55AFA7', '668AEE0B5CD49EE4', '2C9C87690BD8E23B', '4ABFC024D15BFC10', '3225DF52212FAF3E', '2E7D98DEB5012260']:
        title_key = next((k for k in new_keys if f"quest{qid}.title" in k), None)
        if title_key and qid in reg_data:
            reg_data[qid]['ru_title'] = new_keys[title_key]
    with open(REG_JSON, 'w', encoding='utf-8') as f:
        json.dump(reg_data, f, ensure_ascii=False, indent=2)
    print(f"✅ Обновлён реестр квестов: {REG_JSON}")

print("\n🎉 Все слои проекта успешно обновлены новыми терминами квестов!")
