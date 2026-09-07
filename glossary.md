# Глобальный глоссарий терминов и предметов — Society: Sunlit Valley

Единый справочник терминологилогии для согласованной локализации всех компонентов сборки:
* FTB Quests (`ftbquests`)
* Тултипы и предметы (`society`, `society_tips`)
* Древо навыков Puffish Skills (`society_skills`)
* Диалоги жителей (`dialog`)
* Портативные чертежи (`portable_blueprints`)
* Кастомный JEI и скрипты KubeJS

---

## 1. Символы и макросы

| Символ / Код | Описание | Область применения |
| :--- | :--- | :--- |
| `§e●` (`U+25CF`) | Золотая монета | Чат, HUD, всплывающие подсказки, записки |
| `:coin:` | Макрос монеты | **Исключительно** в книгах Patchouli |
| `@i`, `%%`, `:tag:` | Технические плейсхолдеры | **Не изменять и не удалять** |
| `{@pagebreak}` | Разделитель страниц | Квесты FTB Quests |

---

## 2. Персонажи и профессии (строго без феминитивов)

| Английский (EN) | Русский (RU) | ID / Контекст | Роль в игре |
| :--- | :--- | :--- | :--- |
| **Blacksmith** | **&6Кузнец&r** | `society:blacksmith` | Открывает/продает жеоды, инструменты |
| **Librarian** | **&6Библиотекарь&r** | `society:librarian` | Житель Вероника (Veronica), книги и свитки |
| **Veronica** | **Вероника** | NPC | Имя Библиотекаря |
| **Banker** | **&6Банкир&r** | `society:banker` | Финансы, хранилище, валюта |
| **Market** | **&6Торговец с Рынка&r** | `society:market` | Семена, саженцы, базовые продукты |
| **Fisher** | **&6Рыбак&r** | `society:fisher` | Снасти, наживки, рыбалка |
| **Carpenter** | **&6Плотник&r** | `society:carpenter` | Чертежи, постройки, мебель |
| **Shepherd** | **&6Пастух&r** | `society:shepherd` | Животноводство, корма, шерсть |
| **Barkeeper** | **&6Бармен&r** | `society:barkeeper` | Таверна, напитки, слухи |
| **Witch / Herbalist** | **&6Ведьма / Травница&r** | `society:witch` | Житель Эвелин (Evelyne), травы, зелья |
| **Evelyne** | **Эвелин** | NPC | Имя Ведьмы |
| **Trader** | **&6Странствующий торговец&r** | `society:trader` | Житель Карлос (Carlos), редкие товары |
| **Carlos** | **Карлос** | NPC | Имя Торговца |
| **Wise Oak** | **&6Мудрый Дуб&r** | `society:wise_oak` | Древний NPC в лесу |

---

## 3. Ключевые предметы и механизмы сборки

| Английский (EN) | Русский (RU) | ID предмета / блока | Назначение / Механика |
| :--- | :--- | :--- | :--- |
| **&6Greenhouse Glass&r** | **&6Тепличное стекло&r** | `society:greenhouse_glass` | Игнорирование сезонов (радиус 16 блоков) |
| **&6Crystals of Regret&r** | **&6Кристаллы сожаления&r** | `society:crystal_of_regret_*` | Сброс очков в древе навыков (K) |
| **Red Wrench** | **Красный гаечный ключ** | `society:red_wrench` | Настройка механизмов |
| **Ancient Builder's Tool** | **Древний инструмент строителя** | `society:ancient_builders_tool` | Создание фермерских чертежей |
| **Drum Cornucopia** | **Барабан изобилия** | `society:drum_cornucopia` | Автосбор урожая в 7:00 |
| **Fish Pond** | **Рыбный пруд** | `society:fish_pond` | Разведение рыбы |
| **Fish Pond Basket** | **Корзина для рыбного пруда** | `society:fish_pond_basket` | Автосбор продуктов из прудов |
| **Fish Pond Manager** | **Менеджер рыбного пруда** | `society:fish_pond_manager` | Автосдача квестов прудов в 7:00 |
| **&6Caterpillar Box&r** | **&6Инкубатор для гусениц&r** | `society:caterpillar_box` | Выведение бабочек и мотыльков |
| **&6Caterpillar Eggs&r** | **&6Яйца гусениц&r** | `longwings:*` | Яйца для разведения |
| **&6Diamond Heart&r** | **&bАлмазное сердце&r** | `quark:diamond_heart` | Навыки животноводства (Пересадка, Биомант), мана Botania |
| **Artisan Cheese Press** | **Ремесленный пресс для сыра** | `society:cheese_press` | Производит сыр за 2 дня (6:00 AM) с сохранением качества |
| **Auto-Cheese Press (Cheese Form)** | **Автоматический пресс для сыра** | `meadow:cheese_form` | Автоматический станок за 90 сек со сбросом качества (требует сычуг) |
| **Crystalarium** | **Кристалляриум** | `society:crystalarium` | Дублирует самоцветы и минералы |
| **Golden Clock** | **Золотые часы** | `society:golden_clock` | Ускоряет работу станков в зоне 5x5x5 на +1 день в 7:00 |
| **Fairy Dust** | **Пыльца фей** | `society:fairy_dust` | ПКМ по станку: мгновенно ускоряет процесс на 1 день |
| **Willow Sapling** | **Саженец ивы** | `cluttered:willow_sapling` | Покупка на Рынке после открытия Мастерства фермерства |
| **Willow Log** | **Ивовое бревно** | `cluttered:willow_log` | Древесина ивы; база для установки Подсочника |
| **Grimwood Sapling** | **Саженец мрачного дерева** | `atmospheric:grimwood_sapling` | Дроп 0.5% при сборе созревших культур с Мастерством фермерства |
| **Mystic Syrup** | **Мистический сироп** | `society:mystic_syrup` | Добывается Подсочником с ивы с листвой за 7 дней |
| **Tapper** | **Подсочник** | `society:tapper` | Станок для сбора смолы и сиропа с деревьев |
| **Auto-Tapper** | **Автоматический подсочник** | `society:auto_tapper` | Автоматический станок для сбора жидкостей с деревьев с откачкой снизу |
| **Iron / Gold / Diamond / Netherite Sprinkler** | **Железный / Золотой / Алмазный / Незеритовый спринклер** | `dew_drop_farmland_growth:*_sprinkler` | Автополив посевов в 6:00 утра (области 3x3, 5x5, 7x7, 9x9) |
| **Fertilizers (Speed / Hydrating / Quality / Bountiful)** | **Удобрения (Скорости / Увлажнения / Качества / Обильные)** | `dew_drop_farmland_growth:*_fertilizer` | Сельскохозяйственные удобрения для грядок и пашни |
| **Garden Pot** | **Садовый горшок** | `dew_drop_farmland_growth:garden_pot` | Выращивание культур в помещении в любой сезон |

---

## 4. Жеоды, раскалывание и тайники

| Английский (EN) | Русский (RU) | ID предмета |
| :--- | :--- | :--- |
| **&6Geode&r** | **&6Жеода&r** | `society:geode` |
| **&6Frozen Geode&r** | **&6Замёрзшая жеода&r** | `society:frozen_geode` |
| **&6Magma Geode&r** | **&6Магматическая жеода&r** | `society:magma_geode` |
| **&6Omni Geode&r** | **&6Омни-жеода&r** | `society:omni_geode` |
| **&6Geode Buster&r** | **&6Молот для жеод&r** | `society:geode_buster` |
| **&6Extractinator&r** | **&6Раскалыватель жеод&r** | `extractinator:extractinator` |
| **&6Relic Trove&r** | **&6Тайник с магическими реликвиями&r** | `society:relic_trove` |
| **&6Artifact Trove&r** | **&6Тайник с сокровищами&r** | `society:artifact_trove` |

---

## 5. Уютное кафе (Cozy Cafe)

| Английский (EN) | Русский (RU) | ID / Тег |
| :--- | :--- | :--- |
| **Cozy Cafe** | **«Уютное кафе»** | `itemGroup.cozycafe` |
| **&6Cafe Manager&r** | **&6Менеджер кафе&r** | `block.cozycafe.cafe_manager` |
| **&6Plating Station&r** | **&6Станция сервировки&r** | `block.cozycafe.plating_station` |
| **&6Serving Plate&r** | **&6Сервировочная тарелка&r** | `item.cozycafe.serving_plate` |
| **Dirty Serving Plate** | **Грязная сервировочная тарелка** | `item.cozycafe.dirty_serving_plate` |
| **Cafe Menu** | **Меню кафе** | `block.cozycafe.cafe_menu` |
| **Cafe Sign** | **Вывеска кафе** | `block.cozycafe.cafe_sign` |
| **Plated [Dish]** | **Сервированное [Блюдо]** | `item.cozycafe.serving_plate.served` |
| **Customer** | **Посетитель** | `entity.cozycafe.customer` |

---

## 6. Качество предметов (Quality Food / Crops)

| Английский (EN) | Русский (RU) | Цветовой код |
| :--- | :--- | :--- |
| **Iron Quality** | **Железное качество** | `&7Железное&r` |
| **Gold Quality** | **Золотое качество** | `&6Золотое&r` |
| **Diamond Quality** | **Алмазное качество** | `&bАлмазное&r` |
| **Iridium Quality** | **Иридиевое качество** | `&dИридиевое&r` |

---

## 7. Времена года и события (Serene Seasons)

| Английский (EN) | Русский (RU) | Период |
| :--- | :--- | :--- |
| **Spring / Summer / Autumn / Winter** | **Весна / Лето / Осень / Зима** | Сезоны (по 30 дней) |
| **Early / Mid / Late [Season]** | **Ранний / Средний / Поздний [Сезон]** | Подсезоны (по 10 дней) |
| **&6Book fair&r / &6Book Fair&r** | **&6Ярмарка книг&r** | Поздний подсезон (21–30 дни) |

---

## 8. Интерфейс, кнопки и управление

| Английский (EN) | Русский (RU) | Значение |
| :--- | :--- | :--- |
| **Understood!** | **Понятно!** | Завершение квеста-гайда |
| **Shift + Right Click** | **Shift + ПКМ** | Комбинация управления |
| **Right Click** | **ПКМ** | Правая кнопка мыши |
| **Left Click** | **ЛКМ** | Левая кнопка мыши |
| **Offhand** | **Вторая рука** | Слот щита/тотема/наживки |
| **Hotbar** | **Панель быстрого доступа** | 9 основных слотов инвентаря |
| **Tooltip** | **Всплывающая подсказка** | Текст при наведении курсора |
| **Bundles** | **Наборы / Узелки** | Квесты сдачи ресурсов |

---

## 9. Музыка ветра и колокольчики (Chimes)

| Английский (EN) | Русский (RU) | ID предмета / блока |
| :--- | :--- | :--- |
| **Bamboo Wind Chime** | **Японский стеклянный колокольчик (Бамбуковый Фурин)** | `block.chimes.bamboo_chimes` |
| **Carved Bamboo Wind Chime** | **Японский стеклянный колокольчик (Резной Бамбуковый Фурин)** | `block.chimes.carved_bamboo_chimes` |
| **Iron Wind Chime** | **Японский стеклянный колокольчик (Железный Фурин)** | `block.chimes.iron_chimes` |
| **Copper Wind Chime** | **Японский стеклянный колокольчик (Медный Фурин)** | `block.chimes.copper_chimes` |
| **Amethyst Wind Chime** | **Японский стеклянный колокольчик (Аметистовый Фурин)** | `block.chimes.amethyst_chimes` |
| **Glass Wind Bell** | **Японский стеклянный колокольчик (Стеклянный Фурин)** | `block.chimes.glass_bells` |
| **Customizable Wind Bell** | **Японский стеклянный колокольчик (Настраиваемый Фурин)** | `item.glass_wind_bell.customizable` |
| **Windsail** | **Язычок (ветровой вымпел)** | `block.glass_wind_bell.*.tag` |
| **Base** | **Основание (купол)** | `block.glass_wind_bell.*.base` |

---

## 10. Железные дороги и логистика (More Minecarts)

| Английский (EN) | Русский (RU) | ID предмета / блока |
| :--- | :--- | :--- |
| **Vitric Cactus / Glass Cactus** | **Кристаллический кактус** | `block.moreminecarts.glass_cactus` |
| **Glass Spines** | **Стеклянные шипы** | `item.moreminecarts.glass_spines` |
| **Chunk Loader** | **Топливный прогрузчик чанков** | `block.moreminecarts.chunk_loader` |
| **Minecart with Chunk Loader** | **Вагонетка с прогрузчиком чанков** | `item.moreminecarts.minecart_with_chunk_loader` |
| **Maglev Rail** | **Маглев-рельс** | `block.moreminecarts.maglev_rail` |
| **Powered Maglev Rail** | **Энергорельс маглева** | `block.moreminecarts.maglev_powered_rail` |
| **Lightspeed Rail** | **Светоскоростной рельс** | `block.moreminecarts.lightspeed_rail` |
| **Turbo Rail** | **Турбо-рельс** | `block.moreminecarts.lightspeed_powered_rail` |
| **Mob Spring / Coupler** | **Пружинная сцепка** | `item.moreminecarts.coupler` |
| **Aerodynamic Minecart Upgrade Kit** | **Аэродинамический комплект улучшения** | `item.moreminecarts.high_speed_upgrade` |
| **Silica Steel** | **Кремневая сталь / Слиток кремневой стали** | `item.moreminecarts.silica_steel` |
| **Chunkrodite** | **Чанкродит** | `item.moreminecarts.chunkrodite` |
| **Ender Pearl Stasis Chamber** | **Стазис-камера жемчуга Края** | `block.moreminecarts.pearl_stasis_chamber` |
| **Holo-Scaffold Generator** | **Генератор голографических лесов** | `block.moreminecarts.holo_scaffold_generator` |

---

## 11. Ночники и светящийся декор (Night Lights)

| Английский (EN) | Русский (RU) | ID предмета / блока |
| :--- | :--- | :--- |
| **Night Lights** | **«Ночники и светильники»** | `itemGroup.nightlights.nightlights` |
| **Frog Night Light** | **Лягушачий ночник** | `block.nightlights.frog_*` |
| **Mushroom Night Light** | **Грибной ночник** | `block.nightlights.mushroom_*` |
| **Octopus Night Light** | **Ночник-осьминог** | `block.nightlights.octopus_*` |
| **Hanging Lights** | **Подвесные светильники** | `block.nightlights.hanging_lights_*` |
| **Fairy Lights** | **Волшебная гирлянда** | `block.nightlights.fairy_lights_*` |

---

## 12. Слаймоводство (Splendid Slimes)

| Английский (EN) | Русский (RU) | ID предмета / блока |
| :--- | :--- | :--- |
| **Splendid Slimes** | **«Великолепные слаймы»** | `itemGroup.splendid_slimes` |
| **Plort** | **Плорт** | `item.splendid_slimes.*_plort` |
| **Largo** | **Ларго** | `entity.splendid_slimes.largo_splendid_slime` |
| **Tarr** | **Варр** | `entity.splendid_slimes.tarr` |
| **Slime Vac** | **Вакуумный сборщик (Слаймопушка)** | `item.splendid_slimes.slime_vac` |
| **Slime Incubator** | **Инкубатор слаймов** | `block.splendid_slimes.slime_incubator` |
| **Plort Press** | **Пресс плортов** | `block.splendid_slimes.plort_press` |
| **Plort Rippit** | **Переработчик плортов** | `block.splendid_slimes.plort_rippit` |
| **Slime Feeder** | **Кормушка для слаймов** | `block.splendid_slimes.slime_feeder` |
| **Slime Inspector** | **Анализатор слаймов** | `item.splendid_slimes.slime_inspector` |
| **Slime Heart** | **Сердце слайма** | `item.splendid_slimes.*_slime_heart` |
| **Corral Block** | **Блок загона для слаймов** | `block.splendid_slimes.corral_block` |
| **Rocket Pod** | **Капсула для реактивного прыжка** | `item.splendid_slimes.rocket_pod` |

### Утверждённые породы слаймов (24 вида):
* **Всевидящий Слайм** (`all_seeing`), **Барни Слайм** (`bear`), **Редстоун Слайм** (`bitwise`), **Ифритовый Слайм** (`blazing`), **Костяной Слайм** (`bony`), **Кот-Бум Слайм** (`boomcat`), **Песчаный Слайм** (`dusty`), **Эндер Слайм** (`ender`), **Золото-рудный Слайм** (`gold`), **Джусик Слайм** (`juicy`), **Светящийся Слайм** (`luminous`), **Криэйт Слайм** (`mechanic`), **Дракон Слайм** (`minty`), **Экспертикус Слайм** (`orby`), **Фантом Слайм** (`phantom`), **Призмариновый Слайм** (`prisma`), **Бездноглаз Слайм** (`puddle`), **Гниющий Слайм** (`rotting`), **Шалкерный Слайм** (`shulking`), **Розовый слайм** (`slimy`), **Искро-Кот Слайм** (`sparkcat`), **Карамельный Слайм** (`sweet`), **Паучок Слайм** (`webby`), **Плакса Слайм** (`weeping`).

---

## 13. Винтажная кулинария (Vintage Delight)

| Английский (EN) | Русский (RU) | ID предмета / блока | Назначение / Механика |
| :--- | :--- | :--- | :--- |
| **Fermenting Jar** | **Банка для брожения** | `block.vintagedelight.fermenting_jar` | Ферментация, маринование и квашение |
| **Cheese Mold** | **Форма для сыра** | `block.vintagedelight.cheese_mold` | Прессование творожных сгустков в сыр |
| **Cheese Wheel** | **Головка сыра** | `block.vintagedelight.cheese_wheel` | Разрезаемый блок сыра (на ломтики) |
| **Evaporator** | **Выпариватель** | `block.vintagedelight.evaporator` | Ускоренное выпаривание соли из воды |
| **Salt Dust** | **Соль** | `item.vintagedelight.salt_dust` | Базовая приправа для консервации |
| **Ghost Pepper** | **Перец чили** | `item.vintagedelight.ghost_pepper` | Острое растение, даёт эффект горения/тепла |
| **Magic Vine** | **Волшебная лоза** | `block.vintagedelight.magic_vine` | Декоративная древесная лоза |
| **Century Egg** | **Столетнее яйцо** | `item.vintagedelight.century_egg` | Ферментированный деликатес |
| **Organic Mash** | **Органическая масса** | `item.vintagedelight.organic_mash` | Удобрение и сырьё для компоста |
| **Surströmming** | **Сюрстрёмминг** | `item.vintagedelight.surstromming` | Квашеная рыба с резким эффектом |

---

## 14. Уютный декор и мебель (Cluttered)

| Английский (EN) | Русский (RU) | ID предмета / блока | Назначение / Механика |
| :--- | :--- | :--- | :--- |
| **Hand Drill** | **Ручная дрель** | `item.cluttered.hand_drill` | ПКМ переключает вариацию блока; Shift + ПКМ вращает блок |
| **Bouncy Mushroom** | **Прыгучий гриб** | `block.cluttered.luphie_bouncy_mushroom` | Полностью гасит урон от падения и подбрасывает сущности вверх |
| **Glowing Bouncy Mushroom** | **Светящийся прыгучий гриб** | `block.cluttered.luphie_glowing_bouncy_mushroom` | Батутный блок с источником света |
| **Eye Block** | **Смотрящий блок** | `block.cluttered.luphie_eye_block` | Декоративный блок с живым глазом, следящим за игроком |
| **Sewing Machine** | **Швейная машинка** | `block.cluttered.luphie_sewing_machine` | Винтажный декоративный блок |
| **Retro Radio** | **Ретро-радиоприёмник** | `block.cluttered.luphie_retro_radio` | Винтажный декоративный приёмник |
| **Polaroid Camera** | **Камера Polaroid** | `item.cluttered.luphie_polaroid_camera` | Декоративный фотоаппарат |
| **Willow Wood** | **Ивовая древесина** | `block.cluttered.willow_*` | Полный набор строительных и декоративных блоков ивы |
| **Flowering Willow** | **Цветущая ива** | `block.cluttered.flowering_willow_*` | Декоративная цветущая древесина и листья |

---

## 15. Современная мебель и техника (Refurbished Furniture)

| Английский (EN) | Русский (RU) | ID предмета / блока | Назначение / Механика |
| :--- | :--- | :--- | :--- |
| **Electricity Generator** | **Генератор электричества** | `block.refurbished_furniture.*_electricity_generator` | Источник энергии для бытовой техники (радиус сети до 16 блоков) |
| **Light Switch** | **Выключатель света** | `block.refurbished_furniture.*_lightswitch` | Управление группами связанных светильников (через Wrench) |
| **Ceiling Fan** | **Потолочный вентилятор** | `block.refurbished_furniture.*_ceiling_fan` | Вращающийся вентилятор; наносит урон при прыжке в лопасти |
| **Freezer** | **Морозильник** | `block.refurbished_furniture.freezer` | Заморозка воды в лёд и длительное хранение скоропортящихся продуктов |
| **Recycle Bin** | **Корзина для переработки** | `block.refurbished_furniture.recycle_bin` | Разборка ненужной мебели обратно в базовые доски и металл |
| **Workbench** | **Верстак мебели** | `block.refurbished_furniture.workbench` | Специализированный станок для крафта современной мебели |
| **Kitchen Cabinetry** | **Кухонный гарнитур** | `block.refurbished_furniture.*_kitchen_cabinetry` | Модульные шкафы и тумбы со встроенными ящиками |
| **Kitchen Sink** | **Кухонная мойка** | `block.refurbished_furniture.*_kitchen_sink` | Бесконечный или наполняемый резервуар воды для кулинарии |

---

## 16. Высокие и низкие двери (Dramatic Doors)

| Английский (EN) | Русский (RU) | ID предмета / блока | Назначение / Механика |
| :--- | :--- | :--- | :--- |
| **Tall Door** | **Высокая дверь** | `block.dramaticdoors.tall_*_door` | Трёхблочная полноразмерная дверь (открывается целиком от 1 клика) |
| **Short Door** | **Низкая дверь** | `block.dramaticdoors.short_*_door` | Одноблочная дверь для полуростовых проходов и погребов |
| **Tall Fence Gate** | **Высокая калитка** | `block.dramaticdoors.tall_*_fence_gate` | Высокая калитка против перепрыгивания крупными животными |

---

## 17. Коллекционные шляпы и аксессуары (Simple Hats)

| Английский (EN) | Русский (RU) | ID предмета / блока | Назначение / Механика |
| :--- | :--- | :--- | :--- |
| **Hat Grab-Bag** | **Мешок со шляпой** | `item.simplehats.hatbag_*` | Случайный лутбокс со шляпой соответствующей редкости |
| **Hat Scraps** | **Обрывки шляпы** | `item.simplehats.hatscraps_*` | Материал для перекрафта: 8 обрывков собираются в мешок |
| **Hat Stand** | **Стойка для шляп** | `item.simplehats.hatdisplay` | Декоративная подставка для демонстрации головных уборов |
| **Dyeable** | **Можно перекрасить** | Тултип шляпы | Поддерживает окрашивание красителями в верстаке |
| **Cycle variants** | **Смена вариаций в сетке крафта** | Тултип шляпы | Помещение в верстак циклически переключает фасон/модель |

---

## 18. Энтомология и шелководство (Longwings)

| Английский (EN) | Русский (RU) | ID предмета / блока | Назначение / Механика |
| :--- | :--- | :--- | :--- |
| **Catching Net** | **Ловчий сачок** | `item.longwings.catching_net` | Поимка летающих бабочек и мотыльков (ПКМ) в инвентарь |
| **Caterpillar Box** | **Инкубатор для гусениц** | `society:caterpillar_box` | Выкармливание гусениц листьями до стадии куколок/коконов |
| **Silk Thread** | **Шёлковая нить** | `item.longwings.silk_thread` | Ценный материал, получаемый из размотанных коконов |
| **Silk Fabric** | **Шёлковая ткань** | `item.longwings.silk_fabric` | Ткань премиум-качества для крафта одежды и мебели |
| **Butterfly Feeder** | **Кормушка для бабочек** | `block.longwings.feeder` | Поддержание популяции бабочек растворами сахара/мёда |
| **Glass Jar** | **Стеклянная банка для бабочек** | `block.longwings.glass_jar` | Декоративное содержание пойманных бабочек |

---

## 19. Разнообразный быт и текстиль (Etcetera)

| Английский (EN) | Русский (RU) | ID предмета / блока | Назначение / Механика |
| :--- | :--- | :--- | :--- |
| **Raw Bismuth** | **Рудный висмут** | `item.etcetera.raw_bismuth` | Переливающаяся руда Незера; сырьё для слитков |
| **Bismuth Ingot** | **Слиток висмута** | `item.etcetera.bismuth_ingot` | Металл для создания радужных блоков, стекла и фонарей |
| **Iridescent Glass** | **Радужное стекло** | `block.etcetera.iridescent_glass` | Декоративное стекло с перламутровым отливом |
| **Cotton** | **Хлопок** | `block.etcetera.cotton` | Растение для пошива свитеров, шляп и текстиля |
| **Sweater** | **Свитер** | `item.etcetera.*_sweater` | 16 цветов свитеров; универсальный любимый подарок жителей |
| **Tidal Helmet** | **Приливный шлем** | `item.etcetera.tidal_helmet` | Шлем из панциря черепахи и сердца моря |
| **Turtle Raft** | **Черепаший плот** | `item.etcetera.turtle_raft` | Плот с возможностью закрепления флагов |
| **Chapple** | **Яблоплёнок** | `entity.etcetera.chapple` | Гибрид цыплёнка и яблока; несёт яйцеяблоки |
| **Eggple** | **Яйцеяблоко** | `item.etcetera.eggple` | Питательный плод яблоплёнка (также золотая вариация) |

---

## 20. Строительные инструменты (Building Gadgets 2)

| Английский (EN) | Русский (RU) | ID предмета / блока | Назначение / Механика |
| :--- | :--- | :--- | :--- |
| **Building Gadget** | **Строительный гаджет** | `item.buildinggadgets2.gadget_building` | Скоростное размещение блоков по площади/сетке (бесплатно без FE) |
| **Exchanging Gadget** | **Гаджет замены** | `item.buildinggadgets2.gadget_exchanging` | Замена одних блоков на другие в мире без промежуточного дропа |
| **Copy Paste Gadget** | **Гаджет копирования и вставки** | `item.buildinggadgets2.gadget_copy_paste` | Копирование и тиражирование построек с поворотом |
| **Cut Paste Gadget** | **Гаджет вырезания и вставки** | `item.buildinggadgets2.gadget_cut_paste` | Вырезание структуры в память и перенос на новое место |
| **Destruction Gadget** | **Гаджет разрушения** | `item.buildinggadgets2.gadget_destruction` | Мгновенное стирание объемов блоков без выпадения дропа |
| **Template Manager** | **Менеджер шаблонов** | `block.buildinggadgets2.template_manager` | Блок для сохранения, загрузки и экспорта чертежей |
| **Template** | **Шаблон** | `item.buildinggadgets2.template` | Бумажный носитель для записи схем |
| **Redprint** | **Редпринт** | `item.buildinggadgets2.redprint` | Чертёж для сохранения и быстрой загрузки шаблонов |
| **Gadget Core** | **Ядро гаджета** | `item.buildinggadgets2.gadget_core` | Базовый технологический компонент для крафта гаджетов |

---

## 21. Автоматизация кулинарии (Create: Central Kitchen)

| Английский (EN) | Русский (RU) | ID предмета / блока | Назначение / Механика |
| :--- | :--- | :--- | :--- |
| **Blaze Stove** | **Плита всполоха** | `block.create_central_kitchen.blaze_stove` | Источник жара и мост для Механической руки к кухонному котлу |
| **Cooking Guide** | **Руководство по готовке** | `item.create_central_kitchen.cooking_guide` | Модуль настройки рецептов котла (Shift+ПКМ по горелке) |
| **Miner's Cooking Guide** | **Шахтёрское руководство по готовке** | `item.create_central_kitchen.miners_cooking_guide` | Модуль автоматизации для медного котелка Miner's Delight |
| **Sap** | **Древесный сок** | `fluid.create_central_kitchen.sap`, `...:sap_bucket` | Сок клёнов и берёз из сборщика сока (Tapper); сырьё для сиропа |
| **Syrup** | **Сироп** | `fluid.create_central_kitchen.syrup`, `...:syrup_bucket` | Сладкий уваренный сироп для десертов, блинов и напитков |
| **Aloe Gel** | **Гель алоэ** | `fluid.create_central_kitchen.aloe_gel`, `...:aloe_gel_bucket` | Растительный экстракт из листьев алоэ для кулинарии и медицины |
| **Tomato Sauce** | **Томатный соус** | `fluid.create_central_kitchen.tomato_sauce`, `...:tomato_sauce_bucket` | Густой соус из томатов в миксере для пасты и пиццы |
| **Incomplete [Dish]** | **Незаконченный [Блюдо]** | `item.create_central_kitchen.incomplete_*` | Промежуточный полуфабрикат конвейерной сборки Create |

---

## 22. Опасные существа и фауна (Legendary Creatures)

| Английский (EN) | Русский (RU) | ID предмета / сущности | Назначение / Механика |
| :--- | :--- | :--- | :--- |
| **Desert Mojo** | **Пустынный моджо** | `entity.legendarycreatures.desert_mojo` | Подземный голем кастомных пещерных биомов Society |
| **Forest Mojo** | **Лесной моджо** | `entity.legendarycreatures.forest_mojo` | Лесной пещерный страж биома пышных пещер |
| **Hound** | **Гончая** | `entity.legendarycreatures.hound` | Агрессивный зверь с атакой захвата и эффектом опутывания |
| **Scarecrow** | **Пугало** | `entity.legendarycreatures.scarecrow` | Враждебный моб, появляющийся при сборе урожая |
| **Corpse Eater** | **Пожиратель трупов** | `entity.legendarycreatures.corpse_eater` | Ночной хищник с уникальным лутом в сборке Society |
| **Wisp** | **Висп** | `entity.legendarycreatures.wisp` | Магический огонёк (частицы `wisp_particle` в машинах Society) |
| **Convulsion** | **Судороги** | `effect.legendarycreatures.convulsion` | Эффект неконтролируемых рывков (в ядах и пыльных слаймах) |
| **Root** | **Опутывание** | `effect.legendarycreatures.root` | Эффект блокировки движения при затяжном укусе гончей |
| **Doom Fire** | **Огонь рока** | `block.legendarycreatures.doom_fire` | Магический огонь |
## 23. Заказы и контракты (Bountiful)

| Английский (EN) | Русский (RU) | ID предмета / блока | Назначение / Механика |
| :--- | :--- | :--- | :--- |
| **Bounty Board** | **Доска объявлений** | `block.bountiful.bountyboard` | Центральный блок для взятия заказов и сдачи выполненных контрактов |
| **Decree** | **Распоряжение** | `item.bountiful.decree` | Указ, определяющий тематику появляющихся заказов на доске |
| **Bounty** | **Заказ** | `item.bountiful.bounty` | Свиток контракта с перечнем требований, таймером и наградой |
| **Decree: Artisan** | **Распоряжение: Ремесленника** | `bountiful.decree.artisan.name` | Контракты на ремесленные товары (масло, сыр, вино, ткань) |
| **Decree: Farming** | **Распоряжение: Фермера** | `bountiful.decree.farming.name` | Контракты на сбор и отгрузку сельскохозяйственных культур |
| **Decree: Fishing** | **Распоряжение: Рыбака** | `bountiful.decree.fishing.name` | Контракты на вылов рыбы и добычу сокровищ |
| **Decree: Geologist** | **Распоряжение: Геолога** | `bountiful.decree.geologist.name` | Контракты на добычу минералов, геод и самоцветов |
| **Decree: Cooking** | **Распоряжение: Кулинара** | `bountiful.decree.cooking.name` | Контракты на приготовление сложных блюд |
| **Seasonal Decrees** | **Сезонные распоряжения** | `bountiful.decree.[spring/summer/autumn/winter].name` | Сезонные контракты (автоматически адаптируются под текущий сезон) |

---

## 24. Земледелие, удобрения и спринклеры (Dew Drop Farmland Growth)

| Английский (EN) | Русский (RU) | ID предмета / блока | Назначение / Механика |
| :--- | :--- | :--- | :--- |
| **Iron Sprinkler** | **Железный спринклер** | `block.dew_drop_farmland_growth.iron_sprinkler` | Автополив области 3×3 каждое утро в 6:00 |
| **Gold Sprinkler** | **Золотой спринклер** | `block.dew_drop_farmland_growth.gold_sprinkler` | Автополив области 5×5 каждое утро в 6:00 |
| **Diamond Sprinkler** | **Алмазный спринклер** | `block.dew_drop_farmland_growth.diamond_sprinkler` | Автополив области 7×7 каждое утро в 6:00 |
| **Netherite Sprinkler** | **Иридиевый спринклер** | `block.dew_drop_farmland_growth.netherite_sprinkler` | Автополив области 9×9 каждое утро в 6:00 |
| **Weak Fertilizer** | **Слабое удобрение** | `item.dew_drop_farmland_growth.weak_fertilizer` | Ускорение созревания урожая (~1 день) |
| **Strong Fertilizer** | **Сильное удобрение** | `item.dew_drop_farmland_growth.strong_fertilizer` | Ускорение созревания урожая (~2 дня) |
| **Hyper Fertilizer** | **Гипер-удобрение** | `item.dew_drop_farmland_growth.hyper_fertilizer` | Ускорение созревания урожая (~3 дня / +33% скорости) |
| **Hydrating Fertilizer** | **Увлажняющее удобрение** | `item.dew_drop_farmland_growth.hydrating_fertilizer` | Автополив пашни до середины роста культуры |
| **Deluxe Hydrating Fertilizer** | **Роскошное увлажняющее удобрение** | `item.dew_drop_farmland_growth.deluxe_hydrating_fertilizer` | Перманентное 100% увлажнение; улучшение Садового горшка |
| **Low Quality Fertilizer** | **Удобрение базового качества** | `item.dew_drop_farmland_growth.low_quality_fertilizer` | Повышение шанса качественного урожая (серебро/золото) |
| **High Quality Fertilizer** | **Удобрение высокого качества** | `item.dew_drop_farmland_growth.high_quality_fertilizer` | Шанс качества ~80% (открывает иридий ~16%) |
| **Pristine Quality Fertilizer** | **Удобрение безупречного качества** | `item.dew_drop_farmland_growth.pristine_quality_fertilizer` | Шанс качества ~94% (иридий ~22%, золото ~34%) |
| **Bountiful Fertilizer** | **Изобильное удобрение** | `item.dew_drop_farmland_growth.bountiful_fertilizer` | +25% к валовому сбору, принудительно 0★ качество |
| **Garden Pot** | **Садовый горшок** | `block.dew_drop_farmland_growth.garden_pot` | Круглогодичное выращивание культур в помещении |


