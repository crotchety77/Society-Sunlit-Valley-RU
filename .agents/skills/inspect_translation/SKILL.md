---
name: inspect_translation
description: Мгновенный поиск любого термина, ID предмета или ключа локализации по всем 6 пространствам имён сборки (Society, Skills, Quests, Dialogs, Blueprints, Tips).
---

# Навык: inspect_translation (Инспекция переводов)

Используйте этот навык перед переводом новых квестов, диалогов или предметов, чтобы проверить уже устоявшуюся терминологию сборки.

## Как использовать

Запустите скрипт инспекции с ID предмета или словом:

```powershell
# Поиск по ID предмета
python tools/inspect_term.py "relic_trove"

# Поиск по названию
python tools/inspect_term.py "Раскалыватель жеод"

# Поиск по ключу диалога или квеста
python tools/inspect_term.py "dialog.npc.blacksmith"
```

Инструмент выведет текущие значения `EN` и `RU` по всем разделам сразу.
