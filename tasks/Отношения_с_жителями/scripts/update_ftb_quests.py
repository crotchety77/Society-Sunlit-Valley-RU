# -*- coding: utf-8 -*-
"""
Скрипт обновления карточки «Вручение подарков» в FTB Quests (getting_started.snbt)
и локализации ftbquestlocalizer.
"""
import os
import sys
import json
import shutil

# Ensure UTF-8 output on Windows console
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
GAME_SNBT = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\config\ftbquests\quests\chapters\getting_started.snbt"
GAME_FTB_LANG_DIR = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\ftbquestlocalizer\lang"
PROJ_FTB_DIR = os.path.join(PROJECT_ROOT, "translations", "ftbquests")
PROJ_BACKUP_SNBT = os.path.join(PROJECT_ROOT, "game_data", "ftbquests", "chapters")

def main():
    print("=== [1/4] Обновление локализации FTB Quests (из new_translate) ===")
    os.makedirs(PROJ_FTB_DIR, exist_ok=True)
    ru_file = os.path.join(PROJ_FTB_DIR, "ru_ru.json")
    en_file = os.path.join(PROJ_FTB_DIR, "en_us.json")
    new_translate_path = os.path.join(PROJECT_ROOT, "tasks", "Отношения_с_жителями", "new_translate")
    
    with open(ru_file, "r", encoding="utf-8") as f:
        ru_data = json.load(f)
    with open(en_file, "r", encoding="utf-8") as f:
        en_data = json.load(f)
        
    # Read exact keys from new_translate
    import re
    with open(new_translate_path, "r", encoding="utf-8") as f:
        nt_text = f.read()
    match = re.search(r'### Файл 4: `translations/ftbquests/ru_ru\.json`\s*```json\s*(\{[\s\S]*?\})\s*```', nt_text)
    if match:
        quest_data = json.loads(match.group(1))
        ru_data.update(quest_data)
        print("  ✅ Считаны ключи из new_translate и добавлены в ru_ru.json")
    else:
        print("  ⚠️ Не удалось распарсить JSON из new_translate, оставляем существующий ru_ru.json")
    
    en_data["ftbquests.chapter.getting_started.quest3E08F21BA8F69499.description2"] = "&6Shift + Right Click&r on a villager with an item to give them a gift (cooldown: &6once every 4 days&r). Daily chatter grants &a+5 points&r."
    en_data["ftbquests.chapter.getting_started.quest3E08F21BA8F69499.description4"] = "&6★ Gift Categories (100 pts = 1 ♥, max 500):&r\n• &d💖 Loved:&r &a+40 pts&r &7(nearly half a heart)&r\n• &b👍 Liked:&r &a+25 pts&r &7(quarter heart)&r\n• &f😐 Neutral:&r &a+10 pts&r\n• &c👎 Disliked:&r &c-15 pts&r\n• &4💔 Hated:&r &4-30 pts&r"
    en_data["ftbquests.chapter.getting_started.quest3E08F21BA8F69499.description5"] = "&6★ Universal Loved (+40 for all):&r\n&ePrismatic Shard&r, &eRabbit's Foot&r, &eOolong Tea&r, &eSunlit Pearl&r, &eJellie Wine&r, &eGnome&r, &eBowl of Soul&r, &ePearl Block&r."
    en_data["ftbquests.chapter.getting_started.quest3E08F21BA8F69499.description6"] = "&6★ Rewards at ♥5 Hearts:&r\nAt max friendship, villagers give unique &eSkill Books&r (&bBanker&r, &bMarket&r, &bLibrarian&r) and rare artifacts!"

    with open(ru_file, "w", encoding="utf-8") as f:
        json.dump(ru_data, f, ensure_ascii=False, indent=2)
    with open(en_file, "w", encoding="utf-8") as f:
        json.dump(en_data, f, ensure_ascii=False, indent=2)
    print("Обновлены локальные файлы translations/ftbquests/ru_ru.json и en_us.json")

    print("=== [2/4] Синхронизация JSON в профиль игры ===")
    os.makedirs(GAME_FTB_LANG_DIR, exist_ok=True)
    game_ru = os.path.join(GAME_FTB_LANG_DIR, "ru_ru.json")
    game_en = os.path.join(GAME_FTB_LANG_DIR, "en_us.json")
    shutil.copy2(ru_file, game_ru)
    shutil.copy2(en_file, game_en)
    print(f"Скопировано -> {game_ru}")
    print(f"Скопировано -> {game_en}")

    print("=== [3/4] Добавление {@pagebreak} в getting_started.snbt ===")
    os.makedirs(PROJ_BACKUP_SNBT, exist_ok=True)
    shutil.copy2(GAME_SNBT, os.path.join(PROJ_BACKUP_SNBT, "getting_started.snbt"))
    
    with open(GAME_SNBT, "r", encoding="utf-8") as f:
        content = f.read()

    target_block = """\t\t\tdescription: [
\t\t\t\t"{ftbquests.chapter.getting_started.quest3E08F21BA8F69499.description1}"
\t\t\t\t""
\t\t\t\t"{ftbquests.chapter.getting_started.quest3E08F21BA8F69499.description2}"
\t\t\t\t""
\t\t\t\t"{ftbquests.chapter.getting_started.quest3E08F21BA8F69499.description3}"
\t\t\t]"""

    replacement_block = """\t\t\tdescription: [
\t\t\t\t"{ftbquests.chapter.getting_started.quest3E08F21BA8F69499.description1}"
\t\t\t\t""
\t\t\t\t"{ftbquests.chapter.getting_started.quest3E08F21BA8F69499.description2}"
\t\t\t\t""
\t\t\t\t"{ftbquests.chapter.getting_started.quest3E08F21BA8F69499.description3}"
\t\t\t\t"{@pagebreak}"
\t\t\t\t"{ftbquests.chapter.getting_started.quest3E08F21BA8F69499.description4}"
\t\t\t\t""
\t\t\t\t"{ftbquests.chapter.getting_started.quest3E08F21BA8F69499.description5}"
\t\t\t\t""
\t\t\t\t"{ftbquests.chapter.getting_started.quest3E08F21BA8F69499.description6}"
\t\t\t]"""

    if target_block in content:
        content = content.replace(target_block, replacement_block)
        with open(GAME_SNBT, "w", encoding="utf-8") as f:
            f.write(content)
        with open(os.path.join(PROJ_BACKUP_SNBT, "getting_started.snbt"), "w", encoding="utf-8") as f:
            f.write(content)
        print("✅ Успешно обновлен getting_started.snbt со страницей 2!")
    elif "{@pagebreak}" in content and "quest3E08F21BA8F69499.description4" in content:
        print("✅ getting_started.snbt уже содержит pagebreak для данного квеста.")
    else:
        print("❌ ОШИБКА: Исходный блок квеста не найден в getting_started.snbt!")

    print("=== [4/4] ВЕРИФИКАЦИЯ ФАЙЛОВ ИГРЫ ===")
    with open(GAME_SNBT, "r", encoding="utf-8") as f:
        snbt_check = f.read()
    with open(game_ru, "r", encoding="utf-8") as f:
        ru_check = json.load(f)
        
    pagebreak_ok = "{@pagebreak}" in snbt_check and "quest3E08F21BA8F69499.description4" in snbt_check
    lang_ok = "ftbquests.chapter.getting_started.quest3E08F21BA8F69499.description4" in ru_check
    
    if pagebreak_ok and lang_ok:
        print("✅ ВЕРИФИКАЦИЯ ПРОЙДЕНА: SNBT и ru_ru.json в папке игры содержат все 2 страницы квеста!")
        print("\n--- Проверенный текст страницы 2 из игрового ru_ru.json: ---")
        print(f"description4: {ru_check['ftbquests.chapter.getting_started.quest3E08F21BA8F69499.description4']}")
        print(f"description5: {ru_check['ftbquests.chapter.getting_started.quest3E08F21BA8F69499.description5']}")
        print(f"description6: {ru_check['ftbquests.chapter.getting_started.quest3E08F21BA8F69499.description6']}")
        print("----------------------------------------------------------\n")
        return True
    else:
        print(f"❌ ОШИБКА ВЕРИФИКАЦИИ: pagebreak_ok={pagebreak_ok}, lang_ok={lang_ok}")
        return False

if __name__ == "__main__":
    main()
