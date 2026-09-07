import os
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
from audit_ftb_quests import parse_snbt_file, extract_quest_keys_from_snbt, has_cyrillic

def analyze_all():
    p_414 = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\config\ftbquests\quests'
    p_404 = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley (1)\config\ftbquests\quests'

    p1_ru = json.load(open(r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\ftbquestlocalizer\lang\ru_ru.json', encoding='utf-8'))
    p1_en = json.load(open(r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\ftbquestlocalizer\lang\en_us.json', encoding='utf-8'))
    p2_ru = json.load(open(r'D:\ModrinthApp\profiles\Society_ Sunlit Valley (1)\kubejs\assets\ftbquestlocalizer\lang\ru_ru.json', encoding='utf-8'))
    p2_en = json.load(open(r'D:\ModrinthApp\profiles\Society_ Sunlit Valley (1)\kubejs\assets\ftbquestlocalizer\lang\en_us.json', encoding='utf-8'))

    # Reward tables diff
    rt_414_dir = os.path.join(p_414, 'reward_tables')
    rt_404_dir = os.path.join(p_404, 'reward_tables')
    rt_414 = {f[:-5]: parse_snbt_file(os.path.join(rt_414_dir, f)) for f in os.listdir(rt_414_dir) if f.endswith('.snbt')}
    rt_404 = {f[:-5]: parse_snbt_file(os.path.join(rt_404_dir, f)) for f in os.listdir(rt_404_dir) if f.endswith('.snbt')}

    print("=== REWARD TABLES DIFF ===")
    print("New reward tables in 4.1.4:", set(rt_414.keys()) - set(rt_404.keys()))
    print("Removed reward tables in 4.1.4:", set(rt_404.keys()) - set(rt_414.keys()))

    # Chapter groups diff
    cg_414 = parse_snbt_file(os.path.join(p_414, 'chapter_groups.snbt'))
    cg_404 = parse_snbt_file(os.path.join(p_404, 'chapter_groups.snbt'))
    print("=== CHAPTER GROUPS ===")
    print("4.1.4 chapter groups:", [g.get('title') or g.get('id') for g in cg_414.get('chapter_groups', [])])
    print("4.0.4 chapter groups:", [g.get('title') or g.get('id') for g in cg_404.get('chapter_groups', [])])

    # Analyze gift quest specifically
    gift_id = "3E08F21BA8F69499"
    print("\n=== GIFT QUEST (3E08F21BA8F69499) ===")
    for k, v in sorted(p1_en.items()):
        if gift_id in k:
            print(f"EN [{k}] = {repr(v)}")
            print(f"RU [{k}] = {repr(p1_ru.get(k, '<MISSING>'))}")

    # Analyze changed quests
    print("\n=== CHANGED QUESTS DETAILED DIFF ===")
    chap_414_dir = os.path.join(p_414, 'chapters')
    chap_404_dir = os.path.join(p_404, 'chapters')
    chaps_414 = {f[:-5]: parse_snbt_file(os.path.join(chap_414_dir, f)) for f in sorted(os.listdir(chap_414_dir)) if f.endswith('.snbt')}
    chaps_404 = {f[:-5]: parse_snbt_file(os.path.join(chap_404_dir, f)) for f in sorted(os.listdir(chap_404_dir)) if f.endswith('.snbt')}

    q_414 = {}
    for cname, cdata in chaps_414.items():
        for q in cdata.get('quests', []):
            q_414[q['id']] = (cname, q)

    q_404 = {}
    for cname, cdata in chaps_404.items():
        for q in cdata.get('quests', []):
            q_404[q['id']] = (cname, q)

    for qid in sorted(set(q_414.keys()) & set(q_404.keys())):
        c1, q1 = q_414[qid]
        c2, q2 = q_404[qid]
        diffs = []
        if q1.get('title') != q2.get('title'):
            diffs.append(f"title: {q2.get('title')} -> {q1.get('title')}")
        if q1.get('description') != q2.get('description'):
            diffs.append(f"description: {q2.get('description')} -> {q1.get('description')}")
        if str(q1.get('tasks')) != str(q2.get('tasks')):
            diffs.append(f"tasks modified")
        if str(q1.get('rewards')) != str(q2.get('rewards')):
            diffs.append(f"rewards modified")
        if diffs:
            print(f"\nQuest [{c1}] {qid}:")
            for d in diffs:
                print(f"  - {d}")

    # Color code analysis in existing translations
    print("\n=== COLOR CODE USAGE ANALYSIS ===")
    color_codes = set()
    for k, v in p1_en.items():
        matches = re.findall(r'&[0-9a-fk-or]', v)
        color_codes.update(matches)
    print("Color codes found in 4.1.4 EN:", sorted(color_codes))

    ru_codes = set()
    for k, v in p1_ru.items():
        matches = re.findall(r'&[0-9a-fk-or]|§[0-9a-fk-or]', v)
        ru_codes.update(matches)
    print("Color codes found in 4.1.4 RU:", sorted(ru_codes))

if __name__ == '__main__':
    analyze_all()
