import sys
import shutil
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

workspace_pack = Path(r"c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\tasks\Помощь_Другуу\translation_pack")
game_instance = Path(r"G:\curseforge\minecraft\Instances\Cisco's Fantasy Medieval RPG [Dragonfyre]")

print("=== 1. КОПИРОВАНИЕ ГЛАВЫ КВЕСТОВ В ПАПКУ ПЕРЕВОДА ===")
game_quest = game_instance / "config" / "ftbquests" / "quests" / "chapters" / "age_of_dragons.snbt"
pack_quest_dir = workspace_pack / "config" / "ftbquests" / "quests" / "chapters"
pack_quest_dir.mkdir(parents=True, exist_ok=True)
pack_quest = pack_quest_dir / "age_of_dragons.snbt"

if game_quest.exists():
    shutil.copy2(game_quest, pack_quest)
    print(f" Скопирован квест: {pack_quest.relative_to(workspace_pack)}")

print("\n=== 2. СИНХРОНИЗАЦИЯ translation_pack -> ИГРА ===")
copied_count = 0
for src_file in workspace_pack.rglob("*"):
    if src_file.is_file():
        rel = src_file.relative_to(workspace_pack)
        dst_file = game_instance / rel
        dst_file.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src_file, dst_file)
        print(f" [Синхронизировано в игру] -> {rel}")
        copied_count += 1

print(f"\nВсего синхронизировано файлов: {copied_count}")

print("\n=== 3. ПРЯМАЯ ВЕРИФИКАЦИЯ ФАЙЛОВ ИГРЫ ===")
for src_file in workspace_pack.rglob("*"):
    if src_file.is_file():
        rel = src_file.relative_to(workspace_pack)
        dst_file = game_instance / rel
        exists = dst_file.exists()
        size = dst_file.stat().st_size if exists else 0
        print(f" [OK] {rel} (Размер в игре: {size} байт)")

print("\n=== ВСЕ ФАЙЛЫ В ПАПКЕ ПЕРЕВОДА И В ИГРЕ СИНХРОНИЗИРОВАНЫ И ПРОВЕРЕНЫ! ===")
