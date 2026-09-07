import sys
import json
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

base_path = Path(r"G:\curseforge\minecraft\Instances\Cisco's Fantasy Medieval RPG [Dragonfyre]")

print("=== ВЕРИФИКАЦИЯ СОЗДАННЫХ ФАЙЛОВ ===")

# 1. Quest check
qf = base_path / "config" / "ftbquests" / "quests" / "chapters" / "age_of_dragons.snbt"
print("\n1. FTBQuests age_of_dragons.snbt (Lines 20-35):")
print("\n".join(qf.read_text(encoding="utf-8").splitlines()[20:35]))

# 2. Medieval Origins check
mof = base_path / "kubejs" / "assets" / "medievalorigins" / "lang" / "ru_ru.json"
print("\n2. Medieval Origins ru_ru.json:")
print(mof.read_text(encoding="utf-8"))

# 3. Origins Classes check
ocf = base_path / "kubejs" / "assets" / "origins-classes" / "lang" / "ru_ru.json"
print("\n3. Origins Classes ru_ru.json:")
print(ocf.read_text(encoding="utf-8"))

# 4. Skill Tree check
stf = base_path / "kubejs" / "assets" / "skilltree" / "lang" / "ru_ru.json"
print("\n4. Passive Skill Tree ru_ru.json:")
print(stf.read_text(encoding="utf-8"))

# 5. Mowzie's Cataclysm check
mcf = base_path / "kubejs" / "assets" / "mowzies_cataclysm" / "lang" / "ru_ru.json"
print("\n5. Mowzie's Cataclysm ru_ru.json:")
print(mcf.read_text(encoding="utf-8"))

# 6. Tooltip JS check
ttf = base_path / "kubejs" / "client_scripts" / "example_custom_tooltips.js"
print("\n6. KubeJS Tooltip Script:")
print(ttf.read_text(encoding="utf-8"))
