import os, zipfile, sys

sys.stdout.reconfigure(encoding='utf-8')
jar_path = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\mods\puffish_skills-0.16.1-1.20-forge.jar"

with zipfile.ZipFile(jar_path, 'r') as z:
    for cls in ['PointsCommand.class', 'ExperienceCommand.class', 'SkillsCommand.class', 'CategoryCommand.class']:
        for n in z.namelist():
            if n.endswith(cls):
                raw = z.read(n)
                s = ""
                strs = []
                for b in raw:
                    if 32 <= b <= 126:
                        s += chr(b)
                    else:
                        if len(s) >= 2:
                            strs.append(s)
                        s = ""
                print(f"=== {cls} ===")
                print(strs)
