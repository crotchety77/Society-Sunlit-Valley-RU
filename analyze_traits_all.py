import os, glob

with open(r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\SplendidSlime_javap.txt', 'r', encoding='utf-8') as f:
    ss_txt = f.read()

with open(r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\SlimeUtils_javap.txt', 'r', encoding='utf-8') as f:
    su_txt = f.read()

with open(r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\SlimeComfortUtils_javap.txt', 'r', encoding='utf-8') as f:
    sc_txt = f.read()

# Let's inspect handleHungryTraits, handleMoodyTraits, tick, etc.
def find_method(txt, name):
    res = []
    lines = txt.split('\n')
    recording = False
    for l in lines:
        if name in l and ('public ' in l or 'private ' in l or 'protected ' in l):
            recording = True
        elif recording and ('public ' in l or 'private ' in l or 'protected ' in l) and '(' in l:
            break
        if recording:
            res.append(l)
    return '\n'.join(res)

print("=== handleHungryTraits ===")
print(find_method(su_txt, 'handleHungryTraits'))

print("=== handleMoodyTraits ===")
print(find_method(su_txt, 'handleMoodyTraits'))

print("=== checkComfort / SlimeComfortUtils ===")
print(sc_txt[:3000])

print("=== hasTrait in SplendidSlime ===")
print(find_method(ss_txt, 'hasTrait'))

print("=== tick / customServerAiStep in SplendidSlime ===")
print(find_method(ss_txt, 'customServerAiStep'))

print("=== emitEffects in SplendidSlime ===")
print(find_method(ss_txt, 'emitEffects'))

