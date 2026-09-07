# -*- coding: utf-8 -*-
import os
import sys
import json
import shutil
import subprocess

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

PROJECT_ROOT = r"c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода"
TASK_DIR = os.path.join(PROJECT_ROOT, "tasks", "task_cheeze_machinee")
NEW_TRANSLATE_MD = os.path.join(TASK_DIR, "new_translate.md")

SOCIETY_LANG_PATH = os.path.join(PROJECT_ROOT, "translations", "society", "ru_ru.json")
MEADOW_LANG_PATH = os.path.join(PROJECT_ROOT, "translations", "mods", "meadow.json")

GAME_PROFILE = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley"
GAME_SOCIETY_LANG = os.path.join(GAME_PROFILE, "kubejs", "assets", "society", "lang", "ru_ru.json")
GAME_MEADOW_LANG = os.path.join(GAME_PROFILE, "kubejs", "assets", "meadow", "lang", "ru_ru.json")

WORKSPACE_CLIENT_TOOLTIPS = os.path.join(PROJECT_ROOT, "game_data", "client_scripts", "tooltips", "addTooltips.js")
GAME_CLIENT_TOOLTIPS = os.path.join(GAME_PROFILE, "kubejs", "client_scripts", "tooltips", "addTooltips.js")

WORKSPACE_CHEESE_PRESS = os.path.join(PROJECT_ROOT, "game_data", "startup_scripts", "customMachines", "cheesePress.js")
GAME_CHEESE_PRESS = os.path.join(GAME_PROFILE, "kubejs", "startup_scripts", "customMachines", "cheesePress.js")

def apply_and_sync():
    print("1. Применение ключей из new_translate.md...")
    
    # Общество (Society)
    society_updates = {
        "block.society.cheese_press": "Ремесленный пресс для сыра",
        "block.society.cheese_press.description": "Производит сыр из молока за §e2 дня§7.",
        "society.working_block_entity.preserve_quality": "Сохраняет качество входных предметов",
        "tooltip.society.cheese_press.shift_1": "Работает вручную через взаимодействие с прессом. Также поддерживает автоматизацию с помощью §6Ремесленной воронки§7.",
        "tooltip.society.cheese_press.shift_2": "Может быть улучшен §6Розовой материей§7, после чего напрямую производит §6Выдержанный сыр§7, минуя этап выдержки в бочке.",
        "tooltip.society.cheese_form": "Производит сыр за §e90 секунд§7. Для каждого цикла требуется §6Сычужный фермент§7.",
        "tooltip.society.cheese_form.tip": "Производит обычный сыр §cбез качества§7.",
        "tooltip.society.cheese_form.shift_1": "Полностью поддерживает §aавтоматизацию§7: молоко и сычужный фермент загружаются автоматически, а готовый сыр выгружается через §6воронки§7."
    }

    with open(SOCIETY_LANG_PATH, "r", encoding="utf-8") as f:
        society_data = json.load(f)
    society_data.update(society_updates)
    with open(SOCIETY_LANG_PATH, "w", encoding="utf-8") as f:
        json.dump(society_data, f, ensure_ascii=False, indent=2)
    print("   ✅ translations/society/ru_ru.json обновлён.")

    # Meadow
    with open(MEADOW_LANG_PATH, "r", encoding="utf-8") as f:
        meadow_data = json.load(f)
    meadow_data["block.meadow.cheese_form"] = "Автоматический пресс для сыра"
    with open(MEADOW_LANG_PATH, "w", encoding="utf-8") as f:
        json.dump(meadow_data, f, ensure_ascii=False, indent=2)
    print("   ✅ translations/mods/meadow.json обновлён.")

    # 2. Синхронизация client_scripts и startup_scripts
    if os.path.exists(WORKSPACE_CLIENT_TOOLTIPS):
        os.makedirs(os.path.dirname(GAME_CLIENT_TOOLTIPS), exist_ok=True)
        shutil.copyfile(WORKSPACE_CLIENT_TOOLTIPS, GAME_CLIENT_TOOLTIPS)
        print("   ✅ kubejs/client_scripts/tooltips/addTooltips.js скопирован в игру.")
    
    if os.path.exists(WORKSPACE_CHEESE_PRESS):
        os.makedirs(os.path.dirname(GAME_CHEESE_PRESS), exist_ok=True)
        shutil.copyfile(WORKSPACE_CHEESE_PRESS, GAME_CHEESE_PRESS)
        print("   ✅ kubejs/startup_scripts/customMachines/cheesePress.js скопирован в игру.")

    # 3. Запуск общего sync_all_to_game.js
    print("\n2. Запуск sync_all_to_game.js...")
    subprocess.run(["node", "sync_all_to_game.js"], cwd=PROJECT_ROOT, check=True)

    # 4. Прямая физическая верификация
    print("\n3. ПРЯМАЯ ВЕРИФИКАЦИЯ ФИЗИЧЕСКИХ ФАЙЛОВ ИГРЫ:")
    
    print("\n--- Society (kubejs/assets/society/lang/ru_ru.json) ---")
    with open(GAME_SOCIETY_LANG, "r", encoding="utf-8") as f:
        game_society = json.load(f)
    for k in society_updates.keys():
        print(f"  {k} -> {game_society.get(k)}")

    print("\n--- Meadow (kubejs/assets/meadow/lang/ru_ru.json) ---")
    with open(GAME_MEADOW_LANG, "r", encoding="utf-8") as f:
        game_meadow = json.load(f)
    print(f"  block.meadow.cheese_form -> {game_meadow.get('block.meadow.cheese_form')}")

if __name__ == "__main__":
    apply_and_sync()
