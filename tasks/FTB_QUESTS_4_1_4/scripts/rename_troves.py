import os
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def update_file(path, replacements):
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return 0
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    count = 0
    for k, v in list(data.items()):
        new_v = v
        for old, new in replacements:
            if isinstance(new_v, str) and old in new_v:
                new_v = new_v.replace(old, new)
        if new_v != v:
            data[k] = new_v
            count += 1
            print(f"[{os.path.basename(path)}] {k}:")
            print(f"  - {repr(v)}")
            print(f"  + {repr(new_v)}")
            
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return count

def main():
    # Target item name updates
    society_replacements = [
        ("Сундук с реликвиями", "Тайник с магическими реликвиями"),
        ("Сундук с артефактами", "Тайник с сокровищами"),
        ("Сундуков реликвий и артефактов", "Тайников с магическими реликвиями и Тайников с сокровищами"),
        ("сундуки с реликвиями и артефактами", "тайники с магическими реликвиями и сокровищами"),
        ("Тайника реликвий", "Тайника с магическими реликвиями"),
        ("Экстрактинатора", "Раскалывателя жеод"),
    ]

    skills_replacements = [
        ("§6Сундук с реликвиями§7", "§6Тайник с магическими реликвиями§7"),
        ("Сундук с реликвиями", "Тайник с магическими реликвиями"),
        ("§6Сундук с артефактами§7", "§6Тайник с сокровищами§7"),
        ("Сундук с артефактами", "Тайник с сокровищами"),
        ("Сундуков реликвий и артефактов", "Тайников с магическими реликвиями и Тайников с сокровищами"),
        ("сундуки с реликвиями и артефактами", "тайники с магическими реликвиями и сокровищами"),
    ]

    quests_replacements = [
        ("&6сундуки с реликвиями&r", "&6тайники с магическими реликвиями&r"),
        ("сундуки с реликвиями", "тайники с магическими реликвиями"),
        ("сундук с реликвиями", "тайник с магическими реликвиями"),
        ("сундук с артефактами", "тайник с сокровищами"),
        ("сундуки с артефактами", "тайники с сокровищами"),
    ]

    files_map = [
        (r'translations/society/ru_ru.json', society_replacements),
        (r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\society\lang\ru_ru.json', society_replacements),
        (r'translations/skills/ru_ru.json', skills_replacements),
        (r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\society_skills\lang\ru_ru.json', skills_replacements),
        (r'translations/ftbquests/ru_ru.json', quests_replacements),
        (r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\ftbquestlocalizer\lang\ru_ru.json', quests_replacements),
    ]

    total_updated = 0
    for fp, repls in files_map:
        total_updated += update_file(fp, repls)

    print(f"\nTotal entries updated across all files: {total_updated}")

if __name__ == '__main__':
    main()
