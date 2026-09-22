# 09_EVIDENCE — Centralized Evidence Registry

## 📜 Реестр доказательств (Evidence Matrix)

| ID | Утверждение (Claim) | Исходный файл | Класс / Область | Метод / Строка | Уровень уверенности |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **GYM-001** | Подиум спавнит тренера каждые 10 секунд при наличии владельца рядом | `registerCobblemonTrainerPodium.js` | `StartupEvents.registry("block")` | `blockInfo.serverTick(200, 0, ...)` | **100% CONFIRMED** |
| **GYM-002** | Подиум кэширует тренера в NBT до его победы или удаления | `registerCobblemonTrainerPodium.js` | `global.runTrainerPodium` | строки 84–110 (`trainers.get(...)`) | **100% CONFIRMED** |
| **GYM-003** | Подача редстоун-сигнала блокирует спавн тренеров на подиуме | `registerCobblemonTrainerPodium.js` | `global.runTrainerPodium` | строка 68 (`!hasNeighborSignal`) | **100% CONFIRMED** |
| **TRAINER-001** | Существуют 18 стандартных тиров тренеров (от 10 до 95 с шагом 5) | `cobblemonGymUtils.js` | `trainerBuckets` | строки 4–358 (Map тиров) | **100% CONFIRMED** |
| **TRAINER-002** | На улучшенном подиуме 75% спавнов берутся из Elite Easy и 25% из Elite Hard | `cobblemonGymUtils.js` | `global.getRandomTrainer` | строки 574–582 | **100% CONFIRMED** |
| **TRAINER-003** | Каждые 15 побед спавнится Босс Лиги | `registerCobblemonTrainerPodium.js` | `global.runTrainerPodium` | строки 96–100 (`wins % 15 === 0`) | **100% CONFIRMED** |
| **TRAINER-004** | Боссы Лиги на стандартном подиуме скейлятся от 1 до 8 ранга | `cobblemonGymUtils.js` | `global.getLeagueBoss` | строки 586–590 | **100% CONFIRMED** |
| **PARTY-001** | Команды тренеров загружаются из статических JSON-файлов RCTMod | `rctmod-forge-1.20.1-0.12.1-beta.jar` | `TrainerTeam.class` | `data/rctmod/trainers/*.json` | **100% CONFIRMED** |
| **PARTY-002** | Значок (Badge) НЕ передается в генератор и не влияет на состав врагов | `registerCobblemonTrainerPodium.js` | `global.runTrainerPodium` | строки 131–134 | **100% CONFIRMED** |
| **LOOT-001** | Базовая формула денег: `loserLevel * 4 * trainerLevel * variance`, кап 5000 | `cobblemonHandleDeath.js` | `global.handleCobblemonDefeat` | строки 34–45 | **100% CONFIRMED** |
| **LOOT-002** | Значок удваивает денежную награду ($\times 2.0$) | `cobblemonHandleDeath.js` | `global.handleCobblemonDefeat` | строки 46–49 (`reward *= 2`) | **100% CONFIRMED** |
| **LOOT-003** | Улучшение подиума (Elite) удваивает денежную награду ($\times 2.0$) | `cobblemonHandleDeath.js` | `global.handleCobblemonDefeat` | строки 53–56 (`reward *= 2`) | **100% CONFIRMED** |
| **LOOT-004** | Перк The Art of Battle увеличивает деньги на 25% ($\times 1.25$) | `cobblemonHandleDeath.js` | `global.handleCobblemonDefeat` | строки 66–69 (`reward *= 1.25`) | **100% CONFIRMED** |
| **LOOT-005** | Значок дропает лут из `sunlit_cobblemon:badge_reward/<type>_type_gym` | `cobblemonGymUtils.js` | `global.getTypeRewards` | строки 591–609 | **100% CONFIRMED** |
| **LOOT-006** | Каждые 10 и 100 побед выдается сундучный лут | `cobblemonGymUtils.js` | `global.getWinsRewards` | строки 612–630 | **100% CONFIRMED** |
| **LOOT-007** | Каждые 15 побед на Elite-подиуме гарантированно выпадает Медальон Лиги | `cobblemonHandleDeath.js` | `global.handleCobblemonDefeat` | строки 58–64 (`sunlit_league_medallion`) | **100% CONFIRMED** |
| **LOOT-008** | При поражении взимается штраф 5% от баланса $\times (\text{wins}+1)$ | `cobblemonUtils.js` | `global.handleLeagueFee` | строки 182–190 | **100% CONFIRMED** |
| **BADGE-001** | Значки требуют ранг `trainer_lvl_5` и стоят 1 Медальон Лиги в Poké Mart | `poke_mart.json` | `shops/poke_mart.json` | строки 659–895 | **100% CONFIRMED** |
| **BADGE-002** | Значок экипируется в Curios-слот `gym_badge` | `registerCobblemonItems.js` | `StartupEvents.registry("item")` | тег `curios:gym_badge` | **100% CONFIRMED** |
| **BADGE-003** | Бой блокируется, если покемоны игрока не соответствуют типу значка | `cobblemonTrainerPodium.js` | `ItemEvents.entityInteracted` | строки 180–192 (`partyIsMonotype`) | **100% CONFIRMED** |
| **BADGE-004** | Вторичный тип покемона удовлетворяет условию монотипа | `cobblemonUtils.js` | `global.partyIsMonotype` | строки 159–165 | **100% CONFIRMED** |
| **UPGRADE-001**| Камень Элиты стоит 4 Медальона Лиги в Poké Mart | `poke_mart.json` | `shops/poke_mart.json` | строки 454–463 | **100% CONFIRMED** |
| **UPGRADE-002**| Клик Камнем Элиты переключает свойство блока на `upgraded: true` | `cobblemonTrainerPodium.js` | `BlockEvents.rightClicked` | строки 238–255 | **100% CONFIRMED** |
| **UPGRADE-003**| Разрушение улучшенного подиума возвращает Камень Элиты | `cobblemonTrainerPodium.js` | `BlockEvents.broken` | строки 78–80 | **100% CONFIRMED** |
| **DIFFICULTY-001**| Легендарки дают уровень 105 и блокируют бой на обычном подиуме | `cobblemonUtils.js` | `global.getPartyLevel` | строки 17–19 | **100% CONFIRMED** |
| **DIFFICULTY-002**| Оверлевел одного покемона (>125% от среднего) форсирует тир по максимуму | `cobblemonUtils.js` | `global.getPartyLevel` | строки 25–26 | **100% CONFIRMED** |
| **DIFFICULTY-003**| В Elite Hard 99.4% покемонов имеют EV и 99% имеют 6×31 IV с AI 9–11 | `audit_gym_mechanics.py` | Анализ 30 JSON элиты | 176 покемонов, 175 с EV | **100% CONFIRMED** |
