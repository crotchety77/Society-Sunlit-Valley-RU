import os
import zipfile
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
jar_path = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\mods\puffish_skills-0.16.1-1.20-forge.jar"

with zipfile.ZipFile(jar_path, 'r') as z:
    for n in z.namelist():
        if 'skillsmod/commands' in n or 'SkillsMod' in n:
            raw = z.read(n).decode('latin1', errors='ignore')
            # Look for constant strings in bytecode
            # (Strings in JVM class file format)
            matches = re.findall(r'[\x01-\x1f]([a-z_]{2,30})[\x01-\x1f]', raw)
            print(f"=== {n} ===")
            print(set(matches))
