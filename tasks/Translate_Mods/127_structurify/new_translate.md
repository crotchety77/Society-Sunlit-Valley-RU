# Локализация мода: structurify

**JAR:** `structurify-forge-1.0.21+mc1.20.1.jar` | **Всего строк:** 67 | **Не переведено:** 67

## 1. Визуальный контекст и оформление
* Форматирование: Названия предметов/блоков начинаются с Заглавной буквы.
* Валюта: использовать значок монеты `§e●` (`U+25CF`).
* Тултипы: подсветка клавиш `§6Shift + ПКМ§7`.

## 2. Непереведённые строки (требуют перевода)

```json
{
  "structurify": "TODO: Structurify",
  "command.structurify.locate.exception.all_structures_are_disabled": "TODO: Can't locate any structure, all structures are disabled based on the Structurify mod config.",
  "command.structurify.locate.structure_is_disabled": "TODO: Can't locate %s structure, structure is currently disabled based on the Structurify mod config.",
  "gui.structurify.label.yes": "TODO: Yes",
  "gui.structurify.label.no": "TODO: No",
  "gui.structurify.label.enabled": "TODO: Enabled",
  "gui.structurify.label.disabled": "TODO: Disabled",
  "gui.structurify.title": "TODO: Structurify configuration",
  "gui.structurify.structures_category.title": "TODO: Structure settings",
  "gui.structurify.structures_category.description": "TODO: Disable or enable the generation of structures within the game. Additionally, manage a blacklist of biomes where specific structures should not generate.",
  "gui.structurify.structures.structures_group.title": "TODO: „%s“ structures",
  "gui.structurify.structures.structures_group.description": "TODO: List of all structures for the „%s“ namespace.",
  "gui.structurify.structures.global.title": "TODO: Global settings",
  "gui.structurify.structures.global.description": "TODO: Global settings for structures.",
  "gui.structurify.structures.disable_all_structures.title": "TODO: Disable all structures",
  "gui.structurify.structures.disable_all_structures.description": "TODO: All structures will be disabled regardless of the specific structure options.",
  "gui.structurify.structures.min_structure_distance_from_world_center.title": "TODO: Min. distance from world center (in blocks)",
  "gui.structurify.structures.min_structure_distance_from_world_center.description": "TODO: All structures will only generate if they are farther than specified distance from the world center.",
  "gui.structurify.structures.structure.title": "TODO: „%s“ settings",
  "gui.structurify.structures.structure.description": "TODO: „%s“ settings",
  "gui.structurify.structures.biomes_description": "TODO: Structure can be found in the following biomes/biome tags:",
  "gui.structurify.structures.warning": "TODO: Bear in mind that each structure may still be enabled or disabled by individual mods and datapacks.",
  "gui.structurify.structures.flatness_check_group.title": "TODO: Flatness check settings",
  "gui.structurify.structures.structure.enable_flatness_check.title": "TODO: Enable flatness check",
  "gui.structurify.structures.structure.enable_flatness_check.description": "TODO: The structure will only generate if the terrain within the specified distance is flat enough based on the specified threshold.",
  "gui.structurify.structures.structure.flatness_check_distance.title": "TODO: Flatness check distance (in blocks)",
  "gui.structurify.structures.structure.flatness_check_distance.description": "TODO: The distance in blocks from the structure’s center within which terrain flatness will be checked.",
  "gui.structurify.structures.structure.flatness_check_threshold.title": "TODO: Flatness check threshold (in blocks)",
  "gui.structurify.structures.structure.flatness_check_threshold.description": "TODO: The maximum height difference (in blocks) allowed for the terrain to be considered flat.",
  "gui.structurify.structures.structure.allow_air_blocks_in_flatness_check.title": "TODO: Allow air blocks in flatness check",
  "gui.structurify.structures.structure.allow_air_blocks_in_flatness_check.description": "TODO: Air blocks will count as solid blocks and will not fail the check.",
  "gui.structurify.structures.structure.allow_liquid_blocks_in_flatness_check.title": "TODO: Allow liquid blocks in flatness check",
  "gui.structurify.structures.structure.allow_liquid_blocks_in_flatness_check.description": "TODO: Liquid blocks will count as solid blocks and will not fail the check.",
  "gui.structurify.structures.biome_check_group.title": "TODO: Biome check settings",
  "gui.structurify.structures.structure.enable_biome_check.title": "TODO: Enable biome check",
  "gui.structurify.structures.structure.enable_biome_check.description": "TODO: The structure will only generate if all biomes within the specified distance are present in the list below.",
  "gui.structurify.structures.structure.biome_check_distance.title": "TODO: Biome check distance (in blocks)",
  "gui.structurify.structures.structure.biome_check_distance.description": "TODO: The distance in blocks from the structure’s center within which biomes will be checked.",
  "gui.structurify.structures.structure.biome_check_mode.title": "TODO: Biome check mode",
  "gui.structurify.structures.structure.biome_check_mode.description": "TODO: The mode based on what biome check checks the biomes.",
  "gui.structurify.structures.structure.biome_check_mode.strict": "TODO: Strict",
  "gui.structurify.structures.structure.biome_check_mode.blacklist": "TODO: Blacklist",
  "gui.structurify.structures.structure.biome_check_blacklisted_biomes.title": "TODO: Blacklisted Biomes/Biome tags",
  "gui.structurify.structures.structure.biome_check_blacklisted_biomes.description": "TODO: List of current blacklisted biomes/biome tags in which the „%s“ structure can not be generated when the biome check is enabled.",
  "gui.structurify.structures.structure.biomes.title": "TODO: Biomes / Biome tags",
  "gui.structurify.structures.structure.biomes.description": "TODO: List of current biomes/biome tags in which the „%s“ structure can be generated.",
  "gui.structurify.structure_sets.warning": "TODO: Bear in mind that each structure set may have unique placement rules and overrides defined by individual mods and datapacks, which means that changing this value might not always produce the intended structure spread.",
  "gui.structurify.structure_sets_category.title": "TODO: Structure Spread settings",
  "gui.structurify.structure_sets_category.description": "TODO: Configure custom structure spread either via global spacing and separation modifier or per structure specific spacing and separation values.",
  "gui.structurify.structure_sets.global_spacing_and_separation.title": "TODO: Global settings",
  "gui.structurify.structure_sets.global_spacing_and_separation.description": "TODO: Global settings for structure sets.",
  "gui.structurify.structure_sets.enable_global_spacing_and_separation_modifier.title": "TODO: Enable global spacing and separation modifier",
  "gui.structurify.structure_sets.enable_global_spacing_and_separation_modifier.description": "TODO: Spacing and separation of each structure set will be multiplied by this value.",
  "gui.structurify.structure_sets.global_spacing_and_separation_modifier.title": "TODO: Global spacing and separation modifier",
  "gui.structurify.structure_sets.global_spacing_and_separation_modifier.description": "TODO: When different from default value of 1.0, each structure set will be either more concentrated or more spread out.\n\n < 1.0 - more concentrated \n = 1.0 - unaffected \n > 1.0 - more spread out",
  "gui.structurify.structure_sets.structure_group.title": "TODO: „%s“ structures",
  "gui.structurify.structure_sets.structure_group.description": "TODO: Structure set settings for „%s“ namespace.",
  "gui.structurify.structure_sets.override_global_spacing_and_separation_modifier.title": "TODO: Override global settings",
  "gui.structurify.structure_sets.override_global_spacing_and_separation_modifier.description": "TODO: Whenever to override global spacing and separation modifier from global settings with specific settings of the „%s“ structure set.",
  "gui.structurify.structure_sets.salt.title": "TODO: Salt",
  "gui.structurify.structure_sets.salt.description": "TODO: Salt is a number that assists in randomization, each structure set should have an unique salt.",
  "gui.structurify.structure_sets.frequency.title": "TODO: Frequency",
  "gui.structurify.structure_sets.frequency.description": "TODO: Frequency represents the probability to try to generate if other conditions are met.",
  "gui.structurify.structure_sets.spacing.title": "TODO: Spacing",
  "gui.structurify.structure_sets.spacing.description": "TODO: Spacing is the average distance in chunks between structures within the same structure set (group of structures).",
  "gui.structurify.structure_sets.separation.title": "TODO: Separation",
  "gui.structurify.structure_sets.separation.description": "TODO: Separation is the minimum distance in chunks between structures within the same structure set (group of structures). The separation value cannot be greater than the spacing value."
}
```

