import os

base_path = r"c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\SborkaCobblemon\tasks\01_cobblemon_skills\docs\next_level_research\disassembled"

def inspect_class_methods(class_name):
    file_path = os.path.join(base_path, f"{class_name}.javap.txt")
    if not os.path.exists(file_path):
        return f"File {file_path} not found"
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

poke_utils_code = inspect_class_methods("io.github.chakyl.cobblemonfarmers.utils.PokeUtils")
print("=== PokeUtils class ===")
for line in poke_utils_code.splitlines():
    if "public " in line or "protected " in line or "private " in line or "static " in line:
        if "{" not in line and "Code:" not in line and "LineNumberTable:" not in line and not line.strip().startswith("//"):
            print(line.strip())

