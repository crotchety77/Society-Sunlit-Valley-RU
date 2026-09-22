# 03_TRAINER_PARTY_GENERATION — Enemy Party Generation & Scaling

## 🔬 Принцип формирования вражеской команды

В отличие от диких покемонов, команды тренеров в системе Poké Gyms **НЕ генерируются процедурно «на лету»** и **НЕ скалируются динамически по формулам статов**.

Каждый противник представляет собой **статически предзаданный файл JSON** в структуре данных RCTMod (`data/rctmod/trainers/<trainer_id>.json`), в котором до мельчайших деталей прописаны все параметры каждого покемона.

---

## ⚙️ Пошаговый алгоритм выбора тренера игрой

```text
[ Игрок приближается к Подиуму ]
           │
           ▼
1. getPartyLevel(player)
   ├── Если в группе есть Легендарный/Мифический покемон -> Возвращает 105 (Illegal)
   ├── Если уровень топ-покемона > (Средний * 1.25) -> Возвращает уровень топ-покемона
   ├── Если 3 и более покемонов имеют максимальный уровень -> Возвращает максимальный уровень
   └── Иначе -> Возвращает Math.round(Сумма уровней / Число покемонов)
           │
           ▼
2. getPlayerPodiumLevelTier(partyLevel)
   └── Формула: Math.max(10, (Math.round(partyLevel / 5) * 5) - 5)
       (Округляет до тиров: 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95)
           │
           ▼
3. Проверка статуса Подиума:
   ├── Если upgraded == true:
   │     Тир переопределяется в "elite"
   │     ├── 15-я победа (wins > 14 && wins % 15 === 0): getLeagueBoss(95, true) -> Tier 9 Boss
   │     ├── 75% вероятность: Случайный тренер из eliteModeEasy (46 тренеров)
   │     └── 25% вероятность: Случайный тренер из eliteModeHard (30 тренеров)
   │
   └── Если upgraded == false:
         ├── 15-я победа (wins > 14 && wins % 15 === 0): getLeagueBoss(levelTier, false)
         │     bossNumber = Math.min(8, Math.max(1, Math.floor(levelTier / 10) - 1))
         │     Спавн: league_<archetype><bossNumber> (уровни 25..100)
         └── Обычный бой: getRandomTrainer(levelTier, false) -> trainerBuckets.get(levelTier)
           │
           ▼
4. Кэширование в NBT Подиума:
   Подиум записывает выбранного тренера в blockEntity.data.trainers[levelTier].
   Тренер сохраняется и не меняется при перезаходе игрока, пока не будет побежден или удален.
           │
           ▼
5. Спавн rctmod:trainer:
   Создается сущность с NBT: { TrainerId: newTrainer, NoAI: true }.
   Устанавливаются persistentData: { levelTier, gymLeader, badgeType }.
```

---

## 🔍 Анатомия JSON-файла тренера (RCTMod Team Structure)

Каждый тренер загружается напрямую через класс `com.gitlab.srcmc.rctmod.api.data.pack.TrainerTeam`.

Пример соревновательного тренера (`gym_obliterator_blaze.json`):

```json
{
  "displayName": "Gym Obliterator Blaze",
  "aiLevel": 9,
  "team": [
    {
      "species": "cobblemon:torkoal",
      "gender": "MALE",
      "level": 100,
      "nature": "cobblemon:modest",
      "ability": "drought",
      "moveset": [
        "irondefense",
        "amnesia",
        "hyperbeam",
        "flamethrower"
      ],
      "ivs": {
        "hp": 31, "attack": 31, "defence": 31,
        "special_attack": 31, "special_defence": 31, "speed": 31
      },
      "evs": {
        "hp": 252,
        "special_defence": 252
      },
      "shiny": false,
      "heldItem": "cobblemon:eject_button",
      "aspects": [ "male" ]
    }
  ]
}
```

---

## ❓ Влияет ли выбранный Badge на состав вражеской команды?

### 🔴 Статус: **CONFIRMED — NOT CONNECTED (НЕТ, НЕ ВЛИЯЕТ)**

* **Исходный код**: `kubejs/startup_scripts/cobblemon/registerCobblemonTrainerPodium.js` (строки 131–135)
* **Анализ вызовов**:
  ```javascript
  let badge = global.getGymBadgeType(ownerPlayer);
  if (badge !== "none") {
    freshTrainer.persistentData.badgeType = badge;
  }
  ```
* **Фактическое поведение**:
  1. Значок считывается из Curios-слота `gym_badge` игрока.
  2. Значение значка записывается **исключительно** в NBT сущности тренера (`persistentData.badgeType`) для последующей проверки в `cobblemonHandleDeath.js` при победе.
  3. Методы `global.getRandomTrainer(levelBucket, upgraded)` и `global.getLeagueBoss(levelBucket, upgraded)` **НЕ принимают и НЕ используют параметр badge**.
  4. Проверка `partyIsMonotype(player, badge)` в `cobblemonTrainerPodium.js` проверяет **только группу самого игрока**.

> **Вывод**: Выбор значка (например, Fire Badge или Water Badge) **не делает противников травяными, огненными или водными**. Пул тренеров зависит исключительно от уровня вашей команды и наличия улучшения подиума!

---

## 📊 Матрица параметров команды тренера

| Параметр | Источник значения | Динамический расчёт? | Зависимость от Gym Upgrade | Зависимость от Badge |
| :--- | :--- | :---: | :---: | :---: |
| **Количество покемонов** | JSON `team.length` (1–6) | ❌ Нет (статично) | ✅ Да (в элите средний размер 4.8–5.9) | ❌ Нет |
| **Уровни покемонов** | JSON `pokemon.level` | ❌ Нет (статично) | ✅ Да (в элите строго 88–100) | ❌ Нет |
| **Индивидуальные значения (IV)**| JSON `pokemon.ivs` | ❌ Нет (статично) | ✅ Да (в Elite Hard 99% имеют 6×31) | ❌ Нет |
| **Усилия (EV)** | JSON `pokemon.evs` | ❌ Нет (статично) | ✅ Да (в Elite Hard 99% имеют 252/252) | ❌ Нет |
| **Характер (Nature)** | JSON `pokemon.nature` | ❌ Нет (статично) | ✅ Да (оптимизированы под билд) | ❌ Нет |
| **Способность (Ability)** | JSON `pokemon.ability` | ❌ Нет (статично) | ✅ Да (включая скрытые способности) | ❌ Нет |
| **Удерживаемый предмет** | JSON `pokemon.heldItem` | ❌ Нет (статично) | ✅ Да (100% соревновательные шапки) | ❌ Нет |
| **Набор атак (Moveset)** | JSON `pokemon.moveset` | ❌ Нет (статично) | ✅ Да (покрывающие и статусные ТМ) | ❌ Нет |
| **Уровень AI** | JSON `aiLevel` (0–11) | ❌ Нет (статично) | ✅ Да (поднимается с 0 до 9–11) | ❌ Нет |
| **Шайни / Варианты** | JSON `shiny`, `aspects` | ❌ Нет (статично) | ❌ Нет | ❌ Нет |
| **Легендарные покемоны** | JSON `species` | ❌ Нет (статично) | ✅ Да (появляются в пуле Hard/Boss) | ❌ Нет |
