// Priority: 10
// Скрипт KubeJS для понятных игровых подсказок (tooltips) мода Unusual Fish
// Разработано на основе подтверждённого технического аудита кода (MECHANICS-AUDIT.md)
// Примечание: Древнее оружие отключено сборкой в globalRemovedItems.js; Скат-блинчик — крупный дикий моб океана (без ведра).

ItemEvents.tooltip((tooltip) => {
  // 1. Морской шип / Подводная мина (unusualfishmod:sea_boom)
  tooltip.add("unusualfishmod:sea_boom", [
    Text.of("Взводится в воде и атакует цели в радиусе 2 блоков.").gray(),
    Text.of("Выпускает 24 шипа (по 5 урона каждый).").gold(),
    Text.of("ПКМ с двуликой рыбой-ласточкой: ").gold().append(Text.of("переключить «Только враждебные мобы».").gray())
  ]);

  // 2. Вольт-детектор (unusualfishmod:volt_detector)
  tooltip.add("unusualfishmod:volt_detector", [
    Text.of("Обнаруживает существ и подаёт сигнал редстоуна.").gray(),
    Text.of("Базовый радиус: ").gray().append(Text.of("2,5 блока").gold()),
    Text.of("Каждая ").gray().append(Text.of("медная антенна").gold()).append(Text.of(" увеличивает радиус на 2,5 блока.").gray())
  ]);

  // 3. Медная антенна (unusualfishmod:copper_antenna)
  tooltip.add("unusualfishmod:copper_antenna", [
    Text.of("Устанавливается на ").gray().append(Text.of("Вольт-детектор").gold()).append(Text.of(", увеличивая радиус его сканирования на 2,5 блока.").gray())
  ]);

  // 4. Погодные ракушки (Weather Shells)
  tooltip.add("unusualfishmod:fluvial_shell", [
    Text.of("Зажмите ПКМ, чтобы вызвать дождь на 1 минуту.").blue(),
    Text.of("Расходует 1 ед. прочности.").darkGray()
  ]);

  tooltip.add("unusualfishmod:thunderous_shell", [
    Text.of("Зажмите ПКМ, чтобы вызвать грозовой шторм на 1 минуту.").yellow(),
    Text.of("Расходует 1 ед. прочности.").darkGray()
  ]);

  tooltip.add("unusualfishmod:clement_shell", [
    Text.of("Зажмите ПКМ, чтобы разогнать тучи и вернуть ясную погоду на 30 минут.").white(),
    Text.of("Расходует 1 ед. прочности.").darkGray()
  ]);

  // 5. Призмариновое копьё (unusualfishmod:prismarine_spear)
  tooltip.add("unusualfishmod:prismarine_spear", [
    Text.of("Зажмите ПКМ (0,5 сек), чтобы метнуть копьё во врага.").aqua(),
    Text.of("Подбирается после броска.").gray()
  ]);

  // 6. Сырой лобстер (unusualfishmod:raw_lobster) - подсказка о прикормке ската
  tooltip.add("unusualfishmod:raw_lobster", [
    Text.of("Любимое лакомство ").gray().append(Text.of("Морского блинчика (ската)").gold()).append(Text.of(".")).gray(),
    Text.of("Покормите им ската в тёплом океане, чтобы получить сокровища со дна.").yellow()
  ]);
});
