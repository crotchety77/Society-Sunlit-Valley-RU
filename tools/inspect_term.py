import os
import json
import sys
import argparse

sys.stdout.reconfigure(encoding='utf-8')

PROJECT_TRANSLATIONS = r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\translations'

FILES_TO_INSPECT = [
    ('society', os.path.join(PROJECT_TRANSLATIONS, 'society', 'ru_ru.json'), os.path.join(PROJECT_TRANSLATIONS, 'society', 'en_us.json')),
    ('skills', os.path.join(PROJECT_TRANSLATIONS, 'skills', 'ru_ru.json'), os.path.join(PROJECT_TRANSLATIONS, 'skills', 'en_us.json')),
    ('ftbquests', os.path.join(PROJECT_TRANSLATIONS, 'ftbquests', 'ru_ru.json'), os.path.join(PROJECT_TRANSLATIONS, 'ftbquests', 'en_us.json')),
    ('dialogs', os.path.join(PROJECT_TRANSLATIONS, 'dialogs', 'ru_ru.json'), os.path.join(PROJECT_TRANSLATIONS, 'dialogs', 'en_us.json')),
    ('buildings', os.path.join(PROJECT_TRANSLATIONS, 'buildings', 'ru_ru.json'), os.path.join(PROJECT_TRANSLATIONS, 'buildings', 'en_us.json')),
    ('tips', os.path.join(PROJECT_TRANSLATIONS, 'tips', 'ru_ru.json'), os.path.join(PROJECT_TRANSLATIONS, 'tips', 'en_us.json')),
]

def inspect_term(query, case_sensitive=False):
    print(f"====================================================")
    print(f"🔍 ИНСПЕКЦИЯ ТЕРМИНА / ID: '{query}'")
    print(f"====================================================")

    q = query if case_sensitive else query.lower()
    matches_found = 0

    for name, ru_path, en_path in FILES_TO_INSPECT:
        ru_data = {}
        en_data = {}
        if os.path.exists(ru_path):
            with open(ru_path, 'r', encoding='utf-8') as f:
                ru_data = json.load(f)
        if os.path.exists(en_path):
            with open(en_path, 'r', encoding='utf-8') as f:
                en_data = json.load(f)

        section_matches = []
        all_keys = set(ru_data.keys()).union(set(en_data.keys()))
        for k in all_keys:
            ru_val = str(ru_data.get(k, ''))
            en_val = str(en_data.get(k, ''))
            
            k_match = (q in k) if case_sensitive else (q in k.lower())
            ru_match = (q in ru_val) if case_sensitive else (q in ru_val.lower())
            en_match = (q in en_val) if case_sensitive else (q in en_val.lower())

            if k_match or ru_match or en_match:
                section_matches.append((k, en_val, ru_val))

        if section_matches:
            matches_found += len(section_matches)
            print(f"\n📂 [{name.upper()}] Найдено совпадений: {len(section_matches)}")
            for k, en_v, ru_v in section_matches[:8]:
                print(f"  • Ключ: {k}")
                if en_v:
                    print(f"    EN: {repr(en_v)}")
                print(f"    RU: {repr(ru_v)}")
            if len(section_matches) > 8:
                print(f"    ... и ещё {len(section_matches) - 8} совпадений.")

    if matches_found == 0:
        print(f"\nНичего не найдено по запросу '{query}'.")
    else:
        print(f"\nВсего найдено: {matches_found} вхождений.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Мгновенный поиск термина / ID по всем 6 пространствам имён")
    parser.add_argument("query", help="Текст, ключ или ID предмета для поиска")
    parser.add_argument("--case-sensitive", action="store_true", help="Учитывать регистр")

    args = parser.parse_args()
    inspect_term(args.query, args.case_sensitive)
