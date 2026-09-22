# ⚠️ Особые случаи и исключения (Special Cases)
> **Сборка:** `Society: Sunlit Cobblemon 4.1.x`  
> **Контекст:** [README.md](README.md) | [Совместимость](breeding_compatibility.md) | [Оптимизация](breeding_optimization.md)

---

## 🎮 Player Knowledge

### 1. Покемоны, которые НЕ МОГУТ размножаться (`EggGroup.UNDISCOVERED`)
Попытка посадить на Пастбище следующих покемонов **никогда не даст яйцо** (даже в паре с Ditto):
* **Покемоны-малыши (Baby Pokémon):** Pichu, Cleffa, Igglybuff, Togepi, Tyrogue, Smoochum, Elekid, Magby, Azurill, Wynaut, Budew, Chingling, Bonsly, Mime Jr., Happiny, Munchlax, Riolu, Mantyke, Toxel. *(Чтобы разводить их, нужно сначала развить их во взрослую форму!)*.
* **Легендарные и Мифические покемоны:** Mewtwo, Zapdos, Rayquaza, Arceus, Koraidon и др.
* **Ультра-чудовища (Ultra Beasts) и Парадоксы (Paradox Pokémon):** Nihilego, Roaring Moon, Iron Valiant и др.

---

### 2. Скрещивание Ditto + Ditto
* **По умолчанию отключено:** Пара из двух Ditto **не производит яиц** (`dittoAndDittoRandomEgg: false` в конфиге сборки).

---

### 3. Бесполые покемоны (Genderless)
* Покемоны без пола (Magnemite, Voltorb, Staryu, Porygon, Beldum, Bronzor, Rotom, Klink, Golett, Cryogonal, Dhelmise, Sinistea, Falinks и др.) могут размножаться **ИСКЛЮЧИТЕЛЬНО с Ditto**. Они не могут скрещиваться друг с другом.

---

### 4. Региональные формы (Regional Forms)
В коде аддона зашита специальная обработка эволюционных ветвей региональных вариантов:
* **Perrserker** $\rightarrow$ производит **Галарского Мяута** (`Galarian Meowth`).
* **Sirfetch'd** $\rightarrow$ производит **Галарского Фарфетчда** (`Galarian Farfetch'd`).
* **Cursola** $\rightarrow$ производит **Галарскую Корсолу** (`Galarian Corsola`).
* **Obstagoon** $\rightarrow$ производит **Галарского Зигзагуна** (`Galarian Zigzagoon`).
* **Runerigus** $\rightarrow$ производит **Галарского Ямаска** (`Galarian Yamask`).
* **Clodsire** $\rightarrow$ производит **Палдейского Вупера** (`Paldean Wooper`).
* **Overqwil** $\rightarrow$ производит **Хисуи Квилфиша** (`Hisuian Qwilfish`).
* **Sneasler** $\rightarrow$ производит **Хисуи Снизла** (`Hisuian Sneasel`).
* **Basculegion** $\rightarrow$ производит **Белополосого Баскулина** (`White-Striped Basculin`).

> 💡 **Правило Вечного камня для региональных форм:**  
> Если региональный родитель держит **Вечный камень (`Everstone`)**, потомок гарантированно наследует его региональную форму. Без Вечного камня покемон вылупляется в стандартной/канто/первичной форме (если у базового вида есть обычная форма).

---

## ⚙️ Technical Evidence

### 1. Блокировка группы Undiscovered (`PastureUtilities.class`)
```kotlin
if (eggGroups1.contains(EggGroup.UNDISCOVERED) || eggGroups2.contains(EggGroup.UNDISCOVERED)) {
    continue // Исключение из пула возможных яиц
}
```

### 2. Хардкод предэволюций региональных форм (`PastureUtilities.getBaby`)
```kotlin
// Декомпилированный фрагмент PastureUtilities.getBaby()
when (mother.species.name) {
    "Perrserker", "Sirfetch'd", "Cursola", "Obstagoon", "Runerigus", 
    "Clodsire", "Overqwil", "Sneasler" -> return babySpecies.forms[1]
    "Basculegion" -> return babySpecies.forms[2]
}
```

### 3. Конфигурация Ditto (`config/cobbreeding/main.json`)
```json
{
  "dittoAndDittoRandomEgg": false,
  "dittoAndDittoAllowLegendary": false
}
```
