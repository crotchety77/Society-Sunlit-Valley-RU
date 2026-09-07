#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Добавление атмосферных тултипов для ночников (лягушки, грибы, осьминоги) в KubeJS и ru_ru.json
"""

import os
import sys
import json

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
KUBEJS_TOOLTIPS_JS = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\client_scripts\tooltips\addTooltips.js"
GAME_NL_RU = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\nightlights\lang\ru_ru.json"
LOCAL_NL_JSON = os.path.join(ROOT_DIR, "translations", "mods", "nightlights.json")
TASK_NEW_TRANSLATE = os.path.join(ROOT_DIR, "tasks", "Translate_Mods", "translate_nightlights", "new_translate.md")

COLORS = [
    'black', 'blue', 'brown', 'cyan', 'gray', 'green',
    'light_blue', 'light_gray', 'lime', 'magenta', 'orange',
    'pink', 'purple', 'red', 'white', 'yellow'
]

TOOLTIPS = {
    "tooltip.nightlights.frog.desc": "Спокойной ночи, ква-ква~",
    "tooltip.nightlights.mushroom.desc": "Сказочный лес...",
    "tooltip.nightlights.octopus.desc": "Глубокий сон..."
}

# 1. Update addTooltips.js
if os.path.exists(KUBEJS_TOOLTIPS_JS):
    with open(KUBEJS_TOOLTIPS_JS, 'r', encoding='utf-8') as f:
        js_content = f.read()
        
    js_snippet = """
  // Night Lights: Атмосферные тултипы для ночников
  const nlColors = ['black', 'blue', 'brown', 'cyan', 'gray', 'green', 'light_blue', 'light_gray', 'lime', 'magenta', 'orange', 'pink', 'purple', 'red', 'white', 'yellow'];
  nlColors.forEach((color) => {
    tooltip.add(`nightlights:frog_${color}`, Text.translatable("tooltip.nightlights.frog.desc").italic().gray());
    tooltip.add(`nightlights:mushroom_${color}`, Text.translatable("tooltip.nightlights.mushroom.desc").italic().gray());
    tooltip.add(`nightlights:octopus_${color}`, Text.translatable("tooltip.nightlights.octopus.desc").italic().gray());
  });
"""
    if "nightlights:frog_" not in js_content:
        idx = js_content.rfind("});")
        if idx != -1:
            js_content = js_content[:idx] + js_snippet + js_content[idx:]
            with open(KUBEJS_TOOLTIPS_JS, 'w', encoding='utf-8') as f:
                f.write(js_content)
            print("✅ Скрипт addTooltips.js дополнен тултипами Night Lights")
    else:
        print("ℹ️ Тултипы Night Lights уже присутствуют в addTooltips.js")

# 2. Update JSON files
for path in [GAME_NL_RU, LOCAL_NL_JSON]:
    if os.path.exists(path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            for k, v in TOOLTIPS.items():
                data[k] = v
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"✅ Обновлён: {path}")
        except Exception as e:
            print(f"❌ Ошибка записи {path}: {e}")

# 3. Update new_translate.md
if os.path.exists(TASK_NEW_TRANSLATE):
    with open(TASK_NEW_TRANSLATE, 'r', encoding='utf-8') as f:
        md_content = f.read()
    for k, v in TOOLTIPS.items():
        if k not in md_content:
            md_content = md_content.replace(
                '"itemGroup.nightlights.nightlights": "«Ночники и светильники»",',
                f'"itemGroup.nightlights.nightlights": "«Ночники и светильники»",\n  "{k}": "{v}",'
            )
    with open(TASK_NEW_TRANSLATE, 'w', encoding='utf-8') as f:
        f.write(md_content)

print("\n🎉 Тултипы для всех ночников успешно добавлены и синхронизированы!")
