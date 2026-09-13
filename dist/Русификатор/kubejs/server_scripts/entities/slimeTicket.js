// Priority: 0
console.info("[SOCIETY] slimeTicket.js loaded - Обработка Билета слайма с записью знаний для Анализатора");

(() => {
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

  function getCleanBreed(tag) {
    if (!tag) return "";
    let s = String(tag).replace(/["']/g, "").trim();
    if (s.indexOf(":") !== -1) {
      s = s.split(":")[1];
    }
    return s;
  }

  function getFavSummaryComponent(fav) {
    if (!fav) return Text.of("§7Неизвестно");
    let comp = Text.of("");
    if (fav.item) {
      comp.append(Item.of(fav.item).displayName);
    }
    if (fav.entity) {
      try {
        let entName = global.getTranslatedEntityName(fav.entity);
        if (fav.item) {
          comp.append(" §7или моб §e").append(entName);
        } else {
          comp.append("§7моб §e").append(entName);
        }
      } catch (err) {
        if (fav.item) {
          comp.append(" §7или моб §e").append(fav.entity);
        }
      }
    }
    return comp;
  }

  ItemEvents.entityInteracted((e) => {
    let { hand, player, level, target, server, item } = e;
    if (hand !== "MAIN_HAND") return;
    if (!item || item.id !== "splendid_slimes:slime_ticket") return;
    if (!target || target.type !== "splendid_slimes:splendid_slime") return;
    if (!target.nbt || !target.nbt.Breed) return;

    let breedName = getCleanBreed(target.nbt.Breed);
    let fav = SlimeFavoriteFoods[breedName];
    if (!fav) return;

    server.runCommandSilent(
      `playsound chimes:block.iron.chime block @a ${player.x} ${player.y} ${player.z}`
    );
    try {
      level.spawnParticles(
        "legendarycreatures:wisp_particle",
        true,
        target.x,
        target.y + 1.5,
        target.z,
        0.2,
        0.2,
        0.2,
        5,
        0.01
      );
    } catch (err) {}

    let translatedSlimeName = Text.translatable(`slime.splendid_slimes.${breedName}`);
    let presentSender = "Билет слайма";

    // Сохраняем открытие знания для игрока по всем каналам
    try {
      let pKey = String(player.uuid);

      // 1. Быстрая память процесса
      global.knownSlimeFavorites = global.knownSlimeFavorites || {};
      global.knownSlimeFavorites[pKey] = global.knownSlimeFavorites[pKey] || {};
      global.knownSlimeFavorites[pKey][breedName] = true;

      // 2. Прямой плоский NBT игрока
      player.persistentData["known_fav_" + breedName] = true;

      // 3. Серверная персистентность мира
      if (!server.persistentData.knownSlimeFavorites) {
        server.persistentData.knownSlimeFavorites = {};
      }
      let sMap = server.persistentData.knownSlimeFavorites;
      sMap[pKey] = sMap[pKey] || {};
      sMap[pKey][breedName] = true;
      server.persistentData.knownSlimeFavorites = sMap;

      let favDisplay = getFavSummaryComponent(fav);

      player.tell(
        Text.of("§a✔ Знание о любимой еде разблокировано: ")
          .append(favDisplay)
          .append(" §7(для слайма ")
          .append(translatedSlimeName.yellow())
          .append("§7) — теперь доступно в Анализаторе!")
      );
    } catch (err) {
      console.error("[SOCIETY] Error saving slime ticket knowledge: " + err);
    }

    // Выдача подарка с предметом внутри
    if (fav.item) {
      let desc = Text.translatable("society.slime_ticket.favorite.item", [translatedSlimeName]).getString();
      player.give(
        Item.of(
          "supplementaries:present_pink",
          `{BlockEntityTag:{Description:"${desc}",ForgeCaps:{},Items:[{Count:1b,Slot:0b,id:"${fav.item}"}],Recipient:"${player.username}",Sender:"${presentSender}",id:"supplementaries:present"}}`
        )
      );
    }

    if (fav.entity) {
      let entName = fav.entity;
      try {
        entName = global.getTranslatedEntityName(fav.entity).getString();
      } catch (err) {}
      let desc = Text.translatable("society.slime_ticket.favorite.entity", [translatedSlimeName]).getString();
      player.give(
        Item.of(
          "supplementaries:present_pink",
          `{BlockEntityTag:{Description:"${desc}",ForgeCaps:{},Items:[{Count:1b,Slot:0b,id:"minecraft:paper",tag:{display:{Name:'{"text":"${entName}"}'}}}],Recipient:"${player.username}",Sender:"${presentSender}",id:"supplementaries:present"}}`
        )
      );
    }

    item.count--;
    try {
      global.addItemCooldown(player, item, 10);
    } catch (err) {}
  });
})();
