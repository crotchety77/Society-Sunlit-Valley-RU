import json
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

en_p = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\society_trading\lang\en_us.json"
ru_p = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\society_trading\lang\ru_ru.json"

en = json.load(open(en_p, encoding='utf-8'))
ru = json.load(open(ru_p, encoding='utf-8'))

missing = {k: en[k] for k in en if k not in ru}
print(f"Missing keys in society_trading ru_ru.json: {len(missing)}")
for k, v in sorted(missing.items()):
    print(f'"{k}": "{v}",')
