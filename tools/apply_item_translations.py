import os
import json
import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')

def update_json_file(filepath, updates):
    if not os.path.exists(filepath):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        data = {}
    else:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    
    for k, v in updates.items():
        data[k] = v
        
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Updated {len(updates)} keys in: {filepath}")

def main():
    base_dir = r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода'
    game_assets = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets'
    
    # 1. Society items
    society_updates = {
        "item.society.red_wrench": "Красный гаечный ключ",
        "item.society.ancient_builders_tool": "Древний инструмент строителя",
        "block.society.drum_cornucopia": "Барабан изобилия",
        "block.society.fish_pond_manager": "Менеджер рыбного пруда"
    }
    update_json_file(os.path.join(base_dir, 'translations', 'society', 'ru_ru.json'), society_updates)
    update_json_file(os.path.join(game_assets, 'society', 'lang', 'ru_ru.json'), society_updates)
    
    # 2. Bakery items
    bakery_updates = {
        "item.bakery.waffle": "Вафля"
    }
    update_json_file(os.path.join(game_assets, 'bakery', 'lang', 'ru_ru.json'), bakery_updates)
    
    # 3. Longwings items
    longwings_updates = {
        "item.longwings.butterfly": "Бабочка",
        "item.longwings.moth": "Мотылёк"
    }
    update_json_file(os.path.join(game_assets, 'longwings', 'lang', 'ru_ru.json'), longwings_updates)
    
    # 4. Sync all to game
    subprocess.run(['node', os.path.join(base_dir, 'sync_all_to_game.js')], cwd=base_dir)
    
    # 5. Direct verification from game assets
    print("\n=== ВЕРИФИКАЦИЯ ИЗ ФАЙЛОВ ИГРЫ ===")
    soc_game = json.load(open(os.path.join(game_assets, 'society', 'lang', 'ru_ru.json'), encoding='utf-8'))
    for k in society_updates:
        print(f"[society] {k} -> {soc_game.get(k)}")
        
    bak_game = json.load(open(os.path.join(game_assets, 'bakery', 'lang', 'ru_ru.json'), encoding='utf-8'))
    for k in bakery_updates:
        print(f"[bakery] {k} -> {bak_game.get(k)}")
        
    lw_game = json.load(open(os.path.join(game_assets, 'longwings', 'lang', 'ru_ru.json'), encoding='utf-8'))
    for k in longwings_updates:
        print(f"[longwings] {k} -> {lw_game.get(k)}")

if __name__ == '__main__':
    main()
