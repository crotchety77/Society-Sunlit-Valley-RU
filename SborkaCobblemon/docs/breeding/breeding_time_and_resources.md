# ⏱️ Время и ресурсы разведения (Time & Resources)
> **Сборка:** `Society: Sunlit Cobblemon 4.1.x`  
> **Контекст:** [README.md](README.md) | [Механика](breeding_mechanics.md) | [Оптимизация](breeding_optimization.md)

---

## 🎮 Player Knowledge

### 1. Время получения яйца на Пастбище
* **Периодичность проверки:** Пастбище производит попытку создать яйцо каждые **10 минут** реального времени.
* **Шанс за одну попытку:** **50%**.
* **Математическое ожидание:** В среднем на 1 яйцо уходит **20 минут** (2 цикла).

### 2. Инкубация яйца в инвентаре
* Яйцо инкубируется, пока находится в инвентаре игрока.
* Время вылупления рассчитывается по формуле **Egg Cycles** (циклы шагов вида покемона):
  * **1 Egg Cycle** в сборке = **30 секунд (600 тиков)**.
* **Ускорение инкубации (х2 скорость):**  
  Если в вашей активной группе покемонов (Party) есть хотя бы один покемон со способностью **`Flame Body`**, **`Magma Armor`** или **`Steam Engine`**, время инкубации любого яйца в инвентаре **сокращается ровно в 2 раза (–50% времени)**!

#### Примеры времени инкубации популярных покемонов:

| Покемон | Egg Cycles | Время без инкубатора | Время с Flame Body / Magma Armor |
| :--- | :---: | :---: | :---: |
| **Magikarp** | 5 | 2.5 мин (3 000 ticks) | **1.25 мин (1 500 ticks)** |
| **Pikachu / Lucario / Zorua** | 10 | 5.0 мин (6 000 ticks) | **2.50 мин (3 000 ticks)** |
| **Starter (Charmander, Froakie...)** | 20 | 10.0 мин (12 000 ticks) | **5.00 мин (6 000 ticks)** |
| **Eevee** | 35 | 17.5 мин (21 000 ticks) | **8.75 мин (10 500 ticks)** |
| **Pseudo-Legendary (Dratini, Larvitar, Gible...)** | 40 | 20.0 мин (24 000 ticks) | **10.00 мин (12 000 ticks)** |

### 3. Расходные ресурсы
* **Разведение полностью бесплатно:** Никаких расходуемых предметов, ягод, денег или энергии во время процесса разведения не тратится.
* Единственная инвестиция — скрафтить и поставить сам блок **Пастбища** (`cobblemon:pasture`).

---

## ⚙️ Technical Evidence

### 1. Конфигурация таймеров (`config/cobbreeding/main.json`)
```json
{
  "eggCheckTicks": 12000,
  "eggCheckChance": 0.5,
  "eggHatchMultiplier": 1.0,
  "shinyMethod": "masuda",
  "shinyMultiplier": 4.0
}
```

### 2. Логика инвентарного тика яйца (`PokemonEgg.class`)
```kotlin
// Декомпилированный метод inventoryTick() в PokemonEgg.class
override fun inventoryTick(stack: ItemStack, level: Level, entity: Entity, slot: int, isSelected: boolean) {
    if (level.isClientSide) return
    
    var tickTime = stack.tag?.getInt("tickTime") ?: 0
    tickTime++
    stack.tag.putInt("tickTime", tickTime)
    
    // Каждые 20 тиков (1 секунда):
    if (tickTime >= 20) {
        stack.tag.putInt("tickTime", 0)
        var timer = stack.tag?.getInt("timer") ?: 100
        
        // Базовое уменьшение:
        timer -= 20
        
        // Проверка способностей инкубатора игрока:
        val registry = Cobbreeding.INCUBATOR_ABILITIES_REGISTRY
        if (registry.shouldHatchFaster((entity as Player).uuidAsString)) {
            timer -= 20 // Дополнительные -20 тиков за секунду (итого -40 тиков/сек)
        }
        
        stack.tag.putInt("timer", timer)
        
        // Если таймер истек — вылупление:
        if (timer <= 0) {
            hatchPokemon(stack, level, entity)
        }
    }
}
```

### 3. Реестр способностей инкубатора (`IncubatorAbilitiesRegistry.class`)
Способности регистрируются через `com.cobblemon.mod.common.api.abilities.Abilities`:
* `flamebody` (Flame Body)
* `magmaarmor` (Magma Armor)
* `steamengine` (Steam Engine)
Эффекты нескольких покемонов с этими способностями в группе не стакаются (фиксированный модификатор `shouldHatchFaster = true`).
