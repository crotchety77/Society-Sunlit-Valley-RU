import os
import re
import sys
import shutil
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

GAME_INSTANCE = Path(r"G:\curseforge\minecraft\Instances\Cisco's Fantasy Medieval RPG [Dragonfyre]")
CHAPTERS_DIR = GAME_INSTANCE / "config" / "ftbquests" / "quests" / "chapters"

SCRIPT_DIR = Path(__file__).resolve().parent
INPUT_DIR = SCRIPT_DIR / "chapters_to_translate"

def parse_translated_txt(txt_path):
    """
    Строгий построчный парсер перевода из .txt файла.
    """
    content = txt_path.read_text(encoding="utf-8")
    blocks = re.findall(r'===\s*\[КВЕСТ\s*\d+\s*\|\s*ID:\s*([A-F0-9]+)\]\s*===(.*?)(?:---\s*КОНЕЦ КВЕСТА|\Z)', content, re.DOTALL)
    
    translations = {}
    for qid, body in blocks:
        lines = body.splitlines()
        
        ru_title = ""
        ru_sub = ""
        mode = None
        ru_desc_lines = []
        
        for line in lines:
            if line.startswith("RU_TITLE:"):
                ru_title = line[len("RU_TITLE:"):].strip()
                mode = None
            elif line.startswith("RU_SUBTITLE:"):
                ru_sub = line[len("RU_SUBTITLE:"):].strip()
                mode = None
            elif line.startswith("RU_DESCRIPTION:"):
                mode = "RU_DESC"
            elif line.startswith("EN_TITLE:") or line.startswith("EN_SUBTITLE:") or line.startswith("EN_DESCRIPTION:"):
                mode = None
            elif mode == "RU_DESC":
                ru_desc_lines.append(line)
                
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

def find_quest_spans(snbt_text):
    """
    Честный поиск границ каждого квеста в quests: [ ... ] по балансу скобок.
    """
    m = re.search(r'\bquests:\s*\[', snbt_text)
    if not m:
        return []
        
    start_pos = m.end()
    spans = []
    
    in_string = False
    escape = False
    brace_depth = 0
    quest_start = -1
    
    i = start_pos
    while i < len(snbt_text):
        c = snbt_text[i]
        
        if escape:
            escape = False
            i += 1
            continue
        if c == '\\':
            escape = True
            i += 1
            continue
        if c == '"':
            in_string = not in_string
            i += 1
            continue
            
        if not in_string:
            if c == '{':
                brace_depth += 1
                if brace_depth == 1:
                    quest_start = i
            elif c == '}':
                brace_depth -= 1
                if brace_depth == 0 and quest_start != -1:
                    quest_end = i + 1
                    q_block = snbt_text[quest_start:quest_end]
                    id_m = re.search(r'^\s*id:\s*"([A-F0-9]+)"', q_block, re.MULTILINE)
                    if not id_m:
                        id_m = re.search(r'\bid:\s*"([A-F0-9]+)"', q_block)
                    if id_m:
                        spans.append((id_m.group(1), quest_start, quest_end))
                    quest_start = -1
            elif c == ']' and brace_depth == 0:
                break
        i += 1
        
    return spans

def update_quest_block(q_block, qid, trans):
    """
    Безопасно модифицирует поля title, subtitle, description на корневом уровне квеста,
    не затрагивая внутренние поля tasks: [ ... ].
    """
    new_block = q_block
    
    # 1. Title (корневой уровень квеста: 2-3 таба от начала строки)
    if trans["ru_title"]:
        safe_title = trans["ru_title"].replace('\\', '\\\\').replace('"', r'\"')
        if re.search(r'^\t{2,3}(?<!sub)title:\s*"((?:\\.|[^"\\])*)"', new_block, re.MULTILINE):
            new_block = re.sub(r'(^\t{2,3}(?<!sub)title:\s*)"(?:\\.|[^"\\])*"', rf'\g<1>"{safe_title}"', new_block, flags=re.MULTILINE)
        else:
            new_block = re.sub(r'(\t+id:\s*"' + qid + r'")', f'title: "{safe_title}"\n\t\t\t\\1', new_block)

    # 2. Subtitle (корневой уровень квеста: 2-3 таба)
    if trans["ru_sub"]:
        safe_sub = trans["ru_sub"].replace('\\', '\\\\').replace('"', r'\"')
        if re.search(r'^\t{2,3}subtitle:\s*"((?:\\.|[^"\\])*)"', new_block, re.MULTILINE):
            new_block = re.sub(r'(^\t{2,3}subtitle:\s*)"(?:\\.|[^"\\])*"', rf'\g<1>"{safe_sub}"', new_block, flags=re.MULTILINE)
        else:
            new_block = re.sub(r'(\t+id:\s*"' + qid + r'")', f'subtitle: "{safe_sub}"\n\t\t\t\\1', new_block)

    # 3. Description (корневой уровень)
    if trans["ru_desc_lines"]:
        desc_lines = []
        for l in trans["ru_desc_lines"]:
            escaped = l.replace('\\', '\\\\').replace('"', r'\"')
            desc_lines.append(f'\t\t\t\t"{escaped}"')
        formatted_desc = "description: [\n" + "\n".join(desc_lines) + "\n\t\t\t]"
        
        if re.search(r'^\t{2,3}description:\s*\[.*?\]', new_block, re.DOTALL | re.MULTILINE):
            new_block = re.sub(r'^\t{2,3}description:\s*\[.*?\]', f'\t\t\t{formatted_desc}', new_block, flags=re.DOTALL | re.MULTILINE)
        elif re.search(r'description:\s*\[.*?\]', new_block, re.DOTALL):
            new_block = re.sub(r'description:\s*\[.*?\]', formatted_desc, new_block, count=1, flags=re.DOTALL)
        else:
            new_block = re.sub(r'(\t+id:\s*"' + qid + r'")', f'{formatted_desc}\n\t\t\t\\1', new_block)

    return new_block

def count_tokens_outside_strings(text):
    counts = {'{': 0, '}': 0, '[': 0, ']': 0}
    in_string = False
    escape = False
    for c in text:
        if escape:
            escape = False
            continue
        if c == '\\':
            escape = True
            continue
        if c == '"':
            in_string = not in_string
            continue
        if not in_string and c in counts:
            counts[c] += 1
    return counts

def validate_snbt_integrity(original_text, new_text):
    orig_counts = count_tokens_outside_strings(original_text)
    new_counts = count_tokens_outside_strings(new_text)
    
    if new_counts['{'] != new_counts['}']:
        return False, f"Нарушен баланс фигурных скобок: {new_counts['{']} vs {new_counts['}']}"
    if new_counts['['] != new_counts[']']:
        return False, f"Нарушен баланс квадратных скобок: {new_counts['[']} vs {new_counts['}']}"
        
    old_ids = set(re.findall(r'id:\s*"([A-F0-9]+)"', original_text))
    new_ids = set(re.findall(r'id:\s*"([A-F0-9]+)"', new_text))
    if old_ids != new_ids:
        missing = old_ids - new_ids
        return False, f"Потеряны ID: {missing}"
        
    return True, "OK"

def import_chapter(txt_file):
    chapter_name = f"{txt_file.stem}.snbt"
    snbt_path = CHAPTERS_DIR / chapter_name
    
    if not snbt_path.exists():
        print(f"⚠️  Файл главы '{chapter_name}' не найден в игре. Пропуск.")
        return
        
    translations = parse_translated_txt(txt_file)
    
    has_any = any(t["has_translation"] for t in translations.values())
    if not has_any:
        print(f"⚪ Глава '{chapter_name}': нет новых правок (шаблон чист).")
        return

    original_snbt = snbt_path.read_text(encoding="utf-8")
    spans = find_quest_spans(original_snbt)
    
    updated_snbt = original_snbt
    updated_count = 0
    
    for qid, start_idx, end_idx in sorted(spans, key=lambda x: x[1], reverse=True):
        if qid in translations and translations[qid]["has_translation"]:
            trans = translations[qid]
            old_q_block = updated_snbt[start_idx:end_idx]
            new_q_block = update_quest_block(old_q_block, qid, trans)
            if new_q_block != old_q_block:
                updated_snbt = updated_snbt[:start_idx] + new_q_block + updated_snbt[end_idx:]
                updated_count += 1
                
    if updated_snbt != original_snbt:
        is_valid, msg = validate_snbt_integrity(original_snbt, updated_snbt)
        if not is_valid:
            print(f"❌ ОШИБКА ВАЛИДАЦИИ в '{chapter_name}': {msg}. Запись отменена!")
            return
            
        backup_path = snbt_path.with_suffix(".snbt.bak")
        if not backup_path.exists():
            shutil.copy2(snbt_path, backup_path)
            
        snbt_path.write_text(updated_snbt, encoding="utf-8")
        print(f"✅ Глава '{chapter_name}' успешно обновлена! (Переведено квестов: {updated_count})")
    else:
        print(f"⚪ Глава '{chapter_name}': нет новых правок.")

def main():
    print("=== БЕЗОПАСНЫЙ ИМПОРТ ПЕРЕВОДА FTB QUESTS ===")
    if not INPUT_DIR.exists():
        print(f"❌ Папка с текстами {INPUT_DIR} не найдена.")
        return
        
    txt_files = sorted(list(INPUT_DIR.glob("*.txt")))
    for txt in txt_files:
        import_chapter(txt)
        
    print("\n🎉 Проверка завершена!")
    print("В игре нажмите F3 + T, затем введите /ftbquests reload для проверки.")

if __name__ == "__main__":
    main()
