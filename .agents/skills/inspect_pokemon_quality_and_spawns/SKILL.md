---
name: inspect_pokemon_quality_and_spawns
description: Мгновенное определение качества покемона, его категории редкости (Bucket), базового веса (Weight), условий спавна, биомов, шансов в Статуе Рейда и кастомных спавнеров Пещеры Черепа (Skull Cavern).
---

# 🧬 Навык: Определение качества и спавна покемонов (Inspect Pokémon Spawns & Quality)

> 📖 **Назначение:** Данный навык задаёт строгий регламент поиска, верификации и расчёта характеристик спавна любого покемона в сборке Cobblemon (*Society Sunlit Cobblemon*), исключая догадки и ручной поиск по неверным путям.

---

## 🗂️ 1. Карта файлов и источников данных (Data Sources)

Всегда обращаться напрямую к физическим файлам сборки:

| Назначение | Путь к директории / файлу | Что искать |
| :--- | :--- | :--- |
| **Спавны в мире (World Spawns)** | `G:\curseforge\minecraft\Instances\Society Sunlit Cobblemon\kubejs\data\cobblemon\spawn_pool_world\` | Файлы вида `0919_nymble.json`, `0901_ursaluna.json` |
| **Пещера Черепа (Skull Cavern)** | `...\kubejs\data\cobblemon\spawn_pool_world\` | `society_desert_fault.json`, `society_frozen_caves.json`, `sulfur_caves.json` |
| **Характеристики видов (Species / Stats)** | `Sunlit_Cobblebackported-forge-*.jar -> data/cobblemon/species/` | Базовые статы (BST), способности (HA), EV-выход, эволюции |
| **Формулы движка спавна** | `...\kubejs\startup_scripts\cobblemon\cobblemonUtils.js` | `global.getCurrentSpawnDetails`, `global.getImportantAspect` |
| **Статуи Солнечного Рейда** | `...\kubejs\server_scripts\cobblemon\cobblemonRaid.js` | Расчёт тиров (Tier 0–3), пулы `bucket`, HA (25%), Shiny |
| **Поке-Радар** | `...\kubejs\server_scripts\cobblemon\cobblemonRadar.js` | Фильтрация по `rarity`, HUD-оповещения, шансы |
| **Магазин Покемарта** | `...\kubejs\data\society_trading\shops\poke_mart.json` | Цены на `poke_radar`, `silph_scope`, ранги тренера |

---

## 🔍 2. Алгоритм проверки покемона (5-Step Protocol)

При запросе о любом покемоне агент обязан:

### Шаг 1: Поиск в `spawn_pool_world`
1. Найти JSON-файл вида `<номер>_<имя>.json` или проверить кастомные файлы биомов (`society_desert_fault.json` и др.).
2. Считать точные параметры:
   * **`bucket`** — корзина редкости (`common`, `uncommon`, `rare`, `ultra-rare`).
   * **`weight`** — базовый математический вес в пуле (например, `10.0`, `2.0`, `0.5`).
   * **`level`** — диапазон уровней спавна (например, `"7-22"` или `"28-39"`).
   * **`condition`** — `biomes`, `canSeeSky`, `minSkyLight`, `timeRange`, `neededBaseBlocks`.
   * **`anticondition`** — запрещённые биомы и структуры.

### Шаг 2: Проверка региональных форм (Aspects)
* Проверить `global.getImportantAspect`: если у вида есть формы `alolan`, `galarian`, `hisuian`, `paldean`, `bloodmoon` — определить их параметры отдельно.

### Шаг 3: Проверка характеристик вида (Species Data)
* Базовые статы (HP, Atk, Def, SpA, SpD, Spe).
* Способности: обычные и скрытая (**Hidden Ability** `h:`).
* Catch Rate (коэффициент поимки).

### Шаг 4: Расчёт доступности в Статуе Солнечного Рейда
* Соответствие тиру статуи:
  * **Tier 0:** 50% `common` / 50% `uncommon`
  * **Tier 1:** 75% `uncommon` / 25% `rare`
  * **Tier 2:** 75% `rare` / 25% `uncommon`
  * **Tier 3:** 75% `rare` / 25% `ultra-rare` (+ 25% шанс на Hidden Ability!)

### Шаг 5: Проверка специфики биомов Пещеры Черепа (Skull Cavern)
* Если покемон спавнится в `desert_fault`, `frozen_caves` или `sulfur_caves` — указать подземный характер спавна, тип пещеры и спавнеры подземелья.

---

## 📊 3. Стандарт ответа пользователю

Всегда структурировать ответ по блокам:
1. 🏷️ **Основные параметры:** Вид, Bucket (редкость), Weight (вес), Диапазон уровней.
2. 🗺️ **Где и когда спавнится:** Биомы, время суток, погода, блоки под ногами.
3. ☀️ **В Статуе Рейда:** Доступность по тирам (Tier 0–3) и шанс Hidden Ability.
4. 💡 **Практический совет тренеру:** Как быстрее всего найти/выбить или изолировать пул спавна.
