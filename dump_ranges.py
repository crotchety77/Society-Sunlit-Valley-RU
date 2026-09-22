with open(r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\SplendidSlime_javap.txt', 'r', encoding='utf-8') as f:
    ss_txt = f.read()

lines = ss_txt.split('\n')

def show_lines(start, count):
    for i in range(start, min(len(lines), start + count)):
        print(f"{i}: {lines[i]}")

print("=== DOMINANT (getSlimeFoods) ===")
show_lines(1620, 50)

print("\n=== INVERSE (m_8119_) ===")
show_lines(170, 70)

print("\n=== MOODY (addHappiness) ===")
show_lines(2100, 40)

print("\n=== DEFIANT (m_6469_) ===")
show_lines(2600, 40)

print("\n=== PICKY (handleFeed) ===")
show_lines(2380, 50)

print("\n=== FERAL / SPIKY (m_6123_) ===")
show_lines(2520, 50)
