# 🏭 Сравнительный аудит специализированных станций Cobblemon Farmers

> **Статус документа:** Level 2 Specialized Stations Audit  
> **Охват:** Все 6 классов станций мода `cobblemon_farmers-2.4-all.jar`  
> **Маркировка:** `[FACT]` (Байткод), `[DERIVED]` (Формулы), `[INFERRED]` (Поведение).

---

## 1. 📊 Сравнительная матрица специализированных станций

| Параметр / Механика | Gardening Station | Ranching Station | Craft Station | Mystery Mine | Energy Pylon | Crystal Ball |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Класс BlockEntity** | `GardeningStation...` | `RanchingStation...` | `CraftStation...` | `MysteryMine...` | `EnergyPylon...` | `CrystalBall...` |
| **Разрешённые стихии** | Grass, Water, Flying, Poison, Fairy | Любые типы (All) | Fire, Electric, Psychic | Rock, Ground, Steel | Electric | Psychic, Ghost, Dark |
| **Профильный стат скорости** | `Stats.SPEED` | — (Day Cycle) | `Stats.SPEED` | `Stats.SPEED` | `Stats.SPEED` | `Stats.SPEED` |
| **Профильный стат дропа/силы**| `Stats.SPEED` (AoE) | `Friendship + HP` | `Stats.SPECIAL_ATTACK` | `Stats.ATTACK` | — (Тип батареи) | `Stats.SPECIAL_ATTACK` |
| **Тип таймера** | Real-time Ticker | Day-Cycle (`dayLastForaged`) | Progress / MaxProgress | Progress / MaxProgress | Progress / MaxProgress | Progress / MaxProgress |
| **Приём ускорения Пилона** | 🟢 **Да** (`+BonusSpeed`) | 🔴 **НЕТ** (Заблокировано) | 🟢 **Да** (`+BonusSpeed`) | 🟢 **Да** (`+BonusSpeed`) | 🔴 **НЕТ** | 🔴 **НЕТ** |
| **Приём бонуса Шара** | 🔴 Нет (AoE логика) | 🔴 Нет | 🟢 **Да** (`+BonusMult`) | 🟢 **Да** (`+BonusMult`) | 🔴 Нет | 🔴 Нет |
| **Кнопка приоритета (GUI)** | 🟢 Полив / Сбор / Кость | 🔴 Нет (Только рецепты) | 🟢 Плавлю / Дерево / Смузи | 🟢 Камень / Земля | 🔴 Нет | 🔴 Нет |

---

## 2. 🔬 Детальный аудит каждой станции

### 2.1. Станция садоводства (Gardening Station)
[FACT: Байткод `GardeningStationBlockEntity.class`]
* **Стихийные роли Gardening Station:**
  1. **Water (Водный):** Вызывает `waterFarmland(radius)` — увлажнение пашни (таймер 600 тиков / 30 сек, стат `SPECIAL_ATTACK`).
  2. **Grass (Травяной):** Вызывает `growCropsInRadius(...)` — костная мука / ускорение роста (таймер 24 000 тиков / 1200 сек, стат `SPEED`).
  3. **Flying (Летающий):** Вызывает `harvestNearbyBerries(radius)` — **Сбор ягод (`Harvest Berries`)** с ягодных деревьев Cobblemon (таймер 200 тиков / 10 сек, стат `SPECIAL_DEFENCE`).
  4. **Normal (Обычный):** Вызывает `harvestFromRanchingStation(radius, false)` — пассивный сбор готовой продукции с окружающих Станций Ранчо (таймер 300 тиков / 15 сек, стат `SPEED`).
  5. **Fairy (Волшебный):** Вызывает `harvestFromRanchingStation(radius, true)` — улучшенный магический сбор со Станций Ранчо (таймер 800 тиков / 40 сек, стат `SPECIAL_ATTACK`).
  6. **Dark (Тёмный):** Вызывает `generateExp(radius * 4)` — синтез Конфет Опыта (Exp Candies) (таймер 20 000 тиков, стат `HP`).
* **Брейкпоинт радиуса:** При `Speed = 250` (Shiny) радиус достигает $10$ блоков (площадь $21 \times 21 = 441$ грядка).

---

### 2.2. Станция ранчо (Ranching Station)
[FACT: Байткод `RanchingStationBlockEntity.class` и `RanchingForage.class`]
* **Инвариант независимости от тиков:** Метод `tick()` проверяет `level.getDay() > dayLastForaged`. Станция срабатывает **ровно один раз за игровые сутки**.
* **Защита от ускорения Пилоном:** В методе `EnergyPylonBlockEntity.buffNearestStation` стоит явная проверка:
  `if (target instanceof RanchingStationBlockEntity) return false;`
* **Формула расчёта сердец (0..10):**
  $$\text{Hearts} = \min\left(10, \left\lfloor \frac{5 \times \text{Friendship}}{255} \right\rfloor + \left\lfloor \frac{5 \times \text{HP}}{250} \right\rfloor\right)$$
  * При Shiny и $\text{HP} \ge 250$ сразу активируются максимальные 10 сердец, открывая пул супер-лута (Booster Energy, ДНК Мью, Сердце Феи).

---

### 2.3. Станция ремесла (Craft Station)
[FACT: Байткод `CraftStationBlockEntity.class` и `CraftStationRecipe.class`]
* **Прогресс крафта:** На каждый тик `progress += getBoostedSpeedModifier()`.
* **Множитель выхода:** При завершении рецепта вызывается `fetchMultChance(Stats.SPECIAL_ATTACK)`.
  * При $\text{Sp. Atk} = 255$ и Shiny: шанс составляет **$400\%$** (выход умножается на $4.0\dots 5.0$).
* **Специализации:**
  - Огненные покемоны $\rightarrow$ Высокотемпературная плавка руд.
  - Электрические покемоны $\rightarrow$ Точная распиловка древесины (1 саженец $\rightarrow$ до 12 брёвен).
  - Психические покемоны $\rightarrow$ Кристаллизация и алхимические смузи.

---

### 2.4. Загадочная шахта (Mystery Mine)
[FACT: Байткод `MysteryMineBlockEntity.class` и `MysteryMineRecipe.class`]
* **Два режима работы:**
  1. **Каменный режим (Rock/Steel):** Скорость от `Stats.SPEED`, доп. руда от `Stats.ATTACK`. Базовое время добычи 200 тиков (10 сек) $\rightarrow$ ускоряется до 50 тиков (2.5 сек) с утроенным дропом руд.
  2. **Земляной режим (Ground):** Раскопка археологических блоков, шанс $1.0\%$ на получение древних окаменелостей (Helix, Dome, Amber, Jaw, Sail и др.) и Яиц нюхача.

---

### 2.5. Пилон энергии (Energy Pylon)
[FACT: Байткод `EnergyPylonBlockEntity.class`]
* **Сетевой радиус:** Сканирует куб Манхэттена `GeneralUtils.getBetweenManhattan(pos, radius, height)` вокруг себя.
* **Передача энергии:** Находит ближайшую `StationBaseBlockEntity` и вызывает `target.setBonusSpeed(recipe.getSpeedBonus())`.
* **Тиры батарей:**
  - Базовая батарея: $+10\%$ скорости (`BonusSpeed = 0.10`)
  - Улучшенная батарея: $+25\%$ скорости (`BonusSpeed = 0.25`)
  - Продвинутая батарея: $+50\%$ скорости (`BonusSpeed = 0.50`)
  - Ультра-батарея: $+200\%$ скорости (`BonusSpeed = 2.00`)

---

### 2.6. Хрустальный шар (Crystal Ball)
[FACT: Байткод `CrystalBallBlockEntity.class`]
* **Сетевой мультипликатор:** Потребляет самоцветы стихий (Elemental Gems).
* **Передача бонуса:** Вызывает `target.setBonusMult(25)` на окружающих станциях.
* **Синергия:** В формуле `getBoostedMultChance()` мультипликатор $+25\%$ умножает базовый шанс покемона (например, $200\% \times 1.25 = \mathbf{250\%}$).
