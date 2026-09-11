#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Скрипт применения и синхронизации локализации товаров Карлоса (Carlos Trades).
1. Считывает переводы из tasks/trades_items_NPC/Carlos/new_translate.md.
2. Обновляет translations/society/ru_ru.json, translations/mods/snowyspirit.json,
   translations/mods/supplementaries.json, translations/mods/gag.json.
3. Записывает напрямую в файлы игры в D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\...
4. Запускает sync_all_to_game.js.
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

    # 1. translations/society/ru_ru.json
    society_json = os.path.join(ROOT_DIR, "translations", "society", "ru_ru.json")
    update_json_file(society_json, translations)
    print(f"💾 Обновлён {society_json}")

    # 2. translations/mods/snowyspirit.json
    snowyspirit_keys = {k: v for k, v in translations.items() if "snowyspirit" in k}
    if snowyspirit_keys:
        snowyspirit_json = os.path.join(ROOT_DIR, "translations", "mods", "snowyspirit.json")
        update_json_file(snowyspirit_json, snowyspirit_keys)
        print(f"💾 Обновлён {snowyspirit_json}")

    # 3. translations/mods/supplementaries.json
    supp_keys = {k: v for k, v in translations.items() if "trial_chamber" in k or "supplementaries" in k}
    if supp_keys:
        supp_json = os.path.join(ROOT_DIR, "translations", "mods", "supplementaries.json")
        update_json_file(supp_json, supp_keys)
        print(f"💾 Обновлён {supp_json}")

    # 4. translations/mods/gag.json
    gag_keys = {k: v for k, v in translations.items() if "gag" in k}
    if gag_keys:
        gag_json = os.path.join(ROOT_DIR, "translations", "mods", "gag.json")
        update_json_file(gag_json, gag_keys)
        print(f"💾 Обновлён {gag_json}")

    # 5. Direct update to game files
    game_society = os.path.join(GAME_ASSETS_DIR, "society", "lang", "ru_ru.json")
    update_json_file(game_society, translations)

    if snowyspirit_keys:
        game_snowy = os.path.join(GAME_ASSETS_DIR, "snowyspirit", "lang", "ru_ru.json")
        update_json_file(game_snowy, snowyspirit_keys)

    if supp_keys:
        game_supp = os.path.join(GAME_ASSETS_DIR, "supplementaries", "lang", "ru_ru.json")
        update_json_file(game_supp, supp_keys)

    if gag_keys:
        game_gag = os.path.join(GAME_ASSETS_DIR, "gag", "lang", "ru_ru.json")
        update_json_file(game_gag, gag_keys)

    # 6. Run sync_all_to_game.js
    sync_js = os.path.join(ROOT_DIR, "sync_all_to_game.js")
    if os.path.exists(sync_js):
        res = subprocess.run(["node", sync_js], cwd=ROOT_DIR, capture_output=True, text=True, encoding="utf-8")
        print("\n" + res.stdout)

    # 7. Verification from physical game files
    print("\n" + "="*60)
    print("🔍 ОБЯЗАТЕЛЬНАЯ ВЕРИФИКАЦИЯ ФАЙЛОВ ИГРЫ:")
    print("="*60)
    
    check_targets = [
        ("society", game_society, ["item.society.prize_ticket.description", "tooltip.society.escape_rope_hold"]),
        ("snowyspirit", os.path.join(GAME_ASSETS_DIR, "snowyspirit", "lang", "ru_ru.json"), ["block.snowyspirit.ginger_crate"]),
        ("supplementaries", os.path.join(GAME_ASSETS_DIR, "supplementaries", "lang", "ru_ru.json"), ["filled_map.trial_chamber"]),
        ("gag", os.path.join(GAME_ASSETS_DIR, "gag", "lang", "ru_ru.json"), ["item.gag.mining_dynamite", "item.gag.escape_rope"])
    ]

    all_ok = True
    for mod_name, file_path, keys in check_targets:
        if not os.path.exists(file_path):
            print(f"❌ Файл игры не найден: {file_path}")
            all_ok = False
            continue
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        print(f"\n📁 Мод: [{mod_name}] ({file_path}):")
        for k in keys:
            val = data.get(k)
            if val is not None:
                print(f"  ✅ [{k}] = \"{val}\"")
            else:
                print(f"  ❌ Ключ не найден: [{k}]")
                all_ok = False

    if all_ok:
        print("\n🎉 Все 5 предметов успешно проверены и физически записаны в файлы игры!")

if __name__ == "__main__":
    main()
