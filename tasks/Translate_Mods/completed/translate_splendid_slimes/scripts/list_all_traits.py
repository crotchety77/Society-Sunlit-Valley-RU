#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json

p = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\data\splendid_slimes\slimes"
for f in sorted(os.listdir(p)):
    if f.endswith('.json'):
        d = json.load(open(os.path.join(p, f), 'r', encoding='utf-8'))
        breed = d.get('breed')
        traits = d.get('traits', [])
        print(f"{breed:12}: traits = {traits}")
