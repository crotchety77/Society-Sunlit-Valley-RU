import os
import re

chapters_dir = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley (1)\config\ftbquests\quests\chapters"

for f in os.listdir(chapters_dir):
    if not f.endswith('.snbt'):
        continue
    path = os.path.join(chapters_dir, f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if "263CCA4D2EAF2629" in content:
        print(f"Found 263CCA4D2EAF2629 in {f}")
    if "3DE36C9FBCB58800" in content:
        print(f"Found 3DE36C9FBCB58800 in {f}")
    if "0A455A4E0D7D074E" in content:
        print(f"Found 0A455A4E0D7D074E in {f}")
    if "17C8B0197B8636E7" in content:
        print(f"Found 17C8B0197B8636E7 in {f}")
