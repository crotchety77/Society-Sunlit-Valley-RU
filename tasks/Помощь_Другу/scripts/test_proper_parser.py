import re
from pathlib import Path

base_path = Path(r"G:\curseforge\minecraft\Instances\Cisco's Fantasy Medieval RPG [Dragonfyre]")
ch = base_path / "config" / "ftbquests" / "quests" / "chapters" / "divine_equipment.snbt"
text = ch.read_text(encoding="utf-8")

def parse_quests_properly(snbt_text):
    # Находим блок quests: [ ... ]
    # Учитываем, что внутри квестов есть вложенные массивы [ ... ] и объекты { ... }
    m = re.search(r'quests:\s*\[', snbt_text)
    if not m:
        return []
    
    start_idx = m.end()
    # Идем по символам, считая уровень вложенности
    depth = 1
    i = start_idx
    quests_content = ""
    while i < len(snbt_text) and depth > 0:
        c = snbt_text[i]
        if c == '[':
            depth += 1
        elif c == ']':
            depth -= 1
        i += 1
    
    quests_content = snbt_text[start_idx:i-1]
    
    # Теперь разбиваем quests_content на отдельные объекты верхнего уровня { ... }
    quests = []
    in_quest = False
    brace_depth = 0
    curr_quest = []
    
    in_string = False
    escape = False
    
    for char in quests_content:
        if escape:
            curr_quest.append(char)
            escape = False
            continue
        if char == '\\':
            curr_quest.append(char)
            escape = True
            continue
        if char == '"':
            in_string = not in_string
            curr_quest.append(char)
            continue
            
        if not in_string:
            if char == '{':
                brace_depth += 1
                if brace_depth == 1:
                    curr_quest = ['{']
                    continue
            elif char == '}':
                brace_depth -= 1
                if brace_depth == 0:
                    curr_quest.append('}')
                    quests.append("".join(curr_quest))
                    curr_quest = []
                    continue
                    
        if brace_depth > 0:
            curr_quest.append(char)
            
    return quests

raw_q = parse_quests_properly(text)
print(f"Properly extracted {len(raw_q)} quests from divine_equipment.snbt:")
for idx, q in enumerate(raw_q, 1):
    qid = re.search(r'\bid:\s*"([A-F0-9]+)"', q)
    title = re.search(r'\btitle:\s*"([^"]*)"', q)
    sub = re.search(r'\bsubtitle:\s*"([^"]*)"', q)
    desc = re.search(r'\bdescription:\s*\[(.*?)\]', q, re.DOTALL)
    print(f"Quest {idx}: ID={qid.group(1) if qid else None}, title='{title.group(1) if title else None}', subtitle='{sub.group(1) if sub else None}', has_desc={bool(desc)}")
