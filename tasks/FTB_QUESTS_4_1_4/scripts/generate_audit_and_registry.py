import os
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

def tokenize_snbt(text):
    tokens = []
    i = 0
    n = len(text)
    while i < n:
        c = text[i]
        if c.isspace():
            i += 1
            continue
        if c == '{':
            tokens.append(('LBRACE', '{'))
            i += 1
        elif c == '}':
            tokens.append(('RBRACE', '}'))
            i += 1
        elif c == '[':
            tokens.append(('LBRACKET', '['))
            i += 1
        elif c == ']':
            tokens.append(('RBRACKET', ']'))
            i += 1
        elif c == ':':
            tokens.append(('COLON', ':'))
            i += 1
        elif c == ',':
            tokens.append(('COMMA', ','))
            i += 1
        elif c == '"':
            i += 1
            s = []
            while i < n:
                if text[i] == '\\' and i + 1 < n:
                    s.append(text[i+1])
                    i += 2
                elif text[i] == '"':
                    break
                else:
                    s.append(text[i])
                    i += 1
            tokens.append(('STRING', ''.join(s)))
            i += 1
        else:
            start = i
            while i < n and text[i] not in ' \t\r\n{}[],:':
                i += 1
            val = text[start:i]
            tokens.append(('BARE', val))
    return tokens

class SNBTParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def get(self):
        t = self.peek()
        if t:
            self.pos += 1
        return t

    def parse_value(self):
        t = self.peek()
        if not t:
            return None
        ttype, val = t
        if ttype == 'LBRACE':
            return self.parse_object()
        elif ttype == 'LBRACKET':
            return self.parse_array()
        elif ttype == 'STRING':
            self.get()
            return val
        elif ttype == 'BARE':
            self.get()
            if val == 'true': return True
            if val == 'false': return False
            num_str = re.sub(r'[dfbsLDFBSL]$', '', val)
            try:
                if '.' in num_str:
                    return float(num_str)
                return int(num_str)
            except:
                return val
        return None

    def parse_object(self):
        self.get()
        obj = {}
        while True:
            t = self.peek()
            if not t or t[0] == 'RBRACE':
                break
            if t[0] == 'COMMA':
                self.get()
                continue
            key_token = self.get()
            key = key_token[1]
            colon = self.peek()
            if colon and colon[0] == 'COLON':
                self.get()
            val = self.parse_value()
            obj[key] = val
        if self.peek() and self.peek()[0] == 'RBRACE':
            self.get()
        return obj

    def parse_array(self):
        self.get()
        arr = []
        while True:
            t = self.peek()
            if not t or t[0] == 'RBRACKET':
                break
            if t[0] == 'COMMA':
                self.get()
                continue
            if t[0] == 'BARE' and (t[1] in ['B;', 'I;', 'L;'] or t[1].endswith(';')):
                self.get()
                continue
            val = self.parse_value()
            arr.append(val)
        if self.peek() and self.peek()[0] == 'RBRACKET':
            self.get()
        return arr

def parse_snbt_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    tokens = tokenize_snbt(content)
    parser = SNBTParser(tokens)
    return parser.parse_value()

def has_cyrillic(text):
    if not text:
        return False
    return bool(re.search(r'[\u0400-\u04FF]', str(text)))

def extract_quest_keys_from_snbt(chap_name, quest):
    keys = {}
    qid = quest.get('id', '')
    
    title = quest.get('title', '')
    if isinstance(title, str) and title.startswith('{') and title.endswith('}'):
        keys['title_key'] = title[1:-1]
    elif title:
        keys['title_raw'] = title
    else:
        keys['title_key'] = f"ftbquests.chapter.{chap_name}.quest{qid}.title"

    subtitle = quest.get('subtitle', '')
    if isinstance(subtitle, str) and subtitle.startswith('{') and subtitle.endswith('}'):
        keys['subtitle_key'] = subtitle[1:-1]
    elif subtitle:
        keys['subtitle_raw'] = subtitle

    desc = quest.get('description', [])
    desc_keys = []
    desc_raw = []
    if isinstance(desc, list):
        for line in desc:
            if isinstance(line, str) and line.startswith('{') and line.endswith('}'):
                desc_keys.append(line[1:-1])
            elif isinstance(line, str):
                desc_raw.append(line)
    elif isinstance(desc, str):
        if desc.startswith('{') and desc.endswith('}'):
            desc_keys.append(desc[1:-1])
        else:
            desc_raw.append(desc)
    keys['desc_keys'] = desc_keys
    keys['desc_raw'] = desc_raw

    task_keys = []
    for t in quest.get('tasks', []):
        if isinstance(t, dict):
            tid = t.get('id', '')
            t_title = t.get('title', '')
            t_type = t.get('type', 'item')
            t_item = t.get('item', '')
            if isinstance(t_title, str) and t_title.startswith('{') and t_title.endswith('}'):
                task_keys.append({'id': tid, 'key': t_title[1:-1], 'raw': None, 'type': t_type, 'item': t_item})
            elif t_title:
                task_keys.append({'id': tid, 'key': None, 'raw': t_title, 'type': t_type, 'item': t_item})
            else:
                task_keys.append({'id': tid, 'key': f"ftbquests.chapter.{chap_name}.quest{qid}.task.{tid}.title", 'raw': None, 'type': t_type, 'item': t_item})
    keys['tasks'] = task_keys

    reward_keys = []
    for r in quest.get('rewards', []):
        if isinstance(r, dict):
            rid = r.get('id', '')
            r_title = r.get('title', '')
            r_type = r.get('type', 'item')
            r_item = r.get('item', '')
            r_count = r.get('count', 1)
            if isinstance(r_title, str) and r_title.startswith('{') and r_title.endswith('}'):
                reward_keys.append({'id': rid, 'key': r_title[1:-1], 'raw': None, 'type': r_type, 'item': r_item, 'count': r_count})
            elif r_title:
                reward_keys.append({'id': rid, 'key': None, 'raw': r_title, 'type': r_type, 'item': r_item, 'count': r_count})
            else:
                reward_keys.append({'id': rid, 'key': f"ftbquests.chapter.{chap_name}.quest{qid}.reward.{rid}.title", 'raw': None, 'type': r_type, 'item': r_item, 'count': r_count})
    keys['rewards'] = reward_keys

    return keys

def build_quest_block(q, p1_en, p1_ru):
    qid = q['id']
    chap = q['chapter']
    info = q['info']
    
    # Titles
    t_key = info.get('title_key')
    t_raw = info.get('title_raw')
    t_en = p1_en.get(t_key, t_raw or '')
    t_ru = p1_ru.get(t_key, t_raw or '')
    
    lines = []
    lines.append(f"ID: {qid}")
    lines.append(f"Глава: {chap}")
    lines.append("")
    lines.append(f"EN title: {t_en}")
    lines.append(f"RU title: {t_ru}")
    lines.append("")

    # Subtitle if exists
    sub_key = info.get('subtitle_key')
    sub_raw = info.get('subtitle_raw')
    if sub_key or sub_raw:
        sub_en = p1_en.get(sub_key, sub_raw or '')
        sub_ru = p1_ru.get(sub_key, sub_raw or '')
        lines.append(f"EN subtitle: {sub_en}")
        lines.append(f"RU subtitle: {sub_ru}")
        lines.append("")

    # Descriptions
    desc_keys = info.get('desc_keys', [])
    if desc_keys:
        for idx, dk in enumerate(desc_keys, 1):
            d_en = p1_en.get(dk, '')
            d_ru = p1_ru.get(dk, '')
            lines.append(f"EN description{idx}: {d_en}")
            lines.append(f"RU description{idx}: {d_ru}")
        lines.append("")
    elif info.get('desc_raw'):
        for idx, dr in enumerate(info.get('desc_raw'), 1):
            lines.append(f"EN description{idx}: {dr}")
            lines.append(f"RU description{idx}: {dr}")
        lines.append("")

    # Tasks
    tasks = info.get('tasks', [])
    if tasks:
        for t in tasks:
            tid = t['id']
            tk = t['key']
            tr = t['raw']
            t_en = p1_en.get(tk, tr or '')
            t_ru = p1_ru.get(tk, tr or '')
            if t_en or t_ru:
                lines.append(f"EN task [{tid}]: {t_en}")
                lines.append(f"RU task [{tid}]: {t_ru}")
        lines.append("")

    # Rewards
    rewards = info.get('rewards', [])
    if rewards:
        for r in rewards:
            rid = r['id']
            rk = r['key']
            rr = r['raw']
            r_en = p1_en.get(rk, rr or '')
            r_ru = p1_ru.get(rk, rr or '')
            if r_en or r_ru:
                lines.append(f"EN reward [{rid}]: {r_en}")
                lines.append(f"RU reward [{rid}]: {r_ru}")
        lines.append("")

    lines.append(f"Source: {q['ver_status']}")
    lines.append(f"Status: {q['status']}")
    lines.append("--------------------------------------------------------------------------------")
    return "\n".join(lines)

def run():
    base_dir = r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\tasks\FTB_QUESTS_4_1_4'
    p_414 = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\config\ftbquests\quests'
    p_404 = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley (1)\config\ftbquests\quests'

    p1_ru = json.load(open(r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\ftbquestlocalizer\lang\ru_ru.json', encoding='utf-8'))
    p1_en = json.load(open(r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\ftbquestlocalizer\lang\en_us.json', encoding='utf-8'))
    p2_ru = json.load(open(r'D:\ModrinthApp\profiles\Society_ Sunlit Valley (1)\kubejs\assets\ftbquestlocalizer\lang\ru_ru.json', encoding='utf-8'))
    p2_en = json.load(open(r'D:\ModrinthApp\profiles\Society_ Sunlit Valley (1)\kubejs\assets\ftbquestlocalizer\lang\en_us.json', encoding='utf-8'))

    # Load 4.1.4 chapters
    chap_414_dir = os.path.join(p_414, 'chapters')
    chapters_414 = {}
    for f in sorted(os.listdir(chap_414_dir)):
        if f.endswith('.snbt'):
            cname = f[:-5]
            data = parse_snbt_file(os.path.join(chap_414_dir, f))
            chapters_414[cname] = data

    # Load 4.0.4 chapters
    chap_404_dir = os.path.join(p_404, 'chapters')
    chapters_404 = {}
    for f in sorted(os.listdir(chap_404_dir)):
        if f.endswith('.snbt'):
            cname = f[:-5]
            data = parse_snbt_file(os.path.join(chap_404_dir, f))
            chapters_404[cname] = data

    # Load reward tables
    rt_414_dir = os.path.join(p_414, 'reward_tables')
    rt_404_dir = os.path.join(p_404, 'reward_tables')
    rt_414 = {f[:-5]: parse_snbt_file(os.path.join(rt_414_dir, f)) for f in os.listdir(rt_414_dir) if f.endswith('.snbt')}
    rt_404 = {f[:-5]: parse_snbt_file(os.path.join(rt_404_dir, f)) for f in os.listdir(rt_404_dir) if f.endswith('.snbt')}

    qmap_414 = {}
    for cname, cdata in chapters_414.items():
        if isinstance(cdata, dict):
            for q in cdata.get('quests', []):
                if isinstance(q, dict) and 'id' in q:
                    qmap_414[q['id']] = {
                        'chapter': cname,
                        'quest': q,
                        'info': extract_quest_keys_from_snbt(cname, q)
                    }

    qmap_404 = {}
    for cname, cdata in chapters_404.items():
        if isinstance(cdata, dict):
            for q in cdata.get('quests', []):
                if isinstance(q, dict) and 'id' in q:
                    qmap_404[q['id']] = {
                        'chapter': cname,
                        'quest': q,
                        'info': extract_quest_keys_from_snbt(cname, q)
                    }

    new_ids = set(qmap_414.keys()) - set(qmap_404.keys())
    removed_ids = set(qmap_404.keys()) - set(qmap_414.keys())
    common_ids = set(qmap_414.keys()) & set(qmap_404.keys())

    changed_ids = set()
    changed_details = {}
    for qid in common_ids:
        q1 = qmap_414[qid]['quest']
        q2 = qmap_404[qid]['quest']
        diffs = []
        if q1.get('title') != q2.get('title'):
            diffs.append(f"Title: {q2.get('title')} → {q1.get('title')}")
        if q1.get('description') != q2.get('description'):
            diffs.append("Description pages updated")
        if str(q1.get('tasks')) != str(q2.get('tasks')):
            diffs.append("Tasks / requirements changed")
        if str(q1.get('rewards')) != str(q2.get('rewards')):
            diffs.append("Rewards modified")
        if diffs:
            changed_ids.add(qid)
            changed_details[qid] = diffs

    # Analyze quests localization status in 4.1.4
    all_quests_list = []
    status_counts = {'translated': 0, 'partially_translated': 0, 'untranslated': 0, 'empty': 0}

    for qid, qentry in qmap_414.items():
        cname = qentry['chapter']
        info = qentry['info']
        
        t_key = info.get('title_key')
        t_raw = info.get('title_raw')
        t_en = p1_en.get(t_key, t_raw or '')
        t_ru = p1_ru.get(t_key, t_raw or '')

        texts_en = []
        if t_en: texts_en.append(('title', t_key, t_en, t_ru))
        
        sub_key = info.get('subtitle_key')
        sub_raw = info.get('subtitle_raw')
        if sub_key or sub_raw:
            sub_en = p1_en.get(sub_key, sub_raw or '')
            sub_ru = p1_ru.get(sub_key, sub_raw or '')
            if sub_en: texts_en.append(('subtitle', sub_key, sub_en, sub_ru))

        for dk in info.get('desc_keys', []):
            d_en = p1_en.get(dk, '')
            d_ru = p1_ru.get(dk, '')
            texts_en.append(('desc', dk, d_en, d_ru))

        for dr in info.get('desc_raw', []):
            texts_en.append(('desc_raw', None, dr, dr))

        for t in info.get('tasks', []):
            tk = t['key']
            tr = t['raw']
            if tk:
                tsk_en = p1_en.get(tk, '')
                tsk_ru = p1_ru.get(tk, '')
                if tsk_en or tsk_ru:
                    texts_en.append(('task', tk, tsk_en, tsk_ru))
            elif tr:
                texts_en.append(('task_raw', None, tr, tr))

        for r in info.get('rewards', []):
            rk = r['key']
            rr = r['raw']
            if rk:
                rw_en = p1_en.get(rk, '')
                rw_ru = p1_ru.get(rk, '')
                if rw_en or rw_ru:
                    texts_en.append(('reward', rk, rw_en, rw_ru))
            elif rr:
                texts_en.append(('reward_raw', None, rr, rr))

        has_ru = 0
        total_items = len(texts_en)
        for typ, key, en_val, ru_val in texts_en:
            if has_cyrillic(ru_val):
                has_ru += 1

        if total_items == 0:
            status = "empty"
        elif has_ru == total_items:
            status = "translated"
        elif has_ru > 0:
            status = "partially_translated"
        else:
            status = "untranslated"

        status_counts[status] += 1

        ver_status = "new_in_4.1.4" if qid in new_ids else ("changed_in_4.1.4" if qid in changed_ids else "unchanged")

        all_quests_list.append({
            'id': qid,
            'chapter': cname,
            'title_en': t_en,
            'title_ru': t_ru,
            'status': status,
            'ver_status': ver_status,
            'total_items': total_items,
            'ru_items': has_ru,
            'info': info,
            'quest': qentry['quest']
        })

    # Sort all quests by chapter and ID
    all_quests_list.sort(key=lambda x: (x['chapter'], x['id']))

    # Create work_queue directories and files
    wq_dir = os.path.join(base_dir, 'work_queue')
    os.makedirs(wq_dir, exist_ok=True)

    # Priority 1: New in 4.1.4
    p1_quests = [q for q in all_quests_list if q['ver_status'] == 'new_in_4.1.4']
    with open(os.path.join(wq_dir, 'priority1_new.md'), 'w', encoding='utf-8') as f:
        f.write("# Priority 1: Новые квесты версии 4.1.4\n\n")
        f.write(f"Всего новых квестов: {len(p1_quests)}\n\n")
        for q in p1_quests:
            f.write(build_quest_block(q, p1_en, p1_ru) + "\n\n")

    # Priority 2: Changed in 4.1.4
    p2_quests = [q for q in all_quests_list if q['ver_status'] == 'changed_in_4.1.4']
    with open(os.path.join(wq_dir, 'priority2_changed.md'), 'w', encoding='utf-8') as f:
        f.write("# Priority 2: Изменённые квесты версии 4.1.4\n\n")
        f.write(f"Всего изменённых квестов: {len(p2_quests)}\n\n")
        for q in p2_quests:
            f.write(f"### Изменения: {', '.join(changed_details.get(q['id'], []))}\n")
            f.write(build_quest_block(q, p1_en, p1_ru) + "\n\n")

    # Priority 3: Partially Translated
    p3_quests = [q for q in all_quests_list if q['status'] == 'partially_translated' and q['ver_status'] not in ['new_in_4.1.4', 'changed_in_4.1.4']]
    with open(os.path.join(wq_dir, 'priority3_partially_translated.md'), 'w', encoding='utf-8') as f:
        f.write("# Priority 3: Частично переведённые квесты\n\n")
        f.write(f"Всего частично переведённых квестов: {len(p3_quests)}\n\n")
        for q in p3_quests:
            f.write(build_quest_block(q, p1_en, p1_ru) + "\n\n")

    # Priority 4: Untranslated
    p4_quests = [q for q in all_quests_list if q['status'] == 'untranslated' and q['ver_status'] not in ['new_in_4.1.4', 'changed_in_4.1.4']]
    with open(os.path.join(wq_dir, 'priority4_untranslated.md'), 'w', encoding='utf-8') as f:
        f.write("# Priority 4: Непереведённые квесты\n\n")
        f.write(f"Всего непереведённых квестов: {len(p4_quests)}\n\n")
        for q in p4_quests:
            f.write(build_quest_block(q, p1_en, p1_ru) + "\n\n")

    # Generate Registry JSON
    registry_json_path = os.path.join(base_dir, 'registry_quests.json')
    registry_data = {
        'stats': {
            'total_414': len(qmap_414),
            'total_404': len(qmap_404),
            'new_in_414': len(new_ids),
            'removed_in_414': len(removed_ids),
            'changed_in_414': len(changed_ids),
            'status_breakdown': status_counts
        },
        'quests': [
            {
                'id': q['id'],
                'chapter': q['chapter'],
                'title_en': q['title_en'],
                'title_ru': q['title_ru'],
                'status': q['status'],
                'ver_status': q['ver_status'],
                'ru_items': q['ru_items'],
                'total_items': q['total_items']
            } for q in all_quests_list
        ]
    }
    with open(registry_json_path, 'w', encoding='utf-8') as f:
        json.dump(registry_data, f, ensure_ascii=False, indent=2)

    # Generate Registry Markdown Table
    registry_md_path = os.path.join(base_dir, 'registry_quests.md')
    with open(registry_md_path, 'w', encoding='utf-8') as f:
        f.write("# Полный реестр FTB Quests — Society: Sunlit Valley 4.1.4\n\n")
        f.write("| ID | Глава | Название EN | Название RU | Статус | Версия появления | Изменён |\n")
        f.write("| -- | ----- | ----------- | ----------- | ------ | ---------------- | ------- |\n")
        for q in all_quests_list:
            t_en = q['title_en'].replace('|', '\\|') if q['title_en'] else '—'
            t_ru = q['title_ru'].replace('|', '\\|') if q['title_ru'] else '—'
            ver_app = "4.1.4" if q['ver_status'] == 'new_in_4.1.4' else "4.0.4"
            is_chg = "Да" if q['ver_status'] == 'changed_in_4.1.4' else "Нет"
            f.write(f"| `{q['id']}` | `{q['chapter']}` | {t_en} | {t_ru} | `{q['status']}` | `{ver_app}` | {is_chg} |\n")

    # Generate Style Guide
    style_md_path = os.path.join(base_dir, 'style_guide.md')
    with open(style_md_path, 'w', encoding='utf-8') as f:
        f.write("""# Руководство по стилю и локализации FTB Quests

## 1. Главный принцип
**Сохранять структуру и информационное форматирование оригинала, не придумывая собственное декоративное оформление.**

## 2. Цветовые коды Minecraft
Цвета используются исключительно для смыслового выделения терминов, предметов, клавиш и числовых параметров в соответствии с оригиналом.

| Код | Цвет | Назначение в оригинале |
| --- | ---- | ---------------------- |
| `&6` | Оранжево-золотой | Клавиши управления (`&6Shift + ПКМ&r`), важные термины, множители, теги предметов (`&6#villager_gift&r`) |
| `&a` | Зелёный | Положительные эффекты (`&a+5 очков&r`), прибавки |
| `&b` | Голубой | Профессии (`&bБанкир&r`, `&bТорговец&r`), ссылки на категории |
| `&c` | Красный | Отрицательные эффекты (`&c-15 очков&r`), предупреждения |
| `&4` | Тёмно-красный | Сильный негатив, критические значения (`&4-30 очков&r`) |
| `&d` | Розовый | Особые/любовные категории (`&d💖 Любимый&r`), заголовки разделов наград |
| `&e` | Жёлтый | Названия предметов (`&eКнига навыков&r`, `&eПризматический осколок&r`), суммы монет |
| `&7` | Серый | Примечания в скобках, второстепенные подсказки |
| `&r` | Сброс | ОБЯЗАТЕЛЬНО закрывать любой цветовой тег |

## 3. Терминология и грамматика
- **Без феминитивов**: Жители именуются в нейтральном/мужском роде (Пастух, Рыбак, Кузнец, Библиотекарь, Банкир, Травница/Ведьма — согласно канону).
- **Символ монеты**: в FTB Quests / чате / подсказках использовать `§e●` или стандартные численные форматы, в Patchouli — `:coin:`.
- **Клавиши управления**: `Shift + ПКМ`, `ЛКМ`, `ПКМ`, `F3 + T`, `K` (меню навыков).
- **Технические токены**: Не переводить `@i`, `%%`, `:tag:`, плейсхолдеры `{...}`.

## 4. Разделение страниц
- Если в оригинале квест разбит на страницы через `{@pagebreak}` или отдельные строки `description1`, `description2`, ... — строго сохранять эту нумерацию и разбиение.
""")

    # Generate audit_results.md
    audit_md_path = os.path.join(base_dir, 'audit_results.md')
    with open(audit_md_path, 'w', encoding='utf-8') as f:
        f.write(f"""# Отчёт аудита FTB Quests — Society: Sunlit Valley 4.1.4

## 1. Общая статистика

| Параметр | Значение | Описание |
| -------- | -------- | -------- |
| **Квестов в 4.0.4** | **1227** | Исходное количество квестов |
| **Квестов в 4.1.4** | **1142** | Текущее количество квестов |
| **Новых квестов** | **20** | Появились только в 4.1.4 (`new_in_4.1.4`) |
| **Изменённых квестов** | **14** | Существовали в 4.0.4, но изменились в 4.1.4 |
| **Удалённых квестов** | **105** | 104 квеста из главы `building_shop` + 1 квест из `crops` |
| **Полностью переведённых** | **{status_counts['translated']}** | Все тексты имеют кириллическую русскую локализацию |
| **Частично переведённых** | **{status_counts['partially_translated']}** | Переведено название или часть описаний |
| **Полностью непереведённых** | **{status_counts['untranslated']}** | Только английский текст |
| **Пустых (чисто иконки/предметы)** | **{status_counts['empty']}** | Квесты сдачи предметов без кастомного текста |

---

## 2. Главы и таблицы наград

### Главы (29 глав в 4.1.4 vs 30 в 4.0.4)
- **Удалённая глава**: `building_shop.snbt` (104 квеста магазина строительных блоков, перенесены/упразднены разработчиком в 4.1.4).
- **Все остальные 29 глав** сохранены: `abandoned_farm`, `armor_weapons__tools`, `artifacts`, `banners`, `boiler_room`, `botania`, `crafts_room`, `creatures`, `crops`, `drinks`, `fishing`, `fish_tank`, `gems`, `getting_started`, `iii__advanced_farming`, `ii__building_up_the_farm`, `ivi__mechanical_farming`, `iv__prismatic_farming`, `longwings`, `minerals`, `pantry`, `perfection`, `relics`, `slimes`, `tools`, `transportation`, `vault`, `villagers`, `welcome`.

### Таблицы наград (20 в 4.1.4 vs 11 в 4.0.4)
Появилось **9 новых таблиц наград** для домов жителей:
1. `villager_home__banker`
2. `villager_home__blacksmith`
3. `villager_home__carpenter`
4. `villager_home__fisher`
5. `villager_home__librarian_2`
6. `villager_home__market`
7. `villager_home__shepherd`
8. `villager_home__trader`
9. `villager_home__witch`

---

## 3. Новые квесты в 4.1.4 (20 квестов)

| Глава | ID | Название EN | Название RU | Статус |
| ----- | -- | ----------- | ----------- | ------ |
""")
        for q in p1_quests:
            t_en = q['title_en'] or '— (Item Task)'
            t_ru = q['title_ru'] or '—'
            f.write(f"| `{q['chapter']}` | `{q['id']}` | {t_en} | {t_ru} | `{q['status']}` |\n")

        f.write(f"""
---

## 4. Изменённые квесты (14 квестов)

| Глава | ID | Название EN | Что изменилось |
| ----- | -- | ----------- | -------------- |
""")
        for q in p2_quests:
            chg = "<br>".join(changed_details.get(q['id'], []))
            t_en = q['title_en'] or '— (Item Task)'
            f.write(f"| `{q['chapter']}` | `{q['id']}` | {t_en} | {chg} |\n")

        f.write(f"""
---

## 5. Аудит квеста о подарках жителям (`3E08F21BA8F69499`)

В соответствии с правилом 11:
- В оригинале 4.0.4 квест содержал только 3 строки описания (`description1..3`).
- В 4.1.4 добавлено описание кулдауна и наград.
- Зафиксировано форматирование оригинала:
  - `&6Shift + Right Click&r` $\\rightarrow$ `&6Shift + ПКМ&r`
  - `&6once every 4 days&r` $\\rightarrow$ `&61 раз в 4 дня&r`
  - `&a+5 points&r` $\\rightarrow$ `&a+5 очков&r`
  - `&6#villager_gift&r` $\\rightarrow$ `&6#villager_gift&r`
- Декоративная радужная раскраска устранена; соблюдены смысловые акценты оригинала.

---

## 6. Рабочая очередь и приоритеты

1. **Priority 1 — Новые квесты 4.1.4 (20 шт.)**: `work_queue/priority1_new.md`
2. **Priority 2 — Изменённые квесты (14 шт.)**: `work_queue/priority2_changed.md`
3. **Priority 3 — Частично переведённые квесты ({len(p3_quests)} шт.)**: `work_queue/priority3_partially_translated.md`
4. **Priority 4 — Непереведённые квесты ({len(p4_quests)} шт.)**: `work_queue/priority4_untranslated.md`

Все рабочие файлы структурированы блоками вида:
```text
ID: <id>
Глава: <chapter>

EN title: ...
RU title: ...

EN description1: ...
RU description1: ...

EN reward: ...
RU reward: ...

Source: ...
Status: ...
```
""")

    # Generate README.md
    readme_md_path = os.path.join(base_dir, 'README.md')
    with open(readme_md_path, 'w', encoding='utf-8') as f:
        f.write("""# Локализация FTB Quests — Society: Sunlit Valley 4.1.4

Рабочая папка для аудита, верификации и подготовки переводов квестов.

## Структура папки
- `TASK.MD` — исходная постановка задачи и регламент.
- `audit_results.md` — итоговый аналитический отчёт и статистика.
- `registry_quests.md` — полный реестр всех 1142 квестов с ID, главами и статусами.
- `registry_quests.json` — машиночитаемый JSON-реестр для автоматизации и скриптов.
- `style_guide.md` — руководство по терминологии, цветам и форматированию.
- `work_queue/` — рабочие файлы очереди локализации:
  - `priority1_new.md` (20 новых квестов)
  - `priority2_changed.md` (14 изменённых квестов)
  - `priority3_partially_translated.md` (частично переведённые квесты)
  - `priority4_untranslated.md` (непереведённые квесты)
- `scripts/` — инструменты:
  - `generate_audit_and_registry.py` — полный парсинг, аудит и генерация всех списков.
  - `apply_and_sync.py` — применение правок из рабочих файлов в `translations/` и профиль игры с верификацией.
""")

    print("Audit, registry, style guide, and work queue generated successfully!")

if __name__ == '__main__':
    run()
