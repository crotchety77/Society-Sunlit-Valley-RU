import os
import sys
import zipfile
import io
import json
import hashlib

sys.stdout.reconfigure(encoding='utf-8')

scriptora_zip = r'tasks/translate_to_zip/Scriptora_Society.Sunlit.Valley.4.0.4 (1).zip'
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

# 1. Read Scriptora ZIP
zip_entries = {}
scriptora_rp_entries = {}

with zipfile.ZipFile(scriptora_zip, 'r') as z:
    for info in z.infolist():
        if info.is_dir():
            continue
        fname = info.filename
        raw_bytes = z.read(fname)
        h = sha256_bytes(raw_bytes)
        
        # Check if inner resourcepack
        if 'resourcepacks/' in fname and fname.endswith('.zip'):
            norm_name = 'resourcepacks/Русификатор.zip'
            zip_entries[norm_name] = {'size': info.file_size, 'hash': h, 'orig': fname, 'bytes': raw_bytes}
            with zipfile.ZipFile(io.BytesIO(raw_bytes), 'r') as rp_z:
                for rp_info in rp_z.infolist():
                    if not rp_info.is_dir():
                        rp_bytes = rp_z.read(rp_info.filename)
                        scriptora_rp_entries[rp_info.filename] = {
                            'size': rp_info.file_size,
                            'hash': sha256_bytes(rp_bytes),
                            'bytes': rp_bytes
                        }
        else:
            zip_entries[fname] = {'size': info.file_size, 'hash': h, 'orig': fname, 'bytes': raw_bytes}

print(f"Scriptora ZIP root entries: {len(zip_entries)}")
print(f"Scriptora ZIP inner resourcepack entries: {len(scriptora_rp_entries)}")

# 2. Inspect Game Files
# Categories to inspect:
# - kubejs/assets
# - patchouli_books
# - resourcepacks/Русификатор.zip
# - kubejs/client_scripts
# - kubejs/server_scripts

game_kubejs_assets = {}
game_patchouli = {}
game_rp_entries = {}
game_rp_zip_info = None

# kubejs/assets
k_assets_dir = os.path.join(game_root, 'kubejs', 'assets')
for root, dirs, files in os.walk(k_assets_dir):
    for f in files:
        full_p = os.path.join(root, f)
        rel_p = os.path.relpath(full_p, game_root).replace('\\', '/')
        h = sha256_file(full_p)
        with open(full_p, 'rb') as fh:
            data = fh.read()
        game_kubejs_assets[rel_p] = {'size': os.path.getsize(full_p), 'hash': h, 'bytes': data}

# patchouli_books
p_dir = os.path.join(game_root, 'patchouli_books')
for root, dirs, files in os.walk(p_dir):
    for f in files:
        full_p = os.path.join(root, f)
        rel_p = os.path.relpath(full_p, game_root).replace('\\', '/')
        if 'ru_ru' in rel_p or rel_p.endswith('book.json'):
            h = sha256_file(full_p)
            with open(full_p, 'rb') as fh:
                data = fh.read()
            game_patchouli[rel_p] = {'size': os.path.getsize(full_p), 'hash': h, 'bytes': data}

# resourcepacks/Русификатор.zip
rp_dir = os.path.join(game_root, 'resourcepacks')
for f in os.listdir(rp_dir):
    full_p = os.path.join(rp_dir, f)
    if os.path.isfile(full_p) and f.endswith('.zip'):
        try:
            with zipfile.ZipFile(full_p, 'r') as z:
                if any('ru_ru' in name for name in z.namelist()):
                    h = sha256_file(full_p)
                    with open(full_p, 'rb') as fh:
                        data = fh.read()
                    game_rp_zip_info = {'name': f, 'size': len(data), 'hash': h, 'bytes': data}
                    for info in z.infolist():
                        if not info.is_dir():
                            b = z.read(info.filename)
                            game_rp_entries[info.filename] = {
                                'size': info.file_size,
                                'hash': sha256_bytes(b),
                                'bytes': b
                            }
        except Exception:
            pass

print(f"\nGame kubejs/assets files: {len(game_kubejs_assets)}")
print(f"Game patchouli ru_ru files: {len(game_patchouli)}")
print(f"Game inner resourcepack files: {len(game_rp_entries)}")

# 3. Compare kubejs/assets
print("\n--- kubejs/assets comparison ---")
for p, ginfo in sorted(game_kubejs_assets.items()):
    in_zip = p in zip_entries
    if in_zip:
        zinfo = zip_entries[p]
        same = (zinfo['hash'] == ginfo['hash'])
        status = "SAME" if same else "MODIFIED"
        print(f"[{status}] {p} (game: {ginfo['size']}b, zip: {zinfo['size']}b)")
    else:
        print(f"[NEW/ADDED] {p} ({ginfo['size']}b)")

for p in sorted(zip_entries.keys()):
    if p.startswith('kubejs/assets/') and p not in game_kubejs_assets:
        print(f"[REMOVED/IN_ZIP_ONLY] {p}")

# 4. Compare patchouli_books
print("\n--- patchouli_books comparison ---")
pb_same = 0
pb_modified = 0
pb_new = 0
pb_in_zip_only = 0

for p, ginfo in sorted(game_patchouli.items()):
    if p in zip_entries:
        if zip_entries[p]['hash'] == ginfo['hash']:
            pb_same += 1
        else:
            pb_modified += 1
            print(f"[PB MODIFIED] {p}")
    else:
        pb_new += 1
        print(f"[PB NEW] {p}")

for p in sorted(zip_entries.keys()):
    if p.startswith('patchouli_books/') and p not in game_patchouli:
        pb_in_zip_only += 1
        print(f"[PB IN_ZIP_ONLY] {p}")

print(f"Patchouli Summary: same={pb_same}, modified={pb_modified}, new={pb_new}, zip_only={pb_in_zip_only}")

# 5. Compare inner resourcepack
print("\n--- inner resourcepack comparison ---")
rp_same = 0
rp_modified = 0
rp_new = 0
rp_zip_only = 0

for p, ginfo in sorted(game_rp_entries.items()):
    if p in scriptora_rp_entries:
        if scriptora_rp_entries[p]['hash'] == ginfo['hash']:
            rp_same += 1
        else:
            rp_modified += 1
            print(f"[RP MODIFIED] {p}")
    else:
        rp_new += 1
        print(f"[RP NEW] {p}")

for p in sorted(scriptora_rp_entries.keys()):
    if p not in game_rp_entries:
        rp_zip_only += 1
        print(f"[RP ZIP_ONLY] {p}")

print(f"Resourcepack Summary: same={rp_same}, modified={rp_modified}, new={rp_new}, zip_only={rp_zip_only}")
