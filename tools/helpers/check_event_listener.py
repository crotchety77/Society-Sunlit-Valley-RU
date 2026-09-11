import os
import zipfile
import sys

sys.stdout.reconfigure(encoding='utf-8')
jar_path = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\mods\puffish_skills-0.16.1-1.20-forge.jar"

with zipfile.ZipFile(jar_path, 'r') as z:
    for n in z.namelist():
        if 'EventListener' in n:
            raw = z.read(n)
            # Find all ASCII strings
            s = ""
            strs = []
            for b in raw:
                if 32 <= b <= 126:
                    s += chr(b)
                else:
                    if len(s) >= 2:
                        strs.append(s)
                    s = ""
            print("EventListener strings:", strs)
