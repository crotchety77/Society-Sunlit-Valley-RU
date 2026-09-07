// Priority: 0
console.info("[SOCIETY] slimeBreedName.js loaded - Dynamic Jade Slime Naming");

/**
 * Устанавливает транслируемое имя породы для слайма Splendid Slimes
 */
function updateSlimeName(entity) {
  if (!entity || entity.type !== "splendid_slimes:splendid_slime") return;
  const nbt = entity.nbt;
  if (!nbt) return;

  let breed = nbt.Breed;
  if (!breed) return;
  if (typeof breed === "string" && breed.includes(":")) {
    breed = breed.split(":")[1];
  }

  // Проверка на гибрида (Ларго)
  let secondary = nbt.SecondaryBreed;
  if (secondary && typeof secondary === "string" && secondary.length > 0) {
    if (secondary.includes(":")) {
      secondary = secondary.split(":")[1];
    }
    // Формат для Ларго
    entity.setCustomName(
      Text.of("§6Ларго§r (").append(Text.translatable(`slime.splendid_slimes.${breed}`)).append(" + ").append(Text.translatable(`slime.splendid_slimes.${secondary}`)).append(")")
    );
  } else {
    // Чистокровный слайм
    entity.setCustomName(Text.translatable(`slime.splendid_slimes.${breed}`));
  }

  // Скрываем постоянную 3D-бирку над головой, чтобы имя появлялось только в Jade
  entity.setCustomNameVisible(false);
}

// При спавне или распаковке из банки / слаймопушки
EntityEvents.spawned((e) => {
  const { entity, server } = e;
  if (entity && entity.type === "splendid_slimes:splendid_slime") {
    server.scheduleInTicks(1, () => {
      updateSlimeName(entity);
    });
  }
});

// При взаимодействии (кормление, анализатор, ПКМ)
ItemEvents.entityInteracted((e) => {
  const { target } = e;
  if (target && target.type === "splendid_slimes:splendid_slime") {
    updateSlimeName(target);
  }
});

// При получении урона или атаке
EntityEvents.hurt((e) => {
  const { entity } = e;
  if (entity && entity.type === "splendid_slimes:splendid_slime") {
    updateSlimeName(entity);
  }
});
