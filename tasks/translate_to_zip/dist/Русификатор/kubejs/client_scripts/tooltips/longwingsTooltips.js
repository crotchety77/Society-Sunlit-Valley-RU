// Priority: 10
// Скрипт KubeJS для понятных игровых подсказок (tooltips) мода Longwings (Бабочки и шелкопряды)
// Разработано на основе подтверждённого глубокого аудита кода (DEEP-MECHANICS-AUDIT.md)

ItemEvents.tooltip((tooltip) => {
  // 1. Ловчий сачок (longwings:catching_net)
  tooltip.add("longwings:catching_net", [
    Text.of("Мгновенно ловит летающих бабочек и мотыльков в инвентарь.").gray(),
    Text.of("ПКМ: ").gold().append(Text.of("взмах сачком перед собой.").gray()),
    Text.of("Прочность расходуется лишь в 1 из 15 взмахов (ресурс ~960 поимок).").darkGray()
  ]);

  // 2. Справочник по бабочкам и мотылькам (longwings:butterfly_handbook)
  tooltip.add("longwings:butterfly_handbook", [
    Text.of("Иллюстрированная энциклопедия всех видов бабочек и мотыльков.").gray(),
    Text.of("Встроенный климатомер: ").gold().append(Text.of("держите в руке, чтобы видеть температуру и влажность биома на экране.").yellow()),
    Text.of("Зажмите Shift для подробного отчёта о климате.").gray()
  ]);

  // 3. Миска с сахарной водой (longwings:sugar_water_bowl)
  tooltip.add("longwings:sugar_water_bowl", [
    Text.of("Питательный напиток для игрока и корм для бабочек.").gray(),
    Text.of("Скрытые ритуалы стаи:").gold(),
    Text.of("• Выпейте возле 10+ бабочек: ").aqua().append(Text.of("даёт планирующий полёт и 100% иммунитет к падению.").gray()),
    Text.of("• Выпейте возле 10+ мотыльков: ").green().append(Text.of("даёт шанс 8% найти древние семена Факельника/Кувшинника при срезке листвы.").gray())
  ]);

  // 4. Миска с медовой водой (longwings:honey_water_bowl)
  tooltip.add("longwings:honey_water_bowl", [
    Text.of("Сладкое лакомство для кормушек бабочек.").gray(),
    Text.of("Стимулирует питание и откладывание яиц в инсектарии.").yellow()
  ]);

  // 5. Капельная приманка для бабочек (longwings:butterfly_driplure)
  tooltip.add("longwings:butterfly_driplure", [
    Text.of("Приманивает и спавнит диких чешуекрылых в радиусе.").gray(),
    Text.of("Заправляется ").gray().append(Text.of("фруктовым нектаром").gold()).append(Text.of(" (яблочным, арбузным или ягодным).").gray()),
    Text.of("Призываемый вид зависит от температуры и влажности биома.").yellow()
  ]);

  // 6. Кормушка для бабочек (longwings:butterfly_feeder_bowl)
  tooltip.add("longwings:butterfly_feeder_bowl", [
    Text.of("Станция кормления для искусственных инсектариев.").gray(),
    Text.of("Заправляется сахарной или медовой водой для поддержания стаи.").yellow()
  ]);

  // 7. Защитная сетка (longwings:netting)
  tooltip.add("longwings:netting", [
    Text.of("Ограждение инсектария — не выпускает бабочек и мотыльков наружу.").gray(),
    Text.of("ПКМ Ножницами: ").gold().append(Text.of("переключить декоративный узор плетения.").gray()),
    Text.of("Защищает хрупкие яичные кладки от случайного растаптывания.").darkGray()
  ]);

  // 8. Стеклянная банка для бабочек (longwings:glass_jar)
  tooltip.add("longwings:glass_jar", [
    Text.of("Декоративный террариум для демонстрации живых насекомых.").gray(),
    Text.of("ПКМ с пойманной бабочкой или мотыльком, чтобы поместить внутрь.").yellow()
  ]);

  // 9. Блоки забродивших фруктов (Fruit Mush Blocks)
  const brewBlocks = [
    "longwings:apple_butterfly_brew_block",
    "longwings:melon_butterfly_brew_block",
    "longwings:berry_butterfly_brew_block"
  ];
  brewBlocks.forEach(id => {
    tooltip.add(id, [
      Text.of("Вязкая масса забродивших фруктов для варки нектара.").gray(),
      Text.of("Амортизатор: ").gold().append(Text.of("полностью поглощает урон от падения с любой высоты.").green()),
      Text.of("Замедляет передвижение на 75%.").darkGray()
    ]);
  });
});
