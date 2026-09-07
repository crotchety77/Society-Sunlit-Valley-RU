#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json
import re
import shutil

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

ROOT_DIR = r"c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода"
SNBT_PATH = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\config\ftbquests\quests\chapters\iii__advanced_farming.snbt"
LOCAL_RU = os.path.join(ROOT_DIR, "translations", "ftbquests", "ru_ru.json")
LOCAL_EN = os.path.join(ROOT_DIR, "translations", "ftbquests", "en_us.json")
GAME_RU = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\ftbquestlocalizer\lang\ru_ru.json"
GAME_EN = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\ftbquestlocalizer\lang\en_us.json"
QUESTS_MD = os.path.join(ROOT_DIR, "tasks", "Translate_Mods", "translate_splendid_slimes", "quests_translate.md")

# 1. Backup SNBT
shutil.copyfile(SNBT_PATH, SNBT_PATH + ".bak")
print(f"📦 Создан бэкап: {SNBT_PATH}.bak")

# 2. Edit SNBT
with open(SNBT_PATH, 'r', encoding='utf-8') as f:
    snbt = f.read()

target_old = """\t\t\tdescription: [
\t\t\t\t"{ftbquests.chapter.iii__advanced_farming.quest632578AFE8A0D12D.description1}"
\t\t\t\t""
\t\t\t\t"{ftbquests.chapter.iii__advanced_farming.quest632578AFE8A0D12D.description2}"
\t\t\t\t""
\t\t\t\t"{ftbquests.chapter.iii__advanced_farming.quest632578AFE8A0D12D.description3}"
\t\t\t]
\t\t\tid: "632578AFE8A0D12D\""""

target_new = """\t\t\tdescription: [
\t\t\t\t"{ftbquests.chapter.iii__advanced_farming.quest632578AFE8A0D12D.description1}"
\t\t\t\t""
\t\t\t\t"{ftbquests.chapter.iii__advanced_farming.quest632578AFE8A0D12D.description2}"
\t\t\t\t""
\t\t\t\t"{ftbquests.chapter.iii__advanced_farming.quest632578AFE8A0D12D.description3}"
\t\t\t\t""
\t\t\t\t"{ftbquests.chapter.iii__advanced_farming.quest632578AFE8A0D12D.description4}"
\t\t\t]
\t\t\tid: "632578AFE8A0D12D\""""

if target_old in snbt:
    snbt = snbt.replace(target_old, target_new)
    with open(SNBT_PATH, 'w', encoding='utf-8') as f:
        f.write(snbt)
    print("✅ SNBT успешно обновлён (добавлен отдельный ключ description4)")
else:
    print("⚠️ Точный фрагмент не найден, проверяем регулярным выражением...")
    pattern = re.compile(
        r'(\t+description:\s*\[\s*\"\{ftbquests\.chapter\.iii__advanced_farming\.quest632578AFE8A0D12D\.description1\}\"[\s\S]*?\"\{ftbquests\.chapter\.iii__advanced_farming\.quest632578AFE8A0D12D\.description3\}\"\s*)(\]\s*id:\s*\"632578AFE8A0D12D\")'
    )
    if pattern.search(snbt):
        snbt = pattern.sub(
            r'\1\t\t\t\t""\n\t\t\t\t"{ftbquests.chapter.iii__advanced_farming.quest632578AFE8A0D12D.description4}"\n\t\t\t\2',
            snbt
        )
        with open(SNBT_PATH, 'w', encoding='utf-8') as f:
            f.write(snbt)
        print("✅ SNBT успешно обновлён через regex")

# 3. Update Lang Files
d3_text = "Ухаживать за ними проще, чем за скотом, хотя порой они создают куда больше хаоса..."
d4_text = "Чтобы определить породу Слайма, воспользуйтесь &6Анализатором слаймов&r!"
d4_en = "To identify a Slime's breed and stats, use a &6Slime Inspector&r!"

for path, is_ru in [(LOCAL_RU, True), (GAME_RU, True), (LOCAL_EN, False), (GAME_EN, False)]:
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            d = json.load(f)
        if is_ru:
            d["ftbquests.chapter.iii__advanced_farming.quest632578AFE8A0D12D.description3"] = d3_text
            d["ftbquests.chapter.iii__advanced_farming.quest632578AFE8A0D12D.description4"] = d4_text
        else:
            d["ftbquests.chapter.iii__advanced_farming.quest632578AFE8A0D12D.description4"] = d4_en
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(d, f, ensure_ascii=False, indent=2)
        print(f"✅ Обновлён языковой файл: {path}")

# 4. Update quests_translate.md
if os.path.exists(QUESTS_MD):
    with open(QUESTS_MD, 'r', encoding='utf-8') as f:
        md = f.read()
    md = md.replace(
        '"ftbquests.chapter.iii__advanced_farming.quest632578AFE8A0D12D.description3": "Ухаживать за ними проще, чем за скотом, хотя порой они создают куда больше хаоса...\\n\\nЧтобы определить породу Слайма, воспользуйтесь &6Анализатором слаймов&r!"',
        '"ftbquests.chapter.iii__advanced_farming.quest632578AFE8A0D12D.description3": "Ухаживать за ними проще, чем за скотом, хотя порой они создают куда больше хаоса...",\n  "ftbquests.chapter.iii__advanced_farming.quest632578AFE8A0D12D.description4": "Чтобы определить породу Слайма, воспользуйтесь &6Анализатором слаймов&r!"'
    )
    with open(QUESTS_MD, 'w', encoding='utf-8') as f:
        f.write(md)
    print("✅ Обновлён quests_translate.md")

