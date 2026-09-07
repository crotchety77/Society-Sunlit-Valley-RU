import re

p = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\config\ftbquests\quests\chapters\iii__advanced_farming.snbt'
with open(p + '.bak', 'r', encoding='utf-8') as f:
    txt = f.read()

# Let's find all occurrences of 263CCA4D2EAF2629
for m in re.finditer(r'id:\s*\"263CCA4D2EAF2629\"', txt):
    print(f"Match at {m.start()}:")
    print(txt[max(0, m.start() - 300):min(len(txt), m.end() + 300)])
    print("=" * 60)
