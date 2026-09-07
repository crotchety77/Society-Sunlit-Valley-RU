import os
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

from audit_ftb_quests import parse_snbt_file

def audit_p1():
    base_dir = r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\tasks\FTB_QUESTS_4_1_4'
    p_414 = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\config\ftbquests\quests'
    p1_ru = json.load(open(r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\ftbquestlocalizer\lang\ru_ru.json', encoding='utf-8'))
    p1_en = json.load(open(r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\ftbquestlocalizer\lang\en_us.json', encoding='utf-8'))

    with open(os.path.join(base_dir, 'registry_quests.json'), 'r', encoding='utf-8') as f:
        reg = json.load(f)

    new_quests_meta = [q for q in reg['quests'] if q['ver_status'] == 'new_in_4.1.4']

    # Load SNBT for detailed inspection
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

    detailed_p1 = []

    for qm in new_quests_meta:
        qid = qm['id']
        cname, qobj = q_snbt_map[qid]

        # Extract all fields
        title_raw = qobj.get('title', '')
        subtitle_raw = qobj.get('subtitle', '')
        desc_raw = qobj.get('description', [])
        tasks_raw = qobj.get('tasks', [])
        rewards_raw = qobj.get('rewards', [])

        # Keys
        t_key = f"ftbquests.chapter.{cname}.quest{qid}.title" if not (isinstance(title_raw, str) and title_raw.startswith('{')) else title_raw[1:-1]
        sub_key = f"ftbquests.chapter.{cname}.quest{qid}.subtitle" if not (isinstance(subtitle_raw, str) and subtitle_raw.startswith('{')) else subtitle_raw[1:-1]

        t_en = p1_en.get(t_key, title_raw if not title_raw.startswith('{') else '')
        t_ru = p1_ru.get(t_key, '')

        sub_en = p1_en.get(sub_key, subtitle_raw if not subtitle_raw.startswith('{') else '')
        sub_ru = p1_ru.get(sub_key, '')

        # Descriptions
        desc_list = []
        if isinstance(desc_raw, list):
            for idx, item in enumerate(desc_raw, 1):
                if isinstance(item, str) and item.startswith('{') and item.endswith('}'):
                    k = item[1:-1]
                    d_en = p1_en.get(k, '')
                    d_ru = p1_ru.get(k, '')
                    desc_list.append({'idx': idx, 'key': k, 'en': d_en, 'ru': d_ru})
                elif isinstance(item, str):
                    desc_list.append({'idx': idx, 'key': None, 'en': item, 'ru': ''})
        elif isinstance(desc_raw, str):
            if desc_raw.startswith('{') and desc_raw.endswith('}'):
                k = desc_raw[1:-1]
                desc_list.append({'idx': 1, 'key': k, 'en': p1_en.get(k, ''), 'ru': p1_ru.get(k, '')})
            else:
                desc_list.append({'idx': 1, 'key': None, 'en': desc_raw, 'ru': ''})

        # Tasks
        task_list = []
        for t in tasks_raw:
            if isinstance(t, dict):
                tid = t.get('id', '')
                ttitle = t.get('title', '')
                ttype = t.get('type', 'item')
                titem = t.get('item', '')
                if isinstance(ttitle, str) and ttitle.startswith('{') and ttitle.endswith('}'):
                    tk = ttitle[1:-1]
                    task_list.append({'id': tid, 'key': tk, 'en': p1_en.get(tk, ''), 'ru': p1_ru.get(tk, ''), 'type': ttype, 'item': titem})
                elif ttitle:
                    task_list.append({'id': tid, 'key': None, 'en': ttitle, 'ru': '', 'type': ttype, 'item': titem})
                else:
                    tk = f"ftbquests.chapter.{cname}.quest{qid}.task.{tid}.title"
                    task_list.append({'id': tid, 'key': tk, 'en': p1_en.get(tk, ''), 'ru': p1_ru.get(tk, ''), 'type': ttype, 'item': titem})

        # Rewards
        reward_list = []
        for r in rewards_raw:
            if isinstance(r, dict):
                rid = r.get('id', '')
                rtitle = r.get('title', '')
                rtype = r.get('type', 'item')
                ritem = r.get('item', '')
                rcount = r.get('count', 1)
                if isinstance(rtitle, str) and rtitle.startswith('{') and rtitle.endswith('}'):
                    rk = rtitle[1:-1]
                    reward_list.append({'id': rid, 'key': rk, 'en': p1_en.get(rk, ''), 'ru': p1_ru.get(rk, ''), 'type': rtype, 'item': ritem, 'count': rcount})
                elif rtitle:
                    reward_list.append({'id': rid, 'key': None, 'en': rtitle, 'ru': '', 'type': rtype, 'item': ritem, 'count': rcount})
                else:
                    rk = f"ftbquests.chapter.{cname}.quest{qid}.reward.{rid}.title"
                    reward_list.append({'id': rid, 'key': rk, 'en': p1_en.get(rk, ''), 'ru': p1_ru.get(rk, ''), 'type': rtype, 'item': ritem, 'count': rcount})

        # Categorize scope
        has_title = bool(t_en)
        has_sub = bool(sub_en)
        has_desc = any(bool(d['en']) for d in desc_list)
        has_custom_tasks = any(bool(t['en']) for t in task_list if t['type'] != 'item' or t['en'])
        has_custom_rewards = any(bool(r['en']) for r in reward_list if r['en'])

        if has_title and has_desc:
            scope = 'full_text'
        elif has_title or has_desc or has_sub or has_custom_tasks or has_custom_rewards:
            scope = 'partial_text'
        elif len(task_list) > 0 and all(t['type'] in ['item', 'stat', 'observation', 'advancement'] and not t['en'] for t in task_list):
            scope = 'item_only'
        else:
            scope = 'no_translation_needed'

        detailed_p1.append({
            'id': qid,
            'chapter': cname,
            'scope': scope,
            'title': {'key': t_key, 'en': t_en, 'ru': t_ru},
            'subtitle': {'key': sub_key, 'en': sub_en, 'ru': sub_ru},
            'descriptions': desc_list,
            'tasks': task_list,
            'rewards': reward_list,
            'raw_quest': qobj
        })

    # Print summary
    print(f"=== SUMMARY OF 20 NEW QUESTS IN 4.1.4 ===")
    scope_counts = {}
    for q in detailed_p1:
        scope_counts[q['scope']] = scope_counts.get(q['scope'], 0) + 1
        print(f"[{q['chapter']}] ID: {q['id']} | Scope: {q['scope']} | Title EN: '{q['title']['en']}'")

    print("\nScope counts:", scope_counts)

if __name__ == '__main__':
    audit_p1()
