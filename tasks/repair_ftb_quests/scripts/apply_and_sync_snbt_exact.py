import os
import sys
import re
import shutil
import json
import subprocess

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

GAME_DIR = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\config\ftbquests\quests\chapters'
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

def replace_snbt_quest_desc(chapter_file, quest_id, new_lines):
    fpath = os.path.join(GAME_DIR, chapter_file)
    bak_path = fpath + '.bak'
    
    # Restore from .bak if exists to ensure clean baseline
    if os.path.exists(bak_path):
        with open(bak_path, 'r', encoding='utf-8') as f:
            content = f.read()
    else:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        shutil.copy2(fpath, bak_path)

    # Find `id: "{quest_id}"`
    pos = content.find(f'id: "{quest_id}"')
    if pos == -1:
        raise Exception(f"Quest {quest_id} not found in {chapter_file}")
        
    # Look backward for `description: [`
    desc_start = content.rfind('description: [', 0, pos)
    if desc_start == -1 or pos - desc_start > 1500:
        raise Exception(f"description block not found before id: {quest_id}")
        
    # Find matching `]`
    desc_end = content.find(']', desc_start)
    if desc_end == -1 or desc_end > pos:
        raise Exception(f"Closing `]` of description not found before id: {quest_id}")
        
    # Build new description content
    indent = '\n\t\t\t\t'
    formatted_lines = indent.join([f'"{l}"' for l in new_lines])
    new_desc_block = f"description: [{indent}{formatted_lines}\n\t\t\t]"
    
    new_content = content[:desc_start] + new_desc_block + content[desc_end+1:]
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"✓ Успешно обновлён квест {quest_id} в {chapter_file}")

# 1. Заменяем в iii__advanced_farming.snbt
butterfly_lines = [
    "{ftbquests.chapter.iii__advanced_farming.quest263CCA4D2EAF2629.description1}",
    "",
    "{ftbquests.chapter.iii__advanced_farming.quest263CCA4D2EAF2629.description2}",
    "",
    "{ftbquests.chapter.iii__advanced_farming.quest263CCA4D2EAF2629.description3}"
]
replace_snbt_quest_desc('iii__advanced_farming.snbt', '263CCA4D2EAF2629', butterfly_lines)

# 2. Заменяем в getting_started.snbt
gifts_lines = [
    "{ftbquests.chapter.getting_started.quest3E08F21BA8F69499.description1}",
    "",
    "{ftbquests.chapter.getting_started.quest3E08F21BA8F69499.description2}",
    "",
    "{ftbquests.chapter.getting_started.quest3E08F21BA8F69499.description3}"
]
replace_snbt_quest_desc('getting_started.snbt', '3E08F21BA8F69499', gifts_lines)

# 3. Синхронизируем переводы в игру
subprocess.run(['node', os.path.join(REPO_ROOT, 'sync_all_to_game.js')], cwd=REPO_ROOT, check=True)
print("✓ Синхронизация завершена!")
