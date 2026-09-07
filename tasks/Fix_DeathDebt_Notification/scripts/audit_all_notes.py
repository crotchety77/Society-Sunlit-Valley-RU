import json
import sys
from pathlib import Path

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

WORKSPACE = Path(r"c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода")
RU_JSON = WORKSPACE / "translations" / "society" / "ru_ru.json"
EN_JSON = WORKSPACE / "translations" / "society" / "en_us.json"

with open(RU_JSON, "r", encoding="utf-8") as f:
    ru_dict = json.load(f)

with open(EN_JSON, "r", encoding="utf-8") as f:
    en_dict = json.load(f)

note_keys = [
    "society.starting_item_sharestone.title",
    "society.starting_item_sharestone.author",
    "society.starting_item_sharestone.text",
    "society.skull_cavern.intro.note.title",
    "society.skull_cavern.intro.note.author",
    "society.skull_cavern.intro.note",
    "society.shipping_bin.debt_paid_note.title",
    "society.shipping_bin.debt_paid_note",
    "society.hospital_receipt.title",
    "society.hospital_receipt.author",
    "society.hospital_receipt.first_death.title",
    "society.hospital_receipt.note.free",
    "society.hospital_receipt.note.paid",
    "society.hospital_receipt.note.debt"
]

print("="*60)
print("AUDIT OF ALL NOTE PAPER TRANSLATIONS IN THE GAME")
print("="*60)

for k in note_keys:
    ru_val = ru_dict.get(k, "<MISSING>")
    en_val = en_dict.get(k, "<MISSING>")
    print(f"\n🔑 KEY: {k}")
    print(f"🇷🇺 RU:\n{ru_val}")
    print(f"🇬🇧 EN:\n{en_val}")
    print("-" * 40)
