# TestPlan: Полная верификация и локализация Patchouli Almanac («Фермерский альманах»)

> **Документ:** `docs/Patchouli/Almanac_Localization_TestPlan.md`  
> **Статус:** `APPROVED / READY FOR EXECUTION`  
> **Целевая книга:** `patchouli:almanac` (Фермерский альманах)

---

## 1. Scope (Область охвата)
Локализация книги `patchouli:almanac` охватывает:
* **Категории:** 6 категорий (`categories/*.json`)
* **Статьи (Entries):** 191 статья (`entries/**/*.json`)
* **Страницы (Pages):** 386 страниц контента
* **Связанные игровые объекты:** 191 уникальный игровой объект (растения, деревья, животные, рыбы, механизмы, кулинарные блюда, удобрения, ресурсы).
* **Смежные пространства имён (Namespaces):** `minecraft`, `farmersdelight`, `vintagedelight`, `pamhc2trees`, `aquaculture`, `unusualfishmod`, `netherdepthsupgrade`, `dew_drop_watering_cans`, `dew_drop_farmland_growth`, `society`.

---

## 2. Принцип Single Source of Truth (Единый источник истины)

```
Игровой реестр (Registry ID)
         ↓
Языковой ключ локализации (Translation Key)
         ↓
Актуальный файл локализации игры (kubejs/assets/**/lang/ru_ru.json)
         ↓
Patchouli Almanac (ru_ru/*.json)
```

> ⚠️ **Критическое правило:** Старый перевод внутри Almanac **НЕ** является источником истины. Источником истины является **текущее фактическое название предмета в инвентаре игры**.

---

## 3. Инвентаризация файлов и структуры

| Компонент | Исходный путь (EN) | Целевой путь (RU) | Кол-во файлов | Кол-во страниц |
| :--- | :--- | :--- | :---: | :---: |
| **Корневой манифест** | `almanac/book.json` | `almanac/ru_ru/book.json` | 1 | — |
| **Категории (Categories)** | `almanac/en_us/categories/*.json` | `almanac/ru_ru/categories/*.json` | 6 | — |
| • `animals` (Животные) | `categories/animals.json` | `categories/animals.json` | 1 | — |
| • `crops` (Культуры) | `categories/crops.json` | `categories/crops.json` | 1 | — |
| • `fertilizer` (Удобрения) | `categories/fertilizer.json` | `categories/fertilizer.json` | 1 | — |
| • `fish` (Рыба) | `categories/fish.json` | `categories/fish.json` | 1 | — |
| • `mechanics` (Механики) | `categories/mechanics.json` | `categories/mechanics.json` | 1 | — |
| • `trees` (Деревья) | `categories/trees.json` | `categories/trees.json` | 1 | — |
| **Статьи (Entries)** | `almanac/en_us/entries/**/*.json` | `almanac/ru_ru/entries/**/*.json` | **191** | **386** |
| • `animals/` | `entries/animals/*.json` | `entries/animals/*.json` | 18 | 36 |
| • `crops/` | `entries/crops/*.json` | `entries/crops/*.json` | 66 | 132 |
| • `fertilizer/` | `entries/fertilizer/*.json` | `entries/fertilizer/*.json` | 6 | 12 |
| • `fish/` | `entries/fish/*.json` | `entries/fish/*.json` | 74 | 148 |
| • `mechanics/` | `entries/mechanics/*.json` | `entries/mechanics/*.json` | 11 | 24 |
| • `trees/` | `entries/trees/*.json` | `entries/trees/*.json` | 16 | 34 |
| **ИТОГО:** | — | — | **198 JSON** | **386 Pages** |

---

## 4. Матрица проверок (Verification Matrix)

| Уровень проверки | Объект проверки | Метод проверки | Критерий PASS |
| :--- | :--- | :--- | :--- |
| **L1. Структурный** | Наличие всех файлов и страниц | Сравнение графа с `en_us` | 6/6 категорий, 191/191 статей, 386/386 страниц |
| **L2. Синтаксический** | Валидность JSON | Парсер `json.loads` | 0 синтаксических ошибок, валидный JSON |
| **L3. Идентичность названий** | Поля `name` в статьях | Сверка с `Source of Truth Matrix` | 100% совпадение с актуальным названием в игре |
| **L4. Текст страниц** | Поля `text`, `description` | Аудит ключевых объектов и терминов | Отсутствие артефактов старого перевода (156 Drift разрешены) |
| **L5. Ихтиологический** | Названия рыб в `entries/fish/` | Сверка с аудитом 74 рыб | 100% совпадение с единой основой (Raw/Smoked) |
| **L6. Ссылочный** | Внутренние ссылки `$(l:...)` | Проверка существования целей | 0 битых ссылок |
| **L7. Игровой/Runtime** | Открытие книги в игре | Загрузка `patchouli:almanac` | Книга открывается без ошибок, все страницы на русском |

---

## 5. Набор тестовых сценариев (Test Cases)

* **TEST-001:** Все 6 файлов категорий присутствуют в `patchouli_books/almanac/ru_ru/categories/`.
* **TEST-002:** Все 191 файлов статей присутствуют в `patchouli_books/almanac/ru_ru/entries/`.
* **TEST-003:** Общее количество страниц в `ru_ru` равно **386** (без потерь).
* **TEST-004:** Все JSON-файлы валидны и не содержат trailing commas или неэкранированных кавычек.
* **TEST-005:** Все Category IDs (`name`, `description`, `icon`) корректны и переведены.
* **TEST-006:** Все Entry IDs соответствуют `en_us` оригиналу.
* **TEST-007:** Имена статей (`name`) в точности совпадают с активными названиями предметов в игре (191/191).
* **TEST-008:** Все 156 случаев Translation Drift разрешены в пользу актуальной локализации игры.
* **TEST-009:** Все 74 рыбы категории `fish/` используют подтверждённые названия из аудита рыб.
* **TEST-010:** Все рецепты коптильни, ковки, крафта и ссылки на предметы ссылаются на валидные `item_id`.
* **TEST-011:** Непреднамеренный английский пользовательский текст отсутствует во всех 386 страницах.
* **TEST-012:** Файлы синхронизированы в игровом профиле (`patchouli_books/almanac/ru_ru/`) и дистрибутиве `Русификатор.zip`.

---

## 6. Стратегия отката (Rollback Strategy)
* Исходное состояние `patchouli_books/almanac/ru_ru/` и `patchouli_books/almanac/en_us/` полностью сохранено в `patchouli_books/almanac/en_us/` и резервных копиях.
* При обнаружении критических расхождений в структуре восстанавливается исходный шаблон из `en_us`.

---

## 7. Артефакты плана выполнения

1. [`docs/Patchouli/Almanac_Localization_TestPlan.md`](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/docs/Patchouli/Almanac_Localization_TestPlan.md) — данный план тестирования.
2. [`docs/Patchouli/Almanac_Localization_Baseline.md`](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/docs/Patchouli/Almanac_Localization_Baseline.md) — фиксация начального состояния.
3. [`docs/Patchouli/Almanac_SourceOfTruth_Matrix.md`](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/docs/Patchouli/Almanac_SourceOfTruth_Matrix.md) — реестр источников правды для 191 объекта.
4. [`docs/Patchouli/Almanac_Translation_Drift_Resolution.md`](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/docs/Patchouli/Almanac_Translation_Drift_Resolution.md) — резолюция всех 156 расхождений.
5. [`docs/Patchouli/Almanac_Fish_Name_Consistency.md`](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/docs/Patchouli/Almanac_Fish_Name_Consistency.md) — таблица согласованности 74 рыб.
6. [`docs/Patchouli/Almanac_Final_Checklist.md`](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/docs/Patchouli/Almanac_Final_Checklist.md) — чек-лист финальной проверки.
7. [`docs/Patchouli/Almanac_Localization_Final_Report.md`](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/docs/Patchouli/Almanac_Localization_Final_Report.md) — итоговый отчёт.
