#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tasks/Translate_Mods/scripts/generate_all_mod_tasks.py
Автоматическая генерация структуры задач для перевода 10 выбранных модов сборки:
1. twigs
2. splendid_slimes
3. vintagedelight
4. whimsy_deco
5. unusualfishmod
6. tanukidecor
7. moreminecarts
8. nightlights
9. chimes
10. cozycafe
"""

import os
import sys
import json
import glob
import zipfile
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
MODS_DIR = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\mods"
KUBEJS_ASSETS_DIR = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets"
LOCAL_TRANSLATIONS_DIR = os.path.join(ROOT_DIR, "translations", "mods")
TASKS_ROOT = os.path.join(ROOT_DIR, "tasks", "Translate_Mods")

TARGET_MODS = [
    {
        "namespace": "twigs",
        "title": "Twigs (Декор, крыши, лампы, бамбук)",
        "desc": "Столы, стулья, лампы, черепичные крыши, бамбук, морские ракушки и декоративные блоки."
    },
    {
        "namespace": "splendid_slimes",
        "title": "Splendid Slimes (Слизни и слаймовые блоки)",
        "desc": "Разновидности слаймов, слаймовые блоки, банки, желе и слаймовые предметы."
    },
    {
        "namespace": "vintagedelight",
        "title": "Vintage Delight (Винтажная кулинария и фермерство)",
        "desc": "Маринование, бочки и банки брожения, перец призрака, соляные лампы, сыры."
    },
    {
        "namespace": "whimsy_deco",
        "title": "Whimsy Deco (Плюшевые игрушки и уютный декор)",
        "desc": "Плюшевые панды, капибары, декоративные настенные полки и винтажные украшения."
    },
    {
        "namespace": "unusualfishmod",
        "title": "Unusual Fish (Необычные рыбы и улов)",
        "desc": "Морские и речные обитатели, тропические рыбы, вёдра с рыбой, предметы улова."
    },
    {
        "namespace": "tanukidecor",
        "title": "Tanuki Decor (Японский интерьер и декор)",
        "desc": "Традиционная японская мебель, татами, футоны, раздвижные перегородки сёджи, фонари."
    },
    {
        "namespace": "moreminecarts",
        "title": "More Minecarts (Расширение железных дорог)",
        "desc": "Вагонетки, стрелочные переводы, рельсы, блоки питания путей и железнодорожная логистика."
    },
    {
        "namespace": "nightlights",
        "title": "Night Lights (Светящийся декор и ночники)",
        "desc": "Светящиеся настенные гирлянды, сказочные ночники-грибы, лампочки и подвесные фонарики."
    },
    {
        "namespace": "chimes",
        "title": "Chimes (Музыка ветра)",
        "desc": "Бамбуковые, стеклянные, железные и медные колокольчики ветра, создающие атмосферный звук."
    },
    {
        "namespace": "cozycafe",
        "title": "Cozy Cafe (Уютное кафе и менеджмент кофейни)",
        "desc": "Менеджер кафе, меню, сервировочные тарелки, напитки, выпечка, интерфейсы обслуживания клиентов."
    }
]

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

def find_jars_for_ns(ns):
    target_en = f"assets/{ns}/lang/en_us.json"
    matches = []
    for jar in glob.glob(os.path.join(MODS_DIR, "*.jar")):
        try:
            with zipfile.ZipFile(jar, 'r') as z:
                if target_en in z.namelist():
                    matches.append(jar)
        except Exception:
            pass
    return matches


def generate_apply_sync_script(ns):
    return f"""#!/usr/bin/env python3
# -*- coding: utf-8 -*-
\"\"\"
Скрипт применения и синхронизации локализации для мода '{ns}'.
1. Считывает переводы из new_translate.md.
2. Сохраняет в translations/mods/{ns}.json.
3. Записывает напрямую в D:\\ModrinthApp\\profiles\\Society_ Sunlit Valley\\kubejs\\assets\\{ns}\\lang\\ru_ru.json.
4. Запускает общий node sync_all_to_game.js.
5. Физически считывает файл игры и верифицирует ключи.
\"\"\"

import os
import sys
import json
import re
import subprocess

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
TASK_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LOCAL_MOD_JSON = os.path.join(ROOT_DIR, "translations", "mods", "{ns}.json")
GAME_RU_PATH = r"D:\\ModrinthApp\\profiles\\Society_ Sunlit Valley\\kubejs\\assets\\{ns}\\lang\\ru_ru.json"

def parse_translations():
    target_file = os.path.join(TASK_DIR, "new_translate.md")
    if not os.path.exists(target_file):
        print(f"❌ Не найден файл с переводами: {{target_file}}")
        return {{}}

    with open(target_file, 'r', encoding='utf-8') as f:
        content = f.read()

    json_blocks = re.findall(r'```json\\s*(\\{{.*?\\}})\\s*```', content, flags=re.DOTALL)
    translations = {{}}
    for block in json_blocks:
        try:
            data = json.loads(block)
            for k, v in data.items():
                if isinstance(v, str) and not v.startswith("TODO:"):
                    translations[k] = v
        except Exception as e:
            print(f"[!] Ошибка парсинга JSON: {{e}}")
            
    return translations

def apply_and_sync():
    new_trans = parse_translations()
    print(f"📦 Считано готовых строк перевода: {{len(new_trans)}}")

    os.makedirs(os.path.dirname(LOCAL_MOD_JSON), exist_ok=True)
    local_data = {{}}
    if os.path.exists(LOCAL_MOD_JSON):
        try:
            with open(LOCAL_MOD_JSON, 'r', encoding='utf-8') as f:
                local_data = json.load(f)
        except Exception:
            pass
    local_data.update(new_trans)
    with open(LOCAL_MOD_JSON, 'w', encoding='utf-8') as f:
        json.dump(local_data, f, ensure_ascii=False, indent=2)
    print(f"💾 Обновлён translations/mods/{ns}.json (всего {{len(local_data)}} ключей)")

    os.makedirs(os.path.dirname(GAME_RU_PATH), exist_ok=True)
    game_data = {{}}
    if os.path.exists(GAME_RU_PATH):
        try:
            with open(GAME_RU_PATH, 'r', encoding='utf-8') as f:
                game_data = json.load(f)
        except Exception:
            pass
    game_data.update(new_trans)
    with open(GAME_RU_PATH, 'w', encoding='utf-8') as f:
        json.dump(game_data, f, ensure_ascii=False, indent=2)
    print(f"🎮 Записано напрямую в файл игры: {{GAME_RU_PATH}}")

    sync_js = os.path.join(ROOT_DIR, "sync_all_to_game.js")
    if os.path.exists(sync_js):
        res = subprocess.run(["node", sync_js], cwd=ROOT_DIR, capture_output=True, text=True, encoding='utf-8')
        print(f"🔄 Результат sync_all_to_game.js:\\n{{res.stdout}}")

    print("\\n🔍 ОБЯЗАТЕЛЬНАЯ ВЕРИФИКАЦИЯ ФАЙЛА ИГРЫ:")
    if os.path.exists(GAME_RU_PATH):
        with open(GAME_RU_PATH, 'r', encoding='utf-8') as f:
            verified = json.load(f)
        print(f"✅ Файл физически обновлён! Всего ключей: {{len(verified)}}")
        if new_trans:
            print("Примеры применённых строк:")
            for k in list(new_trans.keys())[:5]:
                print(f"   ▪ [{{k}}]: {{verified.get(k)}}")
    else:
        print("❌ Файл игры не найден!")

if __name__ == "__main__":
    apply_and_sync()
"""

def generate_all():
    print("🚀 Генерация задач локализации для 10 модов...")
    
    for mod in TARGET_MODS:
        ns = mod["namespace"]
        title = mod["title"]
        desc = mod["desc"]
        
        jars = find_jars_for_ns(ns)
        if not jars:
            print(f"❌ Не найден JAR для {ns}")
            continue
            
        jar_names = ", ".join([os.path.basename(j) for j in jars])
        task_dir = os.path.join(TASKS_ROOT, f"translate_{ns}")
        scripts_dir = os.path.join(task_dir, "scripts")
        os.makedirs(scripts_dir, exist_ok=True)
        
        # Извлекаем строки из всех JAR
        en_us = {}
        ru_jar = {}
        for jar_path in jars:
            with zipfile.ZipFile(jar_path, 'r') as z:
                en_path = f"assets/{ns}/lang/en_us.json"
                ru_path = f"assets/{ns}/lang/ru_ru.json"
                if en_path in z.namelist():
                    en_us.update(parse_relaxed_json(z.read(en_path).decode('utf-8', errors='replace')))
                if ru_path in z.namelist():
                    ru_jar.update(parse_relaxed_json(z.read(ru_path).decode('utf-8', errors='replace')))

                
        # Считываем переопределения KubeJS и локальные
        kubejs_ru = {}
        k_path = os.path.join(KUBEJS_ASSETS_DIR, ns, "lang", "ru_ru.json")
        if os.path.exists(k_path):
            try:
                kubejs_ru = json.load(open(k_path, 'r', encoding='utf-8'))
            except Exception: pass

        local_ru = {}
        l_path = os.path.join(LOCAL_TRANSLATIONS_DIR, f"{ns}.json")
        if os.path.exists(l_path):
            try:
                local_ru = json.load(open(l_path, 'r', encoding='utf-8'))
            except Exception: pass
            
        merged_ru = {}
        if isinstance(ru_jar, dict): merged_ru.update(ru_jar)
        if isinstance(kubejs_ru, dict): merged_ru.update(kubejs_ru)
        if isinstance(local_ru, dict): merged_ru.update(local_ru)

        untranslated = {}
        translated = {}
        
        for k, v in en_us.items():
            if k in merged_ru and isinstance(merged_ru[k], str) and merged_ru[k].strip() and merged_ru[k] != v:
                translated[k] = merged_ru[k]
            else:
                untranslated[k] = v

        # Подсчёт категорий
        items_cnt = sum(1 for k in en_us if k.startswith("item."))
        blocks_cnt = sum(1 for k in en_us if k.startswith("block."))
        gui_cnt = sum(1 for k in en_us if k.startswith(("gui.", "container.", "screen.", "menu.")))
        tooltips_cnt = sum(1 for k in en_us if k.startswith(("tooltip.", "desc.")))

        # 1. TASK.md
        task_md_path = os.path.join(task_dir, "TASK.md")
        with open(task_md_path, 'w', encoding='utf-8') as f:
            f.write(f"# Задача: Локализация мода {title}\n\n")
            f.write(f"**Namespace:** `{ns}`\n")
            f.write(f"**JAR-файл(ы):** `{jar_names}`\n")
            f.write(f"**Тематика:** {desc}\n\n")
            f.write(f"### Статистика строк:\n")
            f.write(f"* Всего строк: **{len(en_us)}**\n")
            f.write(f"* Предметов (`item.`): **{items_cnt}** | Блоков (`block.`): **{blocks_cnt}**\n")
            f.write(f"* GUI / Меню: **{gui_cnt}** | Тултипов: **{tooltips_cnt}**\n")
            f.write(f"* Не переведено: **{len(untranslated)}** | Переведено: **{len(translated)}**\n\n")
            f.write(f"### Порядок работы:\n")
            f.write(f"1. Согласовать перевод в файле `new_translate.md` согласно глоссарию `glossary.md` и правилам форматирования.\n")
            f.write(f"2. Запустить скрипт `python tasks/Translate_Mods/translate_{ns}/scripts/apply_and_sync.py`.\n")
            f.write(f"3. Проверить физический файл игры и нажать `F3 + T` в Minecraft.\n")

        # 2. new_translate.md
        new_trans_path = os.path.join(task_dir, "new_translate.md")
        with open(new_trans_path, 'w', encoding='utf-8') as f:
            f.write(f"# Локализация мода: {title} (`{ns}`)\n\n")
            f.write(f"**JAR:** `{jar_names}` | **Всего строк:** {len(en_us)} | **Не переведено:** {len(untranslated)}\n\n")

            f.write(f"## 1. Визуальный контекст и оформление\n")
            f.write(f"* Форматирование: Названия предметов/блоков начинаются с Заглавной буквы.\n")
            f.write(f"* Валюта: использовать значок монеты `§e●` (`U+25CF`).\n")
            f.write(f"* Тултипы: подсветка клавиш `§6Shift + ПКМ§7`.\n\n")
            
            f.write(f"## 2. Непереведённые строки (требуют перевода)\n\n")
            f.write(f"```json\n")
            untrans_payload = {k: f"TODO: {v}" for k, v in untranslated.items()}
            f.write(json.dumps(untrans_payload, ensure_ascii=False, indent=2))
            f.write(f"\n```\n\n")

            if translated:
                f.write(f"## 3. Существующие переводы (для контекста)\n\n")
                f.write(f"```json\n")
                f.write(json.dumps(translated, ensure_ascii=False, indent=2))
                f.write(f"\n```\n")

        # 3. scripts/apply_and_sync.py
        script_path = os.path.join(scripts_dir, "apply_and_sync.py")
        with open(script_path, 'w', encoding='utf-8') as f:
            f.write(generate_apply_sync_script(ns))

        print(f"✅ Создана задача: translate_{ns} ({len(untranslated)} непереведённых строк)")

if __name__ == "__main__":
    generate_all()
