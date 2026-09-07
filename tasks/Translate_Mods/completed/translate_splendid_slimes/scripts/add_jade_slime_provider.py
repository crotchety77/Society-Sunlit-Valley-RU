#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

p = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\client_scripts\jadeClient.js"
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()

snippet = """
  // Splendid Slimes Jade Tooltip (Порода и Ларго)
  e.entity("society:slime_breed_jade", Java.loadClass("net.minecraft.world.entity.LivingEntity")).tooltip(
    (tooltip, accessor, pluginConfig) => {
      const { entity } = accessor;
      if (entity && entity.type === "splendid_slimes:splendid_slime") {
        const serverData = accessor.getServerData();
        let breed = (serverData && serverData.contains("Breed")) ? serverData.getString("Breed") : (entity.nbt && entity.nbt.Breed ? entity.nbt.Breed : null);
        if (breed) {
          if (breed.includes(":")) breed = breed.split(":")[1];
          let sec = (serverData && serverData.contains("SecondaryBreed")) ? serverData.getString("SecondaryBreed") : (entity.nbt && entity.nbt.SecondaryBreed ? entity.nbt.SecondaryBreed : null);
          if (sec && sec.length > 0) {
            if (sec.includes(":")) sec = sec.split(":")[1];
            tooltip.add(Component.of("§6Порода§r: ").append(Component.translatable(`slime.splendid_slimes.${breed}`)).append(" + ").append(Component.translatable(`slime.splendid_slimes.${sec}`)));
          } else {
            tooltip.add(Component.of("§6Порода§r: ").append(Component.translatable(`slime.splendid_slimes.${breed}`)));
          }
        }
      }
    }
  );
"""

if "society:slime_breed_jade" not in c:
    idx = c.rfind("});")
    if idx != -1:
        c = c[:idx] + snippet + c[idx:]
        with open(p, 'w', encoding='utf-8') as f:
            f.write(c)
        print("✅ Добавлен Jade-провайдер породы для слаймов в jadeClient.js")
else:
    print("ℹ️ Провайдер уже присутствует в jadeClient.js")
