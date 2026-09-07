#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import glob
import json
import zipfile
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MODS_DIR = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\mods"
KUBEJS_DIR = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs"
REMOVED_ITEMS_JS = os.path.join(KUBEJS_DIR, "startup_scripts", "globalRemovedItems.js")

sys.path.insert(0, ROOT_DIR)
from tools.analyze_untranslated_mods import parse_relaxed_json

# Считываем список удалённых автором предметов
removed_items_set = set()
if os.path.exists(REMOVED_ITEMS_JS):
    with open(REMOVED_ITEMS_JS, 'r', encoding='utf-8') as f:
        content = f.read()
    # Извлекаем все строки в кавычках вида "mod:item"
    matches = re.findall(r'["\']([a-zA-Z0-9_]+:[a-zA-Z0-9_]+)["\']', content)
    removed_items_set = set(matches)

print(f"📦 Всего удалённых предметов в сборке автором: {len(removed_items_set)}")

# Сканируем JAR файлы
jars = glob.glob(os.path.join(MODS_DIR, '*.jar'))
mods_info = {}

for jar_path in jars:
    try:
        with zipfile.ZipFile(jar_path, 'r') as z:
            names = z.namelist()
            for n in names:
                if n.startswith('assets/') and n.endswith('/lang/en_us.json'):
                    parts = n.split('/')
                    if len(parts) == 4:
                        ns = parts[1]
                        if ns in ['minecraft', 'realms']:
                            continue
                        try:
                            en_raw = z.read(n).decode('utf-8', errors='replace')
                            en_json = parse_relaxed_json(en_raw)
                        except Exception:
                            en_json = {}
                        if not en_json or not isinstance(en_json, dict):
                            continue
                            
                        # Считываем ru_ru
                        ru_jar = {}
                        ru_path = f"assets/{ns}/lang/ru_ru.json"
                        if ru_path in names:
                            try:
                                ru_raw = z.read(ru_path).decode('utf-8', errors='replace')
                                ru_jar = parse_relaxed_json(ru_raw)
                            except Exception: pass
                            
                        kubejs_ru = {}
                        k_path = os.path.join(KUBEJS_DIR, "assets", ns, "lang", "ru_ru.json")
                        if os.path.exists(k_path):
                            try:
                                kubejs_ru = json.load(open(k_path, 'r', encoding='utf-8'))
                            except Exception: pass
                            
                        local_mod_ru = {}
                        l_path = os.path.join(ROOT_DIR, "translations", "mods", f"{ns}.json")
                        if os.path.exists(l_path):
                            try:
                                local_mod_ru = json.load(open(l_path, 'r', encoding='utf-8'))
                            except Exception: pass
                            
                        merged_ru = {}
                        if isinstance(ru_jar, dict): merged_ru.update(ru_jar)
                        if isinstance(kubejs_ru, dict): merged_ru.update(kubejs_ru)
                        if isinstance(local_mod_ru, dict): merged_ru.update(local_mod_ru)

                        total = len(en_json)
                        translated = 0
                        untrans_keys = []
                        
                        items = []
                        blocks = []
                        gui = []
                        tooltips = []
                        attributes = []
                        other = []
                        
                        for k, v in en_json.items():
                            is_trans = False
                            if k in local_mod_ru and isinstance(local_mod_ru[k], str) and local_mod_ru[k].strip():
                                is_trans = True
                            elif k in kubejs_ru and isinstance(kubejs_ru[k], str) and kubejs_ru[k].strip():
                                is_trans = True
                            elif k in ru_jar and isinstance(ru_jar[k], str) and ru_jar[k].strip() and ru_jar[k] != v:
                                is_trans = True

                            if is_trans:
                                translated += 1
                            else:
                                untrans_keys.append((k, v))
                                
                            if k.startswith("item."):
                                items.append(k)
                            elif k.startswith("block."):
                                blocks.append(k)
                            elif k.startswith(("gui.", "container.", "screen.", "menu.")):
                                gui.append(k)
                            elif k.startswith(("tooltip.", "desc.")):
                                tooltips.append(k)
                            elif k.startswith("attribute."):
                                attributes.append(k)
                            else:
                                other.append(k)
                                
                        # Проверяем, сколько предметов заблокировано
                        blocked_items_cnt = 0
                        for k in items + blocks:
                            # ключ item.mod.name -> mod:name
                            parts_k = k.split('.')
                            if len(parts_k) >= 3:
                                item_id = f"{parts_k[1]}:{parts_k[2]}"
                                if item_id in removed_items_set:
                                    blocked_items_cnt += 1
                                    
                        active_items_cnt = len(items) + len(blocks) - blocked_items_cnt
                        
                        untrans_cnt = total - translated
                        pct = (translated / total * 100) if total > 0 else 0
                        
                        if ns not in mods_info:
                            mods_info[ns] = {
                                'ns': ns,
                                'jars': [os.path.basename(jar_path)],
                                'total': total,
                                'translated': translated,
                                'untrans': untrans_cnt,
                                'pct': round(pct, 1),
                                'items_cnt': len(items),
                                'blocks_cnt': len(blocks),
                                'active_items_cnt': active_items_cnt,
                                'blocked_items_cnt': blocked_items_cnt,
                                'gui_cnt': len(gui),
                                'tooltips_cnt': len(tooltips),
                                'attributes_cnt': len(attributes),
                                'untrans_keys': untrans_keys
                            }
                        else:
                            if os.path.basename(jar_path) not in mods_info[ns]['jars']:
                                mods_info[ns]['jars'].append(os.path.basename(jar_path))
    except Exception:
        pass

# Классификация
tier1_gameplay = [] # Активные предметы, блоки, декор, еда
tier2_ui = []       # UI моды, миникарты, подсказки, настройки
tier3_technical = [] # Чисто атрибуты, API, бэкенд библиотеки

for ns, m in mods_info.items():
    if m['untrans'] == 0:
        continue
        
    if m['active_items_cnt'] > 0:
        tier1_gameplay.append(m)
    elif m['gui_cnt'] > 0 or m['tooltips_cnt'] > 0:
        tier2_ui.append(m)
    else:
        tier3_technical.append(m)

print(f"\n=======================================================")
print(f"📊 АУДИТ РЕАЛЬНОГО ВЛИЯНИЯ НА ИГРОКА (Gamer Experience)")
print(f"=======================================================")
print(f"🎮 ТИР 1: Игровые моды (Предметы в JEI, Блоки, Декор, Еда, Оружие): {len(tier1_gameplay)}")
print(f"🖥️ ТИР 2: Интерфейс и UI (Меню, JEI категории, Тултипы, Хоткеи):   {len(tier2_ui)}")
print(f"⚙️ ТИР 3: Технические библиотеки / API / Неиспользуемые атрибуты: {len(tier3_technical)}")

# Запись подробного отчета
REPORT_PATH = os.path.join(ROOT_DIR, "tasks", "Translate_Mods", "GAMEPLAY_PRIORITY_AUDIT.md")
with open(REPORT_PATH, 'w', encoding='utf-8') as f:
    f.write("# Приоритетный аудит локализации модов для игрока\n\n")
    f.write("Данный аудит учитывает реальное присутствие предметов в игре и в JEI, исключая отключённые автором предметы (`globalRemovedItems.js`) и скрытые технические атрибуты.\n\n")
    
    f.write("## 🎮 ТИР 1: Реальный игровой контент (То, что игрок видит в мире, инвентаре и JEI)\n")
    f.write("> **Приоритет: КРИТИЧЕСКИ ВЫСОКИЙ**. Перевод этих модов напрямую формирует впечатления от игры.\n\n")
    f.write("| Namespace | Не переведено | Всего строк | Активных предметов в JEI | Отключено автором | JAR-файл |\n")
    f.write("| :--- | :---: | :---: | :---: | :---: | :--- |\n")
    for m in sorted(tier1_gameplay, key=lambda x: x['untrans'], reverse=True):
        f.write(f"| `{m['ns']}` | **{m['untrans']}** ({m['pct']}%) | {m['total']} | **{m['active_items_cnt']}** предм./блок. | {m['blocked_items_cnt']} откл. | `{', '.join(m['jars'])}` |\n")
        
    f.write("\n---\n\n")
    f.write("## 🖥️ ТИР 2: Интерфейс, UI, Меню и Всплывающие подсказки\n")
    f.write("> **Приоритет: СРЕДНИЙ**. Окна настроек, интерфейсы интеграций (JEI, Jade, JourneyMap, Camera).\n\n")
    f.write("| Namespace | Не переведено | Всего строк | Состав (GUI / Тултипы) | JAR-файл |\n")
    f.write("| :--- | :---: | :---: | :--- | :--- |\n")
    for m in sorted(tier2_ui, key=lambda x: x['untrans'], reverse=True):
        f.write(f"| `{m['ns']}` | **{m['untrans']}** ({m['pct']}%) | {m['total']} | {m['gui_cnt']} GUI, {m['tooltips_cnt']} тултип. | `{', '.join(m['jars'])}` |\n")
        
    f.write("\n---\n\n")
    f.write("## ⚙️ ТИР 3: Технические моды, API и неиспользуемые атрибуты\n")
    f.write("> **Приоритет: НИЗКИЙ / НЕ ТРЕБУЕТСЯ**. В JEI предметов не имеют, игроку напрямую не видны (стабы других модов, движок).\n\n")
    f.write("| Namespace | Не переведено | Всего строк | Тип данных | JAR-файл |\n")
    f.write("| :--- | :---: | :---: | :--- | :--- |\n")
    for m in sorted(tier3_technical, key=lambda x: x['untrans'], reverse=True):
        f.write(f"| `{m['ns']}` | **{m['untrans']}** ({m['pct']}%) | {m['total']} | {m['attributes_cnt']} атрибутов, {len(m['untrans_keys'])} техн. строк | `{', '.join(m['jars'])}` |\n")

print(f"✅ Отчёт сформирован: {REPORT_PATH}")
