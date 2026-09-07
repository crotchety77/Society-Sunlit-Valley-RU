import sys
from pathlib import Path

sys.path.insert(0, r"c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\tasks\Помощь_Другуу\Скрипты_для_помощи_ftb_quests")
import import_quests

txt_file = Path(r"c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\tasks\Помощь_Другуу\Скрипты_для_помощи_ftb_quests\chapters_to_translate\seven_deadly_sins.txt")
trans = import_quests.parse_translated_txt(txt_file)
print(f"Total parsed entries: {len(trans)}")
for qid, data in trans.items():
    print(f"QID {qid}: ru_title='{data['ru_title']}', ru_sub='{data['ru_sub']}', has_desc_trans={data['has_desc_translation']}, ru_desc_len={len(data['ru_desc_lines'])}")
