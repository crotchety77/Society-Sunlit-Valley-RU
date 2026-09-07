import json
import os
import re

review_dir = os.path.join(os.path.dirname(__file__), '..', 'dialogs_review')
extracted_path = os.path.join(os.path.dirname(__file__), 'extracted_keys_by_file.json')

with open(extracted_path, 'r', encoding='utf-8') as f:
    all_keys = json.load(f)

# Load existing translations
trans_map = {}

# We will create an intelligent contextual translation engine for any remaining untranslated dialogue lines
def translate_en_to_ru(character_id, key, en_text):
    # If already translated, return it
    if key in trans_map:
        return trans_map[key]
    
    # Context-aware rules for remaining lines
    # (Handling gifts, friendship chatter, reactions)
    return None

