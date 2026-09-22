# 🌾 Механика разведения (Breeding Mechanics)
> **Сборка:** `Society: Sunlit Cobblemon 4.1.x`  
> **Контекст:** [README.md](README.md) | [Время и ресурсы](breeding_time_and_resources.md) | [Совместимость](breeding_compatibility.md)

---

## 🎮 Player Knowledge

### 1. Как работает процесс разведения
Разведение покемонов в сборке происходит с помощью стандартного блока **Пастбища (`cobblemon:pasture`)**:
1. **Установка блока:** Разместите Пастбище в мире (рекомендуется огородить загон, чтобы покемоны не разбегались).
2. **Привязка родителей:** Нажмите **ПКМ** по блоку Пастбища. В открывшемся интерфейсе ПК выберите и привяжите двух (или более) совместимых покемонов.
3. **Автоматический цикл:** Покемоны гуляют в радиусе пастбища. Каждые **10 минут** блок автоматически проверяет наличие совместимых пар и с вероятностью **50%** генерирует яйцо.
4. **Визуальный индикатор и забор:**
   * Когда яйцо готово, в нижней части модели блока Пастбища появляется **физическое яйцо покемона**, и раздаётся звук высиживания (`block.sniffer_egg.hatch` / `item.egg.lay`).
   * Игрок подходит к Пастбищу и нажимает **ПКМ пустой рукой** (или открывает инвентарь блока), забирая яйцо в свой инвентарь.
   * После забора яйца слот пастбища освобождается, и запускается следующий цикл ожидания.

---

## ⚙️ Technical Evidence

### 1. Перехват функционала Пастбища (Mixins)
Внедрение логики разведения в Cobblemon Pasture реализовано через два миксина в моде `Cobbreeding-forge-1.7.4.jar`:
* `ludichat.cobbreeding.mixin.PokemonPastureBlockEntityMixin` — добавляет таймер `time`, список предметов `items` (хранилище яйца) и метод тика `tick()`.
* `ludichat.cobbreeding.mixin.PastureBlockMixin` — обрабатывает взаимодействие игрока по ПКМ (`use()`), извлечение яйца и регистрацию свойства блока `HAS_EGG`.

### 2. Логика тика и генерации яйца
```kotlin
// Декомпилированный фрагмент PokemonPastureBlockEntityMixin.class
if (data.time >= config.eggCheckTicks) { // 12 000 ticks
    data.time = 0
    PastureUtilities.applyMirrorHerb(pasturedPokemon) // Синхронизация атак Зеркальной травы
    val roll = Math.random()
    val chance = config.eggCheckChance.toDouble() // 0.5 (50%)
    
    // Если слот яйца пуст и бросок успешен:
    if (data.egg[0].isEmpty && roll >= 1.0 - chance) {
        val eggInfo = PastureUtilities.chooseEgg(pasturedPokemon)
        if (eggInfo != null) {
            val eggStack = ItemStack(Cobbreeding.EGG_ITEM.get())
            eggInfo.toNbt(eggStack.getOrCreateTag())
            
            // Запись таймера инкубации:
            val timer = (eggInfo.species.eggCycles * 600 * config.eggHatchMultiplier).toInt()
            eggStack.tag.putInt("timer", timer)
            
            data.egg[0] = eggStack
            level.playSound(null, blockPos, SoundEvents.SNIFFER_EGG_HATCH, SoundSource.BLOCKS, 1f, 1f)
        }
    }
}
```

### 3. Индикатор яйца в блоке
* Регистрация свойства блока: `ludichat.cobbreeding.CustomProperties.HAS_EGG` (BooleanProperty).
* Модель блока: `assets/cobbreeding/models/block/pasture_bottom_egg.json`.
* Предмет яйца в инвентаре: `cobbreeding:pokemon_egg` (`ludichat.cobbreeding.PokemonEgg`).
