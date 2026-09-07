import os
import re

cur = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\config\ftbquests\quests\chapters\iii__advanced_farming.snbt"
with open(cur, 'r', encoding='utf-8') as f:
    cur_text = f.read()

cur_quests = re.findall(r'id:\s*"([0-9A-Fa-f]+)"', cur_text)
print(f"Current file size: {len(cur_text)} bytes")
print(f"Current quest/task/reward IDs count: {len(cur_quests)}")

# Verify 4 quests
for qid in ["0A455A4E0D7D074E", "17C8B0197B8636E7", "263CCA4D2EAF2629", "3DE36C9FBCB58800"]:
    if qid in cur_text:
        print(f"Found {qid} in active snbt")
    else:
        print(f"MISSING {qid}")
