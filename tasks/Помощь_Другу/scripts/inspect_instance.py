import os
import json
from pathlib import Path

base_path = Path(r"G:\curseforge\minecraft\Instances\Cisco's Fantasy Medieval RPG [Dragonfyre]")

print(f"Base path exists: {base_path.exists()}")

if base_path.exists():
    # 1. Check mods
    mods_path = base_path / "mods"
    if mods_path.exists():
        mods = [f.name for f in mods_path.iterdir() if f.suffix == ".jar"]
        print(f"\nTotal mods: {len(mods)}")
        # Search for key mods
        key_keywords = ["origin", "class", "skill", "quest", "kubejs", "irons", "passive", "levelz", "apotheosis", "born", "cataclysm", "celestisynth", "ftb"]
        print("Relevant mods found:")
        for m in sorted(mods):
            if any(k in m.lower() for k in key_keywords):
                print(f"  - {m}")
                
    # 2. Check kubejs
    kjs_path = base_path / "kubejs"
    if kjs_path.exists():
        print(f"\nKubeJS directory structure:")
        for root, dirs, files in os.walk(kjs_path):
            rel = os.path.relpath(root, kjs_path)
            if rel != ".":
                print(f"  DIR: {rel}")
            for f in files:
                print(f"    FILE: {os.path.join(rel, f)}")
    else:
        print("\nNo kubejs directory found!")

    # 3. Check ftbquests
    ftb_path = base_path / "config" / "ftbquests"
    if ftb_path.exists():
        print(f"\nFTBQuests chapters:")
        ch_path = ftb_path / "quests" / "chapters"
        if ch_path.exists():
            chapters = list(ch_path.glob("*.snbt"))
            print(f"Found {len(chapters)} chapters:")
            for ch in chapters[:15]:
                print(f"  - {ch.name}")
            # inspect one chapter
            if chapters:
                sample = chapters[0].read_text(encoding="utf-8", errors="ignore")[:500]
                print(f"\nSample from {chapters[0].name}:\n{sample}")
    
    # 4. Check datapacks / resourcepacks
    dp_path = base_path / "datapacks"
    if dp_path.exists():
        print(f"\nDatapacks: {[f.name for f in dp_path.iterdir()]}")
    
    rp_path = base_path / "resourcepacks"
    if rp_path.exists():
        print(f"\nResourcepacks: {[f.name for f in rp_path.iterdir()]}")
