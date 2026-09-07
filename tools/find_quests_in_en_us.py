import json
import re

with open(r"c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\translations\ftbquests\en_us.json", 'r', encoding='utf-8') as f:
    en_us = json.load(f)

for qid in ["0A455A4E0D7D074E", "A455A4E0D7D074E", "17C8B0197B8636E7", "263CCA4D2EAF2629", "3DE36C9FBCB58800"]:
    matches = [k for k in en_us.keys() if qid.lower() in k.lower()]
    print(f"Matches for {qid}: {matches}")
