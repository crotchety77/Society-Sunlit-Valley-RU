import zipfile
import json
from pathlib import Path

base_path = Path(r"G:\curseforge\minecraft\Instances\Cisco's Fantasy Medieval RPG [Dragonfyre]")
zip_path = base_path / "config" / "paxi" / "datapacks" / "Cisco's Rpg Origins 1.1.4.zip"

with zipfile.ZipFile(zip_path, 'r') as z:
    for f in z.namelist():
        if ("demigod" in f.lower() or "lux" in f.lower() or "athena" in f.lower()) and f.endswith(".json"):
            print(f"=== {f} ===")
            print(z.read(f).decode('utf-8'))
