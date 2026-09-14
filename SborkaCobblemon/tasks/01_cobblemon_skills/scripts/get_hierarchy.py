import os

base_path = r"c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\SborkaCobblemon\tasks\01_cobblemon_skills\docs\next_level_research\disassembled"

def get_class_hierarchy():
    classes = [
        "StationBaseBlockEntity",
        "GardeningStationBlockEntity",
        "RanchingStationBlockEntity",
        "CraftStationBlockEntity",
        "MysteryMineBlockEntity",
        "EnergyPylonBlockEntity",
        "CrystalBallBlockEntity"
    ]
    
    for c in classes:
        fp = os.path.join(base_path, f"io.github.chakyl.cobblemonfarmers.blockentity.{c}.javap.txt")
        if os.path.exists(fp):
            with open(fp, "r", encoding="utf-8") as f:
                first_few = [f.readline() for _ in range(5)]
                print(f"Class: {c}")
                for line in first_few:
                    if "class " in line:
                        print("  " + line.strip())

get_class_hierarchy()
