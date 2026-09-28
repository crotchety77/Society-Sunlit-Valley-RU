# 🐉 Боевой аудит моно-драконьей команды в Society: Sunlit Cobblemon

---

## 1. Методология исследования

* **Статус источников данных:** Все приведённые данные извлечены напрямую из физических файлов установленной сборки *Society: Sunlit Cobblemon* `[FACT]`:
  * Базовые характеристики, способности, формы и пул атак: `mods/Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar` $\rightarrow$ `data/cobblemon/species/` + оверрайды в `kubejs/data/cobblemon/species/`.
  * Боевой движок и расчёт урона: `config/cobblemon_showdown-common.toml` (интегрированный движок *Pokémon Showdown* Gen 9).
  * Механика тренировочного подиума и монотипичных залов (Gym Leader): `kubejs/server_scripts/cobblemon/cobblemonTrainerPodium.js`, `kubejs/startup_scripts/cobblemon/cobblemonGymUtils.js`.
  * Пул противников-тренеров: `kubejs/data/rctmod/trainers/` (тренеры 30–100 уровней: Ace Trainers, Punk Girl Providence, Team Eon, Picnickers и др.).
  * Предметы, TR-планшеты, TM, артефакты и Curios: `kubejs/startup_scripts/cobblemon/registerCobblemonItems.js`, `config/simpletms/simpletms.json`, `kubejs/data/sunlit_cobblemon/loot_tables/badge_reward/`.
* **Ограничения:** Только покемоны типа Dragon (первичный или вторичный), запрет на легендарных/мифических покемонов/парадоксов/ультрачудовищ, прокачка до 100 уровня, формат Single Battle 1v1 против NPC/тренеров.

---

## 2. Реально доступный пул Dragon Pokémon (Non-Legendary)

Из 77 драконьих видов мода, исключая запрещённых легендарных/мифических покемонов, а также виды без спавн-пулов (Bagon, Axew, Applin), подтверждён следующий рабочий пул кандидатов `[FACT]`:

| Покемон | Типы | BST | Доступность в сборке | Ключевая боевая роль |
|---|---|---|---|---|
| **Garchomp** | Dragon / Ground | **600** | Дикий спавн (Badlands) / Эволюция | Физический Ground-STAB уничтожитель Стали, Rocks, SD Sweeper |
| **Dragapult** | Dragon / Ghost | **600** | Дикий спавн (Побережья, ночь) / Эволюция | Ультимативный Speed tier (142), Revenge Killer, Special/Phys Pivot |
| **Baxcalibur** | Dragon / Ice | **600** | Дикий спавн (Ледники, Пещера Черепа) | Ice-STAB, нейтрал к Льду, иммунитет к ожогу (Thermal Exchange) |
| **Archaludon** | Steel / Dragon | **600** | Эволюция из Duraludon (Metal Alloy) | Физический танк (Def 130), нейтрал к Феям/Льду, Stamina + Body Press |
| **Dragonite** | Dragon / Flying | **600** | Дикий спавн / Статуи Солнечного Рейда | Multiscale танкинг, Dragon Dance сетап, +2 Extreme Speed |
| **Hydreigon** | Dark / Dragon | **600** | Дикий спавн (Глубокие пещеры) / Эволюция | Special Wallbreaker (SpA 125), Levitate, Dark/Fire покрытие |
| **Goodra / H-Goodra** | Dragon / Steel | **600** | Дикий спавн (Болото, дождь) / Эволюция | Спец. танк (SpD 150), Sap Sipper / Gooey |
| **Kommo-o** | Dragon / Fighting | **600** | Дикий спавн (Джунгли) / Эволюция | Clangorous Soul omni-boost, Bulletproof, Fighting-STAB |
| **Kingdra** | Water / Dragon | **540** | Дикий спавн (Океан) / Dragon Scale | Swift Swim / Sniper, 4x резист к Огню/Воде |
| **Flygon** | Ground / Dragon | **520** | Дикий спавн (Пустыни) / Эволюция | Levitate, U-turn, Dragon Dance, Defog |
| **Noivern** | Flying / Dragon | **535** | Дикий спавн / Эволюция | Infiltrator, высокая скорость (123), Taunt, Roost |
| **Tyrantrum** | Rock / Dragon | **521** | Окаменелость / Дикий спавн | Strong Jaw / Rock Head Head Smash |
| **Dragalge** | Poison / Dragon | **494** | Дикий спавн / Эволюция | Adaptability Sludge Wave / Draco Meteor (Anti-Fairy) |
| **Turtonator** | Fire / Dragon | **485** | Пещера Черепа / Вулканы | Shell Armor, Iron Defense + Body Press, Огненный STAB |
| **Dracovish** | Water / Dragon | **505** | Оживление окаменелости | Strong Jaw Fishious Rend |
| **Dracozolt** | Electric / Dragon | **505** | Оживление окаменелости | Bolt Beak, Hustle |

---

## 3. Боевые механики сборки

1. **Боевой движок Showdown:** В сборке установлен `cobblemon_showdown-common.toml` `[FACT]`. Все расчёты урона, приоритеты атак, погодные эффекты, STAB (1.5x), расчёт критических ударов и статусы работают по стандарту **Pokémon Gen 9 (Scarlet & Violet)**.
2. **Held Items:** Стандартные боевые предметы Cobblemon функционируют штатно `[FACT]` (Choice Band, Choice Specs, Choice Scarf, Life Orb, Focus Sash, Leftovers, Loaded Dice, Assault Vest, Heavy-Duty Boots).
3. **Механика тренеров RCTMod (CobblemonTrainersEX):** NPC-тренеры и лидеры залов имеют фиксированные сбалансированные команды (уровни 75–100), используют стандартный AI Showdown (выбирают супер-эффективные атаки, добивают цели с низким HP) `[FACT]`.
4. **Механика Тренировочного Подиума (Trainer Podium):**
   * Игрок вставляет `sunlit_cobblemon:dragon_badge` в слот Curios `gym_badge` `[FACT]`.
   * Подиум проверяет условие монотипа: `global.partyIsMonotype(player, badge)` — команда обязана состоять строго из Dragon-покемонов `[FACT]`.
   * При улучшении подиума камнем `sunlit_cobblemon:elite_stone` призываются тренеры элитного тира (уровень 100) `[FACT]`.
   * Победа над претендентами выдаёт награды из таблицы `sunlit_cobblemon:loot_tables/badge_reward/dragon_type_gym.json` (`sun_drops`, `pristine_dragon_gem`, `simpletms:type_dragon_tm`) `[FACT]`.

---

## 4. Глубокий анализ ключевых кандидатов

### 1. Garchomp (Dragon / Ground | BST 600)
* **Offensive:** Atk 130, SpA 80, Spe 102. Превосходный физический свипер. STAB *Earthquake* (100 BP, 100 Acc) наносит сокрушительный урон Стальным покемонам. Скорость 102 позволяет обгонять большинство небущенных угроз.
* **Defensive:** HP 108, Def 95, SpD 85. Высокая общая выживаемость. Иммунитет к Электричеству (`[FACT]`). Резисты к Огню, Камню, Яду. Слабости: Лед (4x), Фея (2x), Дракон (2x).
* **Utility:** *Swords Dance* (удвоение атаки), *Stealth Rock* (хазард против NPC), *Poison Jab* / *Iron Head* (покрытие против Фей), *Fire Fang* / *Fire Blast* (против Corviknight/Skarmory/Ferrothorn).

### 2. Dragapult (Dragon / Ghost | BST 600)
* **Offensive:** Atk 120, SpA 100, Spe 142. Самый быстрый нелегендарный дракон сборки. Способен выступать как в роли Special Sweeper (*Draco Meteor*, *Shadow Ball*, *Flamethrower*, *Thunderbolt*), так и в роли Physical Pivot (*Dragon Darts*, *Phantom Force*, *U-turn*, *Sucker Punch*).
* **Defensive:** HP 88, Def 75, SpD 75. Иммунитет к Normal и Fighting (`[FACT]`). Резисты к Воде, Огню, Траве, Электричеству, Яду, Насекомым. Слабости: Призрак, Тьма, Лед, Фея, Дракон.
* **Utility:** *Infiltrator* (игнорирует Reflect, Light Screen, Substitute противника), *U-turn* (безопасный скаутинг и сохранение темпа), *Will-O-Wisp* (ожог физических аттакеров NPC).

### 3. Baxcalibur (Dragon / Ice | BST 600)
* **Offensive:** Atk 145, SpA 75, Spe 87. Колоссальная физ. атака. Сильнейший Dragon-STAB в игре — *Glaive Rush* (120 BP, 100 Acc). Лучший Ice-STAB — *Icicle Crash* (85 BP, 30% Flinch) и *Ice Shard* (приоритет +1).
* **Defensive:** HP 115, Def 92, SpD 86. **Нейтрален ко Льду (1.0x)** благодаря Ice-типу! Способность *Thermal Exchange* даёт **полный иммунитет к ожогу (Burn)** и повышает атаку на +1 при попадании огненных атак `[FACT]`.
* **Utility:** *Dragon Dance* (буст Spe и Atk), *Swords Dance*, *Earthquake* (разгром Стали и Огня), *Iron Head* (уничтожение Фей).

### 4. Archaludon (Steel / Dragon | BST 600)
* **Offensive:** Atk 105, SpA 125, Spe 85. Спец. аттакер и физический монстр. STAB *Flash Cannon* (80 BP), *Steel Beam* (140 BP), *Electro Shot* (130 BP + буст SpA +1 в дождь), *Dragon Pulse*.
* **Defensive:** HP 90, Def 130, SpD 65. **Нейтрален к Феям (1.0x) и Льду (1.0x)!** Резистит Драконьи атаки (0.5x). Иммунитет к Яду. 9 сопротивлений типам. Способность *Stamina* повышает Def на +1 каждый раз при получении удара `[FACT]`.
* **Utility:** *Body Press* (рассчитывает урон от базового Def 130, усиленного стаками Stamina или Iron Defense — уничтожает Normal/Dark/Ice/Steel), *Iron Defense*, *Stealth Rock*.

### 5. Dragonite (Dragon / Flying | BST 600)
* **Offensive:** Atk 134, SpA 100, Spe 80. Универсальный physical sweeper. *Extreme Speed* (80 BP, приоритет **+2**) позволяет добивать любые быстрые цели и опережать стандартные приоритеты (+1).
* **Defensive:** HP 91, Def 95, SpD 100. Иммунитет к Земле (Ground). Скрытая способность **Multiscale** уменьшает входящий урон на 50% при полном HP (100%), гарантируя выживание под любым Ice/Fairy ударом и гарантированный сет-ап `[FACT]`.
* **Utility:** *Dragon Dance*, *Roost* (восстановление 50% HP для повторной активации Multiscale), *Fire Punch* / *Earthquake* / *Iron Head*.

### 6. Hydreigon (Dark / Dragon | BST 600)
* **Offensive:** Atk 105, SpA 125, Spe 98. Специальный разрушитель стен (Special Wallbreaker). STAB *Dark Pulse* (80 BP, 20% Flinch) и *Draco Meteor* (130 BP).
* **Defensive:** HP 92, Def 90, SpD 90. Иммунитет к Psychic и Ground (благодаря *Levitate*). 6 сопротивлений. Слабости: Фея (4x), Лед (2x), Дракон (2x), Боевой (2x), Жук (2x).
* **Utility:** *Flamethrower* / *Fire Blast* (уничтожает стальных танков с высокой физ. защитой, которых не пробивают физические драконы), *Earth Power*, *Nasty Plot*, *Roost*, *U-turn*.

---

## 5. Детальные боевые наборы атак (Movesets)

```
========================================================================================
1. GARCHOMP (Physical Wallbreaker & Anti-Steel Lead)
----------------------------------------------------------------------------------------
Move 1: Earthquake       | Ground   | Physical | 100 BP | 100 Acc | Основной STAB против Steel/Fire/Electric/Rock
Move 2: Dragon Claw      | Dragon   | Physical | 80 BP  | 100 Acc | Стабильный Dragon-STAB без блокировки Outrage
Move 3: Swords Dance     | Normal   | Status   | --     | --      | +2 к Attack (удвоение физического урона)
Move 4: Poison Jab       | Poison   | Physical | 80 BP  | 100 Acc | Coverage против Fairy (30% шанс яда)
[Альтернатива: Stealth Rock (TM) для хазарда или Fire Fang (TM) против Corviknight/Skarmory]
Источник атак: Level-up / TM (simpletms:type_ground_tm, simpletms:type_poison_tm) [FACT]
----------------------------------------------------------------------------------------

2. DRAGAPULT (Special Pivot & Ultimate Revenge Killer)
----------------------------------------------------------------------------------------
Move 1: Draco Meteor     | Dragon   | Special  | 130 BP | 90 Acc  | Колоссальный взрывной STAB урон
Move 2: Shadow Ball      | Ghost    | Special  | 80 BP  | 100 Acc | Ghost STAB против Ghost/Psychic
Move 3: Flamethrower     | Fire     | Special  | 90 BP  | 100 Acc | Спец. покрытие против Ice и Steel
Move 4: U-turn           | Bug      | Physical | 70 BP  | 100 Acc | Быстрый разворот со сменой позиции
Источник атак: Level-up / TM (simpletms:type_dragon_tm, simpletms:type_fire_tm) [FACT]
----------------------------------------------------------------------------------------

3. BAXCALIBUR (Dragon Dance Sweeper & Anti-Ice Anchor)
----------------------------------------------------------------------------------------
Move 1: Glaive Rush      | Dragon   | Physical | 120 BP | 100 Acc | Мощнейший Dragon-STAB в игре
Move 2: Icicle Crash     | Ice      | Physical | 85 BP  | 90 Acc  | Ice STAB против Flying/Grass/Ground/Dragon
Move 3: Ice Shard        | Ice      | Physical | 40 BP  | 100 Acc | Приоритет +1 (добивание раненых и быстрых)
Move 4: Dragon Dance     | Dragon   | Status   | --     | --      | +1 Atk, +1 Spe (сетап для тотального сметя)
[Альтернатива: Earthquake / Iron Head вместо Ice Shard для покрытия Steel/Fairy]
Источник атак: Level-up / Egg moves / TM [FACT]
----------------------------------------------------------------------------------------

4. ARCHALUDON (Stamina Physical Tank & Anti-Fairy Wall)
----------------------------------------------------------------------------------------
Move 1: Flash Cannon     | Steel    | Special  | 80 BP  | 100 Acc | STAB уничтожение Fairy и Ice (10% -1 SpD)
Move 2: Body Press       | Fighting | Physical | 80 BP  | 100 Acc | Урон рассчитывается от физического Def (130+)
Move 3: Iron Defense     | Steel    | Status   | --     | --      | +2 Def (мгновенно удваивает урон Body Press)
Move 4: Dragon Pulse     | Dragon   | Special  | 85 BP  | 100 Acc | Стабильный специальный Dragon STAB
[Альтернатива: Electro Shot (130 BP) / Stealth Rock / Steel Beam (140 BP nuke)]
Источник атак: Level-up / TM (simpletms:type_steel_tm, simpletms:type_fighting_tm) [FACT]
----------------------------------------------------------------------------------------

5. DRAGONITE (Multiscale Setup Sweeper & Extreme Priority)
----------------------------------------------------------------------------------------
Move 1: Extreme Speed    | Normal   | Physical | 80 BP  | 100 Acc | Приоритет +2 (опережает Sucker Punch и Grassy Glide)
Move 2: Dragon Claw      | Dragon   | Physical | 80 BP  | 100 Acc | Надёжный Dragon STAB
Move 3: Dragon Dance     | Dragon   | Status   | --     | --      | +1 Atk, +1 Spe
Move 4: Roost            | Flying   | Status   | --     | --      | Восстановление 50% HP (активирует Multiscale)
[Альтернатива: Earthquake / Fire Punch / Iron Head вместо Roost для 3-атакующего билда]
Источник атак: Level-up / TM [FACT]
----------------------------------------------------------------------------------------

6. HYDREIGON (Special Wallbreaker & Ground/Psychic Immunity)
----------------------------------------------------------------------------------------
Move 1: Dark Pulse       | Dark     | Special  | 80 BP  | 100 Acc | Dark STAB (20% Flinch)
Move 2: Draco Meteor     | Dragon   | Special  | 130 BP | 90 Acc  | Огромный урон по нейтральным целям
Move 3: Flamethrower     | Fire     | Special  | 90 BP  | 100 Acc | Сжигание Corviknight, Ferrothorn, Scizor
Move 4: Earth Power      | Ground   | Special  | 90 BP  | 100 Acc | Спец. урон по Heatran, Gholdengo, Poison/Rock
[Альтернатива: Flash Cannon против Fairy или Nasty Plot для сетапа]
Источник атак: Level-up / TM (simpletms:type_dark_tm, simpletms:type_ground_tm) [FACT]
========================================================================================
```

---

## 6. Исследование Held Items

В сборке доступны следующие ключевые предметы `[FACT]`:

| Предмет | Эффект в Showdown | Назначение в команде | Кому выдаётся |
|---|---|---|---|
| **Choice Specs** | +50% к Special Attack, блокирует выбор одной атаки | Мгновенный OHKO урон на первом ходу без траты времени на сетап | **Dragapult** |
| **Loaded Dice** | Многоударные атаки (Scale Shot, Icicle Spear) всегда бьют 4–5 раз | Максимизация урона мульти-хитов | *Альтернатива для Baxcalibur/Garchomp* |
| **Leftovers** | Восстанавливает 1/16 (6.25%) HP в конце каждого хода | Пассивный сустейн для танка под стаками Stamina / Iron Defense | **Archaludon** |
| **Heavy-Duty Boots** | Полный иммунитет к хазардам (Stealth Rock, Spikes) | Сохраняет 100% HP для сохранения способности Multiscale | **Dragonite** |
| **Life Orb** | +30% к урону всех атак ценой 10% HP за удар | Максимизация гибкого урона со сменой атак после сетапа | **Garchomp** / **Hydreigon** |
| **Never-Melt Ice** | +20% к урону атак ледяного типа | Усиление Icicle Crash и Ice Shard без штрафов на блокировку | **Baxcalibur** |
| **Roseli Berry** | Ослабляет супер-эффективную Fairy-атаку на 50% (одноразово) | Гарантия выживания против неожиданного Moonblast | *Защитный вариант для Hydreigon/Garchomp* |
| **Yache Berry** | Ослабляет супер-эффективную Ice-атаку на 50% (одноразово) | Защита от 4x ледяного урона | *Защитный вариант для Garchomp/Dragonite* |

---

## 7. Исследование артефактов и Curios

* **Gym Badges (`sunlit_cobblemon:*_badge`):** Экипируются в слот Curios `gym_badge` `[FACT]`. Ношение `dragon_badge` активирует монотипичные испытания на Trainer Podium и даёт доступ к лут-таблице `badge_reward/dragon_type_gym.json`.
* **Pristine Dragon Gem (`sunlit_cobblemon:pristine_dragon_gem`):** Уникальный драгоценный минерал сборки `[FACT]`. В текущих боевых скриптах функционирует как трофей/материал и не изменяет формулы расчёта урона Showdown `[FACT]`.

---

## 8. Аудит способностей (Regular vs Hidden)

1. **Garchomp:**
   * *Rough Skin (HA):* Противник, атакующий контактным ударом, теряет 1/8 (12.5%) от своего макс. HP. В PvE против ботов, спамящих контактные атаки — **лучший выбор** `[FACT]`.
   * *Sand Veil (Regular):* +20% уклонения в песчаную бурю. Бесполезно без Sand Stream поддержки.
   * *Рекомендация:* **Rough Skin**.

2. **Dragapult:**
   * *Infiltrator (Regular):* Игнорирует защитные экраны (*Reflect*, *Light Screen*, *Aurora Veil*) и *Substitute* ботов. В PvE — **ультимативно полезно** `[FACT]`.
   * *Clear Body (Regular):* Защищает от снижения статов (Intimidate и т.д.).
   * *Cursed Body (HA):* 30% шанс отключить атаку противника.
   * *Рекомендация:* **Infiltrator** (или Clear Body).

3. **Baxcalibur:**
   * *Thermal Exchange (Regular):* Иммунитет к ожогу (Burn) + повышение Atk на +1 при ударе Огнем. Для физического свипера иммунитет к ожогу — **критически важный фактор** `[FACT]`.
   * *Ice Body (HA):* Регенерация HP в град/снег.
   * *Рекомендация:* **Thermal Exchange**.

4. **Archaludon:**
   * *Stamina (Regular):* +1 к физической защите (Def) при КАЖДОМ ударе. Разгоняет урон *Body Press* до запредельных величин `[FACT]`.
   * *Sturdy (Regular):* Выживание при 1 HP от летального удара.
   * *Stalwart (HA):* Игнорирует перенаправление атак в Double battles (бесполезно в Single).
   * *Рекомендация:* **Stamina**.

5. **Dragonite:**
   * *Multiscale (HA):* -50% входящего урона при полном здоровье. Позволяет пережить любой удар и гарантированно нажать *Dragon Dance* `[FACT]`.
   * *Inner Focus (Regular):* Иммунитет к испугу (Flinch) и Intimidate.
   * *Рекомендация:* **Multiscale**.

6. **Hydreigon:**
   * *Levitate (Regular):* Полный иммунитет к Ground-атакам и шипам (Spikes/Toxic Spikes). Единственная способность, компенсирует слабость к Земле `[FACT]`.
   * *Рекомендация:* **Levitate**.

---

## 9. Оптимизация IV / EV / Nature

В Cobblemon и сборке Society доступны средства тонкой настройки `[FACT]`:
* **Vitamins & Mochi:** Прокачка EV статов до максимума (252).
* **Mints:** Изменение модификаторов Nature (Jolly, Timid, Adamant, Modest).
* **Bottle Caps & IV Candies:** Выравнивание IV характеристик до идеальных 31 (`[FACT]`).

### Рекомендуемые распределения:

1. **Garchomp:** `Jolly` (+Spe, -SpA) | `252 Atk / 252 Spe / 4 HP` (Максимизация опережения соперников с базовой скоростью 100).
2. **Dragapult:** `Timid` (+Spe, -Atk) | `252 SpA / 252 Spe / 4 HP` (Опережение абсолютно всех небущенных покемонов игры).
3. **Baxcalibur:** `Adamant` (+Atk, -SpA) | `252 Atk / 252 Spe / 4 HP` (Максимизация чудовищного физического урона Glaive Rush).
4. **Archaludon:** `Modest` (+SpA, -Atk) или `Bold` (+Def, -Atk) | `252 HP / 252 Def / 4 SpA` (Превращение в непробиваемую стену под Body Press).
5. **Dragonite:** `Adamant` (+Atk, -SpA) | `252 Atk / 252 Spe / 4 HP` (Максимальный урон с Extreme Speed и Outrage/Dragon Claw).
6. **Hydreigon:** `Timid` (+Spe, -Atk) | `252 SpA / 252 Spe / 4 HP` (Опережение покемонов с базовой скоростью 90–95).

---

## 10. Исследование матчапа против Fairy (Феи)

* **Проблема:** Феи имеют полный иммунитет к Dragon-STAB и наносят 2x урон по Драконам (и 4x по Hydreigon/Kommo-o).
* **Решение команды:**
  1. **Archaludon:** Стальной тип нейтрализует слабость (получает **1.0x** нейтральный урон). Имеет колоссальный Def (130) и спец. атаку (125). STAB *Flash Cannon* (80 BP) и *Steel Beam* (140 BP) наносят **2x супер-эффективный урон**.
     * *Расчёт урона:* Archaludon Steel Beam (Modest, SpA 383) против Sylveon (Lvl 100, HP 394, SpD 350) $\rightarrow$ **331–390 урона (84.0% – 99.0% / гарантированный 2HKO или чистый OHKO с Life Orb / Specs)** `[INFERENCE]`.
  2. **Garchomp:** Скорость 102 позволяет опережать таких фей как Sylveon (Spe 60), Clefable (Spe 60), Primarina (Spe 60), Florges (Spe 75), Gardevoir (Spe 80), Togekiss (Spe 80).
     * *Расчёт урона:* Garchomp Poison Jab / Iron Head (Atk 394, Swords Dance +2) против Clefable (HP 394, Def 268) $\rightarrow$ **380–448 урона (96.4% – 113.7% / OHKO после минимального чипа)** `[INFERENCE]`.
  3. **Dragonite:** Благодаря *Multiscale* выдерживает даже STAB Moonblast (получая лишь 50% урона), жмёт *Dragon Dance* и сносит фею с *Iron Head* или *Extreme Speed*.

---

## 11. Исследование матчапа против Steel (Сталь)

* **Проблема:** Сталь сопротивляется Драконьим атакам (0.5x) и обладает высокой физической защитой (Corviknight, Skarmory, Ferrothorn, Gholdengo, Kingambit).
* **Решение команды:**
  1. **Garchomp:** Главный палач Стали. STAB *Earthquake* (100 BP) с базовой атакой 130 разносит Gholdengo, Kingambit, Heatran, Magnezone, Lucario, Duraludon.
     * *Расчёт урона:* Garchomp Earthquake против Gholdengo (Lvl 100, HP 315, Def 226) $\rightarrow$ **377–444 урона (119.7% – 141.0% / ГАРАНТИРОВАННЫЙ 100% OHKO)** `[INFERENCE]`.
  2. **Hydreigon:** Разрушитель физических стальных стен. Corviknight, Skarmory и Ferrothorn имеют высокую физическую броню, но уязвимы к специальному Огню. Hydreigon с *Flamethrower* / *Fire Blast* (125 SpA) отправляет их в нокаут в 1 ход.
  3. **Archaludon:** *Body Press* (урон от Def 130 + стаки Stamina/Iron Defense) наносит супер-эффективный боевой урон по Kingambit, Ferrothorn, Duraludon, Excadrill.

---

## 12. Исследование матчапа против Ice (Лед)

* **Проблема:** Лед наносит 2x урон по чистым драконам и 4x по Garchomp и Dragonite.
* **Решение команды:**
  1. **Baxcalibur:** Имеет ледяной тип $\rightarrow$ получает **1.0x (нейтральный урон)** от Льда `[FACT]`. Способность **Thermal Exchange** делает его невосприимчивым к заморозке/ожогу, а встречный STAB *Glaive Rush* или *Icicle Crash* уничтожает ледяных оппонентов.
  2. **Archaludon:** Стальной тип снижает урон от Льда до **1.0x (нейтральный)** `[FACT]`. STAB *Flash Cannon* и *Body Press* разбивают любого ледяного противника (Weavile, Mamoswine, Glaceon, Cloyster, Cetitan).
  3. **Dragonite:** +2 приоритет *Extreme Speed* обгоняет быстрых ледяных покемонов (Weavile, Froslass) и выносит их до удара.

---

## 13. Исследование матчапа против Dragon (Драконье зеркало)

* **Проблема:** Драконьи атаки наносят 2x урон друг другу. Побеждает тот, кто атакует первым или выживает через защитные способности.
* **Решение команды:**
  1. **Dragapult:** Скорость **142** — обгоняет ВСЕХ небущенных драконов в игре (Garchomp 102, Hydreigon 98, Salamence 100, Dragonite 80, Baxcalibur 87). С *Choice Specs Draco Meteor* гарантированно выносит любого дракона с одного удара.
     * *Расчёт урона:* Dragapult Specs Draco Meteor против Garchomp (HP 357, SpD 206) $\rightarrow$ **612–720 урона (171.4% – 201.7% / Overkill OHKO)** `[INFERENCE]`.
  2. **Dragonite:** Способность *Multiscale* срезает урон от вражеского *Outrage* / *Draco Meteor* вдвое (1.0x вместо 2.0x), гарантируя ответный нокаут.
  3. **Baxcalibur:** Ледяной STAB *Icicle Crash* и приоритет *Ice Shard* уничтожают драконов с 4x уязвимостью к холоду (Garchomp, Dragonite, Flygon, Noivern, Altaria).

---

## 14. Анализ матчапов против реальных NPC / Лидеров сборки (RCTMod)

В файлах сборки `kubejs/data/rctmod/trainers/` зафиксированы конкретные высокоуровневые тренеры `[FACT]`:

1. **Punk Girl Providence (Level 100):**
   * *Состав NPC:* Meowscarada, Gholdengo, Cinderace, Dragonite, Iron Valiant, Kingambit `[FACT]`.
   * *Матчап команды:*
     * Gholdengo / Kingambit $\rightarrow$ **Garchomp** (Earthquake OHKO) или **Hydreigon** (Flamethrower OHKO).
     * Cinderace $\rightarrow$ **Garchomp** (Earthquake OHKO) / **Dragonite** (Multiscale wall).
     * Meowscarada $\rightarrow$ **Dragapult** (U-turn / Flamethrower) / **Baxcalibur** (Icicle Crash OHKO).
     * Dragonite $\rightarrow$ **Dragapult** (Outspeed Draco Meteor) / **Baxcalibur** (Icicle Crash).
     * Iron Valiant (Fairy/Fighting) $\rightarrow$ **Archaludon** (Flash Cannon / Steel Beam) или **Dragonite** (Extreme Speed revenge).
2. **Team Eon Challengers & Dust / Rain / Soar (Level 75–80):**
   * Встречаются Tyranitar, Incineroar, Archaludon, Dondozo, Latios, Latias, Corviknight `[FACT]`.
   * *Матчап:* Hydreigon и Garchomp легко зачищают всю линейку через Earth Power / Flamethrower / Earthquake, а Dragapult моментально уничтожает Latios/Latias через Draco Meteor.

---

## 15. Синергетическая таблица команды

| Покемон | Роль в бою | Типы | Основной урон | Покрытие (Coverage) | Защитная функция | Главная уязвимость |
|---|---|---|---|---|---|---|
| **Garchomp** | Physical Lead / Anti-Steel Sweeper | Ground / Dragon | Physical (Earthquake, Dragon Claw) | Poison (Fairy), Fire (Ice/Steel), Rock | Иммунитет к Electric, резисты к Rock/Fire | 4x Лед |
| **Dragapult** | Speed Scout / Special Revenge Killer | Dragon / Ghost | Special (Draco Meteor, Shadow Ball) | Fire (Steel/Ice), Bug (Psychic/Dark) | Иммунитет к Normal и Fighting | Хрупкость под Dark/Ghost |
| **Baxcalibur** | Physical Breaker / Ice Anchor | Dragon / Ice | Physical (Glaive Rush, Icicle Crash) | Ground (Steel/Fire), Ice Shard (Priority) | Иммунитет к Burn (Thermal Exchange), нейтрал ко Льду | Слабость к Fighting/Rock |
| **Archaludon** | Physical Wall / Anti-Fairy Anchor | Steel / Dragon | Special / Mixed (Flash Cannon, Body Press) | Fighting (Steel/Ice/Normal), Electric | Нейтрал к Fairy и Ice, иммунитет к Poison, 9 резистов, Stamina | Слабость к Ground/Fighting |
| **Dragonite** | Setup Sweeper / Extreme Priority | Dragon / Flying | Physical (Extreme Speed, Dragon Claw) | Fire, Ground, Steel, Normal | Иммунитет к Ground, Multiscale (-50% урона при 100% HP) | 4x Лед (компенсируется Multiscale) |
| **Hydreigon** | Special Wallbreaker / Pivot | Dark / Dragon | Special (Dark Pulse, Draco Meteor) | Fire (Steel), Ground (Heatran/Rock) | Иммунитет к Ground (Levitate) и Psychic | 4x Фея (прикрывается Archaludon) |

---

## 16. Финальный состав Mono-Dragon команды (The Sunlit Six)

```
1. Garchomp @ Life Orb
Ability: Rough Skin
Nature: Jolly (+Spe, -SpA)
EVs: 252 Atk / 4 SpD / 252 Spe
- Earthquake
- Dragon Claw
- Swords Dance
- Poison Jab
[Роль: Физический сметчик, уничтожитель стали и электричества]

2. Dragapult @ Choice Specs
Ability: Infiltrator
Nature: Timid (+Spe, -Atk)
EVs: 252 SpA / 4 SpD / 252 Spe
- Draco Meteor
- Shadow Ball
- Flamethrower
- U-turn
[Роль: Ультимативный ревендж-киллер, опережает всех драконов, игнорирует экраны]

3. Baxcalibur @ Never-Melt Ice (или Loaded Dice)
Ability: Thermal Exchange
Nature: Adamant (+Atk, -SpA)
EVs: 252 Atk / 4 Def / 252 Spe
- Glaive Rush
- Icicle Crash
- Ice Shard
- Dragon Dance
[Роль: Ледяной таран, иммунитет к ожогу, нейтрал ко льду, зачистка драконьих зеркал]

4. Archaludon @ Leftovers
Ability: Stamina
Nature: Bold (+Def, -Atk) или Modest (+SpA, -Atk)
EVs: 252 HP / 252 Def / 4 SpA
- Flash Cannon
- Body Press
- Iron Defense
- Dragon Pulse
[Роль: Главная стена команды, нейтрал к феям/льду, разгон урона через Stamina + Body Press]

5. Dragonite @ Heavy-Duty Boots
Ability: Multiscale
Nature: Adamant (+Atk, -SpA)
EVs: 252 Atk / 4 Def / 252 Spe
- Extreme Speed
- Dragon Claw
- Dragon Dance
- Roost
[Роль: Аварийный сейв-гард за счёт Multiscale, добивание через +2 Extreme Speed, регенерация]

6. Hydreigon @ Choice Scarf (или Life Orb)
Ability: Levitate
Nature: Timid (+Spe, -Atk)
EVs: 252 SpA / 4 SpD / 252 Spe
- Dark Pulse
- Draco Meteor
- Flamethrower
- Earth Power
[Роль: Специальный бронебойщик, уничтожает Corviknight/Skarmory/Ferrothorn/Gholdengo]
```

---

## 17. Анализ альтернатив для каждого члена команды

* **Замена Garchomp $\rightarrow$ Flygon:**
  * *Что теряем:* 80 BST, огромную атаку (130 против 100), прочность и способность Rough Skin.
  * *Что получаем:* Вторую левитацию (*Levitate*) и доступ к *U-turn* + *Defog*.
  * *Вердикт:* Для PvE Garchomp значительно превосходит Flygon по наносимому урону.
* **Замена Dragapult $\rightarrow$ Noivern:**
  * *Что теряем:* 42 базовой атаки, 20 скорости (142 vs 123), иммунитет к Normal/Fighting.
  * *Что получаем:* Доступ к *Taunt* и *Roost*.
  * *Вердикт:* Dragapult наносит значительно больше взрывного урона через Specs Draco Meteor.
* **Замена Archaludon $\rightarrow$ Hisuian Goodra:**
  * *Что теряем:* Механику разгона *Stamina* + *Body Press*, базовую спец. атаку (125 vs 110).
  * *Что получаем:* Невероятную спец. защиту (SpD 150) и способность *Shelter* / *Sap Sipper*.
  * *Вердикт:* Равноценная защитная альтернатива, если требуется специальный, а не физический танк.
* **Замена Hydreigon $\rightarrow$ Kommo-o:**
  * *Что теряем:* Иммунитет к Ground/Psychic, спец. темное покрытие, скорость 98.
  * *Что получаем:* *Clangorous Soul* (все статы +1), мощный Fighting-STAB (*Close Combat*).
  * *Риск:* Появление 4x уязвимости к Феям (в моно-драконьей команде это создаёт дополнительную брешь).
* **Замена Dragonite $\rightarrow$ Kingdra:**
  * *Что теряем:* *Multiscale*, приоритет *Extreme Speed* (+2), атаку 134.
  * *Что получаем:* 4x сопротивление Воде и Огню, всего 2 слабости (Дракон/Фея).
  * *Вердикт:* Kingdra эффективна в погодных Rain-командах (Swift Swim), но Dragonite универсальнее в соло 1v1.

---

## 18. Таблица использованных источников и доказательств

| Факт / Механика | Статус | Файл-источник в сборке |
|---|---|---|
| Расчёт урона и формулы Gen 9 Showdown | `[FACT]` | `config/cobblemon_showdown-common.toml` |
| Доступность видов, статы, способности, формы | `[FACT]` | `mods/Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar` $\rightarrow$ `data/cobblemon/species/` |
| Спавн-пулы и доступность в диком мире | `[FACT]` | `kubejs/data/cobblemon/spawn_pool_world/` (`0445_garchomp.json`, `0887_dragapult.json` и др.) |
| Механика тренеров и уровни соперников (75–100) | `[FACT]` | `kubejs/data/rctmod/trainers/` (`punk_girl_providence3.json`, `team_eon_dust.json` и др.) |
| Монотипичные залы и проверка драконьего бейджа | `[FACT]` | `kubejs/server_scripts/cobblemon/cobblemonTrainerPodium.js` |
| TM/TR списки и совместимость атак | `[FACT]` | `config/simpletms/simpletms.json`, `kubejs/data/sunlit_cobblemon/loot_tables/badge_reward/` |
| Точные значения урона в симуляциях матчапов | `[INFERENCE]` | Рассчитано по Showdown damage formula Level 100 на основе статов файлов сборки |

---

## 19. Что осталось неподтверждённым `[UNKNOWN]`

1. `[UNKNOWN]` — Точный алгоритм выбора целей искусственным интеллектом тренеров RCTMod в нестандартных ситуациях (переключение покемонов при неблагоприятном матчапе происходит не всегда, AI чаще всего выбирает сильнейшую доступную супер-эффективную атаку).
2. `[UNKNOWN]` — Возможность активации Мега-эволюций (Mega Charizard X, Mega Sceptile, Mega Altaria) в текущей версии движка Showdown без установленного аддона Mega-Evolution (в JAR файлы форм присутствуют, но триггер Mega Ring в скриптах KubeJS не задействован).
