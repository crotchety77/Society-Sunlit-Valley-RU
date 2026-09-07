import re

with open(r"D:\ModrinthApp\profiles\Society_ Sunlit Valley (1)\config\ftbquests\quests\chapters\iii__advanced_farming.snbt", 'r', encoding='utf-8') as f:
    text = f.read()

# Let's find all quests in text
# Each quest starts with \t\t{\n or {\n
quests = []
# split by \t\t{\n
raw_blocks = text.split("\t\t{\n")
print(f"Total raw blocks: {len(raw_blocks)}")

for i, b in enumerate(raw_blocks[1:], 1):
    id_m = re.search(r'id:\s*"([0-9A-Fa-f]+)"', b)
    title_m = re.search(r'title:\s*"([^"]+)"', b)
    qid = id_m.group(1) if id_m else "NO_ID"
    title = title_m.group(1) if title_m else ""
    if "butterfly" in b.lower() or "caterpillar" in b.lower() or "3b6640956f047ec8" in b.lower():
        print(f"Quest {i}: ID={qid}, Title={title}")
        print(b[:300])
        print("...")
