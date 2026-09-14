import os

base_path = r"c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\SborkaCobblemon\tasks\01_cobblemon_skills\docs\next_level_research\disassembled"

def get_method_bytecode(class_name, method_name):
    file_path = os.path.join(base_path, f"{class_name}.javap.txt")
    if not os.path.exists(file_path):
        return f"File {file_path} not found"
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    lines = content.splitlines()
    method_lines = []
    recording = False
    for line in lines:
        if method_name in line and ("public " in line or "protected " in line or "private " in line or "void " in line or "boolean " in line or "double " in line or "int " in line):
            recording = True
            method_lines.append("="*50)
            method_lines.append(line)
            continue
        if recording:
            if line.startswith("  public ") or line.startswith("  protected ") or line.startswith("  private ") or line.startswith("}"):
                if not line.startswith("    "):
                    recording = False
                    continue
            method_lines.append(line)
    return "\n".join(method_lines)

print("=== StationBaseBlockEntity fetchSpeedModifier ===")
print(get_method_bytecode("io.github.chakyl.cobblemonfarmers.blockentity.StationBaseBlockEntity", "fetchSpeedModifier"))

print("=== StationBaseBlockEntity fetchMultChance ===")
print(get_method_bytecode("io.github.chakyl.cobblemonfarmers.blockentity.StationBaseBlockEntity", "fetchMultChance"))

print("=== StationBaseBlockEntity fetchAoeRadius ===")
print(get_method_bytecode("io.github.chakyl.cobblemonfarmers.blockentity.StationBaseBlockEntity", "fetchAoeRadius"))

print("=== StationBaseBlockEntity getBoostedSpeedModifier ===")
print(get_method_bytecode("io.github.chakyl.cobblemonfarmers.blockentity.StationBaseBlockEntity", "getBoostedSpeedModifier"))

print("=== StationBaseBlockEntity getBoostedMultChance ===")
print(get_method_bytecode("io.github.chakyl.cobblemonfarmers.blockentity.StationBaseBlockEntity", "getBoostedMultChance"))

