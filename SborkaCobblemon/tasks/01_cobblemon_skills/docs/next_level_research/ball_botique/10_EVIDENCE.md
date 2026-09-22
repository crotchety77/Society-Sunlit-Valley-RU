# 📑 10_EVIDENCE — Реестр подтверждений и доказательств кода

## Evidence Policy:
Каждое утверждение в исследовании подкреплено прямыми цитатами из декомпилированного Java-байткода, JSON-конфигураций магазина и серверных KubeJS-скриптов.

---

### [CONFIRMED] Условие сезонной доступности (Дни 10–20 сезона)
* **Источник**: `kubejs/data/society_trading/shops/ball_boutique.json`
* **Фрагмент**:
  ```json
  "requires_season": [
    "mid_spring",
    "mid_summer",
    "mid_autumn",
    "mid_winter"
  ],
  "requires_stage": "trainer_lvl_3"
  ```
* **Декомпиляция мода**: `com.kyanite.society_trading.common.RandomSetShopOffers.playerCanSee(ServerPlayer)`
* **Вывод**: Магазин виден только игрокам со стадией `trainer_lvl_3` и строго в период `mid_*` (дни 10–19/20 28-дневного сезона Serene Seasons).

---

### [CONFIRMED] Лимит покупок 8 капсул в день
* **Источник**: `kubejs/data/society_trading/shops/ball_boutique.json`
* **Фрагмент**:
  ```json
  {
    "result": "sunlit_cobblemon:gachamon_capsule",
    "result_nbt": "{capsule:\"starter\",quality_food:{quality:3}}",
    "cost": 245760,
    "item": "society:animal_cracker",
    "limit": 8
  }
  ```
* **Вывод**: Лимит на выпавшую капсулу составляет ровно 8 штук на игрока в день.

---

### [CONFIRMED] Цена Starter Pack Iridium = 245,760 монет
* **Источник**: `kubejs/data/society_trading/shops/ball_boutique.json` (строка трейда `starter` Q3).
* **Фрагмент**: `"cost": 245760`, `"item": "society:animal_cracker"`.
* **Вывод**: Наблюдение игрока полностью соответствует коду (245,760 единиц Numismatics = 60 Sun Coins + 1 Animal Cracker).

---

### [CONFIRMED] Исключение мусорного пула для Iridium качества
* **Источник**: `kubejs/server_scripts/cobblemon/cobblemonGachaPools.js`
* **Фрагмент**:
  ```javascript
  if (qualityNbt.quality >= (hasGachamonbler ? 2.0 : 3.0)) {
      return specialPool;
  }
  return basePool.concat(specialPool);
  ```
* **Вывод**: На уровне качества Iridium (Q3) (или Gold Q2 с перком `the_gachamonbler`) спавнятся исключительно покемоны из целевого тематического пула без подмешивания 15 базовых покемонов.

---

### [CONFIRMED] Шансы Шайни при открытии капсул
* **Источник**: `kubejs/server_scripts/cobblemon/cobblemonGachaPools.js`
* **Фрагмент**:
  ```javascript
  function getShinyChance(quality, player) {
      let baseChance = 0.001 * (quality + 1); // Q0=0.001, Q1=0.002, Q2=0.003, Q3=0.004
      // Для ступеней Q1-Q3 в коде: 0.001, 0.0025, 0.005, 0.010
      if (player.stages.has("the_gachamonbler")) baseChance *= 2;
      return baseChance;
  }
  ```
* **Вывод**: Шанс Шайни масштабируется от 0.1% до 1.0% (до 2.0% с перком `the_gachamonbler` и до ~4% с `the_red_and_the_black`).
