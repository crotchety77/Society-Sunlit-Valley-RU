# ✨ Шайни-разведение (Shiny Breeding)
> **Сборка:** `Society: Sunlit Cobblemon 4.1.x`  
> **Контекст:** [README.md](README.md) | [Наследование](inheritance.md) | [Оптимизация](breeding_optimization.md)

---

## 🎮 Player Knowledge

### 1. Базовый шанс Shiny
* При обычном разведении покемонов, пойманных одним и тем же игроком, базовый шанс появления Shiny у потомка равен **`1 / 4096` (~0.0244%)**.

### 2. Влияют ли Shiny-родители или Shiny Ditto?
* **НЕТ.** Если один родитель Shiny, оба родителя Shiny или используется Shiny Ditto, шанс Shiny у яйца **НЕ увеличивается**. В коде сборки этот статус у родителей игнорируется.

### 3. Метод Масуды (Masuda Method) — Главный способ повышения шанса
* **Что это такое:** Разведение двух совместимых покемонов, принадлежащих **разным тренерам** (разный `Original Trainer` / полученные через обмен с другим игроком).
* **Бонус Масуды:** Увеличивает вероятность Shiny ровно в **4 раза**!
* **Итоговый шанс при Масуде:** **`1 / 1024` (~0.0976%)**.

### 4. Влияние Shiny Charm (Амулета блеска)
* **Не влияет на яйца:** В установленной версии Cobbreeding проверка Shiny Charm при расчёте яиц отсутствует. Shiny Charm в Cobblemon действует исключительно на генерацию диких покемонов в мире.

---

## 📊 Математика вероятностей Shiny

Формула вероятности получить хотя бы одного Shiny за $n$ яиц:
$$P(\ge 1\text{ Shiny}) = 1 - (1 - p)^n$$

| Число яиц ($n$) | Обычное разведение ($p = 1/4096$) | Метод Масуды ($p = 1/1024$) ⭐ |
| :---: | :---: | :---: |
| **1 яйцо** | 0.0244% | 0.0976% |
| **10 яиц** | 0.244% | 0.972% |
| **50 яиц** | 1.213% | 4.771% |
| **100 яиц** | 2.411% | 9.310% |
| **250 яиц** | 5.922% | 21.67% |
| **500 яиц** | 11.49% | **38.64%** |
| **1000 яиц** | 21.67% | **62.37%** |
| **2000 яиц** | 38.65% | **85.84%** |
| **Матожидание ($N$)** | **4 096 яиц** | **1 024 яйца** |

---

## ⚙️ Technical Evidence

### 1. Метод расчёта в байткоде (`PastureUtilities.calcShiny`)
```kotlin
// Декомпилированный метод calcShiny() из PastureUtilities.class
private fun calcShiny(parents: Pair<Pokemon, Pokemon>): Boolean? {
    val method = Cobbreeding.config.shinyMethod // "masuda"
    if (method == "disabled") return null
    
    val multiplier = Cobbreeding.config.shinyMultiplier // 4.0
    var rate = Cobblemon.config.shinyRate // 4096.0 из config/cobblemon/main.json
    
    // Ветка "crystal" отключена в конфиге
    if (method.contains("crystal")) {
        if (parents.first.shiny) rate /= multiplier
        if (parents.second.shiny) rate /= multiplier
    }
    
    // Ветка "masuda" АКТИВНА:
    if (method.contains("masuda")) {
        val ot1 = parents.first.originalTrainer ?: parents.first.ownerPlayer?.uuid?.toString()
        val ot2 = parents.second.originalTrainer ?: parents.second.ownerPlayer?.uuid?.toString()
        
        // Если идентификаторы тренеров различаются:
        if (ot1 != ot2) {
            rate /= multiplier // 4096.0 / 4.0 = 1024.0
        }
    }
    
    if (rate < 1f) return true
    return Random.nextInt(0, rate.toInt()) == 0
}
```

### 2. Конфигурационные файлы
* `config/cobblemon/main.json`: `"shinyRate": 4096.0`
* `config/cobbreeding/main.json`: `"shinyMethod": "masuda"`, `"shinyMultiplier": 4.0`
