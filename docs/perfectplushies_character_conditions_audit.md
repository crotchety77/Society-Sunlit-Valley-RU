# Технический аудит условий и механик характеров Perfect Plushies

> **Дата аудита:** 2026-09-24  
> **Статус:** FACT-Based Source Code Audit  
> **Исследованные исходные файлы:**  
> - `game_data/startup_scripts/globalAnimalHandlers.js` (`global.getPlushieModifiers`, `global.handleSpecialHarvest`, `global.executePlushieHusbandry`)
> - `game_data/startup_scripts/globalBlockEntityHandlers.js` (`global.getTaggedBlocksInRadius`)
> - `game_data/startup_scripts/globalFurniturePlushies.js` (`global.plushieTraits`)
> - `game_data/server_scripts/entities/animalBase.js` (`handleSpecialItem`, `global.executePlushieHusbandry`)
> - `game_data/server_scripts/blockEvents/plushieMechanics.js` (`BlockEvents.placed`, `breakPlushie`)
> - `game_data/client_scripts/tooltips/addAdvancedTooltips.js`

---

## 1. Архитектура механики и геометрия проверок

### 1.1 Геометрия функции `global.getTaggedBlocksInRadius` `[FACT]`
Реализация в `globalBlockEntityHandlers.js` (строки 1353–1377):
```javascript
global.getTaggedBlocksInRadius = (level, scanTag, centerPos, radius, returnTagged) => {
  const { x, y, z } = centerPos;
  let scanBlock;
  let scannedBlocks = 0;
  let taggedBlocks = [];
  for (let pos of BlockPos.betweenClosed(
    new BlockPos(x - radius, y - radius, z - radius),
    [x + radius, y + radius, z + radius]
  )) {
    if (!level.isLoaded(pos)) continue;
    scanBlock = level.getBlock(pos);
    if (scanBlock.hasTag(scanTag)) {
      scannedBlocks++;
      if (returnTagged) taggedBlocks.push(scanBlock.id);
    }
  }
  if (returnTagged) return taggedBlocks;
  return scannedBlocks;
};
```

* **Геометрия:** Симметричный кубический ограничивающий параллелепипед (Axis-Aligned Bounding Box, AABB), центрированный на позиции блока плюшевой игрушки `centerPos`. `[FACT]`
* **Диапазоны координат:** `[x - radius .. x + radius]`, `[y - radius .. y + radius]`, `[z - radius .. z + radius]`. `[FACT]`
* **Длина ребра куба:** `2 * radius + 1` блоков. `[FACT]`
* **Общий объём проверки:** `(2 * radius + 1)^3` блоков. `[FACT]`
* **Вхождение центрального блока:** Сам блок игрушки `(x, y, z)` ВСЕГДА входит в область проверки при любом `radius >= 0`. `[FACT]`

---

### 1.2 Система качества (Quality) `[FACT]`
В NBT предмета качество хранится в компаунде `quality_food`:
* NBT-ключ: `item.nbt.quality_food.quality` (тип: `int`, допустимые базовые значения: `0`, `1`, `2`, `3`).
* В `global.getPlushieModifiers`: `qualityMult = data.quality + 1`.
* Градации:
  * ★ (Обычное, `quality = 0`): `qualityMult = 1`
  * ★★ (Серебряное, `quality = 1`): `qualityMult = 2`
  * ★★★ (Золотое, `quality = 2`): `qualityMult = 3`
  * ★★★★ (Иридиевое, `quality = 3`): `qualityMult = 4`
* Если NBT отсутствует: `quality = 0` $\rightarrow$ `qualityMult = 1`. `[FACT]`

---

## 2. Сводная таблица аудита всех 15 характеров

| Type | Character | Source | Quality source | Formula | ★ (q=0) | ★★ (q=1) | ★★★ (q=2) | ★★★★ (q=3) | Radius | Area | Boundary | Target | Tooltip value | Confidence |
| :---: | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :---: |
| **0** | **Водный**<br>(`aquatic`) | `globalAnimalHandlers.js:521` | `data.quality` | `5% * qualityMult` | 5% | 10% | 15% | 20% | N/A | N/A | `roll < P` | Речное/Океаническое желе | `Шанс добыть желе: {P}%` | `[FACT]` |
| **1** | **Лесной**<br>(`woodsy`) | `globalAnimalHandlers.js:530` | `data.quality` | `8 * qualityMult` брёвен | 8 шт. | 16 шт. | 24 шт. | 32 шт. | `3` | `7x7x7` | `count > 0` | Брёвна `#society:raw_logs` | `Добывает древесину: {N} шт. [Область: 7x7x7]` | `[FACT]` |
| **2** | **Древний**<br>(`eldritch`) | `globalAnimalHandlers.js:548` | `data.quality` | `1 * qualityMult` серебра | 1 шт. | 2 шт. | 3 шт. | 4 шт. | N/A | N/A | Гарантировано | `oreganized:raw_silver` | `Добывает сырое серебро: {N} шт.` | `[FACT]` |
| **3** | **Гневный**<br>(`wrathful`) | `globalAnimalHandlers.js:552` | `data.quality` | `3 * qualityMult` свинца | 3 шт. | 6 шт. | 9 шт. | 12 шт. | N/A | N/A | Гарантировано | `oreganized:raw_lead` | `Добывает сырой свинец: {N} шт.` | `[FACT]` |
| **4** | **Сомелье**<br>(`sommelier`) | `globalAnimalHandlers.js:556` | `data.quality` | `25% * qualityMult` | 25% | 50% | 75% | 100% | N/A | N/A | `roll < P` | Ремесленная переработка | `Шанс сделать продукт ремесленным: {P}%` | `[FACT]` |
| **5** | **Солнечный**<br>(`sunlit`) | `globalAnimalHandlers.js:560` | `data.quality` | `5% * qualityMult` | 5% | 10% | 15% | 20% | N/A | N/A | `roll < P` | `society:sunlit_crystal` | `Шанс добыть Солнечный кристалл: {P}%` | `[FACT]` |
| **6** | **Голодный**<br>(`hungry`) | `globalAnimalHandlers.js:566` | `data.quality` | `10% * qualityMult` | 10% | 20% | 30% | 40% | N/A | N/A | `roll < P` | Сброс кд сбора (`resetDay`) | `Шанс на доп. сбор без ожидания дня: {P}%` | `[FACT]` |
| **7** | **Тревожный**<br>(`anxious`) | `globalAnimalHandlers.js:570` | `data.quality` | `+25% * qualityMult` | +25% | +50% | +75% | +100% | N/A | N/A | Бонус к шансу | Базовый шанс дропа животного | `Бонус к шансу редкого сбора: +{P}%` | `[FACT]` |
| **8** | **Скромный**<br>(`shy`) | `globalAnimalHandlers.js:574` | `data.quality` | Радиус `3 - quality`<br>Область `(7-2*q)^3` | `7x7x7`<br>(R=3) | `5x5x5`<br>(R=2) | `3x3x3`<br>(R=1) | `1x1x1`<br>(R=0) | `3 - quality` | `(7-2*q)^3` | `count == 1` | Игрушки `#society:plushies` | `Двойная продукция, если нет других игрушек в области {Area} (радиус {R})` | `[FACT]` |
| **9** | **Весёлый**<br>(`cheerful`) | `globalAnimalHandlers.js:587` | `data.quality` | `28 - 4 * qualityMult`<br>(требуется `> T`) | >24 (от 25) | >20 (от 21) | >16 (от 17) | >12 (от 13) | `2` | `5x5x5` | `count > T` | Игрушки `#society:plushies` | `Двойная продукция: требуется от {N} игрушек рядом [Область: 5x5x5]` | `[FACT]` |
| **10** | **Спокойный**<br>(`chill`) | `globalAnimalHandlers.js:601` | `data.quality` | `1 * qualityMult` алмазов | 1 шт. | 2 шт. | 3 шт. | 4 шт. | N/A | N/A | Гарантировано | `society:pristine_diamond` | `Добывает безупречные алмазы: {N} шт.` | `[FACT]` |
| **11** | **Хитрый**<br>(`machiavellian`) | `globalAnimalHandlers.js:605` | `data.quality` | `1 * qualityMult` иридия | 1 шт. | 2 шт. | 3 шт. | 4 шт. | N/A | N/A | Гарантировано | `minecraft:netherite_scrap` (по лору: Иридиевый лом) | `Добывает иридиевый лом: {N} шт.` | `[FACT]` |
| **12** | **Милый**<br>(`cutesy`) | `globalAnimalHandlers.js:609` | `data.quality` | `1 * qualityMult` коробок | 1 шт. | 2 шт. | 3 шт. | 4 шт. | N/A | N/A | Гарантировано | `society:furniture_box` | `Добывает коробки с мебелью: {N} шт.` | `[FACT]` |
| **13** | **Модник**<br>(`fashionista`) | `globalAnimalHandlers.js:614` | `data.quality` | `28 - 4 * qualityMult`<br>(требуется `>= T`) | >=24 | >=20 | >=16 | >=12 | `2` | `5x5x5` | `count >= T` | Мебель `#society:loot_furniture` | `Двойная продукция: требуется от {N} мебели рядом [Область: 5x5x5]` | `[FACT]` |
| **14** | **Нейтральный**<br>(`neutral`) | `globalAnimalHandlers.js:628` | `data.quality` | `10% * qualityMult` | 10% | 20% | 30% | 40% | N/A | N/A | `roll < P` | Удвоение сбора (`doubleDrops`) | `Шанс удвоить сбор: {P}%` | `[FACT]` |

---

## 3. Семантика переменной `count` и доказательство учёта центрального блока [FACT]

### 3.1 Теги и вхождение в сканирование
1. **Тег плюшевых игрушек:** `#society:plushies`
   - Все плюшевые игрушки (включая саму текущую игрушку на позиции `centerPos`) зарегистрированы в теге `#society:plushies` (`handleItemBlockFluidTags.js:424`, `handleItemBlockFluidTags.js:702-705`).
   - Функция `BlockPos.betweenClosed([x - r, y - r, z - r], [x + r, y + r, z + r])` проверяет позицию `(x, y, z)`.
   - Так как блок на `centerPos` имеет тег `#society:plushies`, он **всегда** инкрементирует `scannedBlocks++`.
   - **Вывод для `cheerful (type 9)` и `shy (type 8)`:** `count` включает саму текущую игрушку (`count = 1 + count_other_plushies`). `[FACT]`

2. **Тег мебели:** `#society:loot_furniture`
   - Тег включает мебель: стулья, столы, тумбы, шкафы и т.д.
   - Плюшевые игрушки **НЕ** имеют тега `#society:loot_furniture` (пересечение тегов строго пустое `set() = 0`).
   - Блок текущей игрушки на позиции `(x, y, z)` не имеет тега мебели, поэтому `scanBlock.hasTag("society:loot_furniture")` возвращает `false`.
   - **Вывод для `fashionista (type 13)`:** `count` **НЕ** включает саму текущую игрушку (`count = count_furniture`). `[FACT]`

---

## 4. Граничные тесты (Boundary Tests) [FACT / LOGIC TEST]

| Character | Quality | Formula / Condition | Operator | Threshold ($T$) | count below | Result | count boundary ($T$) | Result | count above | Result | Физически требуется игроку |
| :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **cheerful** | ★ ($q=0$) | `count > (28 - 4*1)` | `>` | 24 | 23 | **FALSE** | 24 | **FALSE** | 25 | **TRUE** | **от 24 других игрушек** (всего 25 в зоне) |
| **cheerful** | ★★ ($q=1$) | `count > (28 - 4*2)` | `>` | 20 | 19 | **FALSE** | 20 | **FALSE** | 21 | **TRUE** | **от 20 других игрушек** (всего 21 в зоне) |
| **cheerful** | ★★★ ($q=2$) | `count > (28 - 4*3)` | `>` | 16 | 15 | **FALSE** | 16 | **FALSE** | 17 | **TRUE** | **от 16 других игрушек** (всего 17 в зоне) |
| **cheerful** | ★★★★ ($q=3$) | `count > (28 - 4*4)` | `>` | 12 | 11 | **FALSE** | 12 | **FALSE** | 13 | **TRUE** | **от 12 других игрушек** (всего 13 в зоне) |
| **fashionista** | ★ ($q=0$) | `count >= (28 - 4*1)` | `>=` | 24 | 23 | **FALSE** | 24 | **TRUE** | 25 | **TRUE** | **от 24 мебели** рядом |
| **fashionista** | ★★ ($q=1$) | `count >= (28 - 4*2)` | `>=` | 20 | 19 | **FALSE** | 20 | **TRUE** | 21 | **TRUE** | **от 20 мебели** рядом |
| **fashionista** | ★★★ ($q=2$) | `count >= (28 - 4*3)` | `>=` | 16 | 15 | **FALSE** | 16 | **TRUE** | 17 | **TRUE** | **от 16 мебели** рядом |
| **fashionista** | ★★★★ ($q=3$) | `count >= (28 - 4*4)` | `>=` | 12 | 11 | **FALSE** | 12 | **TRUE** | 13 | **TRUE** | **от 12 мебели** рядом |
| **shy** | ★ ($q=0$) | `count == 1` ($R=3$, `7x7x7`) | `==` | 1 | 0 (N/A) | - | 1 | **TRUE** | 2 | **FALSE** | **0 других игрушек** в зоне `7x7x7` |
| **shy** | ★★ ($q=1$) | `count == 1` ($R=2$, `5x5x5`) | `==` | 1 | 0 (N/A) | - | 1 | **TRUE** | 2 | **FALSE** | **0 других игрушек** в зоне `5x5x5` |
| **shy** | ★★★ ($q=2$) | `count == 1` ($R=1$, `3x3x3`) | `==` | 1 | 0 (N/A) | - | 1 | **TRUE** | 2 | **FALSE** | **0 других игрушек** в зоне `3x3x3` |
| **shy** | ★★★★ ($q=3$) | `count == 1` ($R=0$, `1x1x1`) | `==` | 1 | 0 (N/A) | - | 1 | **TRUE** | - | - | **Всегда выполняется** (зона `1x1x1` = только сам блок) |

---

## 5. Полный аудит операторов для всех 15 характеров [FACT]

1. **`aquatic` (0):** `Math.random() < (0.05 * qualityMult)` (вероятностный `roll < P`).
2. **`woodsy` (1):** `logCount > 0` (наличие хотя бы 1 бревна в `7x7x7`).
3. **`eldritch` (2):** Без условий / безусловная выдача (`global.spawnItemAboveBlock`).
4. **`wrathful` (3):** Без условий / безусловная выдача (`global.spawnItemAboveBlock`).
5. **`sommelier` (4):** `Math.random() < (0.25 * qualityMult)` (вероятностный `roll < P`).
6. **`sunlit` (5):** `Math.random() < (0.05 * qualityMult)` (вероятностный `roll < P`).
7. **`hungry` (6):** `Math.random() < (0.10 * qualityMult)` (вероятностный `roll < P`).
8. **`anxious` (7):** `animalData.rareDropChance += (0.25 * qualityMult)` (аддитивный модификатор).
9. **`shy` (8):** `plushieCount == 1` (строгое равенство 1, т.е. только сам текущий блок).
10. **`cheerful` (9):** `plushieCount > (28 - 4 * qualityMult)` (строгое неравенство `>`).
11. **`chill` (10):** Без условий / безусловная выдача (`global.spawnItemAboveBlock`).
12. **`machiavellian` (11):** Без условий / безусловная выдача (`global.spawnItemAboveBlock`).
13. **`cutesy` (12):** Без условий / безусловная выдача (`global.spawnItemAboveBlock`).
14. **`fashionista` (13):** `furnitureCount >= (28 - 4 * qualityMult)` (нестрогое неравенство `>=`).
15. **`neutral` (14):** `Math.random() < (0.10 * qualityMult)` (вероятностный `roll < P`).

---

## 6. Критические находки и опровержение неверных гипотез

1. **Лесной (`woodsy`, type 1) — Неверный размер области в старых текстах:**
   - В старом переводе и описании было ошибочно указано `[Область: 5x5x5]`.
   - Фактический код: `global.getTaggedBlocksInRadius(level, "society:raw_logs", plushieBlock, 3, true)` $\rightarrow$ радиус `3`, что даёт область **`7x7x7`** (`[-3..+3]`). `[FACT]`

2. **Скромный (`shy`, type 8) — Точная механика радиуса и области:**
   - Формула радиуса: `radius = 3 - (qualityMult - 1) = 3 - quality`.
   - При ★★★★ (`quality = 3`): `radius = 0`, то есть область `1x1x1`. Так как внутри области находится только сам блок игрушки, счётчик всегда равен `1`, и условие удвоения выполняется **гарантированно**, даже если вокруг стоят десятки других игрушек. `[FACT]`

3. **Весёлый (`cheerful`, type 9) vs Модник (`fashionista`, type 13) — Разница в граничных операторах и семантике:**
   - `cheerful`: `count > (28 - 4 * qualityMult)`. При качестве ★ (`qualityMult = 1`): `count > 24` $\rightarrow$ требуется минимум **25** суммарных игрушек в области `5x5x5` (то есть **24 других игрушки** + сама текущая игрушка).
   - `fashionista`: `count >= (28 - 4 * qualityMult)`. При качестве ★: `count >= 24` $\rightarrow$ требуется минимум **24** блока мебели в области `5x5x5` (сама игрушка мебелью не является). `[FACT]`

---

## 7. Пример конкретного предмета

Тестовый предмет:
```javascript
Item.of('perfectplushies:adv_fennec_fox_plushie', '{affection:0,quality_food:{quality:0},quest_id:1,type:13}')
```
* `type = 13` $\rightarrow$ Модник (`fashionista`).
* `quality = 0` $\rightarrow$ ★ (1 звезда, `qualityMult = 1`).
* Расчёт: `28 - 4 * 1 = 24` мебели в области `5x5x5` (радиус 2).
* **Итоговое отображение в Tooltip:**
  ```
  [Shift] Характер: Модник
  При поселении животного:
  Двойная продукция, если рядом много мебели
  Требуется мебели рядом: от 24 шт. [Область: 5x5x5]
  ```

---

## 8. Итоговые вердикты верификации (Verification Summary)

* **Source-code verification:** `PASS`
* **Boundary verification:** `PASS`
* **Count semantics verification:** `PASS`
* **Radius verification:** `PASS`
* **Tooltip semantics verification:** `PASS`
* **Runtime gameplay test:** `NOT PERFORMED` *(Minecraft-клиент не запущен в headless CI-среде; выполнен исчерпывающий детерминированный logic/boundary test suite `tools/test_plushie_boundaries.py`)*

### Ответы на ключевые вопросы:
* **Does count include the current plushie?**
  * Для `cheerful (9)` и `shy (8)`: **YES** (блок плюшки имеет тег `#society:plushies` и попадает в сканирование).
  * Для `fashionista (13)`: **NO** (блок плюшки не имеет тега `#society:loot_furniture`).
* **Are > and >= correctly reflected in tooltip?** **YES** (формулировки отображают точное количество требуемых объектов для игрока: `от 24 мебели` для fashionista и `от 24 других игрушек` для cheerful).
* **Are all displayed radii equal to actual search radii?** **YES** (все радиусы $R$ и области $(2R+1)^3$ строго соответствуют исходному коду).

