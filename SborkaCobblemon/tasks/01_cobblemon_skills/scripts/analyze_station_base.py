import os

base_path = r"c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\SborkaCobblemon\tasks\01_cobblemon_skills\docs\next_level_research\disassembled"

def read_class(name):
    full_path = os.path.join(base_path, f"{name}.javap.txt")
    if os.path.exists(full_path):
        with open(full_path, "r", encoding="utf-8") as f:
            return f.read()
    return ""

# Analyze StationBaseBlockEntity
station_base = read_class("io.github.chakyl.cobblemonfarmers.blockentity.StationBaseBlockEntity")
poke_utils = read_class("io.github.chakyl.cobblemonfarmers.utils.PokeUtils")
abstract_menu = read_class("io.github.chakyl.cobblemonfarmers.screen.AbstractWorkerMenu")
gardening = read_class("io.github.chakyl.cobblemonfarmers.blockentity.GardeningStationBlockEntity")
ranching = read_class("io.github.chakyl.cobblemonfarmers.blockentity.RanchingStationBlockEntity")
craft = read_class("io.github.chakyl.cobblemonfarmers.blockentity.CraftStationBlockEntity")
mine = read_class("io.github.chakyl.cobblemonfarmers.blockentity.MysteryMineBlockEntity")
pylon = read_class("io.github.chakyl.cobblemonfarmers.blockentity.EnergyPylonBlockEntity")
ball = read_class("io.github.chakyl.cobblemonfarmers.blockentity.CrystalBallBlockEntity")

print("--- StationBaseBlockEntity Fields & Methods ---")
for line in station_base.splitlines():
    if "public " in line or "protected " in line or "private " in line or "static " in line:
        if "{" not in line and "Code:" not in line and "LineNumberTable:" not in line and not line.strip().startswith("//"):
            print(line.strip())

