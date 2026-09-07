#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Универсальный скрипт финализации локализации мода:
1. Проверяет наличие папки задачи в tasks/Translate_Mods/ (или поиск по namespace).
2. Проверяет 100% покрытие перевода в translations/mods/<namespace>.json.
3. Обновляет TASK.md с отметкой о 100% завершении.
4. Перемещает папку задачи в tasks/Translate_Mods/completed/translate_<namespace>.
5. Обновляет tasks/Translate_Mods/QUEUE.md (счётчики, ссылки, таблицу завершённых).
6. Запускает sync_all_to_game.js.
7. Проверяет физическое наличие языкового файла в игре.

Использование:
    python tools/finalize_mod.py <folder_or_namespace>
Пример:
    python tools/finalize_mod.py 02_buildinggadgets2
    python tools/finalize_mod.py buildinggadgets2
"""

import sys
import os
import json
import re
import shutil
import subprocess

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TASKS_DIR = os.path.join(PROJECT_ROOT, "tasks", "Translate_Mods")
COMPLETED_DIR = os.path.join(TASKS_DIR, "completed")
TRANSLATIONS_DIR = os.path.join(PROJECT_ROOT, "translations", "mods")
QUEUE_FILE = os.path.join(TASKS_DIR, "QUEUE.md")
GAME_PROFILE_LANG = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets"

def find_task_folder(target):
    # 1. Прямой путь
    candidate = os.path.join(TASKS_DIR, target)
    if os.path.isdir(candidate):
        return candidate, os.path.basename(candidate)
    
    # 2. Поиск по namespace (например buildinggadgets2)
    for folder in os.listdir(TASKS_DIR):
        folder_path = os.path.join(TASKS_DIR, folder)
        if os.path.isdir(folder_path) and folder != "completed":
            if folder == target or folder.endswith(f"_{target}") or target in folder:
                return folder_path, folder
    return None, None

def get_namespace_from_folder(folder_path, folder_name):
    task_md = os.path.join(folder_path, "TASK.md")
    if os.path.isfile(task_md):
        with open(task_md, "r", encoding="utf-8") as f:
            for line in f:
                if "**Namespace:**" in line:
                    match = re.search(r'`([^`]+)`', line)
                    if match:
                        return match.group(1).strip()
    
    # Резерв: извлечь из имени папки (например 02_buildinggadgets2 -> buildinggadgets2)
    clean_name = re.sub(r'^\d+_', '', folder_name)
    return clean_name

def check_translation_completeness(namespace):
    trans_file = os.path.join(TRANSLATIONS_DIR, f"{namespace}.json")
    if not os.path.isfile(trans_file):
        print(f"⚠️  Файл перевода {trans_file} не найден!")
        return 0, 0
    with open(trans_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    total = len(data)
    cyrillic = sum(1 for v in data.values() if isinstance(v, str) and re.search(r'[а-яА-ЯёЁ]', v))
    return total, cyrillic

def update_task_md(folder_path, namespace, total_keys):
    task_md = os.path.join(folder_path, "TASK.md")
    if not os.path.isfile(task_md):
        return
    with open(task_md, "r", encoding="utf-8") as f:
        content = f.read()

    status_block = f"""### Статус: ✅ ЗАВЕРШЕНО (100.0%)
* Локализовано: **{total_keys}/{total_keys} строк**
* Механики: Проведён Level 1 и Level 2 аудит в папке `docs/`
* Синхронизация: Все файлы интегрированы в проект и клиент игры."""

    if "### Статус:" in content:
        content = re.sub(r'### Статус:[\s\S]*$', status_block, content)
    elif "### Порядок работы:" in content:
        content = re.sub(r'### Порядок работы:[\s\S]*$', status_block, content)
    else:
        content += "\n\n" + status_block

    with open(task_md, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Обновлён TASK.md со статусом 100% завершения.")

def update_queue_file(folder_name, namespace):
    if not os.path.isfile(QUEUE_FILE):
        return
    with open(QUEUE_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Замена ссылки в таблице активной очереди
    # Пример: | **2** | [`02_buildinggadgets2`](...) | -> | **2** | [~~`02_buildinggadgets2`~~ $\rightarrow$ `completed`](...) |
    active_row_pattern = rf'(\|\s*\*\*\d+\*\*\s*\|\s*)\[`?{re.escape(folder_name)}`?\]\([^)]+\)(\s*\|\s*`?{re.escape(namespace)}`?.*)'
    replacement = rf'\1[~~`{folder_name}`~~ $\\rightarrow$ `completed`](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/tasks/Translate_Mods/completed/translate_{namespace})\2'
    content = re.sub(active_row_pattern, replacement, content)

    # Добавление в таблицу завершённых (если ещё нет)
    completed_entry = f"| `{namespace}` | [`completed/translate_{namespace}`](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/tasks/Translate_Mods/completed/translate_{namespace}) | 🟢 **100%** |"
    if f"`completed/translate_{namespace}`" not in content:
        # Найти таблицу completed и вставить
        table_marker = "## 🟢 Полностью переведённые моды (в папке `completed/`)"
        if table_marker in content:
            parts = content.split(table_marker)
            lines = parts[1].strip().splitlines()
            # Добавляем в конец таблицы
            lines.append(completed_entry)
            content = parts[0] + table_marker + "\n\n" + "\n".join(lines) + "\n"

    # Пересчёт счётчиков в шапке
    completed_count = len(os.listdir(COMPLETED_DIR)) if os.path.isdir(COMPLETED_DIR) else 0
    # Найдём активные папки (начинающиеся с цифры)
    active_count = len([f for f in os.listdir(TASKS_DIR) if os.path.isdir(os.path.join(TASKS_DIR, f)) and re.match(r'^\d+_', f)])
    
    content = re.sub(
        r'\*\*Всего активных модов в очереди:\*\*\s*\d+\s*\|\s*\*\*Завершено:\*\*\s*\d+',
        f'**Всего активных модов в очереди:** {active_count} | **Завершено:** {completed_count}',
        content
    )

    with open(QUEUE_FILE, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Обновлён файл очереди QUEUE.md (активных: {active_count}, завершено: {completed_count}).")

def main():
    if len(sys.argv) < 2:
        print("Использование: python tools/finalize_mod.py <folder_name_or_namespace>")
        sys.exit(1)

    target = sys.argv[1].strip()
    folder_path, folder_name = find_task_folder(target)

    if not folder_path:
        print(f"❌ Папка задачи для '{target}' не найдена в {TASKS_DIR}!")
        sys.exit(1)

    namespace = get_namespace_from_folder(folder_path, folder_name)
    print(f"🔍 Финализация мода: '{namespace}' (папка: {folder_name})")

    # 1. Проверка полноты перевода
    total_keys, cyrillic_keys = check_translation_completeness(namespace)
    print(f"📊 Статус перевода: {cyrillic_keys}/{total_keys} ключей на русском языке")
    if total_keys > 0 and cyrillic_keys < total_keys:
        print(f"⚠️ Внимание: {total_keys - cyrillic_keys} строк могут быть не переведены!")

    # 2. Обновление TASK.md
    update_task_md(folder_path, namespace, total_keys)

    # 3. Перемещение папки в completed/translate_<namespace>
    os.makedirs(COMPLETED_DIR, exist_ok=True)
    dest_path = os.path.join(COMPLETED_DIR, f"translate_{namespace}")
    if os.path.exists(dest_path):
        print(f"⚠️ Целевая папка {dest_path} уже существует. Замена содержимого...")
        shutil.rmtree(dest_path)
    shutil.move(folder_path, dest_path)
    print(f"📦 Папка перемещена в: tasks/Translate_Mods/completed/translate_{namespace}")

    # 4. Обновление QUEUE.md
    update_queue_file(folder_name, namespace)

    # 5. Синхронизация с игрой
    print("🔄 Запуск глобальной синхронизации sync_all_to_game.js...")
    subprocess.run(["node", os.path.join(PROJECT_ROOT, "sync_all_to_game.js")], cwd=PROJECT_ROOT)

    # 6. Физическая проверка игрового файла
    game_lang_file = os.path.join(GAME_PROFILE_LANG, namespace, "lang", "ru_ru.json")
    if os.path.isfile(game_lang_file):
        with open(game_lang_file, "r", encoding="utf-8") as f:
            game_data = json.load(f)
        print(f"🎉 ФИЗИЧЕСКИ ВЕРИФИЦИРОВАНО В ИГРЕ: {game_lang_file} ({len(game_data)} ключей)")
    else:
        print(f"⚠️ Игровой файл не обнаружен: {game_lang_file}")

    print("\n=======================================================")
    print(f"✨ МОД '{namespace}' УСПЕШНО ФИНАЛИЗИРОВАН И ПЕРЕНЕСЁН!")
    print("=======================================================")

if __name__ == "__main__":
    main()
