import os

base_path = r"c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\SborkaCobblemon\tasks\01_cobblemon_skills\docs\next_level_research\disassembled"

fp = os.path.join(base_path, "io.github.chakyl.cobblemonfarmers.blockentity.GardeningStationBlockEntity.javap.txt")
with open(fp, "r", encoding="utf-8") as f:
    text = f.read()

def print_method(name):
    lines = text.splitlines()
    in_m = False
    print(f"=== {name} ===")
    for line in lines:
        if f" {name}(" in line:
            in_m = True
            print(line)
            continue
        if in_m:
            if line.startswith("  public ") or line.startswith("  private ") or line.startswith("  protected "):
                break
            print(line)

print_method("runAction")
print_method("getScalingStat")
print_method("getActionTime")
print_method("fetchAoeRadius")
