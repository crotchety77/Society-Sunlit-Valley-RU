---
name: replace_terms
description: Сквозной поиск и безопасная замена терминов, предметов и фраз по всем языковым файлам сборки (translations/ и game assets/) с верификацией и синхронизацией.
---

# Навык: replace_terms (Сквозная замена терминологии)

Используйте этот навык, когда требуется изменить термин, название предмета, профессию, статус или формулировку во всей сборке сразу, чтобы исключить разночтения и рассинхронизацию.

## Структура директорий сборки

| Раздел | Проект (`translations/`) | Профиль игры (`kubejs/assets/`) |
| :--- | :--- | :--- |
| **Предметы и блоки Society** | `translations/society/ru_ru.json` | `kubejs/assets/society/lang/ru_ru.json` |
| **Навыки Puffish Skills** | `translations/skills/ru_ru.json` | `kubejs/assets/society_skills/lang/ru_ru.json` |
| **Квесты FTB Quests** | `translations/ftbquests/ru_ru.json` | `kubejs/assets/ftbquestlocalizer/lang/ru_ru.json` |
| **Диалоги NPC** | `translations/dialogs/ru_ru.json` | `kubejs/assets/dialog/lang/ru_ru.json` |
| **Постройки и чертежи** | `translations/buildings/*` | `kubejs/assets/portable_blueprints/lang/ru_ru.json` |
| **Советы загрузки** | `translations/tips/*` | `kubejs/assets/society_tips/lang/ru_ru.json` |
| **Сторонние моды (overrides)** | `translations/overrides/*` | `kubejs/assets/<namespace>/lang/ru_ru.json` |

## Использование инструмента

В проекте есть готовый инструмент [tools/replace_term.py](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/tools/replace_term.py).

### Примеры запуска:

1. **Точная замена фразы**:
   ```powershell
   python tools/replace_term.py "Сундук с реликвиями" "Тайник с магическими реликвиями"
   ```

2. **Замена с игнорированием регистра**:
   ```powershell
   python tools/replace_term.py "сундук сокровищ" "тайник с сокровищами" --ignore-case
   ```

3. **Замена по регулярному выражению**:
   ```powershell
   python tools/replace_term.py "Сундук[а-я]* с реликвиями" "Тайник с магическими реликвиями" --regex
   ```

## Обязательные шаги процесса

1. **Поиск и замена**: Скрипт обходит все JSON-файлы исходников (`translations/`) и физических игровых файлов (`D:\ModrinthApp\...\kubejs\assets`).
2. **Синхронизация**: Автоматически вызывается `sync_all_to_game.js`.
3. **Верификация**: Считать изменённые ключи напрямую из физических файлов игры и вывести их значения пользователю.
4. **Инструкция**: Напомнить пользователю нажать **`F3 + T`** в игре.
