import os
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

ROOT = r"c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода"
GAME_ASSETS = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets"

items = [
    ("minecraft:coal", "item.minecraft.coal"),
    ("minecraft:copper_ingot", "item.minecraft.copper_ingot"),
    ("minecraft:iron_ingot", "item.minecraft.iron_ingot"),
    ("create:zinc_ingot", "item.create.zinc_ingot"),
    ("minecraft:gold_ingot", "item.minecraft.gold_ingot"),
    ("minecraft:redstone", "item.minecraft.redstone"),
    ("minecraft:flint_and_steel", "item.minecraft.flint_and_steel"),
    ("society:iron_upgrade_smithing_template", "item.society.iron_upgrade_smithing_template"),
    ("society:gold_upgrade_smithing_template", "item.society.gold_upgrade_smithing_template"),
    ("society:diamond_upgrade_smithing_template", "item.society.diamond_upgrade_smithing_template"),
    ("minecraft:netherite_upgrade_smithing_template", "item.minecraft.netherite_upgrade_smithing_template"),
    ("society:geode_buster", "item.society.geode_buster"),
    ("extractinator:extractinator", "block.extractinator.extractinator"),
    ("create:brown_toolbox", "block.create.brown_toolbox"),
    ("refurbished_furniture:workbench", "block.refurbished_furniture.workbench"),
    ("furniture:bin", "block.furniture.bin"),
    ("society:moon_statue", "block.society.moon_statue"),
    ("buildinggadgets2:gadget_core", "item.buildinggadgets2.gadget_core"),
    ("justhammers:small_core", "item.justhammers.small_core"),
    ("justhammers:impact_core", "item.justhammers.impact_core"),
]

# Check translations in game and project
for item_id, default_key in items:
    ns = item_id.split(":")[0]
    name = item_id.split(":")[1]
    
    # Check tooltips in addTooltips.js
    print(f"--- {item_id} ---")
    
    # Check society ru_ru
    soc_ru = json.load(open(os.path.join(ROOT, "translations/society/ru_ru.json"), encoding="utf-8"))
    
    # Check mod ru
    mod_path = os.path.join(ROOT, f"translations/mods/{ns}.json")
    mod_ru = json.load(open(mod_path, encoding="utf-8")) if os.path.exists(mod_path) else {}
    
    game_mod_path = os.path.join(GAME_ASSETS, f"{ns}/lang/ru_ru.json")
    game_ru = json.load(open(game_mod_path, encoding="utf-8")) if os.path.exists(game_mod_path) else {}
    
    # Find matching keys
    found_keys = {}
    for d, src in [(soc_ru, "society"), (mod_ru, f"mod_{ns}"), (game_ru, f"game_{ns}")]:
        for k, v in d.items():
            if name in k or (default_key and k == default_key) or f"item.{ns}.{name}" in k or f"block.{ns}.{name}" in k:
                found_keys[k] = (v, src)
    
    for k, (v, src) in found_keys.items():
        print(f"  [{src}] {k} -> {v}")
    if not found_keys:
        print(f"  [!] No custom keys found (uses vanilla/default)")
