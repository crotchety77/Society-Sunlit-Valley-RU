import os
import shutil
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

ACTIVE_CHAPTERS = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\config\ftbquests\quests\chapters"
BASE_DIR = r"c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода"
REFERENCE_DIR = os.path.join(BASE_DIR, "game_data", "ftbquests", "reference_414")

def init_reference_if_needed():
    if not os.path.exists(REFERENCE_DIR):
        os.makedirs(REFERENCE_DIR, exist_ok=True)
        for f in os.listdir(ACTIVE_CHAPTERS):
            if f.endswith('.snbt'):
                shutil.copy2(os.path.join(ACTIVE_CHAPTERS, f), os.path.join(REFERENCE_DIR, f))
        print("✅ Инициализирован эталон 4.1.4 в game_data/ftbquests/reference_414/")

def check_integrity():
    if not os.path.exists(ACTIVE_CHAPTERS):
        print(f"❌ Ошибка: Папка квестов не найдена: {ACTIVE_CHAPTERS}")
        return False

    init_reference_if_needed()

    print("====================================================")
    print("🔍 ВАЛИДАЦИЯ ЦЕЛОСТНОСТИ ГЛАВ FTB QUESTS (*.snbt)")
    print("====================================================")

    all_ok = True
    active_files = [f for f in sorted(os.listdir(ACTIVE_CHAPTERS)) if f.endswith('.snbt')]

    for f in active_files:
        act_path = os.path.join(ACTIVE_CHAPTERS, f)
        act_size = os.path.getsize(act_path)
        with open(act_path, 'r', encoding='utf-8') as file:
            act_content = file.read()
        
        act_ids = len(re.findall(r'id:\s*"([0-9A-Fa-f]+)"', act_content))

        # Check reference
        ref_path = os.path.join(REFERENCE_DIR, f)
        if os.path.exists(ref_path):
            ref_size = os.path.getsize(ref_path)
            with open(ref_path, 'r', encoding='utf-8') as rfile:
                ref_content = rfile.read()
            ref_ids = len(re.findall(r'id:\s*"([0-9A-Fa-f]+)"', ref_content))

            # If active size dropped by > 10% or IDs dropped
            if act_ids < ref_ids or act_size < (ref_size * 0.90):
                print(f"❌ [ОШИБКА] {f:<32} | IDs: {act_ids}/{ref_ids} | Размер: {act_size} B (эталон: {ref_size} B)")
                all_ok = False
            else:
                print(f"✅ {f:<32} | IDs: {act_ids:>3} (эталон: {ref_ids:>3}) | Размер: {act_size:>6} B")
        else:
            print(f"ℹ️ {f:<32} | IDs: {act_ids:>3} | Размер: {act_size:>6} B")

    print("====================================================")
    if all_ok:
        print("🎉 ВСЕ ГЛАВЫ КВЕСТОВ В ПОЛНОМ ПОРЯДКЕ И СОХРАНЯЮТ ЦЕЛОСТНОСТЬ!")
    else:
        print("🚨 ОБНАРУЖЕНЫ ПОВРЕЖДЁННЫЕ ИЛИ УРЕЗАННЫЕ ГЛАВЫ КВЕСТОВ!")
    print("====================================================")
    return all_ok

if __name__ == '__main__':
    ok = check_integrity()
    sys.exit(0 if ok else 1)
