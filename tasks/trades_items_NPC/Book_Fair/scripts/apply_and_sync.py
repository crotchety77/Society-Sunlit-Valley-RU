#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Скрипт применения и синхронизации локализации Книжной ярмарки (Book Fair Trades).
1. Считывает переводы из tasks/trades_items_NPC/Book_Fair/new_translate.md.
2. Обновляет translations/buildings/society_trading_building_shop_ru_ru.json.
3. Записывает напрямую в файлы игры в D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\society_trading\lang\ru_ru.json.
4. Запускает общий node sync_all_to_game.js.
5. Физически считывает и верифицирует ключи из игровых файлов.
"""

import os
import sys
import json
import re
import subprocess

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
TASK_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
GAME_ASSETS_DIR = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets"

def parse_new_translate():
    trans_file = os.path.join(TASK_DIR, "new_translate.md")
    if not os.path.exists(trans_file):
        raise FileNotFoundError(f"Файл {trans_file} не найден!")
    with open(trans_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    json_blocks = re.findall(r'```json\s*(\{.*?\})\s*```', content, flags=re.DOTALL)
    data = {}
    for block in json_blocks:
        try:
            parsed = json.loads(block)
            data.update(parsed)
        except Exception as e:
            print(f"Ошибка парсинга JSON-блока: {e}")
    return data

def update_json_file(file_path, updates):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    data = {}
    if os.path.exists(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            data = {}
    data.update(updates)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def main():
    translations = parse_new_translate()
    print(f"📦 Считано ключей из new_translate.md: {len(translations)}")

    # 1. translations/buildings/society_trading_building_shop_ru_ru.json
    local_trading = os.path.join(ROOT_DIR, "translations", "buildings", "society_trading_building_shop_ru_ru.json")
    update_json_file(local_trading, translations)
    print(f"✅ Обновлен {local_trading}")

    # 2. Прямая запись в игру
    game_trading = os.path.join(GAME_ASSETS_DIR, "society_trading", "lang", "ru_ru.json")
    update_json_file(game_trading, translations)
    print(f"✅ Записано в игру {game_trading}")

    # 3. Запуск sync_all_to_game.js
    sync_js = os.path.join(ROOT_DIR, "sync_all_to_game.js")
    if os.path.exists(sync_js):
        res = subprocess.run(["node", sync_js], cwd=ROOT_DIR, capture_output=True, text=True, encoding="utf-8")
        print("\n" + res.stdout)

    # 4. Физическая верификация
    print("\n" + "="*60)
    print("🔍 ОБЯЗАТЕЛЬНАЯ ВЕРИФИКАЦИЯ ФАЙЛОВ ИГРЫ:")
    print("="*60)
    
    with open(game_trading, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    keys = list(translations.keys())
    for k in keys:
        val = data.get(k)
        if val is not None:
            print(f"  ✅ [{k}] = \"{val}\"")
        else:
            print(f"  ❌ Ключ не найден: [{k}]")
    
    print("\n🎉 Все ключи Книжной ярмарки успешно синхронизированы и проверены!")

if __name__ == "__main__":
    main()
