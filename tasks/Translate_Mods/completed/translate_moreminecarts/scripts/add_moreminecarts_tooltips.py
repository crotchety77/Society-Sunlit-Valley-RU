#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Добавление тултипов для More Minecarts (Вагонетка с прогрузчиком чанков, Чанкродит) в KubeJS и ru_ru.json
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
    # Чанкродит
    "item.moreminecarts.chunkrodite.desc": "Топливо для Вагонетки с прогрузчиком чанков (15 минут)",
    "block.moreminecarts.chunkrodite_block.desc": "Топливо для Вагонетки с прогрузчиком чанков (2 часа 15 минут)",
    
    # Вагонетка с прогрузчиком чанков
    "tooltip.moreminecarts.chunk_loader.short": "Мобильный прогрузчик чанков для транспортных путей.",
    "tooltip.moreminecarts.chunk_loader.details_1": "Непрерывно удерживает активным чанк, в котором находится в данный момент, прогружая путь перед собой.",
    "tooltip.moreminecarts.chunk_loader.fuel_header": "Топливо и время работы:",
    "tooltip.moreminecarts.chunk_loader.fuel_1": "▪ Чанкродит: §e15 мин§7 | Блок чанкродита: §e2 ч 15 мин§7",
    "tooltip.moreminecarts.chunk_loader.fuel_2": "▪ Уголь: §e5 мин§7 | Редстоун / Лазурит: §e45 мин§7",
    "tooltip.moreminecarts.chunk_loader.fuel_3": "▪ Осколок аметиста: §e30 сек§7 | Алмаз: §e9 ч§7 | Незерит: §e48 ч§7",
    "tooltip.moreminecarts.chunk_loader.note": "Используется для автономных грузовых поездов через весь мир."
}

# 1. Update addTooltips.js
if os.path.exists(KUBEJS_TOOLTIPS_JS):
    with open(KUBEJS_TOOLTIPS_JS, 'r', encoding='utf-8') as f:
        js_content = f.read()
        
    js_snippet = """
  // More Minecarts: Чанкродит
  tooltip.add("moreminecarts:chunkrodite", Text.translatable("item.moreminecarts.chunkrodite.desc").gray());
  tooltip.add("moreminecarts:chunkrodite_block", Text.translatable("block.moreminecarts.chunkrodite_block.desc").gray());

  // More Minecarts: Вагонетка с прогрузчиком чанков и Блок прогрузчика
  ["moreminecarts:minecart_with_chunk_loader", "moreminecarts:chunk_loader"].forEach((id) => {
    tooltip.addAdvanced(id, (item, advanced, text) => {
      text.add(Text.translatable("tooltip.moreminecarts.chunk_loader.short").gray());
      if (tooltip.shift) {
        text.add(Text.of(""));
        text.add(Text.translatable("tooltip.moreminecarts.chunk_loader.details_1").aqua());
        text.add(Text.of(""));
        text.add(Text.translatable("tooltip.moreminecarts.chunk_loader.fuel_header").gold());
        text.add(Text.translatable("tooltip.moreminecarts.chunk_loader.fuel_1").gray());
        text.add(Text.translatable("tooltip.moreminecarts.chunk_loader.fuel_2").gray());
        text.add(Text.translatable("tooltip.moreminecarts.chunk_loader.fuel_3").gray());
        text.add(Text.of(""));
        text.add(Text.translatable("tooltip.moreminecarts.chunk_loader.note").darkGray());
      } else {
        text.add(Text.of("§8Удерживайте [§7SHIFT§8] для списка топлива и деталей§r"));
      }
    });
  });
"""
    if "moreminecarts:minecart_with_chunk_loader" not in js_content:
        idx = js_content.rfind("});")
        if idx != -1:
            js_content = js_content[:idx] + js_snippet + js_content[idx:]
            with open(KUBEJS_TOOLTIPS_JS, 'w', encoding='utf-8') as f:
                f.write(js_content)
            print("✅ Скрипт addTooltips.js дополнен тултипами More Minecarts")
    else:
        print("ℹ️ Тултипы More Minecarts уже присутствуют в addTooltips.js")

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
                '"item.moreminecarts.chunkrodite": "Чанкродит",',
                f'"item.moreminecarts.chunkrodite": "Чанкродит",\n  "{k}": "{v}",'
            )
    with open(TASK_NEW_TRANSLATE, 'w', encoding='utf-8') as f:
        f.write(md_content)
    print("✅ new_translate.md обновлен новыми ключами")

print("\n🎉 Все тултипы для More Minecarts успешно применены!")
