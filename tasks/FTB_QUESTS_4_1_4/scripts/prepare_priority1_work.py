import os
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

from audit_ftb_quests import parse_snbt_file, has_cyrillic

def extract_formatting(text):
    if not text:
        return []
    items = []
    # Color & format codes
    codes = re.findall(r'&[0-9a-fk-or]', text)
    if codes:
        items.append(f"Цветовые коды: {', '.join(sorted(set(codes)))}")
    # Tags
    tags = re.findall(r'#[a-zA-Z0-9_:]+', text)
    if tags:
        items.append(f"Теги: {', '.join(tags)}")
    # Placeholders / tokens
    placeholders = re.findall(r'\{[a-zA-Z0-9_.-]+\}|%[a-zA-Z0-9_]+%|@[a-zA-Z0-9_]+', text)
    if placeholders:
        items.append(f"Плейсхолдеры: {', '.join(placeholders)}")
    # Newlines
    if '\n' in text:
        items.append("Переносы строк (\\n)")
    return items

def main():
    base_dir = r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\tasks\FTB_QUESTS_4_1_4'
    p_414 = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\config\ftbquests\quests'
    p1_ru = json.load(open(r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\ftbquestlocalizer\lang\ru_ru.json', encoding='utf-8'))
    p1_en = json.load(open(r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\ftbquestlocalizer\lang\en_us.json', encoding='utf-8'))

    with open(os.path.join(base_dir, 'registry_quests.json'), 'r', encoding='utf-8') as f:
        reg = json.load(f)

    # Load 4.1.4 chapters SNBT
    chap_414_dir = os.path.join(p_414, 'chapters')
    chapters_414 = {}
    for f in sorted(os.listdir(chap_414_dir)):
        if f.endswith('.snbt'):
            cname = f[:-5]
            data = parse_snbt_file(os.path.join(chap_414_dir, f))
            chapters_414[cname] = data

    q_snbt_map = {}
    for cname, cdata in chapters_414.items():
        if isinstance(cdata, dict):
            for q in cdata.get('quests', []):
                if isinstance(q, dict) and 'id' in q:
                    q_snbt_map[q['id']] = (cname, q)

    new_quests_meta = [q for q in reg['quests'] if q['ver_status'] == 'new_in_4.1.4']

    processed_quests = []

    for qm in new_quests_meta:
        qid = qm['id']
        cname, qobj = q_snbt_map[qid]

        title_raw = qobj.get('title', '')
        subtitle_raw = qobj.get('subtitle', '')
        desc_raw = qobj.get('description', [])
        tasks_raw = qobj.get('tasks', [])
        rewards_raw = qobj.get('rewards', [])

        # Title
        t_key = None
        t_en = ""
        t_ru = ""
        if isinstance(title_raw, str) and title_raw.startswith('{') and title_raw.endswith('}'):
            t_key = title_raw[1:-1]
            t_en = p1_en.get(t_key, '')
            t_ru = p1_ru.get(t_key, '')
        elif title_raw:
            t_en = title_raw
            t_ru = ""
        else:
            default_t_key = f"ftbquests.chapter.{cname}.quest{qid}.title"
            if default_t_key in p1_en:
                t_key = default_t_key
                t_en = p1_en[default_t_key]
                t_ru = p1_ru.get(default_t_key, '')

        # Subtitle
        sub_key = None
        sub_en = ""
        sub_ru = ""
        if isinstance(subtitle_raw, str) and subtitle_raw.startswith('{') and subtitle_raw.endswith('}'):
            sub_key = subtitle_raw[1:-1]
            sub_en = p1_en.get(sub_key, '')
            sub_ru = p1_ru.get(sub_key, '')
        elif subtitle_raw:
            sub_en = subtitle_raw
            sub_ru = ""
        else:
            default_sub_key = f"ftbquests.chapter.{cname}.quest{qid}.subtitle"
            if default_sub_key in p1_en:
                sub_key = default_sub_key
                sub_en = p1_en[default_sub_key]
                sub_ru = p1_ru.get(default_sub_key, '')

        # Descriptions (filter out empty strings)
        desc_list = []
        if isinstance(desc_raw, list):
            for item in desc_raw:
                if not item or item == '{@pagebreak}':
                    continue
                if isinstance(item, str) and item.startswith('{') and item.endswith('}'):
                    k = item[1:-1]
                    d_en = p1_en.get(k, '')
                    d_ru = p1_ru.get(k, '')
                    # extract description number from key
                    m = re.search(r'description(\d+)$', k)
                    d_num = int(m.group(1)) if m else len(desc_list) + 1
                    desc_list.append({'idx': d_num, 'key': k, 'en': d_en, 'ru': d_ru})
                elif isinstance(item, str) and item.strip():
                    desc_list.append({'idx': len(desc_list) + 1, 'key': None, 'en': item, 'ru': ''})
        elif isinstance(desc_raw, str) and desc_raw.strip():
            if desc_raw.startswith('{') and desc_raw.endswith('}'):
                k = desc_raw[1:-1]
                desc_list.append({'idx': 1, 'key': k, 'en': p1_en.get(k, ''), 'ru': p1_ru.get(k, '')})
            else:
                desc_list.append({'idx': 1, 'key': None, 'en': desc_raw, 'ru': ''})

        # Tasks (keep only tasks with actual translatable custom titles)
        task_list = []
        for t in tasks_raw:
            if isinstance(t, dict):
                tid = t.get('id', '')
                ttitle = t.get('title', '')
                ttype = t.get('type', 'item')
                titem = t.get('item', '')
                tk = None
                t_en_val = ""
                t_ru_val = ""
                if isinstance(ttitle, str) and ttitle.startswith('{') and ttitle.endswith('}'):
                    tk = ttitle[1:-1]
                    t_en_val = p1_en.get(tk, '')
                    t_ru_val = p1_ru.get(tk, '')
                elif ttitle:
                    t_en_val = ttitle
                else:
                    # check if ftbquestlocalizer has task title key
                    for k in p1_en:
                        if f"quest{qid}.task." in k:
                            tk = k
                            t_en_val = p1_en[k]
                            t_ru_val = p1_ru.get(k, '')
                            break
                if t_en_val or tk:
                    task_list.append({'id': tid, 'key': tk, 'en': t_en_val, 'ru': t_ru_val, 'type': ttype, 'item': titem})

        # Rewards (keep rewards with actual translatable titles)
        reward_list = []
        for r in rewards_raw:
            if isinstance(r, dict):
                rid = r.get('id', '')
                rtitle = r.get('title', '')
                rtype = r.get('type', 'item')
                ritem = r.get('item', '')
                rcount = r.get('count', 1)
                rk = None
                r_en_val = ""
                r_ru_val = ""
                if isinstance(rtitle, str) and rtitle.startswith('{') and rtitle.endswith('}'):
                    rk = rtitle[1:-1]
                    r_en_val = p1_en.get(rk, '')
                    r_ru_val = p1_ru.get(rk, '')
                elif rtitle:
                    r_en_val = rtitle
                if r_en_val or rk:
                    reward_list.append({'id': rid, 'key': rk, 'en': r_en_val, 'ru': r_ru_val, 'type': rtype, 'item': ritem, 'count': rcount})

        # Categorize scope
        has_title = bool(t_en)
        has_sub = bool(sub_en)
        has_desc = any(bool(d['en']) for d in desc_list)
        has_custom_tasks = any(bool(t['en']) for t in task_list)
        has_custom_rewards = any(bool(r['en']) for r in reward_list)

        if has_title and has_desc:
            scope = 'full_text'
        elif has_title or has_desc or has_sub or has_custom_tasks or has_custom_rewards:
            scope = 'partial_text'
        elif len(tasks_raw) > 0:
            scope = 'item_only'
        else:
            scope = 'no_translation_needed'

        existing_ru_keys = []
        if t_ru and has_cyrillic(t_ru): existing_ru_keys.append(('title', t_key, t_ru))
        if sub_ru and has_cyrillic(sub_ru): existing_ru_keys.append(('subtitle', sub_key, sub_ru))
        for d in desc_list:
            if d['ru'] and has_cyrillic(d['ru']): existing_ru_keys.append(('desc', d['key'], d['ru']))
        for t in task_list:
            if t['ru'] and has_cyrillic(t['ru']): existing_ru_keys.append(('task', t['key'], t['ru']))
        for r in reward_list:
            if r['ru'] and has_cyrillic(r['ru']): existing_ru_keys.append(('reward', r['key'], r['ru']))

        processed_quests.append({
            'id': qid,
            'chapter': cname,
            'scope': scope,
            'title': {'key': t_key, 'en': t_en, 'ru': t_ru},
            'subtitle': {'key': sub_key, 'en': sub_en, 'ru': sub_ru},
            'descriptions': desc_list,
            'tasks': task_list,
            'rewards': reward_list,
            'existing_ru': existing_ru_keys,
            'raw_quest': qobj
        })

    # Update registry_quests.json
    for q in reg['quests']:
        for pq in processed_quests:
            if q['id'] == pq['id']:
                q['scope'] = pq['scope']
                q['title_en'] = pq['title']['en'] or pq['subtitle']['en'] or ''
                break
    with open(os.path.join(base_dir, 'registry_quests.json'), 'w', encoding='utf-8') as f:
        json.dump(reg, f, ensure_ascii=False, indent=2)

    # Prepare work directory by chapters
    work_p1_dir = os.path.join(base_dir, 'work', 'priority1')
    os.makedirs(work_p1_dir, exist_ok=True)

    chapters_with_text = {}
    for pq in processed_quests:
        if pq['scope'] in ['full_text', 'partial_text']:
            chapters_with_text.setdefault(pq['chapter'], []).append(pq)

    def render_clean_block(pq):
        lines = []
        name_display = pq['title']['en'] or (f"[{pq['subtitle']['en']}]" if pq['subtitle']['en'] else "Item Task")
        lines.append(f"### Квест: `{pq['id']}` — **{name_display}**")
        lines.append(f"- **ID**: `{pq['id']}`")
        lines.append(f"- **Глава**: `{pq['chapter']}`")
        lines.append(f"- **Объём**: `{pq['scope']}`")
        lines.append(f"- **Существующий перевод в ru_ru.json**: {'Да (' + str(len(pq['existing_ru'])) + ' полей)' if pq['existing_ru'] else 'Нет'}")
        lines.append("")

        # Title
        if pq['title']['en'] or pq['title']['key']:
            lines.append("#### [Название / Title]")
            if pq['title']['key']: lines.append(f"- **Ключ**: `{pq['title']['key']}`")
            lines.append(f"- **EN Title**: `{pq['title']['en']}`" if pq['title']['en'] else "- **EN Title**: *[Не задан в оригинале]*")
            fmt = extract_formatting(pq['title']['en'])
            if fmt: lines.append(f"- **Форматирование**: {'; '.join(fmt)}")
            lines.append(f"```text\nRU Title: {pq['title']['ru']}\n```")
            lines.append("")

        # Subtitle
        if pq['subtitle']['en'] or pq['subtitle']['key']:
            lines.append("#### [Подзаголовок / Subtitle]")
            if pq['subtitle']['key']: lines.append(f"- **Ключ**: `{pq['subtitle']['key']}`")
            lines.append(f"- **EN Subtitle**: `{pq['subtitle']['en']}`")
            fmt = extract_formatting(pq['subtitle']['en'])
            if fmt: lines.append(f"- **Форматирование**: {'; '.join(fmt)}")
            lines.append(f"```text\nRU Subtitle: {pq['subtitle']['ru']}\n```")
            lines.append("")

        # Descriptions
        if pq['descriptions']:
            lines.append("#### [Описание / Description]")
            for d in pq['descriptions']:
                idx = d['idx']
                k = d['key'] or f"ftbquests.chapter.{pq['chapter']}.quest{pq['id']}.description{idx}"
                lines.append(f"##### Страница {idx} (`{k}`)")
                lines.append(f"- **EN Description {idx}**:")
                lines.append(f"> {d['en']}")
                fmt = extract_formatting(d['en'])
                if fmt: lines.append(f"- **Форматирование**: {'; '.join(fmt)}")
                lines.append(f"```text\nRU Description {idx}: {d['ru']}\n```")
                lines.append("")

        # Tasks
        if pq['tasks']:
            lines.append("#### [Цели / Tasks]")
            for t in pq['tasks']:
                lines.append(f"- **Task ID `{t['id']}`** (Тип: `{t['type']}`)")
                if t['key']: lines.append(f"  - **Ключ**: `{t['key']}`")
                lines.append(f"  - **EN Task**: `{t['en']}`")
                fmt = extract_formatting(t['en'])
                if fmt: lines.append(f"  - **Форматирование**: {'; '.join(fmt)}")
                lines.append(f"```text\nRU Task [{t['id']}]: {t['ru']}\n```")
                lines.append("")

        # Rewards
        if pq['rewards']:
            lines.append("#### [Награды / Rewards]")
            for r in pq['rewards']:
                lines.append(f"- **Reward ID `{r['id']}`**")
                if r['key']: lines.append(f"  - **Ключ**: `{r['key']}`")
                lines.append(f"  - **EN Reward**: `{r['en']}`")
                lines.append(f"```text\nRU Reward [{r['id']}]: {r['ru']}\n```")
                lines.append("")

        lines.append("---")
        return "\n".join(lines)

    # Write per-chapter files
    for cname in sorted(chapters_with_text.keys()):
        qlist = chapters_with_text[cname]
        chap_file = os.path.join(work_p1_dir, f"{cname}.md")
        with open(chap_file, 'w', encoding='utf-8') as f:
            f.write(f"# Priority 1 — Рабочий файл главы `{cname}`\n\n")
            f.write(f"Количество квестов для локализации в главе: **{len(qlist)}**\n\n")
            f.write("---\n\n")
            for pq in qlist:
                f.write(render_clean_block(pq) + "\n\n")

    # Generate translation_queue.md
    tq_path = os.path.join(base_dir, 'translation_queue.md')
    with open(tq_path, 'w', encoding='utf-8') as f:
        f.write("# Очередь ручной локализации FTB Quests — Priority 1 (Новые квесты 4.1.4)\n\n")
        f.write("В этот список включены **только квесты, содержащие текст для перевода** (13 квестов из 20 новых).\n")
        f.write("7 чисто предметных квестов (`item_only`) исключены из очереди перевода, так как не имеют кастомного текста.\n\n")
        f.write("## Сводная таблица очереди перевода\n\n")
        f.write("| № | Глава | ID | Название EN | Тип | Кол-во страниц | Файл для работы |\n")
        f.write("| - | ----- | -- | ----------- | --- | :------------: | --------------- |\n")
        idx = 1
        for cname in sorted(chapters_with_text.keys()):
            for pq in chapters_with_text[cname]:
                t_en = pq['title']['en'] or pq['subtitle']['en'] or '— (Item Task)'
                f.write(f"| {idx} | `{cname}` | `{pq['id']}` | **{t_en}** | `{pq['scope']}` | {len(pq['descriptions'])} | [`work/priority1/{cname}.md`](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/tasks/FTB_QUESTS_4_1_4/work/priority1/{cname}.md) |\n")
                idx += 1

        f.write("\n---\n\n")
        f.write("## Детальные рабочие блоки по главам\n\n")
        for cname in sorted(chapters_with_text.keys()):
            f.write(f"### Глава: `{cname}` (Квестов: {len(chapters_with_text[cname])})\n\n")
            for pq in chapters_with_text[cname]:
                f.write(render_clean_block(pq) + "\n\n")

    # Update work_queue/priority1_new.md
    p1_new_md_path = os.path.join(base_dir, 'work_queue', 'priority1_new.md')
    with open(p1_new_md_path, 'w', encoding='utf-8') as f:
        f.write("# Priority 1: Новые квесты версии 4.1.4 (Полный аудит)\n\n")
        f.write(f"Всего новых квестов: **20**\n")
        f.write(f"- Требуют перевода (`full_text` / `partial_text`): **{len([q for q in processed_quests if q['scope'] in ['full_text', 'partial_text']])}**\n")
        f.write(f"- Чисто предметные задачи (`item_only`): **{len([q for q in processed_quests if q['scope'] == 'item_only'])}**\n\n")
        f.write("## 1. Квесты, требующие локализации (13 шт.)\n\n")
        for pq in [q for q in processed_quests if q['scope'] in ['full_text', 'partial_text']]:
            f.write(render_clean_block(pq) + "\n\n")

        f.write("## 2. Предметные квесты без кастомного текста (7 шт.)\n\n")
        f.write("| Глава | ID | Тип предмета / задачи | Scope |\n")
        f.write("| ----- | -- | --------------------- | ----- |\n")
        for pq in [q for q in processed_quests if q['scope'] == 'item_only']:
            item_strs = []
            for t in pq['raw_quest'].get('tasks', []):
                it = t.get('item')
                if isinstance(it, dict):
                    item_strs.append(it.get('id', 'item'))
                elif it:
                    item_strs.append(str(it))
            item_desc = ", ".join(item_strs) or "Item task"
            f.write(f"| `{pq['chapter']}` | `{pq['id']}` | `{item_desc}` | `{pq['scope']}` |\n")

    print("Refined priority1 generation completed successfully!")

if __name__ == '__main__':
    main()
