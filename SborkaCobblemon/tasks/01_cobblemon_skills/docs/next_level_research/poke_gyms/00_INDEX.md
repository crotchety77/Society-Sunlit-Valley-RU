# 🔬 Poké Gym / Trainer / Loot Mechanics — Deep Code Audit
## Iteration 1: Technical Code Audit & System Deconstruction

> **Environment**: Minecraft 1.20.1 Forge / Society: Sunlit Cobblemon (Modpack Profile)  
> **Source Target Directory**: `SborkaCobblemon/tasks/01_cobblemon_skills/docs/next_level_research/poke_gyms/`  
> **Audit Status**: ✅ **COMPLETED (Code First — 100% Verified from Source Code & Data)**  
> **Methodology**: Strict Bytecode & Code Verification (KubeJS Startup/Server Scripts, Datapacks, RCTMod JAR Data & Classes).

---

## 📑 Навигация по документам аудита

| Документ | Содержание и фокус исследования | Статус |
| :--- | :--- | :---: |
| [01_ARCHITECTURE.md](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/SborkaCobblemon/tasks/01_cobblemon_skills/docs/next_level_research/poke_gyms/01_ARCHITECTURE.md) | Полная архитектура системы Gym, жизненный цикл блоков `trainer_podium`, события боёв и межмодовые связи. | ✅ CONFIRMED |
| [02_TRAINERS.md](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/SborkaCobblemon/tasks/01_cobblemon_skills/docs/next_level_research/poke_gyms/02_TRAINERS.md) | Полная классификация тренеров: Стандартные ранги (10–95), Elite Easy (75%), Elite Hard (25%), Боссы Лиги (1–9), Богини и Eon. | ✅ CONFIRMED |
| [03_TRAINER_PARTY_GENERATION.md](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/SborkaCobblemon/tasks/01_cobblemon_skills/docs/next_level_research/poke_gyms/03_TRAINER_PARTY_GENERATION.md) | Генерация команд: Фиксированные vs динамические составы, уровни, IV, EV, Nature, Ability, Held Items, Movesets, влияние Badge. | ✅ CONFIRMED |
| [04_LOOT_SYSTEM.md](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/SborkaCobblemon/tasks/01_cobblemon_skills/docs/next_level_research/poke_gyms/04_LOOT_SYSTEM.md) | Математика наград: Формула монет, мультипликаторы (Badge ×2, Elite ×2, Art of Battle ×1.25), таблицы майлстоунов (10/100 побед), штрафы. | ✅ CONFIRMED |
| [05_BADGES.md](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/SborkaCobblemon/tasks/01_cobblemon_skills/docs/next_level_research/poke_gyms/05_BADGES.md) | 18 значков Gym Badges (Curios): Правила получения, монотипное ограничение игрока, влияние на лут и независимость врагов. | ✅ CONFIRMED |
| [06_GYM_UPGRADES.md](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/SborkaCobblemon/tasks/01_cobblemon_skills/docs/next_level_research/poke_gyms/06_GYM_UPGRADES.md) | Механика улучшения подиума через `elite_stone`: переключение пулов тренеров, масштабирование сложности, фарм медальонов. | ✅ CONFIRMED |
| [07_DIFFICULTY.md](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/SborkaCobblemon/tasks/01_cobblemon_skills/docs/next_level_research/poke_gyms/07_DIFFICULTY.md) | Факторы сложности: Расчёт среднего уровня группы, анти-чит пороги, уровни AI (0–11), EV/IV скачки, штрафы поражения. | ✅ CONFIRMED |
| [08_STRATEGIC_IMPLICATIONS.md](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/SborkaCobblemon/tasks/01_cobblemon_skills/docs/next_level_research/poke_gyms/08_STRATEGIC_IMPLICATIONS.md) | Стратегические выводы для игрока: Выбор значка, тайминг апгрейда подиума, экономика фарма, риски серии побед. | ✅ CONFIRMED |
| [09_EVIDENCE.md](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/SborkaCobblemon/tasks/01_cobblemon_skills/docs/next_level_research/poke_gyms/09_EVIDENCE.md) | Централизованный реестр доказательств (Evidence Matrix) с точными ссылками на файлы, классы, методы и строки кода. | ✅ CONFIRMED |
| [10_OPEN_QUESTIONS.md](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/SborkaCobblemon/tasks/01_cobblemon_skills/docs/next_level_research/poke_gyms/10_OPEN_QUESTIONS.md) | Граничные условия, непроверенные на практике гипотезы и план внутриигровых тестов для Iteration 2. | ✅ CONFIRMED |

---

## 🗺️ Краткая карта системы Poké Gym

```text
[ Игрок с командой Pokémon ]
       │
       ▼
[ Расчёт среднего уровня партии ] ───► getPartyLevel() (анти-чит на оверлевел и легендарок)
       │
       ▼
[ Определение тира подиума ] ────────► getPlayerPodiumLevelTier() -> Tier 10..95 (или "elite" при апгрейде)
       │
       ▼
[ Спавн тренера на подиуме ] ────────► rctmod:trainer (кэшируется в NBT подиума)
       │                               ├── Обычный подиум: пулы Tier 10–95 / Босс Лиги каждые 15 побед
       │                               └── Улучшенный подиум: Elite Easy (75%) / Elite Hard (25%) / Tier 9 Boss
       ▼
[ Взаимодействие (Правый клик) ] ────► Проверка владения, проверка тира, проверка Монотипа (если надет Badge)
       │
       ▼
[ Бой Cobblemon / Showdown ] ────────► AI Level 0..11, предустановленные IV/EV, приемы, шапки
       │
       ├──► ПОРАЖЕНИЕ ───────────────► handleLeagueFee("loss"): штраф 5% баланса × (wins+1) [мин. 512, макс. 10k]
       │                               Сброс серии побед: bagItemsUsed = 0.
       │
       └──► ПОБЕДА ──────────────────► CobblemonEvents.BATTLE_VICTORY
                                       ├── Базовые деньги: Σ min(2000, max(round(lvl * 4 * trainerLvl * var), 16)), кап 5000
                                       ├── Мультипликатор Значка: ×2 монеты + дроп sunlit_cobblemon:badge_reward/<type>_type_gym
                                       ├── Мультипликатор Элиты: ×2 монеты + Medallion каждые 15 побед
                                       ├── Мультипликатор Искусства Боя: ×1.25 монеты (или 1% шанс дропа книги)
                                       ├── Майлстоун побед: дроп 10_wins.json / 100_wins.json каждые 10 / 100 побед
                                       └── Мастерство животноводства: 5% шанс на society:animal_cracker
```

---

## 🔑 Ключевые фундаментальные факты (Executive Summary)

1. **Значок (Badge) НЕ изменяет пул, тир или покемонов вражеского тренера.**  
   Вражеский тренер генерируется исключительно на основе уровня вашей команды (или статуса Elite). Значок накладывает **строгое ограничение на команду САМОГО игрока** (вся группа обязана быть строго монотипной с типом значка) и взамен **удваивает денежную награду и даёт дополнительный лут-дроп самоцветов, ТМ и конфет соответствующего типа**.
2. **Улучшение Подиума (`elite_stone`) — это фундаментальный скачок сложности.**  
   Подиум перестает скейлиться под ваш уровень и переключается на пул максимального уровня 88–100 (средний 96.4–99.9), где 71–99% врагов имеют идеальные 6×31 IV, боевые EV 252/252, синергичные шапки и соревновательный AI (вплоть до ранга 11).
3. **Мультипликаторы наград перемножаются.**  
   При наличии Значка (×2), улучшенного подиума (×2) и перка *The Art of Battle* (×1.25), базовый куш умножается на **×5.0** (до 25 000 монет за бой).
4. **Легендарные покемоны запрещены на стандартном подиуме.**  
   Присутствие хотя бы одного Legendary/Mythical покемона в группе выставляет виртуальный уровень группы в `105`, блокируя начало боя на обычном подиуме сообщением *"banned_mon"*. На улучшенном Elite-подиуме ограничение снимается.
