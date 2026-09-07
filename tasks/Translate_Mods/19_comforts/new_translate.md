# Локализация мода: comforts

**JAR:** `comforts-forge-6.4.0+1.20.1.jar` | **Всего строк:** 77 | **Не переведено:** 37

## 1. Визуальный контекст и оформление
* Форматирование: Названия предметов/блоков начинаются с Заглавной буквы.
* Валюта: использовать значок монеты `§e●` (`U+25CF`).
* Тултипы: подсветка клавиш `§6Shift + ПКМ§7`.

## 2. Непереведённые строки (требуют перевода)

```json
{
  "itemGroup.comforts": "TODO: Comforts",
  "itemGroup.comforts.general": "TODO: Comforts",
  "comforts.skipping_day": "TODO: Sleeping through this day",
  "item.comforts.sleeping_bag.auto_use.tooltip": "TODO: Automatically attempts to sleep.\nTo place, use while crouching.",
  "item.comforts.hammock.placement.tooltip": "TODO: Requires %s to place.",
  "item.comforts.rope_and_nail.placement.tooltip": "TODO: Used for placing hammocks.",
  "block.comforts.no_sleep": "TODO: This is decorative, you cannot sleep here",
  "block.comforts.hammock.no_sleep.2": "TODO: You can only sleep during the day, at night, or during thunderstorms",
  "block.comforts.hammock.no_rope": "TODO: You must hang the hammock on a pair of rope and nail",
  "block.comforts.hammock.no_space": "TODO: There is not enough space to fit the hammock",
  "block.comforts.hammock.missing_rope": "TODO: There must also be a rope and nail on the other end to hang the hammock",
  "gui.comforts.config.autoUse.name": "TODO: Automatically use sleeping bags",
  "gui.comforts.config.autoUse.description": "TODO: If enabled, players automatically attempt to use sleeping bags when placed.",
  "gui.comforts.config.restrictSleeping.name": "TODO: Restrict consecutive sleeping",
  "gui.comforts.config.restrictSleeping.description": "TODO: If enabled, players cannot sleep again for a period of time after sleeping.",
  "gui.comforts.config.restMultiplier.name": "TODO: Sleepiness multiplier",
  "gui.comforts.config.restMultiplier.description": "TODO: If restrictSleeping is true, this value will determine the length of wait time (larger numbers sleep sooner).",
  "gui.comforts.config.hammockUse.name": "TODO: Time of day to use hammocks",
  "gui.comforts.config.hammockUse.description": "TODO: The time of day that hammocks can be used.",
  "gui.comforts.config.sleepingBagUse.name": "TODO: Time of day to use sleeping bags",
  "gui.comforts.config.sleepingBagUse.description": "TODO: The time of day that sleeping bags can be used.",
  "gui.comforts.config.sleepingBagBreakChance.name": "TODO: Sleeping bag break chance",
  "gui.comforts.config.sleepingBagBreakChance.description": "TODO: The percentage chance that a sleeping bag will break upon use.",
  "gui.comforts.config.sleepingBagBreakChanceLuckMultiplier.name": "TODO: Sleeping bag luck multiplier",
  "gui.comforts.config.sleepingBagBreakChanceLuckMultiplier.description": "TODO: The value that will be multiplied by a player's luck then added to sleepingBagBreakChance.",
  "gui.comforts.config.sleepingBagEffects.name": "TODO: Sleeping bag effects",
  "gui.comforts.config.sleepingBagEffects.description": "TODO: The status effects to apply to players after using the sleeping bag.\nFormat: effect;duration(secs);power",
  "gui.comforts.config.hammocksStopPhantoms.name": "TODO: Hammocks stop phantoms",
  "gui.comforts.config.hammocksStopPhantoms.description": "TODO: If enabled, attempting to sleep in hammocks stops phantoms from spawning.",
  "gui.comforts.config.sleepingBagsStopPhantoms.name": "TODO: Sleeping bags stop phantoms",
  "gui.comforts.config.sleepingBagsStopPhantoms.description": "TODO: If enabled, attempting to sleep in sleeping bags stops phantoms from spawning.",
  "gui.comforts.config.daySleepingPercentage.name": "TODO: Day sleep percentage",
  "gui.comforts.config.daySleepingPercentage.description": "TODO: What percentage of players must sleep to skip the day.\nA percentage value of 0 will allow the day to be skipped by just 1 player, and a percentage value of 100 will require all players to sleep before skipping the day.\nA value of less than 0 will default to the playerSleepingPercentage game rule.",
  "gui.comforts.config.dayWakeTimeOffset.name": "TODO: Night to day wake time offset",
  "gui.comforts.config.dayWakeTimeOffset.description": "TODO: The amount of time, in ticks, to add or remove from the new time after sleeping through a night.",
  "gui.comforts.config.nightWakeTimeOffset.name": "TODO: Day to night wake time offset",
  "gui.comforts.config.nightWakeTimeOffset.description": "TODO: The amount of time, in ticks, to add or remove from the new time after sleeping through a day."
}
```

## 3. Существующие переводы (для контекста)

```json
{
  "block.comforts.hammock_black": "Чёрный гамак",
  "block.comforts.hammock_blue": "Синий гамак",
  "block.comforts.hammock_brown": "Коричневый гамак",
  "block.comforts.hammock_cyan": "Бирюзовый гамак",
  "block.comforts.hammock_gray": "Серый гамак",
  "block.comforts.hammock_green": "Зелёный гамак",
  "block.comforts.hammock_light_blue": "Голубой гамак",
  "block.comforts.hammock_light_gray": "Светло-серый гамак",
  "block.comforts.hammock_lime": "Лаймовый гамак",
  "block.comforts.hammock_magenta": "Пурпурный гамак",
  "block.comforts.hammock_orange": "Оранжевый гамак",
  "block.comforts.hammock_pink": "Розовый гамак",
  "block.comforts.hammock_purple": "Фиолетовый гамак",
  "block.comforts.hammock_red": "Красный гамак",
  "block.comforts.hammock_white": "Белый гамак",
  "block.comforts.hammock_yellow": "Жёлтый гамак",
  "block.comforts.rope_and_nail": "Верёвка и гвоздь",
  "block.comforts.sleeping_bag_black": "Чёрный спальный мешок",
  "block.comforts.sleeping_bag_blue": "Синий спальный мешок",
  "block.comforts.sleeping_bag_brown": "Коричневый спальный мешок",
  "block.comforts.sleeping_bag_cyan": "Бирюзовый спальный мешок",
  "block.comforts.sleeping_bag_gray": "Серый спальный мешок",
  "block.comforts.sleeping_bag_green": "Зелёный спальный мешок",
  "block.comforts.sleeping_bag_light_blue": "Голубой спальный мешок",
  "block.comforts.sleeping_bag_light_gray": "Светло-серый спальный мешок",
  "block.comforts.sleeping_bag_lime": "Лаймовый спальный мешок",
  "block.comforts.sleeping_bag_magenta": "Пурпурный спальный мешок",
  "block.comforts.sleeping_bag_orange": "Оранжевый спальный мешок",
  "block.comforts.sleeping_bag_pink": "Розовый спальный мешок",
  "block.comforts.sleeping_bag_purple": "Фиолетовый спальный мешок",
  "block.comforts.sleeping_bag_red": "Красный спальный мешок",
  "block.comforts.sleeping_bag_white": "Белый спальный мешок",
  "block.comforts.sleeping_bag_yellow": "Жёлтый спальный мешок",
  "block.comforts.hammock.occupied": "Этот гамак занят",
  "block.comforts.sleeping_bag.occupied": "Этот спальный мешок занят",
  "block.comforts.hammock.too_far_away": "Вы не можете вздремнуть, гамак слишком далеко",
  "block.comforts.sleeping_bag.too_far_away": "Вы не можете уснуть, спальный мешок слишком далеко",
  "block.comforts.hammock.no_sleep": "Вздремнуть можно только днём",
  "block.comforts.sleeping_bag.broke": "Спальный мешок сломан",
  "capability.comforts.not_sleepy": "Вы недостаточно устали для отдыха"
}
```
