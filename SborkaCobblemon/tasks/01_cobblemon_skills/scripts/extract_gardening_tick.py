import os

base_path = r"c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\SborkaCobblemon\tasks\01_cobblemon_skills\docs\next_level_research\disassembled"

fp = os.path.join(base_path, "io.github.chakyl.cobblemonfarmers.blockentity.GardeningStationBlockEntity.javap.txt")
with open(fp, "r", encoding="utf-8") as f:
    text = f.read()

lines = text.splitlines()
in_tick = False
for line in lines:
    if "public void tick(" in line:
        in_tick = True
        print(line)
        continue
    if in_tick:
        if line.startswith("  public ") or line.startswith("  private ") or line.startswith("  protected "):
            break
        print(line)

