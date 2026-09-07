#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sys
import json

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

p = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\config\ftbquests\quests\chapters\iii__advanced_farming.snbt"
c = open(p, 'r', encoding='utf-8').read()

m = re.search(r'\{[^{}]*?id:\s*"632578AFE8A0D12D"[^{}]*?\}', c, re.DOTALL)
if m:
    print("=== SNBT BLOCK ===")
    print(m.group(0))

ru = json.load(open(r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\ftbquestlocalizer\lang\ru_ru.json", 'r', encoding='utf-8'))
print("\n=== RU KEYS FOR 632578AFE8A0D12D ===")
for k, v in ru.items():
    if "632578AFE8A0D12D" in k:
        print(f"{k} -> {repr(v)}")
