import os
import re
from pathlib import Path

base_path = Path(r"G:\curseforge\minecraft\Instances\Cisco's Fantasy Medieval RPG [Dragonfyre]")

# 1. Inspect carpgitemmod.js
carpg = base_path / "kubejs" / "startup_scripts" / "carpgitemmod.js"
if carpg.exists():
    print("=== KUBEJS CUSTOM ITEMS (carpgitemmod.js) ===")
    print(carpg.read_text(encoding="utf-8", errors="ignore")[:1000])

# 2. Inspect FTBQuests chapter format
ch_path = base_path / "config" / "ftbquests" / "quests" / "chapters"
if ch_path.exists():
    for f in list(ch_path.glob("*.snbt"))[:3]:
        text = f.read_text(encoding="utf-8", errors="ignore")
        print(f"\n=== QUEST CHAPTER: {f.name} ===")
        # find title, subtitle, description lines
        titles = re.findall(r'title:\s*"([^"]+)"', text)
        subtitles = re.findall(r'subtitle:\s*"([^"]+)"', text)
        print(f"Titles found ({len(titles)}):", titles[:3])
        print(f"Subtitles found ({len(subtitles)}):", subtitles[:3])

# 3. Inspect Passive Skill Tree / Origins lang keys
print("\n=== CHECKING ASSETS IN KUBEJS ===")
kjs_assets = base_path / "kubejs" / "assets"
for p in kjs_assets.rglob("*"):
    if p.is_file():
        print(" ", p.relative_to(kjs_assets))
