import re

act = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\config\ftbquests\quests\chapters\getting_started.snbt"
ref = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley (1)\config\ftbquests\quests\chapters\getting_started.snbt"

with open(act, 'r', encoding='utf-8') as f:
    act_ids = set(re.findall(r'id:\s*"([0-9A-Fa-f]+)"', f.read()))

with open(ref, 'r', encoding='utf-8') as f:
    ref_ids = set(re.findall(r'id:\s*"([0-9A-Fa-f]+)"', f.read()))

print("In reference but not in active 4.1.4:", len(ref_ids - act_ids))
print("In active 4.1.4 but not in reference:", len(act_ids - ref_ids))
