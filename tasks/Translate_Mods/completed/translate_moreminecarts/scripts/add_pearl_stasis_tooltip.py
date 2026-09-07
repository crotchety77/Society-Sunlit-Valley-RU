#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Добавление тултипа для Стазис-камеры жемчуга Края в KubeJS и ru_ru.json
"""

import os
import sys
import json

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
KUBEJS_TOOLTIPS_JS = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\client_scripts\tooltips\addTooltips.js"
GAME_MM_RU = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\moreminecarts\lang\ru_ru.json"
LOCAL_MM_JSON = os.path.join(ROOT_DIR, "translations", "mods", "moreminecarts.json")
TASK_NEW_TRANSLATE = os.path.join(ROOT_DIR, "tasks", "Translate_Mods", "translate_moreminecarts", "new_translate.md")

TOOLTIPS = {
    "tooltip.moreminecarts.pearl_stasis.short": "Устройство удалённой телепортации игрока.",
    "tooltip.moreminecarts.pearl_stasis.details_1": "Положите Жемчуг Края (ПКМ), чтобы привязать камеру к себе.",
    "tooltip.moreminecarts.pearl_stasis.details_2": "При активации редстоуном мгновенно телепортирует владельца к себе из любой точки мира.",
    "tooltip.moreminecarts.pearl_stasis.note": "Используется для кнопок SOS, экстренной эвакуации и станций вызова."
}

# 1. Update addTooltips.js
if os.path.exists(KUBEJS_TOOLTIPS_JS):
    with open(KUBEJS_TOOLTIPS_JS, 'r', encoding='utf-8') as f:
        js_content = f.read()
        
    js_snippet = """
  // More Minecarts: Стазис-камера жемчуга Края
  ["moreminecarts:pearl_stasis_minecart", "moreminecarts:pearl_stasis_chamber"].forEach((id) => {
    tooltip.addAdvanced(id, (item, advanced, text) => {
      text.add(Text.translatable("tooltip.moreminecarts.pearl_stasis.short").gray());
      if (tooltip.shift) {
        text.add(Text.of(""));
        text.add(Text.translatable("tooltip.moreminecarts.pearl_stasis.details_1").aqua());
        text.add(Text.translatable("tooltip.moreminecarts.pearl_stasis.details_2").yellow());
        text.add(Text.of(""));
        text.add(Text.translatable("tooltip.moreminecarts.pearl_stasis.note").darkGray());
      } else {
        text.add(Text.of("§8Удерживайте [§7SHIFT§8] для инструкции§r"));
      }
    });
  });
"""
    if "moreminecarts:pearl_stasis_minecart" not in js_content:
        idx = js_content.rfind("});")
        if idx != -1:
            js_content = js_content[:idx] + js_snippet + js_content[idx:]
            with open(KUBEJS_TOOLTIPS_JS, 'w', encoding='utf-8') as f:
                f.write(js_content)
            print("✅ Скрипт addTooltips.js дополнен тултипом стазис-камеры")

# 2. Update JSON files
for path in [GAME_MM_RU, LOCAL_MM_JSON]:
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
                '"item.moreminecarts.pearl_stasis_minecart": "Вагонетка со стазис-камерой",',
                f'"item.moreminecarts.pearl_stasis_minecart": "Вагонетка со стазис-камерой",\n  "{k}": "{v}",'
            )
    with open(TASK_NEW_TRANSLATE, 'w', encoding='utf-8') as f:
        f.write(md_content)

print("\n🎉 Тултип стазис-камеры успешно добавлен!")
