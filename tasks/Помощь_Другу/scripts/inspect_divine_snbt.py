import sys
from pathlib import Path

base_path = Path(r"G:\curseforge\minecraft\Instances\Cisco's Fantasy Medieval RPG [Dragonfyre]")
ch = base_path / "config" / "ftbquests" / "quests" / "chapters" / "divine_equipment.snbt"
print(ch.read_text(encoding="utf-8")[:1500])
