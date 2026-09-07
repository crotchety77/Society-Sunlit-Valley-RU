// Priority: 10
// Скрипт KubeJS для детального отображения имен жителей на приглашениях, их домах и кузнечных шаблонах

ItemEvents.tooltip((tooltip) => {
  const villagerData = {
    "carpenter": { role: "Плотник", name: "Эйс", color: "#E69A58" },
    "market": { role: "Торговец с рынка", name: "Леон", color: "#55FF55" },
    "blacksmith": { role: "Кузнец", name: "Эйден", color: "#FF5555" },
    "shepherd": { role: "Пастух", name: "Мария", color: "#FFAA00" },
    "fisher": { role: "Рыбак", name: "Харуна", color: "#55FFFF" },
    "banker": { role: "Банкир", name: "Кэролайн", color: "#FFD700" },
    "librarian": { role: "Библиотекарь", name: "Вероника", color: "#FF55FF" },
    "witch": { role: "Ведьма", name: "Эвелин", color: "#C055FF" },
    "trader": { role: "Странствующий торговец", name: "Карлос", color: "#55AAFF" }
  };

  const getVillagerId = (item) => {
    if (!item.nbt) return null;
    let nbtType = item.nbt.get("type");
    if (!nbtType) return null;
    
    if (typeof nbtType === "string") {
      return nbtType.replace("society:", "");
    }
    if (nbtType.id) {
      return String(nbtType.id).replace("society:", "");
    }
    return String(nbtType).replace("society:", "").replace(/[{}"']/g, "");
  };

  // 1. Приглашения (society:invitation)
  tooltip.addAdvanced("society:invitation", (item, advanced, text) => {
    let baseId = getVillagerId(item);
    if (baseId && villagerData[baseId]) {
      let info = villagerData[baseId];
      // Заменяем стандартное название "Приглашение" на персональное
      text.set(0, Text.of(`Приглашение: ${info.role} (${info.name})`).color(info.color));
      // Добавляем красивую поясняющую плашку
      text.add(1, Text.of(`✦ Призывает жителя: ${info.name}`).gray());
    }
  });

  // 2. Блок дома жителя (society:villager_home)
  tooltip.addAdvanced("society:villager_home", (item, advanced, text) => {
    let baseId = getVillagerId(item);
    if (baseId && villagerData[baseId]) {
      let info = villagerData[baseId];
      // Заменяем стандартное название "Дом жителя" на персональное
      text.set(0, Text.of(`Дом жителя: ${info.role} (${info.name})`).color(info.color));
      text.add(1, Text.of(`✦ Принадлежит: ${info.name} (${info.role})`).gray());
    }
  });

  // 3. Шаблон электруемового улучшения
  tooltip.addAdvanced("oreganized:electrum_upgrade_smithing_template", (item, advanced, text) => {
    text.set(0, Text.literal("Кузнечный шаблон ").white()
      .append(Text.literal("электруемового").color("#FFAA00"))
      .append(Text.literal(" улучшения").white())
    );
  });

  // 4. Шаблон иридиевого улучшения
  tooltip.addAdvanced("minecraft:netherite_upgrade_smithing_template", (item, advanced, text) => {
    text.set(0, Text.literal("Кузнечный шаблон ").white()
      .append(Text.literal("иридиевого").color("#AA00AA"))
      .append(Text.literal(" улучшения").white())
    );
  });

  // 5. Подсказка для тепличного стекла
  tooltip.add([
    "moreminecarts:chiseled_organic_glass",
    "moreminecarts:chiseled_organic_glass_pane"
  ], Text.of("Выращивает первый урожай под собой в любой сезон. Радиус 16 блоков.").green());
});
