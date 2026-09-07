# -*- coding: utf-8 -*-
import os
import sys
import json
import subprocess
import re

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = r"c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода"
TASK_DIR = os.path.join(ROOT_DIR, "tasks", "task_aquaculture_hooks")
GAME_LANG_PATH = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\society\lang\ru_ru.json"
GAME_TOOLTIPS_PATH = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\client_scripts\tooltips\addTooltips.js"

def main():
    print("=== [1/3] Запуск синхронизации sync_all_to_game.js ===")
    res = subprocess.run(["node", "sync_all_to_game.js"], cwd=ROOT_DIR, capture_output=True, text=True, encoding="utf-8")
    print(res.stdout)
    if res.stderr:
        print("[ERROR]", res.stderr)
    
    print("=== [2/3] Физическая верификация файла игры ru_ru.json ===")
    if not os.path.exists(GAME_LANG_PATH):
        raise FileNotFoundError(f"Файл игры не найден: {GAME_LANG_PATH}")
        
    with open(GAME_LANG_PATH, "r", encoding="utf-8") as f:
        game_lang = json.load(f)
        
    keys_to_check = [
        "tooltip.aquaculture.iron_fishing_rod",
        "tooltip.aquaculture.gold_fishing_rod",
        "tooltip.aquaculture.neptunium_fishing_rod",
        "tooltip.netherdepthsupgrade.lava_fishing_rod",
        "tooltip.aquaculture.iron_hook",
        "tooltip.aquaculture.gold_hook",
        "tooltip.aquaculture.diamond_hook",
        "tooltip.aquaculture.redstone_hook",
        "tooltip.aquaculture.nether_star_hook",
        "tooltip.society.net_bobber",
        "tooltip.society.needle_bobber"
    ]
    
    verified_count = 0
    for k in keys_to_check:
        if k in game_lang:
            print(f"  [OK] {k} -> {game_lang[k][:60]}...")
            verified_count += 1
        else:
            print(f"  [FAIL] Ключ отсутствует: {k}")
            
    print(f"\nВерифицировано ключей в игре: {verified_count}/{len(keys_to_check)}")
    
    print("=== [3/3] Верификация client_scripts в игре ===")
    if os.path.exists(GAME_TOOLTIPS_PATH):
        with open(GAME_TOOLTIPS_PATH, "r", encoding="utf-8") as f:
            content = f.read()
            if "aquaculture:iron_fishing_rod" in content and "society:net_bobber" in content:
                print("  [OK] addTooltips.js успешно обновлён в игре!")
            else:
                print("  [WARNING] В addTooltips.js не найдены новые регистрации.")

if __name__ == "__main__":
    main()
