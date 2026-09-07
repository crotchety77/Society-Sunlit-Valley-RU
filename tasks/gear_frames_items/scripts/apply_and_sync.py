import os
import re
import json
import subprocess
import sys

if sys.stdout.encoding != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

TASK_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.dirname(TASK_DIR))
NEW_TRANSLATE_PATH = os.path.join(TASK_DIR, "new_translate.md")
SOCIETY_LANG_PATH = os.path.join(PROJECT_ROOT, "translations", "society", "ru_ru.json")
GAME_SOCIETY_LANG_PATH = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\society\lang\ru_ru.json"

def parse_new_translate(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Extract JSON code block
    json_match = re.search(r"```json\s*(\{[\s\S]*?\})\s*```", content)
    if not json_match:
        raise ValueError("Could not find JSON block in new_translate.md")
    
    return json.loads(json_match.group(1))

def apply_and_sync():
    print("1. Считывание ключей из new_translate.md...")
    translations = parse_new_translate(NEW_TRANSLATE_PATH)
    print(f"   Найдено {len(translations)} ключей.")

    print("2. Обновление translations/society/ru_ru.json...")
    with open(SOCIETY_LANG_PATH, "r", encoding="utf-8") as f:
        society_lang = json.load(f)
    
    for k, v in translations.items():
        society_lang[k] = v
    
    with open(SOCIETY_LANG_PATH, "w", encoding="utf-8") as f:
        json.dump(society_lang, f, ensure_ascii=False, indent=2)
    print("   ✅ translations/society/ru_ru.json обновлён.")

    print("3. Запуск общего sync_all_to_game.js...")
    subprocess.run(["node", "sync_all_to_game.js"], cwd=PROJECT_ROOT, check=True)

    print("4. Прямая верификация физического файла игры...")
    with open(GAME_SOCIETY_LANG_PATH, "r", encoding="utf-8") as f:
        game_lang = json.load(f)
    
    verified_keys = [
        "item.society.ancient_cog",
        "item.society.ancient_cog.description",
        "item.society.recycled_core",
        "item.society.recycled_core.description",
        "item.society.pink_matter",
        "item.society.pink_matter.description",
        "item.society.tiny_gnome",
        "item.society.tiny_gnome.description"
    ]
    print("\n--- РЕЗУЛЬТАТЫ ФИЗИЧЕСКОЙ ВЕРИФИКАЦИИ В ИГРЕ ---")
    for k in verified_keys:
        print(f"  {k} -> {game_lang.get(k)}")

if __name__ == "__main__":
    apply_and_sync()
