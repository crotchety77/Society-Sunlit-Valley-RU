# Задача: Исправление имён жителей и подписи странствующего торговца

## 🎯 Цели задачи
1. **Замена «Кладовщик» на «Библиотекарь»**:
   - `translations/society/ru_ru.json`: ключ `"entity.minecraft.villager.weaponsmith"` $\rightarrow$ `"Библиотекарь"`.
   - `translations/ftbquests/ru_ru.json`:
     - Заголовок квеста `49477F09DF6EBA50` (глава `villagers`): `"Кладовщик"` $\rightarrow$ `"Библиотекарь"`.
     - Описание квеста `49477F09DF6EBA50`: `"&6Кладовщик&r..."` $\rightarrow$ `"&6Библиотекарь&r..."`.
     - Описание квеста `61501449BF31B773` (глава `ii__building_up_the_farm`): `"житель-&6кладовщик&r"` $\rightarrow$ `"житель-&6библиотекарь&r"`.
   - Реестры квестов FTB Quests: `tasks/FTB_QUESTS_4_1_4/registry_quests.md` и `.json`.
2. **Имя странствующего торговца**:
   - Добавить `"entity.minecraft.wandering_trader": "Карлос"` в `translations/society/ru_ru.json` и `translations/mods/minecraft.json`.
   - При наведении на торговца и в надписи над головой теперь будет отображаться лаконичное имя **Карлос** вместо длинного технического «Странствующий торговец».
3. **Синхронизация и проверка**:
   - Запустить скрипт применения и синхронизации `apply_and_sync.py`.
   - Физически проверить игровые файлы в `D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\`.

## 📋 Чек-лист
- [x] Составить и согласовать файл `new_translate.md`
- [x] Разработать скрипт `scripts/apply_and_sync.py`
- [x] Применить изменения в проекте и синхронизировать с игрой
- [x] Верифицировать ключи в `kubejs/assets/`
