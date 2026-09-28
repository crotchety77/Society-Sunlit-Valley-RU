import re

with open('game_data/startup_scripts/globalFurniturePlushies.js', encoding='utf-8') as f:
    text = f.read()

loot_match = re.search(r'global\.lootFurniture\s*=\s*\[(.*?)\];', text, re.DOTALL)
plush_match = re.search(r'global\.originalPlushies\s*=\s*\[(.*?)\];', text, re.DOTALL)

loot = [x.strip(' "\',') for x in loot_match.group(1).splitlines() if x.strip(' "\',')]
plush = [x.strip(' "\',') for x in plush_match.group(1).splitlines() if x.strip(' "\',')]
adv_plush = [p.split(':')[0] + ':adv_' + p.split(':')[1] for p in plush]

overlap = set(adv_plush).intersection(set(loot))
print(f"Overlap between plushies and lootFurniture: {overlap}")
print(f"Total loot furniture count: {len(loot)}")
print(f"Total plushies count: {len(adv_plush)}")
