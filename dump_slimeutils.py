import os

with open(r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\SlimeUtils_javap.txt', 'r', encoding='utf-8') as f:
    su_txt = f.read()

with open(r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\SplendidSlime_javap.txt', 'r', encoding='utf-8') as f:
    ss_txt = f.read()

print("=== SLIME UTILS FULL DUMP ===")
print(su_txt)
