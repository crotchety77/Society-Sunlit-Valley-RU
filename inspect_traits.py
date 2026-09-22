import os, re

with open(r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\SplendidSlime_javap.txt', 'r', encoding='utf-8') as f:
    ss_txt = f.read()

with open(r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\SlimeUtils_javap.txt', 'r', encoding='utf-8') as f:
    su_txt = f.read()

with open(r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\SlimeComfortUtils_javap.txt', 'r', encoding='utf-8') as f:
    sc_txt = f.read()

with open(r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\SlimeBreed_javap.txt', 'r', encoding='utf-8') as f:
    sb_txt = f.read()

# Let's inspect where traits are used in SplendidSlime
print("=== TRAITS USAGES IN SPLENDIDSLIME ===")
lines = ss_txt.split('\n')
current_method = ""
for i, l in enumerate(lines):
    if ('public ' in l or 'private ' in l or 'protected ' in l) and '(' in l:
        current_method = l.strip()
    for tr in ['dominant', 'inverse', 'moody', 'defiant', 'picky', 'feral', 'flaming', 'explosive', 'spiky', 'putrid', 'nuclear', 'largoless', 'weeping', 'foodporting', 'floating', 'handy', 'aquatic', 'friendly']:
        if f'"{tr}"' in l or f'String {tr}' in l:
            print(f"Method: {current_method}")
            print(f"  Line {i}: {l.strip()}")
            # print surrounding lines
            start = max(0, i-5)
            end = min(len(lines), i+15)
            for j in range(start, end):
                print(f"    {lines[j]}")
            print("-" * 50)

print("\n=== SLIME UTILS / BREEDING / FUSION ===")
lines = su_txt.split('\n')
for i, l in enumerate(lines):
    if ('public ' in l or 'private ' in l or 'protected ' in l) and '(' in l:
        current_method = l.strip()
    if 'fuse' in l.lower() or 'largo' in l.lower() or 'diet' in l.lower() or 'trait' in l.lower() or 'breed' in l.lower():
        print(f"Method: {current_method} -> {l.strip()}")

