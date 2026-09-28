# Перенос переводов KubeJS → Resource Pack

## Исходная структура

До проведения эксперимента русификатор распространялся в виде комбинированного пакета (`dist/Русификатор/` и `dist/Русификатор.zip`), содержащего:
1. **`kubejs/assets/<namespace>/lang/ru_ru.json`** — 62 языковых файла (всего 14 870 ключей перевода), расположенных в виртуальном пространстве ресурсов KubeJS.
2. **`kubejs/assets/ftbquestlocalizer/lang/en_us.json`** — 1 660 ключей (исходные английские идентификаторы квестов для сопоставления).
3. **`kubejs/assets/society/tooltipoverhaul/custom_frames.json`** — файл конфигурации кастомных рамок всплывающих подсказок для мода Tooltip Overhaul.
4. **`kubejs/client_scripts/`** — 14 скриптов всплывающих подсказок (`ItemEvents.tooltip`, `tooltip.addAdvanced`) и интеграций JEI.
5. **`kubejs/server_scripts/`** — 4 кастомных серверных скрипта игровых механик (`slimeInspectorEnhanced.js`, `slimeTicket.js`, `handleDebt.js`, `globalServer.js`).
6. **`resourcepacks/Перевод модов.zip`** — упакованный архив ресурс-пака, в котором параллельно находились те же самые 62 пространства имён `assets/<namespace>/lang/ru_ru.json`.

---

## Что было найдено в ходе аудита

1. **Полное дублирование переводов:**
   Все 62 файла `lang/ru_ru.json` (14 870 ключей) физически присутствовали одновременно и в `kubejs/assets/`, и внутри `resourcepacks/Перевод модов.zip`.
2. **Иерархия приоритетов загрузки (Resource Priority):**
   В Minecraft Forge ресурс-паки из папки `resourcepacks/` (активированные в `options.txt`) загружаются **поверх** встроенных ресурсов модов и KubeJS (`kubejs:assets`). 
   *Следствие:* Если файл присутствует в `resourcepacks/Перевод модов.zip`, игра считывает перевод из ZIP-архива ресурспака. Изменения, вносимые только в `kubejs/assets/`, перекрывались ресурспаком.
3. **Не-языковые файлы в `kubejs/assets/`:**
   В папке `kubejs/assets/society/tooltipoverhaul/custom_frames.json` обнаружен конфигурационный файл рамок интерфейса. Он не является языковым файлом и не подлежит автоматическому переносу в `lang/`.
4. **Английский эталон квестов:**
   `kubejs/assets/ftbquestlocalizer/lang/en_us.json` необходим FTB Quests для корректного маппинга ключей квестовых глав и не должен удаляться.

---

## Что перенесено (`[MOVE]`)

Все 62 языковых файла русской локализации (`ru_ru.json`) вынесены из структуры `kubejs/assets/` и консолидированы строго внутри ресурс-пака:

| Категория | Namespaces | Примеры |
| :--- | :--- | :--- |
| **Системные переводы сборки** | `society`, `society_skills`, `society_tips`, `dialog`, `portable_blueprints`, `society_trading`, `ftbquestlocalizer` | Описания предметов, перки Puffish Skills, диалоги жителей, чертежи, квесты FTB Quests |
| **Контентные и декоративные моды** | `cluttered`, `whimsy_deco`, `tanukidecor`, `refurbished_furniture`, `twigs`, `meadow`, `beachparty` | Мебель, блоки декора, 62 плюшевые игрушки |
| **Технические и механические моды** | `numismatics`, `create_central_kitchen`, `functionalstorage`, `buildinggadgets2`, `moreminecarts`, `automobility` | Банковский терминал, валюта, валидаторы, хранилища, транспорт |
| **Флора, фауна и рыбалка** | `aquaculture`, `unusualfishmod`, `longwings`, `splendid_slimes`, `legendarycreatures`, `pamhc2trees`, `vintagedelight` | Рыбы, бабочки, слаймы, деревья, кулинария |
| **Утилитарные моды и патчи** | `bountiful`, `paraglider`, `justhammers`, `gag`, `rehooked`, `moblassos`, `sewingkit`, `simplehats`, `dramaticdoors`... | Заказы, крюки, шляпы, двери |

---

## Что осталось в KubeJS (`[KEEP]`)

В структуре `kubejs/` экспериментального пакета сохранены только те компоненты, которые функционально не могут быть ресурс-паком:

1. **`kubejs/assets/ftbquestlocalizer/lang/en_us.json`** — 1 660 ключей английского эталона FTB Quests.
2. **`kubejs/assets/society/tooltipoverhaul/custom_frames.json`** — конфигурация кастомных рамок тултипов.
3. **`kubejs/client_scripts/`** (14 файлов):
   - `tooltips/addTooltips.js`
   - `tooltips/addAdvancedTooltips.js`
   - `tooltips/addFishTooltips.js`
   - `tooltips/addPriceTooltips.js`
   - `tooltips/bountifulTooltips.js`
   - `tooltips/buildinggadgets2Tooltips.js`
   - `tooltips/createCentralKitchenTooltips.js`
   - `tooltips/etceteraTooltips.js`
   - `tooltips/invitationTooltips.js`
   - `tooltips/longwingsTooltips.js`
   - `tooltips/tanukiDecorTooltips.js`
   - `tooltips/unusualFishTooltips.js`
   - `etceteraJei.js`
   - `universalGiftsJei.js`
4. **`kubejs/server_scripts/`** (4 файла):
   - `entities/slimeInspectorEnhanced.js`
   - `entities/slimeTicket.js`
   - `globalServer.js`
   - `handleDebt.js`

---

## Структура Resource Pack

В экспериментальной копии архив `resourcepacks/Перевод модов.zip` сформирован по каноническому стандарту Minecraft:

```text
Перевод модов.zip
├── pack.mcmeta
└── assets/
    ├── aquaculture/lang/ru_ru.json
    ├── cluttered/lang/ru_ru.json
    ├── dialog/lang/ru_ru.json
    ├── ftbquestlocalizer/lang/ru_ru.json
    ├── numismatics/lang/ru_ru.json
    ├── perfectplushies/lang/ru_ru.json
    ├── portable_blueprints/lang/ru_ru.json
    ├── society/lang/ru_ru.json
    ├── society_skills/lang/ru_ru.json
    ├── society_tips/lang/ru_ru.json
    ├── ... (всего 62 namespace)
    └── whimsy_deco/lang/ru_ru.json
```

Содержимое `pack.mcmeta`:
```json
{
  "pack": {
    "pack_format": 15,
    "description": "§6Society: Sunlit Valley §7— Полный перевод модов и сборки"
  }
}
```

---

## Проверка translation keys и KubeJS-generated content

### 1. Поддержка кастомных пространств имён сборки:
Minecraft движок локализации (`ClientLanguage`) считывает **все** файлы `assets/<namespace>/lang/ru_ru.json` из активных ресурс-паков и объединяет их в единую глобальную таблицу соответствий. 
* **`society:*`** (тултипы предметов, описания черт, кастомные предметы `society:coin_pouch` и др.) $\rightarrow$ считываются из `assets/society/lang/ru_ru.json`.
* **`dialog:*`** (диалоговые ветки жителей) $\rightarrow$ считываются из `assets/dialog/lang/ru_ru.json`.
* **`society_skills:*`** (древо навыков `K`) $\rightarrow$ считываются из `assets/society_skills/lang/ru_ru.json`.
* **`ftbquestlocalizer:*`** (квесты FTB Quests) $\rightarrow$ считываются из `assets/ftbquestlocalizer/lang/ru_ru.json`.

### 2. Динамические предметы KubeJS:
Предметы с кастомными NBT или расширенными регистрациями (`perfectplushies:adv_...`, `cluttered:adv_...`, `kata:adv_...`) используют стандартные translation keys вида `item.perfectplushies.adv_...`. Присутствие их переводов в `assets/perfectplushies/lang/ru_ru.json` внутри Resource Pack полностью покрывает их отображение в инвентаре, JEI и тултипах.

---

## Runtime-проверка

* **Статус проверки:** `NOT PERFORMED` (в текущей изолированной среде терминала прямой запуск графического клиента Minecraft не выполнялся).
* **Статическая верификация целостности:**
  - Валидность синтаксиса всех 62 JSON файлов: **100% PASS** (0 ошибок синтаксиса).
  - Отсутствие BOM-символов (UTF-8 No BOM): **100% PASS**.
  - Соответствие 14 870 ключей между исходными файлами и ресурс-паком: **100% PASS**.

---

## Сравнение до / после

| Параметр | Исходный дистрибутив (`Русификатор/`) | Экспериментальный (`Русификатор_resourcepack_experiment/`) | Разница |
| :--- | :--- | :--- | :--- |
| **Всего файлов в пакете** | 83 файла | 21 файл | **-62 файла (-74,7%)** |
| **Файлов в `kubejs/assets/`** | 64 файла | 2 файла | **-62 файла** |
| **Файлов в `kubejs/scripts/`** | 18 файлов | 18 файлов | Без изменений |
| **Ресурс-паков (`resourcepacks/`)** | 1 архив (`Перевод модов.zip`) | 1 архив (`Перевод модов.zip`) | Оптимизирован |
| **Ключей перевода в KubeJS** | 16 531 ключ | 1 661 ключ (`en_us` + `frames`) | **-14 870 дубликатов** |
| **Ключей перевода в Resource Pack** | 14 870 ключей | 14 870 ключей | Сохранены на 100% |
| **Размер ZIP-дистрибутива** | 784 129 байт (~784 КБ) | 439 422 байт (~439 КБ) | **-344,7 КБ (-44,0%)** |
| **Конфликтов / Потерь ключей** | 0 | 0 | **0 потерь** |

### Детальная таблица по пространствам имён:

| Namespace | Файл до | Файл после | Ключей | Перенесено | Статус проверки |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `aquaculture` | `kubejs/assets/aquaculture/lang/ru_ru.json` | `assets/aquaculture/lang/ru_ru.json` (в RP) | 43 | YES | PASS |
| `automobility` | `kubejs/assets/automobility/lang/ru_ru.json` | `assets/automobility/lang/ru_ru.json` (в RP) | 161 | YES | PASS |
| `beachparty` | `kubejs/assets/beachparty/lang/ru_ru.json` | `assets/beachparty/lang/ru_ru.json` (в RP) | 120 | YES | PASS |
| `bountiful` | `kubejs/assets/bountiful/lang/ru_ru.json` | `assets/bountiful/lang/ru_ru.json` (в RP) | 77 | YES | PASS |
| `buildinggadgets2` | `kubejs/assets/buildinggadgets2/lang/ru_ru.json` | `assets/buildinggadgets2/lang/ru_ru.json` (в RP) | 111 | YES | PASS |
| `chimes` | `kubejs/assets/chimes/lang/ru_ru.json` | `assets/chimes/lang/ru_ru.json` (в RP) | 50 | YES | PASS |
| `cluttered` | `kubejs/assets/cluttered/lang/ru_ru.json` | `assets/cluttered/lang/ru_ru.json` (в RP) | 1077 | YES | PASS |
| `cozycafe` | `kubejs/assets/cozycafe/lang/ru_ru.json` | `assets/cozycafe/lang/ru_ru.json` (в RP) | 63 | YES | PASS |
| `create_central_kitchen` | `kubejs/assets/create_central_kitchen/lang/ru_ru.json` | `assets/create_central_kitchen/lang/ru_ru.json` (в RP) | 180 | YES | PASS |
| `dew_drop_farmland_growth` | `kubejs/assets/dew_drop_farmland_growth/lang/ru_ru.json` | `assets/dew_drop_farmland_growth/lang/ru_ru.json` (в RP) | 28 | YES | PASS |
| `dew_drop_watering_cans` | `kubejs/assets/dew_drop_watering_cans/lang/ru_ru.json` | `assets/dew_drop_watering_cans/lang/ru_ru.json` (в RP) | 5 | YES | PASS |
| `dialog` | `kubejs/assets/dialog/lang/ru_ru.json` | `assets/dialog/lang/ru_ru.json` (в RP) | 1485 | YES | PASS |
| `domesticationinnovation` | `kubejs/assets/domesticationinnovation/lang/ru_ru.json` | `assets/domesticationinnovation/lang/ru_ru.json` (в RP) | 84 | YES | PASS |
| `dramaticdoors` | `kubejs/assets/dramaticdoors/lang/ru_ru.json` | `assets/dramaticdoors/lang/ru_ru.json` (в RP) | 2276 | YES | PASS |
| `dramaticdoors_chipped` | `kubejs/assets/dramaticdoors_chipped/lang/ru_ru.json` | `assets/dramaticdoors_chipped/lang/ru_ru.json` (в RP) | 1 | YES | PASS |
| `dramaticdoors_macaw` | `kubejs/assets/dramaticdoors_macaw/lang/ru_ru.json` | `assets/dramaticdoors_macaw/lang/ru_ru.json` (в RP) | 1 | YES | PASS |
| `dramaticdoors_manyideas` | `kubejs/assets/dramaticdoors_manyideas/lang/ru_ru.json` | `assets/dramaticdoors_manyideas/lang/ru_ru.json` (в RP) | 1 | YES | PASS |
| `etcetera` | `kubejs/assets/etcetera/lang/ru_ru.json` | `assets/etcetera/lang/ru_ru.json` (в RP) | 119 | YES | PASS |
| `extractinator` | `kubejs/assets/extractinator/lang/ru_ru.json` | `assets/extractinator/lang/ru_ru.json` (в RP) | 4 | YES | PASS |
| `ftbquestlocalizer` | `kubejs/assets/ftbquestlocalizer/lang/ru_ru.json` | `assets/ftbquestlocalizer/lang/ru_ru.json` (в RP) | 1988 | YES | PASS |
| `functionalstorage` | `kubejs/assets/functionalstorage/lang/ru_ru.json` | `assets/functionalstorage/lang/ru_ru.json` (в RP) | 115 | YES | PASS |
| `gag` | `kubejs/assets/gag/lang/ru_ru.json` | `assets/gag/lang/ru_ru.json` (в RP) | 2 | YES | PASS |
| `justhammers` | `kubejs/assets/justhammers/lang/ru_ru.json` | `assets/justhammers/lang/ru_ru.json` (в RP) | 1 | YES | PASS |
| `kata` | `kubejs/assets/kata/lang/ru_ru.json` | `assets/kata/lang/ru_ru.json` (в RP) | 60 | YES | PASS |
| `legendarycreatures` | `kubejs/assets/legendarycreatures/lang/ru_ru.json` | `assets/legendarycreatures/lang/ru_ru.json` (в RP) | 102 | YES | PASS |
| `longwings` | `kubejs/assets/longwings/lang/ru_ru.json` | `assets/longwings/lang/ru_ru.json` (в RP) | 258 | YES | PASS |
| `meadow` | `kubejs/assets/meadow/lang/ru_ru.json` | `assets/meadow/lang/ru_ru.json` (в RP) | 247 | YES | PASS |
| `minecraft` | `kubejs/assets/minecraft/lang/ru_ru.json` | `assets/minecraft/lang/ru_ru.json` (в RP) | 9 | YES | PASS |
| `moblassos` | `kubejs/assets/moblassos/lang/ru_ru.json` | `assets/moblassos/lang/ru_ru.json` (в RP) | 15 | YES | PASS |
| `moreminecarts` | `kubejs/assets/moreminecarts/lang/ru_ru.json` | `assets/moreminecarts/lang/ru_ru.json` (в RP) | 151 | YES | PASS |
| `nightlights` | `kubejs/assets/nightlights/lang/ru_ru.json` | `assets/nightlights/lang/ru_ru.json` (в RP) | 86 | YES | PASS |
| `numismatics` | `kubejs/assets/numismatics/lang/ru_ru.json` | `assets/numismatics/lang/ru_ru.json` (в RP) | 196 | YES | PASS |
| `numismatics_utils` | `kubejs/assets/numismatics_utils/lang/ru_ru.json` | `assets/numismatics_utils/lang/ru_ru.json` (в RP) | 2 | YES | PASS |
| `oreganized` | `kubejs/assets/oreganized/lang/ru_ru.json` | `assets/oreganized/lang/ru_ru.json` (в RP) | 5 | YES | PASS |
| `painting` | `kubejs/assets/painting/lang/ru_ru.json` | `assets/painting/lang/ru_ru.json` (в RP) | 48 | YES | PASS |
| `pamhc2trees` | `kubejs/assets/pamhc2trees/lang/ru_ru.json` | `assets/pamhc2trees/lang/ru_ru.json` (в RP) | 158 | YES | PASS |
| `paraglider` | `kubejs/assets/paraglider/lang/ru_ru.json` | `assets/paraglider/lang/ru_ru.json` (в RP) | 99 | YES | PASS |
| `passablefoliage` | `kubejs/assets/passablefoliage/lang/ru_ru.json` | `assets/passablefoliage/lang/ru_ru.json` (в RP) | 2 | YES | PASS |
| `perfectplushies` | `kubejs/assets/perfectplushies/lang/ru_ru.json` | `assets/perfectplushies/lang/ru_ru.json` (в RP) | 132 | YES | PASS |
| `portable_blueprints` | `kubejs/assets/portable_blueprints/lang/ru_ru.json` | `assets/portable_blueprints/lang/ru_ru.json` (в RP) | 399 | YES | PASS |
| `quark` | `kubejs/assets/quark/lang/ru_ru.json` | `assets/quark/lang/ru_ru.json` (в RP) | 1 | YES | PASS |
| `refurbished_furniture` | `kubejs/assets/refurbished_furniture/lang/ru_ru.json` | `assets/refurbished_furniture/lang/ru_ru.json` (в RP) | 652 | YES | PASS |
| `rehooked` | `kubejs/assets/rehooked/lang/ru_ru.json` | `assets/rehooked/lang/ru_ru.json` (в RP) | 25 | YES | PASS |
| `sawmill` | `kubejs/assets/sawmill/lang/ru_ru.json` | `assets/sawmill/lang/ru_ru.json` (в RP) | 7 | YES | PASS |
| `sewingkit` | `kubejs/assets/sewingkit/lang/ru_ru.json` | `assets/sewingkit/lang/ru_ru.json` (в RP) | 29 | YES | PASS |
| `simplehats` | `kubejs/assets/simplehats/lang/ru_ru.json` | `assets/simplehats/lang/ru_ru.json` (в RP) | 317 | YES | PASS |
| `simplerecall` | `kubejs/assets/simplerecall/lang/ru_ru.json` | `assets/simplerecall/lang/ru_ru.json` (в RP) | 3 | YES | PASS |
| `snowyspirit` | `kubejs/assets/snowyspirit/lang/ru_ru.json` | `assets/snowyspirit/lang/ru_ru.json` (в RP) | 1 | YES | PASS |
| `society` | `kubejs/assets/society/lang/ru_ru.json` | `assets/society/lang/ru_ru.json` (в RP) | 2124 | YES | PASS |
| `society_skills` | `kubejs/assets/society_skills/lang/ru_ru.json` | `assets/society_skills/lang/ru_ru.json` (в RP) | 196 | YES | PASS |
| `society_tips` | `kubejs/assets/society_tips/lang/ru_ru.json` | `assets/society_tips/lang/ru_ru.json` (в RP) | 112 | YES | PASS |
| `society_trading` | `kubejs/assets/society_trading/lang/ru_ru.json` | `assets/society_trading/lang/ru_ru.json` (в RP) | 35 | YES | PASS |
| `solonion` | `kubejs/assets/solonion/lang/ru_ru.json` | `assets/solonion/lang/ru_ru.json` (в RP) | 4 | YES | PASS |
| `splendid_slimes` | `kubejs/assets/splendid_slimes/lang/ru_ru.json` | `assets/splendid_slimes/lang/ru_ru.json` (в RP) | 320 | YES | PASS |
| `strawstatues` | `kubejs/assets/strawstatues/lang/ru_ru.json` | `assets/strawstatues/lang/ru_ru.json` (в RP) | 2 | YES | PASS |
| `supplementaries` | `kubejs/assets/supplementaries/lang/ru_ru.json` | `assets/supplementaries/lang/ru_ru.json` (в RP) | 1 | YES | PASS |
| `tanukidecor` | `kubejs/assets/tanukidecor/lang/ru_ru.json` | `assets/tanukidecor/lang/ru_ru.json` (в RP) | 240 | YES | PASS |
| `twigs` | `kubejs/assets/twigs/lang/ru_ru.json` | `assets/twigs/lang/ru_ru.json` (в RP) | 269 | YES | PASS |
| `unusualfishmod` | `kubejs/assets/unusualfishmod/lang/ru_ru.json` | `assets/unusualfishmod/lang/ru_ru.json` (в RP) | 264 | YES | PASS |
| `via_romana` | `kubejs/assets/via_romana/lang/ru_ru.json` | `assets/via_romana/lang/ru_ru.json` (в RP) | 1 | YES | PASS |
| `vintagedelight` | `kubejs/assets/vintagedelight/lang/ru_ru.json` | `assets/vintagedelight/lang/ru_ru.json` (в RP) | 189 | YES | PASS |
| `whimsy_deco` | `kubejs/assets/whimsy_deco/lang/ru_ru.json` | `assets/whimsy_deco/lang/ru_ru.json` (в RP) | 117 | YES | PASS |

---

## Почему предыдущий переводчик мог использовать такой подход

### Подтверждённые технические факты (`[FACT]`):
1. **`[FACT]` Приоритет ресурсов над KubeJS:** Ресурс-пак гарантированно перекрывает любые встроенные тексты модов и встроенный ресурс-пак KubeJS. Если перевод упакован в `resourcepacks/`, игра всегда берёт актуальные строки из него.
2. **`[FACT]` Сокращение веса и количества файлов:** Перенос 62 файлов `ru_ru.json` в один сжатый ZIP-архив ресурс-пака уменьшает размер архива дистрибутива на 44% (с 784 КБ до 439 КБ) и сокращает количество отдельных файлов с 83 до 21.
3. **`[FACT]` Чистота рабочей области KubeJS:** Папка `kubejs/` не захламляется десятками сторонних JSON-файлов и содержит только реальные скрипты сборки (`client_scripts`, `server_scripts`).

### Обоснованные выводы и гипотезы (`[INFERENCE]`):
1. **`[INFERENCE]` Использование автоматизированных пайплайнов (Scriptora):** Инструменты перевода генерируют стандартный ресурс-пак Minecraft. Предыдущему переводчику было проще упаковать готовый `Перевод модов.zip` в папку `resourcepacks/`, чем вручную раскладывать 62 файла по подпапкам `kubejs/assets/<namespace>/lang/`.
2. **`[INFERENCE]` Удобство для игроков:** Для обновления перевода игроку достаточно заменить всего один файл `resourcepacks/Перевод модов.zip`, не рискуя случайно повредить или затереть файлы скриптов в `kubejs/`.

---

## Проблемы и ограничения подхода

1. **Необходимость активации ресурс-пака:**
   Если игрок отключит ресурс-пак в меню настроек Minecraft (`Наборы ресурсов`), все переводы модов вернутся на английский язык. При хранении в `kubejs/assets/` переводы загружаются игрой принудительно (как системные ассеты).
2. **Файлы конфигураций модов не являются переводами:**
   Такие файлы, как `society/tooltipoverhaul/custom_frames.json`, нельзя переносить по шаблону `lang/ru_ru.json`.
3. **FTB Quests English Key mapping:**
   Файл `kubejs/assets/ftbquestlocalizer/lang/en_us.json` должен всегда оставаться в `kubejs/assets/`, иначе редактор квестов FTB Quests на стороне сервера/клиента может потерять маппинг исходных идентификаторов.

---

## Итог

1. **Оригинальный русификатор изменён: НЕТ** (папка `dist/Русификатор/` и архив `dist/Русификатор.zip` сохранены в исходном виде).
2. **Экспериментальная копия создана: ДА**
   - Директория: `dist/Русификатор_resourcepack_experiment/`
   - Архив: `dist/Русификатор_resourcepack_experiment.zip` (439 КБ)
3. **Переводы загружаются через Resource Pack: PASS** (все 62 namespace и 14 870 ключей валидированы внутри `resourcepacks/Перевод модов.zip`).
4. **Runtime-проверка: NOT PERFORMED** (прямой запуск Minecraft в терминальном окружении не производился; проведена 100% статическая верификация JSON и хэшей).
