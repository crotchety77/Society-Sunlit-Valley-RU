import os, json, re, sys

sys.stdout.reconfigure(encoding='utf-8')

workspace = r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода'
game_assets = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets'
desc_file = os.path.join(workspace, 'tasks', '25_books_puffish_skills', 'description_books')

# 1. Parse description_books file
content = open(desc_file, 'r', encoding='utf-8').read()

# Cut off any ignore sections at the bottom
if '[!!!]' in content:
    content = content.split('[!!!]')[0]

# Strip markdown backticks
content = re.sub(r'```[\s\S]*?```', lambda m: m.group(0).replace('```', ''), content)

# Regex to find blocks: "society:<book_id>\n<content until next society: or end>"
pattern = r'(society:[a-z0-9_]+)\n([\s\S]*?)(?=(?:society:[a-z0-9_]+|$))'
matches = re.findall(pattern, content)

parsed_entries = {}
for book_full_id, raw_body in matches:
    book_id = book_full_id.split(':')[1]
    body = raw_body.strip()
    
    # Filter out empty or commented entries
    if not body or body.startswith('#') or body.startswith('//'):
        continue
    
    # Split paragraphs by 2 or more newlines
    paragraphs = [p.strip() for p in re.split(r'\n\s*\n', body) if p.strip()]
    
    formatted_paragraphs = []
    for idx, p in enumerate(paragraphs):
        # Format internal newlines
        lines = [line.strip() for line in p.split('\n') if line.strip() and not line.strip().startswith('#')]
        if not lines:
            continue
        joined = "\n".join(lines)
        
        # If it's a "Способ получения" or "Другие способы" paragraph, ensure dark gray styling if not starting with color
        if idx > 0 and not joined.startswith('§'):
            joined = f"§8{joined}"
        formatted_paragraphs.append(joined)
        
    if not formatted_paragraphs:
        continue
        
    final_text = "\n\n".join(formatted_paragraphs)
    if not final_text.endswith('§r'):
        final_text += "§r"
        
    parsed_entries[book_id] = final_text

print(f"📖 Распарсено {len(parsed_entries)} шаблонов из description_books:")
for b_id, txt in parsed_entries.items():
    print(f"\n--- [{b_id}] ---")
    print(repr(txt))

# 2. Update project files
soc_proj = os.path.join(workspace, 'translations', 'society', 'ru_ru.json')
skills_proj = os.path.join(workspace, 'translations', 'skills', 'ru_ru.json')

with open(soc_proj, 'r', encoding='utf-8') as f: soc_data = json.load(f)
with open(skills_proj, 'r', encoding='utf-8') as f: skills_data = json.load(f)

for b_id, desc in parsed_entries.items():
    soc_data[f"item.society.{b_id}.description"] = desc
    skills_data[f"society_skills.books.{b_id}.description"] = desc

with open(soc_proj, 'w', encoding='utf-8') as f: json.dump(soc_data, f, ensure_ascii=False, indent=2)
with open(skills_proj, 'w', encoding='utf-8') as f: json.dump(skills_data, f, ensure_ascii=False, indent=2)

# 3. Update game files directly
soc_game = os.path.join(game_assets, 'society', 'lang', 'ru_ru.json')
skills_game = os.path.join(game_assets, 'society_skills', 'lang', 'ru_ru.json')

with open(soc_game, 'r', encoding='utf-8') as f: g_soc = json.load(f)
with open(skills_game, 'r', encoding='utf-8') as f: g_skills = json.load(f)

for b_id, desc in parsed_entries.items():
    g_soc[f"item.society.{b_id}.description"] = desc
    g_skills[f"society_skills.books.{b_id}.description"] = desc

with open(soc_game, 'w', encoding='utf-8') as f: json.dump(g_soc, f, ensure_ascii=False, indent=2)
with open(skills_game, 'w', encoding='utf-8') as f: json.dump(g_skills, f, ensure_ascii=False, indent=2)

print("\n" + "=" * 60)
print("🔍 ВЕРИФИКАЦИЯ: ПРЯМОЕ ЧТЕНИЕ ИЗ ФАЙЛОВ ИГРЫ (MODRINTH):")
print("=" * 60)
for b_id in parsed_entries.keys():
    print(f"[Game Skills] society_skills.books.{b_id}.description:\n{g_skills.get(f'society_skills.books.{b_id}.description')}")
print("=" * 60)
