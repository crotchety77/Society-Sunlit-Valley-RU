import os

dir1 = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\config\ftbquests\quests\chapters"
dir2 = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley (1)\config\ftbquests\quests\chapters"

for f in sorted(os.listdir(dir1)):
    if not f.endswith('.snbt'):
        continue
    p1 = os.path.join(dir1, f)
    p2 = os.path.join(dir2, f)
    s1 = os.path.getsize(p1)
    s2 = os.path.getsize(p2) if os.path.exists(p2) else -1
    diff = "DIFF" if s1 != s2 else "SAME"
    print(f"{f:<35} | Active: {s1:>6} | (1): {s2:>6} | {diff}")
