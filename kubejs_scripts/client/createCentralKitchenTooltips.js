// Priority: 10
// Скрипт всплывающих подсказок KubeJS для мода Create: Central Kitchen

ItemEvents.tooltip((tooltip) => {
  // Руководство по готовке (cooking_guide)
  tooltip.add("create_central_kitchen:cooking_guide", [
    Text.of("Модуль автоматизации кулинарии для кухонного котла.").gray(),
    Text.of("Shift + ПКМ по Горелке всполоха: ").gold().append(Text.of("превращает её в Плиту всполоха.").green()),
    Text.of("ПКМ по Плите: ").gold().append(Text.of("настройка рецепта (выбор блюда из JEI).").gray()),
    Text.of("Shift + ПКМ гаечным ключом: ").gold().append(Text.of("снять руководство и вернуть горелку.").yellow()),
    Text.of("⚙️ Позволяет Механической руке Create загружать ингредиенты и забирать готовые блюда.").aqua(),
    Text.of("🛒 Продаётся у Торговца на Рынке за монеты.").yellow()
  ]);
});
