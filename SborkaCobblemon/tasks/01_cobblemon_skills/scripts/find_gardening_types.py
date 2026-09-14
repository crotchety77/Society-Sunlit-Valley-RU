import os

base_path = r"c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\SborkaCobblemon\tasks\01_cobblemon_skills\docs\next_level_research\disassembled"

def search_text(filename, keyword):
    fp = os.path.join(base_path, f"{filename}.javap.txt")
    with open(fp, "r", encoding="utf-8") as f:
        text = f.read()
    print(f"=== {filename} matches for '{keyword}' ===")
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if keyword.lower() in line.lower():
            start = max(0, i-5)
            end = min(len(lines), i+15)
            print("\n".join(lines[start:end]))
            print("-" * 40)

search_text("io.github.chakyl.cobblemonfarmers.utils.ElementalTypeUtils", "gardening")
search_text("io.github.chakyl.cobblemonfarmers.utils.ElementalTypeUtils", "flying")
search_text("io.github.chakyl.cobblemonfarmers.blockentity.GardeningStationBlockEntity", "flying")
search_text("io.github.chakyl.cobblemonfarmers.blockentity.GardeningStationBlockEntity", "harvest")
