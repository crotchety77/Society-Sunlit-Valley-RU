import zipfile
import json
from pathlib import Path

base_path = Path(r"G:\curseforge\minecraft\Instances\Cisco's Fantasy Medieval RPG [Dragonfyre]")
mods_path = base_path / "mods"

def inspect_jar_lang(jar_name, lang_file="assets/{}/lang/en_us.json"):
    for f in mods_path.glob(f"*{jar_name}*.jar"):
        print(f"\n--- Checking {f.name} ---")
        try:
            with zipfile.ZipFile(f, 'r') as z:
                # find lang files
                langs = [n for n in z.namelist() if "lang/" in n and n.endswith(".json")]
                print("Found lang files:", langs)
                if langs:
                    en_lang = [n for n in langs if "en_us.json" in n]
                    if en_lang:
                        data = json.loads(z.read(en_lang[0]).decode('utf-8'))
                        print(f"Sample 5 keys from {en_lang[0]}:")
                        for k in list(data.keys())[:5]:
                            print(f"  '{k}': '{data[k]}'")
        except Exception as e:
            print(f"Error: {e}")

inspect_jar_lang("Medieval")
inspect_jar_lang("PassiveSkillTree")
inspect_jar_lang("simplyswords")
