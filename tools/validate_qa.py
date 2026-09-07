import json, re, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
workspace = Path(__file__).resolve().parent.parent
ru_path = workspace / 'translations' / 'society' / 'ru_ru.json'
en_path = workspace / 'translations' / 'society' / 'en_us.json'

with open(ru_path, 'r', encoding='utf-8') as f:
    ru = json.load(f)

with open(en_path, 'r', encoding='utf-8') as f:
    en = json.load(f)

print("=" * 50)
print("=== RUNNING TRANSLATION VALIDATION QA ===")
print("=" * 50)

errors = []
warnings = []

translation_files = list((workspace / 'translations').rglob('*ru_ru.json'))
print(f"Found {len(translation_files)} Russian translation JSON files to validate.")

for json_file in sorted(translation_files):
    rel_path = json_file.relative_to(workspace)
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        errors.append(f"[{rel_path}] JSON syntax error: {e}")
        continue

    print(f"Checking {rel_path} ({len(data)} keys)...")
    for k, v in data.items():
        if not isinstance(v, str):
            errors.append(f"[{rel_path} : {k}] Value is not a string: {v}")
            continue

        # Check for legacy & color codes (&6, &d, etc.)
        legacy_amp = re.findall(r'&[0-9a-fk-or]', v)
        if legacy_amp:
            errors.append(f"[{rel_path} : {k}] Contains legacy '&' color codes: {legacy_amp} in text: {v}")

        # Check for unescaped single '%' (not %%, and not format tokens like %s, %d, %1$s, etc.)
        text_without_formatters = re.sub(r'%[0-9]*\$?[a-zA-Z]', '', v)
        single_percents = re.findall(r'(?<!%)%(?!%)', text_without_formatters)
        if single_percents:
            errors.append(f"[{rel_path} : {k}] Contains unescaped single '%': {v}")

print("=" * 50)
if errors:
    print(f"\n❌ FAILED with {len(errors)} errors:")
    for err in errors:
        print(f"  - {err}")
    sys.exit(1)
else:
    print("✓ All syntax checks passed (0 legacy '&' codes, 0 unescaped '%' signs across all translation files).")
    print("=" * 50)
