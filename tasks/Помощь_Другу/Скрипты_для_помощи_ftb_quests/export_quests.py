import os
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

GAME_INSTANCE = Path(r"G:\curseforge\minecraft\Instances\Cisco's Fantasy Medieval RPG [Dragonfyre]")
CHAPTERS_DIR = GAME_INSTANCE / "config" / "ftbquests" / "quests" / "chapters"

SCRIPT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = SCRIPT_DIR / "chapters_to_translate"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def extract_root_quest_fields(q_block):
    """
    Извлекает только корневые поля квеста (id, title, subtitle, description),
    игнорируя внутренние блоки tasks: [ ... ] и rewards: [ ... ].
    """
    in_string = False
    escape = False
    brace_depth = 0
    bracket_depth = 0
    
    cleaned = []
    in_desc = False
    
    i = 0
    while i < len(q_block):
        c = q_block[i]
        
        if escape:
            escape = False
            if brace_depth == 1 and (bracket_depth == 0 or in_desc):
                cleaned.append(c)
            i += 1
            continue
            
        if c == '\\':
            escape = True
            if brace_depth == 1 and (bracket_depth == 0 or in_desc):
                cleaned.append(c)
            i += 1
            continue
            
        if c == '"':
            in_string = not in_string
            if brace_depth == 1 and (bracket_depth == 0 or in_desc):
                cleaned.append(c)
            i += 1
            continue
            
        if not in_string:
            if c == '{':
                brace_depth += 1
            elif c == '}':
                brace_depth -= 1
            elif c == '[':
                bracket_depth += 1
                preceding = "".join(cleaned[-20:])
                if "description:" in preceding:
                    in_desc = True
            elif c == ']':
                if in_desc and bracket_depth == 1:
                    in_desc = False
                bracket_depth -= 1
                
            if brace_depth == 1 and (bracket_depth == 0 or in_desc):
                cleaned.append(c)
        else:
            if brace_depth == 1 and (bracket_depth == 0 or in_desc):
                cleaned.append(c)
        i += 1
        
    cleaned_str = "".join(cleaned)
    
    id_m = re.search(r'\bid:\s*"([A-F0-9]+)"', cleaned_str)
    qid = id_m.group(1) if id_m else "UNKNOWN"
    
    title_m = re.search(r'(?<!sub)title:\s*"((?:\\.|[^"\\])*)"', cleaned_str)
    title = title_m.group(1).replace(r'\"', '"').replace(r'\\', '\\') if title_m else ""
    
    sub_m = re.search(r'subtitle:\s*"((?:\\.|[^"\\])*)"', cleaned_str)
    subtitle = sub_m.group(1).replace(r'\"', '"').replace(r'\\', '\\') if sub_m else ""
    
    desc_m = re.search(r'description:\s*\[(.*?)\]', cleaned_str, re.DOTALL)
    desc_lines = []
    if desc_m:
        raw_lines = re.findall(r'"((?:\\.|[^"\\])*)"', desc_m.group(1))
        desc_lines = [l.replace(r'\"', '"').replace(r'\\', '\\') for l in raw_lines]
        
    return {
        "id": qid,
        "title": title,
        "subtitle": subtitle,
        "description": desc_lines
    }

def parse_quests_from_snbt(snbt_text):
    m = re.search(r'\bquests:\s*\[', snbt_text)
    if not m:
        return []
    
    start_idx = m.end()
    depth = 1
    i = start_idx
    while i < len(snbt_text) and depth > 0:
        c = snbt_text[i]
        if c == '[':
            depth += 1
        elif c == ']':
            depth -= 1
        i += 1
    
    quests_content = snbt_text[start_idx:i-1]
    
    raw_quests = []
    brace_depth = 0
    curr_quest = []
    in_string = False
    escape = False
    
    for char in quests_content:
        if escape:
            curr_quest.append(char)
            escape = False
            continue
        if char == '\\':
            curr_quest.append(char)
            escape = True
            continue
        if char == '"':
            in_string = not in_string
            curr_quest.append(char)
            continue
            
        if not in_string:
            if char == '{':
                brace_depth += 1
                if brace_depth == 1:
                    curr_quest = ['{']
                    continue
            elif char == '}':
                brace_depth -= 1
                if brace_depth == 0:
                    curr_quest.append('}')
                    raw_quests.append("".join(curr_quest))
                    curr_quest = []
                    continue
                    
        if brace_depth > 0:
            curr_quest.append(char)
            
    return [extract_root_quest_fields(q) for q in raw_quests]

def export_chapter(chapter_file):
    text = chapter_file.read_text(encoding="utf-8")
    quests = parse_quests_from_snbt(text)
    
    out_file = OUTPUT_DIR / f"{chapter_file.stem}.txt"
    
    existing_translations = {}
    if out_file.exists():
        try:
            from import_quests import parse_translated_txt
            existing_translations = parse_translated_txt(out_file)
        except Exception:
            pass
            
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(f"# =========================================================================\n")
        f.write(f"# ГЛАВА: {chapter_file.name}\n")
        f.write(f"# Всего квестов: {len(quests)}\n")
        f.write(f"# ИНСТРУКЦИЯ: Заполняйте поля RU_TITLE, RU_SUBTITLE, RU_DESCRIPTION.\n")
        f.write(f"# Если оставляете поле RU_ пустым — квест НЕ будет перезаписан.\n")
        f.write(f"# =========================================================================\n\n")
        
        for idx, q in enumerate(quests, 1):
            qid = q['id']
            ru_t = existing_translations.get(qid, {}).get("ru_title", "")
            ru_s = existing_translations.get(qid, {}).get("ru_sub", "")
            ru_d = existing_translations.get(qid, {}).get("ru_desc_lines", [])
            
            f.write(f"=== [КВЕСТ {idx} | ID: {qid}] ===\n")
            f.write(f"EN_TITLE: {q['title']}\n")
            f.write(f"RU_TITLE: {ru_t}\n\n")
            
            f.write(f"EN_SUBTITLE: {q['subtitle']}\n")
            f.write(f"RU_SUBTITLE: {ru_s}\n\n")
            
            f.write(f"EN_DESCRIPTION:\n")
            if q['description']:
                for line in q['description']:
                    f.write(f"{line}\n")
            else:
                f.write(f"(нет описания)\n")
                
            f.write(f"\nRU_DESCRIPTION:\n")
            if ru_d:
                for line in ru_d:
                    f.write(f"{line}\n")
            f.write(f"\n--- КОНЕЦ КВЕСТА {qid} ---\n\n\n")
            
    print(f" -> Экспортирована глава '{chapter_file.name}' -> {out_file.name} ({len(quests)} квестов)")

def main():
    print("=== ЭКСПОРТ ЧИСТЫХ ШАБЛОНОВ FTB QUESTS ===")
    if not CHAPTERS_DIR.exists():
        print(f"Ошибка: Папка квестов не найдена: {CHAPTERS_DIR}")
        return

    chapter_files = sorted(list(CHAPTERS_DIR.glob("*.snbt")))
    for ch in chapter_files:
        export_chapter(ch)
        
    print(f"\n Все шаблоны созданы в папке:\n {OUTPUT_DIR.resolve()}")

if __name__ == "__main__":
    main()
