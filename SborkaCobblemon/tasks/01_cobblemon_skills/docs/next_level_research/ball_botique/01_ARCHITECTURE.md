# 🏛️ 01_ARCHITECTURE — Архитектура магазина Ball Boutique

## 1. Компоненты системы

Магазин **Ball Boutique** (`shop.society_trading.ball_boutique`) построен на базе связки серверных скриптов KubeJS, кастомного Java-мода `society_trading` и системы спавна покемонов `cobblemon`.

| Компонент | Файл / Путь | Класс / Ресурсный ID | Назначение | Ключевые методы / Поля |
| :--- | :--- | :--- | :--- | :--- |
| **Shop JSON Definition** | `kubejs/data/society_trading/shops/ball_boutique.json` | `society_trading:ball_boutique` | Определение ассортимента, цен, случайных сетов, лимитов и условий видимости | `random_sets`, `trades`, `requires_season`, `requires_stage` |
| **Shop Core Logic** | `mods/society_trading-1.2.8.jar` | `com.kyanite.society_trading.common.Shop` | Хранение и сериализация структуры магазина, загрузка трейдов из DataPack | `fromNetwork`, `toNetwork`, `requiresStage`, `requiresSeason` |
| **Random Offers Handler** | `mods/society_trading-1.2.8.jar` | `com.kyanite.society_trading.common.RandomSetShopOffers` | Формирование ежедневных роллов случайных сетов с учётом условий видимости | `roll`, `getRolledOffers`, `playerCanSee` |
| **Shop Server Data** | `mods/society_trading-1.2.8.jar` | `com.kyanite.society_trading.common.ShopData` | Серверное сохранение текущего состояния роллов и синхронизация с клиентом | `getOrCreate`, `getShop`, `save` |
| **Trade Limit Capability** | `mods/society_trading-1.2.8.jar` | `com.kyanite.society_trading.common.capability.TradeLimitCapability` | Отслеживание количества покупок игрока по каждой сделке и ежедневный сброс | `getTradeCount`, `incrementTradeCount`, `resetTrades` |
| **Capsule Loot & Mechanics** | `kubejs/server_scripts/cobblemon/cobblemonGachaPools.js` | `ItemEvents.rightClicked` | Обработка открытия капсул, фильтрация пулов по качеству и генерация покемонов | `rollGacha`, `getGachaPool`, `getShinyChance` |
| **Item Quality System** | `kubejs/server_scripts/` & `mods/` | NBT: `{quality_food: {quality: X}}` / `{quality: X}` | Система качества предметов (0=Regular, 1=Silver, 2=Gold, 3=Iridium) | Чтение NBT-тегов качества в трейдах и при открытии |

---

## 2. Жизненный цикл магазина Ball Boutique

```mermaid
flowchart TD
    A["Новый день (Minecraft Time 06:00 / Day Change)"] --> B["ShopData.resetDailyTrades()"]
    B --> C["RandomSetShopOffers.roll()"]
    C --> D["Ролл 1 TM из 593 вариантов (Set 0)"]
    C --> E["Ролл 1 Капсулы из 52 вариантов (Set 1)"]
    
    F["Игрок открывает Ball Boutique (NPC / Блок)"] --> G{"Проверка playerCanSee()"}
    G -- "Стадия < trainer_lvl_3" --> H["Магазин недоступен / Скрыт"]
    G -- "Сезон != mid_*" --> H
    G -- "trainer_lvl_3 + mid_season" --> I["Отображение GUI магазина:"]
    
    I --> J["13 Постоянных сделок (Покеболы, Pofflet Box)"]
    I --> K["1 Случайный диск ТМ (Лимит: 4)"]
    I --> L["1 Случайная Капсула Гачамон (Лимит: 8)"]
    
    L --> M["Покупка: Списание Монет + Доп. предмета"]
    M --> N["Выдача предмета: sunlit_cobblemon:gachamon_capsule с NBT"]
    N --> O["Игрок нажимает ПКМ по капсуле"]
    O --> P["cobblemonGachaPools.js: rollGacha()"]
    P --> Q{"Качество >= 3 (или >=2 с перком)?"}
    Q -- "Да (Iridium)" --> R["100% Специальный Тематический Пул"]
    Q -- "Нет (Regular/Silver/Gold)" --> S["Базовый Пул (мусор) + Специальный Пул"]
    R --> T["Расчёт Shiny Chance + Спавн покемона"]
    S --> T
```

---

## 3. Точки интеграции и хранение данных

1. **Место хранения состояния роллов магазина**:
   - Хранится на сервере в `World Saved Data` (NBT мира) через класс `ShopData`.
   - Для магазинов со стилем `per_day` роллы привязаны к игровому дню Minecraft (`level.getDayTime() / 24000L`).
2. **Место хранения лимитов покупок игрока**:
   - Привязано к игроку через Forge Capability `TradeLimitCapability`.
   - Сбрасывается при наступлении нового игрового дня.
3. **Открытие магазина**:
   - Магазин имеет `selector_weight: -101`, что означает невозможность его случайного вызова через универсальный Auto-Trader. Он вызывается строго через диалог соответствующего NPC или интерактивный интерфейс тренера.
