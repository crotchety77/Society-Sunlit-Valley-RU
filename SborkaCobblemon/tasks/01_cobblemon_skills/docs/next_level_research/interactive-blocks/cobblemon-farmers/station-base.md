# 🧬 Анатомия и реверс-инжиниринг `StationBaseBlockEntity`

> **Базовый класс:** `io.github.chakyl.cobblemonfarmers.blockentity.StationBaseBlockEntity`  
> **Родитель:** `net.minecraft.world.level.block.entity.BlockEntity`  
> **Статус аудита:** 🟢 100% Байткод-подтверждение (`javap -p -c -constants`)

---

## 1. 💾 Хранение покемона и структура данных

### 1.1. Механизм хранения покемона в блоке
[FACT: Байткод `StationBaseBlockEntity` и `PokeUtils.getItemFormPokemon`]
* Покемон хранится внутри `ItemStackHandler` в виде особого виртуального предмета **Pokemon Item Form** (`CobblemonItems.POKEMON_MODEL` / `PokemonItem.from(pokemon)`).
* При клике в GUI покемон сериализуется из Party игрока (`PlayerPartyStore`) в NBT предмета, содержащий полный слепок данных покемона:
  - UUID, Вид (Species), Уровень (Level), Форма (Form), Аспекты (Aspects).
  - IV (Individual Values), EV (Effort Values), Характер (Nature), Способность (Ability).
  - Флаг Shiny (`isShiny`), Дружба (`friendship`), Текущее и максимальное HP.
* **Рендеринг в мире:** Метод `initializeWorker()` считывает предмет и спавнит визуальную сущность `PokemonEntity` (тип `CobblemonEntities.POKEMON`) строго над блоком станции с ориентацией по сторонам света (`PokeUtils.getPokemonRotation`).

---

## 2. 🔍 Валидация работника и лимиты слотов

### 2.1. Определение валидности типа покемона (`validWorkerType`)
[FACT: Байткод `PokeUtils.validWorkerType`]
* Станция опрашивает `ElementalTypeUtils` для проверки соответствия основного (`primaryType`) или вторичного (`secondaryType`) типа покемона разрешённым типам станции:
  - Садоводство $\rightarrow$ Травяной, Водный, Летающий, Ядовитый, Волшебный.
  - Ремесло $\rightarrow$ Огненный, Электрический, Психический.
  - Шахта $\rightarrow$ Каменный, Земляной, Стальной.
  - Пилон энергии $\rightarrow$ Электрический.
  - Хрустальный шар $\rightarrow$ Психический, Призрачный, Тёмный.

### 2.2. Лимиты рабочих слотов игрока (`Worker Slots`)
[FACT: Байткод `GeneralUtils.getWorkerCap` и `PokeUtils.hasWorkerSlot`]
$$\text{WorkerCap} = \lfloor \text{Attribute}(\text{WORKER\_CAP}) + \text{Attribute}(\text{WORKER\_PERMITS}) - \text{Attribute}(\text{PUBLIC\_CONTRACTS}) \rfloor$$
* Перед помещением покемона в станцию метод `PokeUtils.hasWorkerSlot(player)` проверяет:
  $$\text{Attribute}(\text{WORKERS\_ASSIGNED}) < \text{WorkerCap}$$
* Если лимит исчерпан, покемон не устанавливается, и раздаётся звук ошибки.

---

## 3. 📐 Математические формулы характеристик (Bytecode Proof)

### 3.1. Множитель скорости работы (`SpeedModifier`)
[FACT: Байткод `StationBaseBlockEntity.fetchSpeedModifier`]

Инструкции байткода:
```
ldc2_w    #154   // double 127.5d
ddiv
ldc2_w    #156   // double 100.0d
dmul
invokestatic #163 // Mth.floor(double)
i2d
ldc2_w    #156   // double 100.0d
ddiv
// if (pokemon.getShiny()) mult = 2.0; else mult = 1.0;
```

**Математическая формула:**
$$\text{SpeedModifier} = \frac{\left\lfloor \frac{\text{Stat}}{127.5} \times 100 \right\rfloor}{100} \times (\text{isShiny} ? 2.0 : 1.0)$$

* **Пример при Stat = 128 (Обычный):** $\lfloor \frac{128}{127.5} \times 100 \rfloor / 100 = 1.00 \times 1.0 = \mathbf{1.0\times}$
* **Пример при Stat = 255 (Обычный):** $\lfloor \frac{255}{127.5} \times 100 \rfloor / 100 = 2.00 \times 1.0 = \mathbf{2.0\times}$
* **Пример при Stat = 255 (Shiny):** $2.00 \times 2.0 = \mathbf{4.0\times}$

---

### 3.2. Шанс мульти-производства (`MultChance`)
[FACT: Байткод `StationBaseBlockEntity.fetchMultChance`]

Инструкции байткода:
```
ldc2_w    #154   // double 127.5d
ddiv
ldc2_w    #156   // double 100.0d
dmul
invokestatic #163 // Mth.floor(double)
// if (pokemon.getShiny()) mult = 2; else mult = 1;
```

**Математическая формула:**
$$\text{MultChance} = \left\lfloor \frac{\text{Stat}}{127.5} \times 100 \right\rfloor \times (\text{isShiny} ? 2 : 1)$$

* Значение представляет собой **процент вероятности** ($100 = 100\%$, $200 = 200\%$, $400 = 400\%$).
* При шансе $> 100\%$ алгоритм распределения в `processRecipe` гарантированно удваивает/утраивает выход продукции!

---

### 3.3. Радиус зоны действия (`AoeRadius`)
[FACT: Байткод `StationBaseBlockEntity.fetchAoeRadius`]

Инструкции байткода:
```
ldc2_w    #176   // double 500.0d
ddiv
ldc2_w    #178   // double 10.0d
dmul
// if (pokemon.getShiny()) mult = 2.0; else mult = 1.0;
ldc2_w    #178   // double 10.0d (clamp max)
invokestatic #183 // Mth.clamp(val, 0.0, 10.0)
```

**Математическая формула:**
$$\text{AoeRadius} = (\text{int}) \operatorname{clamp}\left(\frac{\text{Stat}}{500.0} \times 10.0 \times (\text{isShiny} ? 2.0 : 1.0), 0.0, 10.0\right)$$

* **Обычный покемон:** При $\text{Stat} = 250 \rightarrow \frac{250}{500} \times 10 = \mathbf{5}$ блоков (зона $11 \times 11$).
* **Шайни покемон:** При $\text{Stat} = 250 \rightarrow 5 \times 2.0 = \mathbf{10}$ блоков (зона $21 \times 21$, максимум clamp).

---

## 4. ⚡ Интеграция внешних баффов (Pylon & Crystal Ball)

### 4.1. Ускорение от Пилона (`getBoostedSpeedModifier`)
[FACT: Байткод `StationBaseBlockEntity.getBoostedSpeedModifier`]
$$\text{BoostedSpeed} = \frac{\operatorname{round}((\text{SpeedModifier} + \text{BonusSpeed}) \times 100)}{100}$$
* `BonusSpeed` передаётся соседним Пилоном энергии ($+0.10 \dots +2.00$).

### 4.2. Мультипликатор от Хрустального шара (`getBoostedMultChance`)
[FACT: Байткод `StationBaseBlockEntity.getBoostedMultChance`]
$$\text{BoostedMultChance} = (\text{int})\left(\text{MultChance} \times (1.0 + \text{BonusMult} \times 0.01)\right)$$
* `BonusMult` передаётся Хрустальным шаром ($+25\% \rightarrow \text{множитель } 1.25$).

---

## 5. 📦 NBT Сериализация и сохранение состояния

[FACT: Байткод `StationBaseBlockEntity.saveAdditional` и `load`]
При сохранении в файл мира блок записывает следующие NBT-теги:

| NBT Ключ | Java Тип | Описание |
| :--- | :--- | :--- |
| `owner` | `UUID` (128-bit) | UUID владельца блока |
| `publicContract` | `Byte` (boolean) | Флаг публичного доступа |
| `bonusSpeed` | `Double` | Текущий активный бонус скорости от пилона |
| `bonusMult` | `Int` | Текущий активный бонус мультипликатора от шара |
| `inventory` | `CompoundTag` | Содержимое слотов предметов и покемона |

---

## 6. 📊 Сводная таблица наследования и переопределений

| Метод базового класса | Назначение в `StationBase` | Переопределяется ли в подклассах? |
| :--- | :--- | :---: |
| `fetchSpeedModifier(Stats)` | Универсальный расчёт множителя скорости по статам | **Переиспользуется всеми** |
| `fetchMultChance(Stats)` | Универсальный расчёт процента доп. дропа | **Переиспользуется всеми** |
| `fetchAoeRadius(Stats)` | Расчёт радиуса Манхэттена с clamp до 10 | **Переиспользуется Садоводством** |
| `getBoostedSpeedModifier()` | Сложение базовой скорости с бонусом пилона | **Переиспользуется всеми** |
| `getBoostedMultChance()` | Умножение шанса на бонус шара | **Переиспользуется всеми** |
| `tick(...)` | Базовая заглушка | **Полностью переопределяется каждой станцией** |
| `canProcess(...)` | Проверка валидности рецепта | **Уникален для каждой станции** |
| `canReceiveBonusSpeed()` | Разрешение приёма ускорения пилона | **True для всех, кроме RanchingStation** |
