#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

ROOT_DIR = r"c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода"
TOOLTIPS_JS = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\client_scripts\tooltips\addTooltips.js"
NEW_TRANSLATE_MD = os.path.join(ROOT_DIR, "tasks", "Translate_Mods", "translate_splendid_slimes", "new_translate.md")

# 1. Update addTooltips.js
if os.path.exists(TOOLTIPS_JS):
    with open(TOOLTIPS_JS, 'r', encoding='utf-8') as f:
        js = f.read()

    inspector_tooltip = """  // Splendid Slimes: Анализатор слаймов
  tooltip.add("splendid_slimes:slime_inspector", [
    Text.of("§7Незаменимый инструмент слаймовода."),
    Text.of("§6ПКМ по слайму§7 выводит подробный отчёт в чат:"),
    Text.of("§8▪ Породу (или состав гибрида Ларго) и рацион"),
    Text.of("§8▪ Любимое лакомство (удваивающее плорты)"),
    Text.of("§8▪ Базовую стоимость плортов в §e● монетах"),
    Text.of("§8▪ Сытость и уровень настроения слайма")
  ]);
"""

    if 'splendid_slimes:slime_inspector' not in js:
        idx = js.rfind('});')
        if idx != -1:
            js = js[:idx] + inspector_tooltip + js[idx:]
            with open(TOOLTIPS_JS, 'w', encoding='utf-8') as f:
                f.write(js)
            print("✅ Тултип Анализатора слаймов добавлен в addTooltips.js")
    else:
        print("ℹ️ Тултип Анализатора слаймов уже есть в addTooltips.js")

# 2. Update new_translate.md
if os.path.exists(NEW_TRANSLATE_MD):
    with open(NEW_TRANSLATE_MD, 'r', encoding='utf-8') as f:
        md = f.read()
    
    target = "* **Капсула для реактивного прыжка** (`splendid_slimes:rocket_pod`):"
    if "* **Анализатор слаймов** (`splendid_slimes:slime_inspector`):" not in md:
        replacement = """* **Анализатор слаймов** (`splendid_slimes:slime_inspector`):
  > `§7Незаменимый инструмент слаймовода.`
  > `§6ПКМ по слайму§7 выводит подробный отчёт в чат:`
  > `§8▪ Породу (или состав гибрида Ларго) и рацион`
  > `§8▪ Любимое лакомство (удваивающее плорты)`
  > `§8▪ Базовую стоимость плортов в §e● монетах`
  > `§8▪ Сытость и уровень настроения слайма`

* **Капсула для реактивного прыжка** (`splendid_slimes:rocket_pod`):"""
        md = md.replace(target, replacement)
        with open(NEW_TRANSLATE_MD, 'w', encoding='utf-8') as f:
            f.write(md)
        print("✅ new_translate.md обновлён новым тултипом")

