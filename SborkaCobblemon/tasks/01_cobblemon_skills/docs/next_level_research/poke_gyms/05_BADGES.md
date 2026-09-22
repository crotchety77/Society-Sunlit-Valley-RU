# 05_BADGES — Gym Badges, Monotype Restriction & Economics

## 🎖️ Анатомия значков зала (Gym Badges)

В сборке представлено ровно **18 значков** (по одному для каждого существующего типа покемонов):

| Значок | Реестровый ID | Требуемый тип команды игрока | Типовой дроп самоцвета |
| :--- | :--- | :--- | :--- |
| ⚪ **Normal Badge** | `sunlit_cobblemon:normal_badge` | Normal | Pristine Normal Gem |
| 🔥 **Fire Badge** | `sunlit_cobblemon:fire_badge` | Fire | Pristine Fire Gem |
| 💧 **Water Badge** | `sunlit_cobblemon:water_badge` | Water | Pristine Water Gem |
| ⚡ **Electric Badge** | `sunlit_cobblemon:electric_badge` | Electric | Pristine Electric Gem |
| 🌿 **Grass Badge** | `sunlit_cobblemon:grass_badge` | Grass | Pristine Grass Gem |
| ❄️ **Ice Badge** | `sunlit_cobblemon:ice_badge` | Ice | Pristine Ice Gem |
| 🥊 **Fighting Badge** | `sunlit_cobblemon:fighting_badge` | Fighting | Pristine Fighting Gem |
| ☠️ **Poison Badge** | `sunlit_cobblemon:poison_badge` | Poison | Pristine Poison Gem |
| 🏜️ **Ground Badge** | `sunlit_cobblemon:ground_badge` | Ground | Pristine Ground Gem |
| 🦅 **Flying Badge** | `sunlit_cobblemon:flying_badge` | Flying | Pristine Flying Gem |
| 🔮 **Psychic Badge** | `sunlit_cobblemon:psychic_badge` | Psychic | Pristine Psychic Gem |
| 🐛 **Bug Badge** | `sunlit_cobblemon:bug_badge` | Bug | Pristine Bug Gem |
| 🪨 **Rock Badge** | `sunlit_cobblemon:rock_badge` | Rock | Pristine Rock Gem |
| 👻 **Ghost Badge** | `sunlit_cobblemon:ghost_badge` | Ghost | Pristine Ghost Gem |
| 🐉 **Dragon Badge** | `sunlit_cobblemon:dragon_badge` | Dragon | Pristine Dragon Gem |
| 🌑 **Dark Badge** | `sunlit_cobblemon:dark_badge` | Dark | Pristine Dark Gem |
| ⚙️ **Steel Badge** | `sunlit_cobblemon:steel_badge` | Steel | Pristine Steel Gem |
| 🌸 **Fairy Badge** | `sunlit_cobblemon:fairy_badge` | Fairy | Pristine Fairy Gem |

---

## 🛒 Как получить значки?

* **Где купить**: Магазин **Poké Mart** (NPC-продавец `pmart_*`).
* **Стоимость**: **1× `sunlit_cobblemon:sunlit_league_medallion`** за любой значок.
* **Требование**: Ранг тренера **`trainer_lvl_5`** (разблокируется по прогрессии).
* **Смена значка**: Полностью бесплатна. Значок можно в любой момент снять или заменить через интерфейс экипировки **Curios** (горячая клавиша `G`).

---

## 🔒 Механика монотипного ограничения (`partyIsMonotype`)

* **Исходный код**: `kubejs/startup_scripts/cobblemon/cobblemonUtils.js` (строки 153–168)
* **Реализация в коде**:
  ```javascript
  global.partyIsMonotype = (player, type) => {
    if (player == undefined) return false;
    const party = global.getPlayerParty(player);
    if (party == undefined) return false;
    let isMonoType = true;
    party.forEach((pokemon) => {
      if (isMonoType) {
        if (pokemon.primaryType.name != type) {
          if (pokemon.secondaryType) {
            isMonoType = pokemon.secondaryType.name == type;
          } else {
            isMonoType = false;
          }
        }
      }
    });
    return isMonoType;
  };
  ```

### Правила проверки группы:
1. **Каждый покемон в группе** обязан иметь стихию надетого значка.
2. Подходит **как первичный, так и вторичный тип** (Dual-Typing полностью разрешён!).
   * *Пример*: При надетом `fire_badge` разрешены Charizard (Fire/Flying), Volcarona (Bug/Fire), Blaziken (Fire/Fighting), Scovillain (Grass/Fire), Rotom-Heat (Electric/Fire).
3. Если в группе оказывается хотя бы 1 покемон другого типа (или если игрок надел значок, не сменив команду), при попытке взаимодействия с тренером игра блокирует бой сообщением:
   > *"You must use a team of the badge's type to challenge this gym!"* (`badge_restricts`).

---

## 🎯 Влияние значка на бой и награды

| Аспект игры | Влияние значка | Механизм реализации |
| :--- | :---: | :--- |
| **Сложность врагов** | ❌ **НЕТ** | Вражеский AI, IV, EV и уровни не изменяются. |
| **Типы врагов** | ❌ **НЕТ** | Противники выбираются из общего пула тира игрока. |
| **Денежный выигрыш** | ✅ **× 2.0** | Удваивает финальное начисление монет в кошелёк. |
| **Стихийный дроп** | ✅ **100% ролл** | Роллит таблицу `badge_reward/<type>_type_gym` (самоцветы, ТМ, конфеты). |
| **Ограничение команды** | ✅ **100% Monotype** | Запрещает выставлять покемонов без соответствующего типа. |

> **Главный стратегический вывод**: Значок — это **экономический бустер**, требующий от игрока собрать и прокачать специализированную монотипную команду. Он не делает бои легче или сложнее со стороны врага, но накладывает ограничение на типы ваших собственных бойцов.
