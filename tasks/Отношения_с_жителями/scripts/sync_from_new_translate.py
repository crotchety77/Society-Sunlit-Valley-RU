# -*- coding: utf-8 -*-
import os
import sys
import json
import re

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
NEW_TRANSLATE_PATH = os.path.join(PROJECT_ROOT, "tasks", "Отношения_с_жителями", "new_translate")
LOCAL_FTB_RU = os.path.join(PROJECT_ROOT, "translations", "ftbquests", "ru_ru.json")
GAME_FTB_RU = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\ftbquestlocalizer\lang\ru_ru.json"

def main():
    with open(NEW_TRANSLATE_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    # Find the JSON block for ftbquests
    match = re.search(r'### Файл 4: `translations/ftbquests/ru_ru\.json`\s*```json\s*(\{[\s\S]*?\})\s*```', text)
    if not match:
        print("❌ Не удалось найти JSON блок для ftbquests в new_translate")
        return False

    json_str = match.group(1)
    # Parse JSON
    try:
        quest_data = json.loads(json_str)
    except Exception as e:
        print(f"❌ Ошибка парсинга JSON из new_translate: {e}")
        return False

    print("Извлечены ключи из new_translate:")
    for k in quest_data:
        print(f"  - {k}")

    # 1. Update translations/ftbquests/ru_ru.json
    with open(LOCAL_FTB_RU, "r", encoding="utf-8") as f:
        local_data = json.load(f)
    local_data.update(quest_data)
    with open(LOCAL_FTB_RU, "w", encoding="utf-8") as f:
        json.dump(local_data, f, ensure_ascii=False, indent=2)

    # 2. Update game ru_ru.json
    with open(GAME_FTB_RU, "r", encoding="utf-8") as f:
        game_data = json.load(f)
    game_data.update(quest_data)
    with open(GAME_FTB_RU, "w", encoding="utf-8") as f:
        json.dump(game_data, f, ensure_ascii=False, indent=2)

    print("\n✅ УСПЕШНО СИНХРОНИЗИРОВАНО В ФАЙЛЫ ИГРЫ!")
    print("\n--- Проверенные значения из игрового файла ftbquestlocalizer/lang/ru_ru.json: ---")
    for k in ['description4', 'description5', 'description6']:
        full_k = f'ftbquests.chapter.getting_started.quest3E08F21BA8F69499.{k}'
        print(f"{k}:\n{game_data.get(full_k)}\n")
    return True

if __name__ == "__main__":
    main()
