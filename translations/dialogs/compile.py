import os
import sys
import json
import re

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

review_dir = os.path.dirname(os.path.abspath(__file__))
ru_data = {}
qa_errors = []

files = sorted([f for f in os.listdir(review_dir) if f.endswith('.md') and not f.startswith('README')])

total_parsed = 0
translated_count = 0

for file in files:
    file_path = os.path.join(review_dir, file)
    with open(file_path, 'r', encoding='utf-8') as f:
        for line_index, line in enumerate(f):
            line = line.strip()
            if line.startswith('|') and '`dialog.npc.' in line:
                parts = [p.strip() for p in line.split('|')]
                if len(parts) >= 4:
                    m = re.search(r'`([^`]+)`', parts[1])
                    if m:
                        key = m.group(1)
                        ru_val = parts[3]
                        total_parsed += 1
                        
                        if ru_val:
                            if re.search(r'(?<!%)%(?!%)', ru_val):
                                qa_errors.append(f"[ОШИБКА %] В файле {file} (строка {line_index + 1}): знак % в ключе '{key}'. Замените на %%!")
                            ru_data[key] = ru_val
                            translated_count += 1

print('====================================================')
print('         СБОРКА ПЕРЕВОДА ДИАЛОГОВ (SOCIETY)')
print('====================================================')
print(f'Всего строк диалогов найдено: {total_parsed}')
print(f'Переведено строк:             {translated_count} / {total_parsed}')
print('----------------------------------------------------')

if qa_errors:
    print('\n[ВНИМАНИЕ] Обнаружены критические ошибки форматирования:')
    for err in qa_errors:
        print(' ❌ ' + err)
    print('----------------------------------------------------')

out_ru_path = os.path.join(review_dir, 'ru_ru.json')
with open(out_ru_path, 'w', encoding='utf-8') as f:
    json.dump(ru_data, f, ensure_ascii=False, indent=2)

print(f'✅ Итоговый файл успешно сохранён:\n   {out_ru_path}')

modpack_path = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\dialog\lang\ru_ru.json'
try:
    modpack_dir = os.path.dirname(modpack_path)
    if os.path.exists(modpack_dir):
        with open(modpack_path, 'w', encoding='utf-8') as f:
            json.dump(ru_data, f, ensure_ascii=False, indent=2)
        print(f'\n🚀 [СИНХРОНИЗАЦИЯ] Файл скопирован в модпак:\n   {modpack_path}')
        print('   (В игре нажмите F3 + T для применения перевода)')
except Exception:
    pass

print('====================================================\n')
