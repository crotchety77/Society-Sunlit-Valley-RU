import os
import sys
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

GAME_DIR = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\config\ftbquests\quests\chapters'

snbt_files = [f for f in os.listdir(GAME_DIR) if f.endswith('.snbt')]

ru_only_qids = [
    '1BAF470C2BE0A492', '362B0DE04E15818D', '3C02C152B8677DF1', '3C54AC272D438F76',
    '477FFAD808985736', '539C1B8E3358BBE1', '5B7E846EEFCA5603', '62D0735680A06D71',
    '6BCAB845986C9D3A', '0A455A4E0D7D074E', '118A9A2B8922DA00', '145DAA4D0C7740A3',
    '49EB48B999881A3', '7FEA26673F89CE0', 'B3AAC4CEC0098A3', 'F643DD3F3B61A7D',
    '41C453E806763C4F', '18490F31FFAB134E'
]

for fname in snbt_files:
    fpath = os.path.join(GAME_DIR, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for qid in ru_only_qids:
        # Search for qid in content
        if qid.lower() in content.lower():
            # Find surrounding snippet
            idx = content.lower().find(qid.lower())
            start = max(0, idx - 100)
            end = min(len(content), idx + 400)
            print(f"=== Found {qid} in {fname} ===")
            print(content[start:end])
            print("-" * 50)
