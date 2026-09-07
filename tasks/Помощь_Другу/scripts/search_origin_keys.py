import os
import zipfile
import json
from pathlib import Path

base_path = Path(r"G:\curseforge\minecraft\Instances\Cisco's Fantasy Medieval RPG [Dragonfyre]")

print("=== ПОИСК КЛЮЧЕЙ И ОПРЕДЕЛЕНИЙ ДЛЯ 'Demi-God', 'Lux', 'Athena', 'Divine Blessing' ===")

keywords = ["demi-god", "demigod", "lux", "athena", "divine blessing", "divine_blessing", "blessing"]

# 1. Search in JARs (lang files and data files)
mods_path = base_path / "mods"
for jar in mods_path.glob("*.jar"):
    try:
        with zipfile.ZipFile(jar, 'r') as z:
            for name in z.namelist():
                # check origins or powers or lang
                if any(x in name.lower() for x in ["origins/", "powers/", "lang/en_us.json"]):
                    try:
                        content = z.read(name).decode('utf-8', errors='ignore')
                        for kw in keywords:
                            if kw in content.lower():
                                print(f"[JAR: {jar.name}] File: {name} matched '{kw}'")
                                # If lang file, extract matching keys
                                if name.endswith(".json"):
                                    try:
                                        data = json.loads(content)
                                        if isinstance(data, dict):
                                            for k, v in data.items():
                                                if any(kw in str(k).lower() or kw in str(v).lower() for kw in keywords):
                                                    print(f"   KEY: {k} -> {v}")
                                    except:
                                        pass
                    except:
                        pass
    except:
        pass

# 2. Search in workspace/instance files (kubejs, config, datapacks)
for folder in ["kubejs", "config", "datapacks", "patchouli_books"]:
    target_dir = base_path / folder
    if target_dir.exists():
        for p in target_dir.rglob("*"):
            if p.is_file() and p.suffix in [".json", ".snbt", ".js", ".txt"]:
                try:
                    content = p.read_text(encoding="utf-8", errors="ignore")
                    for kw in keywords:
                        if kw in content.lower():
                            print(f"[INSTANCE: {p.relative_to(base_path)}] matched '{kw}'")
                except:
                    pass
