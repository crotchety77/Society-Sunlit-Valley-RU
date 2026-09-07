#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Утилита для инспекции языковых файлов модов из сборки Society: Sunlit Valley.
Ищет .jar в папке mods/, извлекает en_us.json и ru_ru.json, сопоставляет с kubejs/assets/ и translations/.
"""

import os
import sys
import glob
import json
import zipfile
import argparse

# Обеспечение корректного вывода UTF-8 в консоли Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')


MODS_DIR = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\mods"
KUBEJS_ASSETS_DIR = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets"
LOCAL_TRANSLATIONS_DIR = os.path.join(os.path.dirname(__file__), "..", "translations")

def find_jar_for_namespace(namespace):
    """Ищет jar-файл, содержащий assets/<namespace>/lang/."""
    jars = glob.glob(os.path.join(MODS_DIR, "*.jar"))
    target_prefix = f"assets/{namespace}/lang/"
    
    matches = []
    for jar_path in jars:
        try:
            with zipfile.ZipFile(jar_path, 'r') as z:
                for name in z.namelist():
                    if name.startswith(target_prefix):
                        matches.append(jar_path)
                        break
        except Exception:
            continue
    return matches

import re

def parse_relaxed_json(raw_text):
    """Парсит JSON, очищая от комментариев и висячих запятых."""
    try:
        return json.loads(raw_text)
    except Exception:
        # Убираем однострочные комментарии // ...
        cleaned = re.sub(r'//.*$', '', raw_text, flags=re.MULTILINE)
        # Убираем многострочные комментарии /* ... */
        cleaned = re.sub(r'/\*.*?\*/', '', cleaned, flags=re.DOTALL)
        # Убираем висячие запятые перед } и ]
        cleaned = re.sub(r',\s*([}\]])', r'\1', cleaned)
        return json.loads(cleaned)

def extract_lang_data(jar_path, namespace):
    """Извлекает en_us.json и встроенный ru_ru.json из jar."""
    en_us = {}
    ru_ru_jar = {}
    
    with zipfile.ZipFile(jar_path, 'r') as z:
        en_path = f"assets/{namespace}/lang/en_us.json"
        ru_path = f"assets/{namespace}/lang/ru_ru.json"
        
        if en_path in z.namelist():
            try:
                raw = z.read(en_path).decode('utf-8', errors='replace')
                en_us = parse_relaxed_json(raw)
            except Exception as e:
                print(f"[!] Ошибка чтения en_us.json: {e}")
                
        if ru_path in z.namelist():
            try:
                raw = z.read(ru_path).decode('utf-8', errors='replace')
                ru_ru_jar = parse_relaxed_json(raw)
            except Exception as e:
                print(f"[!] Ошибка чтения встроенного ru_ru.json: {e}")
                
    return en_us, ru_ru_jar


def get_kubejs_overrides(namespace):
    """Считывает переводы из kubejs/assets/<namespace>/lang/ru_ru.json."""
    game_path = os.path.join(KUBEJS_ASSETS_DIR, namespace, "lang", "ru_ru.json")
    if os.path.exists(game_path):
        try:
            with open(game_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            pass
    return {}

def inspect_mod(namespace, output_task=False):
    """Проводит аудит локализации мода."""
    # Если передан ID предмета вроде 'twigs:purple_silt_shingles' -> извлекаем namespace
    if ":" in namespace:
        namespace = namespace.split(":")[0]
        
    print(f"==================================================")
    print(f"🔍 Инспекция локализации мода: [{namespace}]")
    print(f"==================================================")
    
    jars = find_jar_for_namespace(namespace)
    if not jars:
        print(f"❌ Не найден .jar файл для пространства имён '{namespace}' в {MODS_DIR}")
        return
        
    jar_path = jars[0]
    print(f"📦 Найден JAR: {os.path.basename(jar_path)}")
    
    en_us, ru_jar = extract_lang_data(jar_path, namespace)
    kubejs_ru = get_kubejs_overrides(namespace)
    
    if not en_us:
        print(f"⚠️ В jar не найден assets/{namespace}/lang/en_us.json")
        return
        
    # Собираем актуальный русский перевод
    merged_ru = {}
    merged_ru.update(ru_jar)
    merged_ru.update(kubejs_ru)
    
    total_keys = len(en_us)
    translated_keys = {}
    untranslated_keys = {}
    
    for k, v_en in en_us.items():
        if k in merged_ru and merged_ru[k].strip() and merged_ru[k] != v_en:
            translated_keys[k] = {
                "en": v_en,
                "ru": merged_ru[k],
                "source": "kubejs" if k in kubejs_ru else "jar"
            }
        else:
            untranslated_keys[k] = v_en
            
    print(f"📊 Статистика ключей:")
    print(f"   ▪ Всего в en_us.json: {total_keys}")
    print(f"   ▪ Переведено на русский: {len(translated_keys)} ({len(translated_keys)/total_keys*100:.1f}%)")
    print(f"   ▪ Не переведено: {len(untranslated_keys)} ({len(untranslated_keys)/total_keys*100:.1f}%)")
    
    if untranslated_keys:
        print(f"\n--- Примеры непереведённых строк (первые 10) ---")
        for i, (k, v) in enumerate(list(untranslated_keys.items())[:10], 1):
            print(f" {i}. [{k}]: {v}")
            
    if output_task:
        task_dir = os.path.join(os.path.dirname(__file__), "..", "tasks", f"translate_{namespace}")
        os.makedirs(task_dir, exist_ok=True)
        task_file = os.path.join(task_dir, "new_translate.md")
        
        with open(task_file, 'w', encoding='utf-8') as f:
            f.write(f"# Локализация мода: {namespace}\n\n")
            f.write(f"**JAR-файл:** `{os.path.basename(jar_path)}`\n")
            f.write(f"**Всего ключей:** {total_keys} | **Не переведено:** {len(untranslated_keys)}\n\n")
            f.write(f"## 1. Непереведённые ключи\n\n")
            f.write(f"```json\n")
            untranslated_json = {k: f"TODO: {v}" for k, v in untranslated_keys.items()}
            f.write(json.dumps(untranslated_json, ensure_ascii=False, indent=2))
            f.write(f"\n```\n\n")
            
            f.write(f"## 2. Существующие переводы (для контекста)\n\n")
            f.write(f"```json\n")
            existing_json = {k: item["ru"] for k, item in translated_keys.items()}
            f.write(json.dumps(existing_json, ensure_ascii=False, indent=2))
            f.write(f"\n```\n")
            
        print(f"\n✅ Создан файл задачи: {task_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Аудит и извлечение языковых строк мода.")
    parser.add_argument("namespace", help="Namespace мода (напр. 'twigs', 'whimsy_deco', 'cozycafe') или ID предмета")
    parser.add_argument("--create-task", action="store_true", help="Сгенерировать файл задачи new_translate.md в tasks/")
    args = parser.parse_args()
    
    inspect_mod(args.namespace, output_task=args.create_task)
