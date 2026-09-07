import json
import os
import re
import shutil

# 1. Update translations/society/ru_ru.json and en_us.json
ws_root = os.path.abspath(".")
ru_path = os.path.join(ws_root, "translations", "society", "ru_ru.json")
en_path = os.path.join(ws_root, "translations", "society", "en_us.json")

with open(ru_path, "r", encoding="utf-8") as f:
    ru_data = json.load(f)
ru_data["tooltip.society.diamond_heart.biomancy"] = "§7Может применяться §fБиомантами§7 в сельском хозяйстве, если у них прокачан соответствующий навык."

with open(ru_path, "w", encoding="utf-8") as f:
    json.dump(ru_data, f, ensure_ascii=False, indent=2)

with open(en_path, "r", encoding="utf-8") as f:
    en_data = json.load(f)
en_data["tooltip.society.diamond_heart.biomancy"] = "§7Can be used by §fBiomancers§7 in animal husbandry if they have unlocked the corresponding skill."

with open(en_path, "w", encoding="utf-8") as f:
    json.dump(en_data, f, ensure_ascii=False, indent=2)

print("Updated translations/society/ JSON files.")

# 2. Update workspace addTooltips.js
add_tooltips_ws = os.path.join(ws_root, "game_data", "client_scripts", "tooltips", "addTooltips.js")
with open(add_tooltips_ws, "r", encoding="utf-8") as f:
    c = f.read()

pattern = r'tooltip\.add\("quark:diamond_heart",\s*\[\s*Text\.of\([^\]]+\)\s*\]\);'
replacement = 'tooltip.add("quark:diamond_heart", [\n    Text.translatable("tooltip.society.diamond_heart.biomancy")\n  ]);'

c = re.sub(pattern, replacement, c)

with open(add_tooltips_ws, "w", encoding="utf-8") as f:
    f.write(c)

print("Updated addTooltips.js in workspace.")

# 3. Copy to game client_scripts
game_tooltips = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\client_scripts\tooltips\addTooltips.js"
shutil.copy2(add_tooltips_ws, game_tooltips)
print("Synced addTooltips.js to game profile.")

# 4. Copy to game assets/society/lang/
game_ru = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\society\lang\ru_ru.json"
game_en = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\society\lang\en_us.json"
shutil.copy2(ru_path, game_ru)
shutil.copy2(en_path, game_en)
print("Synced lang files to game profile.")

# 5. Verify physical files
with open(game_tooltips, "r", encoding="utf-8") as f:
    c_game = f.read()
    assert "Text.translatable(\"tooltip.society.diamond_heart.biomancy\")" in c_game
    print("[OK] Game addTooltips.js contains Text.translatable!")

with open(game_ru, "r", encoding="utf-8") as f:
    ru_game = json.load(f)
    assert ru_game.get("tooltip.society.diamond_heart.biomancy") == "§7Может применяться §fБиомантами§7 в сельском хозяйстве, если у них прокачан соответствующий навык."
    print("[OK] Game ru_ru.json contains exact translatable string:", ru_game["tooltip.society.diamond_heart.biomancy"])
