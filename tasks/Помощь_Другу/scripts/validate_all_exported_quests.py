import re
import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

GAME_INSTANCE = Path(r"G:\curseforge\minecraft\Instances\Cisco's Fantasy Medieval RPG [Dragonfyre]")
CHAPTERS_DIR = GAME_INSTANCE / "config" / "ftbquests" / "quests" / "chapters"
TRANSLATE_DIR = Path(r"c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\tasks\Помощь_Другуу\Скрипты_для_помощи_ftb_quests\chapters_to_translate")

print("=== ПРОВЕРКА ВСЕХ 21 ВЫГРУЖЕННЫХ ФАЙЛОВ ГЛАВ КВЕСТОВ ===\n")

total_quests = 0
total_files = 0
issues_found = []

for txt_file in sorted(TRANSLATE_DIR.glob("*.txt")):
    total_files += 1
    content = txt_file.read_text(encoding="utf-8")
    
    # 1. Извлекаем блоки квестов
    blocks = re.findall(r'===\s*\[КВЕСТ\s*(\d+)\s*\|\s*ID:\s*([A-F0-9]+)\]\s*===(.*?)(?:---\s*КОНЕЦ КВЕСТА|\Z)', content, re.DOTALL)
    
    snbt_file = CHAPTERS_DIR / f"{txt_file.stem}.snbt"
    snbt_exists = snbt_file.exists()
    
    print(f"📄 [{txt_file.name}] — Квестов в файле: {len(blocks)}")
    total_quests += len(blocks)
    
    for idx, qid, body in blocks:
        # Проверяем наличие всех ключевых полей
        if "EN_TITLE:" not in body or "RU_TITLE:" not in body:
            issues_found.append(f"{txt_file.name} (Квест {idx} {qid}): Отсутствует блок TITLE")
        if "EN_SUBTITLE:" not in body or "RU_SUBTITLE:" not in body:
            issues_found.append(f"{txt_file.name} (Квест {idx} {qid}): Отсутствует блок SUBTITLE")
        if "EN_DESCRIPTION:" not in body or "RU_DESCRIPTION:" not in body:
            issues_found.append(f"{txt_file.name} (Квест {idx} {qid}): Отсутствует блок DESCRIPTION")

print(f"\n=======================================================")
print(f"ИТОГ: Проверено {total_files} файлов глав, суммарно {total_quests} квестов.")
if not issues_found:
    print("✅ ВСЕ ФАЙЛЫ ИДЕАЛЬНО СФОРМАТИРОВАНЫ И СТРУКТУРИРОВАНЫ БЕЗ ОШИБОК!")
else:
    print(f"❌ Найдено проблем: {len(issues_found)}")
    for iss in issues_found[:10]:
        print("  -", iss)
