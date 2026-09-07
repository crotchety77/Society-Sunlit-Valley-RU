import os
import sys
import shutil
import zipfile
import json
import hashlib

sys.stdout.reconfigure(encoding='utf-8')

game_root = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley'
scriptora_zip_path = r'tasks/translate_to_zip/Scriptora_Society.Sunlit.Valley.4.0.4 (1).zip'
task_dir = r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\tasks\translate_to_zip'
dist_dir = os.path.join(task_dir, 'dist', 'Русификатор')
dist_zip = os.path.join(task_dir, 'dist', 'Русификатор.zip')

def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

# Clean dist directory
if os.path.exists(dist_dir):
    shutil.rmtree(dist_dir)
os.makedirs(dist_dir, exist_ok=True)

# 1. Read Scriptora ZIP
zip_files = {} # clean_rel -> {hash, size, orig}
with zipfile.ZipFile(scriptora_zip_path, 'r') as z:
    for info in z.infolist():
        if info.is_dir():
            continue
        orig = info.filename
        raw = z.read(orig)
        if 'resourcepacks/' in orig and orig.endswith('.zip'):
            clean = 'resourcepacks/Перевод модов.zip'
        else:
            clean = orig
        zip_files[clean] = {
            'hash': sha256_bytes(raw),
            'size': info.file_size,
            'orig': orig
        }

print(f"Loaded {len(zip_files)} files from Scriptora ZIP.")

# List of files to copy from game into dist
# A. kubejs/assets/ (ru_ru.json, textures, custom_frames)
files_to_package = []

k_assets = os.path.join(game_root, 'kubejs', 'assets')
for root, dirs, files in os.walk(k_assets):
    for f in files:
        full_p = os.path.join(root, f)
        rel_p = os.path.relpath(full_p, game_root).replace('\\', '/')
        # Include all ru_ru.json
        if f == 'ru_ru.json':
            files_to_package.append(rel_p)
        # Include translated community center textures
        elif 'community_center_' in f and f.endswith('.png'):
            files_to_package.append(rel_p)
        # Include tooltip overhaul frame configs
        elif rel_p == 'kubejs/assets/society/tooltipoverhaul/custom_frames.json':
            files_to_package.append(rel_p)

# B. patchouli_books/ (fish_finder/ru_ru)
p_dir = os.path.join(game_root, 'patchouli_books')
for root, dirs, files in os.walk(p_dir):
    for f in files:
        full_p = os.path.join(root, f)
        rel_p = os.path.relpath(full_p, game_root).replace('\\', '/')
        if 'ru_ru' in rel_p:
            files_to_package.append(rel_p)

# C. resourcepacks/ (Перевод модов.zip)
rp_file = os.path.join(game_root, 'resourcepacks', 'Перевод модов.zip')
if os.path.exists(rp_file):
    files_to_package.append('resourcepacks/Перевод модов.zip')

# D. Custom Client Scripts (Tooltips & JEI)
client_scripts = [
    'kubejs/client_scripts/tooltips/bountifulTooltips.js',
    'kubejs/client_scripts/tooltips/buildinggadgets2Tooltips.js',
    'kubejs/client_scripts/tooltips/createCentralKitchenTooltips.js',
    'kubejs/client_scripts/etceteraJei.js',
    'kubejs/client_scripts/tooltips/etceteraTooltips.js',
    'kubejs/client_scripts/tooltips/invitationTooltips.js',
    'kubejs/client_scripts/tooltips/longwingsTooltips.js',
    'kubejs/client_scripts/tooltips/tanukiDecorTooltips.js',
    'kubejs/client_scripts/universalGiftsJei.js',
    'kubejs/client_scripts/tooltips/unusualFishTooltips.js'
]
for cs in client_scripts:
    if os.path.exists(os.path.join(game_root, cs.replace('/', os.sep))):
        files_to_package.append(cs)

# E. Custom Server Scripts (Mechanics & Hospital/Debt Fixes)
server_scripts = [
    'kubejs/server_scripts/globalServer.js',
    'kubejs/server_scripts/handleDebt.js',
    'kubejs/server_scripts/entities/slimeTicket.js',
    'kubejs/server_scripts/entities/slimeInspectorEnhanced.js'
]
for ss in server_scripts:
    if os.path.exists(os.path.join(game_root, ss.replace('/', os.sep))):
        files_to_package.append(ss)

print(f"Total files selected for package: {len(files_to_package)}")

# Copy files to dist/Русификатор
for rel_p in files_to_package:
    src_full = os.path.join(game_root, rel_p.replace('/', os.sep))
    dest_full = os.path.join(dist_dir, rel_p.replace('/', os.sep))
    os.makedirs(os.path.dirname(dest_full), exist_ok=True)
    shutil.copy2(src_full, dest_full)

# Create ZIP archive
if os.path.exists(dist_zip):
    os.remove(dist_zip)

with zipfile.ZipFile(dist_zip, 'w', zipfile.ZIP_DEFLATED) as z:
    for root, dirs, files in os.walk(dist_dir):
        for f in files:
            full_p = os.path.join(root, f)
            arcname = os.path.relpath(full_p, dist_dir).replace('\\', '/')
            z.write(full_p, arcname)

print(f"Created ZIP distribution: {dist_zip} ({os.path.getsize(dist_zip)} bytes)")

# 2. Detailed Verification and Categorization
unchanged_files = []
modified_files = []
new_files = []
unsafe_or_mixed_files = [
    {
        'path': 'kubejs/server_scripts/translateInspector.js',
        'reason': 'Инструмент разработчика (/trans) для инспекции NBT и ключей предметов. Не требуется обычному игроку, оставлен вне сборки.'
    }
]

manual_check_files = [
    {
        'path': 'patchouli_books/almanac/ru_ru/',
        'count': 201,
        'reason': 'Присутствовал в архиве Scriptora (201 файл альманаха), но в актуальной установленной игре отсутствует (в игре только en_us/fr_fr/ko_kr, а сам альманах генерируется/ссылается иначе). Не включен в пакет по правилу приоритета игры как источника истины.'
    }
]

for rel_p in files_to_package:
    src_full = os.path.join(game_root, rel_p.replace('/', os.sep))
    curr_hash = sha256_file(src_full)
    if rel_p in zip_files:
        if zip_files[rel_p]['hash'] == curr_hash:
            unchanged_files.append(rel_p)
        else:
            modified_files.append(rel_p)
    else:
        new_files.append(rel_p)

# In Scriptora zip but not in current package
removed_or_unused = [p for p in zip_files if p not in files_to_package]

print("\n" + "="*60)
print("AUDIT SUMMARY METRICS:")
print("="*60)
print(f"Количество файлов в исходном архиве: {len(zip_files)}")
print(f"Количество файлов в текущем переводе (в пакете): {len(files_to_package)}")
print(f"Количество новых файлов (добавлены нами): {len(new_files)}")
print(f"Количество изменённых файлов (обновлены нами): {len(modified_files)}")
print(f"Количество неизменных файлов: {len(unchanged_files)}")
print(f"Количество удалённых/неиспользуемых файлов из старого архива: {len(removed_or_unused)}")
print(f"Количество файлов, которые нельзя безопасно распространять (смешанные): {len(unsafe_or_mixed_files)}")
print(f"Количество объектов, требующих ручной проверки: {len(manual_check_files)}")

# Save JSON report
report_data = {
    'metrics': {
        'scriptora_total': len(zip_files),
        'package_total': len(files_to_package),
        'new_files': len(new_files),
        'modified_files': len(modified_files),
        'unchanged_files': len(unchanged_files),
        'removed_or_unused_from_scriptora': len(removed_or_unused),
        'unsafe_mixed_files': len(unsafe_or_mixed_files),
        'manual_check_items': len(manual_check_files)
    },
    'new_files_list': new_files,
    'modified_files_list': modified_files,
    'unchanged_files_list': unchanged_files,
    'removed_or_unused_list': removed_or_unused,
    'unsafe_or_mixed_files': unsafe_or_mixed_files,
    'manual_check_files': manual_check_files
}

with open(os.path.join(task_dir, 'distribution_audit_report.json'), 'w', encoding='utf-8') as fh:
    json.dump(report_data, fh, ensure_ascii=False, indent=2)

print("\nReport saved to tasks/translate_to_zip/distribution_audit_report.json")
