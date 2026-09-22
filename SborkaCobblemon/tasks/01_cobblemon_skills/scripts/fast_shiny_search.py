import zipfile
import re

jar_path = r'G:\curseforge\minecraft\Instances\Society Sunlit Cobblemon\mods\cobblemon_farmers-2.4-all.jar'

with zipfile.ZipFile(jar_path, 'r') as z:
    for name in z.namelist():
        if name.endswith('.class'):
            data = z.read(name)
            if b'getShiny' in data or b'isShiny' in data or b'shiny' in data.lower():
                print("Found match in:", name)
