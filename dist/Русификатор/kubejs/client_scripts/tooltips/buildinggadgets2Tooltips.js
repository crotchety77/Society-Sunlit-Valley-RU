// Priority: 10
// Скрипт всплывающих подсказок KubeJS для мода Building Gadgets 2
// Отражает подтверждённые механики глубокого байткод-аудита и конфигов Society

ItemEvents.tooltip((tooltip) => {
  // 1. Строительный гаджет (gadget_building)
  tooltip.add("buildinggadgets2:gadget_building", [
    Text.of("Высокоскоростное строительство по площади, стенам и сеткам.").gray(),
    Text.of("ПКМ: ").gold().append(Text.of("разместить выбранные блоки.").gray()),
    Text.of("Shift + ПКМ по блоку: ").gold().append(Text.of("выбрать образец материала.").aqua()),
    Text.of("Shift + ПКМ по сундуку: ").gold().append(Text.of("привязать удалённый источник ресурсов.").green()),
    Text.of("Клавиша «G»: ").yellow().append(Text.of("радиальное меню выбора 9 режимов постройки.").gray()),
    Text.of("Shift + ПКМ по воздуху: ").gold().append(Text.of("меню настроек, якоря и смещения.").yellow()),
    Text.of("⚡ Не требует энергии (0 FE) в этой сборке.").darkGreen()
  ]);

  // 2. Гаджет замены (gadget_exchanging)
  tooltip.add("buildinggadgets2:gadget_exchanging", [
    Text.of("Мгновенная замена блоков в мире без промежуточного разрушения.").gray(),
    Text.of("ПКМ: ").gold().append(Text.of("заменить целевые блоки на выбранный материал.").gray()),
    Text.of("Shift + ПКМ по блоку: ").gold().append(Text.of("выбрать материал для замены.").aqua()),
    Text.of("Shift + ПКМ по сундуку: ").gold().append(Text.of("привязать удалённый склад.").green()),
    Text.of("Бережная замена: не сбивает факелы, проводку и декор на блоках.").aqua(),
    Text.of("⚡ Не требует энергии (0 FE) в этой сборке.").darkGreen()
  ]);

  // 3. Гаджет копирования и вставки (gadget_copy_paste)
  tooltip.add("buildinggadgets2:gadget_copy_paste", [
    Text.of("Копирует и тиражирует готовые постройки.").gray(),
    Text.of("ПКМ по углам структуры: ").gold().append(Text.of("выделить кубическую область.").aqua()),
    Text.of("ПКМ в режиме вставки: ").gold().append(Text.of("разместить постройку в мире.").green()),
    Text.of("Shift + ПКМ по воздуху: ").gold().append(Text.of("поворот, отзеркаливание и смещение.").yellow()),
    Text.of("Совместим с Менеджером шаблонов и буфером обмена (JSON).").gray()
  ]);

  // 4. Гаджет вырезания и вставки (gadget_cut_paste)
  tooltip.add("buildinggadgets2:gadget_cut_paste", [
    Text.of("Бережный перенос целых построек на новое место.").gray(),
    Text.of("1. Вырезание: ").gold().append(Text.of("выделите структуру в мире (сохраняется в памяти).").gray()),
    Text.of("2. Вставка: ").gold().append(Text.of("разместите вырезанную постройку в новой точке.").green()),
    Text.of("⚡ Не требует энергии (0 FE) в этой сборке.").darkGreen()
  ]);

  // 5. Гаджет разрушения (gadget_destruction)
  tooltip.add("buildinggadgets2:gadget_destruction", [
    Text.of("Мгновенное стирание кубических объёмов блоков (до 16×16×16).").gray(),
    Text.of("⚠️ ВНИМАНИЕ: ").red().append(Text.of("удаляемые блоки не выпадают в виде дропа!").yellow()),
    Text.of("⏪ Ошибка? ").aqua().append(Text.of("Клавиша Отмены «U» полностью восстанавливает стёртые блоки.").green()),
    Text.of("Shift + ПКМ по воздуху: ").gold().append(Text.of("настройка точных размеров зоны стирания.").gray())
  ]);

  // 6. Менеджер шаблонов (template_manager)
  tooltip.add("buildinggadgets2:template_manager", [
    Text.of("Рабочая станция с 3D-просмотром для записи и чтения чертежей.").gray(),
    Text.of("Положите обычную бумагу и нажмите «Сохранить» — она станет Шаблоном!").green(),
    Text.of("Поддерживает экспорт и импорт JSON-схем через буфер обмена.").yellow()
  ]);

  // 7. Шаблон и Редпринт (template, redprint)
  tooltip.add("buildinggadgets2:template", [
    Text.of("Бумажный носитель чертежа с записанной схемой.").gray(),
    Text.of("Создаётся в Менеджере шаблонов из обычной бумаги.").aqua()
  ]);
  tooltip.add("buildinggadgets2:redprint", [
    Text.of("Глобальный серверный чертёж с уникальным именем.").gray(),
    Text.of("Не имеет рецепта на верстаке (выдаётся сервером или квестами).").darkGray()
  ]);

  // 8. Ядро гаджета (gadget_core)
  tooltip.add("buildinggadgets2:gadget_core", [
    Text.of("Высокотехнологичный электронный компонент.").gray(),
    Text.of("Базовый ингредиент для создания строительных гаджетов.").gold()
  ]);
});
