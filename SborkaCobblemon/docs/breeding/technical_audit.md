# 🔬 Технический аудит и доказательная база (Technical Audit)
> **Сборка:** `Society: Sunlit Cobblemon 4.1.x`  
> **Контекст:** [README.md](README.md) | [Механика](breeding_mechanics.md) | [Шайни-разведение](shiny_breeding.md)

---

## 📦 Модули и используемые компоненты

1. **Базовое ядро:** `Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar`
   * Содержит основные сущности `com.cobblemon.mod.common.pokemon.Pokemon`, `Species`, `FormData`, `IVs`, `Natures`, `Stats`.
2. **Аддон разведения:** `Cobbreeding-forge-1.7.4.jar`
   * Пакет: `ludichat.cobbreeding`
   * Классы: `Cobbreeding`, `Config`, `PastureUtilities`, `PokemonEgg`, `IncubatorAbilitiesRegistry`, `PastureBreedingData`.
   * Миксины: `PokemonPastureBlockEntityMixin`, `PastureBlockMixin`.

---

## ⚙️ Файлы активных конфигураций

### 1. `config/cobbreeding/main.json`
```json
{
  "eggCheckTicks": 12000,
  "eggCheckChance": 0.5,
  "eggHatchMultiplier": 1.0,
  "shinyMethod": "masuda",
  "shinyMultiplier": 4.0,
  "hiddenAbilitiesEnabled": true,
  "forcedAbilitiesEnabled": false,
  "dittoAndDittoRandomEgg": false,
  "dittoAndDittoAllowLegendary": false
}
```

### 2. `config/cobblemon/main.json`
```json
{
  "shinyRate": 4096.0
}
```

---

## 📜 Ключевые методы байткода (Decompiled Reference)

### 1. Расчёт шанса Shiny (`PastureUtilities.calcShiny`)
```kotlin
private fun calcShiny(parents: Pair<Pokemon, Pokemon>): Boolean? {
    val method = Cobbreeding.config.shinyMethod
    if (method == "disabled") return null
    val multiplier = Cobbreeding.config.shinyMultiplier
    var rate = Cobblemon.config.shinyRate
    
    if (method.contains("crystal")) {
        if (parents.first.shiny) rate /= multiplier
        if (parents.second.shiny) rate /= multiplier
    }
    
    if (method.contains("masuda")) {
        val ot1 = parents.first.originalTrainer ?: parents.first.ownerPlayer?.uuid?.toString()
        val ot2 = parents.second.originalTrainer ?: parents.second.ownerPlayer?.uuid?.toString()
        if (ot1 != ot2) {
            rate /= multiplier
        }
    }
    
    if (rate < 1f) return true
    return Random.nextInt(0, rate.toInt()) == 0
}
```

### 2. Наследование IV (`PastureUtilities.calcStats`)
```kotlin
private fun calcStats(parents: Pair<Pokemon, Pokemon>): IVs {
    val childIVs = IVs()
    val availableStats = Stats.values().toMutableSet()
    val parent1 = parents.first
    val parent2 = parents.second
    
    val power1 = powerItemToIV(parent1.heldItem().item)
    val power2 = powerItemToIV(parent2.heldItem().item)
    
    // Power Items гарантируют передачу стата
    val powerMap = listOfNotNull(
        if (power1 != null) parent1 to power1 else null,
        if (power2 != null) parent2 to power2 else null
    ).toMap()
    
    if (powerMap.isNotEmpty()) {
        val (p, stat) = powerMap.entries.random()
        childIVs.set(stat, p.ivs.get(stat))
        availableStats.remove(stat)
    }
    
    val count = if (parent1.heldItem().is(DESTINY_KNOT) || parent2.heldItem().is(DESTINY_KNOT)) 4 else 2
    repeat(count) {
        val stat = availableStats.random()
        val p = parents.random()
        childIVs.set(stat, p.ivs.get(stat))
        availableStats.remove(stat)
    }
    
    return childIVs
}
```

### 3. Инкубация яйца и способности (`PokemonEgg.class`)
```kotlin
// Ускорение таймера инкубации при наличии Flame Body, Magma Armor или Steam Engine
if (Cobbreeding.INCUBATOR_ABILITIES_REGISTRY.shouldHatchFaster(player.uuidAsString)) {
    timer -= 20 // Дополнительное списание тиков
}
```

---

## 🎯 Evidence Policy & Статус верификации

* **Cobbreeding 1.7.4:** Полный реверс-инжиниринг через `javap -p -c -constants`.
* **Cobblemon 1.5.2:** Проверены исходники структур данных `Pokemon`, `Species`, `EggGroup`, `IVs`.
* **KubeJS:** Подтверждено отсутствие переопределений логики `calcShiny` и `calcStats` в серверных скриптах сборки.
