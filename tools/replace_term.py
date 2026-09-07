import os
import json
import re
import sys
import argparse
import subprocess

sys.stdout.reconfigure(encoding='utf-8')

PROJECT_TRANSLATIONS = r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\translations'
GAME_ASSETS = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets'
SYNC_SCRIPT = r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\sync_all_to_game.js'

def search_and_replace_in_json(filepath, old_term, new_term, is_regex=False, case_sensitive=True):
    if not os.path.exists(filepath):
        return []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return []

    changes = []
    flags = 0 if case_sensitive else re.IGNORECASE
    
    for k, v in list(data.items()):
        if isinstance(v, str):
            if is_regex:
                if re.search(old_term, v, flags):
                    new_v = re.sub(old_term, new_term, v, flags=flags)
                    if new_v != v:
                        data[k] = new_v
                        changes.append((k, v, new_v))
            else:
                if case_sensitive:
                    if old_term in v:
                        new_v = v.replace(old_term, new_term)
                        data[k] = new_v
                        changes.append((k, v, new_v))
                else:
                    pattern = re.escape(old_term)
                    if re.search(pattern, v, re.IGNORECASE):
                        new_v = re.sub(pattern, new_term, v, flags=re.IGNORECASE)
                        if new_v != v:
                            data[k] = new_v
                            changes.append((k, v, new_v))

    if changes:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    return changes

def run_replacement(old_term, new_term, is_regex=False, case_sensitive=True, sync=True):
    print(f"====================================================")
    print(f"🔍 ЗАМЕНА ТЕРМИНА: '{old_term}' -> '{new_term}'")
    print(f"====================================================")

    all_changes = {}

    # 1. Search in translations/
    for root, dirs, files in os.walk(PROJECT_TRANSLATIONS):
        for f in files:
            if f.endswith('.json'):
                fp = os.path.join(root, f)
                ch = search_and_replace_in_json(fp, old_term, new_term, is_regex, case_sensitive)
                if ch:
                    all_changes[fp] = ch

    # 2. Search in game assets/
    if os.path.exists(GAME_ASSETS):
        for root, dirs, files in os.walk(GAME_ASSETS):
            for f in files:
                if f.endswith('.json'):
                    fp = os.path.join(root, f)
                    ch = search_and_replace_in_json(fp, old_term, new_term, is_regex, case_sensitive)
                    if ch:
                        all_changes[fp] = ch

    # Output summary
    total_keys = sum(len(ch) for ch in all_changes.values())
    print(f"\nНайдено и заменено вхождений: {total_keys} (файлов: {len(all_changes)})")

    for fp, ch_list in all_changes.items():
        rel = os.path.relpath(fp, r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода') if 'СозданиеПеревода' in fp else fp
        print(f"\n📁 [{rel}] ({len(ch_list)} замен):")
        for k, old_val, new_val in ch_list[:10]:
            print(f"  Ключ: {k}")
            print(f"    - {repr(old_val)}")
            print(f"    + {repr(new_val)}")
        if len(ch_list) > 10:
            print(f"    ... и ещё {len(ch_list) - 10} замен.")

    # 3. Sync if requested
    if sync and os.path.exists(SYNC_SCRIPT):
        print("\n🚀 Запуск общей синхронизации sync_all_to_game.js...")
        subprocess.run(['node', SYNC_SCRIPT], cwd=r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода')

    print("\n✅ Замена и проверка завершены. Нажмите F3 + T в игре!")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Скрипт сквозной замены терминов по всем языковым файлам")
    parser.add_argument("old", help="Старый термин / текст для поиска")
    parser.add_argument("new", help="Новый термин / текст для замены")
    parser.add_argument("--regex", action="store_true", help="Использовать регулярные выражения")
    parser.add_argument("--ignore-case", action="store_true", help="Игнорировать регистр при поиске")
    parser.add_argument("--no-sync", action="store_true", help="Не запускать sync_all_to_game.js")

    args = parser.parse_args()
    run_replacement(args.old, args.new, is_regex=args.regex, case_sensitive=not args.ignore_case, sync=not args.no_sync)
