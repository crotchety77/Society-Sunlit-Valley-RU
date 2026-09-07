import os
from pathlib import Path

base_path = Path(r"G:\curseforge\minecraft\Instances\Cisco's Fantasy Medieval RPG [Dragonfyre]")
ch = base_path / "config" / "ftbquests" / "quests" / "chapters" / "age_of_dragons.snbt"
if ch.exists():
    text = ch.read_text(encoding="utf-8")
    print("=== FIRST 60 LINES OF age_of_dragons.snbt ===")
    print("\n".join(text.splitlines()[:60]))
