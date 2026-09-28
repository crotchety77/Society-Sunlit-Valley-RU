import os, zipfile

game_dir = r'G:\curseforge\minecraft\Instances\Society Sunlit Valley'
matches = []

target_str = 'Макиавеллиев'
target_utf8 = target_str.encode('utf-8')

for root, dirs, files in os.walk(game_dir):
    for f in files:
        p = os.path.join(root, f)
        # check plain files
        try:
            with open(p, 'rb') as fp:
                data = fp.read()
                if target_utf8 in data:
                    matches.append((p, 'direct file'))
        except Exception:
            pass
        # check zip/jar files
        if f.endswith('.zip') or f.endswith('.jar'):
            try:
                with zipfile.ZipFile(p, 'r') as z:
                    for zn in z.namelist():
                        zdata = z.read(zn)
                        if target_utf8 in zdata:
                            matches.append((f'{p} -> {zn}', 'inside archive'))
            except Exception:
                pass

print(f'Total matches for "{target_str}": {len(matches)}')
for m, t in matches:
    print(f'[{t}] {m}')
