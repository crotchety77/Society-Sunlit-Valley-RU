import os
import re
import json
import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')

def parse_markdown_chapter(md_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        text = f.read()

    quests = {}
    blocks = re.split(r'\n---\s*\n', text)
    for b in blocks:
        id_match = re.search(r'###\s*Квест:\s*`([0-9A-Fa-f]+)`', b)
        if not id_match:
            continue
        qid = id_match.group(1).upper()
        chap_match = re.search(r'-\s*\*\*Глава\*\*:\s*`?([a-zA-Z0-9_]+)`?', b)
        chap = chap_match.group(1) if chap_match else ""

        # Title
        title_key_match = re.search(r'####\s*\[Название[^\]]*\]\s*-\s*\*\*Ключ\*\*:\s*`([^`]+)`', b)
        title_match = re.search(r'RU Title:\s*(.+)', b)

        # Subtitle
        sub_key_match = re.search(r'####\s*\[Подзаголовок[^\]]*\]\s*-\s*\*\*Ключ\*\*:\s*`([^`]+)`', b)
        subtitle_match = re.search(r'RU Subtitle:\s*(.+)', b)

        # Descriptions with explicit keys
        # Format: ##### Страница X (`key`)
        desc_dict = {}
        for desc_block in re.split(r'#####\s*Страница', b)[1:]:
            key_m = re.search(r'\(`([^`]+)`\)', desc_block)
            val_m = re.search(r'RU Description \d+:\s*(.+)', desc_block)
            if key_m and val_m:
                desc_dict[key_m.group(1)] = val_m.group(1).strip()
            elif val_m:
                # fallback by index
                idx_m = re.search(r'RU Description (\d+):', desc_block)
                if idx_m:
                    desc_dict[f"ftbquests.chapter.{chap}.quest{qid}.description{idx_m.group(1)}"] = val_m.group(1).strip()

        # Tasks with explicit keys
        task_dict = {}
        for task_block in re.split(r'-\s*\*\*Task ID', b)[1:]:
            tkey_m = re.search(r'-\s*\*\*Ключ\*\*:\s*`([^`]+)`', task_block)
            tval_m = re.search(r'RU Task\s*\[[^\]]+\]:\s*(.+)', task_block)
            if tkey_m and tval_m:
                task_dict[tkey_m.group(1)] = tval_m.group(1).strip()

        quests[qid] = {
            'id': qid,
            'chapter': chap,
            'title_key': title_key_match.group(1) if title_key_match else f"ftbquests.chapter.{chap}.quest{qid}.title",
            'title': title_match.group(1).strip() if title_match else None,
            'subtitle_key': sub_key_match.group(1) if sub_key_match else f"ftbquests.chapter.{chap}.quest{qid}.subtitle",
            'subtitle': subtitle_match.group(1).strip() if subtitle_match else None,
            'explicit_descriptions': desc_dict,
            'explicit_tasks': task_dict
        }
    return quests


def update_snbt_descriptions(snbt_path, qid, num_descriptions, has_pagebreaks=True):
    if not os.path.exists(snbt_path):
        return
    with open(snbt_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find quest description block specifically for qid
    pat = re.compile(rf'(description:\s*\[[\t\r\n\s]*"\{{ftbquests\.chapter\.[^.]+\.quest{qid}\.description1\}}"[\s\S]*?\])')
    m = pat.search(content)
    if m:
        chap_name = os.path.splitext(os.path.basename(snbt_path))[0]
        lines = []
        for i in range(1, num_descriptions + 1):
            if i == 4:
                lines.append('\t\t\t"{@pagebreak}"')
            elif i == 5:
                lines.append('\t\t\t"{@pagebreak}"')
            elif i > 1 and i < 4:
                lines.append('\t\t\t""')
            lines.append(f'\t\t\t"{{ftbquests.chapter.{chap_name}.quest{qid}.description{i}}}"')
        
        new_desc = "description: [\n" + "\n".join(lines) + "\n\t\t]"
        content = content[:m.start()] + new_desc + content[m.end():]
        with open(snbt_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated SNBT description for quest {qid} in {snbt_path}")



def main():
    base_dir = r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода'
    repo_ru_path = os.path.join(base_dir, 'translations', 'ftbquests', 'ru_ru.json')
    game_ru_path = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\ftbquestlocalizer\lang\ru_ru.json'
    game_snbt_dir = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\config\ftbquests\quests\chapters'

    with open(repo_ru_path, 'r', encoding='utf-8') as f:
        repo_ru = json.load(f)

    # Work files to apply (all files in work/priority1/)
    work_dir = os.path.join(base_dir, 'tasks', 'FTB_QUESTS_4_1_4', 'work', 'priority1')
    work_files = [os.path.join(work_dir, f) for f in os.listdir(work_dir) if f.endswith('.md')]

    applied_keys = []


    for wf in work_files:
        if not os.path.exists(wf):
            continue
        quests = parse_markdown_chapter(wf)
        for qid, q in quests.items():
            chap = q['chapter']
            if q['title']:
                repo_ru[q['title_key']] = q['title']
                applied_keys.append(q['title_key'])
            if q['subtitle']:
                repo_ru[q['subtitle_key']] = q['subtitle']
                applied_keys.append(q['subtitle_key'])
            for d_key, d_val in q['explicit_descriptions'].items():
                repo_ru[d_key] = d_val
                applied_keys.append(d_key)
            for t_key, t_val in q['explicit_tasks'].items():
                repo_ru[t_key] = t_val
                applied_keys.append(t_key)
            
            # Check SNBT for quest 263CCA4D2EAF2629 (pagebreaks)
            if qid == '263CCA4D2EAF2629' and len(q['explicit_descriptions']) >= 5:
                snbt_file = os.path.join(game_snbt_dir, f"{chap}.snbt")
                update_snbt_descriptions(snbt_file, qid, len(q['explicit_descriptions']))


    # Write to translations/ftbquests/ru_ru.json
    with open(repo_ru_path, 'w', encoding='utf-8') as f:
        json.dump(repo_ru, f, ensure_ascii=False, indent=2)

    # Write to game ru_ru.json
    with open(game_ru_path, 'w', encoding='utf-8') as f:
        json.dump(repo_ru, f, ensure_ascii=False, indent=2)

    print(f"Applied {len(applied_keys)} keys to repo and game lang!")

    # Run sync_all_to_game.js
    subprocess.run(['node', os.path.join(base_dir, 'sync_all_to_game.js')], cwd=base_dir)

    # Verify directly from game file
    with open(game_ru_path, 'r', encoding='utf-8') as f:
        game_check = json.load(f)

    print("\n=== ВЕРИФИКАЦИЯ ИЗ ФАЙЛА ИГРЫ ===")
    test_keys = [
        "ftbquests.chapter.iii__advanced_farming.questA455A4E0D7D074E.description1",
        "ftbquests.chapter.iii__advanced_farming.quest17C8B0197B8636E7.subtitle",
        "ftbquests.chapter.iii__advanced_farming.quest263CCA4D2EAF2629.title",
        "ftbquests.chapter.iii__advanced_farming.quest263CCA4D2EAF2629.description1",
        "ftbquests.chapter.iii__advanced_farming.quest263CCA4D2EAF2629.description2",
        "ftbquests.chapter.iii__advanced_farming.quest263CCA4D2EAF2629.description3",
        "ftbquests.chapter.iii__advanced_farming.quest263CCA4D2EAF2629.description4",
        "ftbquests.chapter.iii__advanced_farming.quest263CCA4D2EAF2629.description5",
        "ftbquests.chapter.iii__advanced_farming.quest3DE36C9FBCB58800.title",
        "ftbquests.chapter.iii__advanced_farming.quest3DE36C9FBCB58800.subtitle",
        "ftbquests.chapter.iii__advanced_farming.quest3DE36C9FBCB58800.description1",
        "ftbquests.chapter.iii__advanced_farming.quest3DE36C9FBCB58800.description2"
    ]
    for tk in test_keys:
        print(f"{tk} -> {game_check.get(tk)}")

if __name__ == '__main__':
    main()
