# Полный аудит локализации Patchouli Almanac

## 1. Исходники книги и механизм загрузки Patchouli

Книга `patchouli:almanac` (Фермерский альманах) является внешней книгой (External Book), расположенной по пути:
* `patchouli_books/almanac/`
* Файл конфигурации: `patchouli_books/almanac/book.json`
* Категории: `patchouli_books/almanac/en_us/categories/` (6 категорий)
* Главы/Статьи: `patchouli_books/almanac/en_us/entries/` (191 статья в 6 подпапках)
* Всего страниц: 386 страниц (`patchouli:text`, `patchouli:entity`, `patchouli:multiblock`).

### Технический механизм загрузки в Patchouli (байткод-аудит):
1. **`BookContentExternalLoader`**: При поиске файлов сканирует структуру `patchouli_books/almanac/en_us/`.
2. **`BookContentsBuilder.loadLocalizedJson`**: При инициализации заменяет путь `en_us` на локаль клиента (`replaceAll("en_us", "ru_ru")`) и пытается загрузить файл из `patchouli_books/almanac/ru_ru/`.
3. **Флаг `i18n`**: В `book.json` параметр `"i18n"` по умолчанию равен `false`. При `i18n: false` методы `BookCategory.getName()` и `BookEntry.getName()` вызывают `Component.literal(name)` — то есть выводят литеральную строку `"name"` напрямую из загруженного JSON-файла, не обращаясь к `ru_ru.json`.
4. **Причина английских названий:** Если папка `ru_ru/` отсутствует в `patchouli_books/almanac/` (как было в исходной сборке), Patchouli выполняет fallback на `en_us/` и загружает файлы с литеральными английскими именами.

## 2. Анализ категорий (Разделов книги)

| Файл категории | ID | EN Название | Актуальное RU название | Старое название в Scriptora | Статус |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `animals.json` | `animals` | Farm Animals | **Домашние животные** | Фермерские животные | DRIFT |
| `crops.json` | `crops` | Crops | **Сельхозкультуры** | Урожай | DRIFT |
| `pets.json` | `pets` | Pets | **Питомцы** | Питомцы | PASS |
| `slimes.json` | `slimes` | Slimes | **Слаймы** | Слизни | DRIFT |
| `tree_crops.json` | `tree_crops` | Tree Crops | **Древесные культуры** | Древесные культуры | PASS |
| `trees.json` | `trees` | Trees | **Деревья** | Деревья | PASS |

## 3. Анализ глав и расхождений (Entries Audit)

Все 191 запись разделены на 6 категорий:

### Категория: `animals` (44 статей)

| Файл | ID / Иконка | English | Актуальное RU | Старое RU | Статус |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `animals/bat.json` | `pamhc2trees:plumitem` | Bat | **Летучая мышь** | [UNTRANSLATED] | UNTRANSLATED |
| `animals/bison.json` | `wildernature:bison_horn` | Bison | **Бизон** | Бизон | PASS |
| `animals/chapple.json` | `minecraft:apple` | Chapple | **Chapple** | Яблокурица | DRIFT |
| `animals/chicken.json` | `minecraft:egg` | Chicken | **Курица** | Курица | PASS |
| `animals/cochineal.json` | `atmospheric:carmine_husk` | Cochineal | **Кошениль** | Кошениль | PASS |
| `animals/cow.json` | `society:large_milk` | Cow | **Корова** | Корова | PASS |
| `animals/cruncher.json` | `species:cruncher_egg` | Cruncher | **Кусач** | [UNTRANSLATED] | UNTRANSLATED |
| `animals/deer.json` | `society:dried_foul_berries` | Deer | **Deer** | Олень | DRIFT |
| `animals/duck.json` | `untitledduckmod:duck_egg` | Duck | **Утка** | Утка | PASS |
| `animals/flamingo.json` | `society:flamingo_egg` | Flamingo | **Flamingo** | Фламинго | DRIFT |
| `animals/frog.json` | `society:ribbit_gadget` | Frog | **Лягушка** | Лягушка | PASS |
| `animals/frostbiter.json` | `windswept:frozen_branch` | Frostbiter | **Обморозитель** | Обморозитель | PASS |
| `animals/galliraptor.json` | `farmlife:galliraptor_egg` | Galliraptor | **Galliraptor** | Галлираптор | DRIFT |
| `animals/glow_squid.json` | `minecraft:glow_ink_sac` | Glow Squid | **Glow Squid** | Светящийся спрут | DRIFT |
| `animals/goat.json` | `society:large_goat_milk` | Goat | **Коза** | Коза | PASS |
| `animals/golden_chapple.json` | `minecraft:golden_apple` | Golden Chapple | **Golden Chapple** | Золотое курояблоко | DRIFT |
| `animals/goober.json` | `species:petrified_egg` | Goober | **Губер** | Губер | PASS |
| `animals/goose.json` | `untitledduckmod:goose_egg` | Goose | **Гусь** | Гусь | PASS |
| `animals/mammutilation.json` | `species:ichor_bottle` | Mammutilation | **Маммутиляция** | Маммутиляция | PASS |
| `animals/minisheep.json` | `society:fine_wool` | Minisheep | **Minisheep** | Мини-овца | DRIFT |
| `animals/moobloom.json` | `betterarcheology:growth_totem` | Moobloom | **Мублум** | Мублум | PASS |
| `animals/mooshroom.json` | `minecraft:red_mushroom` | Mooshroom | **Mooshroom** | Грибная корова | DRIFT |
| `animals/panda.json` | `pamhc2trees:mangoitem` | Panda | **Панда** | Панда | PASS |
| `animals/penguin.json` | `society:penguin_egg` | Penguin | **Penguin** | Пингвин | DRIFT |
| `animals/pig.json` | `society:truffle` | Pig | **Свинья** | Свинья | PASS |
| `animals/rabbit.json` | `minecraft:rabbit_foot` | Rabbit | **Кролик** | Кролик | PASS |
| `animals/raccoon.json` | `furniture:trash_bag` | Raccoon | **Енот** | Енот | PASS |
| `animals/red_panda.json` | `society:ruby` | Red Panda | **Red Panda** | Красная панда | DRIFT |
| `animals/sheep.json` | `society:large_sheep_milk` | Sheep | **Овца** | Овца | PASS |
| `animals/shima_enaga.json` | `atmospheric:currant` | Shima Enaga | **Длиннохвостая синица** | [UNTRANSLATED] | UNTRANSLATED |
| `animals/snail.json` | `autumnity:snail_shell_piece` | Snail | **Улитка** | Улитка | PASS |
| `animals/sniffer.json` | `minecraft:sniffer_egg` | Sniffer | **Sniffer** | Нюхач | DRIFT |
| `animals/snow_pig.json` | `snowpig:frozen_porkchop` | Snow Pig | **Снежная свинья** | Снежная свинья | PASS |
| `animals/snuffle.json` | `snuffles:snuffle_fluff` | Snuffle | **Снуфлик** | Нюхль | DRIFT |
| `animals/squid.json` | `minecraft:ink_sac` | Squid | **Squid** | Спрут | DRIFT |
| `animals/squirrel.json` | `pamhc2trees:hazelnutitem` | Squirrel | **Белка** | Белка | PASS |
| `animals/tri_bull.json` | `society:large_tri_bull_milk` | Domestic Tri-bull | **Domestic Tri-bull** | Домашний три-бык | DRIFT |
| `animals/turkey.json` | `autumnity:turkey_egg` | Turkey | **Индейка** | Индейка | PASS |
| `animals/turtle.json` | `minecraft:turtle_egg` | Turtle | **Черепаха** | [UNTRANSLATED] | UNTRANSLATED |
| `animals/warped_wooly_cow.json` | `society:large_warped_milk` | Warped Wooly Cow | **Warped Wooly Cow** | Искажённая шерстистая корова | DRIFT |
| `animals/water_buffalo.json` | `society:large_buffalo_milk` | Water Buffalo | **Water Buffalo** | Водяной буйвол | DRIFT |
| `animals/wooly_cow.json` | `meadow:highland_wool` | Wooly Cow | **Шерстяная корова** | Шерстяная корова | PASS |
| `animals/wooly_sheep.json` | `meadow:rocky_wool` | Wooly Sheep | **Шерстистая овца** | Шерстистая овца | PASS |
| `animals/wraptor.json` | `species:wraptor_egg` | Wraptor | **Ираптор** | Враптор | DRIFT |

### Категория: `crops` (47 статей)

| Файл | ID / Иконка | English | Актуальное RU | Старое RU | Статус |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `crops/aloe_vera.json` | `atmospheric:aloe_leaves` | Aloe Vera 🔥 | **Листья алоэ 🔥** | Алоэ вера 🔥 | DRIFT |
| `crops/ancient_fruit.json` | `society:ancient_fruit` | Ancient Fruit 🌼🔥🍂 | **Ancient Fruit 🌼🔥🍂** | Древний плод 🌼🔥🍂 | DRIFT |
| `crops/barley.json` | `farm_and_charm:barley` | Barley 🍂❆ | **Ячмень 🍂❆** | Ячмень 🍂❆ | PASS |
| `crops/beetroot.json` | `minecraft:beetroot` | Beetroot 🍂 | **Beetroot 🍂** | Свёкла 🍂 | DRIFT |
| `crops/bellpepper.json` | `veggiesdelight:bellpepper` | Bell Pepper 🔥 | **Болгарский перец 🔥** | Болгарский перец 🔥 | PASS |
| `crops/blueberry.json` | `society:blueberry` | Blueberry 🔥 | **Blueberry 🔥** | Черника 🔥 | DRIFT |
| `crops/broccoli.json` | `veggiesdelight:broccoli` | Broccoli 🍂 | **Брокколи 🍂** | Брокколи 🍂 | PASS |
| `crops/cabbage.json` | `farmersdelight:cabbage` | Cabbage 🍂❆ | **Капуста 🍂❆** | Капуста 🍂❆ | PASS |
| `crops/carrot.json` | `minecraft:carrot` | Carrot 🌼🍂 | **Carrot 🌼🍂** | Морковь 🌼🍂 | DRIFT |
| `crops/cauliflower.json` | `veggiesdelight:cauliflower` | Cauliflower 🌼 | **Цветная капуста 🌼** | Цветная капуста 🌼 | PASS |
| `crops/coffee_beans.json` | `herbalbrews:coffee_beans` | Coffee Beans 🌼 | **Coffee Beans 🌼** | Кофейные зёрна 🌼 | DRIFT |
| `crops/corn.json` | `farm_and_charm:corn` | Corn 🔥🍂 | **Кукуруза 🔥🍂** | Кукуруза 🔥🍂 | PASS |
| `crops/cotton.json` | `etcetera:cotton_flower` | Cotton 🔥 | **Цветок хлопка 🔥** | Хлопок 🔥 | DRIFT |
| `crops/cranberry.json` | `society:cranberry` | Cranberry 🍂 | **Cranberry 🍂** | [UNTRANSLATED] | UNTRANSLATED |
| `crops/cucumber.json` | `vintagedelight:cucumber` | Cucumber 🌼 | **Огурец 🌼** | Огурец 🌼 | PASS |
| `crops/eggplant.json` | `society:eggplant` | Eggplant 🍂 | **Eggplant 🍂** | Баклажан 🍂 | DRIFT |
| `crops/flax.json` | `supplementaries:flax` | Flax 🌼 | **Лён 🌼** | Лён 🌼 | PASS |
| `crops/foul_berries.json` | `autumnity:foul_berries` | Foul Berries 🍂 | **Кислые ягоды 🍂** | Мерзкие ягоды 🍂 | DRIFT |
| `crops/garlic.json` | `veggiesdelight:garlic` | Garlic 🌼 | **Чеснок 🌼** | Чеснок 🌼 | PASS |
| `crops/gearo_berry.json` | `vintagedelight:gearo_berry` | Gearo Berries 🌼 | **Ягоды гиро 🌼** | Ягоды георо 🌼 | DRIFT |
| `crops/ghost_pepper.json` | `vintagedelight:ghost_pepper` | Ghost Pepper 🔥 | **Перец чили 🔥** | Перец-призрак 🔥 | DRIFT |
| `crops/ginger.json` | `snowyspirit:ginger` | Ginger ❆ | **Имбирь ❆** | Имбирь ❆ | PASS |
| `crops/grapes.json` | `vinery:red_grape` | Grapes 🌐 | **Красный виноград 🌐** | Виноград 🌐 | DRIFT |
| `crops/green_tea.json` | `herbalbrews:green_tea_leaf` | Green Tea 🌼🔥🍂 | **Лист зелёного чая 🌼🔥🍂** | Зелёный чай 🌼🔥🍂 | DRIFT |
| `crops/hops.json` | `brewery:hops` | Hops 🔥 | **Хмель 🔥** | Хмель 🔥 | PASS |
| `crops/iconography.json` | `minecraft:written_book` | Iconogaphy | **Iconogaphy** | Обозначения | DRIFT |
| `crops/lettuce.json` | `farm_and_charm:lettuce` | Lettuce 🌼 | **Салат латук 🌼** | Салат 🌼 | DRIFT |
| `crops/nether_grapes.json` | `nethervinery:warped_grape` | Nether Grapes 🌼🍂 | **Искажённый виноград 🌼🍂** | Виноград из Незера 🌐 | DRIFT |
| `crops/oat.json` | `farm_and_charm:oat` | Oat 🔥 | **Овёс 🔥** | Овёс 🔥 | PASS |
| `crops/onion.json` | `farm_and_charm:onion` | Onion 🌼 | **Лук 🌼** | Лук 🌼 | PASS |
| `crops/peanut.json` | `vintagedelight:peanut` | Peanut 🍂 | **Арахис 🍂** | Арахис 🍂 | PASS |
| `crops/pitcher_plant.json` | `minecraft:pitcher_plant` | Pitcher Plant 🔥 | **Pitcher Plant 🔥** | Кувшинница 🔥 | DRIFT |
| `crops/potato.json` | `minecraft:potato` | Potato 🌼 | **Potato 🌼** | Картофель 🌼 | DRIFT |
| `crops/rice.json` | `farmersdelight:rice` | Rice 🔥🍂 | **Рис 🔥🍂** | Рис 🔥🍂 | PASS |
| `crops/rooibos.json` | `herbalbrews:rooibos_leaf` | Rooibos 🔥 | **Rooibos 🔥** | Ройбуш 🔥 | DRIFT |
| `crops/sparkpod.json` | `society:sparkpod` | Sparkpod 🌼 | **Sparkpod 🌼** | [UNTRANSLATED] | UNTRANSLATED |
| `crops/strawberry.json` | `farm_and_charm:strawberry` | Strawberry 🌼 | **Клубника 🌼** | Клубника 🌼 | PASS |
| `crops/sweet_berries.json` | `minecraft:sweet_berries` | Sweet Berries 🌼❆ | **Sweet Berries 🌼❆** | Сладкие ягоды 🌼🍂 | DRIFT |
| `crops/sweet_potato.json` | `veggiesdelight:sweet_potato` | Sweet Potato 🍂 | **Батат 🍂** | Батат 🍂 | PASS |
| `crops/tomato.json` | `farmersdelight:tomato` | Tomato 🌼🔥🍂 | **Томат 🌼🔥🍂** | Томат 🌼🔥🍂 | PASS |
| `crops/torchflower.json` | `minecraft:torchflower` | Torchflower 🔥 | **Torchflower 🔥** | Факельник 🔥 | DRIFT |
| `crops/tubabacco.json` | `society:tubabacco_leaf` | Tubabacco 🌼❆ | **Tubabacco 🌼❆** | Тубакко 🌼❆ | DRIFT |
| `crops/turnip.json` | `veggiesdelight:turnip` | Turnip 🌼 | **Репа 🌼** | Репа 🌼 | PASS |
| `crops/wheat.json` | `minecraft:wheat` | Wheat 🔥🍂 | **Wheat 🔥🍂** | Пшеница 🔥🍂 | DRIFT |
| `crops/wild_berries.json` | `windswept:wild_berries` | Wild Berries ❆ | **Дикие ягоды ❆** | Дикие ягоды ❆ | PASS |
| `crops/yerba_mate.json` | `herbalbrews:yerba_mate_leaf` | Yerba Mate 🌼🔥🍂 | **Yerba Mate 🌼🔥🍂** | Мате 🌼🔥🍂 | DRIFT |
| `crops/zucchini.json` | `veggiesdelight:zucchini` | Zucchini 🔥 | **Цукини 🔥** | Цукини 🔥 | PASS |

### Категория: `pets` (15 статей)

| Файл | ID / Иконка | English | Актуальное RU | Старое RU | Статус |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `pets/allay.json` | `minecraft:amethyst_shard` | Allay | **Allay** | Эллей | DRIFT |
| `pets/axolotl.json` | `beachparty:rubber_ring_axolotl` | Axolotl | **Axolotl Надувной круг** | Аксолотль | DRIFT |
| `pets/cat.json` | `minecraft:cod` | Cat | **Cat** | Кошка | DRIFT |
| `pets/dog.json` | `farm_and_charm:dog_food` | Dog | **Корм для собак** | Собака | DRIFT |
| `pets/ferret.json` | `minecraft:iron_shovel` | Ferret | **Ferret** | Хорёк | DRIFT |
| `pets/foxhound.json` | `minecraft:coal` | Foxhound | **Foxhound** | Адская гончая | DRIFT |
| `pets/grizzly_bear.json` | `buzzier_bees:honey_apple` | Grizzly Bear | **Яблоко в меду** | Медведь гризли | DRIFT |
| `pets/hamster.json` | `hamsters:hamster` | Hamster | **Hamster** | Хомяк | DRIFT |
| `pets/hedgehog.json` | `supplementaries:bamboo_spikes` | Hedgehog | **Бамбуковые шипы** | Ёж | DRIFT |
| `pets/horse.json` | `relics:horse_flute` | Horse | **Лошадиная флейта** | Лошадь | DRIFT |
| `pets/owl.json` | `tanukidecor:owl_clock` | Owl | **Часы-сова** | Сова | DRIFT |
| `pets/polar_bear.json` | `minecraft:snowball` | Polar Bear | **Polar Bear** | Белый медведь | DRIFT |
| `pets/red_wolf.json` | `species:wicked_treat` | Red Wolf | **Лакомка** | Красный волк | DRIFT |
| `pets/shiba.json` | `minecraft:arrow` | Shiba | **Shiba** | Сиба | DRIFT |
| `pets/wolf.json` | `minecraft:bone` | Wolf | **Wolf** | Волк | DRIFT |

### Категория: `slimes` (24 статей)

| Файл | ID / Иконка | English | Актуальное RU | Старое RU | Статус |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `slimes/all_seeing.json` | `splendid_slimes:plort{plort:{id:"splendid_slimes:all_seeing"}}` | All-Seeing | **%s плорт** | Всевидящий | DRIFT |
| `slimes/bear.json` | `splendid_slimes:plort{plort:{id:"splendid_slimes:bear"}}` | Bear | **%s плорт** | [UNTRANSLATED] | UNTRANSLATED |
| `slimes/bitwize.json` | `splendid_slimes:plort{plort:{id:"splendid_slimes:bitwise"}}` | Bitwise | **%s плорт** | Битовый | DRIFT |
| `slimes/blazing.json` | `splendid_slimes:plort{plort:{id:"splendid_slimes:blazing"}}` | Blazing | **%s плорт** | Пылающий | DRIFT |
| `slimes/bony.json` | `splendid_slimes:plort{plort:{id:"splendid_slimes:bony"}}` | Bony | **%s плорт** | Костлявый | DRIFT |
| `slimes/boomcat.json` | `splendid_slimes:plort{plort:{id:"splendid_slimes:boomcat"}}` | Boomcat | **%s плорт** | Бумкот | DRIFT |
| `slimes/dusty.json` | `splendid_slimes:plort{plort:{id:"splendid_slimes:dusty"}}` | Dusty | **%s плорт** | Пыльный | DRIFT |
| `slimes/ender.json` | `splendid_slimes:plort{plort:{id:"splendid_slimes:ender"}}` | Ender | **%s плорт** | Эндер-слайм | DRIFT |
| `slimes/gold.json` | `splendid_slimes:plort{plort:{id:"splendid_slimes:gold"}}` | Gold | **%s плорт** | Золотой | DRIFT |
| `slimes/juicy.json` | `splendid_slimes:plort{plort:{id:"splendid_slimes:juicy"}}` | Juicy | **%s плорт** | Сочный | DRIFT |
| `slimes/luminous.json` | `splendid_slimes:plort{plort:{id:"splendid_slimes:luminous"}}` | Luminous | **%s плорт** | Светящийся | DRIFT |
| `slimes/mechanic.json` | `splendid_slimes:plort{plort:{id:"splendid_slimes:mechanic"}}` | Mechanic Slime | **%s плорт** | [UNTRANSLATED] | UNTRANSLATED |
| `slimes/minty.json` | `splendid_slimes:plort{plort:{id:"splendid_slimes:minty"}}` | Minty | **%s плорт** | Мятный | DRIFT |
| `slimes/orby.json` | `splendid_slimes:plort{plort:{id:"splendid_slimes:orby"}}` | Orby | **%s плорт** | Орби | DRIFT |
| `slimes/phantom.json` | `splendid_slimes:plort{plort:{id:"splendid_slimes:phantom"}}` | Phantom | **%s плорт** | Фантом | DRIFT |
| `slimes/prisma.json` | `splendid_slimes:plort{plort:{id:"splendid_slimes:prisma"}}` | Prisma | **%s плорт** | Призма | DRIFT |
| `slimes/puddle.json` | `splendid_slimes:plort{plort:{id:"splendid_slimes:puddle"}}` | Puddle | **%s плорт** | Водяной | DRIFT |
| `slimes/rotting.json` | `splendid_slimes:plort{plort:{id:"splendid_slimes:rotting"}}` | Rotting | **%s плорт** | Гниющий | DRIFT |
| `slimes/shulking.json` | `splendid_slimes:plort{plort:{id:"splendid_slimes:shulking"}}` | Shulking | **%s плорт** | Шалкерный | DRIFT |
| `slimes/slimy.json` | `splendid_slimes:plort{plort:{id:"splendid_slimes:slimy"}}` | Slimy | **%s плорт** | Слизистый | DRIFT |
| `slimes/sparkcat.json` | `splendid_slimes:plort{plort:{id:"splendid_slimes:sparkcat"}}` | Sparkcat | **%s плорт** | Искрокот | DRIFT |
| `slimes/sweet.json` | `splendid_slimes:plort{plort:{id:"splendid_slimes:sweet"}}` | Sweet | **%s плорт** | Сладкий | DRIFT |
| `slimes/webby.json` | `splendid_slimes:plort{plort:{id:"splendid_slimes:webby"}}` | Webby | **%s плорт** | Паутинный | DRIFT |
| `slimes/weeping.json` | `splendid_slimes:plort{plort:{id:"splendid_slimes:weeping"}}` | Weeping | **%s плорт** | Плачущий | DRIFT |

### Категория: `tree_crops` (15 статей)

| Файл | ID / Иконка | English | Актуальное RU | Старое RU | Статус |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `tree_crops/apple.json` | `minecraft:apple` | Apple 🍂 | **Apple 🍂** | [UNTRANSLATED] | UNTRANSLATED |
| `tree_crops/banana.json` | `pamhc2trees:bananaitem` | Banana 🔥 | **Банан** | [UNTRANSLATED] | UNTRANSLATED |
| `tree_crops/cherry.json` | `vinery:cherry` | Cherry 🌼 | **Вишня** | [UNTRANSLATED] | UNTRANSLATED |
| `tree_crops/cinnamon.json` | `pamhc2trees:cinnamonitem` | Cinnamon 🍂❆ | **Корица** | [UNTRANSLATED] | UNTRANSLATED |
| `tree_crops/dragonfruit.json` | `pamhc2trees:dragonfruititem` | Dragonfruit ❆ | **Питайя** | [UNTRANSLATED] | UNTRANSLATED |
| `tree_crops/hazelnut.json` | `pamhc2trees:hazelnutitem` | Hazelnut 🍂 | **Фундук** | [UNTRANSLATED] | UNTRANSLATED |
| `tree_crops/lemon.json` | `pamhc2trees:lemonitem` | Lemon 🌼🔥 | **Лимон** | Лимон 🌼🔥 | DRIFT |
| `tree_crops/lychee.json` | `pamhc2trees:lycheeitem` | Lychee 🌐 | **Личи** | Личи 🌐 | DRIFT |
| `tree_crops/mango.json` | `pamhc2trees:mangoitem` | Mango 🔥 | **Манго** | Манго 🔥 | DRIFT |
| `tree_crops/orange.json` | `atmospheric:orange` | Orange 🔥 | **Апельсин** | Апельсин 🔥 | DRIFT |
| `tree_crops/passionfruit.json` | `atmospheric:passion_fruit` | Passionfruit 🌼 | **Маракуйя** | Маракуйя 🌼 | DRIFT |
| `tree_crops/pawpaw.json` | `pamhc2trees:pawpawitem` | Pawpaw 🍂 | **Азимина** | Азимина 🍂 | DRIFT |
| `tree_crops/peach.json` | `pamhc2trees:peachitem` | Peach 🔥 | **Персик** | Персик 🔥 | DRIFT |
| `tree_crops/plum.json` | `pamhc2trees:plumitem` | Plum 🍂 | **Слива** | Слива 🍂 | DRIFT |
| `tree_crops/starfruit.json` | `pamhc2trees:starfruititem` | Starfruit 🌐 | **Карамбола** | Карамбола 🌐 | DRIFT |

### Категория: `trees` (46 статей)

| Файл | ID / Иконка | English | Актуальное RU | Старое RU | Статус |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `trees/pale_oak.json` | `minecraft:pale_oak_sapling` | Pale Oak Tree 🌐 | **Саженец бледного дуба** | Бледный дуб 🌐 | DRIFT |
| `trees/atmospheric/aspen.json` | `atmospheric:aspen_sapling` | Aspen Tree 🌐 | **Саженец осины** | Осина 🌐 | DRIFT |
| `trees/atmospheric/dry_laurel.json` | `atmospheric:dry_laurel_sapling` | Dry Laurel Tree 🌐 | **Саженец сухого лавра** | Сухое лавровое дерево 🌐 | DRIFT |
| `trees/atmospheric/green_aspen.json` | `atmospheric:green_aspen_sapling` | Green Aspen Tree 🌐 | **Саженец зелёной осины** | Зелёная осина 🌐 | DRIFT |
| `trees/atmospheric/grimwood.json` | `atmospheric:grimwood_sapling` | Grimwood Tree 🌐 | **Саженец мрачного дерева** | Мраколес 🌐 | DRIFT |
| `trees/atmospheric/kousa.json` | `atmospheric:kousa_sapling` | Kousa Tree ❆ | **Саженец кизила** | Дерево Кизил ❆ | DRIFT |
| `trees/atmospheric/laurel.json` | `atmospheric:laurel_sapling` | Laurel Tree 🌐 | **Саженец лавра** | Лавровое дерево 🌐 | DRIFT |
| `trees/atmospheric/morado.json` | `atmospheric:morado_sapling` | Morado Tree 🌐 | **Саженец морадо** | Morado Tree 🌐 | DRIFT |
| `trees/atmospheric/rosewood.json` | `atmospheric:rosewood_sapling` | Rosewood Tree 🌐 | **Саженец палисандра** | Палисандровое дерево 🌐 | DRIFT |
| `trees/atmospheric/yucca.json` | `atmospheric:yucca_sapling` | Yucca Tree 🌐 | **Саженец юкки** | Дерево юкки 🌐 | DRIFT |
| `trees/autumnity/maple.json` | `autumnity:maple_sapling` | Maple Tree 🌐 | **Саженец клёна** | Кленовое дерево 🌐 | DRIFT |
| `trees/autumnity/orange_maple.json` | `autumnity:orange_maple_sapling` | Orange Maple Tree 🌐 | **Саженец оранжевого клёна** | Оранжевый клён 🌐 | DRIFT |
| `trees/autumnity/red_maple.json` | `autumnity:red_maple_sapling` | Red Maple Tree 🌐 | **Саженец красного клёна** | Красный клён 🌐 | DRIFT |
| `trees/autumnity/yellow_maple.json` | `autumnity:yellow_maple_sapling` | Yellow Maple Tree 🌐 | **Саженец жёлтого клёна** | Жёлтый клён 🌐 | DRIFT |
| `trees/letsdo/apple.json` | `vinery:apple_tree_sapling` | Dark Apple Tree 🍂 | **Саженец яблони** | Тёмная яблоня 🍂 | DRIFT |
| `trees/letsdo/darkcherry.json` | `vinery:dark_cherry_sapling` | Darkcherry Tree 🌼 | **Саженец тёмной вишни** | Дерево тёмной вишни 🌼 | DRIFT |
| `trees/letsdo/palm.json` | `beachparty:palm_sapling` | Palm Tree 🔥 | **Саженец пальмы** | Пальма 🔥 | DRIFT |
| `trees/letsdo/pine.json` | `meadow:pine_sapling` | Pine Tree 🌐 | **Сосновый саженец** | Сосна 🌐 | DRIFT |
| `trees/pams/apple.json` | `pamhc2trees:apple_sapling` | Apple Tree 🍂 | **Саженец яблочного дерева** | Яблоня 🍂 | DRIFT |
| `trees/pams/banana.json` | `pamhc2trees:banana_sapling` | Banana Tree 🔥 | **Саженец бананового дерева** | Банановое дерево 🔥 | DRIFT |
| `trees/pams/cherry.json` | `pamhc2trees:cherry_sapling` | Cherry Tree 🌼 | **Саженец вишнёвого дерева** | Вишнёвое дерево 🌼 | DRIFT |
| `trees/pams/cinnamon.json` | `pamhc2trees:cinnamon_sapling` | Cinnamon Tree 🍂❆ | **Саженец коричного дерева** | Коричное дерево 🍂❆ | DRIFT |
| `trees/pams/dragonfruit.json` | `pamhc2trees:dragonfruit_sapling` | Dragonfruit Tree ❆ | **Саженец питахайевого дерева** | Дерево питахайи ❆ | DRIFT |
| `trees/pams/hazelnut.json` | `pamhc2trees:hazelnut_sapling` | Hazelnut Tree 🍂 | **Саженец фундучного дерева** | Фундуковое дерево 🍂 | DRIFT |
| `trees/pams/lemon.json` | `pamhc2trees:lemon_sapling` | Lemon Tree 🌼🔥 | **Саженец лимонного дерева** | Лимонное дерево 🌼🔥 | DRIFT |
| `trees/pams/lychee.json` | `pamhc2trees:lychee_sapling` | Lychee Tree 🌼 | **Саженец личиого дерева** | Личи 🌼 | DRIFT |
| `trees/pams/mango.json` | `pamhc2trees:mango_sapling` | Mango Tree 🔥 | **Саженец мангового дерева** | Манговое дерево 🔥 | DRIFT |
| `trees/pams/orange.json` | `pamhc2trees:apple_sapling` | Orange Tree 🔥 | **Саженец яблочного дерева** | Апельсиновое дерево 🔥 | DRIFT |
| `trees/pams/passionfruit.json` | `pamhc2trees:passionfruit_sapling` | Passionfruit Tree 🌼 | **Саженец маракуйевого дерева** | Дерево маракуйи 🌼 | DRIFT |
| `trees/pams/pawpaw.json` | `pamhc2trees:pawpaw_sapling` | Pawpaw Tree 🍂 | **Pawpaw Саженец** | Дерево азимины 🍂 | DRIFT |
| `trees/pams/peach.json` | `pamhc2trees:peach_sapling` | Peach Tree 🔥 | **Саженец персикового дерева** | Персиковое дерево 🔥 | DRIFT |
| `trees/pams/plum.json` | `pamhc2trees:plum_sapling` | Plum Tree 🍂 | **Саженец сливового дерева** | Сливовое дерево 🍂 | DRIFT |
| `trees/pams/starfruit.json` | `pamhc2trees:starfruit_sapling` | Starfruit Tree 🌐 | **Саженец дерева карамболы** | Дерево карамболы 🌐 | DRIFT |
| `trees/quark/ancient.json` | `quark:ancient_sapling` | Ashen Tree 🌐 | **Саженец древнего дерева** | Пепельное дерево 🌐 | DRIFT |
| `trees/quark/fiery_trumpet.json` | `quark:red_blossom_sapling` | Fiery Trumpet Tree 🌐 | **Саженец огненной табебуйи** | Огненное Трубное Дерево 🌐 | DRIFT |
| `trees/quark/frosty_trumpet.json` | `quark:blue_blossom_sapling` | Frosty Trumpet Tree 🌐 | **Саженец морозной табебуйи** | Морозное трубчатое дерево 🌐 | DRIFT |
| `trees/quark/serene_trumpet.json` | `quark:lavender_blossom_sapling` | Serene Trumpet Tree 🌐 | **Саженец безмятежной табебуйи** | Безмятежное Трубное Дерево 🌐 | DRIFT |
| `trees/quark/sunny_trumpet.json` | `quark:yellow_blossom_sapling` | Sunny Trumpet Tree 🌐 | **Саженец солнечной табебуйи** | Солнечное Трубное Дерево 🌐 | DRIFT |
| `trees/quark/warm_trumpet.json` | `quark:orange_blossom_sapling` | Warm Trumpet Tree 🌐 | **Саженец тёплой табебуйи** | Тёплое трубчатое дерево 🌐 | DRIFT |
| `trees/vanilla/acacia.json` | `minecraft:acacia_sapling` | Acacia Tree 🔥 | **Acacia Tree 🔥** | Акациевое дерево 🔥 | DRIFT |
| `trees/vanilla/birch.json` | `minecraft:birch_sapling` | Birch Tree 🌼🍂 | **Birch Tree 🌼🍂** | Берёза 🌼🍂 | DRIFT |
| `trees/vanilla/cherry.json` | `minecraft:cherry_sapling` | Cherry Tree 🌼 | **Cherry Tree 🌼** | Вишнёвое дерево 🌼 | DRIFT |
| `trees/vanilla/dark_oak.json` | `minecraft:oak_sapling` | Dark Oak Tree 🍂 | **Dark Oak Tree 🍂** | Тёмный дуб 🍂 | DRIFT |
| `trees/vanilla/jungle.json` | `minecraft:jungle_sapling` | Jungle Tree 🔥 | **Jungle Tree 🔥** | Дерево джунглей 🔥 | DRIFT |
| `trees/vanilla/oak.json` | `minecraft:oak_sapling` | Oak Tree 🌐 | **Oak Tree 🌐** | Дуб 🌐 | DRIFT |
| `trees/vanilla/spruce.json` | `minecraft:spruce_sapling` | Spruce Tree 🌼🍂❆ | **Spruce Tree 🌼🍂❆** | Ель 🌼🍂❆ | DRIFT |

## 4. Почему названия глав и категорий оставались на английском (3 конкретных примера)

### Пример 1: Название категории «Crops» (`categories/crops.json`)
* **Английское название:** `Crops`
* **Источник:** `patchouli_books/almanac/en_us/categories/crops.json` (`"name": "Crops"`)
* **Почему отображалось на английском:** В `patchouli_books/almanac/book.json` флаг `i18n` не установлен (`false`). Метод `BookCategory.getName()` вызывает `Component.literal(this.name)`. В исходной папке игры `G:\curseforge\minecraft\Instances\Society Sunlit Valley\patchouli_books\almanac\` папка `ru_ru` полностью отсутствовала, из-за чего игра брала fallback из `en_us`.
* **Где должен находиться русский перевод:** В `patchouli_books/almanac/ru_ru/categories/crops.json` (`"name": "Сельхозкультуры"`).
* **Что нужно сделать:** Разместить локализованный файл `crops.json` в `patchouli_books/almanac/ru_ru/categories/`.

### Пример 2: Статья сельскохозяйственной культуры «Corn 🔥🍂» (`entries/crops/corn.json`)
* **Английское название:** `Corn 🔥🍂`
* **Источник:** `patchouli_books/almanac/en_us/entries/crops/corn.json` (`"name": "Corn 🔥🍂"`)
* **Почему отображалось на английском:** Метод `BookEntry.getName()` возвращает литерал `Component.literal(this.name)`. Без наличия файла `patchouli_books/almanac/ru_ru/entries/crops/corn.json` загрузчик загружал английский файл. В старом же переводе Scriptora у других культур были устаревшие названия («Мерзкие ягоды 🍂» вместо актуального «Кислые ягоды 🍂»).
* **Где должен находиться русский перевод:** В `patchouli_books/almanac/ru_ru/entries/crops/corn.json` (`"name": "Кукуруза 🔥🍂"`).
* **Что нужно сделать:** Синхронизировать название статьи с реальным именем предмета в инвентаре (`farm_and_charm:corn` $\rightarrow$ «Кукуруза») и положить в `ru_ru/`.

### Пример 3: Статья животного «Bison» (`entries/animals/bison.json`)
* **Английское название:** `Bison`
* **Источник:** `patchouli_books/almanac/en_us/entries/animals/bison.json` (`"name": "Bison"`)
* **Почему отображалось на английском:** Поле `name` является литералом `"Bison"`. Иконка ссылается на `wildernature:bison_horn` (Рог бизона). Без русского JSON-файла игра выводила `"Bison"`, а в тексте характеристики дропа отображались как `"Drops: Bison Horn"` на английском.
* **Где должен находиться русский перевод:** В `patchouli_books/almanac/ru_ru/entries/animals/bison.json` (`"name": "Бизон"`, `"Добыча: Рог бизона"`).
* **Что нужно сделать:** Создать `ru_ru/entries/animals/bison.json` с полным переводом всех текстовых полей и добычи.

## 5. Классификация Evidence

* **`[FACT]` (Подтверждено кодом и файлами):**
  - Все 191 предмет и моб Альманаха имеют 100% подтверждённые переводы в `translations/mods/`, `game_data/` или ванильном Minecraft.
  - Механизм загрузки Patchouli 1.20.1 доказан декомпиляцией `BookContentExternalLoader.class` и `BookContentsBuilder.class`.
* **`[INFERENCE]` (Обоснованные выводы):**
  - Предыдущий переводчик не скопировал папку `patchouli_books/almanac/ru_ru` в корневой каталог игры, поэтому клиент Minecraft загружал дефолтный `en_us`.
* **`[UNKNOWN]`:**
  - 0 нераспознанных или неизвестных объектов.

## 6. Итоговая статистика

```text
Книга: patchouli:almanac

Категорий: 6
Глав: 191
Страниц: 386

Переведено категорий: 6
Не переведено категорий: 0

Переведено глав: 191
Не переведено глав: 0

Найдено объектов: 191
Объектов с актуальным RU: 191
Объектов со старым RU: 133
Объектов без RU: 0

Translation drift: 133
Unknown: 0
```

### Общий статус аудита:
**PASS**
