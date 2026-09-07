import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

fp = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\config\ftbquests\quests\chapters\getting_started.snbt'
with open(fp, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace title for quest 681EECD8B1D07F34
# Find block from id: "681EECD8B1D07F34" to the end of the object before the next quest
idx = content.find('id: "681EECD8B1D07F34"')
if idx != -1:
    end_idx = content.find('x: 4.5d', idx)
    block = content[idx:end_idx]
    block_fixed = re.sub(r'title:\s*"[^"]*"', 'title: "{ftbquests.chapter.getting_started.quest681EECD8B1D07F34.title}"', block)
    content = content[:idx] + block_fixed + content[end_idx:]

with open(fp, 'w', encoding='utf-8') as f:
    f.write(content)

print("Title for 681EECD8B1D07F34 restored to localization key!")
