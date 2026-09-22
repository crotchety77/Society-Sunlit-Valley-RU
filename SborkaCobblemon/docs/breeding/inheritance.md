# 🧬 Наследование характеристик (Inheritance)
> **Сборка:** `Society: Sunlit Cobblemon 4.1.x`  
> **Контекст:** [README.md](README.md) | [Совместимость](breeding_compatibility.md) | [Оптимизация](breeding_optimization.md)

---

## 🎮 Player Knowledge

При вылуплении покемон получает набор характеристик, частично унаследованных от родителей и частично сгенерированных случайно:

### 1. IV (Индивидуальные значения характеристик: 0–31)
* **По умолчанию (без предметов):** Наследуются **3 случайных IV** от родителей (выбираются случайно между отцом и матерью). Оставшиеся 3 IV генерируются случайно (0–31).
* **Узел судьбы (`cobblemon:destiny_knot`):** Если **любой** из родителей держит Узел судьбы, наследуются **5 IV** от родителей, и только 1 IV генерируется случайно.
* **Силовые предметы (Power Items):**
  * `Power Weight` $\rightarrow$ гарантирует передачу **HP IV**.
  * `Power Bracer` $\rightarrow$ гарантирует передачу **Attack IV**.
  * `Power Belt` $\rightarrow$ гарантирует передачу **Defense IV**.
  * `Power Lens` $\rightarrow$ гарантирует передачу **Sp. Attack IV**.
  * `Power Band` $\rightarrow$ гарантирует передачу **Sp. Defense IV**.
  * `Power Anklet` $\rightarrow$ гарантирует передачу **Speed IV**.
  *(Указанный стат наследуется со 100% вероятностью от родителя, держащего предмет)*.

---

### 2. Nature (Характер)
* **Без предметов:** Случайный из 25 характеров (шанс 4%).
* **Вечный камень (`cobblemon:everstone`):** Если родитель держит Вечный камень, его характер передаётся потомку со **100% вероятностью**. Если Вечный камень держат оба родителя — шанс 50/50 между их характерами.

---

### 3. Ability (Способности и Скрытые способности)
Способность потомка рассчитывается на основе способности **Матери** (или не-Ditto покемона):
* **Если у матери Скрытая способность (Hidden Ability):**
  * **60% шанс** передать Скрытую способность.
  * **40% шанс** получить одну из стандартных способностей.
* **Если у матери Обычная способность:**
  * **80% шанс** унаследовать именно эту способность матери.
  * **20% шанс** получить вторую обычную способность вида.
  * ⚠️ **0% шанс на скрытую способность** (скрытую способность нельзя вывести с нуля от матери с обычной способностью).

---

### 4. Poké Ball (Покебол)
* **Разные виды родителей:** Потомок всегда наследует покебол **Матери**.
* **Одинаковый вид родителей:** Шанс **50% на покебол Матери** и **50% на покебол Отца**.
* **Скрещивание с Ditto:** Всегда наследуется покебол **партнёра Ditto** (независимо от пола).
* 🚫 **Исключения:** `Master Ball` и `Cherish Ball` **никогда не наследуются** и при разведении автоматически конвертируются в обычный `Poke Ball`.

---

### 5. Egg Moves (Яйцевые атаки) и Зеркальная трава (Mirror Herb)
* Если отец или мать знают атаки из пула `eggMoves` вида потомка, новорожденный покемон появляется на свет с этими атаками.
* **Зеркальная трава (`cobblemon:mirror_herb`):**  
  Работает прямо на Пастбище! Дайте покемону Зеркальную траву и освободите у него слот атаки (чтобы было $\le 3$ атак). Поместите его в Пастбище вместе с другим покемоном, знающим нужную атаку — покемон мгновенно скопирует яйцевой приём!

---

## ⚙️ Technical Evidence

### 1. Алгоритм IV (`PastureUtilities.calcStats`)
```kotlin
// Декомпилированный фрагмент PastureUtilities.calcStats()
val inheritedStats = mutableSetOf<Stat>()
val powerItemMap = mapOf(
    parent1 to powerItemToIV(parent1.heldItem().item),
    parent2 to powerItemToIV(parent2.heldItem().item)
).filterValues { it != null }

// 1. Применение Power Items:
if (powerItemMap.isNotEmpty()) {
    val (parent, stat) = powerItemMap.entries.random()
    childIVs.set(stat, parent.ivs.get(stat))
    availableStats.remove(stat)
}

// 2. Определение числа наследуемых IV:
val totalInherit = if (parent1.heldItem().is(DESTINY_KNOT) || parent2.heldItem().is(DESTINY_KNOT)) 5 else 3

// 3. Добор оставшихся IV:
repeat(totalInherit - if (powerItemMap.isNotEmpty()) 1 else 0) {
    val stat = availableStats.random()
    val parent = parents.random()
    childIVs.set(stat, parent.ivs.get(stat))
    availableStats.remove(stat)
}
```

### 2. Алгоритм передачи характера (`PastureUtilities.calcNature`)
```kotlin
// Декомпилированный фрагмент PastureUtilities.calcNature()
val everstones = listOfNotNull(
    if (parent1.heldItem().is(EVERSTONE)) parent1.nature else null,
    if (parent2.heldItem().is(EVERSTONE)) parent2.nature else null
)
return if (everstones.isNotEmpty()) {
    everstones.random() // 100% от одного или 50/50 при двух
} else {
    Natures.getRandomNature() // 1 из 25
}
```

### 3. Алгоритм передачи способностей (`PastureUtilities.calcAbility`)
В байткоде `PastureUtilities.calcAbility` используется сплит по приоритету (`Priority.LOW` для HA):
* Если `mother.ability.priority == Priority.LOW`: ролл `nextUInt(10) < 6` $\rightarrow$ **60% HA**.
* Если обычная способность: ролл `nextUInt(10) < 8` $\rightarrow$ **80% Mother Ability**.
