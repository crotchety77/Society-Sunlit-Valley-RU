#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Создание серверного KubeJS скрипта для динамического именования слаймов в Jade
"""

import os
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
GAME_SERVER_SCRIPTS = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\server_scripts\entities"
TARGET_SCRIPT = os.path.join(GAME_SERVER_SCRIPTS, "slimeBreedName.js")

JS_CODE = """// Priority: 0
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
"""

# 1. Запись в игру
if os.path.exists(GAME_SERVER_SCRIPTS):
    with open(TARGET_SCRIPT, 'w', encoding='utf-8') as f:
        f.write(JS_CODE)
    print(f"✅ Скрипт успешно установлен в игру: {TARGET_SCRIPT}")

# 2. Также сохраняем локальную копию в репозитории
LOCAL_KUBEJS = os.path.join(ROOT_DIR, "kubejs_scripts", "server", "slimeBreedName.js")
os.makedirs(os.path.dirname(LOCAL_KUBEJS), exist_ok=True)
with open(LOCAL_KUBEJS, 'w', encoding='utf-8') as f:
    f.write(JS_CODE)
print(f"💾 Локальная копия сохранена в репозитории: {LOCAL_KUBEJS}")
