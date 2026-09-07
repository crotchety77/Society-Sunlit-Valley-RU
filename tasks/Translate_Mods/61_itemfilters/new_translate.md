# Локализация мода: itemfilters

**JAR:** `item-filters-forge-2001.1.0-build.59.jar` | **Всего строк:** 41 | **Не переведено:** 10

## 1. Визуальный контекст и оформление
* Форматирование: Названия предметов/блоков начинаются с Заглавной буквы.
* Валюта: использовать значок монеты `§e●` (`U+25CF`).
* Тултипы: подсветка клавиш `§6Shift + ПКМ§7`.

## 2. Непереведённые строки (требуют перевода)

```json
{
  "itemGroup.itemfilters.main": "TODO: Item Filters",
  "itemGroup.itemfilters.itemfilters": "TODO: Item Filters",
  "itemfilters.variants": "TODO: Variants [%d]",
  "itemfilters.help_text.variants": "TODO: Tab, Scroll Wheel, Cursor Up/Down: adjust highlight\nEnter: select highlighted",
  "itemfilters.help_text.filter": "TODO: Filter (Right-Click to clear)",
  "itemfilters.help_text.nbt": "TODO: NBT String\n▶ e.g. { text:\"hello\", value: 1, active: true }",
  "itemfilters.help_text.weak_nbt": "TODO: Weak NBT String\n▶ e.g. { text:\"hello\", value: 1, active: true }\n▶ Only the NBT fields supplied will be checked (any other fields in the item are ignored)",
  "itemfilters.help_text.regex": "TODO: Regular Expression\n Matched against the item ID\n▶ e.g. \"^minecraft:\" matches all vanilla items",
  "itemfilters.help_text.max_count": "TODO: Maximum Stack Size\n▶ May also include relational operators, e.g. \"<64\" or \">=16\"",
  "itemfilters.help_text.damage": "TODO: Item Damage\n▶ May also include relational operators, e.g. \"<10\" or \">=5\"\n and optionally by percentage, e.g. \">50%\""
}
```

## 3. Существующие переводы (для контекста)

```json
{
  "item.itemfilters.filter": "Предметный фильтр",
  "item.itemfilters.always_true": "Фильтр: всегда True",
  "item.itemfilters.always_true.description": "Соответствовать всем предметам",
  "item.itemfilters.always_false": "Фильтр: всегда False",
  "item.itemfilters.always_false.description": "Не соответствовать предметам",
  "item.itemfilters.or": "Фильтр: ИЛИ",
  "item.itemfilters.or.description": "Соответствовать одному из фильтров",
  "item.itemfilters.and": "Фильтр: И",
  "item.itemfilters.and.description": "Соответствовать всем фильтрам",
  "item.itemfilters.not": "Фильтр: НЕ",
  "item.itemfilters.not.description": "Инвертирует фильтр",
  "item.itemfilters.xor": "Фильтр: XOR",
  "item.itemfilters.xor.description": "Соответствовать только одному из двух фильров, но не обоим",
  "item.itemfilters.tag": "Фильтр по Тегу",
  "item.itemfilters.tag.description": "Имена тегов, например, 'minecraft:wool' или 'forge:cobblestone'",
  "item.itemfilters.mod": "Фильтр по мобу",
  "item.itemfilters.mod.description": "Используйте ID моба",
  "item.itemfilters.id_regex": "Фильтр по ID RegEx",
  "item.itemfilters.id_regex.description": "Проверяет ID предмета с помощью регулярных выражений",
  "item.itemfilters.damage": "Фильтр по урону",
  "item.itemfilters.damage.description": "Проверяет урон предмета",
  "item.itemfilters.block": "Фильтр по блоку",
  "item.itemfilters.block.description": "Проверяет, является ли предмет блоком",
  "item.itemfilters.max_count": "Фильтр максимального количества",
  "item.itemfilters.max_count.description": "Проверяет максимальное количество предметов",
  "item.itemfilters.strong_nbt": "Фильтр по NBT (Сильный)",
  "item.itemfilters.strong_nbt.description": "Соответствовать, если все NBT равны",
  "item.itemfilters.weak_nbt": "Фильтр по NBT  (Слабый)",
  "item.itemfilters.weak_nbt.description": "Соответствовать, если присутствует только указанная часть NBT",
  "item.itemfilters.custom": "Настраиваемый фильтр",
  "item.itemfilters.custom.description": "Требуется мод или скрипт для работы, обычно это KubeJS"
}
```
