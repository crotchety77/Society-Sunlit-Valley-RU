import os
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

ROOT = r"c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода"
GAME_ASSETS = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets"

items = [
    "minecraft:coal",
    "minecraft:copper_ingot",
    "minecraft:iron_ingot",
    "create:zinc_ingot",
    "minecraft:gold_ingot",
    "minecraft:redstone",
    "minecraft:flint_and_steel",
    "society:iron_upgrade_smithing_template",
    "society:gold_upgrade_smithing_template",
    "society:diamond_upgrade_smithing_template",
    "minecraft:netherite_upgrade_smithing_template",
    "society:geode_buster",
    "extractinator:extractinator",
    "create:brown_toolbox",
    "refurbished_furniture:workbench",
    "furniture:bin",
    "society:moon_statue",
    "buildinggadgets2:gadget_core",
    "justhammers:small_core",
    "justhammers:impact_core",
]

# 1. Check addTooltips.js for each item
tooltips_file = os.path.join(ROOT, "game_data/client_scripts/tooltips/addTooltips.js")
with open(tooltips_file, "r", encoding="utf-8") as f:
    tt_content = f.read()

print("=== 1. ПРОВЕРКА ПОДСКАЗОК В addTooltips.js ===")
for item in items:
    if f'"{item}"' in tt_content or f"'{item}'" in tt_content:
        print(f"✅ {item} найден в addTooltips.js")
        # Extract snippet
        idx = tt_content.find(f'"{item}"')
        if idx == -1:
            idx = tt_content.find(f"'{item}'")
        snippet = tt_content[max(0, idx-50):min(len(tt_content), idx+250)]
        print("   Snippet:", snippet.replace('\n', ' '))
    else:
        print(f"⚪ {item} нет в addTooltips.js")

# 2. Check translation keys in all relevant files
print("\n=== 2. ПРОВЕРКА ЯЗЫКОВЫХ КЛЮЧЕЙ ===")
for item in items:
    ns, name = item.split(":")
    print(f"\n[{item}]")
    
    # Check society ru_ru
    soc_ru = json.load(open(os.path.join(ROOT, "translations/society/ru_ru.json"), encoding="utf-8"))
    soc_en = json.load(open(os.path.join(ROOT, "translations/society/en_us.json"), encoding="utf-8"))
    
    # Mod files
    mod_ru_path = os.path.join(ROOT, f"translations/mods/{ns}.json")
    mod_ru = json.load(open(mod_ru_path, encoding="utf-8")) if os.path.exists(mod_ru_path) else {}
    
    # Game files
    game_ru_path = os.path.join(GAME_ASSETS, f"{ns}/lang/ru_ru.json")
    game_ru = json.load(open(game_ru_path, encoding="utf-8")) if os.path.exists(game_ru_path) else {}
    game_en_path = os.path.join(GAME_ASSETS, f"{ns}/lang/en_us.json")
    game_en = json.load(open(game_en_path, encoding="utf-8")) if os.path.exists(game_en_path) else {}
    
    # Look for item/block name keys
    keys_to_check = [
        f"item.{ns}.{name}",
        f"block.{ns}.{name}",
        f"item.{ns}.{name}.description",
        f"block.{ns}.{name}.description",
        f"tooltip.{ns}.{name}",
        f"tooltip.society.{name}",
    ]
    
    for k in keys_to_check:
        v_ru = soc_ru.get(k) or mod_ru.get(k) or game_ru.get(k)
        v_en = soc_en.get(k) or game_en.get(k)
        if v_ru or v_en:
            print(f"  Key: {k}")
            print(f"    EN: {v_en}")
            print(f"    RU: {v_ru}")
