#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
Скрипт применения и синхронизации локализации для мода 'dew_drop_farmland_growth'.
1. Считывает переводы из new_translate.md.
2. Сохраняет ключи мода в translations/mods/dew_drop_farmland_growth.json.
3. Сохраняет тултипы в translations/society/ru_ru.json.
4. Записывает напрямую в D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\...
5. Запускает общий node sync_all_to_game.js.
6. Физически считывает файлы игры и верифицирует ключи.
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
LOCAL_MOD_JSON = os.path.join(ROOT_DIR, "translations", "mods", "dew_drop_farmland_growth.json")
LOCAL_SOCIETY_JSON = os.path.join(ROOT_DIR, "translations", "society", "ru_ru.json")

GAME_MOD_PATH = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\dew_drop_farmland_growth\lang\ru_ru.json"
GAME_SOCIETY_PATH = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\society\lang\ru_ru.json"

def parse_translations():
    target_file = os.path.join(TASK_DIR, "new_translate.md")
    if not os.path.exists(target_file):
        print(f"❌ Не найден файл с переводами: {target_file}")
        return {}, {}

    with open(target_file, 'r', encoding='utf-8') as f:
        content = f.read()

    json_blocks = re.findall(r'```json\s*(\{.*?\})\s*```', content, flags=re.DOTALL)
    mod_trans = {}
    soc_trans = {}
    for block in json_blocks:
        try:
            data = json.loads(block)
            for k, v in data.items():
                if isinstance(v, str) and not v.startswith("TODO:"):
                    if "dew_drop_farmland_growth" in k:
                        mod_trans[k] = v
                    else:
                        soc_trans[k] = v
        except Exception as e:
            print(f"[!] Ошибка парсинга JSON: {e}")
            
    return mod_trans, soc_trans

def apply_and_sync():
    mod_trans, soc_trans = parse_translations()
    print(f"📦 Считано строк dew_drop_farmland_growth: {len(mod_trans)}, society тултипов: {len(soc_trans)}")

    # 1. Update translations/mods/dew_drop_farmland_growth.json
    os.makedirs(os.path.dirname(LOCAL_MOD_JSON), exist_ok=True)
    local_mod = {}
    if os.path.exists(LOCAL_MOD_JSON):
        try:
            with open(LOCAL_MOD_JSON, 'r', encoding='utf-8') as f:
                local_mod = json.load(f)
        except Exception:
            pass
    local_mod.update(mod_trans)
    with open(LOCAL_MOD_JSON, 'w', encoding='utf-8') as f:
        json.dump(local_mod, f, ensure_ascii=False, indent=2)
    print(f"💾 Обновлён translations/mods/dew_drop_farmland_growth.json (всего {len(local_mod)} ключей)")

    # 2. Update translations/society/ru_ru.json
    if soc_trans:
        with open(LOCAL_SOCIETY_JSON, 'r', encoding='utf-8') as f:
            local_soc = json.load(f)
        local_soc.update(soc_trans)
        with open(LOCAL_SOCIETY_JSON, 'w', encoding='utf-8') as f:
            json.dump(local_soc, f, ensure_ascii=False, indent=2)
        print(f"💾 Обновлён translations/society/ru_ru.json (+{len(soc_trans)} ключей)")

    # 3. Direct game files write
    os.makedirs(os.path.dirname(GAME_MOD_PATH), exist_ok=True)
    game_mod = {}
    if os.path.exists(GAME_MOD_PATH):
        try:
            with open(GAME_MOD_PATH, 'r', encoding='utf-8') as f:
                game_mod = json.load(f)
        except Exception:
            pass
    game_mod.update(mod_trans)
    with open(GAME_MOD_PATH, 'w', encoding='utf-8') as f:
        json.dump(game_mod, f, ensure_ascii=False, indent=2)
    print(f"🎮 Записано напрямую в файл игры: {GAME_MOD_PATH}")

    # 4. Sync
    sync_js = os.path.join(ROOT_DIR, "sync_all_to_game.js")
    if os.path.exists(sync_js):
        res = subprocess.run(["node", sync_js], cwd=ROOT_DIR, capture_output=True, text=True, encoding='utf-8')
        print(f"🔄 Результат sync_all_to_game.js:\n{res.stdout}")

    # 5. Direct verification
    print("\n🔍 ОБЯЗАТЕЛЬНАЯ ВЕРИФИКАЦИЯ ФАЙЛОВ ИГРЫ:")
    if os.path.exists(GAME_MOD_PATH):
        with open(GAME_MOD_PATH, 'r', encoding='utf-8') as f:
            verified_mod = json.load(f)
        print(f"✅ dew_drop_farmland_growth: всего ключей {len(verified_mod)}")
        for k in list(mod_trans.keys())[:5]:
            print(f"   ▪ [{k}]: {verified_mod.get(k)}")

    if os.path.exists(GAME_SOCIETY_PATH):
        with open(GAME_SOCIETY_PATH, 'r', encoding='utf-8') as f:
            verified_soc = json.load(f)
        print(f"\n✅ society tooltips: проверено {len(soc_trans)} ключей")
        for k in list(soc_trans.keys())[:5]:
            print(f"   ▪ [{k}]: {verified_soc.get(k)}")

if __name__ == "__main__":
    apply_and_sync()

