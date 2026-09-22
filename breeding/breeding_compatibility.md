# 👫 Совместимость родителей (Breeding Compatibility)
> **Сборка:** `Society: Sunlit Cobblemon 4.1.x`  
> **Контекст:** [README.md](README.md) | [Наследование](inheritance.md) | [Особые случаи](special_cases.md)

---

## 🎮 Player Knowledge

Чтобы два покемона на Пастбище могли произвести яйцо, они должны соответствовать строгим правилам совместимости:

### 1. Правило полов
* **Стандартная пара:** Должны быть разнополыми — строго **Самец (Male) + Самка (Female)**.
* **Скрещивание с Дитто (Ditto):**
  * Ditto может спариваться с Самцом (**Male + Ditto**).
  * Ditto может спариваться с Самкой (**Female + Ditto**).
  * Ditto может спариваться с Бесполым покемоном (**Genderless + Ditto**).
* 🚫 **Несовместимо:** Самец + Самец, Самка + Самка, Бесполый + Бесполый (без Ditto).

---

### 2. Группы яиц (Egg Groups)
Оба родителя должны иметь **хотя бы одну общую группу яиц** из следующего списка:
1. `Monster`
2. `Water 1`, `Water 2`, `Water 3`
3. `Bug`
4. `Flying`
5. `Field`
6. `Fairy`
7. `Grass`
8. `Human-Like`
9. `Mineral`
10. `Amorphous`
11. `Dragon`

---

### 3. Определение вида потомка (Species Selection)
* **Стандартная пара:** Потомок всегда рождается тем же видом, что и **Мать (Самка)**.
* **Скрещивание с Ditto:** Потомок всегда рождается видом **партнёра Ditto**.
* **Стадия эволюции:** Потомок всегда вылупляется на **низшей базовой стадии эволюции** (Pre-Evolution), за исключением особых предметов благовоний (Incenses), если они предусмотрены видом.

---

## ⚙️ Technical Evidence

### 1. Проверка совместимости (`PastureUtilities.getPossibleEggs`)
```kotlin
// Декомпилированный алгоритм getPossibleEggs()
val eggGroups1 = pokemon1.species.eggGroups
val eggGroups2 = pokemon2.species.eggGroups

// 1. Проверка группы Undiscovered (не способны размножаться):
if (eggGroups1.contains(EggGroup.UNDISCOVERED) || eggGroups2.contains(EggGroup.UNDISCOVERED)) {
    continue // Разведение невозможно
}

// 2. Ветка Ditto:
if (eggGroups1.contains(EggGroup.DITTO)) {
    val babyForm = dittoBreed(pokemon2)
    if (babyForm != null) registerPair(babyForm, pokemon2, pokemon1)
    continue
}
if (eggGroups2.contains(EggGroup.DITTO)) {
    val babyForm = dittoBreed(pokemon1)
    if (babyForm != null) registerPair(babyForm, pokemon1, pokemon2)
    continue
}

// 3. Стандартная пара (разнополые + пересечение Egg Groups):
if (pokemon1.gender != pokemon2.gender && pokemon1.gender != Gender.GENDERLESS && pokemon2.gender != Gender.GENDERLESS) {
    val hasSharedGroup = eggGroups1.any { eggGroups2.contains(it) }
    if (hasSharedGroup) {
        val mother = if (pokemon1.gender == Gender.FEMALE) pokemon1 else pokemon2
        val father = if (pokemon1.gender == Gender.MALE) pokemon1 else pokemon2
        val babyForm = getBaby(mother)
        registerPair(babyForm, mother, father)
    }
}
```

### 2. Поиск предэволюции (`PastureUtilities.getBaby`)
```kotlin
// Метод отката эволюции до базовой стадии
var currentSpecies = mother.species
while (currentSpecies.preEvolution != null) {
    currentSpecies = currentSpecies.preEvolution!!.species
}
return currentSpecies.standardForm
```
