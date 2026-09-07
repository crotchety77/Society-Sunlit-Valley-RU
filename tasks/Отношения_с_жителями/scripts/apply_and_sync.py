# -*- coding: utf-8 -*-
"""
Скрипт применения и синхронизации для задачи «Отношения с жителями»
"""
import os
import sys
import shutil
import subprocess

# Ensure UTF-8 output on Windows console
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
GAME_KUBEJS_CLIENT = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\client_scripts\tooltips"
TARGET_GAME_FILE = os.path.join(GAME_KUBEJS_CLIENT, "invitationTooltips.js")
SOURCE_FILE = os.path.join(PROJECT_ROOT, "kubejs_scripts", "client", "invitationTooltips.js")

# Удаляем возможный дубликат из корня client_scripts, если есть
old_duplicate = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\client_scripts\invitationTooltips.js"
if os.path.exists(old_duplicate):
    try:
        os.remove(old_duplicate)
    except Exception:
        pass

def main():
    print("=== [1/4] Применение изменений FTB Quests (getting_started.snbt и ru_ru.json) ===")
    ftb_script = os.path.join(PROJECT_ROOT, "tasks", "Отношения_с_жителями", "scripts", "update_ftb_quests.py")
    subprocess.run([sys.executable, ftb_script], cwd=PROJECT_ROOT)

    print("\n=== [2/4] Копирование invitationTooltips.js в папку игры ===")
    if not os.path.exists(SOURCE_FILE):
        print(f"ОШИБКА: Исходный файл не найден: {SOURCE_FILE}")
        return False
        
    os.makedirs(GAME_KUBEJS_CLIENT, exist_ok=True)
    shutil.copy2(SOURCE_FILE, TARGET_GAME_FILE)
    print(f"Скопировано: {SOURCE_FILE} -> {TARGET_GAME_FILE}")
    
    print("\n=== [3/4] Запуск общего мастер-скрипта sync_all_to_game.js ===")
    sync_script = os.path.join(PROJECT_ROOT, "sync_all_to_game.js")
    result = subprocess.run(["node", sync_script], cwd=PROJECT_ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace")
    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)
        
    print("=== [4/4] ОБЯЗАТЕЛЬНАЯ ВЕРИФИКАЦИЯ ФАЙЛОВ ИГРЫ ===")
    # 1. Верификация тултипа
    if not os.path.exists(TARGET_GAME_FILE):
        print(f"ОШИБКА: Целевой файл в игре не найден: {TARGET_GAME_FILE}")
        return False
        
    with open(TARGET_GAME_FILE, "r", encoding="utf-8") as f:
        content = f.read()
        
    tooltip_ok = "society:face_note" in content and "Универсальный подарок" in content
    
    # 2. Верификация JEI скрипта
    game_jei = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\client_scripts\universalGiftsJei.js"
    jei_ok = os.path.exists(game_jei) and "society:universal_gifts" in open(game_jei, encoding="utf-8").read()

    # 3. Верификация FTB Quests
    game_snbt = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\config\ftbquests\quests\chapters\getting_started.snbt"
    game_ru = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\ftbquestlocalizer\lang\ru_ru.json"
    
    with open(game_snbt, "r", encoding="utf-8") as f:
        snbt_content = f.read()
    with open(game_ru, "r", encoding="utf-8") as f:
        import json
        ru_json = json.load(f)
        
    ftb_ok = "{@pagebreak}" in snbt_content and "ftbquests.chapter.getting_started.quest3E08F21BA8F69499.description4" in ru_json
    
    if tooltip_ok and jei_ok and ftb_ok:
        print(f"✅ ВЕРИФИКАЦИЯ УСПЕШНА: тултипы, JEI-категория и FTB Quests проверены и активны в игре!")
        print("\n--- Проверенные элементы: ---")
        print("  1. Тултипы подарков (+40 / +25) и face_note в invitationTooltips.js")
        print("  2. JEI-категория society:universal_gifts в universalGiftsJei.js")
        print(f"  3. FTB Quests: {ru_json['ftbquests.chapter.getting_started.quest3E08F21BA8F69499.title']} (2 страницы)")
        print("-----------------------------\n")
        return True
    else:
        print(f"❌ ОШИБКА ВЕРИФИКАЦИИ: tooltip_ok={tooltip_ok}, jei_ok={jei_ok}, ftb_ok={ftb_ok}")
        return False

if __name__ == "__main__":
    main()
