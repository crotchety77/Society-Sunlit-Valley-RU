#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

p = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\data\splendid_slimes\slimes"
for f in sorted(os.listdir(p)):
    if f.endswith('.json'):
        d = json.load(open(os.path.join(p, f), 'r', encoding='utf-8'))
        breed = d.get('breed')
        diet = d.get('diet')
        foods = d.get('foods', [])
        fav = d.get('favorite_food', {})
        print(f"{breed:12} | Foods: {foods} | Fav: {fav.get('item') or fav.get('tag')}")
