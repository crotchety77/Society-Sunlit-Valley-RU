import os
import sys
import json
import shutil

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

workspace_root = r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода'
cobblemon_root = r'G:\curseforge\minecraft\Instances\Society Sunlit Cobblemon'
cobblemon_dir = os.path.join(workspace_root, 'SborkaCobblemon')
translations_dir = os.path.join(cobblemon_dir, 'translations')
assets_target = os.path.join(cobblemon_root, 'kubejs', 'assets')

def main():
    print("=====================================================================")
    print("⚡ СИНХРОНИЗАЦИЯ ПЕРЕВОДОВ И СКРИПТОВ ДЛЯ SOCIETY SUNLIT COBBLEMON")
    print("=====================================================================")
    print(f"Целевая папка игры: {cobblemon_root}")

    if not os.path.exists(cobblemon_root):
        print(f"❌ ОШИБКА: Папка сборки Cobblemon не найдена: {cobblemon_root}")
        sys.exit(1)

    # 1. Sync mod translations from SborkaCobblemon/translations/mods/*.json
    mods_dir = os.path.join(translations_dir, 'mods')
    if os.path.exists(mods_dir):
        print("\n--- 1. Синхронизация переводов модов Cobblemon ---")
        for f in os.listdir(mods_dir):
            if f.endswith('.json'):
                namespace = os.path.splitext(f)[0]
                src = os.path.join(mods_dir, f)
                dest_dir = os.path.join(assets_target, namespace, 'lang')
                dest_file = os.path.join(dest_dir, 'ru_ru.json')
                os.makedirs(dest_dir, exist_ok=True)

                try:
                    with open(src, 'r', encoding='utf-8') as fh:
                        new_data = json.load(fh)
                    existing_data = {}
                    if os.path.exists(dest_file):
                        try:
                            with open(dest_file, 'r', encoding='utf-8') as fh:
                                existing_data = json.load(fh)
                        except Exception:
                            pass
                    merged = {**existing_data, **new_data}
                    with open(dest_file, 'w', encoding='utf-8') as fh:
                        json.dump(merged, fh, ensure_ascii=False, indent=2)
                    print(f"✅ [{namespace}] Синхронизировано ({len(new_data)} ключей) -> {dest_file}")
                except Exception as e:
                    print(f"❌ Ошибка синхронизации {f}: {e}")

    # 2. Sync FTB Quests for Cobblemon
    ftb_dir = os.path.join(translations_dir, 'ftbquests')
    ftb_target = os.path.join(assets_target, 'ftbquestlocalizer', 'lang', 'ru_ru.json')
    if os.path.exists(ftb_dir):
        ftb_src = os.path.join(ftb_dir, 'ru_ru.json')
        if os.path.exists(ftb_src):
            print("\n--- 2. Синхронизация квестов FTB Quests Cobblemon ---")
            try:
                with open(ftb_src, 'r', encoding='utf-8') as fh:
                    ftb_new = json.load(fh)
                existing_ftb = {}
                if os.path.exists(ftb_target):
                    with open(ftb_target, 'r', encoding='utf-8') as fh:
                        existing_ftb = json.load(fh)
                merged_ftb = {**existing_ftb, **ftb_new}
                with open(ftb_target, 'w', encoding='utf-8') as fh:
                    json.dump(merged_ftb, fh, ensure_ascii=False, indent=2)
                print(f"✅ FTB Quests синхронизировано ({len(merged_ftb)} ключей) -> {ftb_target}")
            except Exception as e:
                print(f"❌ Ошибка синхронизации квестов: {e}")

    # 3. Sync skills for Cobblemon
    skills_dir = os.path.join(translations_dir, 'skills')
    skills_target = os.path.join(assets_target, 'society_skills', 'lang', 'ru_ru.json')
    if os.path.exists(skills_dir):
        skills_src = os.path.join(skills_dir, 'ru_ru.json')
        if os.path.exists(skills_src):
            print("\n--- 3. Синхронизация навыков Cobblemon ---")
            try:
                with open(skills_src, 'r', encoding='utf-8') as fh:
                    skills_new = json.load(fh)
                existing_skills = {}
                if os.path.exists(skills_target):
                    with open(skills_target, 'r', encoding='utf-8') as fh:
                        existing_skills = json.load(fh)
                merged_skills = {**existing_skills, **skills_new}
                with open(skills_target, 'w', encoding='utf-8') as fh:
                    json.dump(merged_skills, fh, ensure_ascii=False, indent=2)
                print(f"✅ society_skills синхронизировано ({len(merged_skills)} ключей) -> {skills_target}")
            except Exception as e:
                print(f"❌ Ошибка синхронизации навыков: {e}")

    print("\n=====================================================================")
    print("🎉 СИНХРОНИЗАЦИЯ COBBLEMON ЗАВЕРШЕНА!")
    print("=====================================================================")

if __name__ == '__main__':
    main()
