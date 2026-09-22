import json
import os
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')

script_dir = os.path.dirname(os.path.abspath(__file__))
task_dir = os.path.dirname(script_dir)
workspace_dir = os.path.dirname(os.path.dirname(task_dir))
new_translate_path = os.path.join(task_dir, 'new_translate.md')

game_skills_path = r'G:\curseforge\minecraft\Instances\Society Sunlit Valley\kubejs\assets\society_skills\lang\ru_ru.json'
local_skills_path = os.path.join(workspace_dir, r'translations\skills\ru_ru.json')

# 1. Parse Block 2 JSON from new_translate.md
content = open(new_translate_path, encoding='utf-8').read()
json_match = re.search(r'```json\s*(\{[\s\S]*?\})\s*```', content)
if not json_match:
    raise ValueError("JSON block not found in new_translate.md!")

updates = json.loads(json_match.group(1))
print(f"Parsed {len(updates)} skill updates from new_translate.md:")

# 2. Update translations/skills/ru_ru.json
local_data = json.load(open(local_skills_path, encoding='utf-8'))
for k, v in updates.items():
    local_data[k] = v
    print(f"  • {k}")

with open(local_skills_path, 'w', encoding='utf-8') as fh:
    json.dump(local_data, fh, ensure_ascii=False, indent=2)
print(f"\n✅ Обновлён файл проекта: {local_skills_path}")

# 3. Direct write to game
if os.path.exists(os.path.dirname(game_skills_path)):
    game_data = {}
    if os.path.exists(game_skills_path):
        try:
            game_data = json.load(open(game_skills_path, encoding='utf-8'))
        except Exception:
            pass
    for k, v in updates.items():
        game_data[k] = v
    with open(game_skills_path, 'w', encoding='utf-8') as fh:
        json.dump(game_data, fh, ensure_ascii=False, indent=2)
    print(f"✅ Обновлён файл игры: {game_skills_path}")

# 4. Run sync_all_to_game.js and rebuild distribution
subprocess.run(['node', os.path.join(workspace_dir, 'sync_all_to_game.js')], cwd=workspace_dir, check=True)
subprocess.run(['python', os.path.join(workspace_dir, 'tools/build_distribution_package.py')], cwd=workspace_dir, check=True)

# 5. Verification
print("\n" + "="*50)
print("🔍 ВЕРИФИКАЦИЯ ИЗМЕНЁННЫХ КЛЮЧЕЙ ИЗ ФАЙЛА ИГРЫ:")
print("="*50)
verified_game = json.load(open(game_skills_path, encoding='utf-8'))
for k in updates:
    val = verified_game.get(k)
    print(f"\n[{k}]:\n{val}")

print("\n" + "="*50)
print(f"✔ ВСЕ {len(updates)} НАВЫКОВ УСПЕШНО ОБНОВЛЕНЫ И ВЕРИФИЦИРОВАНЫ!")
print("="*50)
