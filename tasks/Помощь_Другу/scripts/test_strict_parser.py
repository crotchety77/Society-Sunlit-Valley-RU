import re
from pathlib import Path

def parse_translated_txt_strict(txt_path):
    content = txt_path.read_text(encoding="utf-8")
    blocks = re.findall(r'===\s*\[КВЕСТ\s*\d+\s*\|\s*ID:\s*([A-F0-9]+)\]\s*===(.*?)(?:---\s*КОНЕЦ КВЕСТА|\Z)', content, re.DOTALL)
    
    translations = {}
    for qid, body in blocks:
        lines = body.splitlines()
        
        en_title = ""
        ru_title = ""
        en_sub = ""
        ru_sub = ""
        
        mode = None
        en_desc_lines = []
        ru_desc_lines = []
        
        for line in lines:
            stripped = line.strip()
            if line.startswith("EN_TITLE:"):
                en_title = line[len("EN_TITLE:"):].strip()
                mode = None
            elif line.startswith("RU_TITLE:"):
                ru_title = line[len("RU_TITLE:"):].strip()
                mode = None
            elif line.startswith("EN_SUBTITLE:"):
                en_sub = line[len("EN_SUBTITLE:"):].strip()
                mode = None
            elif line.startswith("RU_SUBTITLE:"):
                ru_sub = line[len("RU_SUBTITLE:"):].strip()
                mode = None
            elif line.startswith("EN_DESCRIPTION:"):
                mode = "EN_DESC"
            elif line.startswith("RU_DESCRIPTION:"):
                mode = "RU_DESC"
            elif mode == "EN_DESC":
                en_desc_lines.append(line)
            elif mode == "RU_DESC":
                ru_desc_lines.append(line)
                
        # Clean trailing empty lines from desc
        while ru_desc_lines and not ru_desc_lines[-1].strip():
            ru_desc_lines.pop()
        while ru_desc_lines and not ru_desc_lines[0].strip():
            ru_desc_lines.pop(0)
            
        translations[qid] = {
            "ru_title": ru_title,
            "ru_sub": ru_sub,
            "ru_desc_lines": ru_desc_lines,
            "has_translation": bool(ru_title or ru_sub or ru_desc_lines)
        }
        
    return translations

txt_file = Path(r"c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\tasks\Помощь_Другуу\Скрипты_для_помощи_ftb_quests\chapters_to_translate\seven_deadly_sins.txt")
trans = parse_translated_txt_strict(txt_file)
print(f"Total parsed: {len(trans)}")
for qid, d in trans.items():
    print(f"QID {qid}: ru_title='{d['ru_title']}', ru_sub='{d['ru_sub']}', has_trans={d['has_translation']}")
