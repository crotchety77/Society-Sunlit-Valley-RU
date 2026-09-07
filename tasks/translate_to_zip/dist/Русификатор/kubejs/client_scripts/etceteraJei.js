// Priority: 10
// Скрипт KubeJS для отображения рецептов Молотка и Долота в JEI/EMI (мод Etcetera)
// Источник данных: подтверждённый аудит processes/hammering.json и processes/chiselling.json

JEIAddedEvents.registerCategories((e) => {
  const guiHelper = e.data.jeiHelpers.guiHelper;

  // 1. Категория: Дробление молотком
  e.custom("etcetera:hammering", (category) => {
    category
      .title(Text.translatable("jei.etcetera.category.hammering"))
      .background(guiHelper.createBlankDrawable(177, 30))
      .icon(guiHelper.createDrawableItemStack(Item.of("etcetera:hammer")))
      .isRecipeHandled(() => true)
      .handleLookup((builder, recipe) => {
        const { input, output } = recipe.data;
        // Исходный блок
        builder
          .addSlot("input", 27, 6)
          .addItemStack(Item.of(input))
          .setBackground(guiHelper.getSlotDrawable(), -1, -1);
        // Инструмент (Молоток)
        builder
          .addSlot("catalyst", 63, 6)
          .addItemStack(Item.of("etcetera:hammer"))
          .setBackground(guiHelper.getSlotDrawable(), -1, -1);
        // Результат дробления
        builder
          .addSlot("output", 132, 6)
          .addItemStack(Item.of(output))
          .setBackground(guiHelper.getSlotDrawable(), -1, -1);
      });
  });

  // 2. Категория: Обтёсывание долотом
  e.custom("etcetera:chiselling", (category) => {
    category
      .title(Text.translatable("jei.etcetera.category.chiselling"))
      .background(guiHelper.createBlankDrawable(177, 30))
      .icon(guiHelper.createDrawableItemStack(Item.of("etcetera:chisel")))
      .isRecipeHandled(() => true)
      .handleLookup((builder, recipe) => {
        const { input, output } = recipe.data;
        // Исходный блок
        builder
          .addSlot("input", 27, 6)
          .addItemStack(Item.of(input))
          .setBackground(guiHelper.getSlotDrawable(), -1, -1);
        // Инструмент (Долото)
        builder
          .addSlot("catalyst", 63, 6)
          .addItemStack(Item.of("etcetera:chisel"))
          .setBackground(guiHelper.getSlotDrawable(), -1, -1);
        // Резной блок
        builder
          .addSlot("output", 132, 6)
          .addItemStack(Item.of(output))
          .setBackground(guiHelper.getSlotDrawable(), -1, -1);
      });
  });
});

JEIAddedEvents.registerRecipes((e) => {
  // Точные 38 рецептов дробления молотком из processes/hammering.json
  const hammeringRecipes = [
    { input: "minecraft:stone", output: "minecraft:cobblestone" },
    { input: "minecraft:stone_stairs", output: "minecraft:cobblestone_stairs" },
    { input: "minecraft:stone_slab", output: "minecraft:cobblestone_slab" },
    { input: "minecraft:infested_stone_bricks", output: "minecraft:infested_cracked_stone_bricks" },
    { input: "minecraft:stone_bricks", output: "minecraft:cracked_stone_bricks" },
    { input: "minecraft:deepslate_bricks", output: "minecraft:cracked_deepslate_bricks" },
    { input: "minecraft:deepslate_tiles", output: "minecraft:cracked_deepslate_tiles" },
    { input: "minecraft:nether_bricks", output: "minecraft:cracked_nether_bricks" },
    { input: "minecraft:polished_blackstone_bricks", output: "minecraft:cracked_polished_blackstone_bricks" },
    { input: "minecraft:smooth_stone", output: "etcetera:leveled_stone" },
    { input: "minecraft:smooth_stone_slab", output: "etcetera:leveled_stone_slab" },
    { input: "etcetera:leveled_stone", output: "etcetera:crumbling_stone" },
    { input: "minecraft:cobblestone", output: "minecraft:gravel" },
    { input: "minecraft:deepslate", output: "minecraft:cobbled_deepslate" },
    { input: "minecraft:sandstone", output: "minecraft:sand" },
    { input: "minecraft:smooth_sandstone", output: "minecraft:sand" },
    { input: "minecraft:chiseled_sandstone", output: "minecraft:sand" },
    { input: "minecraft:cut_sandstone", output: "minecraft:sand" },
    { input: "minecraft:red_sandstone", output: "minecraft:red_sand" },
    { input: "minecraft:smooth_red_sandstone", output: "minecraft:red_sand" },
    { input: "minecraft:chiseled_red_sandstone", output: "minecraft:red_sand" },
    { input: "minecraft:cut_red_sandstone", output: "minecraft:red_sand" },
    { input: "minecraft:white_concrete", output: "minecraft:white_concrete_powder" },
    { input: "minecraft:lime_concrete", output: "minecraft:lime_concrete_powder" },
    { input: "minecraft:black_concrete", output: "minecraft:black_concrete_powder" },
    { input: "minecraft:red_concrete", output: "minecraft:red_concrete_powder" },
    { input: "minecraft:yellow_concrete", output: "minecraft:yellow_concrete_powder" },
    { input: "minecraft:brown_concrete", output: "minecraft:brown_concrete_powder" },
    { input: "minecraft:magenta_concrete", output: "minecraft:magenta_concrete_powder" },
    { input: "minecraft:pink_concrete", output: "minecraft:pink_concrete_powder" },
    { input: "minecraft:blue_concrete", output: "minecraft:blue_concrete_powder" },
    { input: "minecraft:light_blue_concrete", output: "minecraft:light_blue_concrete_powder" },
    { input: "minecraft:cyan_concrete", output: "minecraft:cyan_concrete_powder" },
    { input: "minecraft:purple_concrete", output: "minecraft:purple_concrete_powder" },
    { input: "minecraft:gray_concrete", output: "minecraft:gray_concrete_powder" },
    { input: "minecraft:light_gray_concrete", output: "minecraft:light_gray_concrete_powder" },
    { input: "minecraft:orange_concrete", output: "minecraft:orange_concrete_powder" },
    { input: "minecraft:green_concrete", output: "minecraft:green_concrete_powder" }
  ];

  hammeringRecipes.forEach((r) => {
    e.custom("etcetera:hammering").add(r);
  });

  // Точные 15 рецептов обтёсывания долотом из processes/chiselling.json
  const chisellingRecipes = [
    { input: "minecraft:polished_blackstone", output: "minecraft:chiseled_polished_blackstone" },
    { input: "minecraft:sandstone", output: "minecraft:chiseled_sandstone" },
    { input: "minecraft:red_sandstone", output: "minecraft:chiseled_red_sandstone" },
    { input: "minecraft:infested_stone_bricks", output: "minecraft:infested_chiseled_stone_bricks" },
    { input: "minecraft:stone_bricks", output: "minecraft:chiseled_stone_bricks" },
    { input: "minecraft:cobbled_deepslate", output: "minecraft:chiseled_deepslate" },
    { input: "minecraft:nether_bricks", output: "minecraft:chiseled_nether_bricks" },
    { input: "minecraft:quartz_block", output: "minecraft:chiseled_quartz_block" },
    { input: "etcetera:iridescent_lantern", output: "minecraft:sea_lantern" },
    { input: "etcetera:iridescent_terracotta", output: "minecraft:light_gray_terracotta" },
    { input: "etcetera:iridescent_glazed_terracotta", output: "minecraft:light_gray_glazed_terracotta" },
    { input: "etcetera:iridescent_concrete", output: "minecraft:light_gray_concrete" },
    { input: "etcetera:iridescent_wool", output: "minecraft:light_gray_wool" },
    { input: "etcetera:iridescent_glass", output: "minecraft:glass" },
    { input: "etcetera:iridescent_glass_pane", output: "minecraft:glass_pane" }
  ];

  chisellingRecipes.forEach((r) => {
    e.custom("etcetera:chiselling").add(r);
  });
});
