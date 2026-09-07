#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import glob
import json
import zipfile
import re
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MODS_DIR = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\mods"
KUBEJS_ASSETS_DIR = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets"
LOCAL_TRANSLATIONS_DIR = os.path.join(ROOT_DIR, "translations", "mods")
TASKS_ROOT = os.path.join(ROOT_DIR, "tasks", "Translate_Mods")

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

results = {}
jars = glob.glob(os.path.join(MODS_DIR, '*.jar'))

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
                        ru_path = f'assets/{ns}/lang/ru_ru.json'
                        ru_jar = {}
                        if ru_path in names:
                            try:
                                ru_raw = z.read(ru_path).decode('utf-8', errors='replace')
                                ru_jar = parse_relaxed_json(ru_raw)
                            except Exception: pass
                        kubejs_ru = {}
                        k_path = os.path.join(KUBEJS_ASSETS_DIR, ns, 'lang', 'ru_ru.json')
                        if os.path.exists(k_path):
                            try:
                                kubejs_ru = json.load(open(k_path, 'r', encoding='utf-8'))
                            except Exception: pass
                        local_mod_ru = {}
                        l_path = os.path.join(LOCAL_TRANSLATIONS_DIR, f'{ns}.json')
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
                        items_cnt = sum(1 for k in en_json if k.startswith('item.'))
                        blocks_cnt = sum(1 for k in en_json if k.startswith('block.'))
                        gui_cnt = sum(1 for k in en_json if k.startswith(('gui.', 'container.', 'screen.', 'menu.')))
                        tooltips_cnt = sum(1 for k in en_json if k.startswith(('tooltip.', 'desc.')))
                        
                        for k, v in en_json.items():
                            if k in merged_ru and isinstance(merged_ru[k], str) and merged_ru[k].strip() and merged_ru[k] != v:
                                translated += 1
                        pct = (translated / total * 100) if total > 0 else 0
                        untrans = total - translated
                        if untrans > 0:
                            task_folder = os.path.join(TASKS_ROOT, f'translate_{ns}')
                            has_task = os.path.exists(task_folder)
                            is_content = (items_cnt + blocks_cnt > 0) or (gui_cnt > 0 and tooltips_cnt > 0)
                            results[ns] = {
                                'ns': ns,
                                'total': total,
                                'untrans': untrans,
                                'pct': round(pct, 1),
                                'items': items_cnt,
                                'blocks': blocks_cnt,
                                'gui': gui_cnt,
                                'tooltips': tooltips_cnt,
                                'is_content': is_content,
                                'has_task': has_task,
                                'jar': os.path.basename(jar_path)
                            }
    except Exception as e:
        pass

print(f"Всего модов с непереведёнными строками: {len(results)}")
print("\n--- Игровые моды БЕЗ папки задачи ---")
no_task_content = [v for v in results.values() if not v['has_task'] and v['is_content']]
for v in sorted(no_task_content, key=lambda x: x['untrans'], reverse=True):
    print(f"  [{v['ns']}]: {v['untrans']}/{v['total']} не переведено ({v['pct']}%) [items: {v['items']}, blocks: {v['blocks']}, gui: {v['gui']}] -> {v['jar']}")

print("\n--- Технические моды БЕЗ папки задачи ---")
no_task_tech = [v for v in results.values() if not v['has_task'] and not v['is_content']]
for v in sorted(no_task_tech, key=lambda x: x['untrans'], reverse=True):
    print(f"  [{v['ns']}]: {v['untrans']}/{v['total']} не переведено ({v['pct']}%) -> {v['jar']}")
