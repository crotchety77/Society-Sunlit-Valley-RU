import os
import glob

# Search for any directory with ftbquests or 4.1.4 or chapters
for root, dirs, files in os.walk(r"c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода"):
    for d in dirs:
        if "4.1.4" in d or "4.0.4" in d or "chapters" in d:
            print(os.path.join(root, d))
