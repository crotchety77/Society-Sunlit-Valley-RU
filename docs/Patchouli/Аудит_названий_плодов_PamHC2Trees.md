# 🔎 Аудит и нормализация названий плодов Pam's HarvestCraft 2 Trees (`pamhc2trees`)

> **Статус документа:** Отчёт аудита (ReadOnly — без применения изменений в файлы)
> **Мод:** Pam's HarvestCraft 2 - Trees (`pamhc2trees-1.20-1.0.2.jar`)
> **Область аудита:** Все 57 предметов-плодов и продуктов мода, 50 саженцев, 50 растущих блоков плодов, статьи справочника Patchouli Almanac и кросс-модовые связи.

## 1. Резюме аудита

В ходе сплошного аудита файлов `pamhc2trees-1.20-1.0.2.jar`, `translations/mods/pamhc2trees.json`, `kubejs/assets/pamhc2trees/lang/ru_ru.json` и справочника `patchouli:almanac` установлено:
1. **Массовый пропуск локализации плодов (English Literals):** Из 57 предметов мода **56 предметов оставлены на английском языке** (`"Acorn"`, `"Banana"`, `"Plum"`, `"Lychee"`, `"Peach"`, `"Cinnamon"` и др.). Единственный переведённый плод — `"Карамбола"` (`starfruititem`).
2. **Машинный полуперевод блоков на деревьях:** Все 50 блоков созревания плодов `block.pamhc2trees.pam*` имеют сырые машинные названия вида `"Acorn Фрукт"`, `"Banana Фрукт"`, `"Plum Фрукт"`, `"Cinnamon Фрукт Бревно"`.
3. **Рассинхронизация с саженцами:** Большинство саженцев переведено (`"Саженец сливового дерева"`, `"Саженец бананового дерева"`), но сами плоды и блоки на деревьях разорваны по терминологии с саженцами.
4. **Рассинхронизация с Patchouli Almanac:** В главах `entries/tree_crops/` справочника фермера плоды отображаются английскими названиями (`Banana`, `Plum`, `Lychee`, `Dragonfruit`, `Peach`, `Pawpaw` и др.), тогда как деревья в `entries/trees/pams/` переведены на русский.

## 2. Полный реестр плодов и продуктов `pamhc2trees` (57 предметов)

| ID | English | Current RU | Культура / Саженец | Каноническое RU | Статус | Источник |
| :--- | :--- | :--- | :--- | :--- | :---: | :---: |
| `pamhc2trees:acornitem` | Acorn | `Acorn` | Acorn Саженец | **Жёлудь** | `DRIFT` | [FACT] |
| `pamhc2trees:almonditem` | Almond | `Almond` | Саженец миндального дерева | **Миндаль** | `DRIFT` | [FACT] |
| `pamhc2trees:appleitem` | Apple | `Apple` | Саженец яблочного дерева | **Яблоко** | `DRIFT` | [FACT] |
| `pamhc2trees:apricotitem` | Apricot | `Apricot` | Саженец абрикосового дерева | **Абрикос** | `DRIFT` | [FACT] |
| `pamhc2trees:avocadoitem` | Avocado | `Avocado` | Саженец авокадового дерева | **Авокадо** | `DRIFT` | [FACT] |
| `pamhc2trees:bananaitem` | Banana | `Banana` | Саженец бананового дерева | **Банан** | `DRIFT` | [FACT] |
| `pamhc2trees:breadfruititem` | Breadfruit | `Breadfruit` | Саженец хлебного дерева | **Хлебный плод** | `DRIFT` | [INFERENCE] |
| `pamhc2trees:candlenutitem` | Candlenut | `Candlenut` | Candlenut Саженец | **Свечной орех** | `CHOICE` | [INFERENCE] |
| `pamhc2trees:cashewitem` | Cashew | `Cashew` | Саженец кешьюого дерева | **Кешью** | `DRIFT` | [FACT] |
| `pamhc2trees:cherryitem` | Cherry | `Cherry` | Саженец вишнёвого дерева | **Вишня** | `DRIFT` | [FACT] |
| `pamhc2trees:chestnutitem` | Chestnut | `Chestnut` | Саженец каштанового дерева | **Каштан** | `DRIFT` | [FACT] |
| `pamhc2trees:cinnamonitem` | Cinnamon | `Cinnamon` | Саженец коричного дерева | **Корица** | `DRIFT` | [FACT] |
| `pamhc2trees:coconutitem` | Coconut | `Coconut` | Саженец кокосового дерева | **Кокос** | `DRIFT` | [FACT] |
| `pamhc2trees:dateitem` | Date | `Date` | Date Саженец | **Финик** | `DRIFT` | [FACT] |
| `pamhc2trees:dragonfruititem` | Dragonfruit | `Dragonfruit` | Саженец питахайевого дерева | **Питахайя** | `CHOICE` | [FACT] |
| `pamhc2trees:durianitem` | Durian | `Durian` | Саженец дурианового дерева | **Дуриан** | `DRIFT` | [FACT] |
| `pamhc2trees:figitem` | Fig | `Fig` | Саженец инжирного дерева | **Инжир** | `DRIFT` | [FACT] |
| `pamhc2trees:gooseberryitem` | Gooseberry | `Gooseberry` | Gooseberry Саженец | **Крыжовник** | `DRIFT` | [FACT] |
| `pamhc2trees:grapefruititem` | Grapefruit | `Grapefruit` | Саженец грейпфрутового дерева | **Грейпфрут** | `DRIFT` | [FACT] |
| `pamhc2trees:guavaitem` | Guava | `Guava` | Саженец гуавового дерева | **Гуава** | `DRIFT` | [FACT] |
| `pamhc2trees:hazelnutitem` | Hazelnut | `Hazelnut` | Саженец фундучного дерева | **Фундук** | `CHOICE` | [FACT] |
| `pamhc2trees:jackfruititem` | Jackfruit | `Jackfruit` | Саженец джекфрутового дерева | **Джекфрут** | `DRIFT` | [FACT] |
| `pamhc2trees:lemonitem` | Lemon | `Lemon` | Саженец лимонного дерева | **Лимон** | `DRIFT` | [FACT] |
| `pamhc2trees:limeitem` | Lime | `Lime` | Саженец лаймового дерева | **Лайм** | `DRIFT` | [FACT] |
| `pamhc2trees:lycheeitem` | Lychee | `Lychee` | Саженец личиого дерева | **Личи** | `DRIFT` | [FACT] |
| `pamhc2trees:mangoitem` | Mango | `Mango` | Саженец мангового дерева | **Манго** | `DRIFT` | [FACT] |
| `pamhc2trees:mapleitem` | Maple Syrup | `Maple Syrup` | Саженец кленового дерева | **Кленовый сироп** | `DRIFT` | [FACT] |
| `pamhc2trees:nutmegitem` | Nutmeg | `Nutmeg` | Саженец мускатного дерева | **Мускатный орех** | `DRIFT` | [FACT] |
| `pamhc2trees:oliveitem` | Olive | `Olive` | Olive Саженец | **Оливка** | `CHOICE` | [FACT] |
| `pamhc2trees:orangeitem` | Orange | `Orange` | Саженец апельсинового дерева | **Апельсин** | `DRIFT` | [FACT] |
| `pamhc2trees:papayaitem` | Papaya | `Papaya` | Саженец папайевого дерева | **Папайя** | `DRIFT` | [FACT] |
| `pamhc2trees:passionfruititem` | Passionfruit | `Passionfruit` | Саженец маракуйевого дерева | **Маракуйя** | `CHOICE` | [FACT] |
| `pamhc2trees:pawpawitem` | Pawpaw | `Pawpaw` | Pawpaw Саженец | **Азимина** | `CHOICE` | [INFERENCE] |
| `pamhc2trees:peachitem` | Peach | `Peach` | Саженец персикового дерева | **Персик** | `DRIFT` | [FACT] |
| `pamhc2trees:pearitem` | Pear | `Pear` | Саженец грушевого дерева | **Груша** | `DRIFT` | [FACT] |
| `pamhc2trees:pecanitem` | Pecan | `Pecan` | Саженец пеканового дерева | **Пекан** | `DRIFT` | [FACT] |
| `pamhc2trees:peppercornitem` | Peppercorn | `Peppercorn` | Саженец перечного дерева | **Горошина чёрного перца** | `CHOICE` | [INFERENCE] |
| `pamhc2trees:persimmonitem` | Persimmon | `Persimmon` | Саженец хурмового дерева | **Хурма** | `DRIFT` | [FACT] |
| `pamhc2trees:pinenutitem` | Pinenuts | `Pinenuts` | Pinenut Саженец | **Кедровые орехи** | `CHOICE` | [INFERENCE] |
| `pamhc2trees:pistachioitem` | Pistachio | `Pistachio` | Саженец фисташкового дерева | **Фисташка** | `CHOICE` | [FACT] |
| `pamhc2trees:plumitem` | Plum | `Plum` | Саженец сливового дерева | **Слива** | `DRIFT` | [FACT] |
| `pamhc2trees:pomegranateitem` | Pomegranate | `Pomegranate` | Саженец гранатового дерева | **Гранат** | `DRIFT` | [FACT] |
| `pamhc2trees:rambutanitem` | Rambutan | `Rambutan` | Саженец рамбутанового дерева | **Рамбутан** | `DRIFT` | [FACT] |
| `pamhc2trees:roastedacornitem` | Roasted Acorn | `Roasted Acorn` | Acorn Саженец | **Жареный жёлудь** | `DRIFT` | [INFERENCE] |
| `pamhc2trees:roastedalmonditem` | Roasted Almond | `Roasted Almond` | Саженец миндального дерева | **Жареный миндаль** | `DRIFT` | [INFERENCE] |
| `pamhc2trees:roastedcashewitem` | Roasted Cashew | `Roasted Cashew` | Саженец кешьюого дерева | **Жареный кешью** | `DRIFT` | [INFERENCE] |
| `pamhc2trees:roastedchestnutitem` | Roasted Chestnut | `Roasted Chestnut` | Саженец каштанового дерева | **Жареный каштан** | `DRIFT` | [INFERENCE] |
| `pamhc2trees:roastedhazelnutitem` | Roasted Hazelnut | `Roasted Hazelnut` | Саженец фундучного дерева | **Жареный фундук** | `DRIFT` | [INFERENCE] |
| `pamhc2trees:roastedpecanitem` | Roasted Pecan | `Roasted Pecan` | Саженец пеканового дерева | **Жареный пекан** | `DRIFT` | [INFERENCE] |
| `pamhc2trees:roastedpinenutitem` | Roasted Pinenuts | `Roasted Pinenuts` | Pinenut Саженец | **Жареные кедровые орехи** | `DRIFT` | [INFERENCE] |
| `pamhc2trees:roastedpistachioitem` | Roasted Pistachio | `Roasted Pistachio` | Саженец фисташкового дерева | **Жареные фисташки** | `DRIFT` | [INFERENCE] |
| `pamhc2trees:roastedwalnutitem` | Roasted Walnut | `Roasted Walnut` | Саженец орехового дерева | **Жареный грецкий орех** | `DRIFT` | [INFERENCE] |
| `pamhc2trees:soursopitem` | Soursop | `Soursop` | Soursop Саженец | **Саусеп** | `CHOICE` | [INFERENCE] |
| `pamhc2trees:starfruititem` | Starfruit | `Карамбола` | Саженец дерева карамболы | **Карамбола** | `PASS` | [FACT] |
| `pamhc2trees:tamarinditem` | Tamarind | `Tamarind` | Саженец тамариндового дерева | **Тамаринд** | `DRIFT` | [FACT] |
| `pamhc2trees:vanillabeanitem` | Vanillabean | `Vanillabean` | Саженец ванильного дерева | **Стручок ванили** | `CHOICE` | [FACT] |
| `pamhc2trees:walnutitem` | Walnut | `Walnut` | Саженец орехового дерева | **Грецкий орех** | `DRIFT` | [FACT] |

---

## 3. Источники истины и доказательная база

Классификация источников:
* **`[FACT]`** — Название подтверждено активными файлами сборки: существующими саженцами `pamhc2trees`, рецептами KubeJS, предметами других модов (`vinery`, `atmospheric`, `farmersdelight`, `candlelight`) или устоявшимся глоссарием сборки.
* **`[INFERENCE]`** — Русское название выведено на основе академической ботанической и кулинарной номенклатуры (например, `pawpaw` $\rightarrow$ *Азимина*, `candlenut` $\rightarrow$ *Свечной орех*, `roasted*` $\rightarrow$ *Жареный ...*).
* **`[UNKNOWN]`** — Недостоверные или неопределённые случаи (в данном аудите отсутствуют, все 57 культур идентифицированы).

## 4. Анализ вариантов выбора (`[CHOICE]`)

Для 10 культур зафиксированы варианты перевода, требующие эксплицитного выбора:

### `pamhc2trees:candlenutitem` (Candlenut)
* **Предлагаемый канон:** **Свечной орех**
* **Обоснование и альтернативы:** Выбор между «Свечной орех» (понятное бытовое название плода свечного дерева) и «Лумбанг» (ботаническое имя). Рекомендуется «Свечной орех».

### `pamhc2trees:dragonfruititem` (Dragonfruit)
* **Предлагаемый канон:** **Питахайя**
* **Обоснование и альтернативы:** Выбор между «Питахайя» (принято в глоссарии сборки) и калькой «Драконий фрукт». В глоссарии и KubeJS канонично «Питахайя».

### `pamhc2trees:hazelnutitem` (Hazelnut)
* **Предлагаемый канон:** **Фундук**
* **Обоснование и альтернативы:** Выбор между «Фундук» (кулинарный плод) и «Лесной орех» / «Орех лещины». В рецептах сборки традиционно «Фундук».

### `pamhc2trees:oliveitem` (Olive)
* **Предлагаемый канон:** **Оливка**
* **Обоснование и альтернативы:** Выбор между «Оливка» (как в Vinery) и «Маслина» / «Оливки». Для соответствия Vinery рекомендуется «Оливка».

### `pamhc2trees:passionfruititem` (Passionfruit)
* **Предлагаемый канон:** **Маракуйя**
* **Обоснование и альтернативы:** Саженец переведён буквально «дерева страсти» (калька с passion fruit), но плод в игре везде «Маракуйя».

### `pamhc2trees:pawpawitem` (Pawpaw)
* **Предлагаемый канон:** **Азимина**
* **Обоснование и альтернативы:** Выбор между ботаническим «Азимина» (или «Азимина трёхлопастная») и транслитерацией «Пау-пау» / «По-по». В русской ботанической традиции плод называется «Азимина» («северный банан»).

### `pamhc2trees:peppercornitem` (Peppercorn)
* **Предлагаемый канон:** **Горошина чёрного перца**
* **Обоснование и альтернативы:** Выбор между «Горошина чёрного перца», «Чёрный перец (горошек)» и «Перечный горошек». Рекомендуется «Горошина чёрного перца».

### `pamhc2trees:pinenutitem` (Pinenuts)
* **Предлагаемый канон:** **Кедровые орехи**
* **Обоснование и альтернативы:** Выбор между «Кедровый орех» (ед.ч.) и «Кедровые орехи» (мн.ч., так как в EN Pinenuts). В кулинарии и обиходе чаще «Кедровые орехи».

### `pamhc2trees:pistachioitem` (Pistachio)
* **Предлагаемый канон:** **Фисташка**
* **Обоснование и альтернативы:** Выбор между ед.ч. «Фисташка» и мн.ч. «Фисташки». В сборке принято ед.ч. «Фисташка».

### `pamhc2trees:soursopitem` (Soursop)
* **Предлагаемый канон:** **Саусеп**
* **Обоснование и альтернативы:** Выбор между кулинарно-торговым «Саусеп» и ботаническим «Сметанное яблоко». В кулинарии и напитках наиболее известен как «Саусеп».

### `pamhc2trees:vanillabeanitem` (Vanillabean)
* **Предлагаемый канон:** **Стручок ванили**
* **Обоснование и альтернативы:** Выбор между «Стручок ванили» и «Ванильный стручок» / «Ваниль». Рекомендуется «Стручок ванили» как точное обозначение предмета-стручка.

---

## 5. Проверка терминологии и структуры названий

При аудите строго соблюдены правила предметной дифференциации:
1. **Плод vs Дерево/Растение:** Предмет обозначает сам плод/орех/продукт, а не порождающее дерево (например, `plumitem` $\rightarrow$ **Слива**, а не *«Сливовое дерево»*; `bananaitem` $\rightarrow$ **Банан**, а не *«Банановое дерево»*).
2. **Плод vs Семя/Саженец:** Саженец остаётся `«Саженец ...»`, плод — именительный падеж плода.
3. **Недревесные/смоляные продукты:** `mapleitem` является сиропом сока клёна $\rightarrow$ **Кленовый сироп**; `cinnamonitem` является пряностью из коры $\rightarrow$ **Корица**; `vanillabeanitem` является стручком $\rightarrow$ **Стручок ванили**.
4. **Сырые vs Жареные орехи:** 9 видов жареных орехов `roasted*item` согласованы по роду и числу: *Жареный миндаль*, *Жареный кешью*, *Жареный каштан*, *Жареный фундук*, *Жареный пекан*, *Жареный грецкий орех*, *Жареный жёлудь*, *Жареные кедровые орехи*, *Жареные фисташки*.

## 6. Проверка согласованности цепочек (Tree $\rightarrow$ Fruit Block $\rightarrow$ Fruit Item $\rightarrow$ Patchouli)

| Культура | Саженец (`block..._sapling`) | Блок на дереве (`block...pam*`) | Текущий плод (`item...`) | Канонический плод | Patchouli Almanac |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Acorn | `Acorn Саженец` | `Acorn Фрукт` | `Acorn` | **Жёлудь** | — |
| Almond | `Саженец миндального дерева` | `Almond Фрукт` | `Almond` | **Миндаль** | — |
| Apple | `Саженец яблочного дерева` | `Apple Фрукт` | `Apple` | **Яблоко** | Яблоко / Яблоня |
| Apricot | `Саженец абрикосового дерева` | `Apricot Фрукт` | `Apricot` | **Абрикос** | — |
| Avocado | `Саженец авокадового дерева` | `Avocado Фрукт` | `Avocado` | **Авокадо** | — |
| Banana | `Саженец бананового дерева` | `Banana Фрукт` | `Banana` | **Банан** | Banana / Банановое дерево |
| Breadfruit | `Саженец хлебного дерева` | `Breadfruit Фрукт` | `Breadfruit` | **Хлебный плод** | — |
| Candlenut | `Candlenut Саженец` | `Candlenut Фрукт` | `Candlenut` | **Свечной орех** | — |
| Cashew | `Саженец кешьюого дерева` | `Cashew Фрукт` | `Cashew` | **Кешью** | — |
| Cherry | `Саженец вишнёвого дерева` | `Cherry Фрукт` | `Cherry` | **Вишня** | — |
| Chestnut | `Саженец каштанового дерева` | `Chestnut Фрукт` | `Chestnut` | **Каштан** | — |
| Cinnamon | `Саженец коричного дерева` | `Cinnamon Фрукт Бревно` | `Cinnamon` | **Корица** | Cinnamon / Коричное дерево |
| Coconut | `Саженец кокосового дерева` | `Coconut Фрукт` | `Coconut` | **Кокос** | — |
| Date | `Date Саженец` | `Date Фрукт` | `Date` | **Финик** | — |
| Dragonfruit | `Саженец питахайевого дерева` | `Dragonfruit Фрукт` | `Dragonfruit` | **Питахайя** | Dragonfruit / Драконье дерево |
| Durian | `Саженец дурианового дерева` | `Durian Фрукт` | `Durian` | **Дуриан** | — |
| Fig | `Саженец инжирного дерева` | `Fig Фрукт` | `Fig` | **Инжир** | — |
| Gooseberry | `Gooseberry Саженец` | `Gooseberry Фрукт` | `Gooseberry` | **Крыжовник** | — |
| Grapefruit | `Саженец грейпфрутового дерева` | `Grapefruit Фрукт` | `Grapefruit` | **Грейпфрут** | — |
| Guava | `Саженец гуавового дерева` | `Guava Фрукт` | `Guava` | **Гуава** | — |
| Hazelnut | `Саженец фундучного дерева` | `Hazelnut Фрукт` | `Hazelnut` | **Фундук** | Hazelnut / Орешник |
| Jackfruit | `Саженец джекфрутового дерева` | `Jackfruit Фрукт` | `Jackfruit` | **Джекфрут** | — |
| Lemon | `Саженец лимонного дерева` | `Lemon Фрукт` | `Lemon` | **Лимон** | Lemon / Лимонное дерево |
| Lime | `Саженец лаймового дерева` | `Lime Фрукт` | `Lime` | **Лайм** | — |
| Lychee | `Саженец личиого дерева` | `Lychee Фрукт` | `Lychee` | **Личи** | Lychee / Дерево личи |
| Mango | `Саженец мангового дерева` | `Mango Фрукт` | `Mango` | **Манго** | Mango / Дерево манго |
| Maple Syrup | `Саженец кленового дерева` | `Maple Фрукт Бревно` | `Maple Syrup` | **Кленовый сироп** | — |
| Nutmeg | `Саженец мускатного дерева` | `Nutmeg Фрукт` | `Nutmeg` | **Мускатный орех** | — |
| Olive | `Olive Саженец` | `Olive Фрукт` | `Olive` | **Оливка** | — |
| Orange | `Саженец апельсинового дерева` | `Orange Фрукт` | `Orange` | **Апельсин** | Апельсин / Апельсиновое дерево |
| Papaya | `Саженец папайевого дерева` | `Papaya Фрукт` | `Papaya` | **Папайя** | — |
| Passionfruit | `Саженец маракуйевого дерева` | `Passionfruit Фрукт` | `Passionfruit` | **Маракуйя** | Маракуйя / Дерево страсти |
| Pawpaw | `Pawpaw Саженец` | `Pawpaw Фрукт` | `Pawpaw` | **Азимина** | Pawpaw / Pawpaw дерево |
| Peach | `Саженец персикового дерева` | `Peach Фрукт` | `Peach` | **Персик** | Peach / Персиковое дерево |
| Pear | `Саженец грушевого дерева` | `Pear Фрукт` | `Pear` | **Груша** | — |
| Pecan | `Саженец пеканового дерева` | `Pecan Фрукт` | `Pecan` | **Пекан** | — |
| Peppercorn | `Саженец перечного дерева` | `Peppercorn Фрукт` | `Peppercorn` | **Горошина чёрного перца** | — |
| Persimmon | `Саженец хурмового дерева` | `Persimmon Фрукт` | `Persimmon` | **Хурма** | — |
| Pinenuts | `Pinenut Саженец` | `Pinenut Фрукт` | `Pinenuts` | **Кедровые орехи** | — |
| Pistachio | `Саженец фисташкового дерева` | `Pistachio Фрукт` | `Pistachio` | **Фисташка** | — |
| Plum | `Саженец сливового дерева` | `Plum Фрукт` | `Plum` | **Слива** | Plum / Сливовое дерево |
| Pomegranate | `Саженец гранатового дерева` | `Pomegranate Фрукт` | `Pomegranate` | **Гранат** | — |
| Rambutan | `Саженец рамбутанового дерева` | `Rambutan Фрукт` | `Rambutan` | **Рамбутан** | — |
| Soursop | `Soursop Саженец` | `Soursop Фрукт` | `Soursop` | **Саусеп** | — |
| Starfruit | `Саженец дерева карамболы` | `Starfruit Фрукт` | `Карамбола` | **Карамбола** | Карамбола / Дерево карамболы |
| Tamarind | `Саженец тамариндового дерева` | `Tamarind Фрукт` | `Tamarind` | **Тамаринд** | — |
| Vanillabean | `Саженец ванильного дерева` | `Vanillabean Фрукт` | `Vanillabean` | **Стручок ванили** | — |
| Walnut | `Саженец орехового дерева` | `Walnut Фрукт` | `Walnut` | **Грецкий орех** | — |

---

## 7. Реестр старых и английских переводов

| ID | Старое RU | Предлагаемое RU | Причина | Confidence |
| :--- | :--- | :--- | :--- | :---: |
| `pamhc2trees:acornitem` | `Acorn` | **Жёлудь** | В KubeJS и Minecraft плод дуба традиционно «Жёлудь». Текущий саженец «Acorn Саженец», блок «Acorn Фрукт». | HIGH |
| `pamhc2trees:almonditem` | `Almond` | **Миндаль** | Саженец переведён как «Саженец миндального дерева». Плод оставлен «Almond». Блок «Almond Фрукт». | HIGH |
| `pamhc2trees:appleitem` | `Apple` | **Яблоко** | Ванильный и канонический плод «Яблоко». В pamhc2trees оставлен английский литерал «Apple». Саженец — «Саженец яблони». | HIGH |
| `pamhc2trees:apricotitem` | `Apricot` | **Абрикос** | Саженец «Саженец абрикосового дерева». Плод «Apricot». Блок «Apricot Фрукт». | HIGH |
| `pamhc2trees:avocadoitem` | `Avocado` | **Авокадо** | Саженец «Саженец авокадо». Плод «Avocado». Блок «Avocado Фрукт». | HIGH |
| `pamhc2trees:bananaitem` | `Banana` | **Банан** | Саженец «Саженец бананового дерева». Плод «Banana». В Almanac глава «Banana». Блок «Banana Фрукт». | HIGH |
| `pamhc2trees:breadfruititem` | `Breadfruit` | **Хлебный плод** | Саженец «Саженец хлебного дерева». Плод Artocarpus altilis по-русски — «Хлебный плод» (или «Плод хлебного дерева»). Плод оставлен «Breadfruit». | HIGH |
| `pamhc2trees:candlenutitem` | `Candlenut` | **Свечной орех** | Aleurites moluccanus (лумбанг / кукуи / свечное дерево). Саженец «Candlenut Саженец». Плод «Candlenut». | HIGH |
| `pamhc2trees:cashewitem` | `Cashew` | **Кешью** | Саженец «Саженец дерева кешью». Плод «Cashew». Блок «Cashew Фрукт». | HIGH |
| `pamhc2trees:cherryitem` | `Cherry` | **Вишня** | Саженец «Саженец вишневого дерева». Плод «Cherry». В Vinery и ванилле «Вишня». | HIGH |
| `pamhc2trees:chestnutitem` | `Chestnut` | **Каштан** | Саженец «Саженец каштанового дерева». Плод «Chestnut». Блок «Chestnut Фрукт». | HIGH |
| `pamhc2trees:cinnamonitem` | `Cinnamon` | **Корица** | Саженец «Саженец коричного дерева». Плод «Cinnamon». В Almanac «Cinnamon». Блок «Cinnamon Фрукт Бревно». | HIGH |
| `pamhc2trees:coconutitem` | `Coconut` | **Кокос** | Саженец «Саженец кокосовой пальмы». Плод «Coconut». Блок «Coconut Фрукт». В Beachparty «Кокос». | HIGH |
| `pamhc2trees:dateitem` | `Date` | **Финик** | Саженец «Date Саженец». Плод «Date». Блок «Date Фрукт». Плод финиковой пальмы — «Финик». | HIGH |
| `pamhc2trees:dragonfruititem` | `Dragonfruit` | **Питахайя** | Саженец «Саженец драконьего дерева». Плод «Dragonfruit». В Almanac «Dragonfruit». В сборке используется как «Питахайя». | HIGH |
| `pamhc2trees:durianitem` | `Durian` | **Дуриан** | Саженец «Саженец дурианового дерева». Плод «Durian». Блок «Durian Фрукт». | HIGH |
| `pamhc2trees:figitem` | `Fig` | **Инжир** | Саженец «Саженец инжирного дерева». Плод «Fig». Блок «Fig Фрукт». В Vinery «Инжир». | HIGH |
| `pamhc2trees:gooseberryitem` | `Gooseberry` | **Крыжовник** | Саженец «Gooseberry Саженец». Плод «Gooseberry». Общеупотребительное русское — «Крыжовник». | HIGH |
| `pamhc2trees:grapefruititem` | `Grapefruit` | **Грейпфрут** | Саженец «Саженец грейпфрутового дерева». Плод «Grapefruit». Блок «Grapefruit Фрукт». | HIGH |
| `pamhc2trees:guavaitem` | `Guava` | **Гуава** | Саженец «Саженец дерева гуавы». Плод «Guava». Блок «Guava Фрукт». | HIGH |
| `pamhc2trees:hazelnutitem` | `Hazelnut` | **Фундук** | Саженец «Саженец орешника». Плод «Hazelnut». В Almanac «Hazelnut». | HIGH |
| `pamhc2trees:jackfruititem` | `Jackfruit` | **Джекфрут** | Саженец «Саженец дерева джекфрут». Плод «Jackfruit». Блок «Jackfruit Фрукт». | HIGH |
| `pamhc2trees:lemonitem` | `Lemon` | **Лимон** | Саженец «Саженец лимонного дерева». Плод «Lemon». В Almanac «Lemon». | HIGH |
| `pamhc2trees:limeitem` | `Lime` | **Лайм** | Саженец «Саженец дерева лайма». Плод «Lime». Блок «Lime Фрукт». | HIGH |
| `pamhc2trees:lycheeitem` | `Lychee` | **Личи** | Саженец «Саженец дерева личи». Плод «Lychee». В Almanac «Lychee». Блок «Lychee Фрукт». | HIGH |
| `pamhc2trees:mangoitem` | `Mango` | **Манго** | Саженец «Саженец дерева манго». Плод «Mango». В Almanac «Mango». | HIGH |
| `pamhc2trees:mapleitem` | `Maple Syrup` | **Кленовый сироп** | Саженец «Саженец клена». Предмет «Maple Syrup» (сок/сироп клена). Текущее в RU «Maple Syrup». Блок «Maple Фрукт Бревно». | HIGH |
| `pamhc2trees:nutmegitem` | `Nutmeg` | **Мускатный орех** | Саженец «Саженец мускатного дерева». Плод «Nutmeg». Блок «Nutmeg Фрукт». | HIGH |
| `pamhc2trees:oliveitem` | `Olive` | **Оливка** | Саженец «Olive Саженец». Плод «Olive». В Vinery «Оливка». Блок «Olive Фрукт». | HIGH |
| `pamhc2trees:orangeitem` | `Orange` | **Апельсин** | Саженец «Саженец апельсинового дерева». Плод «Orange». В Atmospheric «Апельсин». | HIGH |
| `pamhc2trees:papayaitem` | `Papaya` | **Папайя** | Саженец «Саженец папайи». Плод «Papaya». Блок «Papaya Фрукт». | HIGH |
| `pamhc2trees:passionfruititem` | `Passionfruit` | **Маракуйя** | Саженец «Саженец дерева страсти». Плод «Passionfruit». В Atmospheric «Маракуйя» (atmospheric:passion_fruit). | HIGH |
| `pamhc2trees:pawpawitem` | `Pawpaw` | **Азимина** | Asimina triloba (Pawpaw). Саженец «Pawpaw Саженец». Плод «Pawpaw». В Almanac «Pawpaw». | HIGH |
| `pamhc2trees:peachitem` | `Peach` | **Персик** | Саженец «Саженец персикового дерева». Плод «Peach». В Almanac «Peach». | HIGH |
| `pamhc2trees:pearitem` | `Pear` | **Груша** | Саженец «Саженец грушевого дерева». Плод «Pear». Блок «Pear Фрукт». | HIGH |
| `pamhc2trees:pecanitem` | `Pecan` | **Пекан** | Саженец «Саженец дерева пекан». Плод «Pecan». Блок «Pecan Фрукт». | HIGH |
| `pamhc2trees:peppercornitem` | `Peppercorn` | **Горошина чёрного перца** | Саженец «Саженец перечного дерева». Плод «Peppercorn». Блок «Peppercorn Фрукт Бревно». | HIGH |
| `pamhc2trees:persimmonitem` | `Persimmon` | **Хурма** | Саженец «Саженец хурмы». Плод «Persimmon». Блок «Persimmon Фрукт». | HIGH |
| `pamhc2trees:pinenutitem` | `Pinenuts` | **Кедровые орехи** | Саженец «Pinenut Саженец». Плод «Pinenuts». | HIGH |
| `pamhc2trees:pistachioitem` | `Pistachio` | **Фисташка** | Саженец «Саженец фисташкового дерева». Плод «Pistachio». Блок «Pistachio Фрукт». | HIGH |
| `pamhc2trees:plumitem` | `Plum` | **Слива** | Саженец «Саженец сливового дерева». Плод «Plum». В Almanac «Plum». | HIGH |
| `pamhc2trees:pomegranateitem` | `Pomegranate` | **Гранат** | Саженец «Саженец гранатового дерева». Плод «Pomegranate». Блок «Pomegranate Фрукт». | HIGH |
| `pamhc2trees:rambutanitem` | `Rambutan` | **Рамбутан** | Саженец «Саженец дерева рамбутан». Плод «Rambutan». Блок «Rambutan Фрукт». | HIGH |
| `pamhc2trees:roastedacornitem` | `Roasted Acorn` | **Жареный жёлудь** | В EN «Roasted Acorn». В текущем RU оставлен «Roasted Acorn». Производный продукт от Acorn. | HIGH |
| `pamhc2trees:roastedalmonditem` | `Roasted Almond` | **Жареный миндаль** | В EN «Roasted Almond». В текущем RU оставлен «Roasted Almond». | HIGH |
| `pamhc2trees:roastedcashewitem` | `Roasted Cashew` | **Жареный кешью** | В EN «Roasted Cashew». В текущем RU оставлен «Roasted Cashew». | HIGH |
| `pamhc2trees:roastedchestnutitem` | `Roasted Chestnut` | **Жареный каштан** | В EN «Roasted Chestnut». В текущем RU оставлен «Roasted Chestnut». | HIGH |
| `pamhc2trees:roastedhazelnutitem` | `Roasted Hazelnut` | **Жареный фундук** | В EN «Roasted Hazelnut». В текущем RU оставлен «Roasted Hazelnut». | HIGH |
| `pamhc2trees:roastedpecanitem` | `Roasted Pecan` | **Жареный пекан** | В EN «Roasted Pecan». В текущем RU оставлен «Roasted Pecan». | HIGH |
| `pamhc2trees:roastedpinenutitem` | `Roasted Pinenuts` | **Жареные кедровые орехи** | В EN «Roasted Pinenuts». В текущем RU оставлен «Roasted Pinenuts». | HIGH |
| `pamhc2trees:roastedpistachioitem` | `Roasted Pistachio` | **Жареные фисташки** | В EN «Roasted Pistachio». В текущем RU оставлен «Roasted Pistachio». | HIGH |
| `pamhc2trees:roastedwalnutitem` | `Roasted Walnut` | **Жареный грецкий орех** | В EN «Roasted Walnut». В текущем RU оставлен «Roasted Walnut». | HIGH |
| `pamhc2trees:soursopitem` | `Soursop` | **Саусеп** | Annona muricata (Soursop / сметанное яблоко / гравиола / саусеп). Саженец «Soursop Саженец». Плод «Soursop». | HIGH |
| `pamhc2trees:tamarinditem` | `Tamarind` | **Тамаринд** | Саженец «Саженец тамариндового дерева». Плод «Tamarind». Блок «Tamarind Фрукт». | HIGH |
| `pamhc2trees:vanillabeanitem` | `Vanillabean` | **Стручок ванили** | Саженец «Саженец ванильного дерева». Плод «Vanillabean». Блок «Vanillabean Фрукт Бревно». | HIGH |
| `pamhc2trees:walnutitem` | `Walnut` | **Грецкий орех** | Саженец «Саженец грецкого ореха». Плод «Walnut». Блок «Walnut Фрукт». | HIGH |

---

## 8. Аудит расхождений со справочником Patchouli Almanac

В справочнике `patchouli:almanac` обнаружены следующие прямые расхождения между главами плодов (`tree_crops`) и главами деревьев (`trees/pams`):

| Плод ID | Файл главы плода | Текущий заголовок плода | Файл главы дерева | Текущий заголовок дерева | Требуемое исправление |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `pamhc2trees:appleitem` | `entries/tree_crops/apple.json` | `Яблоко` | `entries/trees/pams/apple.json` | `Яблоня` | Заголовок плода $\rightarrow$ **Яблоко** |
| `pamhc2trees:bananaitem` | `entries/tree_crops/banana.json` | `Banana` | `entries/trees/pams/banana.json` | `Банановое дерево` | Заголовок плода $\rightarrow$ **Банан** |
| `pamhc2trees:cinnamonitem` | `entries/tree_crops/cinnamon.json` | `Cinnamon` | `entries/trees/pams/cinnamon.json` | `Коричное дерево` | Заголовок плода $\rightarrow$ **Корица** |
| `pamhc2trees:dragonfruititem` | `entries/tree_crops/dragonfruit.json` | `Dragonfruit` | `entries/trees/pams/dragonfruit.json` | `Драконье дерево` | Заголовок плода $\rightarrow$ **Питахайя** |
| `pamhc2trees:hazelnutitem` | `entries/tree_crops/hazelnut.json` | `Hazelnut` | `entries/trees/pams/hazelnut.json` | `Орешник` | Заголовок плода $\rightarrow$ **Фундук** |
| `pamhc2trees:lemonitem` | `entries/tree_crops/lemon.json` | `Lemon` | `entries/trees/pams/lemon.json` | `Лимонное дерево` | Заголовок плода $\rightarrow$ **Лимон** |
| `pamhc2trees:lycheeitem` | `entries/tree_crops/lychee.json` | `Lychee` | `entries/trees/pams/lychee.json` | `Дерево личи` | Заголовок плода $\rightarrow$ **Личи** |
| `pamhc2trees:mangoitem` | `entries/tree_crops/mango.json` | `Mango` | `entries/trees/pams/mango.json` | `Дерево манго` | Заголовок плода $\rightarrow$ **Манго** |
| `pamhc2trees:orangeitem` | `entries/tree_crops/orange.json` | `Апельсин` | `entries/trees/pams/orange.json` | `Апельсиновое дерево` | Заголовок плода $\rightarrow$ **Апельсин** |
| `pamhc2trees:passionfruititem` | `entries/tree_crops/passionfruit.json` | `Маракуйя` | `entries/trees/pams/passionfruit.json` | `Дерево страсти` | Заголовок плода $\rightarrow$ **Маракуйя** |
| `pamhc2trees:pawpawitem` | `entries/tree_crops/pawpaw.json` | `Pawpaw` | `entries/trees/pams/pawpaw.json` | `Pawpaw дерево` | Заголовок плода $\rightarrow$ **Азимина** |
| `pamhc2trees:peachitem` | `entries/tree_crops/peach.json` | `Peach` | `entries/trees/pams/peach.json` | `Персиковое дерево` | Заголовок плода $\rightarrow$ **Персик** |
| `pamhc2trees:plumitem` | `entries/tree_crops/plum.json` | `Plum` | `entries/trees/pams/plum.json` | `Сливовое дерево` | Заголовок плода $\rightarrow$ **Слива** |
| `pamhc2trees:starfruititem` | `entries/tree_crops/starfruit.json` | `Карамбола` | `entries/trees/pams/starfruit.json` | `Дерево карамболы` | Заголовок плода $\rightarrow$ **Карамбола** |

---

## 9. Итоговая статистика аудита

```text
Всего плодов и продуктов: 57
PASS: 1
DRIFT: 46
CHOICE: 10
UNKNOWN: 0

Найдено старых/английских названий предметов: 56
Найдено машинных названий блоков созревания на деревьях: 50
Найдено несогласованных саженцев (с префиксом/латиницей): 8
Найдено прямых расхождений в Patchouli Almanac: 14
```

## 10. Рекомендованные изменения

> ⚠️ **Внимание:** Изменения не применены автоматически и представлены исключительно для проверки и утверждения.

### `pamhc2trees:acornitem`
* **Текущее:** `Acorn`
* **Рекомендуется:** **Жёлудь**
* **Причина:** В KubeJS и Minecraft плод дуба традиционно «Жёлудь». Текущий саженец «Acorn Саженец», блок «Acorn Фрукт».
* **Evidence:** [FACT]
* **Confidence:** HIGH

### `pamhc2trees:almonditem`
* **Текущее:** `Almond`
* **Рекомендуется:** **Миндаль**
* **Причина:** Саженец переведён как «Саженец миндального дерева». Плод оставлен «Almond». Блок «Almond Фрукт».
* **Evidence:** [FACT]
* **Confidence:** HIGH

### `pamhc2trees:appleitem`
* **Текущее:** `Apple`
* **Рекомендуется:** **Яблоко**
* **Причина:** Ванильный и канонический плод «Яблоко». В pamhc2trees оставлен английский литерал «Apple». Саженец — «Саженец яблони».
* **Evidence:** [FACT]
* **Confidence:** HIGH

### `pamhc2trees:apricotitem`
* **Текущее:** `Apricot`
* **Рекомендуется:** **Абрикос**
* **Причина:** Саженец «Саженец абрикосового дерева». Плод «Apricot». Блок «Apricot Фрукт».
* **Evidence:** [FACT]
* **Confidence:** HIGH

### `pamhc2trees:avocadoitem`
* **Текущее:** `Avocado`
* **Рекомендуется:** **Авокадо**
* **Причина:** Саженец «Саженец авокадо». Плод «Avocado». Блок «Avocado Фрукт».
* **Evidence:** [FACT]
* **Confidence:** HIGH

### `pamhc2trees:bananaitem`
* **Текущее:** `Banana`
* **Рекомендуется:** **Банан**
* **Причина:** Саженец «Саженец бананового дерева». Плод «Banana». В Almanac глава «Banana». Блок «Banana Фрукт».
* **Evidence:** [FACT]
* **Confidence:** HIGH

### `pamhc2trees:breadfruititem`
* **Текущее:** `Breadfruit`
* **Рекомендуется:** **Хлебный плод**
* **Причина:** Саженец «Саженец хлебного дерева». Плод Artocarpus altilis по-русски — «Хлебный плод» (или «Плод хлебного дерева»). Плод оставлен «Breadfruit».
* **Evidence:** [INFERENCE]
* **Confidence:** HIGH

### `pamhc2trees:candlenutitem`
* **Текущее:** `Candlenut`
* **Рекомендуется:** **Свечной орех**
* **Причина:** Aleurites moluccanus (лумбанг / кукуи / свечное дерево). Саженец «Candlenut Саженец». Плод «Candlenut».
* **Evidence:** [INFERENCE]
* **Confidence:** HIGH

### `pamhc2trees:cashewitem`
* **Текущее:** `Cashew`
* **Рекомендуется:** **Кешью**
* **Причина:** Саженец «Саженец дерева кешью». Плод «Cashew». Блок «Cashew Фрукт».
* **Evidence:** [FACT]
* **Confidence:** HIGH

### `pamhc2trees:cherryitem`
* **Текущее:** `Cherry`
* **Рекомендуется:** **Вишня**
* **Причина:** Саженец «Саженец вишневого дерева». Плод «Cherry». В Vinery и ванилле «Вишня».
* **Evidence:** [FACT]
* **Confidence:** HIGH

### `pamhc2trees:chestnutitem`
* **Текущее:** `Chestnut`
* **Рекомендуется:** **Каштан**
* **Причина:** Саженец «Саженец каштанового дерева». Плод «Chestnut». Блок «Chestnut Фрукт».
* **Evidence:** [FACT]
* **Confidence:** HIGH

### `pamhc2trees:cinnamonitem`
* **Текущее:** `Cinnamon`
* **Рекомендуется:** **Корица**
* **Причина:** Саженец «Саженец коричного дерева». Плод «Cinnamon». В Almanac «Cinnamon». Блок «Cinnamon Фрукт Бревно».
* **Evidence:** [FACT]
* **Confidence:** HIGH

### `pamhc2trees:coconutitem`
* **Текущее:** `Coconut`
* **Рекомендуется:** **Кокос**
* **Причина:** Саженец «Саженец кокосовой пальмы». Плод «Coconut». Блок «Coconut Фрукт». В Beachparty «Кокос».
* **Evidence:** [FACT]
* **Confidence:** HIGH

### `pamhc2trees:dateitem`
* **Текущее:** `Date`
* **Рекомендуется:** **Финик**
* **Причина:** Саженец «Date Саженец». Плод «Date». Блок «Date Фрукт». Плод финиковой пальмы — «Финик».
* **Evidence:** [FACT]
* **Confidence:** HIGH

### `pamhc2trees:dragonfruititem`
* **Текущее:** `Dragonfruit`
* **Рекомендуется:** **Питахайя**
* **Причина:** Саженец «Саженец драконьего дерева». Плод «Dragonfruit». В Almanac «Dragonfruit». В сборке используется как «Питахайя».
* **Evidence:** [FACT]
* **Confidence:** HIGH

### `pamhc2trees:durianitem`
* **Текущее:** `Durian`
* **Рекомендуется:** **Дуриан**
* **Причина:** Саженец «Саженец дурианового дерева». Плод «Durian». Блок «Durian Фрукт».
* **Evidence:** [FACT]
* **Confidence:** HIGH

### `pamhc2trees:figitem`
* **Текущее:** `Fig`
* **Рекомендуется:** **Инжир**
* **Причина:** Саженец «Саженец инжирного дерева». Плод «Fig». Блок «Fig Фрукт». В Vinery «Инжир».
* **Evidence:** [FACT]
* **Confidence:** HIGH

### `pamhc2trees:gooseberryitem`
* **Текущее:** `Gooseberry`
* **Рекомендуется:** **Крыжовник**
* **Причина:** Саженец «Gooseberry Саженец». Плод «Gooseberry». Общеупотребительное русское — «Крыжовник».
* **Evidence:** [FACT]
* **Confidence:** HIGH

### `pamhc2trees:grapefruititem`
* **Текущее:** `Grapefruit`
* **Рекомендуется:** **Грейпфрут**
* **Причина:** Саженец «Саженец грейпфрутового дерева». Плод «Grapefruit». Блок «Grapefruit Фрукт».
* **Evidence:** [FACT]
* **Confidence:** HIGH

### `pamhc2trees:guavaitem`
* **Текущее:** `Guava`
* **Рекомендуется:** **Гуава**
* **Причина:** Саженец «Саженец дерева гуавы». Плод «Guava». Блок «Guava Фрукт».
* **Evidence:** [FACT]
* **Confidence:** HIGH

### `pamhc2trees:hazelnutitem`
* **Текущее:** `Hazelnut`
* **Рекомендуется:** **Фундук**
* **Причина:** Саженец «Саженец орешника». Плод «Hazelnut». В Almanac «Hazelnut».
* **Evidence:** [FACT]
* **Confidence:** HIGH

### `pamhc2trees:jackfruititem`
* **Текущее:** `Jackfruit`
* **Рекомендуется:** **Джекфрут**
* **Причина:** Саженец «Саженец дерева джекфрут». Плод «Jackfruit». Блок «Jackfruit Фрукт».
* **Evidence:** [FACT]
* **Confidence:** HIGH

### `pamhc2trees:lemonitem`
* **Текущее:** `Lemon`
* **Рекомендуется:** **Лимон**
* **Причина:** Саженец «Саженец лимонного дерева». Плод «Lemon». В Almanac «Lemon».
* **Evidence:** [FACT]
* **Confidence:** HIGH

### `pamhc2trees:limeitem`
* **Текущее:** `Lime`
* **Рекомендуется:** **Лайм**
* **Причина:** Саженец «Саженец дерева лайма». Плод «Lime». Блок «Lime Фрукт».
* **Evidence:** [FACT]
* **Confidence:** HIGH

### `pamhc2trees:lycheeitem`
* **Текущее:** `Lychee`
* **Рекомендуется:** **Личи**
* **Причина:** Саженец «Саженец дерева личи». Плод «Lychee». В Almanac «Lychee». Блок «Lychee Фрукт».
* **Evidence:** [FACT]
* **Confidence:** HIGH

### `pamhc2trees:mangoitem`
* **Текущее:** `Mango`
* **Рекомендуется:** **Манго**
* **Причина:** Саженец «Саженец дерева манго». Плод «Mango». В Almanac «Mango».
* **Evidence:** [FACT]
* **Confidence:** HIGH

### `pamhc2trees:mapleitem`
* **Текущее:** `Maple Syrup`
* **Рекомендуется:** **Кленовый сироп**
* **Причина:** Саженец «Саженец клена». Предмет «Maple Syrup» (сок/сироп клена). Текущее в RU «Maple Syrup». Блок «Maple Фрукт Бревно».
* **Evidence:** [FACT]
* **Confidence:** HIGH

### `pamhc2trees:nutmegitem`
* **Текущее:** `Nutmeg`
* **Рекомендуется:** **Мускатный орех**
* **Причина:** Саженец «Саженец мускатного дерева». Плод «Nutmeg». Блок «Nutmeg Фрукт».
* **Evidence:** [FACT]
* **Confidence:** HIGH

### `pamhc2trees:oliveitem`
* **Текущее:** `Olive`
* **Рекомендуется:** **Оливка**
* **Причина:** Саженец «Olive Саженец». Плод «Olive». В Vinery «Оливка». Блок «Olive Фрукт».
* **Evidence:** [FACT]
* **Confidence:** HIGH

### `pamhc2trees:orangeitem`
* **Текущее:** `Orange`
* **Рекомендуется:** **Апельсин**
* **Причина:** Саженец «Саженец апельсинового дерева». Плод «Orange». В Atmospheric «Апельсин».
* **Evidence:** [FACT]
* **Confidence:** HIGH

### `pamhc2trees:papayaitem`
* **Текущее:** `Papaya`
* **Рекомендуется:** **Папайя**
* **Причина:** Саженец «Саженец папайи». Плод «Papaya». Блок «Papaya Фрукт».
* **Evidence:** [FACT]
* **Confidence:** HIGH

### `pamhc2trees:passionfruititem`
* **Текущее:** `Passionfruit`
* **Рекомендуется:** **Маракуйя**
* **Причина:** Саженец «Саженец дерева страсти». Плод «Passionfruit». В Atmospheric «Маракуйя» (atmospheric:passion_fruit).
* **Evidence:** [FACT]
* **Confidence:** HIGH

### `pamhc2trees:pawpawitem`
* **Текущее:** `Pawpaw`
* **Рекомендуется:** **Азимина**
* **Причина:** Asimina triloba (Pawpaw). Саженец «Pawpaw Саженец». Плод «Pawpaw». В Almanac «Pawpaw».
* **Evidence:** [INFERENCE]
* **Confidence:** HIGH

### `pamhc2trees:peachitem`
* **Текущее:** `Peach`
* **Рекомендуется:** **Персик**
* **Причина:** Саженец «Саженец персикового дерева». Плод «Peach». В Almanac «Peach».
* **Evidence:** [FACT]
* **Confidence:** HIGH

### `pamhc2trees:pearitem`
* **Текущее:** `Pear`
* **Рекомендуется:** **Груша**
* **Причина:** Саженец «Саженец грушевого дерева». Плод «Pear». Блок «Pear Фрукт».
* **Evidence:** [FACT]
* **Confidence:** HIGH

### `pamhc2trees:pecanitem`
* **Текущее:** `Pecan`
* **Рекомендуется:** **Пекан**
* **Причина:** Саженец «Саженец дерева пекан». Плод «Pecan». Блок «Pecan Фрукт».
* **Evidence:** [FACT]
* **Confidence:** HIGH

### `pamhc2trees:peppercornitem`
* **Текущее:** `Peppercorn`
* **Рекомендуется:** **Горошина чёрного перца**
* **Причина:** Саженец «Саженец перечного дерева». Плод «Peppercorn». Блок «Peppercorn Фрукт Бревно».
* **Evidence:** [INFERENCE]
* **Confidence:** HIGH

### `pamhc2trees:persimmonitem`
* **Текущее:** `Persimmon`
* **Рекомендуется:** **Хурма**
* **Причина:** Саженец «Саженец хурмы». Плод «Persimmon». Блок «Persimmon Фрукт».
* **Evidence:** [FACT]
* **Confidence:** HIGH

### `pamhc2trees:pinenutitem`
* **Текущее:** `Pinenuts`
* **Рекомендуется:** **Кедровые орехи**
* **Причина:** Саженец «Pinenut Саженец». Плод «Pinenuts».
* **Evidence:** [INFERENCE]
* **Confidence:** HIGH

### `pamhc2trees:pistachioitem`
* **Текущее:** `Pistachio`
* **Рекомендуется:** **Фисташка**
* **Причина:** Саженец «Саженец фисташкового дерева». Плод «Pistachio». Блок «Pistachio Фрукт».
* **Evidence:** [FACT]
* **Confidence:** HIGH

### `pamhc2trees:plumitem`
* **Текущее:** `Plum`
* **Рекомендуется:** **Слива**
* **Причина:** Саженец «Саженец сливового дерева». Плод «Plum». В Almanac «Plum».
* **Evidence:** [FACT]
* **Confidence:** HIGH

### `pamhc2trees:pomegranateitem`
* **Текущее:** `Pomegranate`
* **Рекомендуется:** **Гранат**
* **Причина:** Саженец «Саженец гранатового дерева». Плод «Pomegranate». Блок «Pomegranate Фрукт».
* **Evidence:** [FACT]
* **Confidence:** HIGH

### `pamhc2trees:rambutanitem`
* **Текущее:** `Rambutan`
* **Рекомендуется:** **Рамбутан**
* **Причина:** Саженец «Саженец дерева рамбутан». Плод «Rambutan». Блок «Rambutan Фрукт».
* **Evidence:** [FACT]
* **Confidence:** HIGH

### `pamhc2trees:roastedacornitem`
* **Текущее:** `Roasted Acorn`
* **Рекомендуется:** **Жареный жёлудь**
* **Причина:** В EN «Roasted Acorn». В текущем RU оставлен «Roasted Acorn». Производный продукт от Acorn.
* **Evidence:** [INFERENCE]
* **Confidence:** HIGH

### `pamhc2trees:roastedalmonditem`
* **Текущее:** `Roasted Almond`
* **Рекомендуется:** **Жареный миндаль**
* **Причина:** В EN «Roasted Almond». В текущем RU оставлен «Roasted Almond».
* **Evidence:** [INFERENCE]
* **Confidence:** HIGH

### `pamhc2trees:roastedcashewitem`
* **Текущее:** `Roasted Cashew`
* **Рекомендуется:** **Жареный кешью**
* **Причина:** В EN «Roasted Cashew». В текущем RU оставлен «Roasted Cashew».
* **Evidence:** [INFERENCE]
* **Confidence:** HIGH

### `pamhc2trees:roastedchestnutitem`
* **Текущее:** `Roasted Chestnut`
* **Рекомендуется:** **Жареный каштан**
* **Причина:** В EN «Roasted Chestnut». В текущем RU оставлен «Roasted Chestnut».
* **Evidence:** [INFERENCE]
* **Confidence:** HIGH

### `pamhc2trees:roastedhazelnutitem`
* **Текущее:** `Roasted Hazelnut`
* **Рекомендуется:** **Жареный фундук**
* **Причина:** В EN «Roasted Hazelnut». В текущем RU оставлен «Roasted Hazelnut».
* **Evidence:** [INFERENCE]
* **Confidence:** HIGH

### `pamhc2trees:roastedpecanitem`
* **Текущее:** `Roasted Pecan`
* **Рекомендуется:** **Жареный пекан**
* **Причина:** В EN «Roasted Pecan». В текущем RU оставлен «Roasted Pecan».
* **Evidence:** [INFERENCE]
* **Confidence:** HIGH

### `pamhc2trees:roastedpinenutitem`
* **Текущее:** `Roasted Pinenuts`
* **Рекомендуется:** **Жареные кедровые орехи**
* **Причина:** В EN «Roasted Pinenuts». В текущем RU оставлен «Roasted Pinenuts».
* **Evidence:** [INFERENCE]
* **Confidence:** HIGH

### `pamhc2trees:roastedpistachioitem`
* **Текущее:** `Roasted Pistachio`
* **Рекомендуется:** **Жареные фисташки**
* **Причина:** В EN «Roasted Pistachio». В текущем RU оставлен «Roasted Pistachio».
* **Evidence:** [INFERENCE]
* **Confidence:** HIGH

### `pamhc2trees:roastedwalnutitem`
* **Текущее:** `Roasted Walnut`
* **Рекомендуется:** **Жареный грецкий орех**
* **Причина:** В EN «Roasted Walnut». В текущем RU оставлен «Roasted Walnut».
* **Evidence:** [INFERENCE]
* **Confidence:** HIGH

### `pamhc2trees:soursopitem`
* **Текущее:** `Soursop`
* **Рекомендуется:** **Саусеп**
* **Причина:** Annona muricata (Soursop / сметанное яблоко / гравиола / саусеп). Саженец «Soursop Саженец». Плод «Soursop».
* **Evidence:** [INFERENCE]
* **Confidence:** HIGH

### `pamhc2trees:tamarinditem`
* **Текущее:** `Tamarind`
* **Рекомендуется:** **Тамаринд**
* **Причина:** Саженец «Саженец тамариндового дерева». Плод «Tamarind». Блок «Tamarind Фрукт».
* **Evidence:** [FACT]
* **Confidence:** HIGH

### `pamhc2trees:vanillabeanitem`
* **Текущее:** `Vanillabean`
* **Рекомендуется:** **Стручок ванили**
* **Причина:** Саженец «Саженец ванильного дерева». Плод «Vanillabean». Блок «Vanillabean Фрукт Бревно».
* **Evidence:** [FACT]
* **Confidence:** HIGH

### `pamhc2trees:walnutitem`
* **Текущее:** `Walnut`
* **Рекомендуется:** **Грецкий орех**
* **Причина:** Саженец «Саженец грецкого ореха». Плод «Walnut». Блок «Walnut Фрукт».
* **Evidence:** [FACT]
* **Confidence:** HIGH
