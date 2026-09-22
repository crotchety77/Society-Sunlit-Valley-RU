# 📋 Полное руководство и план действий: Сбор и каталогизация предметов с сервера в Excel

Данный документ описывает готовую архитектуру и пошаговый регламент: как безопасно просканировать хранилища на любом общественном сервере Minecraft, извлечь метаданные из JAR-модов и собрать красивый отчёт в Excel.

---

## 🏗 Общая схема процесса (Pipeline)

```
[Общественный сервер / Мир]
           │
           ▼  (Игрок открывает бочку и нажимает F8)
[Клиентский KubeJS: barrel_tm_scanner.js]
  ├─ Читает открытый экран: screen.menu.slots
  ├─ Отсекает личные слоты инвентаря: slot.container !== player.inventory
  ├─ Считывает теги (#simpletms:type_*) и ID предметов
  └─ Сохраняет через JsonIO.write() -> kubejs/my_tms_inventory.json
           │
           ▼
[Python Обработчик: export_tms_to_excel.py]
  ├─ Считывает файлы my_tms_inventory*.json (суммирует дубликаты)
  ├─ Распаковывает метаданные из JAR:
  │   ├─ SimpleTMsForge.jar -> moves.json (точные типы и ID)
  │   └─ Cobblemon.jar -> ru_ru.json (официальные русские названия)
  └─ Генерирует Excel (.xlsx) с цветными бейджами, вкладками и автосуммой
           │
           ▼
[Итоговый Excel-каталог: Cobblemon_TM_TR_Inventory.xlsx]
```

---

## 🚀 Пошаговый план действий (Инструкция)

### Шаг 1. Установка клиентского сканера в сборку
1. Создать/поместить скрипт `barrel_tm_scanner.js` в папку:  
   📁 `<папка_клиента>/kubejs/client_scripts/barrel_tm_scanner.js`
2. Перезагрузить скрипты в игре комбинацией **`F3 + T`** (или командой `/kubejs reload client`).

### Шаг 2. Сканирование бочек на сервере
1. Подключиться к любому серверу.
2. Подойти к первой бочке/сундуку $\rightarrow$ **открыть GUI** $\rightarrow$ нажать **`F8`**.
   * В чате появится: `✔ Бочка #1 добавлена (+X шт.)!`.
3. Подойти ко второй бочке $\rightarrow$ **открыть GUI** $\rightarrow$ нажать **`F8`**.
   * Скрипт суммирует дубликаты и пополнит общий список.
4. *(Если нужно сбросить базу и начать с нуля — нажать **`Shift + F8`**)*.
5. Результат автоматически сохранится в:  
   📁 `<папка_клиента>/kubejs/my_tms_inventory.json`

### Шаг 3. Запуск генератора Excel
1. Поместить сохранённый `.json` в рабочую папку `tasks/Disk_copy_barrel/docs/`.
2. Запустить скрипт генератора:
   ```bash
   python tasks/Disk_copy_barrel/scripts/export_tms_to_excel.py
   ```
3. Открыть готовый файл:  
   📁 `tasks/Disk_copy_barrel/docs/Cobblemon_TM_TR_Inventory.xlsx`

---

## ⚙️ Технические нюансы и решения (Gotchas & Best Practices)

| Проблема / Ограничение | Причина | Правильное решение |
| :--- | :--- | :--- |
| **Java ClassFilter Sandbox** | KubeJS блокирует `java.nio.file.Paths` на клиенте | Использовать встроенный метод **`JsonIO.write('path.json', data)`** |
| **Опрос клавиш в GUI** | `Client.window.handle` в 1.20.1 возвращает `undefined` | Получать нативный дескриптор: `Minecraft.getInstance().getWindow().getWindow()` |
| **Лишние предметы из инвентаря** | `menu.slots` включает 36 слотов инвентаря игрока | Проверять `slot.container === player.inventory` и пропускать их |
| **Числовая сортировка дисков** | Стандартная сортировка ставит `TM-10` перед `TM-2` | Извлекать число `re.search(r'\d+', name)` и сортировать как `int` |
| **Русский язык в Excel** | Windows Excel искажает UTF-8 CSV | Генерировать полноценный `.xlsx` через библиотеку `openpyxl` |

---

## 🔄 Как адаптировать этот метод под ДРУГИЕ предметы

Если вам понадобится просканировать не ТМ-диски, а, например:
* **Покеболы / Априкорны**
* **Семена и урожай из Farmer's Delight**
* **Зелья, свитки или зачарованные книги**

### Достаточно изменить всего 1 условие в `barrel_tm_scanner.js`:

```javascript
// ВМЕСТО фильтра ТМ-дисков:
if (id.includes('simpletms') || id.includes(':tm_'))

// ПОСТАВИТЬ нужный мод/тег:
if (id.includes('cobblemon:poke_ball') || id.includes('apricorn'))
// или вообще убрать if, чтобы сканировать АБСОЛЮТНО ВСЕ предметы в сундуке!
```

---

## 📁 Структура файлов задачи

```text
tasks/Disk_copy_barrel/
├── README.md                      # Быстрый обзор и документация
├── scripts/
│   ├── barrel_tm_scanner.js       # Клиентский скрипт для KubeJS
│   └── export_tms_to_excel.py     # Python-генератор Excel
└── docs/
    ├── WORKFLOW_PLAN.md           # Этот план действий
    ├── my_tms_inventory.json      # Дамп бочки 1 (TM)
    ├── my_tms_inventory2.json     # Дамп бочки 2 (TR)
    ├── my_tms_inventory3.json     # Дамп бочки 3 (TR)
    └── Cobblemon_TM_TR_Inventory.xlsx # Итоговая Excel таблица
```
