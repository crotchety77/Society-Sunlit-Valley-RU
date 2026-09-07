#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

ROOT_DIR = r"c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода"
TOOLTIPS_JS = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\client_scripts\tooltips\addTooltips.js"
LOCAL_SOC_RU = os.path.join(ROOT_DIR, "translations", "society", "ru_ru.json")
GAME_SOC_RU = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\society\lang\ru_ru.json"
NEW_TRANSLATE_MD = os.path.join(ROOT_DIR, "tasks", "Translate_Mods", "translate_splendid_slimes", "new_translate.md")

# 1. Update Lang Files
candy_str = "Накормите слайма, чтобы повысить шкалу настроения."
for path in [LOCAL_SOC_RU, GAME_SOC_RU]:
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            d = json.load(f)
        d["tooltip.society.slime_candy"] = candy_str
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(d, f, ensure_ascii=False, indent=2)
        print(f"✅ Обновлён {path}")

# 2. Update addTooltips.js
if os.path.exists(TOOLTIPS_JS):
    with open(TOOLTIPS_JS, 'r', encoding='utf-8') as f:
        js = f.read()

    old_snippet = """  tooltip.add(
    "splendid_slimes:slime_candy",
    Text.translatable("tooltip.society.slime_candy").gray()
  );"""

    new_snippet = """  tooltip.addAdvanced("splendid_slimes:slime_candy", (item, advanced, text) => {
    if (tooltip.shift) {
      text.add(Text.of("§6▪ Сладкое лакомство:§7 Подходит для каждого слайма."));
      text.add(Text.of("§7Мгновенно поднимает настроение на целый ранг, а довольного слайма"));
      text.add(Text.of("§7вводит в §aПолный восторг (У некоторых Слаймов активируются баффы)§7!"));
      text.add(Text.of(""));
      text.add(Text.of("§eСовет:§8 используйте для быстрого усмирения яростных слаймов и предотвращения побегов из загона."));
      text.add(Text.of(""));
      text.add(Text.of("§8━━━━━━━━━━━ §7Шкала настроения §8━━━━━━━━━━━"));
      text.add(Text.of("§cЯростный§8 (< -50) → §eГрустный§8 (< 0) → §fСпокойный§8 (0) → §aДовольный§8 (> 0) → §b✦ Восторг (100%) §8✦"));
    } else {
      text.add(Text.of("§7Накормите слайма, чтобы повысить шкалу настроения."));
      text.add(Text.of("§8Удерживайте [§7Shift§8] для подробностей§r"));
    }
  });"""

    if old_snippet in js:
        js = js.replace(old_snippet, new_snippet)
        with open(TOOLTIPS_JS, 'w', encoding='utf-8') as f:
            f.write(js)
        print("✅ addTooltips.js успешно обновлён интерактивным тултипом [SHIFT] для Слаймовой конфеты")
    else:
        print("⚠️ Старый сниппет не найден, проверяем наличие")

# 3. Update new_translate.md
if os.path.exists(NEW_TRANSLATE_MD):
    with open(NEW_TRANSLATE_MD, 'r', encoding='utf-8') as f:
        md = f.read()

    tooltip_md_block = """* **Слаймовая конфета** (`splendid_slimes:slime_candy`):
  > **По умолчанию:**
  > `§7Накормите слайма, чтобы повысить шкалу настроения.`
  > `§8Удерживайте [§7Shift§8] для подробностей§r`
  >
  > **При зажатом [SHIFT]:**
  > `§6▪ Сладкое лакомство:§7 Подходит для каждого слайма.`
  > `§7Мгновенно поднимает настроение на целый ранг, а довольного слайма`
  > `§7вводит в §aПолный восторг (У некоторых Слаймов активируются баффы)§7!`
  > 
  > `§eСовет:§8 используйте для быстрого усмирения яростных слаймов и предотвращения побегов из загона.`
  > 
  > `§8━━━━━━━━━━━ §7Шкала настроения §8━━━━━━━━━━━`
  > `§cЯростный§8 (< -50) → §eГрустный§8 (< 0) → §fСпокойный§8 (0) → §aДовольный§8 (> 0) → §b✦ Восторг (100%) §8✦`

"""

    if "* **Слаймовая конфета** (`splendid_slimes:slime_candy`):" not in md:
        target = "* **Анализатор слаймов** (`splendid_slimes:slime_inspector`):"
        md = md.replace(target, tooltip_md_block + target)
        with open(NEW_TRANSLATE_MD, 'w', encoding='utf-8') as f:
            f.write(md)
        print("✅ new_translate.md обновлён блоком тултипа Слаймовой конфеты")

