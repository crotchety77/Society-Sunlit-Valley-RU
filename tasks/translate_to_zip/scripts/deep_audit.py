import os
import sys
import zipfile
import io
import json
import hashlib

sys.stdout.reconfigure(encoding='utf-8')

scriptora_zip_path = r'tasks/translate_to_zip/Scriptora_Society.Sunlit.Valley.4.0.4 (1).zip'
game_root = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley'
ws_root = r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода'

def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

print("="*60)
print("DEEP AUDIT: SCRIPTORA ZIP vs ACTIVE GAME TRANSLATION")
print("="*60)

# Load Scriptora ZIP
zip_files = {} # clean_rel_path -> {bytes, hash, size, orig_path}
with zipfile.ZipFile(scriptora_zip_path, 'r') as z:
    for info in z.infolist():
        if info.is_dir():
            continue
        orig = info.filename
        raw = z.read(orig)
        # Normalize resourcepacks path
        if 'resourcepacks/' in orig:
            clean = 'resourcepacks/Перевод модов.zip'
        else:
            clean = orig
        zip_files[clean] = {
            'bytes': raw,
            'hash': sha256_bytes(raw),
            'size': info.file_size,
            'orig_path': orig
        }

print(f"Total files in Scriptora ZIP: {len(zip_files)}")

# 1. KUBEJS ASSETS
print("\n--- 1. KUBEJS ASSETS ---")
game_kubejs_assets = {}
k_assets_dir = os.path.join(game_root, 'kubejs', 'assets')
for root, dirs, files in os.walk(k_assets_dir):
    for f in files:
        full_p = os.path.join(root, f)
        rel_p = os.path.relpath(full_p, game_root).replace('\\', '/')
        with open(full_p, 'rb') as fh:
            data = fh.read()
        game_kubejs_assets[rel_p] = {
            'bytes': data,
            'size': len(data),
            'hash': sha256_bytes(data),
            'full_path': full_p
        }

print(f"Total files in Game kubejs/assets: {len(game_kubejs_assets)}")

# Classify kubejs/assets
kubejs_assets_report = []
for p, ginfo in sorted(game_kubejs_assets.items()):
    in_zip = p in zip_files
    if in_zip:
        zinfo = zip_files[p]
        if zinfo['hash'] == ginfo['hash']:
            status = 'UNCHANGED'
        else:
            status = 'MODIFIED'
    else:
        status = 'NEW_ADDED'
    
    # Check if JSON
    key_count_game = None
    key_count_zip = None
    if p.endswith('.json'):
        try:
            g_json = json.loads(ginfo['bytes'].decode('utf-8'))
            key_count_game = len(g_json)
        except Exception:
            pass
        if in_zip:
            try:
                z_json = json.loads(zip_files[p]['bytes'].decode('utf-8'))
                key_count_zip = len(z_json)
            except Exception:
                pass

    kubejs_assets_report.append({
        'path': p,
        'status': status,
        'in_zip': in_zip,
        'in_game': True,
        'game_size': ginfo['size'],
        'zip_size': zip_files[p]['size'] if in_zip else None,
        'keys_game': key_count_game,
        'keys_zip': key_count_zip
    })

for item in kubejs_assets_report:
    status_tag = f"[{item['status']}]"
    keys_info = f"(keys: game={item['keys_game']}, zip={item['keys_zip']})" if item['keys_game'] is not None else ""
    print(f"  {status_tag:<12} {item['path']} {keys_info}")

# 2. PATCHOULI BOOKS
print("\n--- 2. PATCHOULI BOOKS ---")
game_patchouli = {}
p_dir = os.path.join(game_root, 'patchouli_books')
for root, dirs, files in os.walk(p_dir):
    for f in files:
        full_p = os.path.join(root, f)
        rel_p = os.path.relpath(full_p, game_root).replace('\\', '/')
        with open(full_p, 'rb') as fh:
            data = fh.read()
        game_patchouli[rel_p] = {
            'bytes': data,
            'size': len(data),
            'hash': sha256_bytes(data),
            'full_path': full_p
        }

print(f"Total files in Game patchouli_books: {len(game_patchouli)}")
# Filter for translation relevance
pb_report = []
for p, ginfo in sorted(game_patchouli.items()):
    if 'ru_ru' in p or p.endswith('book.json'):
        in_zip = p in zip_files
        if in_zip:
            status = 'UNCHANGED' if zip_files[p]['hash'] == ginfo['hash'] else 'MODIFIED'
        else:
            status = 'NEW_ADDED'
        pb_report.append({
            'path': p,
            'status': status,
            'in_zip': in_zip,
            'in_game': True,
            'game_size': ginfo['size'],
            'zip_size': zip_files[p]['size'] if in_zip else None
        })

print(f"Active Russian Patchouli files in Game: {len(pb_report)}")
for item in pb_report[:10]:
    print(f"  [{item['status']:<10}] {item['path']}")
if len(pb_report) > 10:
    print(f"  ... and {len(pb_report) - 10} more fish_finder files")

# Check zip-only patchouli files (e.g. almanac/ru_ru)
pb_zip_only = [p for p in zip_files if p.startswith('patchouli_books/') and p not in game_patchouli]
print(f"Patchouli files present ONLY in Scriptora zip (almanac): {len(pb_zip_only)}")

# 3. RESOURCEPACKS
print("\n--- 3. RESOURCEPACKS ---")
rp_game_path = os.path.join(game_root, 'resourcepacks', 'Перевод модов.zip')
if os.path.exists(rp_game_path):
    rp_game_size = os.path.getsize(rp_game_path)
    rp_game_hash = sha256_file(rp_game_path)
    z_rp_info = zip_files.get('resourcepacks/Перевод модов.zip')
    same_rp = (z_rp_info['hash'] == rp_game_hash) if z_rp_info else False
    print(f"  resourcepacks/Перевод модов.zip: game size={rp_game_size}b, zip size={z_rp_info['size'] if z_rp_info else 'N/A'}b, hash match={same_rp}")

# 4. KUBEJS SCRIPTS (CUSTOM TRANSLATION SCRIPTS)
print("\n--- 4. KUBEJS SCRIPTS (CUSTOM UI & TOOLTIPS) ---")
custom_scripts = [
    'kubejs/client_scripts/tooltips/bountifulTooltips.js',
    'kubejs/client_scripts/tooltips/buildinggadgets2Tooltips.js',
    'kubejs/client_scripts/tooltips/createCentralKitchenTooltips.js',
    'kubejs/client_scripts/etceteraJei.js',
    'kubejs/client_scripts/tooltips/etceteraTooltips.js',
    'kubejs/client_scripts/tooltips/invitationTooltips.js',
    'kubejs/client_scripts/tooltips/longwingsTooltips.js',
    'kubejs/client_scripts/tooltips/tanukiDecorTooltips.js',
    'kubejs/client_scripts/universalGiftsJei.js',
    'kubejs/client_scripts/tooltips/unusualFishTooltips.js',
    'kubejs/server_scripts/entities/slimeTicket.js',
    'kubejs/server_scripts/entities/slimeInspectorEnhanced.js',
    'kubejs/server_scripts/globalServer.js',
    'kubejs/server_scripts/handleDebt.js',
    'kubejs/server_scripts/translateInspector.js'
]

for s in custom_scripts:
    full_p = os.path.join(game_root, s.replace('/', os.sep))
    in_game = os.path.exists(full_p)
    in_zip = s in zip_files
    print(f"  Script: {s:<60} in_game={in_game}, in_zip={in_zip}")

