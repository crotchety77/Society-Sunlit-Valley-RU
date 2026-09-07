#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

ROOT_DIR = r"c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода"
GAME_DIR = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs"

print("=== 1. Поиск точных двух фраз ===")

def search_phrase(phrase, path):
    matches = []
    for root, dirs, files in os.walk(path):
        for f in files:
            if f.endswith(('.json', '.js', '.md')):
                p = os.path.join(root, f)
                try:
                    lines = open(p, 'r', encoding='utf-8').readlines()
                    for idx, l in enumerate(lines):
                        if phrase.lower() in l.lower():
                            matches.append((p, idx + 1, l.strip()))
                except:
                    pass
    return matches

for ph in ["Анализ состояния слизня", "весело хлюпает"]:
    print(f"\n--- Поиск: '{ph}' ---")
    for p, line_no, content in search_phrase(ph, ROOT_DIR) + search_phrase(ph, GAME_DIR):
        print(f"  [{os.path.basename(p)}:{line_no}] {content}")

print("\n=== 2. Поиск всех слов с корнем 'слиз' в моде Splendid Slimes ===")
splendid_json = os.path.join(ROOT_DIR, "translations", "mods", "splendid_slimes.json")
with open(splendid_json, 'r', encoding='utf-8') as f:
    data = json.load(f)

slime_pattern = re.compile(r'\b(слизень|слизня|слизню|слизнем|слизне|слизни|слизней|слизням|слизнями|слизнях|слизене|слизняка|слизняком)\b', re.IGNORECASE)

matches = []
for k, v in data.items():
    if slime_pattern.search(v):
        matches.append((k, v))

print(f"Найдено ключей со словом 'слизень' в splendid_slimes: {len(matches)}")
for k, v in matches:
    print(f"  ▪ [{k}] -> {v}")
