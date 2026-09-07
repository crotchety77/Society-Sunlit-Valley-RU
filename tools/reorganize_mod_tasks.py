#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/reorganize_mod_tasks.py
Реорганизует папки задач в tasks/Translate_Mods/ строго по порядку из GAMEPLAY_PRIORITY_AUDIT.md:
1. Завершённые моды (100%) -> tasks/Translate_Mods/completed/
2. Технические моды (Tier 3) -> tasks/Translate_Mods/technical/
3. Активные игровые моды (Tier 1) строго по убыванию непереведённых строк (cluttered, refurbished_furniture, dramaticdoors...) -> 01_name, 02_name...
4. Затем активные UI моды (Tier 2) по убыванию непереведённых строк.
5. Обновляет QUEUE.md.
"""

import os
import sys
import glob
import json
import shutil

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MODS_TASKS_DIR = os.path.join(ROOT_DIR, "tasks", "Translate_Mods")
COMPLETED_DIR = os.path.join(MODS_TASKS_DIR, "completed")
TECHNICAL_DIR = os.path.join(MODS_TASKS_DIR, "technical")

sys.path.insert(0, ROOT_DIR)
from tools.audit_real_gameplay_mods import mods_info, tier1_gameplay, tier2_ui, tier3_technical

os.makedirs(COMPLETED_DIR, exist_ok=True)
os.makedirs(TECHNICAL_DIR, exist_ok=True)

COMPLETED_NS = {
    'chimes', 'cozycafe', 'moreminecarts', 'nightlights', 
    'splendid_slimes', 'tanukidecor', 'twigs', 'unusualfishmod', 'vintagedelight',
    'cluttered', 'refurbished_furniture', 'dramaticdoors', 'simplehats', 'longwings',
    'automobility', 'pamhc2trees', 'paraglider', 'beachparty', 'functionalstorage'
}

# 1. Перемещение завершённых модов в completed/
print("📁 Перемещение завершённых модов в completed/...")
for ns in COMPLETED_NS:
    # Ищем любую папку содержащую _ns
    matches = glob.glob(os.path.join(MODS_TASKS_DIR, f"*_{ns}")) + [os.path.join(MODS_TASKS_DIR, f"translate_{ns}")]
    target_folder = os.path.join(COMPLETED_DIR, f"translate_{ns}")
    for old_folder in matches:
        if os.path.exists(old_folder) and os.path.abspath(old_folder) != os.path.abspath(target_folder):
            if os.path.exists(target_folder):
                shutil.rmtree(target_folder)
            shutil.move(old_folder, target_folder)
            print(f"  ✅ [completed] {ns} -> completed/translate_{ns}")

# 2. Перемещение технических модов (Tier 3) в technical/
print("\n⚙️ Перемещение технических модов (Tier 3) в technical/...")
for m in tier3_technical:
    ns = m['ns']
    if ns in COMPLETED_NS:
        continue
    matches = glob.glob(os.path.join(MODS_TASKS_DIR, f"*_{ns}")) + [os.path.join(MODS_TASKS_DIR, f"translate_{ns}")]
    target_folder = os.path.join(TECHNICAL_DIR, f"translate_{ns}")
    for old_folder in matches:
        if os.path.exists(old_folder) and os.path.abspath(old_folder) != os.path.abspath(target_folder):
            if os.path.exists(target_folder):
                shutil.rmtree(target_folder)
            shutil.move(old_folder, target_folder)
            print(f"  ⚙️ [technical] {ns} -> technical/translate_{ns}")

# 3. Формирование очереди строго как в GAMEPLAY_PRIORITY_AUDIT.md (по убыванию untrans)
tier1_sorted = sorted([m for m in tier1_gameplay if m['ns'] not in COMPLETED_NS], key=lambda x: x['untrans'], reverse=True)
tier2_sorted = sorted([m for m in tier2_ui if m['ns'] not in COMPLETED_NS], key=lambda x: x['untrans'], reverse=True)

all_active = [( 'TIER_1', m) for m in tier1_sorted] + [('TIER_2', m) for m in tier2_sorted]

print(f"\n🚀 Применение точной нумерации по GAMEPLAY_PRIORITY_AUDIT.md для {len(all_active)} активных модов...")

# Сначала собираем словарь текущих путей папок по namespace
current_folders = {}
for entry in os.listdir(MODS_TASKS_DIR):
    full_p = os.path.join(MODS_TASKS_DIR, entry)
    if os.path.isdir(full_p) and entry not in ['completed', 'technical', 'scripts']:
        # entry может быть '01_dramaticdoors', 'translate_cluttered', '06_cluttered', etc.
        parts = entry.split('_', 1)
        if len(parts) == 2 and parts[0].isdigit():
            ns = parts[1]
        elif entry.startswith('translate_'):
            ns = entry.replace('translate_', '')
        else:
            ns = entry
        current_folders[ns] = full_p

# Временное переименование во избежание конфликтов номеров
temp_map = {}
for ns, fpath in current_folders.items():
    temp_path = os.path.join(MODS_TASKS_DIR, f"__tmp_{ns}")
    if os.path.exists(fpath):
        shutil.move(fpath, temp_path)
        temp_map[ns] = temp_path

queue_rows = []
for idx, (tier, m) in enumerate(all_active, 1):
    ns = m['ns']
    prefix = f"{idx:02d}" if idx < 100 else f"{idx}"
    target_folder_name = f"{prefix}_{ns}"
    target_folder_path = os.path.join(MODS_TASKS_DIR, target_folder_name)
    
    if ns in temp_map and os.path.exists(temp_map[ns]):
        shutil.move(temp_map[ns], target_folder_path)
    else:
        # Папка создаётся если её не было
        scripts_dir = os.path.join(target_folder_path, "scripts")
        os.makedirs(scripts_dir, exist_ok=True)
        
    tier_label = "🎮 Контент" if tier == "TIER_1" else "🖥️ UI / Меню"
    queue_rows.append({
        'num': idx,
        'folder': target_folder_name,
        'ns': ns,
        'tier': tier_label,
        'untrans': m['untrans'],
        'total': m['total'],
        'items': m['active_items_cnt'],
        'blocked': m['blocked_items_cnt'],
        'jar': ', '.join(m['jars'])
    })
    print(f"  [{idx:02d}] {target_folder_name} (осталось {m['untrans']} строк, предметов в JEI: {m['active_items_cnt']})")

# 4. Обновление QUEUE.md
QUEUE_MD_PATH = os.path.join(MODS_TASKS_DIR, "QUEUE.md")
with open(QUEUE_MD_PATH, 'w', encoding='utf-8') as f:
    f.write("# Очередь локализации модов (Приоритет игрового процесса)\n\n")
    f.write(f"> **Всего активных модов в очереди:** {len(all_active)} | **Завершено:** {len(COMPLETED_NS)} | **Технических/библиотек:** {len(tier3_technical)}\n\n")
    f.write("Нумерация строго соответствует **[GAMEPLAY_PRIORITY_AUDIT.md](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/tasks/Translate_Mods/GAMEPLAY_PRIORITY_AUDIT.md)** (по объёму непереведённого контента для игрока: от крупнейших пропусков к единичным строкам).\n\n")
    f.write("## 📋 Активная очередь перевода\n\n")
    f.write("| № | Папка задачи | Namespace | Категория | Не переведено | Активных предметов в JEI | Отключено автором | JAR-файл |\n")
    f.write("| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :--- |\n")
    for r in queue_rows:
        f.write(f"| **{r['num']}** | [`{r['folder']}`](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/tasks/Translate_Mods/{r['folder']}) | `{r['ns']}` | {r['tier']} | **{r['untrans']}** ({round((r['total']-r['untrans'])/r['total']*100, 1)}%) | **{r['items']}** | {r['blocked']} | `{r['jar']}` |\n")

    f.write("\n---\n\n")
    f.write("## 🟢 Полностью переведённые моды (в папке `completed/`)\n\n")
    f.write("| Namespace | Папка | Статус |\n")
    f.write("| :--- | :--- | :---: |\n")
    for ns in sorted(COMPLETED_NS):
        f.write(f"| `{ns}` | [`completed/translate_{ns}`](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/tasks/Translate_Mods/completed/translate_{ns}) | 🟢 **100%** |\n")

print(f"\n🎉 Очередь успешно синхронизирована с GAMEPLAY_PRIORITY_AUDIT.md! Файл: {QUEUE_MD_PATH}")
