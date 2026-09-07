# Согласование перевода и оформления: Улучшения механизмов (Machine Upgrades)

В этом файле собраны все 15 предметов сборки, модифицирующие ремесленные станки и механизмы (`globalArtisanMachineDefinitions.js`).

---

## 1. Сводная таблица предметов-улучшений

| Предмет улучшения | Целевой станок / механизм | Новое форматированное описание |
| :--- | :--- | :--- |
| **§6Крошечный гном**<br>`society:tiny_gnome` | **Ткацкий станок**<br>`society:loom` | Улучшение для %s: §e+25%§7 шанс получить случайный предмет §6Мебели§7 |
| **§6Розовая материя**<br>`society:pink_matter` | **Сырный пресс**<br>`society:cheese_press` | Улучшение для %s: производит §aВыдержанный сыр§7 из §fБольшого молока§7 напрямую, без этапа выдержки в бочке |
| **§6Медальон памяти**<br>`society:gray_anatomy` | **Винный бочонок**<br>`society:wine_keg` | Улучшение для %s: §e+5%§7 шанс создания §6Тайника с магическими реликвиями§7 |
| **§6Сломанные часы**<br>`society:broken_clock` | **Бочка для выдержки**<br>`society:aging_cask` | Улучшение для %s: сокращает время выдержки вдвое |
| **§6Механический штекер**<br>`society:inserter` | **Древняя бочка**<br>`society:ancient_cask` | Улучшение для %s: обработка §e4 предметов§7 за цикл |
| **§6Чёрный опал**<br>`society:black_opal` | **Кристаляриум**<br>`society:crystalarium` | Улучшение для %s: §e+10%§7 шанс создания самоцветов §6Безупречного качества§7 |
| **§6Бесконечный червь**<br>`society:infinity_worm` | **Улучшенная червячная ферма**<br>`society:deluxe_worm_farm` | Улучшение для %s: бесконечная работа без расхода ресурсов |
| **§6Древняя икра**<br>`society:ancient_roe` | **Коптильня для рыбы**<br>`society:fish_smoker` | Улучшение для %s: §aудваивает§7 получаемую продукцию |
| **§6Грибной побег**<br>`society:cordycep` | **Дегидратор**<br>`society:dehydrator` | Улучшение для %s: §aудваивает§7 урожай грибов |
| **§6Алхимический желток**<br>`society:enkephalin` | **Майонезный аппарат**<br>`society:mayonnaise_machine` | Улучшение для %s: §e+5%§7 шанс создания §6Превосходного майонеза§7 |
| **§6Каменная рука**<br>`society:stone_hand` | **Банка для варенья**<br>`society:preserves_jar` | Улучшение для %s: снижает расход сырья на §e2 шт.§7 |
| **§6Древняя шестерня**<br>`society:ancient_cog` | **Семенатор**<br>`society:seed_maker` | Улучшение для %s: §e+5%§7 шанс создания §bсемян Древнего плода§7 |
| **§6Замёрзший наконечник**<br>`society:frosted_tip` | **Зарядный стержень**<br>`society:charging_rod` | Улучшение для %s: работа зимой и §aутроение§7 выработки энергии |
| **Переработанное ядро**<br>`society:recycled_core` | **Перерабатывающий автомат**<br>`society:recycling_machine` | Улучшение для %s: §aудваивает§7 большинство результатов |
| **§6Морской сухарь**<br>`society:sea_biscut` | **Рыбный пруд**<br>`society:fish_pond` | Улучшение для %s: §aудваивает§7 шанс получения побочных продуктов (не влияет на икру) |

---

## 2. Точные ключи локализации (JSON)

```json
{
  "item.society.ancient_cog": "§6Древняя шестерня",
  "item.society.ancient_cog.description": "Улучшение для %s: §e+5%%§7 шанс создания §bсемян Древнего плода§7",
  "item.society.pink_matter": "§6Розовая материя",
  "item.society.pink_matter.description": "Улучшение для %s: производит §aВыдержанный сыр§7 из §fБольшого молока§7 напрямую, без этапа выдержки в бочке",
  "item.society.stone_hand": "§6Каменная рука",
  "item.society.stone_hand.description": "Улучшение для %s: снижает расход сырья на §e2 шт.§7",
  "item.society.broken_clock": "§6Сломанные часы",
  "item.society.broken_clock.description": "Улучшение для %s: сокращает время выдержки вдвое",
  "item.society.sea_biscut": "§6Морской сухарь",
  "item.society.sea_biscut.description": "Улучшение для %s: §aудваивает§7 шанс получения побочных продуктов (не влияет на икру)",
  "item.society.black_opal": "§6Чёрный опал",
  "item.society.black_opal.description": "Улучшение для %s: §e+10%%§7 шанс создания самоцветов §6Безупречного качества§7",
  "item.society.enkephalin": "§6Алхимический желток",
  "item.society.enkephalin.description": "Улучшение для %s: §e+5%%§7 шанс создания §6Превосходного майонеза§7",
  "item.society.tiny_gnome": "§6Крошечный гном",
  "item.society.tiny_gnome.description": "Улучшение для %s: §e+25%%§7 шанс получить случайный предмет §6Мебели§7",
  "item.society.ancient_roe": "§6Древняя икра",
  "item.society.ancient_roe.description": "Улучшение для %s: §aудваивает§7 получаемую продукцию",
  "item.society.frosted_tip": "§6Замёрзший наконечник",
  "item.society.frosted_tip.description": "Улучшение для %s: работа зимой и §aутроение§7 выработки энергии",
  "item.society.infinity_worm": "§6Бесконечный червь",
  "item.society.infinity_worm.description": "Улучшение для %s: бесконечная работа без расхода ресурсов",
  "item.society.inserter": "§6Механический штекер",
  "item.society.inserter.description": "Улучшение для %s: обработка §e4 предметов§7 за цикл",
  "item.society.cordycep": "§6Грибной побег",
  "item.society.cordycep.description": "Улучшение для %s: §aудваивает§7 урожай грибов",
  "item.society.gray_anatomy": "§6Медальон памяти",
  "item.society.gray_anatomy.description": "Улучшение для %s: §e+5%%§7 шанс создания §6Тайника с магическими реликвиями§7",
  "item.society.recycled_core": "Переработанное ядро",
  "item.society.recycled_core.description": "Улучшение для %s: §aудваивает§7 большинство результатов"
}
```
