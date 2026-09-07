import os
import json
from pathlib import Path

base_path = Path(r"G:\curseforge\minecraft\Instances\Cisco's Fantasy Medieval RPG [Dragonfyre]")

print("=== ПОИСК В PAXI / DATAPACKS / RESOURCEPACKS ===")

paxi = base_path / "config" / "paxi"
if paxi.exists():
    for p in paxi.rglob("*"):
        if p.is_file():
            try:
                text = p.read_text(encoding="utf-8", errors="ignore")
                for term in ["demi", "lux", "athena", "blessing", "origin"]:
                    if term in text.lower():
                        print(f"[{p.relative_to(paxi)}] matched '{term}'")
            except:
                pass
