import zipfile
import json
from pathlib import Path

base_path = Path(r"G:\curseforge\minecraft\Instances\Cisco's Fantasy Medieval RPG [Dragonfyre]")
zip_path = base_path / "config" / "paxi" / "datapacks" / "Cisco's Rpg Origins 1.1.4.zip"

print(f"Inspecting {zip_path.name}:")
with zipfile.ZipFile(zip_path, 'r') as z:
    files = z.namelist()
    print(f"Total files: {len(files)}")
    
    # Check for lang files
    langs = [f for f in files if "lang/" in f]
    print("Lang files:", langs)
    
    # Check for origins and powers related to demi-god, lux, athena, blessing
    for f in sorted(files):
        if any(w in f.lower() for w in ["demi", "lux", "athena", "blessing"]):
            print(f"\n--- FILE: {f} ---")
            try:
                content = z.read(f).decode('utf-8', errors='ignore')
                print(content[:1500])
            except Exception as e:
                print(f"Error reading: {e}")
