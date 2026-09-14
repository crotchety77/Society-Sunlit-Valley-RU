import os
import re
import zipfile
import json

COBBLEMON_INSTANCE = r"G:\curseforge\minecraft\Instances\Society Sunlit Cobblemon"
KUBEJS_DIR = os.path.join(COBBLEMON_INSTANCE, "kubejs")
MODS_DIR = os.path.join(COBBLEMON_INSTANCE, "mods")
FTB_QUESTS_DIR = os.path.join(COBBLEMON_INSTANCE, "config", "ftbquests", "quests", "chapters")
OUTPUT_MD = r"c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\SborkaCobblemon\tasks\01_cobblemon_skills\docs\DISCOVERED_MECHANICS.md"

def scan_kubejs_events():
    print("[1/4] Scanning KubeJS scripts for interactions and events...")
    discovered = []
    
    if not os.path.exists(KUBEJS_DIR):
        print("  KubeJS dir not found:", KUBEJS_DIR)
        return discovered

    patterns = [
        (r'ItemEvents\.rightClicked\s*\(\s*[\'"]([^\'"]+)[\'"]', "Item Right-Click Interaction"),
        (r'ItemEvents\.firstRightClicked\s*\(\s*[\'"]([^\'"]+)[\'"]', "Item First-Right-Click Interaction"),
        (r'BlockEvents\.rightClicked\s*\(\s*[\'"]([^\'"]+)[\'"]', "Block Right-Click Interaction"),
        (r'ItemEvents\.entityInteracted\s*\(\s*[\'"]([^\'"]+)[\'"]', "Entity Interaction with Item"),
        (r'EntityEvents\.death\s*\(', "Custom Death / Boss Kill Trigger"),
        (r'CobblemonEvents\.\w+', "Cobblemon Event Hook"),
        (r'createCobbleWorkerRecipe', "Cobblemon Worker Custom Recipe"),
        (r'\.customMachine\s*\(', "Custom Machine Definition"),
    ]

    for root, dirs, files in os.walk(KUBEJS_DIR):
        for f in files:
            if f.endswith(".js"):
                filepath = os.path.join(root, f)
                rel_path = os.path.relpath(filepath, COBBLEMON_INSTANCE)
                try:
                    with open(filepath, "r", encoding="utf-8", errors="ignore") as file:
                        content = file.read()
                        lines = content.splitlines()
                        for line_idx, line in enumerate(lines, 1):
                            for pat, desc in patterns:
                                matches = re.finditer(pat, line)
                                for m in matches:
                                    target = m.group(1) if m.groups() else ""
                                    discovered.append({
                                        "category": "KubeJS Event / Mechanic",
                                        "type": desc,
                                        "target": target or line.strip()[:60],
                                        "file": rel_path,
                                        "line": line_idx,
                                        "raw": line.strip()
                                    })
                except Exception as e:
                    pass
    return discovered

def scan_ftb_quests():
    print("[2/4] Scanning FTB Quests for unique mechanics, bosses and blocks...")
    discovered = []
    if not os.path.exists(FTB_QUESTS_DIR):
        return discovered

    keywords = [
        "boss", "statue", "raid", "altar", "gem_box", "pylon", "ranch", "garden", 
        "mine", "crystal", "permit", "medal", "token", "incubator", "ritual", "chalice", "totem"
    ]

    for root, dirs, files in os.walk(FTB_QUESTS_DIR):
        for f in files:
            if f.endswith(".snbt"):
                filepath = os.path.join(root, f)
                rel_path = os.path.relpath(filepath, COBBLEMON_INSTANCE)
                try:
                    with open(filepath, "r", encoding="utf-8", errors="ignore") as file:
                        content = file.read()
                        
                        # Find title and items
                        title_match = re.search(r'title:\s*"([^"]+)"', content)
                        chapter_title = title_match.group(1) if title_match else f
                        
                        # Search for item ids matching keywords
                        item_matches = re.findall(r'item:\s*"([^"]+)"', content)
                        for itm in set(item_matches):
                            for kw in keywords:
                                if kw in itm.lower():
                                    discovered.append({
                                        "category": "FTB Quest Feature",
                                        "type": f"Chapter: {chapter_title}",
                                        "target": itm,
                                        "file": rel_path,
                                        "line": 1,
                                        "raw": f"Quest item related to {kw}"
                                    })
                except Exception as e:
                    pass
    return discovered

def scan_mods_jars():
    print("[3/4] Scanning Mods JARs for BlockEntities, Screens and Mechanics...")
    discovered = []
    if not os.path.exists(MODS_DIR):
        return discovered

    relevant_mods = [
        "cobblemon", "farmers", "sunlit", "rctmod", "fight", "raid", "breeding", "past", "future"
    ]

    for f in os.listdir(MODS_DIR):
        if f.endswith(".jar") and any(k in f.lower() for k in relevant_mods):
            jar_path = os.path.join(MODS_DIR, f)
            try:
                with zipfile.ZipFile(jar_path, "r") as z:
                    for name in z.namelist():
                        if name.endswith("BlockEntity.class") or name.endswith("Block.class"):
                            discovered.append({
                                "category": "Mod Block / Entity",
                                "type": f"Mod: {f}",
                                "target": name.split("/")[-1].replace(".class", ""),
                                "file": f"mods/{f}",
                                "line": 0,
                                "raw": name
                            })
                        elif "recipe" in name.lower() and name.endswith(".json") and "recipes/" in name:
                            # Sample unique recipe types
                            if "craft_station" in name or "energy_pylon" in name or "ranching" in name:
                                discovered.append({
                                    "category": "Mod Custom Recipe Type",
                                    "type": f"Recipe in {f}",
                                    "target": name.split("/")[-1],
                                    "file": f"mods/{f}",
                                    "line": 0,
                                    "raw": name
                                })
            except Exception as e:
                pass
    return discovered

def generate_report(kubejs_items, quest_items, mod_items):
    print("[4/4] Writing report to DISCOVERED_MECHANICS.md...")
    
    os.makedirs(os.path.dirname(OUTPUT_MD), exist_ok=True)
    
    with open(OUTPUT_MD, "w", encoding="utf-8") as out:
        out.write("# 📡 Радар обнаруженных механик, интерактивных блоков и боссов\n\n")
        out.write("> Автоматический срез механик сборки **Society Sunlit Cobblemon**.\n")
        out.write("> Источники: `kubejs/`, `config/ftbquests/`, `mods/*.jar`.\n\n")
        out.write("---\n\n")
        
        out.write("## 1. ⚡ Серверные триггеры и интерактивные предметы (KubeJS)\n\n")
        out.write("| Тип взаимодействия | Целевой предмет / блок | Файл скрипта | Строка | Исходный код |\n")
        out.write("| :--- | :--- | :--- | :---: | :--- |\n")
        
        seen_k = set()
        for itm in kubejs_items:
            key = (itm["type"], itm["target"], itm["file"])
            if key not in seen_k:
                seen_k.add(key)
                code_snippet = itm["raw"][:50].replace("|", "\\|")
                out.write(f"| **{itm['type']}** | `{itm['target']}` | `{itm['file']}` | {itm['line']} | `{code_snippet}` |\n")
        
        out.write("\n---\n\n")
        out.write("## 2. 🏆 Квестовые механики, боссы и артефакты (FTB Quests)\n\n")
        out.write("| Глава квестов | Предмет / Артефакт | Файл квеста |\n")
        out.write("| :--- | :--- | :--- |\n")
        
        seen_q = set()
        for itm in quest_items:
            key = (itm["type"], itm["target"])
            if key not in seen_q:
                seen_q.add(key)
                out.write(f"| **{itm['type']}** | `{itm['target']}` | `{itm['file']}` |\n")

        out.write("\n---\n\n")
        out.write("## 3. 🧩 Интерактивные блоки и сущности из JAR-модов\n\n")
        out.write("| Мод / Архив | Блок / Сущность (Класс) | Путь в JAR |\n")
        out.write("| :--- | :--- | :--- |\n")
        
        seen_m = set()
        for itm in mod_items:
            key = (itm["type"], itm["target"])
            if key not in seen_m:
                seen_m.add(key)
                out.write(f"| **{itm['type']}** | `{itm['target']}` | `{itm['raw']}` |\n")

    print(f"Done! Saved to: {OUTPUT_MD}")

if __name__ == "__main__":
    k_items = scan_kubejs_events()
    q_items = scan_ftb_quests()
    m_items = scan_mods_jars()
    generate_report(k_items, q_items, m_items)
