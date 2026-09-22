with open(r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\SplendidSlime_javap.txt', 'r', encoding='utf-8') as f:
    ss_txt = f.read()

with open(r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\SlimeUtils_javap.txt', 'r', encoding='utf-8') as f:
    su_txt = f.read()

# Let's inspect specific methods in detail:
# 1. getSlimeFoods (dominant)
# 2. m_8119_ (inverse, nuclear, floating, weeping)
# 3. addHappiness (moody)
# 4. m_6469_ (defiant)
# 5. handleFeed (picky)
# 6. m_6123_ (feral, spiky)
# 7. copyEffect (putrid)
# 8. m_6673_ (aquatic, flaming)
# 9. m_7243_ / breeding (largoless)
# 10. m_6071_ (handy)
# 11. handleHungryTraits (explosive, flaming)

import re

def print_method_exact(txt, name):
    lines = txt.split('\n')
    rec = False
    for i, l in enumerate(lines):
        if re.search(r'\b' + name + r'\b', l) and ('public ' in l or 'private ' in l or 'protected ' in l):
            rec = True
            print(f"=== METHOD: {l.strip()} ===")
        elif rec and ('public ' in l or 'private ' in l or 'protected ' in l) and '(' in l:
            break
        if rec:
            print(l)

print("--- getSlimeFoods ---")
print_method_exact(ss_txt, 'getSlimeFoods')

print("\n--- addHappiness ---")
print_method_exact(ss_txt, 'addHappiness')

print("\n--- m_6469_ (hurt) ---")
print_method_exact(ss_txt, 'm_6469_')

print("\n--- handleFeed ---")
print_method_exact(ss_txt, 'handleFeed')

print("\n--- m_6123_ (playerTouch) ---")
print_method_exact(ss_txt, 'm_6123_')

print("\n--- copyEffect ---")
print_method_exact(su_txt, 'copyEffect')

print("\n--- handleHungryTraits ---")
print_method_exact(su_txt, 'handleHungryTraits')

print("\n--- m_7243_ (canEatItem / breed) ---")
print_method_exact(ss_txt, 'm_7243_')

print("\n--- m_6071_ (mobInteract) ---")
print_method_exact(ss_txt, 'm_6071_')
