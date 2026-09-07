import os
import sys
import zipfile
import io
import json
import hashlib

def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

scriptora_zip = r'tasks/translate_to_zip/Scriptora_Society.Sunlit.Valley.4.0.4 (1).zip'
game_root = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley'
workspace_root = r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода'

print("=== 1. AUDITING SCRIPTORA ZIP ===")
scriptora_files = {} # rel_path -> {size, hash, is_dir}
scriptora_inner_rp = {} # rel_path -> {size, hash}

with zipfile.ZipFile(scriptora_zip, 'r') as z:
    for info in z.infolist():
        if info.is_dir():
            continue
        fname = info.filename
        # Normalize mojibake in filename if any
        if 'resourcepacks/' in fname and fname != 'resourcepacks/':
            # This is the inner resourcepack
            rp_data = z.read(fname)
            with zipfile.ZipFile(io.BytesIO(rp_data), 'r') as rp_z:
                for rp_info in rp_z.infolist():
                    if not rp_info.is_dir():
                        scriptora_inner_rp[rp_info.filename] = {
                            'size': rp_info.file_size,
                            'hash': sha256_bytes(rp_z.read(rp_info.filename))
                        }
            normalized_name = 'resourcepacks/Русификатор.zip'
            scriptora_files[normalized_name] = {
                'size': info.file_size,
                'hash': sha256_bytes(rp_data),
                'orig_name': fname
            }
        else:
            data = z.read(fname)
            scriptora_files[fname] = {
                'size': info.file_size,
                'hash': sha256_bytes(data),
                'orig_name': fname
            }

print(f"Scriptora ZIP contains {len(scriptora_files)} files (including the inner resourcepack).")
print(f"Scriptora inner resourcepack contains {len(scriptora_inner_rp)} files.")

print("\n=== 2. AUDITING GAME DIRECTORY ===")
game_files = {} # rel_path -> {size, hash}
game_inner_rp = {} # rel_path -> {size, hash}

# Check KubeJS Assets
kubejs_assets_dir = os.path.join(game_root, 'kubejs', 'assets')
if os.path.exists(kubejs_assets_dir):
    for root, dirs, files in os.walk(kubejs_assets_dir):
        for f in files:
            full_p = os.path.join(root, f)
            rel_p = os.path.relpath(full_p, game_root).replace('\\', '/')
            game_files[rel_p] = {
                'size': os.path.getsize(full_p),
                'hash': sha256_file(full_p)
            }

# Check Patchouli Books
patchouli_dir = os.path.join(game_root, 'patchouli_books')
if os.path.exists(patchouli_dir):
    for root, dirs, files in os.walk(patchouli_dir):
        for f in files:
            full_p = os.path.join(root, f)
            rel_p = os.path.relpath(full_p, game_root).replace('\\', '/')
            # Only track ru_ru or categories/entries relevant to translation
            if 'ru_ru' in rel_p or rel_p.endswith('book.json'):
                game_files[rel_p] = {
                    'size': os.path.getsize(full_p),
                    'hash': sha256_file(full_p)
                }

# Check Resourcepacks
rp_dir = os.path.join(game_root, 'resourcepacks')
if os.path.exists(rp_dir):
    for f in os.listdir(rp_dir):
        full_p = os.path.join(rp_dir, f)
        if os.path.isfile(full_p) and f.endswith('.zip'):
            try:
                with zipfile.ZipFile(full_p, 'r') as rp_z:
                    is_rus = any('ru_ru' in name for name in rp_z.namelist())
                    if is_rus:
                        norm_name = 'resourcepacks/Русификатор.zip'
                        game_files[norm_name] = {
                            'size': os.path.getsize(full_p),
                            'hash': sha256_file(full_p),
                            'actual_name': f
                        }
                        for rp_info in rp_z.infolist():
                            if not rp_info.is_dir():
                                game_inner_rp[rp_info.filename] = {
                                    'size': rp_info.file_size,
                                    'hash': sha256_bytes(rp_z.read(rp_info.filename))
                                }
            except Exception as e:
                pass

print(f"Game translation-relevant files: {len(game_files)}")
print(f"Game inner resourcepack files: {len(game_inner_rp)}")

# Let's also check KubeJS scripts in game
game_kubejs_scripts = {}
for subdir in ['client_scripts', 'server_scripts']:
    sdir = os.path.join(game_root, 'kubejs', subdir)
    if os.path.exists(sdir):
        for root, dirs, files in os.walk(sdir):
            for f in files:
                full_p = os.path.join(root, f)
                rel_p = os.path.relpath(full_p, game_root).replace('\\', '/')
                game_kubejs_scripts[rel_p] = {
                    'size': os.path.getsize(full_p),
                    'hash': sha256_file(full_p)
                }

print(f"Game KubeJS scripts total: {len(game_kubejs_scripts)}")

# Check workspace scripts vs game scripts
ws_scripts_dir = os.path.join(workspace_root, 'kubejs_scripts')
ws_scripts = {}
if os.path.exists(ws_scripts_dir):
    for root, dirs, files in os.walk(ws_scripts_dir):
        for f in files:
            full_p = os.path.join(root, f)
            rel_p = os.path.relpath(full_p, ws_scripts_dir).replace('\\', '/')
            ws_scripts[rel_p] = {
                'size': os.path.getsize(full_p),
                'hash': sha256_file(full_p)
            }
print(f"Workspace custom scripts in kubejs_scripts/: {len(ws_scripts)}")
for s in ws_scripts:
    print(f"  custom script: {s}")

