import os
import json
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')

TASK_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NEW_TRANSLATE_PATH = os.path.join(TASK_DIR, 'new_translate.md')
ROOT_DIR = os.path.dirname(os.path.dirname(TASK_DIR))

SOCIETY_TRANSLATION_FILE = os.path.join(ROOT_DIR, 'translations', 'society', 'ru_ru.json')
GAME_SOCIETY_FILE = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\society\lang\ru_ru.json'
SYNC_SCRIPT = os.path.join(ROOT_DIR, 'sync_all_to_game.js')

def parse_new_translate(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    json_match = re.search(r'```json\s*(\{[\s\S]*?\})\s*```', content)
    if not json_match:
        raise ValueError("Could not find json block in new_translate.md")
    return json.loads(json_match.group(1))

def apply_and_sync():
    print("=== 1. Чтение переводов из new_translate.md ===")
    keys = parse_new_translate(NEW_TRANSLATE_PATH)
    for k, v in keys.items():
        print(f"  {k} -> {v}")

    print("\n=== 2. Применение в translations/society/ru_ru.json ===")
    with open(SOCIETY_TRANSLATION_FILE, 'r', encoding='utf-8') as f:
        soc_data = json.load(f)
    for k, v in keys.items():
        soc_data[k] = v
    with open(SOCIETY_TRANSLATION_FILE, 'w', encoding='utf-8') as f:
        json.dump(soc_data, f, ensure_ascii=False, indent=2)
    print("  Успешно сохранено.")

    print("\n=== 3. Запуск общей синхронизации sync_all_to_game.js ===")
    res = subprocess.run(['node', SYNC_SCRIPT], cwd=ROOT_DIR, capture_output=True, text=True, encoding='utf-8')
    if res.returncode != 0:
        print("Ошибка синхронизации:", res.stderr)
        return False
    print("  Синхронизация завершена успешно.")

    print("\n=== 4. ПРЯМАЯ ВЕРИФИКАЦИЯ ФИЗИЧЕСКИХ ФАЙЛОВ ИГРЫ ===")
    with open(GAME_SOCIETY_FILE, 'r', encoding='utf-8') as f:
        game_data = json.load(f)

    all_ok = True
    for k, expected_v in keys.items():
        actual_v = game_data.get(k)
        if actual_v == expected_v:
            print(f"  [OK] {k} == {actual_v}")
        else:
            print(f"  [FAIL] {k}: ожидалось '{expected_v}', получено '{actual_v}'")
            all_ok = False

    return all_ok

if __name__ == '__main__':
    success = apply_and_sync()
    if not success:
        sys.exit(1)
