import subprocess
import zipfile
import re

jar_path = r'G:\curseforge\minecraft\Instances\Society Sunlit Cobblemon\mods\cobblemon_farmers-2.4-all.jar'

with zipfile.ZipFile(jar_path, 'r') as z:
    classes = [name[:-6].replace('/', '.') for name in z.namelist() if name.endswith('.class')]

print(f"Total classes: {len(classes)}")

for cls in classes:
    res = subprocess.run(['javap', '-p', '-c', '-constants', '-cp', jar_path, cls], capture_output=True, text=True)
    out = res.stdout
    if 'getShiny' in out or 'isShiny' in out:
        print(f"\n[FOUND SHINY USAGE] in {cls}")
        lines = out.splitlines()
        for idx, line in enumerate(lines):
            if 'getShiny' in line or 'isShiny' in line:
                for c in range(max(0, idx-5), min(len(lines), idx+10)):
                    print(f"  {lines[c]}")
                print("  ---")
