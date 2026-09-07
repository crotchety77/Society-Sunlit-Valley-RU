import os
import re
import json
import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')

def parse_work_file(filepath):
    """
    Parses entries from a work_queue markdown file.
    Returns list of dicts with updated translations.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    blocks = content.split('--------------------------------------------------------------------------------')
    updates = {}

    for b in blocks:
        lines = [l.strip() for l in b.strip().split('\n') if l.strip()]
        if not lines:
            continue
        
        entry = {}
        for l in lines:
            if l.startswith('ID:'):
                entry['id'] = l.split(':', 1)[1].strip()
            elif l.startswith('Глава:'):
                entry['chapter'] = l.split(':', 1)[1].strip()
            elif l.startswith('RU title:'):
                val = l.split(':', 1)[1].strip()
                if val: entry['title'] = val
            elif l.startswith('RU subtitle:'):
                val = l.split(':', 1)[1].strip()
                if val: entry['subtitle'] = val
            elif re.match(r'^RU description\d+:', l):
                m = re.match(r'^RU description(\d+):(.*)$', l)
                idx = m.group(1)
                val = m.group(2).strip()
                if val:
                    entry.setdefault('descriptions', {})[idx] = val
            elif re.match(r'^RU task \[(.*?)\]:(.*)$', l):
                m = re.match(r'^RU task \[(.*?)\]:(.*)$', l)
                tid = m.group(1).strip()
                val = m.group(2).strip()
                if val:
                    entry.setdefault('tasks', {})[tid] = val
            elif re.match(r'^RU reward \[(.*?)\]:(.*)$', l):
                m = re.match(r'^RU reward \[(.*?)\]:(.*)$', l)
                rid = m.group(1).strip()
                val = m.group(2).strip()
                if val:
                    entry.setdefault('rewards', {})[rid] = val

        if 'id' in entry and 'chapter' in entry:
            updates[entry['id']] = entry

    return updates

def apply_and_sync():
    base_dir = r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\tasks\FTB_QUESTS_4_1_4'
    repo_ru_path = r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\translations\ftbquests\ru_ru.json'
    game_ru_path = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\ftbquestlocalizer\lang\ru_ru.json'

    repo_ru = json.load(open(repo_ru_path, encoding='utf-8'))
    game_ru = json.load(open(game_ru_path, encoding='utf-8')) if os.path.exists(game_ru_path) else dict(repo_ru)

    wq_dir = os.path.join(base_dir, 'work_queue')
    applied_count = 0

    for wf in ['priority1_new.md', 'priority2_changed.md', 'priority3_partially_translated.md', 'priority4_untranslated.md']:
        wfp = os.path.join(wq_dir, wf)
        if os.path.exists(wfp):
            updates = parse_work_file(wfp)
            for qid, u in updates.items():
                chap = u['chapter']
                if 'title' in u:
                    k = f"ftbquests.chapter.{chap}.quest{qid}.title"
                    repo_ru[k] = u['title']
                    game_ru[k] = u['title']
                    applied_count += 1
                if 'subtitle' in u:
                    k = f"ftbquests.chapter.{chap}.quest{qid}.subtitle"
                    repo_ru[k] = u['subtitle']
                    game_ru[k] = u['subtitle']
                    applied_count += 1
                if 'descriptions' in u:
                    for idx, dval in u['descriptions'].items():
                        k = f"ftbquests.chapter.{chap}.quest{qid}.description{idx}"
                        repo_ru[k] = dval
                        game_ru[k] = dval
                        applied_count += 1
                if 'tasks' in u:
                    for tid, tval in u['tasks'].items():
                        k = f"ftbquests.chapter.{chap}.quest{qid}.task.{tid}.title"
                        repo_ru[k] = tval
                        game_ru[k] = tval
                        applied_count += 1
                if 'rewards' in u:
                    for rid, rval in u['rewards'].items():
                        k = f"ftbquests.chapter.{chap}.quest{qid}.reward.{rid}.title"
                        repo_ru[k] = rval
                        game_ru[k] = rval
                        applied_count += 1

    # Save to repo
    with open(repo_ru_path, 'w', encoding='utf-8') as f:
        json.dump(repo_ru, f, ensure_ascii=False, indent=2)

    # Save to game
    with open(game_ru_path, 'w', encoding='utf-8') as f:
        json.dump(game_ru, f, ensure_ascii=False, indent=2)

    print(f"Applied {applied_count} translation updates to repo and game!")

    # Run sync_all_to_game.js if it exists
    sync_all = r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\sync_all_to_game.js'
    if os.path.exists(sync_all):
        subprocess.run(['node', sync_all], cwd=r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода')

if __name__ == '__main__':
    apply_and_sync()
