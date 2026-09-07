import zipfile
from pathlib import Path

base_path = Path(r"G:\curseforge\minecraft\Instances\Cisco's Fantasy Medieval RPG [Dragonfyre]")
zip_path = base_path / "config" / "paxi" / "datapacks" / "Cisco's Rpg Origins 1.1.4.zip"

powers = [
    "divine_strength", "hubris", "luxian_lineage", "divine_hunger", 
    "lightbringer", "divine_body", "athenas_boon_minor", "athenas_boon_major"
]

with zipfile.ZipFile(zip_path, 'r') as z:
    for p in powers:
        fname = f"data/cisco_rpg_origins/powers/{p}.json"
        if fname in z.namelist():
            print(f"=== {p} ===")
            print(z.read(fname).decode('utf-8'))
