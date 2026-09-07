#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tasks/Translate_Mods/scripts/audit_mods.py
Скрипт аудита состояния локализации всех модов сборки Society: Sunlit Valley.
Сканирует JAR-файлы в mods/, сопоставляет с kubejs/assets/ и translations/mods/,
классифицирует моды на игровые (видимые в JEI/мире) и технические,
и генерирует структурированный audit.md.
"""

import os
import sys
import glob
import json
import zipfile
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

MODS_DIR = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\mods"
KUBEJS_ASSETS_DIR = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets"
LOCAL_TRANSLATIONS_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "..", "translations", "mods")
TASK_ROOT_DIR = os.path.join(os.path.dirname(__file__), "..")
AUDIT_MD_PATH = os.path.join(TASK_ROOT_DIR, "audit.md")

def parse_relaxed_json(raw_text):
    try:
        return json.loads(raw_text)
    except Exception:
        cleaned = re.sub(r'//.*$', '', raw_text, flags=re.MULTILINE)
        cleaned = re.sub(r'/\*.*?\*/', '', cleaned, flags=re.DOTALL)
        cleaned = re.sub(r',\s*([}\]])', r'\1', cleaned)
        try:
            return json.loads(cleaned)
        except Exception:
            return {}

def run_audit():
    results = {}
    jars = glob.glob(os.path.join(MODS_DIR, "*.jar"))

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
                            
                            ru_path = f"assets/{ns}/lang/ru_ru.json"
                            ru_jar = {}
                            if ru_path in names:
                                try:
                                    ru_raw = z.read(ru_path).decode('utf-8', errors='replace')
                                    ru_jar = parse_relaxed_json(ru_raw)
                                except Exception:
                                    pass
                            
                            kubejs_ru = {}
                            k_path = os.path.join(KUBEJS_ASSETS_DIR, ns, "lang", "ru_ru.json")
                            if os.path.exists(k_path):
                                try:
                                    with open(k_path, 'r', encoding='utf-8') as f:
                                        kubejs_ru = json.load(f)
                                except Exception:
                                    pass
                                    
                            local_mod_ru = {}
                            l_path = os.path.join(LOCAL_TRANSLATIONS_DIR, f"{ns}.json")
                            if os.path.exists(l_path):
                                try:
                                    with open(l_path, 'r', encoding='utf-8') as f:
                                        local_mod_ru = json.load(f)
                                except Exception:
                                    pass

                            merged_ru = {}
                            if isinstance(ru_jar, dict): merged_ru.update(ru_jar)
                            if isinstance(kubejs_ru, dict): merged_ru.update(kubejs_ru)
                            if isinstance(local_mod_ru, dict): merged_ru.update(local_mod_ru)

                            total = len(en_json)
                            translated = 0
                            
                            items_cnt = sum(1 for k in en_json if k.startswith("item."))
                            blocks_cnt = sum(1 for k in en_json if k.startswith("block."))
                            entities_cnt = sum(1 for k in en_json if k.startswith("entity."))
                            gui_cnt = sum(1 for k in en_json if k.startswith(("gui.", "container.", "screen.", "menu.")))
                            tooltips_cnt = sum(1 for k in en_json if k.startswith(("tooltip.", "tooltip_always.", "desc.")))
                            
                            player_visible_cnt = sum(1 for k in en_json if k.startswith((
                                "item.", "block.", "entity.", "gui.", "container.", "screen.", 
                                "tooltip.", "category.", "subtitles.", "effect.", "enchantment.", "stat."
                            )))

                            for k, v in en_json.items():
                                if k in local_mod_ru and isinstance(local_mod_ru[k], str) and local_mod_ru[k].strip():
                                    translated += 1
                                elif k in kubejs_ru and isinstance(kubejs_ru[k], str) and kubejs_ru[k].strip():
                                    translated += 1
                                elif k in ru_jar and isinstance(ru_jar[k], str) and ru_jar[k].strip() and ru_jar[k] != v:
                                    translated += 1
                            
                            pct = (translated / total * 100) if total > 0 else 0
                            
                            # Контентным считается мод с предметами, блоками или игровым GUI/тултипами
                            is_content = (items_cnt + blocks_cnt + entities_cnt > 0) or (gui_cnt > 0 and tooltips_cnt > 0)
                            
                            results[ns] = {
                                'namespace': ns,
                                'jar': os.path.basename(jar_path),
                                'total': total,
                                'translated': translated,
                                'untranslated': total - translated,
                                'pct': round(pct, 1),
                                'items_cnt': items_cnt,
                                'blocks_cnt': blocks_cnt,
                                'entities_cnt': entities_cnt,
                                'gui_cnt': gui_cnt,
                                'tooltips_cnt': tooltips_cnt,
                                'player_visible_cnt': player_visible_cnt,
                                'is_content': is_content
                            }
        except Exception:
            continue

    items = list(results.values())

    # Фильтрация по типам
    gameplay_mods = [x for x in items if x['is_content'] and x['untranslated'] > 0 and x['pct'] < 100]
    tech_mods = [x for x in items if not x['is_content'] and x['untranslated'] > 0 and x['pct'] < 100]
    full_trans = [x for x in items if x['untranslated'] == 0 or x['pct'] >= 100]

    # Генерация audit.md
    with open(AUDIT_MD_PATH, 'w', encoding='utf-8') as f:
        f.write("# Аудит локализации модов сборки Society: Sunlit Valley\n\n")
        f.write(f"> **Всего модов:** {len(items)} | **Игровых модов (JEI/UI/мир) с пропусками:** {len(gameplay_mods)} | **Технических/библиотек:** {len(tech_mods)} | **Полностью переведено (100%):** {len(full_trans)}\n\n")
        
        f.write("## 🎮 Раздел 1: Игровые моды (Предметы в JEI, Блоки, UI интерфейсы, Тултипы, Еда, Декор)\n")
        f.write("*Моды, с которыми игрок непосредственно контактирует: видит в инвентаре/JEI, открывает интерфейсы (GUI), читает подсказки или строит.*\n\n")
        f.write("| Namespace | Всего строк | Состав (Предметы / Блоки / GUI / Тултипы) | Прогресс | Осталось перевести | JAR-файл |\n")
        f.write("| :--- | :---: | :--- | :---: | :---: | :--- |\n")
        for x in sorted(gameplay_mods, key=lambda k: (k['pct'] < 20, k['total']), reverse=True):
            status = "🔴" if x['pct'] < 20 else ("🟡" if x['pct'] < 85 else "🟢")
            comp_parts = []
            if x['items_cnt']: comp_parts.append(f"{x['items_cnt']} предм.")
            if x['blocks_cnt']: comp_parts.append(f"{x['blocks_cnt']} блок.")
            if x['gui_cnt']: comp_parts.append(f"{x['gui_cnt']} GUI/меню")
            if x['tooltips_cnt']: comp_parts.append(f"{x['tooltips_cnt']} тултип.")
            comp_str = ", ".join(comp_parts) if comp_parts else f"{x['player_visible_cnt']} игр. ключей"
            f.write(f"| `{x['namespace']}` | **{x['total']}** | {comp_str} | {status} **{x['pct']}%** | **{x['untranslated']}** ({x['translated']}/{x['total']}) | `{x['jar']}` |\n")

        f.write("\n---\n\n")
        f.write("## ⚙️ Раздел 2: Технические моды, API и системные библиотеки\n")
        f.write("*Внутренние библиотеки, меню глубоких настроек, скрытые атрибуты движка (в JEI физических предметов нет).*\n\n")
        f.write("| Namespace | Всего строк | Прогресс | Переведено | Осталось | JAR-файл |\n")
        f.write("| :--- | :---: | :---: | :---: | :---: | :--- |\n")
        for x in sorted(tech_mods, key=lambda k: k['untranslated'], reverse=True):
            f.write(f"| `{x['namespace']}` | {x['total']} | **{x['pct']}%** | {x['translated']}/{x['total']} | **{x['untranslated']}** | `{x['jar']}` |\n")

        f.write("\n---\n\n")
        f.write("## 🔵 Раздел 3: Полностью переведённые (100%)\n\n")
        f.write("| Namespace | Ключей | JAR-файл |\n")
        f.write("| :--- | :---: | :--- |\n")
        for x in sorted(full_trans, key=lambda k: k['total'], reverse=True):
            f.write(f"| `{x['namespace']}` | {x['total']} | `{x['jar']}` |\n")

    print(f"✅ Аудит успешно выполнен! Файл: {AUDIT_MD_PATH}")

if __name__ == "__main__":
    run_audit()

