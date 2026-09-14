# Отчёт по формированию дистрибутива русификатора (Society: Sunlit Valley)

> **Статус дистрибутива:** ✅ Сформирован и верифицирован  
> **Источник истины:** Установленная сборка `D:\ModrinthApp\profiles\Society_ Sunlit Valley`  
> **Исходный архив для сравнения:** `Scriptora_Society.Sunlit.Valley.4.0.4 (1).zip`  
> **Кодировка всех файлов:** UTF-8 (без BOM), валидный JSON и JS  

---

## 📊 Итоговая статистика

```text
Всего файлов в исходном архиве Scriptora:         268
Всего файлов в актуальном пакете русификатора:     160
  ├── Новых файлов (добавлены нами):               78
  ├── Изменённых файлов (глубоко доработаны):      5
  └── Неизменных файлов (из архива Scriptora):     77
Неиспользуемых файлов старого архива:              186
Служебных файлов разработчика (исключены):         1 (translateInspector.js)
```

---

## 📦 Расположение дистрибутива

- **Директория с готовой структурой:**  
  [`tasks/translate_to_zip/dist/Русификатор/`](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/tasks/translate_to_zip/dist/Русификатор)  
  [`dist/Русификатор/`](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/dist/Русификатор)
- **Готовый ZIP-архив для игроков:**  
  [`tasks/translate_to_zip/dist/Русификатор.zip`](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/tasks/translate_to_zip/dist/Русификатор.zip)  
  [`dist/Русификатор.zip`](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/dist/Русификатор.zip)

---

## 🗂 Структура пакета русификатора

```text
Русификатор/
├── kubejs/
│   ├── assets/
│   │   ├── <namespace>/lang/ru_ru.json                # 60 языковых файлов модов и квестов
│   │   ├── ftbquestlocalizer/lang/en_us.json          # Фоллбэк ключей FTB Quests
│   │   ├── society/textures/gui/community_center_*.png # Переведённые текстуры клуба (6 шт.)
│   │   └── society/tooltipoverhaul/custom_frames.json # Конфигурация рамок подсказок
│   ├── client_scripts/
│   │   ├── tooltips/                                  # 12 скриптов всплывающих подсказок [Shift]
│   │   │   ├── addTooltips.js                         # Основной сводный скрипт подсказок
│   │   │   ├── addAdvancedTooltips.js
│   │   │   ├── addFishTooltips.js
│   │   │   ├── addPriceTooltips.js
│   │   │   ├── bountifulTooltips.js
│   │   │   ├── buildinggadgets2Tooltips.js
│   │   │   ├── createCentralKitchenTooltips.js
│   │   │   ├── etceteraTooltips.js
│   │   │   ├── invitationTooltips.js
│   │   │   ├── longwingsTooltips.js
│   │   │   ├── tanukiDecorTooltips.js
│   │   │   └── unusualFishTooltips.js
│   │   ├── etceteraJei.js                             # Интеграция предметов Etcetera в JEI
│   │   └── universalGiftsJei.js                       # Вкладка универсальных подарков в JEI
│   └── server_scripts/
│       ├── globalServer.js                            # Фикс персистентности NBT, записок и уведомлений
│       ├── handleDebt.js                              # Фикс освобождения от долга банка/больницы
│       └── entities/
│           ├── slimeTicket.js                         # Обработка Билетов слайма
│           └── slimeInspectorEnhanced.js              # Анализатор слаймов в чате
├── patchouli_books/
│   └── fish_finder/ru_ru/                             # Книга рыболова: категории и 63 вида рыб
└── resourcepacks/
    └── Перевод модов.zip                              # Ресурспак базовых переводов модов
```

---

## 🔍 Детальный анализ изменений

### 1. Изменённые ключевые словари (5 файлов)

| Файл | Описание изменений |
| :--- | :--- |
| `kubejs/assets/ftbquestlocalizer/lang/ru_ru.json` | Полная вычитка всех квестов FTB Quests, страниц `{@pagebreak}`, цветовых кодов `&6` / `&a`, исправление битых ссылок и терминов. |
| `kubejs/assets/society/lang/ru_ru.json` | Основной словарь сборки: названия предметов, машин, удобрений, семян, наград, тултипов и интерфейсов. Приведён к стандартам единого глоссария. |
| `kubejs/assets/society_skills/lang/ru_ru.json` | Древо навыков Puffish Skills (меню `K`). Исправлено форматирование, экранированы знаки процента (`%%`) для предотвращения `Format Error`. |
| `kubejs/assets/society_tips/lang/ru_ru.json` | Игровые советы на экранах загрузки и в HUD. Исправлены формулировки и терминология. |
| `kubejs/assets/society_trading/lang/ru_ru.json` | Категории торговли и вывески магазинов деревенских жителей. |

---

### 2. Новые компоненты, добавленные в сборку (78 файлов)

#### А. Языковые файлы модов (57 файлов)
Полная локализация модов сборки:
- `dialog` (1477 ключей) — все диалоги NPC, приветствия, сезонные реплики и сюжетные ветки.
- `portable_blueprints` (399 ключей) — чертежи построек, домов и ферм.
- `dramaticdoors` (2276 ключей) — все высокие двери (высотой в 3 блока).
- `cluttered` (1062 ключа) — мебель и декорации.
- `refurbished_furniture` (652 ключа) — обновлённая мебель мистера Крайфиша.
- `longwings` (317 ключей) — бабочки, мотыльки, инкубаторы гусениц и банки для бабочек.
- `simplehats` (317 ключей) — коллекция косметических шляп.
- `splendid_slimes` (320 ключей) — породы слаймов, плорты и шляпки слаймов.
- `aquaculture` (279 ключей) — рыбы, удочки, снасти и филе.
- `twigs` (269 ключей) — декоративные блоки и ветви.
- `unusualfishmod` (264 ключа) — необычные рыбы и рецепты.
- `meadow` (247 ключей) — пастушество, сыроварение и шерсть.
- `tanukidecor` (234 ключа) — японские декорации Тануки.
- `vintagedelight` (189 ключей) — консервация, банки и соленья.
- `create_central_kitchen` (180 ключей) — интеграция Farmer's Delight и Create.
- `automobility` (161 ключ) — автомобили, детали и дорожные знаки.
- `pamhc2trees` (158 ключей) — плодовые деревья Pam's HarvestCraft 2.
- `moreminecarts` (156 ключей) — расширенные вагонетки и рельсы.
- `beachparty` (120 ключей) — пляжная мебель и напитки.
- `etcetera` (119 ключей) — механики, колокола, барабаны и декор.
- `functionalstorage` (115 ключей) — функциональные ящики и контроллеры.
- `buildinggadgets2` (111 ключей) — строительные гаджеты 2.
- `legendarycreatures` (102 ключа) — легендарные существа.
- `paraglider` (98 ключей) — парапланы и сосуды выносливости/сердец.
- `nightlights` (86 ключей) — ночники и гирлянды.
- `stardew_fishing` (85 ключей) — мини-игра рыбалки Stardew Valley.
- `bountiful` (77 ключей) — доска объявлений и контракты.
- `cozycafe` (63 ключа) — напитки и блюда уютного кафе.
- `chimes` (50 ключей) — колокольчики ветра.
- `painting` (48 ключей) — картины и холсты.
- `dew_drop_farmland_growth` (28 ключей) — механика роста от капель росы.
- `dew_drop_watering_cans` (5 ключей) — лейки Росы.
- `domesticationinnovation` (84 ключа) — ошейники и зачарования питомцев.
- `sawmill` (7 ключей) — лесопилка.
- `sewingkit` (29 ключей) — швейный набор.
- `snowyspirit` (1 ключ), `solonion` (4 ключа), `strawstatues` (2 ключа), `supplementaries` (1 ключ), `via_romana` (1 ключ), `whimsy_deco` (95 ключей).

#### Б. Клиентские скрипты KubeJS (Tooltips & JEI — 14 файлов)
- `kubejs/client_scripts/tooltips/addTooltips.js` — центральный реестр подсказок (предметы, семена, книги, бесконечная прочность).
- `kubejs/client_scripts/tooltips/bountifulTooltips.js` — подсказки по декретам и контрактам Bountiful.
- `kubejs/client_scripts/tooltips/buildinggadgets2Tooltips.js` — управление строительными гаджетами.
- `kubejs/client_scripts/tooltips/createCentralKitchenTooltips.js` — рецепты кастрюль и кухни Create.
- `kubejs/client_scripts/tooltips/etceteraTooltips.js` — описание механик колокольчиков и инструментов Etcetera.
- `kubejs/client_scripts/tooltips/invitationTooltips.js` — приглашения жителей и заселение.
- `kubejs/client_scripts/tooltips/longwingsTooltips.js` — руководство по разведению бабочек.
- `kubejs/client_scripts/tooltips/tanukiDecorTooltips.js` — японские декорации.
- `kubejs/client_scripts/tooltips/unusualFishTooltips.js` — наживки и условия ловли рыб.
- `kubejs/client_scripts/etceteraJei.js` — интеграция предметов Etcetera в JEI.
- `kubejs/client_scripts/universalGiftsJei.js` — вкладка универсальных подарков в JEI.

#### В. Серверные скрипты с фиксами механик (5 файлов)
- `kubejs/server_scripts/globalServer.js` — персистентность данных при смерти в `server.persistentData`, фикс NBT записок Candlelight (`global.getNotePaperItem`), уведомления в чат и HUD.
- `kubejs/server_scripts/handleDebt.js` — фикс справок об освобождении от долга банка/больницы.
- `kubejs/server_scripts/entities/slimeTicket.js` — механика Билетов слайма.
- `kubejs/server_scripts/entities/slimeInspectorEnhanced.js` — интерактивный анализатор слаймов.

---

## 🛠 Инструкция по установке для игроков

1. Скачайте архив [`Русификатор.zip`](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/tasks/translate_to_zip/dist/Русификатор.zip).
2. Откройте папку вашего профиля с установленным модпаком **Society: Sunlit Valley** (в CurseForge / Modrinth App / Prism Launcher).
3. Скопируйте содержимое папки `Русификатор` (папки `kubejs`, `patchouli_books`, `resourcepacks`) в корень профиля игры с подтверждением замены файлов.
4. Запустите Minecraft.
5. В меню игры:
   - В разделе **Настройки $ightarrow$ Пакеты ресурсов** убедитесь, что ресурспак `Перевод модов` включён (находится в правом столбце).
   - В игре нажмите **`F3 + T`** для перезагрузки текстур и языковых файлов.
   - Выполните команду **`/ftbquests reload`** в чате для обновления квестов.
