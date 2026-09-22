import zipfile, subprocess, os, tempfile

mods_path = r'G:\curseforge\minecraft\Instances\Society Sunlit Valley\mods'
jar_file = None
for f in os.listdir(mods_path):
    if 'splendid_slimes' in f.lower():
        jar_file = os.path.join(mods_path, f)
        break

temp_dir = tempfile.mkdtemp()
with zipfile.ZipFile(jar_file, 'r') as z:
    for name in z.namelist():
        if name.endswith('.class'):
            z.extract(name, temp_dir)

traits = ['dominant', 'inverse', 'moody', 'defiant', 'picky', 'feral', 'flaming', 'explosive', 'spiky', 'putrid', 'nuclear', 'largoless', 'weeping', 'foodporting', 'floating', 'handy', 'aquatic', 'friendly']

trait_findings = {t: [] for t in traits}

for root, dirs, files in os.walk(temp_dir):
    for f in files:
        if f.endswith('.class'):
            p = os.path.join(root, f)
            res = subprocess.run(['javap', '-p', '-c', '-constants', p], capture_output=True, text=True)
            out = res.stdout
            for t in traits:
                if f'"{t}"' in out:
                    # Find method where it occurs
                    lines = out.split('\n')
                    current_m = ""
                    for idx, line in enumerate(lines):
                        if ('public ' in line or 'private ' in line or 'protected ' in line) and '(' in line:
                            current_m = line.strip()
                        if f'"{t}"' in line:
                            context = '\n'.join(lines[max(0, idx-4):min(len(lines), idx+12)])
                            trait_findings[t].append((f, current_m, context))

for t, hits in trait_findings.items():
    print(f"\n==================== TRAIT: {t.upper()} (Hits: {len(hits)}) ====================")
    for cls_name, method, ctx in hits:
        print(f"Class: {cls_name} | Method: {method}")
        print(ctx)
        print("-" * 40)
