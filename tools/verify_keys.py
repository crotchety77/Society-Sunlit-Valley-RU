import os
import json
import sys
import argparse

sys.stdout.reconfigure(encoding='utf-8')

GAME_ASSETS = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets'

NAMESPACES = {
    'society': 'society',
    'skills': 'society_skills',
    'society_skills': 'society_skills',
    'ftbquests': 'ftbquestlocalizer',
    'quests': 'ftbquestlocalizer',
    'ftbquestlocalizer': 'ftbquestlocalizer',
    'dialog': 'dialog',
    'dialogs': 'dialog',
    'blueprints': 'portable_blueprints',
    'portable_blueprints': 'portable_blueprints',
    'tips': 'society_tips',
    'society_tips': 'society_tips',
}

def verify_keys(namespace, keys):
    ns = NAMESPACES.get(namespace.lower(), namespace)
    target_file = os.path.join(GAME_ASSETS, ns, 'lang', 'ru_ru.json')
    
    if not os.path.exists(target_file):
        print(f"❌ Файл игры не найден: {target_file}")
        return False

    try:
        with open(target_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ Ошибка чтения {target_file}: {e}")
        return False

    print(f"====================================================")
    print(f"🔍 ВЕРИФИКАЦИЯ ФАЙЛА ИГРЫ: assets/{ns}/lang/ru_ru.json")
    print(f"====================================================")

    all_found = True
    for k in keys:
        if k in data:
            print(f"✅ [{k}] = {repr(data[k])}")
        else:
            print(f"❌ Ключ НЕ НАЙДЕН в файле игры: {k}")
            all_found = False

    return all_found

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Прямая верификация ключей в физических файлах игры")
    parser.add_argument("namespace", help="Пространство имён (society, skills, ftbquests, dialog, blueprints, tips)")
    parser.add_argument("keys", nargs="+", help="Один или несколько ключей локализации для проверки")

    args = parser.parse_args()
    verify_keys(args.namespace, args.keys)
