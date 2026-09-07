import os
import re
import sys
import argparse

sys.stdout.reconfigure(encoding='utf-8')

GAME_CHAPTERS = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\config\ftbquests\quests\chapters'

def restore_quest_key(chapter_file, quest_id, field_type="title"):
    if not chapter_file.endswith('.snbt'):
        chapter_file += '.snbt'
        
    fp = os.path.join(GAME_CHAPTERS, chapter_file)
    if not os.path.exists(fp):
        print(f"❌ Файл главы не найден: {fp}")
        return False

    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    idx = content.find(f'"{quest_id}"')
    if idx == -1:
        idx = content.find(quest_id)
        if idx == -1:
            print(f"❌ Квест с ID {quest_id} не найден в {chapter_file}")
            return False

    chap_name = os.path.splitext(os.path.basename(chapter_file))[0]
    expected_key = f"{{ftbquests.chapter.{chap_name}.quest{quest_id}.{field_type}}}"

    # Find quest boundary
    start_idx = content.rfind('{', 0, idx)
    end_idx = content.find('\n\t\t}', idx)
    if end_idx == -1:
        end_idx = content.find('}', idx)

    block = content[start_idx:end_idx+1]
    
    if field_type == "title":
        # Replace title in block
        block_fixed = re.sub(r'title:\s*"[^"]*"', f'title: "{expected_key}"', block)
        if block_fixed == block:
            print(f"⚠️ Поле title не найдено или уже содержит ключ")
    else:
        print(f"Поддерживается восстановление поля title.")
        return False

    content = content[:start_idx] + block_fixed + content[end_idx+1:]
    
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ Успешно восстановлен ключ в {chapter_file}:")
    print(f"   title: \"{expected_key}\"")
    print(f"👉 Введите в игре /ftbquests reload")
    return True

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Восстановление ключа локализации квеста в SNBT после случайного редактирования в игре")
    parser.add_argument("chapter", help="Имя файла главы (например, getting_started.snbt или ii__building_up_the_farm)")
    parser.add_argument("quest_id", help="16-значный HEX ID квеста (например, 681EECD8B1D07F34)")
    parser.add_argument("--field", default="title", help="Тип поля (по умолчанию title)")

    args = parser.parse_args()
    restore_quest_key(args.chapter, args.quest_id, args.field)
