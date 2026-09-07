#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

ROOT_DIR = r"c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода"
MODS_SLIME_JSON = os.path.join(ROOT_DIR, "translations", "mods", "splendid_slimes.json")
GAME_SLIME_JSON = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\splendid_slimes\lang\ru_ru.json"
SOCIETY_JSON = os.path.join(ROOT_DIR, "translations", "society", "ru_ru.json")
GAME_SOCIETY_JSON = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\society\lang\ru_ru.json"

# 1. Обновляем имя предмета "Билет слайма"
for path in [MODS_SLIME_JSON, GAME_SLIME_JSON]:
    if os.path.exists(path):
        data = json.load(open(path, 'r', encoding='utf-8'))
        data["item.splendid_slimes.slime_ticket"] = "Билет слайма"
        data["society.slime_ticket.sender"] = "Билет слайма"
        json.dump(data, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        print(f"✅ Обновлён: {path}")

for path in [SOCIETY_JSON, GAME_SOCIETY_JSON]:
    if os.path.exists(path):
        data = json.load(open(path, 'r', encoding='utf-8'))
        data["item.splendid_slimes.slime_ticket"] = "Билет слайма"
        data["society.slime_ticket.sender"] = "Билет слайма"
        json.dump(data, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        print(f"✅ Обновлён: {path}")

# 2. Обновляем тултип в addTooltips.js (в игре)
GAME_ADD_TOOLTIPS = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\client_scripts\tooltips\addTooltips.js"
if os.path.exists(GAME_ADD_TOOLTIPS):
    c = open(GAME_ADD_TOOLTIPS, 'r', encoding='utf-8').read()
    old_target = """  tooltip.add(
    "splendid_slimes:slime_ticket",
    Text.translatable("tooltip.society.slime_ticket").gray()
  );"""
    new_tooltip = """  tooltip.addAdvanced("splendid_slimes:slime_ticket", (item, advanced, text) => {
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
    if old_target in c:
        c = c.replace(old_target, new_tooltip)
        open(GAME_ADD_TOOLTIPS, 'w', encoding='utf-8').write(c)
        print("✅ Обновлён addTooltips.js в профиле игры")

# 3. Также добавляем в invitationTooltips.js для персистентности в репозитории
INV_TOOLTIPS = os.path.join(ROOT_DIR, "kubejs_scripts", "client", "invitationTooltips.js")
if os.path.exists(INV_TOOLTIPS):
    c = open(INV_TOOLTIPS, 'r', encoding='utf-8').read()
    if 'splendid_slimes:slime_ticket' not in c:
        ticket_block = """
  // Тултип для Билета слайма с поддержкой [SHIFT]
  tooltip.addAdvanced("splendid_slimes:slime_ticket", (item, advanced, text) => {
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
  });
});
"""
        c = c.rstrip().rstrip(';').rstrip(')').rstrip('}') + ticket_block
        # safer append before the closing
        # Let's inspect invitationTooltips structure first
