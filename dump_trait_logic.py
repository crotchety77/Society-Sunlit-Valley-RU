import re

with open(r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\SplendidSlime_javap.txt', 'r', encoding='utf-8') as f:
    ss_txt = f.read()

with open(r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\SlimeUtils_javap.txt', 'r', encoding='utf-8') as f:
    su_txt = f.read()

with open(r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\SlimeComfortUtils_javap.txt', 'r', encoding='utf-8') as f:
    sc_txt = f.read()

def print_method_around(txt, query, before=10, after=40):
    lines = txt.split('\n')
    for i, l in enumerate(lines):
        if query in l:
            start = max(0, i - before)
            end = min(len(lines), i + after)
            print("="*40)
            print(f"QUERY: {query} (Line {i})")
            for j in range(start, end):
                print(f"{j}: {lines[j]}")
            print("="*40)

print("--- 1. DOMINANT (getSlimeFoods) ---")
print_method_around(ss_txt, "dominant", 5, 45)

print("--- 2. INVERSE (m_8119_) ---")
print_method_around(ss_txt, "inverse", 10, 45)

print("--- 3. MOODY (addHappiness) ---")
print_method_around(ss_txt, "moody", 5, 25)

print("--- 4. DEFIANT (m_6469_) ---")
print_method_around(ss_txt, "defiant", 5, 30)

print("--- 5. PICKY (handleFeed) ---")
print_method_around(ss_txt, "picky", 10, 30)

print("--- 6. FERAL & SPIKY (m_6123_ playerTouch) ---")
print_method_around(ss_txt, "spiky", 10, 40)

print("--- 7. PUTRID (copyEffect) ---")
print_method_around(su_txt, "putrid", 5, 35)

print("--- 8. NUCLEAR & FLAMING & FLOATING & WEEPING (m_8119_) ---")
print_method_around(ss_txt, "nuclear", 5, 35)
print_method_around(ss_txt, "weeping", 5, 35)
print_method_around(ss_txt, "floating", 5, 35)
