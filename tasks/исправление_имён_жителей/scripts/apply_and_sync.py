#!/usr/bin/env python3
"""
Скрипт применения и верификации правок имён жителей и странствующего торговца.
"""

import json
import os
import subprocess
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[3]
GAME_DIR = Path(r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets")

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")

def apply_translations():
    print(">>> 1. Обновление translations/society/ru_ru.json...")
    society_path = ROOT_DIR / "translations" / "society" / "ru_ru.json"
    society_data = load_json(society_path)
    society_data["entity.minecraft.villager.weaponsmith"] = "Библиотекарь"
    society_data["entity.minecraft.wandering_trader"] = "Карлос"
    save_json(society_path, society_data)

    print(">>> 2. Обновление translations/mods/minecraft.json...")
    mc_path = ROOT_DIR / "translations" / "mods" / "minecraft.json"
    mc_data = load_json(mc_path) if mc_path.exists() else {}
    mc_data["entity.minecraft.wandering_trader"] = "Карлос"
    save_json(mc_path, mc_data)

    print(">>> 3. Обновление translations/ftbquests/ru_ru.json...")
    ftb_path = ROOT_DIR / "translations" / "ftbquests" / "ru_ru.json"
    ftb_data = load_json(ftb_path)
    ftb_data["ftbquests.chapter.villagers.quest49477F09DF6EBA50.title"] = "Библиотекарь"
    ftb_data["ftbquests.chapter.villagers.quest49477F09DF6EBA50.description1"] = (
        "&6Библиотекарь&r продаёт оборудование для управления вашим хранилищем, "
        "включая систему &6Refined Storage&r для цифрового хранения ваших предметов."
    )
    ftb_data["ftbquests.chapter.ii__building_up_the_farm.quest61501449BF31B773.description2"] = (
        "К счастью, житель-&6библиотекарь&r продаёт различные предметы, которые помогут справиться с этим хаосом."
    )
    save_json(ftb_path, ftb_data)

    # Обновление реестра квестов если существует
    registry_json_path = ROOT_DIR / "tasks" / "FTB_QUESTS_4_1_4" / "registry_quests.json"
    if registry_json_path.exists():
        reg_data = load_json(registry_json_path)
        for chapter, quests in reg_data.get("chapters", {}).items():
            for q in quests:
                if q.get("id") == "49477F09DF6EBA50":
                    q["title_ru"] = "Библиотекарь"
        save_json(registry_json_path, reg_data)

    registry_md_path = ROOT_DIR / "tasks" / "FTB_QUESTS_4_1_4" / "registry_quests.md"
    if registry_md_path.exists():
        content = registry_md_path.read_text(encoding="utf-8")
        content = content.replace("| `49477F09DF6EBA50` | `villagers` | Librarian | Кладовщик |",
                                  "| `49477F09DF6EBA50` | `villagers` | Librarian | Библиотекарь |")
        registry_md_path.write_text(content, encoding="utf-8")

import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

def sync_to_game():
    print(">>> 4. Запуск node sync_all_to_game.js...")
    result = subprocess.run(
        ["node", "sync_all_to_game.js"],
        cwd=str(ROOT_DIR),
        capture_output=True,
        text=True,
        encoding="utf-8"
    )
    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)

def verify_game_files():
    print(">>> 5. ПРЯМАЯ ВЕРИФИКАЦИЯ ФАЙЛОВ ИГРЫ:")
    
    dialog_game = GAME_DIR / "dialog" / "lang" / "ru_ru.json"
    if dialog_game.exists():
        data = load_json(dialog_game)
        print(f"  [dialog/lang/ru_ru.json]")
        print(f"    dialog.npc.trader.name = {data.get('dialog.npc.trader.name')}")
        print(f"    dialog.npc.trader.chatter.description = {data.get('dialog.npc.trader.chatter.description')}")
    else:
        print(f"  [!] Файл не найден: {dialog_game}")

    society_game = GAME_DIR / "society" / "lang" / "ru_ru.json"
    if society_game.exists():
        data = load_json(society_game)
        print(f"  [society/lang/ru_ru.json]")
        print(f"    entity.minecraft.villager.weaponsmith = {data.get('entity.minecraft.villager.weaponsmith')}")
        print(f"    entity.minecraft.wandering_trader = {data.get('entity.minecraft.wandering_trader')}")
    else:
        print(f"  [!] Файл не найден: {society_game}")

    ftb_game = GAME_DIR / "ftbquestlocalizer" / "lang" / "ru_ru.json"
    if ftb_game.exists():
        data = load_json(ftb_game)
        print(f"  [ftbquestlocalizer/lang/ru_ru.json]")
        print(f"    quest49477F09DF6EBA50.title = {data.get('ftbquests.chapter.villagers.quest49477F09DF6EBA50.title')}")
        print(f"    quest49477F09DF6EBA50.description1 = {data.get('ftbquests.chapter.villagers.quest49477F09DF6EBA50.description1')}")
        print(f"    quest61501449BF31B773.description2 = {data.get('ftbquests.chapter.ii__building_up_the_farm.quest61501449BF31B773.description2')}")
    else:
        print(f"  [!] Файл не найден: {ftb_game}")

if __name__ == "__main__":
    apply_translations()
    sync_to_game()
    verify_game_files()
