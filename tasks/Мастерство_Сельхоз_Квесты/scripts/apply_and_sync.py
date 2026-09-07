import os
import json
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')

TASK_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NEW_TRANSLATE_PATH = os.path.join(TASK_DIR, 'new_translate.md')
ROOT_DIR = os.path.dirname(os.path.dirname(TASK_DIR))

SOCIETY_JSON = os.path.join(ROOT_DIR, 'translations', 'society', 'ru_ru.json')
QUESTS_JSON = os.path.join(ROOT_DIR, 'translations', 'ftbquests', 'ru_ru.json')
SKILLS_JSON = os.path.join(ROOT_DIR, 'translations', 'skills', 'ru_ru.json')

GAME_SOCIETY = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\society\lang\ru_ru.json'
GAME_QUESTS = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\ftbquestlocalizer\lang\ru_ru.json'
GAME_SKILLS = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\society_skills\lang\ru_ru.json'

SYNC_SCRIPT = os.path.join(ROOT_DIR, 'sync_all_to_game.js')

def parse_blocks(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    matches = re.findall(r'```json\s*(\{[\s\S]*?\})\s*```', content)
    if len(matches) < 3:
        raise ValueError(f"Expected at least 3 JSON blocks in new_translate.md, found {len(matches)}")
    
    society_keys = json.loads(matches[0])
    quests_keys = json.loads(matches[1])
    skills_keys = json.loads(matches[2])
    return society_keys, quests_keys, skills_keys

def apply_and_sync():
    print("=== 1. Чтение данных из new_translate.md ===")
    soc_keys, qst_keys, skl_keys = parse_blocks(NEW_TRANSLATE_PATH)
    
    print("\n=== 2. Обновление translations/society/ru_ru.json ===")
    with open(SOCIETY_JSON, 'r', encoding='utf-8') as f:
        soc_data = json.load(f)
    for k, v in soc_keys.items():
        soc_data[k] = v
        print(f"  {k} -> {v}")
    with open(SOCIETY_JSON, 'w', encoding='utf-8') as f:
        json.dump(soc_data, f, ensure_ascii=False, indent=2)

    print("\n=== 3. Обновление translations/ftbquests/ru_ru.json ===")
    with open(QUESTS_JSON, 'r', encoding='utf-8') as f:
        qst_data = json.load(f)
    for k, v in qst_keys.items():
        qst_data[k] = v
        print(f"  {k} -> {v}")
    with open(QUESTS_JSON, 'w', encoding='utf-8') as f:
        json.dump(qst_data, f, ensure_ascii=False, indent=2)

    print("\n=== 4. Обновление translations/skills/ru_ru.json ===")
    with open(SKILLS_JSON, 'r', encoding='utf-8') as f:
        skl_data = json.load(f)
    for k, v in skl_keys.items():
        skl_data[k] = v
        print(f"  {k} -> {v}")
    with open(SKILLS_JSON, 'w', encoding='utf-8') as f:
        json.dump(skl_data, f, ensure_ascii=False, indent=2)

    print("\n=== 5. Запуск общей синхронизации sync_all_to_game.js ===")
    res = subprocess.run(['node', SYNC_SCRIPT], cwd=ROOT_DIR, capture_output=True, text=True, encoding='utf-8')
    if res.returncode != 0:
        print("Ошибка синхронизации:", res.stderr)
        return False
    print("  Синхронизация завершена успешно.")

    print("\n=== 6. ПРЯМАЯ ВЕРИФИКАЦИЯ ФИЗИЧЕСКИХ ФАЙЛОВ ИГРЫ ===")
    with open(GAME_SOCIETY, 'r', encoding='utf-8') as f:
        game_soc = json.load(f)
    with open(GAME_QUESTS, 'r', encoding='utf-8') as f:
        game_qst = json.load(f)
    with open(GAME_SKILLS, 'r', encoding='utf-8') as f:
        game_skl = json.load(f)

    all_ok = True
    for k, exp in soc_keys.items():
        act = game_soc.get(k)
        if act == exp:
            print(f"  [OK] society: {k} == {act}")
        else:
            print(f"  [FAIL] society: {k}: ожидалось '{exp}', получено '{act}'")
            all_ok = False

    for k, exp in qst_keys.items():
        act = game_qst.get(k)
        if act == exp:
            print(f"  [OK] quests: {k} == {act}")
        else:
            print(f"  [FAIL] quests: {k}: ожидалось '{exp}', получено '{act}'")
            all_ok = False

    for k, exp in skl_keys.items():
        act = game_skl.get(k)
        if act == exp:
            print(f"  [OK] skills: {k} == {act}")
        else:
            print(f"  [FAIL] skills: {k}: ожидалось '{exp}', получено '{act}'")
            all_ok = False

    return all_ok

if __name__ == '__main__':
    success = apply_and_sync()
    if not success:
        sys.exit(1)
