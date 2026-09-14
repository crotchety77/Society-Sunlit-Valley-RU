import os

base_path = r"c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\SborkaCobblemon\tasks\01_cobblemon_skills\docs\next_level_research\disassembled"

stations = [
    "GardeningStationBlockEntity",
    "RanchingStationBlockEntity",
    "CraftStationBlockEntity",
    "MysteryMineBlockEntity",
    "EnergyPylonBlockEntity",
    "CrystalBallBlockEntity"
]

def analyze_station(station_name):
    file_path = os.path.join(base_path, f"io.github.chakyl.cobblemonfarmers.blockentity.{station_name}.javap.txt")
    if not os.path.exists(file_path):
        return f"File {file_path} not found"
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    print(f"\n{'='*20} {station_name} {'='*20}")
    lines = content.splitlines()
    for line in lines:
        if "public " in line or "protected " in line or "private " in line or "void " in line or "boolean " in line or "double " in line or "int " in line:
            if "{" not in line and "Code:" not in line and "LineNumberTable:" not in line and not line.strip().startswith("//") and not line.strip().startswith("/*"):
                print(line.strip())

for s in stations:
    analyze_station(s)

