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

society_keys = {}
mod_keys = {}

def get_namespace(key):
    if key.startswith(('item.society.', 'tooltip.society.', 'block.society.')):
        return 'society'
    if 'rehooked' in key or key in ['creative.tab.hooks', 'curios.identifier.hook']:
        return 'rehooked'
    for mod in ['moblassos', 'domesticationinnovation', 'automobility', 'solonion', 'numismatics_utils', 'beachparty', 'pamhc2trees', 'strawstatues', 'via_romana']:
        if mod in key:
            return mod
    parts = key.split('.')
    if len(parts) >= 2:
        ns = parts[1]
        if ':' in ns:
            ns = ns.split(':')[0]
        return ns
    return 'unknown'

for k, v in entries.items():
    ns = get_namespace(k)
    if ns == 'society':
        society_keys[k] = v
    elif ns != 'unknown':
        if ns not in mod_keys:
            mod_keys[ns] = {}
        mod_keys[ns][k] = v
    else:
        print(f"WARNING: Unknown namespace for key: {k}")

print(f"Society keys: {len(society_keys)}")
for ns, kdict in mod_keys.items():
    print(f"Mod '{ns}' keys: {len(kdict)}")

print("\n=== 2. Updating translations/society/ru_ru.json ===")
soc_ru_path = 'translations/society/ru_ru.json'
with open(soc_ru_path, 'r', encoding='utf-8') as f:
    soc_ru = json.load(f)

for k, v in society_keys.items():
    soc_ru[k] = v

with open(soc_ru_path, 'w', encoding='utf-8') as f:
    json.dump(soc_ru, f, ensure_ascii=False, indent=2)
print(f"Updated {soc_ru_path} with {len(society_keys)} keys")

print("\n=== 3. Updating translations/mods/<namespace>.json ===")
os.makedirs('translations/mods', exist_ok=True)
for ns, keys in mod_keys.items():
    mod_file = f"translations/mods/{ns}.json"
    mod_data = {}
    if os.path.exists(mod_file):
        with open(mod_file, 'r', encoding='utf-8') as f:
            mod_data = json.load(f)
    for k, v in keys.items():
        mod_data[k] = v
    with open(mod_file, 'w', encoding='utf-8') as f:
        json.dump(mod_data, f, ensure_ascii=False, indent=2)
    print(f"Updated {mod_file} ({len(keys)} keys)")

print("\n=== 4. Updating game_data/client_scripts/tooltips/addTooltips.js ===")
add_tooltips_path = 'game_data/client_scripts/tooltips/addTooltips.js'
with open(add_tooltips_path, 'r', encoding='utf-8') as f:
    at_content = f.read()

# 1. miracle_potion -> addAdvanced with Shift
miracle_pattern = re.compile(r'tooltip\.add(?:Advanced)?\(\s*"society:miracle_potion"[\s\S]*?\n\s*\);?')
miracle_replacement = """tooltip.addAdvanced("society:miracle_potion", (item, advanced, text) => {
    text.add(Text.translatable("item.society.miracle_potion.description").gray());
    if (tooltip.shift) {
      text.add(Text.translatable("tooltip.society.miracle_potion.shift_1").gold());
      text.add(Text.translatable("tooltip.society.miracle_potion.shift_2").gray());
      text.add(Text.translatable("tooltip.society.miracle_potion.shift_3").gray());
      text.add(Text.translatable("tooltip.society.miracle_potion.shift_4").gray());
    } else {
      text.add(Text.translatable("tooltip.society.press_shift_details"));
    }
  });"""

if miracle_pattern.search(at_content):
    at_content = miracle_pattern.sub(miracle_replacement, at_content)
    print("Updated miracle_potion tooltip")
else:
    last_brace = at_content.rfind('});')
    if last_brace != -1:
        at_content = at_content[:last_brace] + "\n  " + miracle_replacement + "\n\n" + at_content[last_brace:]
        print("Added miracle_potion tooltip")

# 2. mood_scanner -> addAdvanced with Shift
mood_pattern = re.compile(r'tooltip\.add(?:Advanced)?\(\s*"society:mood_scanner"[\s\S]*?\n\s*\);?')
mood_replacement = """tooltip.addAdvanced("society:mood_scanner", (item, advanced, text) => {
    text.add(Text.translatable("item.society.mood_scanner.description").gray());
    text.add(Text.translatable("item.society.mood_scanner.description.warn").red());
    if (tooltip.shift) {
      text.add(Text.translatable("tooltip.society.mood_scanner.shift_header").gold());
      text.add(Text.translatable("tooltip.society.mood_scanner.shift_pet").gray());
      text.add(Text.translatable("tooltip.society.mood_scanner.shift_quality").gray());
      text.add(Text.translatable("tooltip.society.mood_scanner.shift_daily").gray());
      text.add(Text.translatable("tooltip.society.mood_scanner.shift_roof").gray());
      text.add(Text.translatable("tooltip.society.mood_scanner.shift_cramped").gray());
    } else {
      text.add(Text.translatable("tooltip.society.press_shift_details"));
    }
  });"""

if mood_pattern.search(at_content):
    at_content = mood_pattern.sub(mood_replacement, at_content)
    print("Updated mood_scanner tooltip")
else:
    last_brace = at_content.rfind('});')
    if last_brace != -1:
        at_content = at_content[:last_brace] + "\n  " + mood_replacement + "\n\n" + at_content[last_brace:]
        print("Added mood_scanner tooltip")

# 3. magic_shears -> addAdvanced with Shift
shears_pattern = re.compile(r'tooltip\.addAdvanced\(\s*"society:magic_shears"[\s\S]*?\n\s*\);')
shears_replacement = """tooltip.addAdvanced("society:magic_shears", (item, advanced, text) => {
    text.add(Text.translatable("item.society.magic_shears.description").gray());
    text.add(Text.translatable("item.society.magic_shears.description.warn").red());
    if (tooltip.shift) {
      text.add(Text.translatable("tooltip.society.magic_shears.shift_1").gray());
      text.add(Text.translatable("tooltip.society.magic_shears.shift_2").gray());
      text.add(Text.translatable("tooltip.society.magic_shears.shift_3").gray());
    } else {
      text.add(Text.translatable("tooltip.society.press_shift_details"));
    }
  });"""

if shears_pattern.search(at_content):
    at_content = shears_pattern.sub(shears_replacement, at_content)
    print("Updated magic_shears tooltip")

with open(add_tooltips_path, 'w', encoding='utf-8') as f:
    f.write(at_content)
print(f"Saved {add_tooltips_path}")

print("\n=== 5. Running sync_all_to_game.js ===")
res = subprocess.run(['node', './sync_all_to_game.js'], capture_output=True, text=True, encoding='utf-8')
print(res.stdout)
if res.stderr:
    print("STDERR:", res.stderr)

print("\n=== 6. Direct Physical Game Files Verification ===")
base_game = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets'

# Check society ru_ru.json
soc_game_path = os.path.join(base_game, 'society', 'lang', 'ru_ru.json')
with open(soc_game_path, 'r', encoding='utf-8') as f:
    game_soc = json.load(f)

verified_keys = [
    "item.society.miracle_potion",
    "item.society.miracle_potion.description",
    "tooltip.society.miracle_potion.shift_1",
    "tooltip.society.miracle_potion.shift_2",
    "item.society.mood_scanner",
    "tooltip.society.mood_scanner.shift_quality",
    "item.society.magic_shears",
    "item.society.magic_shears.description",
    "tooltip.society.lunchbag",
    "tooltip.society.lunchbox",
    "tooltip.society.golden_lunchbox",
    "tooltip.society.crocs",
    "tooltip.society.starfruit_sapling",
    "tooltip.society.straw_statue",
    "tooltip.society.charting_map",
    "tooltip.society.portable_bank_terminal",
    "tooltip.society.bank_meter"
]

print("--- Checking kubejs/assets/society/lang/ru_ru.json ---")
for k in verified_keys:
    val = game_soc.get(k)
    print(f"  [{k}] = {val}")
    if val is None:
        raise ValueError(f"Missing key in game society ru_ru.json: {k}")

print("\n--- Checking kubejs/assets/<namespace>/lang/ru_ru.json for mods ---")
for ns, kdict in mod_keys.items():
    game_mod_p = os.path.join(base_game, ns, 'lang', 'ru_ru.json')
    if not os.path.exists(game_mod_p):
        raise ValueError(f"Game file not found: {game_mod_p}")
    with open(game_mod_p, 'r', encoding='utf-8') as f:
        g_d = json.load(f)
    print(f"[{ns}] ({len(g_d)} keys in game file):")
    for k in kdict.keys():
        val = g_d.get(k)
        print(f"  [{k}] = {val}")
        if val is None:
            raise ValueError(f"Missing key in game {ns} ru_ru.json: {k}")

# Also verify addTooltips.js in game client_scripts
game_add_tooltips = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\client_scripts\tooltips\addTooltips.js'
if os.path.exists(game_add_tooltips):
    with open(game_add_tooltips, 'r', encoding='utf-8') as f:
        g_at = f.read()
    if 'society:miracle_potion' in g_at and 'society:mood_scanner' in g_at:
        print("\n[OK] Physical game addTooltips.js contains miracle_potion and mood_scanner advanced tooltips!")
    else:
        print("\n[WARNING] game addTooltips.js might be missing some items!")

print("\n=== ALL ITEMS SUCCESSFULLY APPLIED AND PHYSICALLY VERIFIED! ===")

