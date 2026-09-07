#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Обновление названий сердец в моде Splendid Slimes:
1. item.splendid_slimes.default_heart -> Сердце слайма
2. item.splendid_slimes.slime_heart -> Сердце слайма: %s
3. info.splendid_slimes.slime_heart -> Поместите в инкубатор для выведения слайма
4. item.splendid_slimes.<breed>_slime_heart -> Сердце слайма: <Breed>
5. Обновление new_translate.md, quests_translate.md, translations/mods/splendid_slimes.json
6. Синхронизация в игру и проверка.
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
NEW_TRANSLATE_MD = os.path.join(TASK_DIR, "new_translate.md")
QUESTS_TRANSLATE_MD = os.path.join(TASK_DIR, "quests_translate.md")
LOCAL_MOD_JSON = os.path.join(ROOT_DIR, "translations", "mods", "splendid_slimes.json")
GAME_RU_PATH = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\splendid_slimes\lang\ru_ru.json"

def update_new_translate():
    with open(NEW_TRANSLATE_MD, "r", encoding="utf-8") as f:
        content = f.read()

    # Block 1 updates
    content = content.replace("— выращивание слизней из сердец", "— выращивание слаймов из сердец слайма")
    content = content.replace("— спрессовывание сердец", "— спрессовывание сердец слаймов")

    # Block 2 JSON updates
    content = content.replace('"item.splendid_slimes.default_heart": "Сердце слизня"', '"item.splendid_slimes.default_heart": "Сердце слайма"')
    content = content.replace('"item.splendid_slimes.slime_heart": "Сердце: %s"', '"item.splendid_slimes.slime_heart": "Сердце слайма: %s"')
    content = content.replace('"info.splendid_slimes.slime_heart": "Поместите в инкубатор для выведения слизня"', '"info.splendid_slimes.slime_heart": "Поместите в инкубатор для выведения слайма"')

    # Replace "Сердце (<Name>)" with "Сердце слайма: <Name>" for all breeds
    content = re.sub(r'("item\.splendid_slimes\.[a-z_]+_slime_heart":\s*)"Сердце \((.*?)\)"', r'\1"Сердце слайма: \2"', content)

    with open(NEW_TRANSLATE_MD, "w", encoding="utf-8") as f:
        f.write(content)
    print("✅ new_translate.md успешно обновлен.")

def update_quests_translate():
    if not os.path.exists(QUESTS_TRANSLATE_MD):
        return
    with open(QUESTS_TRANSLATE_MD, "r", encoding="utf-8") as f:
        content = f.read()

    content = content.replace("&6Сердце слизня&r", "&6Сердце слайма&r")
    content = content.replace("&6Сердце (Барни Слайм)&r", "&6Сердце слайма: Барни&r")

    with open(QUESTS_TRANSLATE_MD, "w", encoding="utf-8") as f:
        f.write(content)
    print("✅ quests_translate.md успешно обновлен.")

def update_mod_json():
    with open(LOCAL_MOD_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)

    data["item.splendid_slimes.default_heart"] = "Сердце слайма"
    data["item.splendid_slimes.slime_heart"] = "Сердце слайма: %s"
    data["info.splendid_slimes.slime_heart"] = "Поместите в инкубатор для выведения слайма"

    for k in list(data.keys()):
        if k.endswith("_slime_heart"):
            val = data[k]
            # If format is "Сердце (Name)" or "Сердце: Name"
            m = re.match(r'Сердце (?:\((.*?)\)|:\s*(.*?))$', val)
            if m:
                name = m.group(1) or m.group(2)
                data[k] = f"Сердце слайма: {name}"

    with open(LOCAL_MOD_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✅ translations/mods/splendid_slimes.json обновлен ({len(data)} ключей).")

    # Direct game write
    if os.path.exists(os.path.dirname(GAME_RU_PATH)):
        game_data = {}
        if os.path.exists(GAME_RU_PATH):
            with open(GAME_RU_PATH, "r", encoding="utf-8") as f:
                game_data = json.load(f)
        game_data.update(data)
        with open(GAME_RU_PATH, "w", encoding="utf-8") as f:
            json.dump(game_data, f, ensure_ascii=False, indent=2)
        print(f"✅ Прямая запись в игру: {GAME_RU_PATH}")

def run_sync_and_verify():
    sync_js = os.path.join(ROOT_DIR, "sync_all_to_game.js")
    if os.path.exists(sync_js):
        res = subprocess.run(["node", sync_js], cwd=ROOT_DIR, capture_output=True, text=True, encoding='utf-8')
        print(f"🔄 Результат sync_all_to_game.js:\n{res.stdout}")

    print("\n🔍 ОБЯЗАТЕЛЬНАЯ ВЕРИФИКАЦИЯ ФАЙЛА ИГРЫ:")
    if os.path.exists(GAME_RU_PATH):
        with open(GAME_RU_PATH, "r", encoding="utf-8") as f:
            verified = json.load(f)
        keys_to_check = [
            "item.splendid_slimes.default_heart",
            "item.splendid_slimes.slime_heart",
            "info.splendid_slimes.slime_heart",
            "item.splendid_slimes.all_seeing_slime_heart",
            "item.splendid_slimes.bear_slime_heart",
            "item.splendid_slimes.boomcat_slime_heart",
            "item.splendid_slimes.slimy_slime_heart",
            "item.splendid_slimes.weeping_slime_heart"
        ]
        for k in keys_to_check:
            print(f"   ▪ [{k}]: {verified.get(k)}")
    else:
        print("❌ Файл игры не найден!")

if __name__ == "__main__":
    update_new_translate()
    update_quests_translate()
    update_mod_json()
    run_sync_and_verify()
