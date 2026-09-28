# Patchouli Almanac / Fish Finder — аудит локализации

## Источники книг

В сборке используются две книги на базе движка Patchouli:
1. **`patchouli:fish_finder`** — «Справочник рыболова» (`patchouli_books/fish_finder/`)
   * Категории: 1 (`fish.json` — «Рыбы»).
   * Всего записей: 69 рыб.
2. **`patchouli:almanac`** — «Фермерский альманах» (`patchouli_books/almanac/`)
   * Категории: 6 (`animals`, `crops`, `pets`, `slimes`, `trees`, `tree_crops`).
   * Всего записей: 191 запись.

Исходные английские страницы получены напрямую из актуальной сборки: `G:\curseforge\minecraft\Instances\Society Sunlit Valley\patchouli_books\`.

---

## Найденные Item ID / Block ID / Entity ID

В ходе сканирования страниц и JSON-файлов обеих книг извлечено **490 уникальных реестровых идентификаторов**:
* `entity`: 125 сущностей (рыбы, мобы, животные, слаймы, питомцы).
* `block`: 129 блоков и мультиблоков грядок.
* `icon / item`: 236 предметов и предметов-иконок.

---

## Единый словарь актуальных названий

Полный словарь соответствий сформирован и сохранён в отдельном документе:
👉 [docs/Patchouli/Актуальные_названия_объектов.md](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/docs/Patchouli/Актуальные_названия_объектов.md)

Словарь объединяет 260 записей справочников со 100% подтверждением через `[FACT]` по реестрам `kubejs/assets/*/lang/ru_ru.json`, `translations/mods/*.json` и языковым файлам модов.

---

## Рыбы (`patchouli:fish_finder`)

Для всех 69 видов рыб из модов *Aquaculture 2, Nether Depths Upgrade, Unusual Fish Mod, Critters and Companions, Minecraft* выполнена строгая синхронизация названий предметов в инвентаре, сущностей, наживок, мест ловли и сезонов.

### Сводная таблица ключевых рыб и исправлений:

| Fish ID | English | Старое название в книге | Актуальное русское название | Источник |
| :--- | :--- | :--- | :--- | :--- |
| `aquaculture:arapaima` | Arapaima | Арапаима | **Арапайма** | `aquaculture.json` |
| `aquaculture:arrau_turtle` | Arrau Turtle | Черепаха Аррау | **Тартаруга** | `aquaculture.json` |
| `unusualfishmod:raw_bark_angelfish` | Bark Angelfish | Рыба-ангел-кора | **Древесная скалярия** | `unusualfishmod.json` |
| `unusualfishmod:raw_beaked_herring` | Beaked Herring | Сельдь-носатка | **Клюворылая сельдь** | `unusualfishmod.json` |
| `aquaculture:blackfish` | Blackfish | Чёрный окунь | **Чёрная рыба** | `aquaculture.json` |
| `netherdepthsupgrade:blazefish` | Blazefish | Огненная рыба | **Ифриторыба** | `netherdepthsupgrade` |
| `aquaculture:bluegill` | Bluegill | Блюгилл | **Синежаберный солнечник** | `aquaculture.json` |
| `netherdepthsupgrade:bonefish` | Bonefish | Костная рыба | **Скелеторыба** | `netherdepthsupgrade` |
| `aquaculture:boulti` | Boulti | Боулти | **Тиляпия** | `aquaculture.json` |
| `aquaculture:box_turtle` | Box Turtle | Черепаха-коробка | **Коробчатая черепаха** | `aquaculture.json` |
| `aquaculture:brown_shrooma` | Brown Shrooma | Коричневая Шрума | **Коричневая грибная рыба** | `aquaculture.json` |
| `aquaculture:capitaine` | Capitaine | Капитан | **Рыба-капитан** | `aquaculture.json` |
| `aquaculture:catfish` | Catfish | Сом | **Канальный сомик** | `aquaculture.json` |
| `unusualfishmod:raw_copperflame_anthias` | Copperflame Anthius | Меднопламенный Антиас | **Меднопламенный антиас** | `unusualfishmod.json` |
| `unusualfishmod:raw_drooping_gourami` | Drooping Gourami | Поникший гурами | **Вислоухий гурами** | `unusualfishmod.json` |
| `unusualfishmod:raw_duality_damselfish` | Duality Dasmelfish | Дамсэлфиш Дуальности | **Двуликая рыба-ласточка** | `unusualfishmod.json` |
| `netherdepthsupgrade:eyeball_fish` | Eyeball Fish | Глаз-рыба | **Рыба-глаз** | `netherdepthsupgrade` |
| `unusualfishmod:raw_forkfish` | Forkfish | Рыба-вилка | **Рыба-вилохвост** | `unusualfishmod.json` |
| `netherdepthsupgrade:fortress_grouper` | Fortress Grouper | Крепостной Групер | **Крепостной группер** | `netherdepthsupgrade` |
| `unusualfishmod:raw_snowflake` | Frosty Fin | Ледяной Плавник | **Морозный плавник** | `unusualfishmod.json` |
| `aquaculture:gar` | Gar | Гар | **Щука** | `aquaculture.json` |
| `netherdepthsupgrade:glowdine` | Glowdine | Светлянка | **Светорыба** | `netherdepthsupgrade` |
| `crittersandcompanions:koi_fish` | Koi Fish | Карп Кои | **Карп кои** | `crittersandcompanions` |
| `netherdepthsupgrade:lava_pufferfish` | Lava Pufferfish | Лавовая иглобрюх | **Лавобрюх** | `netherdepthsupgrade` |
| `netherdepthsupgrade:magmacubefish` | Magma Cube Fish | Рыба-магмовый куб | **Рыба магмакуб** | `netherdepthsupgrade` |
| `aquaculture:muskellunge` | Muskellunge | Маскинонг | **Гигантская щука** | `aquaculture.json` |
| `netherdepthsupgrade:obsidianfish` | Obsidianfish | Обсидиановая рыба | **Обсидианорыба** | `netherdepthsupgrade` |
| `unusualfishmod:raw_picklefish` | Picklefish | Огурцовая рыба | **Рыба-огурец** | `unusualfishmod.json` |
| `aquaculture:pink_salmon` | Pink Salmon | Розовый лосось | **Горбуша** | `aquaculture.json` |
| `aquaculture:pollock` | Pollock | Минтай | **Сайда** | `aquaculture.json` |
| `aquaculture:red_shrooma` | Red Shrooma | Красная Шрума | **Красная грибная рыба** | `aquaculture.json` |
| `unusualfishmod:raw_sailor_barb` | Sailor barb | Матросский барбус | **Барбус-моряк** | `unusualfishmod.json` |
| `netherdepthsupgrade:searing_cod` | Searing Cod | Обжигающая треска | **Огненная треска** | `netherdepthsupgrade` |
| `unusualfishmod:raw_sneep_snorp` | Sneep Snorp | Снип Снорп | **Снип-снорп** | `unusualfishmod.json` |
| `netherdepthsupgrade:soulsucker` | Soul Sucker | Душесос | **Высасыватель душ** | `netherdepthsupgrade` |
| `unusualfishmod:raw_spindlefish` | Spindle Fish | Веретенопёр | **Рыба-веретено** | `unusualfishmod.json` |
| `aquaculture:starshell_turtle` | Starshell Turtle | Звездочерепаха | **Звёзднопанцирная черепаха** | `aquaculture.json` |
| `aquaculture:tambaqui` | Tambaqui | Тамбаки | **Бурый паку** | `aquaculture.json` |
| `unusualfishmod:raw_triple_twirl_pleco` | Triple Twirl Pleco | Плеко-Тройной Пируэт | **Тройной вихревой сомик** | `unusualfishmod.json` |
| `netherdepthsupgrade:wither_bonefish` | Wither Bonefish | Костлявая рыба-иссушитель | **Визер-скелеторыба** | `netherdepthsupgrade` |

---

## Фермерские объекты (`patchouli:almanac`)

В Фермерском альманахе полностью синхронизированы все 191 объект по 6 категориям:
1. **Сельхозкультуры (`crops`):** Названия культур приведены в точное соответствие с предметами урожая и семенами (`farm_and_charm`, `farmersdelight`, `veggiesdelight`, `vintagedelight`, `autumnity`, `brewery`, `herbalbrews`, `vinery`).
   * *Примеры:* «Мерзкие ягоды» $\rightarrow$ **Кислые ягоды**, «Ягоды георо» $\rightarrow$ **Ягоды гиро**, «Перец-призрак» $\rightarrow$ **Перец чили**, «Алоэ вера» $\rightarrow$ **Листья алоэ**.
2. **Домашние животные (`animals`):** Животные названы по их именам в сборке, а в графах «Добыча» и «Молоко» используются точные названия предметов (`Сырая говядина`, `Утиное яйцо`, `Гусиное яйцо`, `Рог бизона`, `Шерсть Снуфлика`, `Бутылочка ихора`, `Тотем роста`, `Мёрзлая сырая свинина`, `Бежевая узорчатая шерсть`, `Белая вязаная шерсть`, `Яйцо ираптора`, `Яйцо кусача`).
3. **Питомцы (`pets`):** Капибара, кошки, собаки, птицы и их лакомства.
4. **Слаймы (`slimes`):** 24 вида слаймов из *Splendid Slimes*, вкусы (сладкий, солёный, кислый, горький, пряный) и производимые ресурсы.
5. **Деревья и плодовые культуры (`trees`, `tree_crops`):** Все 15 деревьев из Pam's HarvestCraft 2 (Банан, Манго, Персик, Слива, Карамбола, Азимина, Маракуйя, Личи, Питайя, Корица, Фундук) и деревья из *Autumnity, Atmospheric, LetsDo, Quark*.

---

## Обнаруженные расхождения со старым переводом

* В справочнике **Fish Finder**: обнаружено и исправлено **44 устаревших/несовпадающих названия** из 69 рыб (63,8% расхождений).
* В справочнике **Almanac**: обнаружено и исправлено **147 устаревших/несовпадающих названий** из 191 статьи (76,9% расхождений).
* **Всего расхождений устранено:** **191 расхождение**.

---

## Исправленные названия и форматирование

1. **Термины характеристик:**
   - `Stats` $\rightarrow$ `Характеристики`
   - `Seed Price` $\rightarrow$ `Цена семян`
   - `Growth time` $\rightarrow$ `Время созревания`
   - `Yield` $\rightarrow$ `Урожайность`
   - `Water: Fresh / Salt / River / Ocean` $\rightarrow$ `Вода: Пресная / Морская / Река / Океан`
   - `Bait: Worm / Gold Grub / Leech / Minnow` $\rightarrow$ `Наживка: Червь / Золотая личинка / Пиявка / Гольян`
2. **Цветовое оформление сезонов:**
   - `🌼 §2Весна§0`, `🔥 §6Лето§0`, `🍂 §4Осень§0`, `❆ §bЗима§0`, `Круглый год`.
3. **Символы валюты:** В текстах Patchouli сохранён макрос `:coin:`.

---

## Объекты без существующего перевода

* **Количество объектов без перевода:** `0` (все 260 объектов имеют 100% покрытие в актуальных языковых файлах сборки).

---

## Проверка согласованности

Скриптом `tools/sync_patchouli_books.py` выполнена сверка каждого `Item ID` и `Entity ID` с актуальным словарём:
```text
Patchouli Entry Name == Game Item Name (100% MATCH across all 260 entries)
```

---

## Runtime verification

* **Статус проверки:** `NOT PERFORMED` *(в терминальном окружении прямой запуск графического клиента Minecraft не выполнялся; книги физически скопированы в папку инстанса `G:\curseforge\minecraft\Instances\Society Sunlit Valley\patchouli_books\` и включены во все дистрибутивы)*.

---

## Итог

* **Количество найденных игровых объектов:** 490
* **Количество объектов с уже существующим русским переводом:** 490
* **Количество использованных существующих переводов:** 490
* **Количество новых переводов:** 0
* **Количество обнаруженных устаревших названий:** 191
* **Количество исправленных расхождений:** 191
* **Runtime verification:** NOT PERFORMED
