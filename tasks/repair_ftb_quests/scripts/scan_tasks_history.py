import os
import sys
import json
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

print("=== Scanning tasks/ for quest translation work ===")
for root, dirs, files in os.walk(os.path.join(REPO_ROOT, 'tasks')):
    for f in files:
        if f.endswith(('.md', '.json', '.py', '.txt')) and not f.endswith('TASK.md'):
            fp = os.path.join(root, f)
            with open(fp, 'r', encoding='utf-8', errors='ignore') as fh:
                txt = fh.read()
                if 'pagebreak' in txt or 'ftbquests' in txt or 'бабочк' in txt or 'пруд' in txt:
                    # Look for quest references
                    qids = set(re.findall(r'[0-9A-Fa-f]{16}', txt))
                    if qids or 'pagebreak' in txt:
                        rel = os.path.relpath(fp, REPO_ROOT)
                        print(f"\nFile: {rel}")
                        if 'pagebreak' in txt:
                            print("  -> Contains {@pagebreak}!")
                        if qids:
                            print(f"  -> Quest IDs found: {list(qids)[:5]}")
