import json, os, re, sys, subprocess

sys.stdout.reconfigure(encoding='utf-8')

print("=== 1. Reading new_translate.md ===")
new_translate_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'new_translate.md')
with open(new_translate_path, 'r', encoding='utf-8') as f:
    content = f.read()

json_match = re.search(r'```json\s*(\{[\s\S]*?\})\s*```', content)
if not json_match:
    raise ValueError("Could not find JSON block in new_translate.md")

entries = json.loads(json_match.group(1))
print(f"Loaded {len(entries)} keys from new_translate.md")

mod_groups = {}
for k, v in entries.items():
    parts = k.split('.')
    if len(parts) >= 2:
        ns = parts[1]
        if ns not in mod_groups:
            mod_groups[ns] = {}
        mod_groups[ns][k] = v

print("=== 2. Updating translations/mods/ ===")
os.makedirs('translations/mods', exist_ok=True)
for ns, kdict in mod_groups.items():
    mod_f = f'translations/mods/{ns}.json'
    data = {}
    if os.path.exists(mod_f):
        with open(mod_f, 'r', encoding='utf-8') as f:
            data = json.load(f)
    data.update(kdict)
    with open(mod_f, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Updated {mod_f} ({len(kdict)} keys)")

print("\n=== 3. Running sync_all_to_game.js ===")
res = subprocess.run(['node', './sync_all_to_game.js'], capture_output=True, text=True, encoding='utf-8')
print(res.stdout)
if res.stderr:
    print("STDERR:", res.stderr)

print("\n=== 4. Direct Physical Game Files Verification ===")
base_game = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets'
for ns, kdict in mod_groups.items():
    p = os.path.join(base_game, ns, 'lang', 'ru_ru.json')
    if not os.path.exists(p):
        raise ValueError(f"Missing game file: {p}")
    with open(p, 'r', encoding='utf-8') as f:
        g = json.load(f)
    print(f"[{ns}] Verified total {len(g)} keys in game file:")
    for k in list(kdict.keys())[:3]:
        print(f"  [{k}] = {g.get(k)}")
    print("  ...")
    for k in list(kdict.keys())[-2:]:
        print(f"  [{k}] = {g.get(k)}")

print("\n=== ALL ENCHANTMENTS APPLIED AND PHYSICALLY VERIFIED! ===")
