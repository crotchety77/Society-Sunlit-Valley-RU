// Priority: 10
// Скрипт KubeJS для понятных подсказок (tooltips) мода Tanuki Decor
// Разработано на основе подтверждённого технического аудита кода (MECHANICS-AUDIT.md)

ItemEvents.tooltip((tooltip) => {
  // 1. Игровой автомат (tanukidecor:slot_machine)
  tooltip.add("tanukidecor:slot_machine", [
    Text.of("Принимает монеты ").gray().append(Text.of("Numismatics").gold()).append(Text.of(".")).gray(),
    Text.of("ПКМ с монетой в руке: ").gold().append(Text.of("запустить спин.").gray()),
    Text.of("Джекпот возвращает ").gray().append(Text.of("3 поставленные монеты").green()).append(Text.of(" (4 с навыком «Красное и чёрное»).").gray()),
    Text.of("Выигрышная ставка: ").yellow().append(Text.of("шанс ").gray()).append(Text.of("5%").gold()).append(Text.of(" получить книгу «Красное и чёрное» при достигнутом мастерстве Приключений.").gray()),
    Text.of("Призматический осколок: ").aqua().append(Text.of("0,5%").gold()).append(Text.of(" при ставке Солнышком или ").gray()).append(Text.of("10%").gold()).append(Text.of(" при ставке Нептуниевой/Призматической монетой.").gray())
  ]);

  // 2. Верстак «Сделай сам» (tanukidecor:diy_workbench)
  tooltip.add("tanukidecor:diy_workbench", [
    Text.of("Универсальная мебельная станция.").gray(),
    Text.of("Использует 4 базовых ресурса: ").gray().append(Text.of("Камень").gold()).append(Text.of(", ").gray()).append(Text.of("Брёвна").gold()).append(Text.of(", ").gray()).append(Text.of("Глину").gold()).append(Text.of(" и ").gray()).append(Text.of("Железо").gold()).append(Text.of(".")).gray(),
    Text.of("Встроенный каталог мебели ").yellow().append(Text.of("содержит сотни предметов интерьера.").gray())
  ]);
});
