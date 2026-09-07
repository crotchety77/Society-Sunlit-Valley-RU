import os
import json
import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода'
game_dir = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets'

def update_file(path, replacements):
    if not os.path.exists(path):
        return
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    modified = 0
    for k, v in data.items():
        if isinstance(v, str):
            orig = v
            # Apply specific dictionary of exact sentence/term replacements
            for old, new in replacements.items():
                if old in v:
                    v = v.replace(old, new)
            if v != orig:
                data[k] = v
                modified += 1
                
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"[{os.path.basename(path)}] Updated {modified} entries in {path}")

# Accurate, context-aware replacements
replacements = {
    "Рыбный садок": "Рыбный пруд",
    "рыбный садок": "рыбный пруд",
    "Рыбного садка": "Рыбного пруда",
    "рыбного садка": "рыбного пруда",
    "Рыбных садках": "Рыбных прудах",
    "рыбных садках": "рыбных прудах",
    "Рыбных садков": "Рыбных прудов",
    "рыбных садков": "рыбных прудов",
    "Рыбные садки": "Рыбные пруды",
    "рыбные садки": "рыбные пруды",
    "Рыбному садку": "Рыбному пруду",
    "рыбному садку": "рыбному пруду",
    "Рыбным садком": "Рыбным прудом",
    "рыбным садком": "рыбным прудом",
    
    # Standalone forms in fishing context
    "из садков": "из прудов",
    "из садка": "из пруда",
    "позади садка": "позади пруда",
    "для садков": "для прудов",
    "в садках": "в прудах",
    "в садке": "в пруду",
    "популяции садка": "популяции пруда",
    "популяция садка": "популяция пруда",
    "Блок рыбного садка": "Блок рыбного пруда",
    "Корзина для рыбного садка": "Корзина для рыбного пруда",
    "Рыбного Садка": "Рыбного Пруда",
    "Рыбном садке": "Рыбном пруде",
    "Рыбном Садке": "Рыбном Пруде"
}

# 1. Update translations/
update_file(os.path.join(base_dir, 'translations', 'society', 'ru_ru.json'), replacements)
update_file(os.path.join(base_dir, 'translations', 'skills', 'ru_ru.json'), replacements)
update_file(os.path.join(base_dir, 'translations', 'ftbquests', 'ru_ru.json'), replacements)

# 2. Update game files directly
update_file(os.path.join(game_dir, 'society', 'lang', 'ru_ru.json'), replacements)
update_file(os.path.join(game_dir, 'society_skills', 'lang', 'ru_ru.json'), replacements)
update_file(os.path.join(game_dir, 'ftbquestlocalizer', 'lang', 'ru_ru.json'), replacements)

# 3. Sync all
subprocess.run(['node', os.path.join(base_dir, 'sync_all_to_game.js')], cwd=base_dir)

print("\n=== ВЕРИФИКАЦИЯ ПРЯМО ИЗ ФАЙЛОВ ИГРЫ ===")
soc = json.load(open(os.path.join(game_dir, 'society', 'lang', 'ru_ru.json'), encoding='utf-8'))
print("block.society.fish_pond ->", soc.get("block.society.fish_pond"))
print("block.society.fish_pond_basket ->", soc.get("block.society.fish_pond_basket"))
print("block.society.fish_pond_manager.description ->", soc.get("block.society.fish_pond_manager.description"))
print("item.society.bullfish_jobs.description ->", repr(soc.get("item.society.bullfish_jobs.description")[:70]))

sk = json.load(open(os.path.join(game_dir, 'society_skills', 'lang', 'ru_ru.json'), encoding='utf-8'))
print("society.skills.fishing.scum_collector.description ->", repr(sk.get("society.skills.fishing.scum_collector.description")[-65:]))
print("society.skills.fishing.mitosis.description ->", repr(sk.get("society.skills.fishing.mitosis.description")[:65]))

ftb = json.load(open(os.path.join(game_dir, 'ftbquestlocalizer', 'lang', 'ru_ru.json'), encoding='utf-8'))
print("quest6FE9F992ACD90629.description1 ->", ftb.get("ftbquests.chapter.ii__building_up_the_farm.quest6FE9F992ACD90629.description1")[:80])
print("quest42B424793E1E91D3.description1 ->", ftb.get("ftbquests.chapter.iv__prismatic_farming.quest42B424793E1E91D3.description1")[:80])
