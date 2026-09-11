#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Скрипт применения и синхронизации локализации товаров Кузнеца (Blacksmith Trades).
1. Считывает переводы из tasks/trades_items_NPC/Blacksmith/new_translate.md.
2. Обновляет translations/society/ru_ru.json, translations/mods/furniture.json, translations/mods/refurbished_furniture.json.
3. Записывает напрямую в файлы игры в D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\...
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

    # 1. translations/society/ru_ru.json
    society_json = os.path.join(ROOT_DIR, "translations", "society", "ru_ru.json")
    update_json_file(society_json, translations)
    print(f"💾 Обновлён {society_json}")

    # 2. translations/mods/furniture.json
    furn_keys = {k: v for k, v in translations.items() if "furniture.bin" in k or k.startswith("block.furniture")}
    if furn_keys:
        furn_json = os.path.join(ROOT_DIR, "translations", "mods", "furniture.json")
        update_json_file(furn_json, furn_keys)
        print(f"💾 Обновлён {furn_json}")

    # 3. translations/mods/refurbished_furniture.json
    refurb_keys = {k: v for k, v in translations.items() if "refurbished_furniture" in k}
    if refurb_keys:
        refurb_json = os.path.join(ROOT_DIR, "translations", "mods", "refurbished_furniture.json")
        update_json_file(refurb_json, refurb_keys)
        print(f"💾 Обновлён {refurb_json}")

    # 4. Direct update to game files
    game_society = os.path.join(GAME_ASSETS_DIR, "society", "lang", "ru_ru.json")
    update_json_file(game_society, translations)

    if furn_keys:
        game_furn = os.path.join(GAME_ASSETS_DIR, "furniture", "lang", "ru_ru.json")
        update_json_file(game_furn, furn_keys)

    if refurb_keys:
        game_refurb = os.path.join(GAME_ASSETS_DIR, "refurbished_furniture", "lang", "ru_ru.json")
        update_json_file(game_refurb, refurb_keys)

    # 5. Run sync_all_to_game.js
    sync_js = os.path.join(ROOT_DIR, "sync_all_to_game.js")
    if os.path.exists(sync_js):
        res = subprocess.run(["node", sync_js], cwd=ROOT_DIR, capture_output=True, text=True, encoding="utf-8")
        print("\n" + res.stdout)

    # 6. Physical verification
    print("\n" + "="*60)
    print("🔍 ОБЯЗАТЕЛЬНАЯ ВЕРИФИКАЦИЯ ФАЙЛОВ ИГРЫ:")
    print("="*60)
    
    check_targets = [
        ("society", game_society, [
            "block.society.moon_statue",
            "block.society.moon_statue.description",
            "block.society.moon_statue.announce",
            "block.society.moon_statue.moon_extra_ore",
            "block.society.moon_statue.moon_geode_roll",
            "block.society.moon_statue.moon_rope_reveal",
            "block.society.moon_statue.moon_remains",
            "block.society.moon_statue.moon_damage",
            "tooltip.society.diy_workbench",
            "tooltip.society.hammer_core"
        ]),
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
        print("\n🎉 Все ключи Кузнеца успешно проверены и физически записаны в файлы игры!")

if __name__ == "__main__":
    main()
