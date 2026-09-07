// Priority: 10
// Скрипт регистрации категории «Универсальные подарки» в JEI

JEIAddedEvents.registerCategories((e) => {
  const guiHelper = e.data.jeiHelpers.guiHelper;
  e.custom("society:universal_gifts", (category) => {
    category
      .title(Text.translatable("jei.society.category.universal_gifts"))
      .background(guiHelper.createBlankDrawable(177, 40))
      .icon(guiHelper.createDrawableItemStack(Item.of("society:face_note")))
      .isRecipeHandled(() => true)
      .setDrawHandler((recipe, recipeSlotsView, guiGraphics) => {
        const { type } = recipe.data;
        let titleText = type === "loved" 
          ? Text.literal("§dУниверсальный\n§dподарок (+40 ♥)") 
          : Text.literal("§bУниверсальный\n§bподарок (+25 ♥)");
        
        guiGraphics.drawWordWrap(Client.font, titleText, 46, 11, 128, 0);
      })
      .handleLookup((builder, recipe) => {
        const { item } = recipe.data;
        if (item.startsWith("#")) {
          builder
            .addSlot("input", 14, 11)
            .addIngredients([Ingredient.of(item)])
            .setBackground(guiHelper.getSlotDrawable(), -1, -1);
        } else {
          builder
            .addSlot("input", 14, 11)
            .addItemStack(Item.of(item))
            .setBackground(guiHelper.getSlotDrawable(), -1, -1);
        }
      });
  });
});

JEIAddedEvents.registerRecipes((e) => {
  const lovedGifts = [
    "society:prismatic_shard",
    "minecraft:rabbit_foot",
    "herbalbrews:oolong_tea",
    "society:sunlit_pearl",
    "vinery:jellie_wine",
    "society:gnome",
    "society:bowl_of_soul",
    "crabbersdelight:pearl_block"
  ];
  
  const likedGifts = [
    "minecraft:totem_of_undying",
    "atmospheric:candied_orange_slices",
    "quark:diamond_heart",
    "society:mossberry",
    "society:mossberry_stew",
    "crabbersdelight:pearl",
    "society:furniture_box",
    "society:ancient_cookie",
    "#etcetera:sweaters",
    "#etcetera:hats",
    "#society:mineral",
    "#forge:gems",
    "#society:pristine_mineral"
  ];

  lovedGifts.forEach((item) => {
    e.custom("society:universal_gifts").add({
      item: item,
      type: "loved",
      bonus: 40
    });
  });

  likedGifts.forEach((item) => {
    e.custom("society:universal_gifts").add({
      item: item,
      type: "liked",
      bonus: 25
    });
  });
});
