# 🏗️ Архитектура системы рабочих Cobblemon Farmers

> **Статус исследования:** Level 2 Deep Architectural Audit  
> **Исходные файлы:** `cobblemon_farmers-2.4-all.jar` (декомпиляция байткода `javap`)  
> **Маркировка:** Все утверждения строго снабжены тегами `[FACT]`, `[DERIVED]`, `[INFERRED]`.

---

## 1. 📐 Диаграмма объектно-ориентированной иерархии

```mermaid
classDiagram
    class BlockEntity {
        <<Minecraft Core>>
        +BlockPos worldPosition
        +BlockState blockState
        +saveAdditional(CompoundTag)
        +load(CompoundTag)
    }
    class MenuProvider {
        <<Minecraft Core>>
        +createMenu(int, Inventory, Player)
    }
    class StationBaseBlockEntity {
        <<Abstract Foundation>>
        #UUID owner
        #boolean publicContract
        -PokemonEntity workerEntity
        #double speedModifier
        #int multChance
        #int aoeRadius
        #double bonusSpeed
        #int bonusMult
        +getPokemonItem() ItemStack
        +hasWorker() boolean
        +initializeWorker() void
        +fetchSpeedModifier(Stats) void
        +fetchMultChance(Stats) void
        +fetchAoeRadius(Stats) void
        +getBoostedSpeedModifier() double
        +getBoostedMultChance() int
        +validateOwner(Player) boolean
        +validatePublicContract(Player) boolean
    }
    class GardeningStationBlockEntity {
        -ItemStackHandler inputInventory
        -ItemStackHandler outputInventory
        -ItemStackHandler pokemonInventory
        +tick(Level, BlockPos, BlockState)
        -handleWatering()
        -handleBonemeal()
        -handleHarvesting()
        -handleRanching()
    }
    class RanchingStationBlockEntity {
        -ItemStackHandler outputInventory
        -ItemStackHandler pokemonInventory
        -int dayLastForaged
        +tick(Level, BlockPos, BlockState)
        -handleDailyDrop()
    }
    class CraftStationBlockEntity {
        -ItemStackHandler inputInventory
        -ItemStackHandler outputInventory
        -ItemStackHandler pokemonInventory
        -int progress
        -int maxProgress
        +tick(Level, BlockPos, BlockState)
        -processRecipe(CraftStationRecipe)
    }
    class MysteryMineBlockEntity {
        -ItemStackHandler inputInventory
        -ItemStackHandler pokemonInventory
        -int progress
        +tick(Level, BlockPos, BlockState)
        -processRecipe(MysteryMineRecipe)
    }
    class EnergyPylonBlockEntity {
        -ItemStackHandler inputInventory
        -ItemStackHandler outputInventory
        -ItemStackHandler pokemonInventory
        -int progress
        +tick(Level, BlockPos, BlockState)
        -buffNearestStation(BlockPos, int, EnergyPylonRecipe)
    }
    class CrystalBallBlockEntity {
        -ItemStackHandler inputInventory
        -ItemStackHandler pokemonInventory
        -int progress
        +tick(Level, BlockPos, BlockState)
        -buffNearestStation(BlockPos, int, CrystalBallRecipe)
    }

    BlockEntity <|-- StationBaseBlockEntity
    StationBaseBlockEntity <|-- GardeningStationBlockEntity
    StationBaseBlockEntity <|-- RanchingStationBlockEntity
    StationBaseBlockEntity <|-- CraftStationBlockEntity
    StationBaseBlockEntity <|-- MysteryMineBlockEntity
    StationBaseBlockEntity <|-- EnergyPylonBlockEntity
    StationBaseBlockEntity <|-- CrystalBallBlockEntity

    MenuProvider <|.. GardeningStationBlockEntity
    MenuProvider <|.. RanchingStationBlockEntity
    MenuProvider <|.. CraftStationBlockEntity
    MenuProvider <|.. MysteryMineBlockEntity
    MenuProvider <|.. EnergyPylonBlockEntity
    MenuProvider <|.. CrystalBallBlockEntity
```

---

## 2. 🔄 Жизненный цикл рабочего цикла (Tick Dataflow Pipeline)

Каждый игровой такт (Tick) рабочие станции выполняют строго последовательный цикл валидации и обработки:

```mermaid
sequenceDiagram
    autonumber
    participant Engine as Minecraft Tick Engine
    participant Station as StationBaseBlockEntity
    participant Utils as PokeUtils / GeneralUtils
    participant Target as Окружающий мир / Рецепты

    Engine->>Station: tick(level, pos, state)
    Station->>Station: hasWorker() [Проверка слота покемона]
    alt Нет покемона в слоте
        Station-->>Engine: Выход из тика (простой)
    else Покемон присутствует
        Station->>Utils: validWorkerType(station, type, level)
        alt Тип не подходит для станции
            Station-->>Engine: Отмена работы (Invalid Type)
        else Валидный тип
            Station->>Station: Чтение статов и расчёт SpeedModifier / MultChance / AoeRadius
            alt Это Инфраструктурный блок (Пилон / Шар)
                Station->>Utils: getBetweenManhattan(pos, radius, height)
                Station->>Target: Наложение баффа bonusSpeed / bonusMult на соседние StationBaseBlockEntity
            else Это Производственная станция (Крафт / Шахта / Сад)
                Station->>Station: progress += getBoostedSpeedModifier()
                alt progress >= maxProgress
                    Station->>Target: Выполнение операции / выдача дропа с учётом getBoostedMultChance()
                    Station->>Station: Сброс progress = 0
                end
            end
        end
    end
```

---

## 3. 🌐 Сетевая модель и синхронизация (Client/Server Packet Architecture)

### 3.1. Синхронизация данных блока (NBT Sync)
[FACT: Байткод `StationBaseBlockEntity.m_58483_` и `onDataPacket`]
1. **Сервер:** При изменении состояния формирует пакет `ClientboundBlockEntityDataPacket.create(this)`.
2. **Клиент:** Получает NBT-тег блока через метод `onDataPacket()`, обновляя угол поворота модели покемона (`getPokemonRotation`), визуальный рендер и параметры частиц.

### 3.2. Клиент-серверное управление приоритетами
[FACT: Байткод `ServerBoundSwapPriorityPacket.class` и `PacketHandler.class`]
* Кнопка в GUI `TogglePriorityButton` отправляет сетевой пакет `ServerBoundSwapPriorityPacket` на сервер.
* Серверный метод `setPrioritySwapped()` переключает режим работы станции (например, Садоводство: переключение между поливом, сбором и костной мукой; Шахта: Каменный vs Земляной режим).

---

## 4. 🔒 Система безопасности и прав доступа (Ownership & Contracts)

### 4.1. Валидация владельца (`validateOwner`)
[FACT: Байткод `StationBaseBlockEntity.validateOwner`]
* Блок хранит UUID владельца (`owner`).
* Если блок приватный, только игрок с совпадающим `player.getUUID()` может открывать GUI и извлекать покемона.
* Если игрок не является владельцем, отправляется локализованное сообщение об ошибке с красным форматированием `ChatFormatting.RED`.

### 4.2. Механика публичного контракта (`publicContract`)
[FACT: Байткод `validatePublicContract` и `PublicContractItem.class`]
* При применении предмета `cobblemon_farmers:public_contract` блок переходит в состояние `publicContract = true`.
* **Эффект:** Любой игрок сервера может использовать станцию и получать продукцию, однако сам контракт резервирует 1 слот работника из лимита владельца (`Attribute.PUBLIC_CONTRACTS`).
