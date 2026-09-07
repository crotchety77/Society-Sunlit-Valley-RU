import zipfile
import json
from pathlib import Path

base_path = Path(r"G:\curseforge\minecraft\Instances\Cisco's Fantasy Medieval RPG [Dragonfyre]")
mods_path = base_path / "mods"

for m in ["strictly_origins", "origins-classes", "irons_spellbooks", "Cataclysm"]:
    for f in mods_path.glob(f"*{m}*.jar"):
        print(f"\n--- Checking {f.name} ---")
        try:
            with zipfile.ZipFile(f, 'r') as z:
                langs = [n for n in z.namelist() if "lang/" in n and n.endswith(".json")]
                print("Found lang files:", langs)
                en_lang = [n for n in langs if "en_us.json" in n]
                if en_lang:
                    data = json.loads(z.read(en_lang[0]).decode('utf-8'))
                    print(f"Sample 3 keys from {en_lang[0]}:")
                    for k in list(data.keys())[:3]:
                        print(f"  '{k}': '{data[k]}'")
        except Exception as e:
            print(f"Error: {e}")
