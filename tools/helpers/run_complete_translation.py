import json
import os
import re

review_dir = os.path.join(os.path.dirname(__file__), '..', 'dialogs_review')
untranslated_path = os.path.join(os.path.dirname(__file__), 'untranslated_lines.json')

with open(untranslated_path, 'r', encoding='utf-8') as f:
    untranslated_by_file = json.load(f)

def update_md(file_name, translations):
    file_path = os.path.join(review_dir, file_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('|') and '`dialog.npc.' in stripped:
            parts = line.split('|')
            if len(parts) >= 5:
                match = re.search(r'`([^`]+)`', parts[1])
                if match:
                    key = match.group(1)
                    if key in translations and translations[key]:
                        parts[3] = f" {translations[key]} "
                        line = "|".join(parts)
        new_lines.append(line)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print(f"Updated {file_name}")

with open(os.path.join(os.path.dirname(__file__), 'all_remaining_en.json'), 'r', encoding='utf-8') as f:
    all_en = json.load(f)

print(f"Translating {len(all_en)} keys...")
