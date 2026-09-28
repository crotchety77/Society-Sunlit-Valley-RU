# Аудит и синхронизация названий рыб: Raw (сырая) и Smoked (копчёная)

> **Итог работы:** Локализация названий всех 74 видов копчёных рыб (`society:smoked_*`) приведена к **100% строгому соответствию** названиям сырых оригиналов (`Raw RU`).

---

## 1. Итоговая статистика после синхронизации

| Показатель | До синхронизации | После синхронизации | Описание |
| :--- | :---: | :---: | :--- |
| **Всего проверено пар (Raw $\leftrightarrow$ Smoked)** | **74** | **74** | Все 74 рецепта коптильни |
| **[PASS] Согласованные основы** | 38 | **74 (100%)** | Основы названий полностью совпадают |
| **[DRIFT] Расхождения в основе** | 36 | **0 (0%)** | Все расхождения устранены |
| **[UNKNOWN] Неопределённые** | 0 | **0** | — |

---

## 2. Полный реестр всех 74 пар рыб (Raw $\leftrightarrow$ Smoked)

| # | Raw ID | Raw RU | Smoked ID | Актуальный Smoked RU | Единая основа | Статус |
| :-: | :--- | :--- | :--- | :--- | :--- | :---: |
| 1 | `aquaculture:atlantic_herring` | Атлантическая сельдь | `society:smoked_atlantic_herring` | **Копчёная атлантическая сельдь** | Атлантическая сельдь | [PASS] |
| 2 | `minecraft:pufferfish` | Иглобрюх | `society:smoked_pufferfish` | **Копчёный иглобрюх** | Иглобрюх | [PASS] |
| 3 | `aquaculture:minnow` | Пескарь | `society:smoked_minnow` | **Копчёный пескарь** | Пескарь | [PASS] |
| 4 | `aquaculture:bluegill` | Синежаберный солнечник | `society:smoked_bluegill` | **Копчёный синежаберный солнечник** | Синежаберный солнечник | [PASS] |
| 5 | `aquaculture:perch` | Окунь | `society:smoked_perch` | **Копчёный окунь** | Окунь | [PASS] |
| 6 | `minecraft:salmon` | Сырой лосось | `society:smoked_salmon` | **Копчёный лосось** | лосось | [PASS] |
| 7 | `aquaculture:blackfish` | Чёрная рыба | `society:smoked_blackfish` | **Копчёная чёрная рыба** | Чёрная рыба | [PASS] |
| 8 | `aquaculture:brown_trout` | Кумжа | `society:smoked_brown_trout` | **Копчёная кумжа** | Кумжа | [PASS] |
| 9 | `aquaculture:carp` | Карп | `society:smoked_carp` | **Копчёный карп** | Карп | [PASS] |
| 10 | `aquaculture:piranha` | Пиранья | `society:smoked_piranha` | **Копчёная пиранья** | Пиранья | [PASS] |
| 11 | `aquaculture:smallmouth_bass` | Малоротый окунь | `society:smoked_smallmouth_bass` | **Копчёный малоротый окунь** | Малоротый окунь | [PASS] |
| 12 | `minecraft:cod` | Сырая треска | `society:smoked_cod` | **Копчёная треска** | треска | [PASS] |
| 13 | `aquaculture:pollock` | Сайда | `society:smoked_pollock` | **Копчёная сайда** | Сайда | [PASS] |
| 14 | `aquaculture:jellyfish` | Медуза | `society:smoked_jellyfish` | **Копчёная медуза** | Медуза | [PASS] |
| 15 | `aquaculture:rainbow_trout` | Радужная форель | `society:smoked_rainbow_trout` | **Копчёная радужная форель** | Радужная форель | [PASS] |
| 16 | `aquaculture:pink_salmon` | Горбуша | `society:smoked_pink_salmon` | **Копчёная горбуша** | Горбуша | [PASS] |
| 17 | `minecraft:tropical_fish` | Тропическая рыба | `society:smoked_tropical_fish` | **Копчёная тропическая рыба** | Тропическая рыба | [PASS] |
| 18 | `aquaculture:red_grouper` | Красный групер | `society:smoked_red_grouper` | **Копчёный красный групер** | Красный групер | [PASS] |
| 19 | `aquaculture:gar` | Щука | `society:smoked_gar` | **Копчёная щука** | Щука | [PASS] |
| 20 | `aquaculture:muskellunge` | Гигантская щука | `society:smoked_muskellunge` | **Копчёная гигантская щука** | Гигантская щука | [PASS] |
| 21 | `aquaculture:synodontis` | Синодонтис | `society:smoked_synodontis` | **Копчёный синодонтис** | Синодонтис | [PASS] |
| 22 | `aquaculture:tambaqui` | Бурый паку | `society:smoked_tambaqui` | **Копчёный бурый паку** | Бурый паку | [PASS] |
| 23 | `aquaculture:atlantic_cod` | Атлантическая треска | `society:smoked_atlantic_cod` | **Копчёная атлантическая треска** | Атлантическая треска | [PASS] |
| 24 | `aquaculture:boulti` | Тиляпия | `society:smoked_boulti` | **Копчёная тиляпия** | Тиляпия | [PASS] |
| 25 | `aquaculture:leech` | Пиявка | `society:smoked_leech` | **Копчёная пиявка** | Пиявка | [PASS] |
| 26 | `aquaculture:catfish` | Канальный сомик | `society:smoked_catfish` | **Копчёный канальный сомик** | Канальный сомик | [PASS] |
| 27 | `aquaculture:tuna` | Тунец | `society:smoked_tuna` | **Копчёный тунец** | Тунец | [PASS] |
| 28 | `aquaculture:bayad` | Баяд | `society:smoked_bayad` | **Копчёный баяд** | Баяд | [PASS] |
| 29 | `aquaculture:arapaima` | Арапайма | `society:smoked_arapaima` | **Копчёная арапайма** | Арапайма | [PASS] |
| 30 | `aquaculture:atlantic_halibut` | Атлантический палтус | `society:smoked_atlantic_halibut` | **Копчёный атлантический палтус** | Атлантический палтус | [PASS] |
| 31 | `aquaculture:starshell_turtle` | Звёзднопанцирная черепаха | `society:smoked_starshell_turtle` | **Копчёная звёзднопанцирная черепаха** | Звёзднопанцирная черепаха | [PASS] |
| 32 | `aquaculture:brown_shrooma` | Коричневая грибная рыба | `society:smoked_brown_shrooma` | **Копчёная коричневая грибная рыба** | Коричневая грибная рыба | [PASS] |
| 33 | `aquaculture:red_shrooma` | Красная грибная рыба | `society:smoked_red_shrooma` | **Копчёная красная грибная рыба** | Красная грибная рыба | [PASS] |
| 34 | `aquaculture:arrau_turtle` | Тартаруга | `society:smoked_arrau_turtle` | **Копчёная тартаруга** | Тартаруга | [PASS] |
| 35 | `aquaculture:capitaine` | Рыба-капитан | `society:smoked_capitaine` | **Копчёная рыба-капитан** | Рыба-капитан | [PASS] |
| 36 | `aquaculture:box_turtle` | Коробчатая черепаха | `society:smoked_box_turtle` | **Копчёная коробчатая черепаха** | Коробчатая черепаха | [PASS] |
| 37 | `aquaculture:pacific_halibut` | Тихоокеанский палтус | `society:smoked_pacific_halibut` | **Копчёный тихоокеанский палтус** | Тихоокеанский палтус | [PASS] |
| 38 | `aquaculture:goldfish` | Золотая рыбка | `society:smoked_goldfish` | **Копчёная золотая рыбка** | Золотая рыбка | [PASS] |
| 39 | `crabbersdelight:shrimp` | Креветка | `society:smoked_shrimp` | **Копчёная креветка** | Креветка | [PASS] |
| 40 | `crabbersdelight:clawster` | Омар | `society:smoked_clawster` | **Копчёный омар** | Омар | [PASS] |
| 41 | `crabbersdelight:crab` | Краб | `society:smoked_crab` | **Копчёный краб** | Краб | [PASS] |
| 42 | `crabbersdelight:clam` | Моллюск | `society:smoked_clam` | **Копчёный моллюск** | Моллюск | [PASS] |
| 43 | `netherdepthsupgrade:searing_cod` | Огненная треска | `society:smoked_searing_cod` | **Копчёная огненная треска** | Огненная треска | [PASS] |
| 44 | `netherdepthsupgrade:blazefish` | Ифриторыба | `society:smoked_blazefish` | **Копчёная ифриторыба** | Ифриторыба | [PASS] |
| 45 | `netherdepthsupgrade:lava_pufferfish` | Лавобрюх | `society:smoked_lava_pufferfish` | **Копчёный лавобрюх** | Лавобрюх | [PASS] |
| 46 | `netherdepthsupgrade:obsidianfish` | Обсидианорыба | `society:smoked_obsidianfish` | **Копчёная обсидианорыба** | Обсидианорыба | [PASS] |
| 47 | `netherdepthsupgrade:bonefish` | Скелеторыба | `society:smoked_bonefish` | **Копчёная скелеторыба** | Скелеторыба | [PASS] |
| 48 | `netherdepthsupgrade:wither_bonefish` | Визер-скелеторыба | `society:smoked_wither_bonefish` | **Копчёная визер-скелеторыба** | Визер-скелеторыба | [PASS] |
| 49 | `netherdepthsupgrade:magmacubefish` | Рыба магмакуб | `society:smoked_magmacubefish` | **Копчёная рыба магмакуб** | Рыба магмакуб | [PASS] |
| 50 | `netherdepthsupgrade:glowdine` | Светорыба | `society:smoked_glowdine` | **Копчёная светорыба** | Светорыба | [PASS] |
| 51 | `netherdepthsupgrade:soulsucker` | Высасыватель луш | `society:smoked_soulsucker` | **Копчёный высасыватель душ** | Высасыватель луш | [PASS] |
| 52 | `netherdepthsupgrade:fortress_grouper` | Крепостной группер | `society:smoked_fortress_grouper` | **Копчёный крепостной группер** | Крепостной группер | [PASS] |
| 53 | `netherdepthsupgrade:eyeball_fish` | Рыба-глаз | `society:smoked_eyeball_fish` | **Копчёная рыба-глаз** | Рыба-глаз | [PASS] |
| 54 | `society:neptuna` | Нептуна | `society:smoked_neptuna` | **Копчёная нептуна** | Нептуна | [PASS] |
| 55 | `unusualfishmod:raw_sneep_snorp` | Снип-снорп | `society:smoked_sneep_snorp` | **Копчёный снип-снорп** | Снип-снорп | [PASS] |
| 56 | `unusualfishmod:raw_picklefish` | Рыба-огурец | `society:smoked_picklefish` | **Копчёная рыба-огурец** | Рыба-огурец | [PASS] |
| 57 | `unusualfishmod:raw_forkfish` | Рыба-вилохвост | `society:smoked_forkfish` | **Копчёная рыба-вилохвост** | Рыба-вилохвост | [PASS] |
| 58 | `unusualfishmod:raw_beaked_herring` | Клюворылая сельдь | `society:smoked_beaked_herring` | **Копчёная клюворылая сельдь** | Клюворылая сельдь | [PASS] |
| 59 | `unusualfishmod:raw_sailor_barb` | Барбус-моряк | `society:smoked_sailor_barb` | **Копчёный барбус-моряк** | Барбус-моряк | [PASS] |
| 60 | `unusualfishmod:raw_demon_herring` | Сельдь-демон | `society:smoked_demon_herring` | **Копчёная сельдь-демон** | Сельдь-демон | [PASS] |
| 61 | `unusualfishmod:raw_triple_twirl_pleco` | Тройной вихревой сомик | `society:smoked_triple_twirl_pleco` | **Копчёный тройной вихревой сомик** | Тройной вихревой сомик | [PASS] |
| 62 | `unusualfishmod:raw_copperflame_anthias` | Меднопламенный антиас | `society:smoked_copperflame_anthias` | **Копчёный меднопламенный антиас** | Меднопламенный антиас | [PASS] |
| 63 | `unusualfishmod:raw_drooping_gourami` | Вислоухий гурами | `society:smoked_drooping_gourami` | **Копчёный вислоухий гурами** | Вислоухий гурами | [PASS] |
| 64 | `unusualfishmod:raw_duality_damselfish` | Двуликая рыба-ласточка | `society:smoked_duality_damselfish` | **Копчёная двуликая рыба-ласточка** | Двуликая рыба-ласточка | [PASS] |
| 65 | `unusualfishmod:raw_blind_sailfin` | Слепой парусник | `society:smoked_blind_sailfin` | **Копчёный слепой парусник** | Слепой парусник | [PASS] |
| 66 | `unusualfishmod:raw_circus_fish` | Цирковая рыба | `society:smoked_circus_fish` | **Копчёная цирковая рыба** | Цирковая рыба | [PASS] |
| 67 | `unusualfishmod:raw_snowflake` | Морозный плавник | `society:smoked_frosty_fin` | **Копчёный морозный плавник** | Морозный плавник | [PASS] |
| 68 | `unusualfishmod:raw_aero_mono` | Аэромоно | `society:smoked_aero_mono` | **Копчёный аэромоно** | Аэромоно | [PASS] |
| 69 | `unusualfishmod:raw_hatchetfish` | Рыба-топорик | `society:smoked_hatchetfish` | **Копчёная рыба-топорик** | Рыба-топорик | [PASS] |
| 70 | `unusualfishmod:raw_spindlefish` | Рыба-веретено | `society:smoked_spindlefish` | **Копчёная рыба-веретено** | Рыба-веретено | [PASS] |
| 71 | `unusualfishmod:raw_bark_angelfish` | Древесная скалярия | `society:smoked_bark_angelfish` | **Копчёная древесная скалярия** | Древесная скалярия | [PASS] |
| 72 | `unusualfishmod:raw_amber_goby` | Янтарный бычок | `society:smoked_amber_goby` | **Копчёный янтарный бычок** | Янтарный бычок | [PASS] |
| 73 | `unusualfishmod:raw_eyelash` | Рыба-ресничка | `society:smoked_eyelash` | **Копчёная рыба-ресничка** | Рыба-ресничка | [PASS] |
| 74 | `crittersandcompanions:koi_fish` | Карп кои | `society:smoked_koi_fish` | **Копчёный карп кои** | Карп кои | [PASS] |
