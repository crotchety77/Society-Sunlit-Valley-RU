import os
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

ru_lang_path = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\longwings\lang\ru_ru.json'
ru_lang = {}
if os.path.exists(ru_lang_path):
    with open(ru_lang_path, 'r', encoding='utf-8') as f:
        ru_lang = json.load(f)

fp = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\startup_scripts\globalRegistry.js'
with open(fp, 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('global.longwings = [')
idx_end = text.find('];', idx)
block = text[idx:idx_end+2]

entries = re.findall(r'variant:\s*"([^"]+)",\s*rarity:\s*(\d+),\s*size:\s*"([^"]+)",\s*type:\s*"([^"]+)"', block)

print(f"Всего видов в реестре: {len(entries)}\n")
print(f"| Индекс | Вариант (ID) | Русское название | Редкость (Rarity) | Размер | Тип |")
print(f"| :---: | :--- | :--- | :---: | :---: | :---: |")
for i, (var, rar, sz, tp) in enumerate(entries[:25]):
    ru_name = ru_lang.get(f"item.longwings.{var}", ru_lang.get(f"entity.longwings.{var}", var.replace("_", " ").title()))
    print(f"| **{i}** | `{var}` | **{ru_name}** | {rar} | {sz} | {tp} |")
