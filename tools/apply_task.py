#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
Универсальный раннер применения и синхронизации задач (tools/apply_task.py).
Считывает строки и JSON из tasks/<task_name>/new_translate(.md), обновляет файлы translations/,
запускает синхронизацию с игрой и верифицирует физические файлы в D:\ModrinthApp\...
"""

import os
import sys
import json
import re
import subprocess
import argparse

# Обеспечение корректного вывода UTF-8 в консоли Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TASKS_DIR = os.path.join(ROOT_DIR, "tasks")
TRANSLATIONS_DIR = os.path.join(ROOT_DIR, "translations")
GAME_ASSETS_DIR = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets"

def find_task_file(task_name):
    """Ищет файл new_translate.md или new_translate в папке задачи."""
    candidates = [
        os.path.join(TASKS_DIR, task_name),
        os.path.join(TASKS_DIR, "Translate_Mods", task_name),
        os.path.join(TASKS_DIR, "Translate_Mods", "completed", task_name),
        task_name
    ]
    task_dir = None
    for c in candidates:
        if os.path.isdir(c):
            task_dir = c
            break
            
    if not task_dir:
        print(f"❌ Папка задачи не найдена: {task_name}")
        return None, None
            
    for fname in ["new_translate.md", "new_translate", "translate.json"]:
        fpath = os.path.join(task_dir, fname)
        if os.path.isfile(fpath):
            return task_dir, fpath
            
    print(f"❌ В папке {task_dir} не найден файл new_translate.md / new_translate")
    return task_dir, None

def extract_json_blocks_from_markdown(content):
    """Извлекает JSON объекты из markdown текста."""
    json_blocks = []
    # Поиск блоков ```json ... ```
    pattern = r'```(?:json)?\s*([\s\S]*?)\s*```'
    matches = re.findall(pattern, content)
    for m in matches:
        try:
            # Убираем комментарии и висячие запятые
            cleaned = re.sub(r'//.*$', '', m, flags=re.MULTILINE)
            cleaned = re.sub(r',\s*([}\]])', r'\1', cleaned)
            data = json.loads(cleaned)
            if isinstance(data, dict):
                json_blocks.append(data)
        except Exception:
            continue
            
    # Если блоков с разметкой нет, пробуем распарсить весь текст как JSON
    if not json_blocks:
        try:
            data = json.loads(content)
            if isinstance(data, dict):
                json_blocks.append(data)
        except Exception:
            pass
            
    return json_blocks

def route_key_to_file(key, default_mod_ns=None):
    """Определяет целевой файл translations/ для конкретного ключа."""
    # 1. FTB Quests
    if key.startswith("ftbquests.") or key.startswith("ftbquestlocalizer."):
        return "ftbquests", os.path.join(TRANSLATIONS_DIR, "ftbquests", "ru_ru.json")
        
    # 2. Society Core
    if key.startswith("society.") or key.startswith("item.society.") or key.startswith("block.society.") or key.startswith("tooltip.society."):
        return "society", os.path.join(TRANSLATIONS_DIR, "society", "ru_ru.json")
        
    # 3. Skills
    if key.startswith("society_skills.") or key.startswith("skills."):
        return "society_skills", os.path.join(TRANSLATIONS_DIR, "skills", "ru_ru.json")
        
    # 4. Tips
    if key.startswith("society_tips."):
        return "society_tips", os.path.join(TRANSLATIONS_DIR, "tips", "society_tips_ru_ru.json")
        
    # 5. Blueprints / Buildings
    if key.startswith("portable_blueprints."):
        return "portable_blueprints", os.path.join(TRANSLATIONS_DIR, "buildings", "portable_blueprints_ru_ru.json")
        
    # 6. External Mods (e.g. block.twigs.twig, item.brewery.beer, twigs.item_group)
    parts = key.split(".")
    mod_namespace = None
    if len(parts) >= 2:
        if parts[0] in ["block", "item", "entity", "itemGroup", "tooltip", "container", "upgrade", "emi", "jei", "subtitles", "filterCategory", "death", "stat", "frame", "engine", "wheel", "attachment"]:
            mod_namespace = parts[1].lower()
        elif re.match(r'^[a-z0-9_.-]+$', parts[0]):
            mod_namespace = parts[0].lower()
            
    if not mod_namespace or not re.match(r'^[a-z0-9_.-]+$', mod_namespace):
        mod_namespace = default_mod_ns if default_mod_ns else "misc"
        
    mod_namespace = mod_namespace.lower()
    return mod_namespace, os.path.join(TRANSLATIONS_DIR, "mods", f"{mod_namespace}.json")

def apply_task(task_name):
    """Основной процесс применения задачи."""
    print(f"==================================================")
    print(f"🚀 Применение задачи: [{task_name}]")
    print(f"==================================================")
    
    task_dir, task_file = find_task_file(task_name)
    if not task_file:
        return False
        
    with open(task_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    json_blocks = extract_json_blocks_from_markdown(content)
    if not json_blocks:
        print(f"⚠️ Не удалось найти JSON блок с ключами в {task_file}")
        return False
        
    # Объединяем все найденные блоки (приоритет у последних)
    all_keys = {}
    for block in json_blocks:
        all_keys.update(block)
        
    print(f"📝 Извлечено ключей для применения: {len(all_keys)}")
    
    # Определяем namespace задачи по умолчанию
    default_mod_ns = re.sub(r'^\d+_', '', task_name).replace('translate_', '').lower()
    
    # Группируем ключи по целевым файлам
    grouped = {}
    for k, v in all_keys.items():
        # Пропускаем плейсхолдеры TODO
        if isinstance(v, str) and v.startswith("TODO:"):
            continue
        ns, target_file = route_key_to_file(k, default_mod_ns)
        if target_file not in grouped:
            grouped[target_file] = (ns, {})
        grouped[target_file][1][k] = v
        
    if not grouped:
        print(f"⚠️ Нет готовых ключей для записи (все строки помечены как TODO).")
        return False
        
    # Записываем изменения в файлы translations/
    for target_file, (ns, keys_dict) in grouped.items():
        os.makedirs(os.path.dirname(target_file), exist_ok=True)
        current_data = {}
        if os.path.exists(target_file):
            try:
                with open(target_file, 'r', encoding='utf-8') as f:
                    current_data = json.load(f)
            except Exception:
                pass
        current_data.update(keys_dict)
        with open(target_file, 'w', encoding='utf-8') as f:
            json.dump(current_data, f, ensure_ascii=False, indent=2)
        print(f"✅ Обновлён [{os.path.basename(target_file)}] (+{len(keys_dict)} ключей)")
        
    # Запускаем общую синхронизацию
    print(f"\n🔄 Запуск синхронизации с игрой...")
    res = subprocess.run(["node", "sync_all_to_game.js"], cwd=ROOT_DIR, capture_output=True, text=True, encoding='utf-8', errors='replace')
    if res.returncode != 0:
        print(f"❌ Ошибка синхронизации: {res.stderr}")
        return False
        
    # Прямая физическая верификация
    print(f"\n🔎 ПРЯМАЯ ВЕРИФИКАЦИЯ ФАЙЛОВ ИГРЫ:")
    sample_count = 0
    for target_file, (ns, keys_dict) in grouped.items():
        # Определяем путь в kubejs/assets/
        if ns == "ftbquests":
            game_json = os.path.join(GAME_ASSETS_DIR, "ftbquestlocalizer", "lang", "ru_ru.json")
        elif ns == "society_skills":
            game_json = os.path.join(GAME_ASSETS_DIR, "society_skills", "lang", "ru_ru.json")
        elif ns == "society_tips":
            game_json = os.path.join(GAME_ASSETS_DIR, "society_tips", "lang", "ru_ru.json")
        elif ns == "portable_blueprints":
            game_json = os.path.join(GAME_ASSETS_DIR, "portable_blueprints", "lang", "ru_ru.json")
        else:
            game_json = os.path.join(GAME_ASSETS_DIR, ns, "lang", "ru_ru.json")
            
        if os.path.exists(game_json):
            try:
                with open(game_json, 'r', encoding='utf-8') as f:
                    game_data = json.load(f)
                for k, expected_v in list(keys_dict.items())[:3]:
                    actual_v = game_data.get(k)
                    status = "✅" if actual_v == expected_v else "❌"
                    print(f"   {status} [{ns}] {k} -> \"{actual_v}\"")
                    sample_count += 1
            except Exception as e:
                print(f"   ❌ Ошибка чтения {game_json}: {e}")
                
    print(f"\n==================================================")
    print(f"🎉 ЗАДАЧА [{task_name}] УСПЕШНО ПРИМЕНЕНА И СИНХРОНИЗИРОВАНА!")
    print(f"👉 В игре нажмите F3 + T (для FTB Quests: F3 + T, затем /ftbquests reload)")
    print(f"==================================================")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Применение задачи перевода.")
    parser.add_argument("task_name", help="Имя папки задачи в tasks/ (например, 'translate_twigs', 'FTB_QUESTS_4_1_4')")
    args = parser.parse_args()
    
    apply_task(args.task_name)
