# Локализация мода: sodium

**JAR:** `embeddium-0.3.31+mc1.20.1.jar` | **Всего строк:** 65 | **Не переведено:** 65

## 1. Визуальный контекст и оформление
* Форматирование: Названия предметов/блоков начинаются с Заглавной буквы.
* Валюта: использовать значок монеты `§e●` (`U+25CF`).
* Тултипы: подсветка клавиш `§6Shift + ПКМ§7`.

## 2. Непереведённые строки (требуют перевода)

```json
{
  "sodium.option_impact.low": "TODO: Low",
  "sodium.option_impact.medium": "TODO: Medium",
  "sodium.option_impact.high": "TODO: High",
  "sodium.option_impact.extreme": "TODO: Extreme",
  "sodium.option_impact.varies": "TODO: Varies",
  "sodium.options.pages.quality": "TODO: Quality",
  "sodium.options.pages.performance": "TODO: Performance",
  "sodium.options.pages.advanced": "TODO: Advanced",
  "sodium.options.view_distance.tooltip": "TODO: The render distance controls how far away terrain will be rendered. Shorter distances mean that less terrain will be rendered, improving frame rates.",
  "sodium.options.simulation_distance.tooltip": "TODO: The simulation distance controls how far away terrain and entities will be loaded and ticked. Shorter distances can reduce the internal server's load and may improve frame rates.",
  "sodium.options.brightness.tooltip": "TODO: Controls the brightness (gamma) of the game.",
  "sodium.options.gui_scale.tooltip": "TODO: Sets the maximum scale factor to be used for the user interface. If 'auto' is used, then the largest scale factor will always be used.",
  "sodium.options.fullscreen.tooltip": "TODO: If enabled, the game will display in full-screen (if supported).",
  "sodium.options.v_sync.tooltip": "TODO: If enabled, the game's frame rate will be synchronized to the monitor's refresh rate, making for a generally smoother experience at the expense of overall input latency. This setting might reduce performance if your system is too slow.",
  "sodium.options.fps_limit.tooltip": "TODO: Limits the maximum number of frames per second. This can help reduce battery usage and general system load when multi-tasking. If VSync is enabled, this option will be ignored unless it is lower than your display's refresh rate.",
  "sodium.options.view_bobbing.tooltip": "TODO: If enabled, the player's view will sway and bob when moving around. Players who experience motion sickness while playing can benefit from disabling this.",
  "sodium.options.attack_indicator.tooltip": "TODO: Controls where the Attack Indicator is displayed on screen.",
  "sodium.options.autosave_indicator.tooltip": "TODO: If enabled, an indicator will be shown when the game is saving the world to disk.",
  "sodium.options.graphics_quality.tooltip": "TODO: The default graphics quality controls some legacy options and is necessary for mod compatibility. If the options below are left to \"Default\", they will use this setting.",
  "sodium.options.clouds_quality.tooltip": "TODO: Controls the presence of rendered clouds in the sky.",
  "sodium.options.weather_quality.tooltip": "TODO: Controls the quality of rain and snow effects.",
  "sodium.options.leaves_quality.name": "TODO: Leaves",
  "sodium.options.leaves_quality.tooltip": "TODO: Controls the quality of leaves.",
  "sodium.options.particle_quality.tooltip": "TODO: Controls the maximum number of particles which can be present on screen at any one time.",
  "sodium.options.smooth_lighting.tooltip": "TODO: Controls whether blocks will be smoothly lit and shaded. This slightly increases the amount of time needed to re-build a chunk, but doesn't affect frame rates.",
  "sodium.options.biome_blend.value": "TODO: %s block(s)",
  "sodium.options.biome_blend.tooltip": "TODO: Controls the range which biomes will be sampled for block colorization. Higher values greatly increase the amount of time it takes to build chunks for diminishing improvements in quality.",
  "sodium.options.entity_distance.tooltip": "TODO: Controls how far away entities can render from the player. Higher values increase the render distance at the expense of frame rates.",
  "sodium.options.entity_shadows.tooltip": "TODO: If enabled, basic shadows will be rendered beneath mobs and other entities.",
  "sodium.options.vignette.name": "TODO: Vignette",
  "sodium.options.vignette.tooltip": "TODO: If enabled, a vignette effect will be rendered on the player's view. This is very unlikely to make a difference to frame rates unless you are fill-rate limited.",
  "sodium.options.mipmap_levels.tooltip": "TODO: Controls the number of mipmaps which will be used for block model textures. Higher values provide better rendering of blocks in the distance, but may adversely affect performance with many animated textures.",
  "sodium.options.use_block_face_culling.name": "TODO: Use Block Face Culling",
  "sodium.options.use_block_face_culling.tooltip": "TODO: If enabled, only the sides of blocks which are facing the camera will be submitted for rendering. This can eliminate a large number of block faces very early in the rendering process, saving memory bandwidth and time on the GPU. Some resource packs may have issues with this option, so try disabling it if you're seeing holes in blocks.",
  "sodium.options.use_compact_vertex_format.name": "TODO: Use Compact Vertex Format",
  "sodium.options.use_compact_vertex_format.tooltip": "TODO: If enabled, a more compact vertex format will be used for rendering chunks. This can reduce graphics memory usage and bandwidth requirements significantly, especially for integrated graphics cards, but can cause z-fighting with some resource packs due to how it reduces the precision of position and texture coordinate attributes. Disabling this has no effect if Oculus is installed.",
  "sodium.options.translucent_face_sorting.name": "TODO: Translucent Face Sorting",
  "sodium.options.translucent_face_sorting.tooltip": "TODO: If enabled, translucent effects from surfaces such as stained glass and water will be applied correctly.",
  "sodium.options.use_fog_occlusion.name": "TODO: Use Fog Occlusion",
  "sodium.options.use_fog_occlusion.tooltip": "TODO: If enabled, chunks which are determined to be fully hidden by fog effects will not be rendered, helping to improve performance. The improvement can be more dramatic when fog effects are heavier (such as while underwater), but it may cause undesirable visual artifacts between the sky and fog in some scenarios.",
  "sodium.options.use_entity_culling.name": "TODO: Use Entity Culling",
  "sodium.options.use_entity_culling.tooltip": "TODO: If enabled, entities determined not to be in any visible chunks will be skipped during rendering. This can help improve performance by avoiding the rendering of entities located underground or behind walls.",
  "sodium.options.animate_only_visible_textures.name": "TODO: Animate Only Visible Textures",
  "sodium.options.animate_only_visible_textures.tooltip": "TODO: If enabled, only animated textures determined to be visible will be updated. This can provide a significant boost to frame rates on some hardware, especially with heavier resource packs. If you experience issues with some textures not being animated, try disabling this option.",
  "sodium.options.cpu_render_ahead_limit.name": "TODO: CPU Render-Ahead Limit",
  "sodium.options.cpu_render_ahead_limit.tooltip": "TODO: Specifies the maximum number of frames the CPU can be waiting on the GPU to finish rendering. Very low or high values may create frame rate instability.",
  "sodium.options.cpu_render_ahead_limit.value": "TODO: %s frame(s)",
  "sodium.options.performance_impact_string": "TODO: Performance Impact: %s",
  "sodium.options.use_persistent_mapping.name": "TODO: Use Persistent Mapping",
  "sodium.options.use_persistent_mapping.tooltip": "TODO: If enabled, a small amount of memory will be persistently mapped as a staging buffer for chunk uploading, helping to reduce CPU overhead and frame time instability when loading or updating chunks.\n\nRequires OpenGL 4.4 or ARB_buffer_storage.",
  "sodium.options.chunk_update_threads.name": "TODO: Chunk Update Threads",
  "sodium.options.chunk_update_threads.tooltip": "TODO: Specifies the number of threads to use for chunk building. Using more threads can speed up chunk loading and update speed, but may negatively impact frame times.",
  "sodium.options.always_defer_chunk_updates.name": "TODO: Always Defer Chunk Updates",
  "sodium.options.always_defer_chunk_updates.tooltip": "TODO: If enabled, rendering will never wait for chunk updates to finish, even if they are important. This can greatly improve frame rates in some scenarios, but it may create significant visual lag in the world.",
  "sodium.options.use_no_error_context.name": "TODO: Use No Error Context",
  "sodium.options.use_no_error_context.tooltip": "TODO: If enabled, the OpenGL context will be created with error checking disabled. This may slightly improve performance, but it also increases the risk that the game will crash instead of gracefully handling OpenGL errors. You should disable this option if you are experiencing sudden unexplained crashes.",
  "sodium.options.buttons.undo": "TODO: Undo",
  "sodium.options.buttons.apply": "TODO: Apply",
  "sodium.options.buttons.donate": "TODO: Support Sodium!",
  "sodium.console.game_restart": "TODO: The game must be restarted to apply one or more video settings!",
  "sodium.console.broken_nvidia_driver": "TODO: Your NVIDIA graphics drivers are out of date!\n  * This will cause severe performance issues and crashes when Embeddium is installed.\n  * Please update your graphics drivers to the latest version (version 536.23 or newer.)",
  "sodium.console.pojav_launcher": "TODO: PojavLauncher is not supported when using Embeddium.\n  * You are very likely to run into extreme performance issues, graphical bugs, and crashes.\n  * You will be on your own if you decide to continue -- we will not help you with any bugs or crashes!",
  "sodium.console.core_shaders_error": "TODO: The following resource packs are incompatible with Embeddium:",
  "sodium.console.core_shaders_warn": "TODO: The following resource packs may be incompatible with Embeddium:",
  "sodium.console.core_shaders_info": "TODO: Check the game log for detailed information."
}
```

