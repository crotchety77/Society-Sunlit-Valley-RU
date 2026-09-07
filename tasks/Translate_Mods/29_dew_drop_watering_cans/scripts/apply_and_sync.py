#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Скрипт применения и физической верификации перевода мода Dew Drop Watering Cans (29_dew_drop_watering_cans).
"""

import json
import os
import re
import subprocess
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

TASK_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ROOT_DIR = os.path.abspath(os.path.join(TASK_DIR, "..", "..", ".."))
GAME_PROFILE_DIR = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley"
GAME_ASSETS_DIR = os.path.join(GAME_PROFILE_DIR, "kubejs", "assets")

NEW_TRANSLATE_FILE = os.path.join(TASK_DIR, "new_translate.md")
MOD_TRANSLATION_FILE = os.path.join(ROOT_DIR, "translations", "mods", "dew_drop_watering_cans.json")
SOCIETY_RU_FILE = os.path.join(ROOT_DIR, "translations", "society", "ru_ru.json")
SOCIETY_EN_FILE = os.path.join(ROOT_DIR, "translations", "society", "en_us.json")
ADD_TOOLTIPS_FILE = os.path.join(ROOT_DIR, "game_data", "client_scripts", "tooltips", "addTooltips.js")

GAME_MOD_LANG_DIR = os.path.join(GAME_ASSETS_DIR, "dew_drop_watering_cans", "lang")
GAME_MOD_RU_FILE = os.path.join(GAME_MOD_LANG_DIR, "ru_ru.json")
GAME_SOCIETY_RU_FILE = os.path.join(GAME_ASSETS_DIR, "society", "lang", "ru_ru.json")


def parse_new_translate():
    """Считывает блоки JSON из new_translate.md"""
    if not os.path.exists(NEW_TRANSLATE_FILE):
        raise FileNotFoundError(f"Файл {NEW_TRANSLATE_FILE} не найден!")

    with open(NEW_TRANSLATE_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Извлечение JSON блоков
    json_blocks = re.findall(r"```json\s*(\{[\s\S]*?\})\s*```", content)
    if len(json_blocks) < 2:
        raise ValueError("В new_translate.md должно быть как минимум 2 блока json (мод и тултипы)!")

    mod_dict = json.loads(json_blocks[0])
    tooltips_dict = json.loads(json_blocks[1])
    return mod_dict, tooltips_dict


def update_project_files(mod_dict, tooltips_dict):
    """Обновляет файлы в translations/ и game_data/"""
    print("📝 Обновление файлов проекта translations/...")
    os.makedirs(os.path.dirname(MOD_TRANSLATION_FILE), exist_ok=True)
    with open(MOD_TRANSLATION_FILE, "w", encoding="utf-8") as f:
        json.dump(mod_dict, f, ensure_ascii=False, indent=2)
    print(f"  ✓ Записан {MOD_TRANSLATION_FILE}")

    # Обновление translations/society/ru_ru.json
    with open(SOCIETY_RU_FILE, "r", encoding="utf-8") as f:
        soc_ru = json.load(f)
    for k, v in tooltips_dict.items():
        soc_ru[k] = v
    with open(SOCIETY_RU_FILE, "w", encoding="utf-8") as f:
        json.dump(soc_ru, f, ensure_ascii=False, indent=2)
    print(f"  ✓ Обновлен {SOCIETY_RU_FILE}")

    # Обновление addTooltips.js (Rule 14)
    print(f"📝 Проверка регистрации тултипов в {ADD_TOOLTIPS_FILE}...")
    with open(ADD_TOOLTIPS_FILE, "r", encoding="utf-8") as f:
        tooltip_code = f.read()

    target_code = """  // Dew Drop Watering Cans
  [
    { item: "dew_drop_watering_cans:copper_watering_can", key: "tooltip.dew_drop_watering_cans.copper_watering_can" },
    { item: "dew_drop_watering_cans:iron_watering_can", key: "tooltip.dew_drop_watering_cans.iron_watering_can" },
    { item: "dew_drop_watering_cans:gold_watering_can", key: "tooltip.dew_drop_watering_cans.gold_watering_can" },
    { item: "dew_drop_watering_cans:diamond_watering_can", key: "tooltip.dew_drop_watering_cans.diamond_watering_can" },
    { item: "dew_drop_watering_cans:netherite_watering_can", key: "tooltip.dew_drop_watering_cans.netherite_watering_can" },
  ].forEach((can) => {
    tooltip.add(can.item, [
      Text.translatable(can.key).gray(),
      Text.translatable("tooltip.dew_drop_watering_cans.common_refill").darkGray()
    ]);
  });
"""

    if "dew_drop_watering_cans:copper_watering_can" not in tooltip_code:
        # Вставляем перед последним `});`
        last_idx = tooltip_code.rfind("});")
        if last_idx != -1:
            tooltip_code = tooltip_code[:last_idx] + target_code + "\n" + tooltip_code[last_idx:]
            with open(ADD_TOOLTIPS_FILE, "w", encoding="utf-8") as f:
                f.write(tooltip_code)
            print("  ✓ Тултипы леек успешно добавлены в addTooltips.js")
    else:
        print("  ✓ Тултипы леек уже присутствуют в addTooltips.js")


def update_game_directly(mod_dict, tooltips_dict):
    """Прямая запись в папку игры (Rule 1)"""
    print("🎮 Прямая запись в папку игры...")
    os.makedirs(GAME_MOD_LANG_DIR, exist_ok=True)
    game_mod_json = {}
    if os.path.exists(GAME_MOD_RU_FILE):
        try:
            with open(GAME_MOD_RU_FILE, "r", encoding="utf-8") as f:
                game_mod_json = json.load(f)
        except Exception:
            pass
    game_mod_json.update(mod_dict)
    with open(GAME_MOD_RU_FILE, "w", encoding="utf-8") as f:
        json.dump(game_mod_json, f, ensure_ascii=False, indent=2)
    print(f"  ✓ Записан {GAME_MOD_RU_FILE}")

    # Обновление game society/lang/ru_ru.json
    if os.path.exists(GAME_SOCIETY_RU_FILE):
        with open(GAME_SOCIETY_RU_FILE, "r", encoding="utf-8") as f:
            soc_game = json.load(f)
        soc_game.update(tooltips_dict)
        with open(GAME_SOCIETY_RU_FILE, "w", encoding="utf-8") as f:
            json.dump(soc_game, f, ensure_ascii=False, indent=2)
        print(f"  ✓ Обновлен {GAME_SOCIETY_RU_FILE}")


def run_global_sync():
    """Запуск общего sync_all_to_game.js"""
    print("🔄 Запуск глобальной синхронизации sync_all_to_game.js...")
    res = subprocess.run(["node", "sync_all_to_game.js"], cwd=ROOT_DIR, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if res.returncode != 0:
        print(f"❌ Ошибка синхронизации:\n{res.stderr}")
        sys.exit(1)
    print("  ✓ Синхронизация завершена успешно.")


def verify_game_files(mod_dict, tooltips_dict):
    """Физическая верификация файлов игры (Rule 2)"""
    print("\n🔍 ОБЯЗАТЕЛЬНАЯ ВЕРИФИКАЦИЯ ФАЙЛОВ ИГРЫ:")
    if not os.path.exists(GAME_MOD_RU_FILE):
        raise FileNotFoundError(f"Файл игры не найден: {GAME_MOD_RU_FILE}")
    with open(GAME_MOD_RU_FILE, "r", encoding="utf-8") as f:
        verified_mod = json.load(f)

    if not os.path.exists(GAME_SOCIETY_RU_FILE):
        raise FileNotFoundError(f"Файл игры не найден: {GAME_SOCIETY_RU_FILE}")
    with open(GAME_SOCIETY_RU_FILE, "r", encoding="utf-8") as f:
        verified_soc = json.load(f)

    all_ok = True
    print("\n📦 Проверка названий леек в игре (assets/dew_drop_watering_cans/lang/ru_ru.json):")
    for k, v in mod_dict.items():
        val = verified_mod.get(k)
        if val == v:
            print(f"  [OK] {k} -> {val}")
        else:
            print(f"  [FAIL] {k} -> ожидалось '{v}', получено '{val}'")
            all_ok = False

    print("\n💬 Проверка тултипов в игре (assets/society/lang/ru_ru.json):")
    for k, v in tooltips_dict.items():
        val = verified_soc.get(k)
        if val == v:
            print(f"  [OK] {k} -> {val}")
        else:
            print(f"  [FAIL] {k} -> ожидалось '{v}', получено '{val}'")
            all_ok = False

    if not all_ok:
        print("\n❌ ВЕРИФИКАЦИЯ НЕ ПРОЙДЕНА!")
        sys.exit(1)
    else:
        print("\n✨ ВСЕ КЛЮЧИ УСПЕШНО ПРОВЕРЕНЫ И ПОДТВЕРЖДЕНЫ В ИГРЕ!")


def main():
    mod_dict, tooltips_dict = parse_new_translate()
    update_project_files(mod_dict, tooltips_dict)
    update_game_directly(mod_dict, tooltips_dict)
    run_global_sync()
    verify_game_files(mod_dict, tooltips_dict)


if __name__ == "__main__":
    main()
