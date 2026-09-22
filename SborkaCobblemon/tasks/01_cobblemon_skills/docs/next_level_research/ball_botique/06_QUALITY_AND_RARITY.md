# ⭐ 06_QUALITY_AND_RARITY — Система Качества (Quality) и Шайни

## 1. Градация качества капсул

В коде сборки качество капсулы задаётся целочисленным или дробным значением в NBT-теге предмета `gachamon_capsule`:
- `{quality_food: {quality: 0}}` $\rightarrow$ **Regular** (Обычное / Без звезды)
- `{quality_food: {quality: 1}}` $\rightarrow$ **Silver** (Серебряное / ⚪ Серебряная звезда)
- `{quality_food: {quality: 2}}` $\rightarrow$ **Gold** (Золотое / 🟡 Золотая звезда)
- `{quality_food: {quality: 3}}` $\rightarrow$ **Iridium** (Иридиевое / 🟣 Иридиевая звезда)

---

## 2. Влияние качества на содержимое (Пул наград)

В скрипте `kubejs/server_scripts/cobblemon/cobblemonGachaPools.js` логика фильтрации пула реализована следующим кодом:

```javascript
function getGachaPool(capsuleType, quality, player) {
    let specialPool = specialGachaSpawns[capsuleType] || [];
    let basePool = baseGachaSpawns || [];
    
    let hasGachamonbler = player && player.stages && player.stages.has("the_gachamonbler");

    // ИРИДИЕВОЕ КАЧЕСТВО (или Золотое с перком the_gachamonbler)
    if (quality >= (hasGachamonbler ? 2.0 : 3.0)) {
        return specialPool; // 100% ЧИСТЫЙ ТЕМАТИЧЕСКИЙ ПУЛ!
    }
    
    // ДЛЯ ВСЕХ ОСТАЛЬНЫХ УРОВНЕЙ КАЧЕСТВА:
    return basePool.concat(specialPool); // Пул разбавлен 15 обычными покемонами!
}
```

### 📊 Вероятность получить целевого покемона в зависимости от качества:

Предположим, в тематическом пуле $N$ покемонов с весом 10 каждый (общий вес $10N$), а в базовом пуле 15 покемонов с весом 10 (общий вес 150):

| Качество капсулы | Состав пула | Шанс получить целевого (на примере Starter Pack, $N=27$) | Шанс получить мусор из Base Pool |
| :--- | :--- | :---: | :---: |
| **Regular (Q0)** | Base Pool (150) + Special Pool (270) | $\frac{270}{420} \approx \mathbf{64.3\%}$ | **35.7%** (Pidgey, Bidoof...) |
| **Silver (Q1)** | Base Pool (150) + Special Pool (270) | $\frac{270}{420} \approx \mathbf{64.3\%}$ | **35.7%** |
| **Gold (Q2)** *(без перка)* | Base Pool (150) + Special Pool (270) | $\frac{270}{420} \approx \mathbf{64.3\%}$ | **35.7%** |
| **Gold (Q2)** *(с перком)* | **Только Special Pool (270)** | $\mathbf{100.0\%}$ | **0%** |
| **Iridium (Q3)** | **Только Special Pool (270)** | $\mathbf{100.0\%}$ **(ГАРАНТИЯ)** | **0%** |

---

## 3. Влияние качества на шанс Шайни (Shiny Chance)

Шанс появления Шайни-версии покемона вычисляется функцией `getShinyChance(quality, player)`:

| Уровень качества | Базовый шанс Шайни | В соотношении (1 из X) | С перком `the_gachamonbler` ($\times 2$) | С перком `the_red_and_the_black` (Reroll) |
| :--- | :---: | :---: | :---: | :---: |
| **Regular (Q0)** | **0.10%** (`0.0010`) | 1 из 1,000 | 0.20% (1 из 500) | $\approx 0.20\%$ |
| **Silver (Q1)** | **0.25%** (`0.0025`) | 1 из 400 | 0.50% (1 из 200) | $\approx 0.50\%$ |
| **Gold (Q2)** | **0.50%** (`0.0050`) | 1 из 200 | 1.00% (1 из 100) | $\approx 0.99\%$ |
| **Iridium (Q3)** | **1.00%** (`0.0100`) | **1 из 100** | **2.00%** (**1 из 50**) | $\approx \mathbf{1.99\%}$ |

> **Комбинация перков тренера**:
> Если у игрока открыты оба навыка ветки Гачамона (`the_gachamonbler` + `the_red_and_the_black`), то при открытии **Иридиевой капсулы** эффективный шанс получить Шайни-покемона составляет:
> $$P(\text{Shiny}) = 1 - (1 - 0.02)^2 = 1 - 0.9604 = \mathbf{3.96\%} \quad (\approx \mathbf{1 \text{ из } 25})$$
