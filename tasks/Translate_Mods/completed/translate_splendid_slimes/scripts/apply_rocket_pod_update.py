#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

ROOT_DIR = r"c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода"
GAME_DIR = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs"
TOOLTIPS_JS = os.path.join(GAME_DIR, "client_scripts", "tooltips", "addTooltips.js")
GAME_SPLENDID_RU = os.path.join(GAME_DIR, "assets", "splendid_slimes", "lang", "ru_ru.json")
LOCAL_SPLENDID_JSON = os.path.join(ROOT_DIR, "translations", "mods", "splendid_slimes.json")
NEW_TRANSLATE_MD = os.path.join(ROOT_DIR, "tasks", "Translate_Mods", "translate_splendid_slimes", "new_translate.md")
GLOSSARY_MD = os.path.join(ROOT_DIR, "glossary.md")

# 1. Update Lang Files
with open(LOCAL_SPLENDID_JSON, 'r', encoding='utf-8') as f:
    d = json.load(f)

d["item.splendid_slimes.rocket_pod"] = "Капсула для реактивного прыжка"
d["block.splendid_slimes.rocket_pod"] = "Капсула для реактивного прыжка"

with open(LOCAL_SPLENDID_JSON, 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
print("✅ Обновлён translations/mods/splendid_slimes.json")

with open(GAME_SPLENDID_RU, 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
print("✅ Обновлён файл игры:", GAME_SPLENDID_RU)

# 2. Update new_translate.md
if os.path.exists(NEW_TRANSLATE_MD):
    with open(NEW_TRANSLATE_MD, 'r', encoding='utf-8') as f:
        md = f.read()
    md = md.replace('"item.splendid_slimes.rocket_pod": "Ракетная грузовая капсула"', '"item.splendid_slimes.rocket_pod": "Капсула для реактивного прыжка"')
    md = md.replace('"block.splendid_slimes.rocket_pod": "Ракетная грузовая капсула"', '"block.splendid_slimes.rocket_pod": "Капсула для реактивного прыжка"')
    with open(NEW_TRANSLATE_MD, 'w', encoding='utf-8') as f:
        f.write(md)
    print("✅ Обновлён new_translate.md")

# 3. Update glossary.md
if os.path.exists(GLOSSARY_MD):
    with open(GLOSSARY_MD, 'r', encoding='utf-8') as f:
        gloss = f.read()
    gloss = gloss.replace("| **Rocket Pod** | **Ракетная грузовая капсула** | `block.splendid_slimes.rocket_pod` |", "| **Rocket Pod** | **Капсула для реактивного прыжка** | `item.splendid_slimes.rocket_pod` |")
    with open(GLOSSARY_MD, 'w', encoding='utf-8') as f:
        f.write(gloss)
    print("✅ Обновлён glossary.md")

# 4. Add Tooltip to addTooltips.js
if os.path.exists(TOOLTIPS_JS):
    with open(TOOLTIPS_JS, 'r', encoding='utf-8') as f:
        js = f.read()

    tooltip_snippet = """  // Splendid Slimes: Капсула для реактивного прыжка
  tooltip.add("splendid_slimes:rocket_pod", [
    Text.of("§7Специальный заряд для §6Слаймопушки§7."),
    Text.of("§7Выстрел под ноги запускает вас на §a10–15 блоков§7"),
    Text.of("§7вверх, позволяя перелетать стены загонов."),
    Text.of("§bУдарная волна безопасна для построек.§r")
  ]);
"""

    if 'splendid_slimes:rocket_pod' not in js:
        idx = js.rfind('});')
        if idx != -1:
            js = js[:idx] + tooltip_snippet + js[idx:]
            with open(TOOLTIPS_JS, 'w', encoding='utf-8') as f:
                f.write(js)
            print("✅ Тултип добавлен в addTooltips.js")
    else:
        print("ℹ️ Тултип уже присутствует в addTooltips.js")

