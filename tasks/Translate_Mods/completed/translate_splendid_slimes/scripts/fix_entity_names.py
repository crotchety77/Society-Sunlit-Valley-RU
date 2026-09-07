#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

ROOT_DIR = r"c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода"
MOD_JSON = os.path.join(ROOT_DIR, "translations", "mods", "splendid_slimes.json")
GAME_JSON = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\splendid_slimes\lang\ru_ru.json"
NEW_TRANSLATE_MD = os.path.join(ROOT_DIR, "tasks", "Translate_Mods", "translate_splendid_slimes", "new_translate.md")

# 1. Update translations/mods/splendid_slimes.json
with open(MOD_JSON, 'r', encoding='utf-8') as f:
    d = json.load(f)

d["entity.splendid_slimes.splendid_slime"] = "Слайм"
d["entity.splendid_slimes.largo_splendid_slime"] = "Слайм Ларго"

with open(MOD_JSON, 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
print("✅ Обновлён translations/mods/splendid_slimes.json")

# 2. Update game file
with open(GAME_JSON, 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
print("✅ Записано напрямую в игру:", GAME_JSON)

# 3. Update new_translate.md
if os.path.exists(NEW_TRANSLATE_MD):
    with open(NEW_TRANSLATE_MD, 'r', encoding='utf-8') as f:
        md = f.read()
    md = md.replace('"entity.splendid_slimes.splendid_slime": "Замечательный слизень"', '"entity.splendid_slimes.splendid_slime": "Слайм"')
    md = md.replace('"entity.splendid_slimes.largo_splendid_slime": "Слизень Ларго"', '"entity.splendid_slimes.largo_splendid_slime": "Слайм Ларго"')
    with open(NEW_TRANSLATE_MD, 'w', encoding='utf-8') as f:
        f.write(md)
    print("✅ Обновлён new_translate.md")
