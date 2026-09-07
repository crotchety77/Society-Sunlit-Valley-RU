import os
import re
import json

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
    """
    Returns list of keys and localizable fields.
    """
    keys = {}
    qid = quest.get('id', '')
    
    # Title
    title = quest.get('title', '')
    if isinstance(title, str) and title.startswith('{') and title.endswith('}'):
        k = title[1:-1]
        keys['title_key'] = k
    elif title:
        keys['title_raw'] = title
    else:
        # Default key convention in ftbquestlocalizer
        keys['title_key'] = f"ftbquests.chapter.{chap_name}.quest{qid}.title"

    # Subtitle
    subtitle = quest.get('subtitle', '')
    if isinstance(subtitle, str) and subtitle.startswith('{') and subtitle.endswith('}'):
        keys['subtitle_key'] = subtitle[1:-1]
    elif subtitle:
        keys['subtitle_raw'] = subtitle

    # Description
    desc = quest.get('description', [])
    desc_keys = []
    desc_raw = []
    if isinstance(desc, list):
        for idx, line in enumerate(desc, 1):
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

    # Tasks
    task_keys = []
    for t in quest.get('tasks', []):
        if isinstance(t, dict):
            tid = t.get('id', '')
            t_title = t.get('title', '')
            if isinstance(t_title, str) and t_title.startswith('{') and t_title.endswith('}'):
                task_keys.append((tid, t_title[1:-1], None))
            elif t_title:
                task_keys.append((tid, None, t_title))
            else:
                task_keys.append((tid, f"ftbquests.chapter.{chap_name}.quest{qid}.task.{tid}.title", None))
    keys['tasks'] = task_keys

    # Rewards
    reward_keys = []
    for r in quest.get('rewards', []):
        if isinstance(r, dict):
            rid = r.get('id', '')
            r_title = r.get('title', '')
            if isinstance(r_title, str) and r_title.startswith('{') and r_title.endswith('}'):
                reward_keys.append((rid, r_title[1:-1], None))
            elif r_title:
                reward_keys.append((rid, None, r_title))
    keys['rewards'] = reward_keys

    return keys

def main():
    p_414 = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\config\ftbquests\quests'
    p_404 = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley (1)\config\ftbquests\quests'

    p1_ru_path = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\ftbquestlocalizer\lang\ru_ru.json'
    p1_en_path = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\ftbquestlocalizer\lang\en_us.json'
    p2_ru_path = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley (1)\kubejs\assets\ftbquestlocalizer\lang\ru_ru.json'
    p2_en_path = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley (1)\kubejs\assets\ftbquestlocalizer\lang\en_us.json'

    p1_ru = json.load(open(p1_ru_path, encoding='utf-8'))
    p1_en = json.load(open(p1_en_path, encoding='utf-8'))
    p2_ru = json.load(open(p2_ru_path, encoding='utf-8'))
    p2_en = json.load(open(p2_en_path, encoding='utf-8'))

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

    # Quests map: qid -> {chapter, quest_obj, keys}
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

    # Check changed quests in common
    changed_ids = set()
    for qid in common_ids:
        q1 = qmap_414[qid]['quest']
        q2 = qmap_404[qid]['quest']
        # compare key attributes
        desc1 = q1.get('description', [])
        desc2 = q2.get('description', [])
        title1 = q1.get('title', '')
        title2 = q2.get('title', '')
        tasks1 = str(q1.get('tasks', []))
        tasks2 = str(q2.get('tasks', []))
        rew1 = str(q1.get('rewards', []))
        rew2 = str(q2.get('rewards', []))
        if desc1 != desc2 or title1 != title2 or tasks1 != tasks2 or rew1 != rew2:
            changed_ids.add(qid)

    print(f"Total quests in 4.1.4: {len(qmap_414)}")
    print(f"Total quests in 4.0.4: {len(qmap_404)}")
    print(f"New quests in 4.1.4: {len(new_ids)}")
    print(f"Removed quests: {len(removed_ids)}")
    print(f"Changed quests: {len(changed_ids)}")
    print(f"Unchanged quests: {len(common_ids - changed_ids)}")

    # Check translation status in 4.1.4 for all quests
    translated_count = 0
    partial_count = 0
    untranslated_count = 0

    quest_status_list = []

    for qid, data in qmap_414.items():
        cname = data['chapter']
        info = data['info']
        
        # Check all texts associated with this quest
        texts_en = []
        texts_ru = []

        # Title
        t_key = info.get('title_key')
        t_raw = info.get('title_raw')
        t_en = p1_en.get(t_key, t_raw or '')
        t_ru = p1_ru.get(t_key, t_raw or '')
        if t_en: texts_en.append(('title', t_key, t_en, t_ru))

        # Subtitle
        sub_key = info.get('subtitle_key')
        sub_raw = info.get('subtitle_raw')
        if sub_key or sub_raw:
            sub_en = p1_en.get(sub_key, sub_raw or '')
            sub_ru = p1_ru.get(sub_key, sub_raw or '')
            if sub_en: texts_en.append(('subtitle', sub_key, sub_en, sub_ru))

        # Descriptions
        for dk in info.get('desc_keys', []):
            d_en = p1_en.get(dk, '')
            d_ru = p1_ru.get(dk, '')
            texts_en.append(('desc', dk, d_en, d_ru))
        for dr in info.get('desc_raw', []):
            texts_en.append(('desc_raw', None, dr, dr))

        # Tasks
        for tid, tk, tr in info.get('tasks', []):
            if tk:
                tsk_en = p1_en.get(tk, '')
                tsk_ru = p1_ru.get(tk, '')
                if tsk_en or tsk_ru:
                    texts_en.append(('task', tk, tsk_en, tsk_ru))
            elif tr:
                texts_en.append(('task_raw', None, tr, tr))

        # Rewards
        for rid, rk, rr in info.get('rewards', []):
            if rk:
                rw_en = p1_en.get(rk, '')
                rw_ru = p1_ru.get(rk, '')
                if rw_en or rw_ru:
                    texts_en.append(('reward', rk, rw_en, rw_ru))
            elif rr:
                texts_en.append(('reward_raw', None, rr, rr))

        # Evaluation
        has_ru = 0
        total_translatable = len(texts_en)
        has_en = 0
        for typ, key, en_val, ru_val in texts_en:
            if has_cyrillic(ru_val):
                has_ru += 1
            elif ru_val and ru_val != en_val:
                # might be translated without cyrillic (rare)
                pass
            else:
                has_en += 1

        if total_translatable == 0:
            status = "empty"
        elif has_ru == total_translatable:
            status = "translated"
            translated_count += 1
        elif has_ru > 0:
            status = "partially_translated"
            partial_count += 1
        else:
            status = "untranslated"
            untranslated_count += 1

        ver_status = "new_in_4.1.4" if qid in new_ids else ("changed_in_4.1.4" if qid in changed_ids else "unchanged")

        quest_status_list.append({
            'id': qid,
            'chapter': cname,
            'title_en': t_en,
            'title_ru': t_ru,
            'status': status,
            'ver_status': ver_status,
            'total_items': total_translatable,
            'ru_items': has_ru,
            'texts': texts_en
        })

    print(f"\n--- 4.1.4 Localization Status ---")
    print(f"Fully Translated: {translated_count}")
    print(f"Partially Translated: {partial_count}")
    print(f"Untranslated: {untranslated_count}")

    # Breakdown of new quests
    print(f"\n--- New Quests in 4.1.4 ({len(new_ids)}) ---")
    for q in quest_status_list:
        if q['ver_status'] == 'new_in_4.1.4':
            print(f"[{q['chapter']}] ID: {q['id']} | EN: '{q['title_en']}' | RU: '{q['title_ru']}' | Status: {q['status']}")

    # Breakdown of changed quests
    print(f"\n--- Changed Quests in 4.1.4 ({len(changed_ids)}) ---")
    for q in quest_status_list:
        if q['ver_status'] == 'changed_in_4.1.4':
            print(f"[{q['chapter']}] ID: {q['id']} | EN: '{q['title_en']}' | RU: '{q['title_ru']}' | Status: {q['status']}")

if __name__ == '__main__':
    main()
