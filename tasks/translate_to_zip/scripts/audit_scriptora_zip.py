import os
import sys
import zipfile
import json
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

ZIP_PATH = r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\tasks\translate_to_zip\Scriptora_Society.Sunlit.Valley.4.0.4 (1).zip'
GAME_DIR = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley'
REPO_ROOT = r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода'

print("=== 1. Анализ исходного архива Scriptora ===")
with zipfile.ZipFile(ZIP_PATH, 'r') as zf:
    zip_files = zf.namelist()

print(f"Всего файлов в архиве Scriptora: {len(zip_files)}")
zip_non_dirs = [f for f in zip_files if not f.endswith('/')]
print(f"Файлов (не папок): {len(zip_non_dirs)}")

for f in sorted(zip_non_dirs)[:30]:
    print(f"  - {f}")
if len(zip_non_dirs) > 30:
    print(f"  ... и ещё {len(zip_non_dirs) - 30} файлов")
