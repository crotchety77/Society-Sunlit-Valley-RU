#!/usr/bin/env python3
# -*- coding: utf-8 -*-

p = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\config\ftbquests\quests\chapters\iii__advanced_farming.snbt"
c = open(p, 'r', encoding='utf-8').read()

target = 'id: "632578AFE8A0D12D"'
pos = c.find(target)
if pos != -1:
    print("=== FOUND QUEST DEFINITION ===")
    print(c[pos-400:pos+300])
else:
    print("NOT FOUND with exact target, searching all occurrences of 632578AFE8A0D12D:")
    for m in [i for i in range(len(c)) if c.startswith('632578AFE8A0D12D', i)]:
        print(f"Occurence at {m}:")
        print(c[m-100:m+200])
        print("---")
