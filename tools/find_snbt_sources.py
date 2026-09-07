import os
import glob
import zipfile

print("=== Checking Downloads ===")
for root, dirs, files in os.walk(r"C:\Users\Foxi8\Downloads"):
    for f in files:
        if "society" in f.lower() or "sunlit" in f.lower() or "ftbquests" in f.lower() or "4.1.4" in f.lower():
            fp = os.path.join(root, f)
            print(fp, os.path.getsize(fp))

print("\n=== Checking backups ===")
backups_dir = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\backups"
if os.path.exists(backups_dir):
    for f in os.listdir(backups_dir):
        if f.endswith('.zip'):
            zp = os.path.join(backups_dir, f)
            try:
                with zipfile.ZipFile(zp, 'r') as z:
                    for name in z.namelist():
                        if "advanced_farming" in name:
                            print(f"Found in {f}: {name}")
            except Exception as e:
                pass
