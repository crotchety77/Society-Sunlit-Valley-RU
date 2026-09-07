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

  // 6. Подсказка для Отношений с жителями (society:face_note)
  tooltip.addAdvanced("society:face_note", (item, advanced, text) => {
    if (tooltip.shift) {
      text.add(Text.of(""));
      text.add(Text.literal("§d♥ Награды за максимальную дружбу (5 сердец):"));
      text.add(Text.literal("§7Некоторые жители могут подарить §eКнигу навыков§7"));
      text.add(Text.of(""));
      text.add(Text.literal("§8ℹ Подарки можно дарить раз в 4 дня "));
      text.add(Text.literal("§8(+40 очков за любимый)."));
    } else {
      text.add(Text.literal("§8[Удерживайте [§7Shift§8]]"));
    }
  });

  // 7. Подсказки для Универсальных подарков
  const universalLovedItems = [
    "society:prismatic_shard",
    "minecraft:rabbit_foot",
    "herbalbrews:oolong_tea",
    "society:sunlit_pearl",
    "vinery:jellie_wine",
    "society:gnome",
    "society:bowl_of_soul",
    "crabbersdelight:pearl_block"
  ];
  tooltip.add(universalLovedItems, Text.literal("§dУниверсальный подарок (+40 очков)"));

  const universalLikedItems = [
    "minecraft:totem_of_undying",
    "atmospheric:candied_orange_slices",
    "quark:diamond_heart",
    "society:mossberry",
    "society:mossberry_stew",
    "crabbersdelight:pearl",
    "society:furniture_box",
    "society:ancient_cookie"
  ];
  tooltip.add(universalLikedItems, Text.literal("§bУниверсальный подарок (+25 очков)"));

  const universalLikedTags = [
    "etcetera:sweaters",
    "etcetera:hats",
    "society:mineral",
    "forge:gems",
    "society:pristine_mineral"
  ];

  universalLikedTags.forEach((tag) => {
    tooltip.addAdvanced(`#${tag}`, (item, advanced, text) => {
      // Исключаем любимые (+40) предметы и предотвращаем повтор от нескольких тегов
      if (!universalLovedItems.includes(item.id)) {
        let alreadyAdded = false;
        for (let i = 0; i < text.size(); i++) {
          if (text.get(i).getString().includes("Универсальный подарок")) {
            alreadyAdded = true;
            break;
          }
        }
        if (!alreadyAdded) {
          text.add(Text.literal("§bУниверсальный подарок (+25 очков)"));
        }
      }
    });
  });

  // Тултип для Билета слайма с поддержкой [SHIFT]
  tooltip.addAdvanced("splendid_slimes:slime_ticket", (item, advanced, text) => {
    if (tooltip.shift) {
      text.add(Text.of("§7Используйте на слайме, чтобы раскрыть его любимое"));
      text.add(Text.of("§7лакомство для Анализатора и получить образец еды."));
      text.add(Text.of(""));
      text.add(Text.of("§6▪ Способ получения:"));
      text.add(Text.of("§7С шансом §e15%§7 выпадает из §fИнкубатора слизней§7 при"));
      text.add(Text.of("§7выведении, если изучена Книга навыка §a«Слаймик. Схватит. Кормить»§7."));
    } else {
      text.add(Text.of("§7Используйте на слайме, чтобы раскрыть его любимое"));
      text.add(Text.of("§7лакомство для Анализатора и получить образец еды."));
      text.add(Text.of("§8[Зажмите SHIFT для подробностей получения]"));
    }
  });

  // Тултип для Заряжающего стержня с поддержкой [SHIFT]
  tooltip.addAdvanced("society:charging_rod", (item, advanced, text) => {
    if (tooltip.shift) {
      text.add(Text.of(""));
      text.add(Text.of("§6▪ Способ получения:"));
      text.add(Text.of("§71. Создание: требуется добыть материалы в §cНижнем мире (Аду)§7."));
      text.add(Text.of("§72. Награда: выдаётся за сбор соответствующего §eУзелка§7."));
    } else {
      text.add(Text.of("§8[Зажмите SHIFT для подробностей получения]"));
    }
  });

  // Тултип для Батареи с поддержкой [SHIFT]
  tooltip.addAdvanced("society:battery", (item, advanced, text) => {
    if (tooltip.shift) {
      text.add(Text.of("§7Ценный источник накопленной энергии молний."));
      text.add(Text.of(""));
      text.add(Text.of("§6▪ Способ получения:"));
      text.add(Text.of("§7Основной источник — §fЗаряжающий стержень§7 во время грозы."));
      text.add(Text.of("§7После удара молнии стержень заряжается и через §e5 дней§7"));
      text.add(Text.of("§7производит готовую батарею."));
    } else {
      text.add(Text.of("§7Ценный источник накопленной энергии молний."));
      text.add(Text.of("§8[Зажмите SHIFT для подробностей получения]"));
    }
  });
});



