import re

src = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley (1)\config\ftbquests\quests\chapters\iii__advanced_farming.snbt"
cur = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\config\ftbquests\quests\chapters\iii__advanced_farming.snbt"

with open(src, 'r', encoding='utf-8') as f:
    src_text = f.read()

# Let's find all quest blocks in src:
# Quests usually have `id: "HEX"`
print("=== Quests in original src (first 10): ===")
for m in re.finditer(r'id:\s*"([0-9A-Fa-f]+)"', src_text):
    print(m.group(1))

print("\nSearching 263CCA4D2EAF2629 case-insensitively:")
m = re.search(r'263cca4d2eaf2629', src_text, re.IGNORECASE)
print(m)

print("\nSearching 3DE36C9FBCB58800:")
m2 = re.search(r'3de36c9fbcb58800', src_text, re.IGNORECASE)
print(m2)
