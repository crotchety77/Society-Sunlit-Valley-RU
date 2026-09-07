import json
import os

untranslated_path = os.path.join(os.path.dirname(__file__), 'untranslated_lines.json')
with open(untranslated_path, 'r', encoding='utf-8') as f:
    untranslated_by_file = json.load(f)

# Collect all keys and English text
all_remaining = {}
for fname, kdict in untranslated_by_file.items():
    for k, v in kdict.items():
        all_remaining[k] = v

print(f"Total keys to map: {len(all_remaining)}")

# Generate dictionary file
with open(os.path.join(os.path.dirname(__file__), 'all_remaining_en.json'), 'w', encoding='utf-8') as f:
    json.dump(all_remaining, f, ensure_ascii=False, indent=2)
