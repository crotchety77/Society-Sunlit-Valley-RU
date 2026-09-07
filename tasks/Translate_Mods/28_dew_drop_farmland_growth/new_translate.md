# Локализация мода: dew_drop_farmland_growth (Земледелие, Удобрения и Спринклеры)

**JAR:** `dew_drop_farmland_growth-9.0.jar` | **Всего строк:** 28 | **Статус:** Полная локализация и аудит тултипов

---

## Блок 1: Визуальный шаблон (как это выглядит в игре)

### 1. Удобрения для скорости созревания
* **Слабое удобрение** (`item.dew_drop_farmland_growth.weak_fertilizer`):
  ```text
  §fСлабое удобрение§r
  §aСокращает время созревания примерно на 1 день§r
  ```
* **Сильное удобрение** (`item.dew_drop_farmland_growth.strong_fertilizer`):
  ```text
  §fСильное удобрение§r
  §aСокращает время созревания примерно на 2 дня§r
  ```
* **Гипер-удобрение** (`item.dew_drop_farmland_growth.hyper_fertilizer`):
  ```text
  §fГипер-удобрение§r
  §aСокращает время созревания примерно на 3 дня§r
  ```

### 2. Удобрения для увлажнения почвы
* **Увлажняющее удобрение** (`item.dew_drop_farmland_growth.hydrating_fertilizer`):
  ```text
  §fУвлажняющее удобрение§r
  §aПоддерживает пашню увлажнённой в течение первой половины роста культуры.§r
  ```
* **Роскошное увлажняющее удобрение** (`item.dew_drop_farmland_growth.deluxe_hydrating_fertilizer`):
  ```text
  §fРоскошное увлажняющее удобрение§r
  §aПашня никогда не высыхает (100%% автополив)§r
  ```

### 3. Удобрения для качества и урожайности
* **Удобрение базового качества** (`item.dew_drop_farmland_growth.low_quality_fertilizer`):
  ```text
  §fУдобрение базового качества§r
  §aПовышает шанс получить серебряный и золотой урожай§r
  §7Качество созреваемой культуры (при условии Обычных семян):
  ▪ Обычное: §f87,4%%§r
  §7▪ Серебряное: §f8,3%%§r
  §7▪ Золотое: §e4,3%%§r
  §7▪ Иридиевое: §b0,0%%§r
  ```
* **Удобрение высокого качества** (`item.dew_drop_farmland_growth.high_quality_fertilizer`):
  ```text
  §fУдобрение высокого качества§r
  §aЗначительно повышает шанс золотого и иридиевого урожая§r
  §7Качество созреваемой культуры (при условии Обычных семян):
  ▪ Обычное: §f20,3%%§r
  §7▪ Серебряное: §f36,6%%§r
  §7▪ Золотое: §e27,0%%§r
  §7▪ Иридиевое: §b16,1%%§r
  ```
* **Удобрение безупречного качества** (`item.dew_drop_farmland_growth.pristine_quality_fertilizer`):
  ```text
  §fУдобрение безупречного качества§r
  §aМаксимально повышает шанс золотого и иридиевого урожая§r
  §7Качество созреваемой культуры (при условии Обычных семян):
  ▪ Обычное: §f6,1%%§r
  §7▪ Серебряное: §f38,5%%§r
  §7▪ Золотое: §e33,9%%§r
  §7▪ Иридиевое: §b21,6%%§r
  ```
* **Изобильное удобрение** (`item.dew_drop_farmland_growth.bountiful_fertilizer`):
  ```text
  §fИзобильное удобрение§r
  §aШанс 25%% получить +1 доп. урожай при сборе§r
  §cУрожай всегда обычного качества (без звёзд)§r
  ```

### 4. Спринклеры (Автоматический полив)
* **Железный спринклер** (`block.dew_drop_farmland_growth.iron_sprinkler`):
  ```text
  §fЖелезный спринклер§r
  §7Поливает пашню каждое утро в 6:00.
  Можно вкапывать в уровень земли и украшать палкой (ПКМ).§r
  §aОбласть: 3x3§r §f(Радиус: 1)§r
  ```
* **Золотой спринклер** (`block.dew_drop_farmland_growth.gold_sprinkler`):
  ```text
  §fЗолотой спринклер§r
  §7Поливает пашню каждое утро в 6:00.
  Можно вкапывать в уровень земли и украшать палкой (ПКМ).§r
  §aОбласть: 5x5§r §f(Радиус: 2)§r
  ```
* **Алмазный спринклер** (`block.dew_drop_farmland_growth.diamond_sprinkler`):
  ```text
  §fАлмазный спринклер§r
  §7Поливает пашню каждое утро в 6:00.
  Можно вкапывать в уровень земли и украшать палкой (ПКМ).§r
  §aОбласть: 7x7§r §f(Радиус: 3)§r
  ```
* **Иридиевый спринклер** (`block.dew_drop_farmland_growth.netherite_sprinkler`):
  ```text
  §fИридиевый спринклер§r
  §7Поливает пашню каждое утро в 6:00.
  Можно вкапывать в уровень земли и украшать палкой (ПКМ).§r
  §aОбласть: 9x9§r §f(Радиус: 4)§r
  ```

### 5. Садовые горшки
* **Садовый горшок** (`block.dew_drop_farmland_growth.garden_pot`):
  ```text
  §fСадовый горшок§r
  §7Позволяет выращивать культуры в помещении в любой сезон. Нельзя поливать спринклерами.§r
  §aИспользование "Роскошного увлажняющего удобрения" избавляет от необходимости поливать горшок. Можно подвешивать на цепь и верёвку.§r
  ```

---

## Блок 2: Точные строки и ключи локализации

### В `translations/mods/dew_drop_farmland_growth.json`:
```json
{
  "itemGroup.dew_drop_farmland_growth": "Капли росы: Земледелие",
  "block.dew_drop_farmland_growth.weak_fertilized_farmland": "Слабо удобренная пашня",
  "block.dew_drop_farmland_growth.strong_fertilized_farmland": "Сильно удобренная пашня",
  "block.dew_drop_farmland_growth.hyper_fertilized_farmland": "Гипер-удобренная пашня",
  "block.dew_drop_farmland_growth.hydrating_farmland": "Увлажнённая пашня",
  "block.dew_drop_farmland_growth.deluxe_hydrating_farmland": "Роскошная увлажнённая пашня",
  "block.dew_drop_farmland_growth.low_quality_fertilized_farmland": "Пашня с удобрением базового качества",
  "block.dew_drop_farmland_growth.high_quality_fertilized_farmland": "Пашня с удобрением высокого качества",
  "block.dew_drop_farmland_growth.pristine_quality_fertilized_farmland": "Пашня с удобрением безупречного качества",
  "block.dew_drop_farmland_growth.bountiful_fertilized_farmland": "Изобильно удобренная пашня",
  "item.dew_drop_farmland_growth.weak_fertilizer": "Слабое удобрение",
  "item.dew_drop_farmland_growth.strong_fertilizer": "Сильное удобрение",
  "item.dew_drop_farmland_growth.hyper_fertilizer": "Гипер-удобрение",
  "item.dew_drop_farmland_growth.hydrating_fertilizer": "Увлажняющее удобрение",
  "item.dew_drop_farmland_growth.deluxe_hydrating_fertilizer": "Роскошное увлажняющее удобрение",
  "item.dew_drop_farmland_growth.bountiful_fertilizer": "Изобильное удобрение",
  "item.dew_drop_farmland_growth.low_quality_fertilizer": "Удобрение базового качества",
  "item.dew_drop_farmland_growth.high_quality_fertilizer": "Удобрение высокого качества",
  "item.dew_drop_farmland_growth.pristine_quality_fertilizer": "Удобрение безупречного качества",
  "block.dew_drop_farmland_growth.tilled_sand": "Вспаханный песок",
  "block.dew_drop_farmland_growth.hyper_fertilized_sand": "Гипер-удобренный песок",
  "block.dew_drop_farmland_growth.iron_sprinkler": "Железный спринклер",
  "block.dew_drop_farmland_growth.gold_sprinkler": "Золотой спринклер",
  "block.dew_drop_farmland_growth.diamond_sprinkler": "Алмазный спринклер",
  "block.dew_drop_farmland_growth.netherite_sprinkler": "Иридиевый спринклер",
  "block.dew_drop_farmland_growth.garden_pot": "Садовый горшок",
  "block.dew_drop_farmland_growth.rope_hanging_garden_pot": "Подвесной садовый горшок на верёвке",
  "block.dew_drop_farmland_growth.iron_hanging_garden_pot": "Подвесной садовый горшок на цепи"
}
```

### В `translations/society/ru_ru.json` (Тултипы удобрений и спринклеров):
```json
{
  "tooltip.society.weak_fertilizer": "Сокращает время созревания примерно на 1 день",
  "tooltip.society.strong_fertilizer": "Сокращает время созревания примерно на 2 дня",
  "tooltip.society.hyper_fertilizer": "Сокращает время созревания примерно на 3 дня",
  "tooltip.society.hydrating_fertilizer": "Поддерживает пашню увлажнённой в течение первой половины роста культуры.",
  "tooltip.society.deluxe_hydrating_fertilizer": "Пашня никогда не высыхает (100%% автополив)",
  "tooltip.society.bountiful_fertilizer": "Шанс 25%% получить +1 доп. урожай при сборе",
  "tooltip.society.bountiful_fertilizer.warn": "Урожай всегда обычного качества (без звёзд)",
  "tooltip.society.low_quality_fertilizer": "Повышает шанс получить серебряный и золотой урожай\n§7Качество созреваемой культуры (при условии Обычных семян):\n▪ Обычное: §f87,4%%\n§7▪ Серебряное: §f8,3%%\n§7▪ Золотое: §e4,3%%\n§7▪ Иридиевое: §b0,0%%",
  "tooltip.society.high_quality_fertilizer": "Значительно повышает шанс золотого и иридиевого урожая\n§7Качество созреваемой культуры (при условии Обычных семян):\n▪ Обычное: §f20,3%%\n§7▪ Серебряное: §f36,6%%\n§7▪ Золотое: §e27,0%%\n§7▪ Иридиевое: §b16,1%%",
  "tooltip.society.pristine_quality_fertilizer": "Максимально повышает шанс золотого и иридиевого урожая\n§7Качество созреваемой культуры (при условии Обычных семян):\n▪ Обычное: §f6,1%%\n§7▪ Серебряное: §f38,5%%\n§7▪ Золотое: §e33,9%%\n§7▪ Иридиевое: §b21,6%%",
  "tooltip.society.sprinkler": "Поливает пашню каждое утро в 6:00.\nМожно вкапывать в уровень земли и украшать палкой (ПКМ)",
  "tooltip.society.sprinkler.area": "Область: %s §f(Радиус: %s)§r",
  "tooltip.society.area": "Область: %s",
  "item.society.garden_pot.description": "Позволяет выращивать культуры в помещении в любой сезон. Нельзя поливать спринклерами.",
  "item.society.garden_pot.description.tip": "Использование \"Роскошного увлажняющего удобрения\" избавляет от необходимости поливать горшок. Можно подвешивать на цепь и верёвку."
}
```
