#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
Скрипт применения и синхронизации подсказок для society:seed_maker.
1. Считывает переводы из new_translate.md.
2. Обновляет translations/society/ru_ru.json.
3. Добавляет tooltip.addAdvanced("society:seed_maker", ...) в addTooltips.js (в игре и в проекте).
4. Записывает в D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\society\lang\ru_ru.json.
5. Запускает sync_all_to_game.js.
6. Выполняет физическую верификацию файлов игры.
"""

import os
import sys
import json
import re
import subprocess

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
TASK_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LOCAL_SOCIETY_JSON = os.path.join(ROOT_DIR, "translations", "society", "ru_ru.json")
GAME_SOCIETY_PATH = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\society\lang\ru_ru.json"
GAME_TOOLTIPS_JS = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\client_scripts\tooltips\addTooltips.js"

def parse_translations():
    target_file = os.path.join(TASK_DIR, "new_translate.md")
    if not os.path.exists(target_file):
        print(f"❌ Не найден файл с переводами: {target_file}")
        return {}

    with open(target_file, 'r', encoding='utf-8') as f:
        content = f.read()

    json_blocks = re.findall(r'```json\s*(\{.*?\})\s*```', content, flags=re.DOTALL)
    soc_trans = {}
    for block in json_blocks:
        try:
            data = json.loads(block)
            for k, v in data.items():
                if isinstance(v, str):
                    soc_trans[k] = v
        except Exception as e:
            print(f"[!] Ошибка парсинга JSON: {e}")
            
    return soc_trans

def update_add_tooltips_js():
    if not os.path.exists(GAME_TOOLTIPS_JS):
        print(f"❌ Не найден addTooltips.js в игре: {GAME_TOOLTIPS_JS}")
        return

    with open(GAME_TOOLTIPS_JS, 'r', encoding='utf-8') as f:
        content = f.read()

    snippet = """  tooltip.addAdvanced("society:seed_maker", (item, advanced, text) => {
    if (tooltip.shift) {
      text.add(Text.translatable("tooltip.society.seed_maker.shift_1").gray());
      text.add(Text.translatable("tooltip.society.seed_maker.shift_2").gray());
      text.add(Text.translatable("tooltip.society.seed_maker.shift_3").gray());
    } else {
      text.add([
        Text.translatable("tooltip.society.hold_key", Text.translatable("key.keyboard.shift").gray()).darkGray(),
      ]);
    }
  });"""

    if 'tooltip.addAdvanced("society:seed_maker"' not in content:
        # Insert after cheese_press advanced tooltip
        target_anchor = 'tooltip.addAdvanced("society:cheese_press"'
        if target_anchor in content:
            content = content.replace(target_anchor, snippet + "\n  " + target_anchor)
            with open(GAME_TOOLTIPS_JS, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Добавлен addAdvanced для society:seed_maker в {GAME_TOOLTIPS_JS}")
        else:
            print("⚠️ Не найден target_anchor для вставки в addTooltips.js")
    else:
        print("ℹ️ addAdvanced для society:seed_maker уже присутствует в addTooltips.js")

def apply_and_sync():
    soc_trans = parse_translations()
    print(f"📦 Считано строк society: {len(soc_trans)}")

    # 1. Update translations/society/ru_ru.json
    if soc_trans:
        with open(LOCAL_SOCIETY_JSON, 'r', encoding='utf-8') as f:
            local_soc = json.load(f)
        local_soc.update(soc_trans)
        with open(LOCAL_SOCIETY_JSON, 'w', encoding='utf-8') as f:
            json.dump(local_soc, f, ensure_ascii=False, indent=2)
        print(f"💾 Обновлён translations/society/ru_ru.json (+{len(soc_trans)} ключей)")

    # 2. Update JS in game
    update_add_tooltips_js()

    # 3. Direct write to game assets
    if os.path.exists(GAME_SOCIETY_PATH):
        with open(GAME_SOCIETY_PATH, 'r', encoding='utf-8') as f:
            game_soc = json.load(f)
        game_soc.update(soc_trans)
        with open(GAME_SOCIETY_PATH, 'w', encoding='utf-8') as f:
            json.dump(game_soc, f, ensure_ascii=False, indent=2)
        print(f"🎮 Записано напрямую в файл игры: {GAME_SOCIETY_PATH}")

    # 4. Sync
    sync_js = os.path.join(ROOT_DIR, "sync_all_to_game.js")
    if os.path.exists(sync_js):
        res = subprocess.run(["node", sync_js], cwd=ROOT_DIR, capture_output=True, text=True, encoding='utf-8')
        print(f"🔄 Результат sync_all_to_game.js:\n{res.stdout}")

    # 5. Direct verification
    print("\n🔍 ОБЯЗАТЕЛЬНАЯ ВЕРИФИКАЦИЯ ФАЙЛОВ ИГРЫ:")
    if os.path.exists(GAME_SOCIETY_PATH):
        with open(GAME_SOCIETY_PATH, 'r', encoding='utf-8') as f:
            verified_soc = json.load(f)
        print(f"✅ society: всего ключей {len(verified_soc)}")
        for k in soc_trans.keys():
            print(f"   ▪ [{k}]: {verified_soc.get(k)}")

if __name__ == "__main__":
    apply_and_sync()
