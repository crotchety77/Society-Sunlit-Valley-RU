#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Добавление тултипа для chimes:glass_bells в KubeJS и языковые файлы
"""

import os
import sys
import json

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
KUBEJS_TOOLTIPS_JS = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\client_scripts\tooltips\addTooltips.js"
GAME_CHIMES_RU = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\chimes\lang\ru_ru.json"
GAME_SOCIETY_RU = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\society\lang\ru_ru.json"
LOCAL_CHIMES_JSON = os.path.join(ROOT_DIR, "translations", "mods", "chimes.json")
LOCAL_SOCIETY_RU = os.path.join(ROOT_DIR, "translations", "society", "ru_ru.json")
TASK_NEW_TRANSLATE = os.path.join(ROOT_DIR, "tasks", "Translate_Mods", "translate_chimes", "new_translate.md")


TOOLTIP_KEY = "item.chimes.glass_bells.description"
TOOLTIP_TEXT = "Покрасьте верх и низ отдельно. Краситель — сверху и снизу в верстаке"


# 1. Update addTooltips.js
if os.path.exists(KUBEJS_TOOLTIPS_JS):
    with open(KUBEJS_TOOLTIPS_JS, 'r', encoding='utf-8') as f:
        js_content = f.read()
        
    if "chimes:glass_bells" not in js_content:
        snippet = '\n  tooltip.add(\n    "chimes:glass_bells",\n    Text.translatable("item.chimes.glass_bells.description").gray()\n  );\n'
        idx = js_content.rfind("});")
        if idx != -1:
            js_content = js_content[:idx] + snippet + js_content[idx:]
            with open(KUBEJS_TOOLTIPS_JS, 'w', encoding='utf-8') as f:
                f.write(js_content)
            print("✅ Добавлен вызов tooltip.add('chimes:glass_bells') в addTooltips.js")
    else:
        print("ℹ️ 'chimes:glass_bells' уже присутствует в addTooltips.js")

# 2. Update JSON files
for path in [GAME_CHIMES_RU, GAME_SOCIETY_RU, LOCAL_CHIMES_JSON, LOCAL_SOCIETY_RU]:
    if os.path.exists(path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            data[TOOLTIP_KEY] = TOOLTIP_TEXT
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"✅ Обновлен: {path}")
        except Exception as e:
            print(f"❌ Ошибка записи {path}: {e}")

# 3. Update new_translate.md
if os.path.exists(TASK_NEW_TRANSLATE):
    with open(TASK_NEW_TRANSLATE, 'r', encoding='utf-8') as f:
        md_content = f.read()
    if TOOLTIP_KEY not in md_content:
        md_content = md_content.replace(
            '"block.chimes.glass_bells": "Японский стеклянный колокольчик (Стеклянный Фурин)",',
            f'"block.chimes.glass_bells": "Японский стеклянный колокольчик (Стеклянный Фурин)",\n  "{TOOLTIP_KEY}": "{TOOLTIP_TEXT}",'
        )
        with open(TASK_NEW_TRANSLATE, 'w', encoding='utf-8') as f:
            f.write(md_content)
        print("✅ new_translate.md обновлен")

print("\n🎉 Тултип успешно добавлен и синхронизирован!")
