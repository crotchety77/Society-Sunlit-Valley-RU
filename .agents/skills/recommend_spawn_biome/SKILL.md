---
name: recommend_spawn_biome
description: Определение математически и практически лучшего биома для поиска и поимки покемона в Cobblemon на основе подтверждённого кода спавнера (Two-Stage Hierarchical Sampling), весов в Bucket, давления Common-пула на мобкап и условий окружения.
---

# Skill: `recommend_spawn_biome`

## Цель

По имени целевого покемона определить **математически лучший** (Mathematical Best) и **практически лучший** (Practical Best) биом для его поиска и поимки в текущей сборке Minecraft/Cobblemon.

> `[CORE PRINCIPLE]`
> **Математический шанс и практические условия охоты НИКОГДА не смешиваются в один искусственный "Score".**
> Игроку всегда предоставляются два независимых вердикта:
> 1. **Mathematical Best** — где максимальна чистая вероятность выбора покемона при наступлении стадии weighted/percentage selection.
> 2. **Practical Best** — где процесс охоты наиболее стабилен, быстр и не подавляется мобкапом, труднодоступным рельефом или нулевой видимостью.

---

## Evidence Policy

Приоритет источников доказательств:
1. `[FACT]` **Код текущего Cobblemon JAR / декомпилированный байткод** — высший авторитет механик и алгоритмов.
2. `[FACT]` **Spawn Pool JSON текущей сборки** (`data/cobblemon/spawn_pool_world/`).
3. `[FACT]` **Biome Tags текущей сборки** (`data/cobblemon/tags/worldgen/biome/`).
4. `[FACT]` **Конфигурация текущей сборки** (`CobblemonConfig`, `BestSpawnerConfig`).
5. `[FACT]` **Species / Evolution данные текущей сборки** (`data/cobblemon/species/`).
6. `[INFERENCE]` **Практический вывод** — логическое следствие из подтверждённых кодом факторов (например, открытый рельеф vs замкнутые пещеры).
7. `[UNKNOWN]` **Не установлено** — если механика или количественная связь не доказаны кодом (запрещено выдумывать формулы/числа).

---

## 1. Архитектура спавнера Cobblemon

В Cobblemon используется **двухступенчатый иерархический спавн** (*Two-Stage Hierarchical Sampling*):

```
                       [ Spawner Tick ]
                              │
                    [ 1. chooseBucket() ]
             (Common 93.8%, Uncommon 5%, Rare 1%, Ultra-Rare 0.2%)
                              │
                    [ 2. World Prospecting ]
          (Проверка Mob Cap: если nearby >= limit → отмена)
                              │
                [ 3. BucketPrecalculation ]
             (Отсекаются ВСЕ покемоны других Bucket)
                              │
                [ 4. SpawnDetail.isSatisfiedBy ]
          (Фильтрация по биому, Y, свету, погоде, блокам)
                              │
          [ 5. Matching Entries in Selected Bucket ]
                              │
          [ 6. Weight / Percentage Selection Stage ]
```

---

## 2. Математическая модель

### 1. Bucket Probability
Bucket выбирается первым и независимо от состава Pokémon внутри других Bucket:

$$P(\text{Bucket}) = \frac{\text{BucketWeight}}{\sum \text{AllBucketWeights}}$$

`[FACT]` Для текущей конфигурации сборки (`BestSpawnerConfig`):
* **Common** = $93.8\%$ ($0.938$)
* **Uncommon** = $5.0\%$ ($0.05$)
* **Rare** = $1.0\%$ ($0.01$)
* **Ultra-Rare** = $0.2\%$ ($0.002$)

> `[FACT]` Количество и веса Pokémon в других Bucket **НЕ** изменяют вероятность выпадения выбранного Bucket.

### 2. Intra-Bucket Probability
После выбора Bucket движок рассматривает **ТОЛЬКО Matching Entries** выбранного Bucket, удовлетворяющие текущему `SpawnContext` (биомы/теги биомов, освещение, $Y$, блок под ногами, погода, небо).

Различаются два типа записей:
* **Weight-based entry:**
  $$P(\text{Target} \mid \text{Bucket}, \text{Context}) = \frac{\text{Weight}(\text{Target})}{\sum_{E \in \text{MatchingEntriesInBucket}(\text{Context})} \text{Weight}(E)}$$
* **Percentage-based entry:**
  Если запись использует фиксированный процент (`percentage > 0`), процентный механизм анализируется отдельно.
  `[RULE]` Запрещено искусственно преобразовывать `percentage` в `weight` или смешивать их в одну формулу. Если порядок или математическая связь между ними в данном контексте не установлены однозначно — помечать как `UNKNOWN`.

> `[IMPORTANT]`
> В знаменатель $\sum \text{Weight}$ включаются **ТОЛЬКО те покемоны выбранного Bucket, которые реально активны и проходят условия в данном конкретном Context**. Покемоны данного Bucket, не проходящие условия биома или высоты $Y$, в знаменатель НЕ включаются.

### 3. Selection Probability
Вероятность выбора Target на стадии weighted/percentage selection после того, как spawn pipeline дошёл до этой стадии:

$$P(\text{Target selected}) = P(\text{Bucket}) \times P(\text{Target} \mid \text{Bucket}, \text{Context})$$

> `[CRITICAL DEFINITION]`
> $P(\text{Target selected})$ — это вероятность выбора Target **при условии успешного прохождения спавн-пайплайна до стадии селекции**.
> Это **НЕ** является гарантированной вероятностью фактического появления покемона в мире на единицу игрового времени, так как до селекции выполняются проверки мобкапа, загрузки чанка, коллизий и наличия свободных блоков. Запрещено формулировать это как *"покемон гарантированно появится каждые X попыток"*.

### 4. Spawn Success & Практические факторы
Если точная вероятность успешного прохождения всего spawn pipeline (World Prospecting / Entity Cap / Block Collision) не может быть строго вычислена из кода: **НЕ рассчитывать её самостоятельно и не выдумывать искусственные проценты**.

Вместо этого указывать как отдельные практические факторы:
* **Entity Cap constraints** (лимит сущностей в чанке `pokemonPerChunk`);
* **Spawn Context constraints** (Surface / Underground / Submerged);
* **Spawn Position availability** (площадь и доступность подходящих блоков);
* **Common Pool Pressure** (давление Common-пула на мобкап).

### 5. Common Pool Pressure
Common Pokémon не уменьшают $P(\text{Rare})$ напрямую в математическом ролле. Они влияют на практическую эффективность охоты, если их фактический спавн приводит к заполнению доступного `entity cap` и последующей блокировке новых `spawn attempts`.

`[RULE]` Диагностическая сумма весов:
$$W_{\text{Common}} = \sum_{E \in \text{MatchingCommon}} \text{Weight}(E)$$
> `W_Common` является исключительно справочной характеристикой размера пула. `W_Common` **НЕ** является коэффициентом Entity Cap и **НЕ** используется для математического штрафа $P(\text{Target selected})$.

`[RULE]` Практическое **Common Pressure** оценивается качественной шкалой:
* **`Low`**
* **`Medium`**
* **`High`**
* **`Unknown`**

> `[PROHIBITION]`
> **Запрещено** автоматически назначать `Cave = High` или `Surface = Low` только по названию контекста!
> Оценка Common Pressure выводится на основании совокупности подтверждённых данных:
> 1. Состава Common-пула в данном биоме;
> 2. Условий спавна Common-мобов (свет, высота, блоки);
> 3. Доступности позиций спавна;
> 4. Скорости естественного деспавна (`CobblemonAgingDespawner`);
> 5. Фактической возможности игрока легко поддерживать свободное пространство (зачистка, обзор).
> Если количественная связь не подтверждена кодом — указывать `Unknown`.

---

## 3. Разделение Direct Wild Spawn и Acquisition Route

Для всей эволюционной ветки целевого покемона обязательно определяются два независимых понятия:

1. **Direct Wild Spawn**:
   > Может ли сам целевой Pokémon появиться в дикой природе в текущей сборке?
2. **Acquisition Route**:
   > Если целевой Pokémon не имеет подходящего wild spawn (или его шанс исчезающе мал), через какую предыдущую эволюционную форму его рационально получить?

*Пример:*
Для **Garchomp**:
* `Direct Wild Spawn`: Доступен (Rare, Surface Peaks, вес 0.06 / Cave Ultra-Rare, вес 0.1).
* `Acquisition Route`: **Gible** (Rare, Surface Peaks, вес 5.4 / Cave Ultra-Rare, вес 9.0) $\rightarrow$ Gabite $\rightarrow$ Garchomp.
*Биом спавна Gible рекомендуется именно как лучший биом для **Acquisition Route** получения Garchomp.*

---

## 4. Пошаговый рабочий регламент (Pipeline)

```
TARGET
  ↓
Evolution Line (анализ всей ветки)
  ↓
Direct Wild Spawn / Acquisition Route (определение стратегии получения)
  ↓
Spawn Entries (извлечение всех записей из JSON текущей сборки)
  ↓
Biome / Biome Tags (сопоставление с реестром биомов)
  ↓
Spawn Context (Surface / Underground / Submerged)
  ↓
Hard Conditions (Light, Min/Max Y, Sky, Weather, Moon, Blocks)
  ↓
chooseBucket() (Common 93.8%, Uncommon 5%, Rare 1%, Ultra-Rare 0.2%)
  ↓
Bucket Probability: P(Bucket)
  ↓
Matching Entries ONLY in selected Bucket (строгий фильтр по контексту)
  ↓
Weight / Percentage Selection Stage
  ↓
Target Selection Probability: P(Target selected) = P(Bucket) × P(Target | Bucket, Context)
  ↓
Separate Practical Analysis
  ├─ Entity Cap
  ├─ Common Pool Pressure (Low / Medium / High / Unknown)
  ├─ Spawn Position Availability
  ├─ Terrain & Accessibility
  └─ Visibility & Despawn Ease
  ↓
ВЫВОД: Mathematical Best + Practical Best (без единого смешанного Score)
```

---

## 5. Использование автоматического расчётного скрипта

Для проведения расчётов использовать верифицированный скрипт:

```bash
python .agents/skills/recommend_spawn_biome/scripts/calculate_best_spawn_biome.py <pokemon_name>
```

---

## 6. Стандарт оформления ответа пользователю

### 1. 🧬 Анализ эволюционной линии и способов получения
* Целевой покемон: `Target`.
* `Direct Wild Spawn`: Доступен / Недоступен (`[FACT]`).
* `Acquisition Route`: Оптимальная цепочка эволюции (`[CALCULATED]`).
* Категория редкости (**Bucket**) и $P(\text{Bucket})$.
* Базовый вес / процент целевой формы.
* Обязательные условия (**Hard Conditions**): диапазон $Y$, уровень света, блоки, погода.

### 2. 📊 Сравнительная таблица биомов

| Biome | Context | Matching Entries | Target Share | Target Selection Probability | Common Pressure | Practical Factors | Verdict |
| :--- | :--- | ---: | ---: | ---: | :--- | :--- | :--- |
| **minecraft:stony_peaks** | Surface | 4 entries | **1.56%** | **0.0156%** | Low | Открытый обзор, легкая зачистка | ⭐ **Practical Best** |
| **minecraft:plains** | Underground ($Y < 50$) | 4 entries | **29.13%** | **0.0583%** | High | Замкнутые пещеры, забивание мобкапа | 🎯 **Mathematical Best** |

*Пояснения к колонкам:*
* `Matching Entries` — число реально активных Spawn Entries выбранного Bucket в данном Context.
* `Target Share` — $P(\text{Target} \mid \text{Bucket}, \text{Context})$ (только для Weight-based).
* `Target Selection Probability` — $P(\text{Target selected}) = P(\text{Bucket}) \times P(\text{Target} \mid \text{Bucket}, \text{Context})$.
* `Common Pressure` — качественная оценка (`Low` / `Medium` / `High` / `Unknown`).
* `Practical Factors` — подтверждённые рельефные и практические условия.
* `Verdict` — `Mathematical Best` / `Practical Best` / `Alternative`.

### 3. 🎯 Раздельные вердикты

#### 🎯 Математический лидер (Mathematical Best):
> **Название биома** — наивысшая вероятность выбора покемона на стадии selection ($P(\text{Target} \mid \text{Bucket}) = X\%$, $P(\text{Target selected}) = Y\%$).

#### ⭐ Практический выбор (Practical Best):
> **Название биома** — наилучшие условия реальной охоты (открытый обзор, свободный мобкап, стабильные попытки генерации).

### 4. 🧭 Рекомендации по охоте с «Компасом природы» (Nature's Compass)
* Точный поисковый запрос для компаса (`#minecraft:...` или ID биома).
* Практические советы: уровень $Y$, освещение, зачистка мобов для предотвращения блокировки спавнера по мобкапу.

---

## 7. Реестр реальных биомов сборки (Фильтрация фантомных модов)

`[FACT]` В сборке **Society Sunlit Cobblemon** активны исключительно следующие биомы:
1. **Ванильные биомы Minecraft 1.20.1** (`minecraft:*`).
2. **Кастомные биомы установленных модов:**
   * **Atmospheric:** `aspen_parkland`, `dunes`, `flourishing_dunes`, `petrified_dunes`, `rocky_dunes`, `grimwoods`, `hot_springs`, `kousa_jungle`, `laurel_forest`, `rainforest`, `rainforest_basin`, `sparse_rainforest`, `sparse_rainforest_basin`, `scrubland`, `snowy_scrubland`, `spiny_thicket`.
   * **Autumnity:** `maple_forest`, `pumpkin_fields`.
   * **Windswept:** `chestnut_forest`, `snowy_chestnut_forest`, `flowering_savanna`, `lavender_fields`, `lavender_hills`, `pine_barrens`, `snowy_pine_barrens`, `tundra`.
   * **Quark:** `glimmering_weald`.

`[PROHIBITION]`
**Категорически запрещено** рекомендовать несуществующие биомы модов **Terralith** (`terralith:*`), **Biomes O' Plenty** (`biomesoplenty:*`) и **Wythers** (`wythers:*`).  
Cobblemon по умолчанию включает их в теги как опциональные (`"required": false`). При раскрытии тегов скрипт и агент обязаны фильтровать список биомов исключительно по реестру установленных модов.
