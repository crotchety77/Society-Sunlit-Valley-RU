#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

ROOT_DIR = r"c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода"
SOCIETY_JSON = os.path.join(ROOT_DIR, "translations", "society", "ru_ru.json")
GAME_SOCIETY_JSON = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\society\lang\ru_ru.json"
GAME_ADD_TOOLTIPS = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\client_scripts\tooltips\addTooltips.js"

# 1. Возвращаем корректную первую строку описания в lang, чтобы убрать пустой пропуск
for p in [SOCIETY_JSON, GAME_SOCIETY_JSON]:
    if os.path.exists(p):
        d = json.load(open(p, 'r', encoding='utf-8'))
        d['block.society.charging_rod.description'] = "Создаёт батареи во время грозы. Не защищает территорию."
        json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        print(f"✅ Установлено описание block.society.charging_rod.description в {p}")

# 2. Очищаем addTooltips.js от дубликата slime_ticket (чтобы не двоилось)
if os.path.exists(GAME_ADD_TOOLTIPS):
    c = open(GAME_ADD_TOOLTIPS, 'r', encoding='utf-8').read()
    # Убираем дублирующий addAdvanced для slime_ticket из addTooltips.js
    dup_block = """  tooltip.addAdvanced("splendid_slimes:slime_ticket", (item, advanced, text) => {
    if (tooltip.shift) {
      text.add(Text.of("§7Используйте на слайме, чтобы раскрыть его любимое"));
      text.add(Text.of("§7лакомство для Анализатора и получить образец еды."));
      text.add(Text.of(""));
      text.add(Text.of("§6▪ Способ получения:"));
      text.add(Text.of("§7С шансом §e15%§7 выпадает из §fИнкубатора слизней§7 при"));
      text.add(Text.of("§7выведении, если изучена Книга навыка §a«Слаймик. Схватит. Кормить»§7."));
    } else {
      text.add(Text.of("§7Используйте на слайме, чтобы раскрыть его любимое"));
      text.add(Text.of("§7лакомство для Анализатора и получить образец еды."));
      text.add(Text.of("§8[Зажмите SHIFT для подробностей получения]"));
    }
  });"""
    if dup_block in c:
        c = c.replace(dup_block, "")
        open(GAME_ADD_TOOLTIPS, 'w', encoding='utf-8').write(c)
        print("✅ Удалён дубликат slime_ticket из addTooltips.js")
