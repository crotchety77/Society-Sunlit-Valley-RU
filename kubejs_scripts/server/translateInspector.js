// Скрипт-инспектор для мгновенного получения данных предмета для перевода
// Команда: /trans (или /translate, /iteminfo)

console.info("[SOCIETY] translateInspector.js loaded");

ServerEvents.commandRegistry((event) => {
  const { commands: Commands } = event;

  const handleInspect = (player) => {
    const item = player.mainHandItem;

    if (!item || item.empty || item.id === "minecraft:air") {
      player.tell(Text.red("❌ Возьмите предмет в правую руку и повторите команду /trans"));
      return 1;
    }

    const itemId = item.id;
    const langKey = item.descriptionId;
    const currentName = item.name.string;
    const modId = item.mod;
    const nbt = item.nbt ? item.nbt.toString() : null;

    // Шаблон для вставки в чат с ИИ
    const copyPayload = `"${langKey}": "${currentName}"`;

    player.tell(Text.of("══════════════════════════════════════════").darkAqua());
    player.tell(Text.gold("🔍 ИНСПЕКТОР ПЕРЕВОДА ПРЕДМЕТА:"));
    
    // 1. Название предмета
    player.tell(
      Text.gray("• Текущее имя: ")
        .append(Text.white(`"${currentName}" `))
        .append(Text.yellow("[Копировать]").hover(Text.gray("Нажмите, чтобы скопировать имя")).clickCopy(currentName))
    );

    // 2. ID предмета
    player.tell(
      Text.gray("• ID: ")
        .append(Text.aqua(itemId).hover(Text.gray("Нажмите, чтобы скопировать ID")).clickCopy(itemId))
        .append(Text.darkGray(` (мод: ${modId})`))
    );

    // 3. Ключ локализации
    player.tell(
      Text.gray("• Ключ локализации: ")
        .append(Text.green(langKey).hover(Text.gray("Нажмите, чтобы скопировать ключ")).clickCopy(langKey))
    );

    // 4. Если есть NBT
    if (nbt) {
      player.tell(
        Text.gray("• NBT-теги: ")
          .append(Text.lightPurple("[Скопировать NBT]").hover(Text.gray("Нажмите, чтобы скопировать NBT")).clickCopy(nbt))
      );
    }

    // 5. Главная кнопка для ИИ
    player.tell(
      Text.of("\n👉 ")
        .append(
          Text.gold("【 📋 НАЖМИТЕ ЗДЕСЬ, ЧТОБЫ СКОПИРОВАТЬ ДЛЯ ИИ 】")
            .bold()
            .hover(Text.yellow("Скопирует готовую строку:\n" + copyPayload))
            .clickCopy(copyPayload)
        )
    );

    player.tell(Text.darkGray("Вставьте скопированную строку в чат с ИИ и напишите желаемый перевод!"));
    player.tell(Text.of("══════════════════════════════════════════").darkAqua());

    return 1;
  };

  // Регистрация команд: /trans, /translate, /iteminfo
  event.register(
    Commands.literal("trans")
      .executes((c) => handleInspect(c.source.player))
  );
  event.register(
    Commands.literal("translate")
      .executes((c) => handleInspect(c.source.player))
  );
  event.register(
    Commands.literal("iteminfo")
      .executes((c) => handleInspect(c.source.player))
  );
});

