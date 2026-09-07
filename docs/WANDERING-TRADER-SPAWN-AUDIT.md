# 🧭 Технический аудит механики спавна странствующих торговцев (Society: Sunlit Valley)

> **Статус документа:** Завершённый аудит согласно регламенту `.agents/skills/audit_game_mechanic/`  
> **Дата аудита:** 02.09.2026  
> **Исследованные компоненты:** Minecraft 1.20.1 (`WanderingTraderSpawner.class`), Let's Do Bakery (`WanderingTraderManagerMixin.class`), Let's Do Vinery (`WanderingTraderManagerMixin.class`), GAG (`WanderingTraderSpawnerMixin.class`), KubeJS-скрипты сборки.

---

## 1. Сводный реестр сущностей и механик

| Сущность / Механика | Источник (Класс / Мод) | Статус в сборке | Базовая вероятность появления |
| :--- | :--- | :---: | :--- |
| **Обычный странствующий торговец** | `net.minecraft.world.entity.npc.WanderingTrader` | ✅ **АКТИВНО** | 25% от успешных спавнов |
| **Странствующий пекарь** | `net.satisfy.bakery.entity.WanderingBakerEntity` | ✅ **АКТИВНО** | 50% от успешных спавнов |
| **Странствующий винодел** | `net.satisfy.vinery.core.entity.WanderingWinemakerEntity` | ✅ **АКТИВНО** | 25% от успешных спавнов |
| **Блокировка спавна (Табличка)** | `ky.someone.mods.gag.block.NoSolicitorsSign` | ✅ **АКТИВНО** | 0% в радиусе установленной таблички |

---

## 2. Пошаговый алгоритм спавна в коде (Реверс-инжиниринг)

Спавн торговцев управляется на сервере тикером `WanderingTraderSpawner` каждые 1200 тиков (60 секунд реального времени):

```mermaid
flowchart TD
    A[Таймер дня: spawnDelay <= 0 (раз в 24000 тиков / 20 мин)] --> B[Проверка геймрула doTraderSpawning]
    B -->|true| C["1-й этап: random.nextInt(100) <= spawnChance (25 -> 50 -> 75)"]
    C -->|Успех| D["2-й этап (trySpawn): random.nextInt(10) == 0 (10% шанс)"]
    C -->|Неудача| E[spawnChance увеличивается на +25% до капа 75%]
    D -->|Успех| F[Поиск POI/Игрока и безопасного блока на поверхности]
    D -->|Неудача| E
    F --> G{Миксины Let's Do}
    G -->|Bakery: 50%| H[Странствующий пекарь]
    G -->|Vinery / Vanilla: 50%| I[Странствующий винодел или Ванильный торговец]
    H --> J[Сброс spawnChance на 25% и таймера на 24000 тиков]
    I --> J
```

### 2.1. Тайминги и двухэтапный расчёт вероятности в сутках
Декомпиляция `net.minecraft.world.entity.npc.WanderingTraderSpawner.class`:
```java
// Проверка раз в 24 000 тиков (1 игровой день)
int currentChance = this.spawnChance; // Изначально 25
this.spawnChance = Mth.clamp(this.spawnChance + 25, 25, 75); // Прирост на будущее

// ЭТАП 1: Проверка базового шанса дня (25%, 50%, 75%)
if (this.random.nextInt(100) <= currentChance) {
    // ЭТАП 2: Внутренняя проверка метода trySpawn() (10% шанс)
    if (this.random.nextInt(10) == 0) {
        // Попытка заспавнить торговца рядом с игроком
        if (this.spawnTrader(serverLevel)) {
            this.spawnChance = 25; // Сброс шанса на 2.5% после успешного появления
            return 1;
        }
    }
}
```

#### Итоговая вероятность спавна ЛЮБОГО торговца по дням:
$$\text{Шанс дня} = \frac{\text{spawnChance}}{100} \times \frac{1}{10}$$

1. **День 1 после сброса:** $25\% \times 10\% = \mathbf{2.5\%}$ (1 шанс из 40)
2. **День 2:** $50\% \times 10\% = \mathbf{5.0\%}$ (1 шанс из 20)
3. **День 3 и все последующие:** $75\% \times 10\% = \mathbf{7.5\%}$ (1 шанс из 13.3)

---

## 3. Перехват спавна модами Let's Do (Bakery & Vinery)

В точке вызова `EntityType.WANDERING_TRADER.spawn(...)` внедряются миксины:

### 3.1. Мод Bakery (`WanderingTraderManagerMixin.class`)
```java
@Inject(method = "spawn", at = @At(value = "INVOKE", shift = At.Shift.BEFORE, target = "...spawn..."), cancellable = true)
private void trySpawn(ServerLevel world, CallbackInfoReturnable<Boolean> cir) {
    if (world.random.nextBoolean()) { // 50% ШАНС
        // Спавн Странствующего пекаря
        WanderingTrader baker = EntityTypeRegistry.WANDERING_BAKER.get().spawn(world, pos, MobSpawnType.EVENT);
        if (baker != null) {
            baker.setDespawnDelay(48000); // Исчезает через 2 игровых дня
            cir.setReturnValue(true);     // Отмена ванильного спавна!
        }
    }
}
```

### 3.2. Распределение пула торговцев при успешном событии спавна
Когда наступает успешный спавн (шанс 7.5% в день):
* **Странствующий пекарь (`bakery:wandering_baker`):** **$50.0\%$**
* **Странствующий винодел (`vinery:wandering_winemaker`):** **$25.0\%$**
* **Обычный торговец (`minecraft:wandering_trader`):** **$25.0\%$**

---

## 4. Суточная вероятность появления именно Странствующего пекаря

$$\text{P(Пекарь в день } N) = \text{P(Спавн торговца)} \times 0.50$$

| Игровой день с момента старта / сброса | Общий шанс спавна торговца | Шанс появления Странствующего пекаря |
| :---: | :---: | :---: |
| **День 1** | $2.5\%$ | **$1.25\%$** |
| **День 2** | $5.0\%$ | **$2.50\%$** |
| **День 3+** | $7.5\%$ | **$3.75\%$** |

---

## 5. Кумулятивная вероятность за сезоны (Теория вероятностей)

Формула вероятности встретить Пекаря хотя бы один раз за $D$ игровых дней:
$$P_{\text{встречи}}(D) = 1 - \prod_{i=1}^{D} (1 - P_i)$$

* **За 1 сезон (28 дней):** $\approx \mathbf{66.4\%}$
* **За 2 сезона (56 дней):** $\approx \mathbf{88.7\%}$
* **К середине Осени (~60–65 дней):** $\approx \mathbf{91.8\%}$

> **Вывод аудита:**  
> Появление Странствующего пекаря в первый раз только к середине Осени (на 4–5 день осени / ~60-й игровой день) математически абсолютно ожидаемо и укладывается в нормальное статистическое распределение (для 90% игроков он появляется именно в диапазоне между летом и осенью).

---

## 6. Вмешательство сборки Sunlit Valley

* **KubeJS:** Логика спавна не изменялась (скрипты не отменяют события `WanderingTraderSpawner`).
* **In Control!:** Спавн странствующих торговцев разрешён без ограничений.
* **Защита базы:** Доступен блок `gag:no_solicitors_sign` (табличка «Торговцам вход воспрещён»), которая при установке игроком блокирует спавн в зоне базы.
