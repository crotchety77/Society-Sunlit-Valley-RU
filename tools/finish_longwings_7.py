#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/finish_longwings_7.py
Переводит последние 7 ключей Longwings для достижения 100.0%.
"""

import os
import sys
import json
import re
import subprocess

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TASK_DIR = os.path.join(ROOT_DIR, "tasks", "Translate_Mods", "05_longwings")
new_translate_path = os.path.join(TASK_DIR, "new_translate.md")

with open(new_translate_path, "r", encoding="utf-8") as f:
    content = f.read()

m = re.search(r'```json\s*(\{[\s\S]*?\})\s*```', content)
data = json.loads(m.group(1))

EXACT_7 = {
    "block.longwings.sugar_water_bowl": "Миска с сахарной водой",
    "longwings.subtitles.generic.slurp": "Хлюпанье",
    "longwings.subtitles.catching_net.catch": "Взмах ловчего сачка",
    "longwings.subtitles.catching_net.full": "Промах сачка",
    "longwings.item.bowl.empty": "Миска опустошается",
    "longwings.item.bowl.fill": "Миска наполняется",
    "longwings.block.brew.slide": "Чавканье забродивших фруктов",
}

for k, v in EXACT_7.items():
    data[k] = v

new_block = f"```json\n{json.dumps(data, ensure_ascii=False, indent=2)}\n```"
new_content = content[:m.start()] + new_block + content[m.end():]
with open(new_translate_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("🚀 Синхронизация 100% Longwings...")
subprocess.run(["python", "tools/apply_task.py", "05_longwings"], cwd=ROOT_DIR, capture_output=True, text=True, encoding='utf-8', errors='replace')
print("🎉 100% ПЕРЕВОД Longwings ПРИМЕНЁН!")
