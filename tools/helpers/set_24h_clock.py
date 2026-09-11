import os
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

fp = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\config\guiclock.json5'
if os.path.exists(fp):
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content.replace('"_24hourformat": false', '"_24hourformat": true')

    with open(fp, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print("✅ Успешно обновлен config/guiclock.json5:")
    with open(fp, 'r', encoding='utf-8') as f:
        for line in f:
            if '_24hourformat' in line:
                print(" ", line.strip())
else:
    print(f"❌ Файл не найден: {fp}")
