// Priority: 0
console.info("[SOCIETY] slimeInspectorEnhanced.js loaded");

(() => {
  // 1. СПИСОК ЛЮБИМОЙ ЕДЫ ДЛЯ ВСЕХ 24 ПОРОД
  const SlimeFavoriteFoods = {
    all_seeing: { item: "minecraft:golden_carrot" },
    bitwise: { item: "society:fire_opal" },
    blazing: { item: "autumnity:cooked_turkey" },
    bony: { item: "society:large_sheep_milk" },
    boomcat: { item: "untitledduckmod:cooked_duck", entity: "untitledduckmod:duck" },
    dusty: { item: "netherdepthsupgrade:bonefish", entity: "trials:bogged" },
    ender: { item: "minecraft:amethyst_shard" },
    gold: { item: "society:bell_pepper_preserves" },
    juicy: { item: "vinery:jungle_grapes_red" },
    luminous: { item: "vintagedelight:pickle" },
    mechanic: { item: "oreganized:lead_ingot" },
    minty: { item: "society:tubasmoke_stick" },
    orby: { item: "society:dried_shimmering_mushrooms" },
    phantom: { item: "minecraft:purple_bed" },
    prisma: { item: "aquaculture:boulti" },
    puddle: { item: "unusualfishmod:raw_sneep_snorp" },
    rotting: { item: "minecraft:chicken", entity: "minecraft:chicken" },
    shulking: { item: "minecraft:chorus_flower" },
    slimy: { item: "farm_and_charm:strawberry" },
    sparkcat: { item: "society:smoked_spindlefish" },
    sweet: { item: "atmospheric:orange" },
    webby: { item: "veggiesdelight:garlic" },
    weeping: { item: "pamhc2trees:bananaitem" },
    bear: { item: "buzzier_bees:crystallized_honey_block" },
  };

  // 2. СТОИМОСТЬ ПЛОРТОВ (В МОНЕТАХ ●)
  const SlimePlortPrices = {
    slimy: 64,
    dusty: 64,
    bony: 72,
    rotting: 72,
    mechanic: 148,
    webby: 128,
    luminous: 132,
    juicy: 90,
    puddle: 224,
    boomcat: 200,
    bear: 256,
    all_seeing: 256,
    bitwise: 288,
    blazing: 256,
    weeping: 320,
    prisma: 400,
    phantom: 512,
    sweet: 256,
    shulking: 512,
    ender: 148,
    orby: 480,
    minty: 332,
    sparkcat: 1400,
    gold: 2048
  };

  function getCleanString(tag) {
    if (!tag) return "";
    let s = String(tag).replace(/["']/g, "").trim();
    if (s.indexOf(":") !== -1) {
      s = s.split(":")[1];
    }
    return s;
  }

  // 3. ОСНОВНОЙ ОБРАБОТЧИК КЛИКА АНАЛИЗАТОРОМ
  ItemEvents.entityInteracted((e) => {
    let { hand, player, item, target, server } = e;

    if (hand !== "MAIN_HAND") return;
    if (!item || item.id !== "splendid_slimes:slime_inspector") return;
    if (!target || target.type !== "splendid_slimes:splendid_slime") return;

    let nbt = target.nbt;
    if (!nbt || !nbt.Breed) return;

    let breed = getCleanString(nbt.Breed);
    let secondary = getCleanString(nbt.SecondaryBreed);
    let isLargo = secondary.length > 0;

    // ПРОВЕРКА: ИЗУЧИЛ ЛИ ИГРОК ЛАКОМСТВО ЧЕРЕЗ БИЛЕТ
    let isFavoriteKnown = (p, b) => {
      try {
        let pKey = String(p.uuid);
        if (global.knownSlimeFavorites && global.knownSlimeFavorites[pKey] && global.knownSlimeFavorites[pKey][b]) {
          return true;
        }
        if (p.persistentData && p.persistentData["known_fav_" + b]) {
          return true;
        }
        if (
          server.persistentData.knownSlimeFavorites &&
          server.persistentData.knownSlimeFavorites[pKey] &&
          server.persistentData.knownSlimeFavorites[pKey][b]
        ) {
          return true;
        }
      } catch (err) {}
      return false;
    };

    // ФОРМИРОВАНИЕ ОТКРЫТОГО ЛАКОМСТВА (ПРЕДМЕТ + МОБ)
    let getFavDisplayComponent = (b) => {
      let fav = SlimeFavoriteFoods[b];
      if (!fav) return Text.of("§7Неизвестно");

      let comp = Text.of("");
      if (fav.item) {
        comp.append(Item.of(fav.item).displayName);
      }
      if (fav.entity) {
        try {
          let entComp = global.getTranslatedEntityName(fav.entity);
          if (fav.item) {
            comp.append(" §7или моб §e").append(entComp);
          } else {
            comp.append("§7моб §e").append(entComp);
          }
        } catch (err) {
          if (fav.item) {
            comp.append(" §7или моб §e").append(fav.entity);
          }
        }
      }
      return comp;
    };

    // ВЫВОД ЛАКОМСТВА С ПРОВЕРКОЙ БИЛЕТА (ЗАМОК / ПРЕДМЕТ)
    let getFavoriteFoodDisplay = (b) => {
      if (isFavoriteKnown(player, b)) {
        return getFavDisplayComponent(b);
      }
      return Text.of("§c🔒 Требуется Билет слайма для раскрытия").hover(
        Text.of(
          "§7Примените §eБилет слайма§7 на слайме этого вида,\n§7чтобы навсегда раскрыть его любимое лакомство!"
        )
      );
    };

    // ФОРМИРОВАНИЕ ИНТЕРАКТИВНОГО ПРЕДМЕТА ПЛОРТА
    let getPlortItemComponent = (b) => {
      try {
        return Item.of("splendid_slimes:plort", { plort: { id: `splendid_slimes:${b}` } }).displayName;
      } catch (err) {
        return Text.translatable("item.splendid_slimes.plort", [Text.translatable(`slime.splendid_slimes.${b}`)]);
      }
    };

    let getPlortPrice = (b) => {
      return SlimePlortPrices[b] || 64;
    };

    // ЗВУК СКАНИРОВАНИЯ
    server.runCommandSilent(
      `playsound minecraft:block.beacon.activate player @a ${player.x} ${player.y} ${player.z} 0.5 1.5`
    );

    // ==================================================
    // 4. ВЫВОД СООБЩЕНИЯ В ЧАТ ИГРОКА
    // ==================================================
    player.tell(Text.of("§8=================================================="));
    if (isLargo) {
      player.tell(
        Text.of("  §f[ Анализ слайма ]: §aЛарго §7(")
          .append(Text.translatable(`slime.splendid_slimes.${breed}`))
          .append(" Слайм + ")
          .append(Text.translatable(`slime.splendid_slimes.${secondary}`))
          .append(" Слайм)")
      );
    } else {
      player.tell(
        Text.of("  §f[ Анализ слайма ]: §a")
          .append(Text.translatable(`slime.splendid_slimes.${breed}`))
          .append(" Слайм")
      );
    }
    player.tell(Text.of("§8--------------------------------------------------"));

    // СТРОКИ ДЛЯ ГИБРИДА ЛАРГО
    if (isLargo) {
      player.tell(
        Text.of("  §f▪ Рацион Ларго: §f")
          .append(Text.translatable(`diet.splendid_slimes.${breed}`))
          .append(" §7и §f")
          .append(Text.translatable(`diet.splendid_slimes.${secondary}`))
          .append(" §8(Подробнее в JEI)")
      );
         
      player.tell(
        Text.of("  §d▪ Любимое лакомство: §e")
          .append(getFavoriteFoodDisplay(breed))
          .append(" §7или §e")
          .append(getFavoriteFoodDisplay(secondary))
      );
      player.tell(Text.of("  §f▪ Производство плортов Ларго:"));
      player.tell(
        Text.of("    §7▪ ")
          .append(getPlortItemComponent(breed))
          .append(` §7— §e${getPlortPrice(breed)} ●`)
      );
      player.tell(
        Text.of("    §7▪ ")
          .append(getPlortItemComponent(secondary))
          .append(` §7— §e${getPlortPrice(secondary)} ●`)
      );
    } else {
      // СТРОКИ ДЛЯ ОДИНОЧНОГО СЛАЙМА
      player.tell(
        Text.of("  §f▪ Рацион питания: §f")
          .append(Text.translatable(`diet.splendid_slimes.${breed}`))
          .append(" §8(Подробнее в JEI)")
      );
      player.tell(
        Text.of("  §d▪ Любимое лакомство: §e")
          .append(getFavoriteFoodDisplay(breed))
      );
      player.tell(
        Text.of("  §f▪ Производство плорта: §f")
          .append(getPlortItemComponent(breed))
          .append(` §7— §e${getPlortPrice(breed)} ●`)
      );
    }

    // СЫТОСТЬ И НАСТРОЕНИЕ
    let hunger = nbt.Hunger != null ? Number(nbt.Hunger.toString()) : 0;
    let happiness = nbt.Happiness != null ? Number(nbt.Happiness.toString()) : 0;
    let moodText = "§aСчастливый";
    if (happiness < -50) moodText = "§cЯростный";
    else if (happiness < 0) moodText = "§6Грустный";
    else if (happiness === 0) moodText = "§eСпокойный";

    player.tell(
      Text.of(
        `  §f▪ Состояние: §7Сытость: §f${hunger > 0 ? "§aСыт" : "§cГолоден"} §7| Настроение: ${moodText}`
      )
    );

    player.tell(Text.of("§8=================================================="));
  });
})();
