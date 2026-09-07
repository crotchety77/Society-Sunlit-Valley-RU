# 🌾 Технический аудит механик агрокультуры и фермерства (Society: Sunlit Valley)

> **Статус документа:** Завершённый аудит согласно регламенту `.agents/skills/audit_game_mechanic/`  
> **Дата аудита:** 02.09.2026  
> **Исследованные компоненты:** `dew_drop_farmland_growth`, `sereneseasons`, `FarmersDelight`, `Farm and Charm`, `Veggies Delight`, `Vintage Delight`, `Puffish Skills`, KubeJS-скрипты.

---

## 1. Сводный реестр механик фермерства

| Механика | Источник (Класс / Скрипт) | Статус в сборке | Ключевой эффект |
| :--- | :--- | :---: | :--- |
| **Суточный рост культур** | `cool.bot.dewdropfarmland.mixin.RandomTickMixin`, `CropHandlerUtils` | ✅ **АКТИВНО** | Случайный ванильный рост отключён. Рост происходит ровно в 6:00 утра (+1 стадия при `moisture >= 1`). |
| **Удобрения пашни** | `cool.bot.dewdropfarmland.utils.CropHandlerUtils.getFertilizerIncrease` | ✅ **АКТИВНО** | Слабое удобрение: $+2$ стадии в день 1; Сильное: $+3$ стадии; Гипер: $+4$ стадии. |
| **Опыт навыка Farming** | `server_scripts/blockEvents/havestHandling.js` | ✅ **АКТИВНО** | При сборе созревшей культуры начисляется $\text{XP} = \text{max\_age} \times 2$. |
| **Сбор с плодовых деревьев** | `server_scripts/loot/pamsTreeLoot.js` | ✅ **АКТИВНО** | Фиксированная награда $+40$ XP за каждый сорванный фрукт Pam's HarvestCraft 2. |
| **Опыт за кулинарные блюда** | `puffish_skills/categories/farming/experience.json` | ✅ **АКТИВНО** | $+20$ XP за каждое съеденное блюдо с тегом `#society:dish`. |
| **Семявыделитель (Seed Maker)** | `customMachines/seedMaker.js` | ✅ **АКТИВНО** | Сбор семян даёт **+60 XP** в Фермерство (`stageCount = 3`). |
| **Ремесленные машины (16 типов)** | `startup_scripts/customMachines/` | ✅ **АКТИВНО** | Ручной сбор продукции даёт $+20 \times \text{stageCount}$ XP (от +20 до +200 XP: Бочка выдержки +200, Дегидратор +160, Грибное бревно/Смола +140, Кристалляриум +100, Семявыделитель/Сыр/Вино +60). |
| **Сборщики смолы (Tappers)** | `customMachines/tapper.js`, `globalBlockEntityHandlers.js` | ✅ **АКТИВНО** | Сбор смолы/сиропа даёт $+20 \times \text{stageCount}$ XP в Фермерство (от +20 до +140 XP за сбор). |
| **Книги опыта** | `server_scripts/itemEvents/experienceBooks.js` | ✅ **АКТИВНО** | Чтение `society:farming_book` даёт $+750$ XP мгновенно. |
| **Сезонная фертильность** | `sereneseasons.init.ModFertility`, `tags/handleSeasonTags.js` | ✅ **АКТИВНО** | Культура не растёт вне своего сезона без теплицы со стеклом `#sereneseasons:greenhouse_glass`. |
| **Интерфейс Jade** | `client_scripts/jadeClient.js` | ✅ **АКТИВНО** | Динамическое чтение свойства `age` и отображение `Рост: X/Y дн.`. |

---

## 2. Подробный технический разбор механик

### 2.1. Механика роста и суточный тикер
* **Декомпилированный класс:** `cool.bot.dewdropfarmland.utils.CropHandlerUtils`
* **Mixin отключения тиков:** `RandomTickMixin` устанавливает `noRandomTick = true` для всех блоков из тега `dew_drop_farmland_growth:cancel_random_tick`.
* **Условие срабатывания:**
  ```java
  // FarmlandEventHandler
  if (level.getDayTime() % 24000 == 5) { // 6:00 AM
      if (farmlandState.getValue(FarmBlock.MOISTURE) >= 1 || isNearSprinkler(level, pos)) {
          CropHandlerUtils.growCrop(level, cropPos, cropState);
      }
  }
  ```
* **Формула созревания:**
  $$\text{Дней до созревания} = \text{max\_age} - \text{бонус\_удобрения}$$

### 2.2. Начисление опыта навыка Фермерства (Puffish Skills)
* **Декомпилированный код (`havestHandling.js`):**
  ```javascript
  if (blockState.block.isMaxAge(blockState)) {
      xpCount += blockState.block.getMaxAge();
  }
  // Задержка в 2 тика для спавна орба и начисления в навык:
  server.scheduleInTicks(2, () => {
      global.giveExperience(server, player, "farming", xpCount * 2);
  });
  ```
* **Сравнение культур по скорости прокачки за сезон (28 дней):**
  1. **Томат (`farmersdelight:tomatoes`):**
     * 1-й сбор: 3-й день ($3 \times 2 = 6$ XP).
     * 12 повторных сборов (каждые 2 дня): $12 \times 6 = 72$ XP.
     * **Итого:** **78 XP** с 1 грядки за сезон.
  2. **Обычные 7-дневные культуры (Капуста, Пшеница, Картофель, Огурец, Арахис):**
     * 4 сбора по 14 XP ($7 \times 2 = 14$).
     * **Итого:** **56 XP** с 1 грядки за сезон.
  3. **Плодовые сады Pam's HarvestCraft (`pamsTreeLoot.js`):**
     * Фиксировано **40 XP за плод**. Сад из 20 деревьев даёт **800 XP** за один сбор.

---

## 3. Сверка с описаниями, квестами и внутриигровыми подсказками

| Утверждение в игре / гайде | Реальность в коде | Статус фактчекинга | Примечание |
| :--- | :--- | :---: | :--- |
| *«Капуста созревает за 4 дня»* | В коде `CabbageBlock extends CropBlock` со свойством `AGE_7` $\rightarrow$ созревает **7 дней**. | ⚠️ **ИСПРАВЛЕНО** | Исправлено в документации и расчётах доходности. |
| *«Культуры растут каждый день, если поливать»* | Подтверждено: проверка `moisture >= 1` в 6:00 утра. | ✅ **ПОДТВЕРЖДЕНО** | Без воды или спринклера рост замораживается. |
| *«Томаты дают многократный урожай»* | `BuddingBushBlock` при сборе сбрасывает возраст до `age: 1`, а не удаляет блок. | ✅ **ПОДТВЕРЖДЕНО** | Повторный урожай каждые 2 дня. |
| *«Еда прокачивает фермерство»* | `puffish_skills:eat_food` с проверкой `#society:dish` начисляет $+20$ XP. | ✅ **ПОДТВЕРЖДЕНО** | Работает только для сложных приготовленных блюд. |

---

## 4. Реестр стадий созревания (`max_age`) всех культур сборки

| ID блока | Мод | max_age | Дней созревания | Повторный сбор (Regrow) |
| :--- | :--- | :---: | :---: | :---: |
| `farmersdelight:tomatoes` | Farmer's Delight | **3** | **3 дня** | **Да (+2 дня)** |
| `minecraft:beetroots` | Minecraft | **3** | **3 дня** | Нет |
| `farmersdelight:rice_panicles` | Farmer's Delight | **3** | **3 дня** | Нет (заливная пашня) |
| `vinery:grapevine_stem` | Vinery | **4** | **4 дня** | **Да (+2 дня, 3 сезона!)** |
| `farm_and_charm:onion_crop` / `society:onion` | Farm and Charm / Society | **4** | **4 дня** | Нет |
| `farm_and_charm:strawberry_crop` | Farm and Charm | **5** | **5 дней** | **Да (+2 дня)** |
| `society:cranberry` | Society | **5** | **5 дней** | **Да (+2 дня)** |
| `veggiesdelight:garlic_crop` | Veggies Delight | **5** | **5 дней** | Нет |
| `society:sweet_potato` | Society | **5** | **5 дней** | Нет |
| `society:eggplant` | Society | **6** | **6 дней** | Нет |
| `brewery:hops_crop` / `hop_trellis` | Brewery | **6** | **6 дней** | **Да (+2 дня)** |
| `farmersdelight:cabbages` | Farmer's Delight | **7** | **7 дней** | Нет |
| `vintagedelight:cucumbers` | Vintage Delight | **7** | **7 дней** | Нет |
| `supplementaries:flax` | Supplementaries | **7** | **7 дней** | Нет |
| `minecraft:wheat` | Minecraft | **7** | **7 дней** | Нет |
| `minecraft:carrots` | Minecraft | **7** | **7 дней** | Нет |
| `minecraft:potatoes` | Minecraft | **7** | **7 дней** | Нет |
| `society:peanut` | Society | **7** | **7 дней** | Нет |
| `vintagedelight:ghost_pepper` | Vintage Delight | **7** | **7 дней** | Нет |
| `society:blueberry` | Society | **7** | **7 дней** | **Да (+3 дня)** |
| `minecraft:pumpkin_stem` | Minecraft | **7** | **7 дней** | **Да (+3 дня)** |
| `society:sparkpod` | Society | **8** | **8 дней** | Нет |
| `society:tubabacco_leaf` | Society | **9** | **9 дней** | Нет |
| `society:ancient_fruit` | Society | **10** | **10 дней** | Нет |
| `society:mana_fruit` | Society | **12** | **12 дней** | Нет |

---

## 5. Инструменты и методы анализа

* **Декомпилятор Java:** `javap -p -c` для классов `CropHandlerUtils.class`, `CabbageBlock.class`, `PeanutBlock.class`, `CucumberBlock.class`.
* **JSON-парсеры:** `zipfile` + `json.loads` для разбора `blockstates/*.json` в JAR-файлах модов.
* **Скриптовый анализ KubeJS:** `D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\server_scripts\` и `startup_scripts\`.
