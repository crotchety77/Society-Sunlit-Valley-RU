// Priority: 10
// Скрипт KubeJS для понятных игровых подсказок (tooltips) мода Etcetera
// Разработано на основе подтверждённого глубокого аудита кода (DEEP-MECHANICS-AUDIT.md)

ItemEvents.tooltip((tooltip) => {
  // 1. Ручной колокольчик (etcetera:handbell)
  tooltip.add("etcetera:handbell", [
    Text.of("ПКМ: ").gold().append(Text.of("издаёт звон в радиусе ").gray()).append(Text.of("48 блоков").gold()).append(Text.of(".")),
    Text.of("Подсвечивает ваших прирученных питомцев и эллеев, созывая к себе тех, кто не сидит на месте.").yellow()
  ]);

  // 2. Приливный шлем (etcetera:tidal_helmet)
  tooltip.add("etcetera:tidal_helmet", [
    Text.of("При погружении в воду дарует ").gray().append(Text.of("силу источника на 1,5 минуты").aqua()).append(Text.of(".")),
    Text.of("Оснащён анимированным индикатором запаса дыхания на экране.").gray()
  ]);

  // 3. Черепаший плот (etcetera:turtle_raft)
  tooltip.add("etcetera:turtle_raft", [
    Text.of("Морской плот на 2 пассажиров из черепашьих щитков.").gray(),
    Text.of("ПКМ с флагом: ").gold().append(Text.of("закрепить флаг на корме.").gray()),
    Text.of("Shift + ПКМ пустой рукой: ").gold().append(Text.of("снять установленный флаг.").gray())
  ]);

  // 4. Яйцеяблоко (etcetera:eggple)
  tooltip.add("etcetera:eggple", [
    Text.of("Плод яблоплёнка. Можно бросить как яйцо.").gray(),
    Text.of("Гарантированно (100%) ").green().append(Text.of("вылупляет цыплёнка-яблоплёнка.").gray()),
    Text.of("Шанс 0,625% вылупить сразу 4 цыплят.").darkGray()
  ]);

  // 5. Золотое яйцеяблоко (etcetera:golden_eggple)
  tooltip.add("etcetera:golden_eggple", [
    Text.of("Редкий золотой плод яблоплёнка. Можно бросить как яйцо.").gray(),
    Text.of("Гарантированно (100%) ").gold().append(Text.of("вылупляет золотого яблоплёнка!").yellow())
  ]);

  // 6. Игральная кость (etcetera:dice)
  tooltip.add("etcetera:dice", [
    Text.of("ПКМ / Сигнал редстоуна: ").gold().append(Text.of("бросить кость (1–6).").gray()),
    Text.of("Компаратор считывает выпавшее значение как силу сигнала редстоуна (1–6).").yellow()
  ]);

  // 7. Барабан (etcetera:drum)
  tooltip.add("etcetera:drum", [
    Text.of("Акустический инструмент. Звучание зависит от блока снизу:").gray(),
    Text.of("• Золото: ").gold().append(Text.of("Битбокс ").gray()).append(Text.of("• Грязь: ").yellow()).append(Text.of("Дарбука ").gray()).append(Text.of("• Глина: ").aqua()).append(Text.of("Дхолак ").gray()).append(Text.of("• Дерево: ").green()).append(Text.of("Табла").gray())
  ]);

  // 8. Стойка для предметов (etcetera:item_stand, glow_item_stand)
  const itemStands = ["etcetera:item_stand", "etcetera:glow_item_stand"];
  itemStands.forEach(id => {
    tooltip.add(id, [
      Text.of("Подставка для демонстрации предметов.").gray(),
      Text.of("ПКМ с предметом: ").gold().append(Text.of("выставить предмет на витрину.").gray()),
      Text.of("ПКМ со стеклом: ").gold().append(Text.of("накрыть защитным музейным колпаком.").gray()),
      Text.of("При разрушении возвращаются и предмет, и блок стекла.").darkGray()
    ]);
  });

  // 9. Крошащийся камень (etcetera:crumbling_stone)
  tooltip.add("etcetera:crumbling_stone", [
    Text.of("Обрушается через ").gray().append(Text.of("1,25 сек").gold()).append(Text.of(" после наступания (мгновенно от стрел).").gray()),
    Text.of("ПКМ с пчелиными сотами: ").gold().append(Text.of("навсегда закрепить от обрушения.").green())
  ]);

  // 10. Вощёный крошащийся камень (etcetera:waxed_crumbling_stone)
  tooltip.add("etcetera:waxed_crumbling_stone", [
    Text.of("Обработан пчелиными сотами.").gray(),
    Text.of("Сохраняет винтажные трещины, но никогда не обрушивается.").green()
  ]);

  // 11. Молоток (etcetera:hammer)
  tooltip.add("etcetera:hammer", [
    Text.of("ПКМ по блокам: ").gold().append(Text.of("дробит камень в булыжник, булыжник в гравий, песчаник в песок, а бетон в сухой порошок.").gray())
  ]);

  // 12. Долото (etcetera:chisel)
  tooltip.add("etcetera:chisel", [
    Text.of("ПКМ по блокам: ").gold().append(Text.of("вытёсывает резные блоки из кварца, чернита, сланца, песчаника и кирпичей.").gray())
  ]);

  // 13. Лампочки (etcetera:light_bulb, tinted_light_bulb)
  tooltip.add("etcetera:light_bulb", [
    Text.of("Компактный светильник. 3 уровня яркости: ").gray().append(Text.of("5, 10 и 15 люмен").yellow()).append(Text.of("."))
  ]);

  tooltip.add("etcetera:tinted_light_bulb", [
    Text.of("Затемнённый светильник. 3 уровня яркости: ").gray().append(Text.of("3, 6 и 10 люмен").yellow()).append(Text.of("."))
  ]);
});
