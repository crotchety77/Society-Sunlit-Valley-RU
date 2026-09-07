# Технический аудит механики: Цепочка получения ивового бревна, саженцев и мистического сиропа

## 1. Сквозная цепочка получения ресурсов (Обратный трейс)

```mermaid
graph TD
    A["🌾 Сбор любых созревших культур<br>(Пшеница, Морковь, Рис, Томаты...)"] -->|Шанс 0.5% (1 из 200)<br>Требуется: farming_mastery| B["🌱 Саженец мрачного дерева<br>(atmospheric:grimwood_sapling)"]
    C["♻️ Листва мрачного дерева в Утилизаторе<br>(4x саженца)"] --> B
    B --> D["🏆 Квест главы Prismatic Farming<br>(458EC4BFA0C47FCB)"]
    E["🏪 Рынок (farmingforblockheads:market)<br>Торговец Леон"] -->|Разблокируется после<br>Мастерства фермерства| F["🌿 Саженец ивы<br>(cluttered:willow_sapling)"]
    F -->|Посадка и выращивание| G["🪵 Ивовое бревно<br>(cluttered:willow_log)"]
    G -->|Установка society:tapper<br>+ листва ивы сверху| H["🍯 Мистический сироп<br>(society:mystic_syrup)<br>Время: 7 игровых дней"]
```

---

## 2. Детальный аудит каждого звена

### Звено 1. Саженец мрачного дерева (`atmospheric:grimwood_sapling`)
* **Первичный факт в коде (`farmingLoot.js:98-103`):**
  ```javascript
  e.addBlockLootModifier(global.cropList)
    .hasAnyStage("farming_mastery")
    .apply((c) => {
      if (checkMaxGrownWithChance(c.destroyedBlock, 0.005)) {
        c.addLoot("atmospheric:grimwood_sapling");
      }
    });
  ```
* **Условия выпадения:**
  1. Наличие этапа `farming_mastery` (разблокируется в древе навыков Puffish Skills по клавише `K`). Без него шанс равен **0%**.
  2. Культура должна быть полностью созревшей (`isMaxAge(blockState) == true`).
* **Точный шанс:** **`0.005` (ровно 0.5% / 1 шанс из 200 созревших культур)**.
* **Культуры-источники:** Все культуры из реестра `global.cropList` (ванильные, Farmer's Delight, Pam's HarvestCraft, Society).
* **Альтернативные источники:**
  - `recyclingMachine.js:35-36`: Переработка `atmospheric:grimwood_leaves` в Утилизаторе даёт `4x atmospheric:grimwood_sapling`.
  - Дикая генерация в редких биомах мода Atmospheric.

---

### Звено 2. Саженец ивы (`cluttered:willow_sapling`)
* **Первичный факт в коде (`generalLoot.js:316-323`):**
  - Саженец ивы **полностью удалён** из всех сундуков сокровищниц, шахт, затонувших кораблей и деревень (заменён на шестерёнки Numismatics).
* **Основной источник получения:**
  - Покупка на **Рынке** (`farmingforblockheads:market` / NPC Леон).
  - Ассортимент рынка открывает продажу саженцев ивы при наличии этапа `farming_mastery` (`society_skills.mastery.farming_mastery`).

---

### Звено 3. Ивовое бревно (`cluttered:willow_log`)
* **Источник получения:**
  - Вырастает из `cluttered:willow_sapling` при посадке на землю/дёрн.
  - Содержит древесину `cluttered:willow_log`, `cluttered:flowering_willow_log` и листву `cluttered:willow_leaves` / `flowering_willow_leaves`.

---

### Звено 4. Мистический сироп (`society:mystic_syrup`)
* **Первичный факт в коде (`tapper.js:91-99`):**
  ```javascript
  [
    "cluttered:willow_log",
    {
      leaves: ["cluttered:flowering_willow_leaves", "cluttered:willow_leaves"],
      output: ["1x society:mystic_syrup"],
      fluidOutput: "society:mystic_syrup",
      time: 7,
    },
  ]
  ```
* **Условия работы:**
  - На блок `cluttered:willow_log` устанавливается Подсочник (`society:tapper`).
  - Над бревном обязательно должны находиться блоки листвы ивы (`cluttered:willow_leaves` или `flowering_willow_leaves`).
  - Время созревания сиропа: **7 игровых дней** (7 утренних переходов в 6:00 AM).
