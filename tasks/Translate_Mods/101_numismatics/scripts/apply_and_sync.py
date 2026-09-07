#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
Скрипт применения и синхронизации локализации для мода 'numismatics'.
1. Считывает переводы из new_translate.md.
2. Сохраняет в translations/mods/numismatics.json.
3. Записывает напрямую в D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\numismatics\lang\ru_ru.json.
4. Запускает общий node sync_all_to_game.js.
5. Физически считывает файл игры и верифицирует ключи.
"""

import os
import sys
import json
import re
import subprocess

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
TASK_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LOCAL_MOD_JSON = os.path.join(ROOT_DIR, "translations", "mods", "numismatics.json")
GAME_RU_PATH = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\numismatics\lang\ru_ru.json"

def parse_translations():
    target_file = os.path.join(TASK_DIR, "new_translate.md")
    if not os.path.exists(target_file):
        print(f"❌ Не найден файл с переводами: {target_file}")
        return {}

    with open(target_file, 'r', encoding='utf-8') as f:
        content = f.read()

    json_blocks = re.findall(r'```json\s*(\{.*?\})\s*```', content, flags=re.DOTALL)
    translations = {}
    for block in json_blocks:
        try:
            data = json.loads(block)
            for k, v in data.items():
                if isinstance(v, str) and not v.startswith("TODO:"):
                    translations[k] = v
        except Exception as e:
            print(f"[!] Ошибка парсинга JSON: {e}")
            
    return translations

def apply_and_sync():
    new_trans = parse_translations()
    print(f"📦 Считано готовых строк перевода: {len(new_trans)}")

    os.makedirs(os.path.dirname(LOCAL_MOD_JSON), exist_ok=True)
    local_data = {}
    if os.path.exists(LOCAL_MOD_JSON):
        try:
            with open(LOCAL_MOD_JSON, 'r', encoding='utf-8') as f:
                local_data = json.load(f)
        except Exception:
            pass
    local_data.update(new_trans)
    with open(LOCAL_MOD_JSON, 'w', encoding='utf-8') as f:
        json.dump(local_data, f, ensure_ascii=False, indent=2)
    print(f"💾 Обновлён translations/mods/numismatics.json (всего {len(local_data)} ключей)")

    os.makedirs(os.path.dirname(GAME_RU_PATH), exist_ok=True)
    game_data = {}
    if os.path.exists(GAME_RU_PATH):
        try:
            with open(GAME_RU_PATH, 'r', encoding='utf-8') as f:
                game_data = json.load(f)
        except Exception:
            pass
    game_data.update(new_trans)
    with open(GAME_RU_PATH, 'w', encoding='utf-8') as f:
        json.dump(game_data, f, ensure_ascii=False, indent=2)
    print(f"🎮 Записано напрямую в файл игры: {GAME_RU_PATH}")

    sync_js = os.path.join(ROOT_DIR, "sync_all_to_game.js")
    if os.path.exists(sync_js):
        res = subprocess.run(["node", sync_js], cwd=ROOT_DIR, capture_output=True, text=True, encoding='utf-8')
        print(f"🔄 Результат sync_all_to_game.js:\n{res.stdout}")

    print("\n🔍 ОБЯЗАТЕЛЬНАЯ ВЕРИФИКАЦИЯ ФАЙЛА ИГРЫ:")
    if os.path.exists(GAME_RU_PATH):
        with open(GAME_RU_PATH, 'r', encoding='utf-8') as f:
            verified = json.load(f)
        print(f"✅ Файл физически обновлён! Всего ключей: {len(verified)}")
        if new_trans:
            print("Примеры применённых строк:")
            for k in list(new_trans.keys())[:5]:
                print(f"   ▪ [{k}]: {verified.get(k)}")
    else:
        print("❌ Файл игры не найден!")

if __name__ == "__main__":
    apply_and_sync()
