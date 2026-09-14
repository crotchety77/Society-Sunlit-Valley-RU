import os
import subprocess
import glob

extracted_dir = r"c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\SborkaCobblemon\tasks\01_cobblemon_skills\docs\next_level_research\extracted_classes"
output_dir = r"c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\SborkaCobblemon\tasks\01_cobblemon_skills\docs\next_level_research\disassembled"

os.makedirs(output_dir, exist_ok=True)

class_files = glob.glob(os.path.join(extracted_dir, "**", "*.class"), recursive=True)
print(f"Total classes found: {len(class_files)}")

for cf in class_files:
    rel_path = os.path.relpath(cf, extracted_dir)
    clean_name = rel_path.replace(os.sep, ".").replace(".class", "")
    out_file = os.path.join(output_dir, f"{clean_name}.javap.txt")
    
    cmd = ["javap", "-p", "-c", "-constants", "-cp", extracted_dir, cf]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(res.stdout)
    except Exception as e:
        print(f"Error decompiling {clean_name}: {e}")

print("Disassembly complete!")
