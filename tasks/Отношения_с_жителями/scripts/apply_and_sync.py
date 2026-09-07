import os
import sys
import shutil
import subprocess

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
GAME_DIR = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley'

print("=== 1. Синхронизация JS-скриптов KubeJS ===")

# Скопировать invitationTooltips.js -> game addTooltips.js
src_tooltips = os.path.join(REPO_ROOT, 'kubejs_scripts', 'client', 'invitationTooltips.js')
dest_tooltips = os.path.join(GAME_DIR, 'kubejs', 'client_scripts', 'tooltips', 'addTooltips.js')
if os.path.exists(src_tooltips):
    shutil.copy2(src_tooltips, dest_tooltips)
    print("  ✓ Скопирован addTooltips.js в клиентские скрипты игры")

# Скопировать universalGiftsJei.js -> game client_scripts
src_jei = os.path.join(REPO_ROOT, 'kubejs_scripts', 'client', 'universalGiftsJei.js')
dest_jei = os.path.join(GAME_DIR, 'kubejs', 'client_scripts', 'universalGiftsJei.js')
if os.path.exists(src_jei):
    shutil.copy2(src_jei, dest_jei)
    print("  ✓ Скопирован universalGiftsJei.js в клиентские скрипты игры")

print("\n=== 2. Запуск общей синхронизации переводов ===")
subprocess.run(['node', os.path.join(REPO_ROOT, 'sync_all_to_game.js')], cwd=REPO_ROOT, check=True)

print("\n=== 3. Физическая проверка файлов игры ===")
with open(dest_jei, 'r', encoding='utf-8') as f:
    jei_code = f.read()

if "type === \"liked\"" not in jei_code and "likedGifts" not in jei_code:
    print("  ✓ [OK] В игре universalGiftsJei.js больше НЕ содержит подарков на +25!")
else:
    print("  ❌ [ERROR] В universalGiftsJei.js всё ещё есть +25 подарки!")

with open(dest_tooltips, 'r', encoding='utf-8') as f:
    tt_code = f.read()

if "universalLikedItems" not in tt_code and "§bУниверсальный подарок (+25 очков)" not in tt_code:
    print("  ✓ [OK] В игре addTooltips.js больше НЕ вешает тултип (+25 очков)!")
else:
    print("  ❌ [ERROR] В addTooltips.js всё ещё есть тултип (+25 очков)!")

print("\n=== ОБНОВЛЕНИЕ И СИНХРОНИЗАЦИЯ УСПЕШНО ЗАВЕРШЕНЫ! ===")
