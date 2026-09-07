import os
import sys
import zipfile
import json
import hashlib

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

ZIP_PATH = r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\tasks\translate_to_zip\Scriptora_Society.Sunlit.Valley.4.0.4 (1).zip'
GAME_DIR = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley'
REPO_ROOT = r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода'

with zipfile.ZipFile(ZIP_PATH, 'r') as zf:
    zip_files = [f for f in zf.namelist() if not f.endswith('/')]
    zip_data = {f: zf.read(f) for f in zip_files}

print("=== КАТЕГОРИИ ФАЙЛОВ В АРХИВЕ SCRIPTORA ===")
categories = {}
for f in zip_files:
    top_dir = f.split('/')[0]
    categories.setdefault(top_dir, []).append(f)

for cat, flist in categories.items():
    print(f"  📁 {cat}: {len(flist)} файлов")

# Compare each file with GAME_DIR
print("\n=== СРАВНЕНИЕ ФАЙЛОВ SCRIPTORA С ТЕКУЩЕЙ ИГРОЙ ===")
identical_count = 0
modified_count = 0
missing_in_game = 0

for f, old_bytes in zip_data.items():
    game_path = os.path.join(GAME_DIR, f.replace('/', os.sep))
    if not os.path.exists(game_path):
        missing_in_game += 1
    else:
        with open(game_path, 'rb') as gf:
            cur_bytes = gf.read()
        if old_bytes == cur_bytes:
            identical_count += 1
        else:
            modified_count += 1

print(f"Идентичны: {identical_count}")
print(f"Изменены в текущей игре: {modified_count}")
print(f"Отсутствуют в игре: {missing_in_game}")

# Check files in GAME_DIR that are NEW compared to Scriptora
print("\n=== ПОИСК НОВЫХ ФАЙЛОВ ПЕРЕВОДА В ИГРЕ ===")
game_lang_files = []
# Scan kubejs/assets/*/lang/ru_ru.json
assets_dir = os.path.join(GAME_DIR, 'kubejs', 'assets')
if os.path.exists(assets_dir):
    for root, dirs, files in os.walk(assets_dir):
        for file in files:
            if file == 'ru_ru.json' or file.endswith('.png') or file.endswith('.json'):
                rel = os.path.relpath(os.path.join(root, file), GAME_DIR).replace('\\', '/')
                game_lang_files.append(rel)

# Scan patchouli_books
patchouli_dir = os.path.join(GAME_DIR, 'patchouli_books')
if os.path.exists(patchouli_dir):
    for root, dirs, files in os.walk(patchouli_dir):
        for file in files:
            rel = os.path.relpath(os.path.join(root, file), GAME_DIR).replace('\\', '/')
            game_lang_files.append(rel)

# Scan client_scripts/tooltips, jei, etc.
client_scripts_dir = os.path.join(GAME_DIR, 'kubejs', 'client_scripts')
if os.path.exists(client_scripts_dir):
    for root, dirs, files in os.walk(client_scripts_dir):
        for file in files:
            rel = os.path.relpath(os.path.join(root, file), GAME_DIR).replace('\\', '/')
            game_lang_files.append(rel)

new_in_game = [f for f in game_lang_files if f not in zip_data]
print(f"Всего файлов локализации/UI в игре: {len(game_lang_files)}")
print(f"Новых файлов (добавлено нами): {len(new_in_game)}")
print("\nПримеры новых файлов:")
for nf in sorted(new_in_game)[:25]:
    print(f"  + {nf}")
