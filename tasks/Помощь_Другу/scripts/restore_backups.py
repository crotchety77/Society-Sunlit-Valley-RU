import shutil
from pathlib import Path

GAME_INSTANCE = Path(r"G:\curseforge\minecraft\Instances\Cisco's Fantasy Medieval RPG [Dragonfyre]")
CHAPTERS_DIR = GAME_INSTANCE / "config" / "ftbquests" / "quests" / "chapters"

print("=== ВОССТАНОВЛЕНИЕ ОРИГИНАЛЬНЫХ ГЛАВ ИЗ БЭКАПОВ ===")
for bak in CHAPTERS_DIR.glob("*.snbt.bak"):
    orig = bak.with_suffix("")
    shutil.copy2(bak, orig)
    print(f" Восстановлен из бэкапа: {orig.name}")

print("\nОригинальное состояние сборки восстановлено.")
