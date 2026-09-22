# 🔮 Ball Boutique & Gachamon Capsules — Deep Code Audit (Index)

> **Статус исследования**: Завершено (Iteration 1: Deep Code & Bytecode Audit)  
> **Пространство имён**: `society_trading`, `sunlit_cobblemon`, `cobblemon`  
> **Ключевые исходные файлы**: 
> - `kubejs/data/society_trading/shops/ball_boutique.json`
> - `kubejs/server_scripts/cobblemon/cobblemonGachaPools.js`
> - `mods/society_trading-1.2.8.jar` (`RandomSetShopOffers`, `RandomStyle`, `ShopData`)

---

## 📌 Оглавление базы знаний

| Файл | Описание | Ключевые темы |
| :--- | :--- | :--- |
| [01_ARCHITECTURE.md](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/SborkaCobblemon/tasks/01_cobblemon_skills/docs/next_level_research/ball_botique/01_ARCHITECTURE.md) | **Архитектура магазина** | Регистрация магазина, селектор, классы, триггеры обновления, персистентность |
| [02_CAPSULE_CATALOG.md](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/SborkaCobblemon/tasks/01_cobblemon_skills/docs/next_level_research/ball_botique/02_CAPSULE_CATALOG.md) | **Полный каталог капсул** | Все 13 типов капсул × 4 уровня качества (52 торговые сделки) |
| [03_PRICES_AND_CURRENCY.md](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/SborkaCobblemon/tasks/01_cobblemon_skills/docs/next_level_research/ball_botique/03_PRICES_AND_CURRENCY.md) | **Цены и валютная система** | Система монет `numismatics`, конвертация, множители качества, кастомные цены |
| [04_REQUIRED_ITEMS.md](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/SborkaCobblemon/tasks/01_cobblemon_skills/docs/next_level_research/ball_botique/04_REQUIRED_ITEMS.md) | **Дополнительные предметы** | Вторичные требования для покупки (Animal Cracker, Gems, Canvas, Wreath и др.) |
| [05_CAPSULE_CONTENTS.md](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/SborkaCobblemon/tasks/01_cobblemon_skills/docs/next_level_research/ball_botique/05_CAPSULE_CONTENTS.md) | **Содержимое капсул и пулы** | Все 13 тематических пулов покемонов, базовый пул, веса, уровни и формы |
| [06_QUALITY_AND_RARITY.md](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/SborkaCobblemon/tasks/01_cobblemon_skills/docs/next_level_research/ball_botique/06_QUALITY_AND_RARITY.md) | **Качество (Quality) и Шайни** | Градация Regular $\rightarrow$ Iridium, фильтрация базового пула, формулы Shiny Chance |
| [07_SHOP_ROTATION.md](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/SborkaCobblemon/tasks/01_cobblemon_skills/docs/next_level_research/ball_botique/07_SHOP_ROTATION.md) | **Механика ротации и лимиты** | Алгоритм ежедневного ролла (`rolled_count: 1`), лимит в 8 покупок, TMs |
| [08_SEASONAL_AVAILABILITY.md](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/SborkaCobblemon/tasks/01_cobblemon_skills/docs/next_level_research/ball_botique/08_SEASONAL_AVAILABILITY.md) | **Сезонная доступность** | Субсезоны `mid_*` (дни 10–20 каждого сезона), стадия `trainer_lvl_3` |
| [09_ECONOMICS.md](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/SborkaCobblemon/tasks/01_cobblemon_skills/docs/next_level_research/ball_botique/09_ECONOMICS.md) | **Экономика и практическая ценность** | Реальная себестоимость, анализ полезности капсул, приоритеты прокачки |
| [10_EVIDENCE.md](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/SborkaCobblemon/tasks/01_cobblemon_skills/docs/next_level_research/ball_botique/10_EVIDENCE.md) | **Реестр доказательств** | Точные цитаты из байткода JAR и скриптов KubeJS |
| [11_OPEN_QUESTIONS.md](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/SborkaCobblemon/tasks/01_cobblemon_skills/docs/next_level_research/ball_botique/11_OPEN_QUESTIONS.md) | **Открытые вопросы и план Iteration 2** | Подготовка к стратегическому гайду |

---

## 🎯 Краткое резюме ключевых механик

1. **Доступность**: Магазин открывается только при наличии стадии **`trainer_lvl_3`** и строго в середине каждого из 4 сезонов (`mid_spring`, `mid_summer`, `mid_autumn`, `mid_winter` — это ровно **дни 10–19/20** 28-дневного сезона Serene Seasons).
2. **Ассортимент**:
   - **13 постоянных сделок**: Pofflet Box (лимит 4) и 12 видов специальных покеболов (Premier, Heal, Lure, Friend, Nest, Dive, Sword, Shield, Dusk, Quick, Repeat, Timer).
   - **Случайный сет 0 (ТМ)**: Роллится 1 ТМ из пула 593 доступных технических дисков (цена 4 Sun монеты, лимит 4).
   - **Случайный сет 1 (Gachamon Capsules)**: Роллится **ровно 1 капсула** в день из 52 возможных комбинаций (13 типов × 4 качества).
3. **Лимит покупок**: Лимит на выпавшую капсулу составляет **8 покупок в день** (`limit: 8`).
4. **Качество капсул**:
   - `0` (Regular / Обычное): Базовый пул + Тематический пул смешаны. Шанс Шайни: `0.1%`.
   - `1` (Silver / Серебряное): Базовый пул + Тематический пул смешаны. Шанс Шайни: `0.25%`.
   - `2` (Gold / Золотое): Базовый пул + Тематический пул смешаны. Шанс Шайни: `0.5%`.
   - `3` (Iridium / Иридиевое): **Исключает базовый пул! 100% гарантия тематического пула!** Шанс Шайни: `1.0%` (до `2.0%` с перком).
