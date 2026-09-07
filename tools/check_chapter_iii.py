import json
import re

snbt_path = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley (1)\config\ftbquests\quests\chapters\iii__advanced_farming.snbt"
with open(snbt_path, 'r', encoding='utf-8') as f:
    snbt_content = f.read()

# All quest IDs
# FTB quests quest structure:
# quests: [
#   {
#       id: "HEX"
#       ...
#   }
# ]
# Let's extract quests list
q_blocks = re.findall(r'id:\s*"([0-9A-Fa-f]+)"', snbt_content)
print(f"Total IDs in (1) iii__advanced_farming: {len(q_blocks)}")

# Let's check some keys
with open(r"c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\translations\ftbquests\ru_ru.json", 'r', encoding='utf-8') as f:
    ru_ru = json.load(f)

with open(r"c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\translations\ftbquests\en_us.json", 'r', encoding='utf-8') as f:
    en_us = json.load(f)

chapter_ru_keys = [k for k in ru_ru.keys() if "iii__advanced_farming" in k]
chapter_en_keys = [k for k in en_us.keys() if "iii__advanced_farming" in k]

print(f"Total ru_ru keys for iii__advanced_farming: {len(chapter_ru_keys)}")
print(f"Total en_us keys for iii__advanced_farming: {len(chapter_en_keys)}")

# Let's check if all quest keys in (1) exist in en_us and ru_ru
missing_in_ru = 0
for k in chapter_en_keys:
    if k not in ru_ru or not ru_ru[k]:
        missing_in_ru += 1
print(f"Missing in ru_ru: {missing_in_ru}")
