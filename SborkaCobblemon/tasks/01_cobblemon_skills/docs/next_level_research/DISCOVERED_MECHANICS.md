# 📡 Радар обнаруженных механик, интерактивных блоков и боссов

> Автоматический срез механик сборки **Society Sunlit Cobblemon**.
> Источники: `kubejs/`, `config/ftbquests/`, `mods/*.jar`.

---

## 1. ⚡ Серверные триггеры и интерактивные предметы (KubeJS)

| Тип взаимодействия | Целевой предмет / блок | Файл скрипта | Строка | Исходный код |
| :--- | :--- | :--- | :---: | :--- |
| **Block Right-Click Interaction** | `extractinator:extractinator` | `kubejs\server_scripts\blockEvents\addExtractinatingRecipes.js` | 30 | `BlockEvents.rightClicked("extractinator:extractina` |
| **Block Right-Click Interaction** | `numismatics:blaze_banker` | `kubejs\server_scripts\blockEvents\bankerBroken.js` | 7 | `BlockEvents.rightClicked("numismatics:blaze_banker` |
| **Block Right-Click Interaction** | `create_central_kitchen:blaze_stove` | `kubejs\server_scripts\blockEvents\bankerBroken.js` | 22 | `BlockEvents.rightClicked("create_central_kitchen:b` |
| **Block Right-Click Interaction** | `furniture:blueprints` | `kubejs\server_scripts\blockEvents\blueprintsBlock.js` | 3 | `BlockEvents.rightClicked("furniture:blueprints", (` |
| **Block Right-Click Interaction** | `trofers:large_pillar` | `kubejs\server_scripts\blockEvents\cancelTrophy.js` | 3 | `BlockEvents.rightClicked("trofers:large_pillar", (` |
| **Block Right-Click Interaction** | `society:fish_pond` | `kubejs\server_scripts\blockEvents\checkFishPond.js` | 124 | `BlockEvents.rightClicked("society:fish_pond", (e) ` |
| **Block Right-Click Interaction** | `vintagedelight:salt` | `kubejs\server_scripts\blockEvents\disableSaltSnowball.js` | 3 | `BlockEvents.rightClicked("vintagedelight:salt", (e` |
| **Block Right-Click Interaction** | `minecraft:spawner` | `kubejs\server_scripts\blockEvents\disableSpawner.js` | 3 | `BlockEvents.rightClicked("minecraft:spawner", (e) ` |
| **Block Right-Click Interaction** | `vinery:apple_leaves` | `kubejs\server_scripts\blockEvents\enrichedBonemeal.js` | 87 | `BlockEvents.rightClicked("vinery:apple_leaves", (e` |
| **Block Right-Click Interaction** | `vinery:dark_cherry_leaves` | `kubejs\server_scripts\blockEvents\enrichedBonemeal.js` | 143 | `BlockEvents.rightClicked("vinery:dark_cherry_leave` |
| **Block Right-Click Interaction** | `society:fish_pond_manager` | `kubejs\server_scripts\blockEvents\fishPondQuestManagerEvents.js` | 1 | `BlockEvents.rightClicked("society:fish_pond_manage` |
| **Block Right-Click Interaction** | `vinery:grapevine_pot` | `kubejs\server_scripts\blockEvents\grapevinePot.js` | 3 | `BlockEvents.rightClicked("vinery:grapevine_pot", (` |
| **Block Right-Click Interaction** | `vinery:grapevine_stem` | `kubejs\server_scripts\blockEvents\havestHandling.js` | 157 | `BlockEvents.rightClicked("vinery:grapevine_stem", ` |
| **Block Right-Click Interaction** | `society:mana_fruit_crop` | `kubejs\server_scripts\blockEvents\havestHandling.js` | 174 | `BlockEvents.rightClicked("society:mana_fruit_crop"` |
| **Block Right-Click Interaction** | `whimsy_deco:gatcha_machine` | `kubejs\server_scripts\blockEvents\plushieMechanics.js` | 92 | `BlockEvents.rightClicked("whimsy_deco:gatcha_machi` |
| **Block Right-Click Interaction** | `farm_and_charm:mincer` | `kubejs\server_scripts\blockEvents\preventChestVoid.js` | 38 | `BlockEvents.rightClicked("farm_and_charm:mincer", ` |
| **Block Right-Click Interaction** | `society:skull_cavern_teleporter` | `kubejs\server_scripts\blockEvents\skullTeleporter.js` | 6 | `BlockEvents.rightClicked("society:skull_cavern_tel` |
| **Block Right-Click Interaction** | `splendid_slimes:slime_incubator` | `kubejs\server_scripts\blockEvents\slimeContainProtect.js` | 3 | `BlockEvents.rightClicked("splendid_slimes:slime_in` |
| **Block Right-Click Interaction** | `tanukidecor:slot_machine` | `kubejs\server_scripts\blockEvents\slotMachine.js` | 3 | `BlockEvents.rightClicked("tanukidecor:slot_machine` |
| **Block Right-Click Interaction** | `bountiful:bountyboard` | `kubejs\server_scripts\blockEvents\updateBountyBoard.js` | 3 | `BlockEvents.rightClicked("bountiful:bountyboard", ` |
| **Block Right-Click Interaction** | `society:auto_grabber` | `kubejs\server_scripts\blockEvents\upgradeSparkstoneMachines.js` | 30 | `BlockEvents.rightClicked("society:auto_grabber", (` |
| **Block Right-Click Interaction** | `minecraft:dirt` | `kubejs\server_scripts\cobblemon\cobblemonBlockInteractions.js` | 44 | `BlockEvents.rightClicked("minecraft:dirt", (e) => ` |
| **Block Right-Click Interaction** | `vinery:dirt_slab` | `kubejs\server_scripts\cobblemon\cobblemonBlockInteractions.js` | 70 | `BlockEvents.rightClicked("vinery:dirt_slab", (e) =` |
| **Block Right-Click Interaction** | `minecraft:farmland` | `kubejs\server_scripts\cobblemon\cobblemonBlockInteractions.js` | 96 | `BlockEvents.rightClicked("minecraft:farmland", (e)` |
| **Block Right-Click Interaction** | `minecraft:amethyst_block` | `kubejs\server_scripts\cobblemon\cobblemonBlockInteractions.js` | 122 | `BlockEvents.rightClicked("minecraft:amethyst_block` |
| **Block Right-Click Interaction** | `society:charging_rod` | `kubejs\server_scripts\cobblemon\cobblemonBlockInteractions.js` | 148 | `BlockEvents.rightClicked("society:charging_rod", (` |
| **Block Right-Click Interaction** | `minecraft:snow_block` | `kubejs\server_scripts\cobblemon\cobblemonBlockInteractions.js` | 172 | `BlockEvents.rightClicked("minecraft:snow_block", (` |
| **Block Right-Click Interaction** | `minecraft:ice` | `kubejs\server_scripts\cobblemon\cobblemonBlockInteractions.js` | 198 | `BlockEvents.rightClicked("minecraft:ice", (e) => {` |
| **Block Right-Click Interaction** | `minecraft:packed_ice` | `kubejs\server_scripts\cobblemon\cobblemonBlockInteractions.js` | 224 | `BlockEvents.rightClicked("minecraft:packed_ice", (` |
| **Block Right-Click Interaction** | `sunlit_cobblemon:sun_raid_statue` | `kubejs\server_scripts\cobblemon\cobblemonBlockInteractions.js` | 250 | `BlockEvents.rightClicked("sunlit_cobblemon:sun_rai` |
| **Block Right-Click Interaction** | `cobblemon:restoration_tank` | `kubejs\server_scripts\cobblemon\cobblemonBlockInteractions.js` | 283 | `BlockEvents.rightClicked("cobblemon:restoration_ta` |
| **Block Right-Click Interaction** | `sunlit_cobblemon:duo_challenge_podium` | `kubejs\server_scripts\cobblemon\cobblemonDuoChallengePodium.js` | 17 | `BlockEvents.rightClicked("sunlit_cobblemon:duo_cha` |
| **Item Right-Click Interaction** | `sunlit_cobblemon:silph_scope` | `kubejs\server_scripts\cobblemon\cobblemonEquipScope.js` | 5 | `ItemEvents.rightClicked("sunlit_cobblemon:silph_sc` |
| **Block Right-Click Interaction** | `sunlit_cobblemon:pale_chalice` | `kubejs\server_scripts\cobblemon\cobblemonFillChalice.js` | 3 | `BlockEvents.rightClicked("sunlit_cobblemon:pale_ch` |
| **Item Right-Click Interaction** | `sunlit_cobblemon:gachamon_capsule` | `kubejs\server_scripts\cobblemon\cobblemonGachaPools.js` | 440 | `ItemEvents.rightClicked("sunlit_cobblemon:gachamon` |
| **Item Right-Click Interaction** | `sunlit_cobblemon:tm_pack` | `kubejs\server_scripts\cobblemon\cobblemonLootOpening.js` | 3 | `ItemEvents.rightClicked("sunlit_cobblemon:tm_pack"` |
| **Item Right-Click Interaction** | `sunlit_cobblemon:greater_tm_pack` | `kubejs\server_scripts\cobblemon\cobblemonLootOpening.js` | 34 | `ItemEvents.rightClicked("sunlit_cobblemon:greater_` |
| **Item Right-Click Interaction** | `sunlit_cobblemon:prismatic_tm_pack` | `kubejs\server_scripts\cobblemon\cobblemonLootOpening.js` | 65 | `ItemEvents.rightClicked("sunlit_cobblemon:prismati` |
| **Item Right-Click Interaction** | `sunlit_cobblemon:berry_capsule` | `kubejs\server_scripts\cobblemon\cobblemonLootOpening.js` | 92 | `ItemEvents.rightClicked("sunlit_cobblemon:berry_ca` |
| **Item Right-Click Interaction** | `sunlit_cobblemon:pofflet_box` | `kubejs\server_scripts\cobblemon\cobblemonLootOpening.js` | 116 | `ItemEvents.rightClicked("sunlit_cobblemon:pofflet_` |
| **Item Right-Click Interaction** | `sunlit_cobblemon:mystery_gift` | `kubejs\server_scripts\cobblemon\cobblemonMysteryGift.js` | 3 | `ItemEvents.rightClicked("sunlit_cobblemon:mystery_` |
| **Item Right-Click Interaction** | `sunlit_cobblemon:poke_radar` | `kubejs\server_scripts\cobblemon\cobblemonRadar.js` | 27 | `ItemEvents.rightClicked("sunlit_cobblemon:poke_rad` |
| **Block Right-Click Interaction** | `sunlit_cobblemon:sun_raid_statue` | `kubejs\server_scripts\cobblemon\cobblemonRaid.js` | 139 | `BlockEvents.rightClicked("sunlit_cobblemon:sun_rai` |
| **Block Right-Click Interaction** | `sunlit_cobblemon:trainer_podium` | `kubejs\server_scripts\cobblemon\cobblemonTrainerPodium.js` | 85 | `BlockEvents.rightClicked("sunlit_cobblemon:trainer` |
| **Custom Death / Boss Kill Trigger** | `EntityEvents.death((e) => {` | `kubejs\server_scripts\cobblemon\cobblemonTrainerPodium.js` | 222 | `EntityEvents.death((e) => {` |
| **Cobblemon Worker Custom Recipe** | `const createCobbleWorkerRecipe = (` | `kubejs\server_scripts\cobblemon\cobbleWorkersRecipes.js` | 5 | `const createCobbleWorkerRecipe = (` |
| **Cobblemon Worker Custom Recipe** | `createCobbleWorkerRecipe(` | `kubejs\server_scripts\cobblemon\cobbleWorkersRecipes.js` | 31 | `createCobbleWorkerRecipe(` |
| **Item Right-Click Interaction** | `fightorflight:oran_lucky_egg` | `kubejs\server_scripts\cobblemon\datagen\generateCobblemonRanching.js` | 8851 | `//     ItemEvents.rightClicked('fightorflight:oran` |
| **Block Right-Click Interaction** | `sunlit_cobblemon:biodome_altar` | `kubejs\server_scripts\cobblemon\legendary\cobblemonBiodome.js` | 156 | `BlockEvents.rightClicked("sunlit_cobblemon:biodome` |
| **Item Right-Click Interaction** | `sunlit_cobblemon:wormhole_generator` | `kubejs\server_scripts\cobblemon\legendary\cobblemonCreateUBWormhole.js` | 48 | `ItemEvents.rightClicked('sunlit_cobblemon:wormhole` |
| **Block Right-Click Interaction** | `sunlit_cobblemon:gem_box` | `kubejs\server_scripts\cobblemon\legendary\cobblemonGemBox.js` | 80 | `BlockEvents.rightClicked("sunlit_cobblemon:gem_box` |
| **Item Right-Click Interaction** | `sunlit_cobblemon:gracidea_flower` | `kubejs\server_scripts\cobblemon\legendary\cobblemonGracidea.js` | 73 | `ItemEvents.rightClicked('sunlit_cobblemon:gracidea` |
| **Block Right-Click Interaction** | `sunlit_cobblemon:mural_stone_5` | `kubejs\server_scripts\cobblemon\legendary\cobblemonMew.js` | 2 | `// BlockEvents.rightClicked("sunlit_cobblemon:mura` |
| **Block Right-Click Interaction** | `society:moon_statue` | `kubejs\server_scripts\cobblemon\legendary\cobblemonMoonRitual.js` | 29 | `BlockEvents.rightClicked("society:moon_statue", (e` |
| **Block Right-Click Interaction** | `sunlit_cobblemon:ominous_black_stake` | `kubejs\server_scripts\cobblemon\legendary\cobblemonStake.js` | 8 | `BlockEvents.rightClicked("sunlit_cobblemon:ominous` |
| **Block Right-Click Interaction** | `society:charging_rod` | `kubejs\server_scripts\cobblemon\legendary\cobblemonTaoTrio.js` | 1 | `BlockEvents.rightClicked("society:charging_rod", (` |
| **Block Right-Click Interaction** | `decorative_blocks:brazier` | `kubejs\server_scripts\cobblemon\legendary\cobblemonTaoTrio.js` | 19 | `BlockEvents.rightClicked("decorative_blocks:brazie` |
| **Item Right-Click Interaction** | `unimplemented_items:potion` | `kubejs\server_scripts\cobblemon\wikigen\cobblemonWikiScripts.js` | 26 | `// ItemEvents.rightClicked("unimplemented_items:po` |
| **Item Right-Click Interaction** | `unimplemented_items:hyper_potion` | `kubejs\server_scripts\cobblemon\wikigen\cobblemonWikiScripts.js` | 122 | `// ItemEvents.rightClicked("unimplemented_items:hy` |
| **Item Right-Click Interaction** | `unimplemented_items:potion_max` | `kubejs\server_scripts\cobblemon\wikigen\cobblemonWikiScripts.js` | 165 | `// ItemEvents.rightClicked("unimplemented_items:po` |
| **Item Right-Click Interaction** | `rehooked:wood_chain` | `kubejs\server_scripts\datagen\wikigen\generateShopTable.js` | 88 | `// ItemEvents.rightClicked('rehooked:wood_chain', ` |
| **Entity Interaction with Item** | `society:car_key` | `kubejs\server_scripts\entities\carKey.js` | 32 | `ItemEvents.entityInteracted("society:car_key", (e)` |
| **Custom Death / Boss Kill Trigger** | `EntityEvents.death((e) => {` | `kubejs\server_scripts\entities\handleSacrifice.js` | 1 | `EntityEvents.death((e) => {` |
| **Custom Death / Boss Kill Trigger** | `EntityEvents.death((e) => {` | `kubejs\server_scripts\entities\spawnBoomcat.js` | 3 | `EntityEvents.death((e) => {` |
| **Item Right-Click Interaction** | `brewery:dark_brew` | `kubejs\server_scripts\itemEvents\cancelItemEvents.js` | 3 | `ItemEvents.rightClicked("brewery:dark_brew", (e) =` |
| **Item Right-Click Interaction** | `farm_and_charm:fertilizer` | `kubejs\server_scripts\itemEvents\cancelItemEvents.js` | 7 | `ItemEvents.rightClicked("farm_and_charm:fertilizer` |
| **Block Right-Click Interaction** | `create:deployer` | `kubejs\server_scripts\itemEvents\cancelItemEvents.js` | 12 | `BlockEvents.rightClicked("create:deployer", (e) =>` |
| **Item Right-Click Interaction** | `society:cornucopia` | `kubejs\server_scripts\itemEvents\cornucopia.js` | 4 | `ItemEvents.rightClicked("society:cornucopia", (e) ` |
| **Item Right-Click Interaction** | `society:yard_work_yearly` | `kubejs\server_scripts\itemEvents\experienceBooks.js` | 11 | `ItemEvents.rightClicked("society:yard_work_yearly"` |
| **Item Right-Click Interaction** | `society:husbandry_hourly` | `kubejs\server_scripts\itemEvents\experienceBooks.js` | 15 | `ItemEvents.rightClicked("society:husbandry_hourly"` |
| **Item Right-Click Interaction** | `society:mining_monthly` | `kubejs\server_scripts\itemEvents\experienceBooks.js` | 19 | `ItemEvents.rightClicked("society:mining_monthly", ` |
| **Item Right-Click Interaction** | `society:combat_quarterly` | `kubejs\server_scripts\itemEvents\experienceBooks.js` | 24 | `ItemEvents.rightClicked("society:combat_quarterly"` |
| **Item Right-Click Interaction** | `society:wet_weekly` | `kubejs\server_scripts\itemEvents\experienceBooks.js` | 29 | `ItemEvents.rightClicked("society:wet_weekly", (e) ` |
| **Item Right-Click Interaction** | `society:book_of_stars` | `kubejs\server_scripts\itemEvents\experienceBooks.js` | 34 | `ItemEvents.rightClicked("society:book_of_stars", (` |
| **Item Right-Click Interaction** | `minecraft:ender_eye` | `kubejs\server_scripts\itemEvents\eyeOfEnderMessage.js` | 14 | `ItemEvents.rightClicked("minecraft:ender_eye", (e)` |
| **Item Right-Click Interaction** | `society:fish_radar` | `kubejs\server_scripts\itemEvents\fishRadar.js` | 5 | `ItemEvents.rightClicked("society:fish_radar", (e) ` |
| **Item Right-Click Interaction** | `society:geode_buster` | `kubejs\server_scripts\itemEvents\geodeCracking.js` | 3 | `ItemEvents.rightClicked("society:geode_buster", e ` |
| **Item Right-Click Interaction** | `society:furniture_box` | `kubejs\server_scripts\itemEvents\lootOpening.js` | 3 | `ItemEvents.rightClicked("society:furniture_box", (` |
| **Item Right-Click Interaction** | `society:bouquet_bag` | `kubejs\server_scripts\itemEvents\lootOpening.js` | 71 | `ItemEvents.rightClicked("society:bouquet_bag", (e)` |
| **Item Right-Click Interaction** | `society:scavenged_food_bag` | `kubejs\server_scripts\itemEvents\lootOpening.js` | 95 | `ItemEvents.rightClicked("society:scavenged_food_ba` |
| **Item Right-Click Interaction** | `society:magic_rope` | `kubejs\server_scripts\itemEvents\magicRope.js` | 52 | `ItemEvents.rightClicked("society:magic_rope", (e) ` |
| **Item Right-Click Interaction** | `society:overflow_token` | `kubejs\server_scripts\itemEvents\overflowToken.js` | 3 | `ItemEvents.rightClicked("society:overflow_token", ` |
| **Item Right-Click Interaction** | `pamhc2trees:pawpawitem` | `kubejs\server_scripts\itemEvents\pawpawRoad.js` | 14 | `ItemEvents.rightClicked("pamhc2trees:pawpawitem", ` |
| **Item Right-Click Interaction** | `society:pig_race_ticket` | `kubejs\server_scripts\itemEvents\pigRacing.js` | 456 | `ItemEvents.rightClicked("society:pig_race_ticket",` |
| **Item Right-Click Interaction** | `society:multiplayer_pig_race_ticket` | `kubejs\server_scripts\itemEvents\pigRacing.js` | 475 | `ItemEvents.rightClicked("society:multiplayer_pig_r` |
| **Item Right-Click Interaction** | `society:plushie_capsule` | `kubejs\server_scripts\itemEvents\plushieCapsule.js` | 3 | `ItemEvents.rightClicked("society:plushie_capsule",` |
| **Entity Interaction with Item** | `etcetera:wrench` | `kubejs\server_scripts\itemEvents\plushieDebug.js` | 3 | `ItemEvents.entityInteracted('etcetera:wrench', (e)` |
| **Item Right-Click Interaction** | `society:crystal_of_regret_farming` | `kubejs\server_scripts\itemEvents\regretCrystals.js` | 18 | `ItemEvents.rightClicked("society:crystal_of_regret` |
| **Item Right-Click Interaction** | `society:crystal_of_regret_husbandry` | `kubejs\server_scripts\itemEvents\regretCrystals.js` | 28 | `ItemEvents.rightClicked("society:crystal_of_regret` |
| **Item Right-Click Interaction** | `society:crystal_of_regret_mining` | `kubejs\server_scripts\itemEvents\regretCrystals.js` | 38 | `ItemEvents.rightClicked("society:crystal_of_regret` |
| **Item Right-Click Interaction** | `society:crystal_of_regret_fishing` | `kubejs\server_scripts\itemEvents\regretCrystals.js` | 48 | `ItemEvents.rightClicked("society:crystal_of_regret` |
| **Item Right-Click Interaction** | `society:crystal_of_regret_adventuring` | `kubejs\server_scripts\itemEvents\regretCrystals.js` | 58 | `ItemEvents.rightClicked("society:crystal_of_regret` |
| **Item Right-Click Interaction** | `society:tubasmoke_stick` | `kubejs\server_scripts\itemEvents\smokeTubasmokeStick.js` | 6 | `ItemEvents.rightClicked("society:tubasmoke_stick",` |
| **Item Right-Click Interaction** | `society:treasure_totem` | `kubejs\server_scripts\itemEvents\totems.js` | 48 | `ItemEvents.rightClicked("society:treasure_totem", ` |
| **Item Right-Click Interaction** | `society:bubble_totem` | `kubejs\server_scripts\itemEvents\totems.js` | 52 | `ItemEvents.rightClicked("society:bubble_totem", (e` |
| **Item Right-Click Interaction** | `society:dry_totem` | `kubejs\server_scripts\itemEvents\totems.js` | 73 | `ItemEvents.rightClicked("society:dry_totem", (e) =` |
| **Item Right-Click Interaction** | `society:rain_totem` | `kubejs\server_scripts\itemEvents\totems.js` | 77 | `ItemEvents.rightClicked("society:rain_totem", (e) ` |
| **Item Right-Click Interaction** | `society:thunder_totem` | `kubejs\server_scripts\itemEvents\totems.js` | 81 | `ItemEvents.rightClicked("society:thunder_totem", (` |
| **Item Right-Click Interaction** | `functionalstorage:creative_vending_upgrade` | `kubejs\server_scripts\itemEvents\validateFishPondQuests.js` | 19 | `ItemEvents.rightClicked("functionalstorage:creativ` |
| **Block Right-Click Interaction** | `mysticaloaktree:wise_oak` | `kubejs\server_scripts\npcs\npcInteraction.js` | 220 | `BlockEvents.rightClicked("mysticaloaktree:wise_oak` |
| **Item Right-Click Interaction** | `society:invitation` | `kubejs\server_scripts\npcs\npcInvite.js` | 3 | `ItemEvents.rightClicked("society:invitation", (e) ` |
| **Cobblemon Event Hook** | `$CobblemonEvents.BATTLE_VICTORY.subscribe("normal", (e) => {` | `kubejs\startup_scripts\cobblemon\cobblemonHandleDeath.js` | 105 | `$CobblemonEvents.BATTLE_VICTORY.subscribe("normal"` |
| **Cobblemon Event Hook** | `$CobblemonEvents.BATTLE_STARTED_POST.subscribe("normal", (e)` | `kubejs\startup_scripts\cobblemon\cobblemonRaidPokemon.js` | 24 | `$CobblemonEvents.BATTLE_STARTED_POST.subscribe("no` |
| **Cobblemon Event Hook** | `$CobblemonEvents.BATTLE_FAINTED.subscribe("normal", (e) => {` | `kubejs\startup_scripts\cobblemon\cobblemonRaidPokemon.js` | 104 | `$CobblemonEvents.BATTLE_FAINTED.subscribe("normal"` |
| **Cobblemon Event Hook** | `$CobblemonEvents.STARTER_CHOSEN.subscribe("normal", (e) => {` | `kubejs\startup_scripts\cobblemon\cobblemonStarterScope.js` | 10 | `$CobblemonEvents.STARTER_CHOSEN.subscribe("normal"` |

---

## 2. 🏆 Квестовые механики, боссы и артефакты (FTB Quests)

| Глава квестов | Предмет / Артефакт | Файл квеста |
| :--- | :--- | :--- |
| **Chapter: {ftbquests.chapter.artifacts.quest2255D3F05F8B895A.task.3516062960629316800.title}** | `society:ember_crystal_cluster` | `config\ftbquests\quests\chapters\artifacts.snbt` |
| **Chapter: {ftbquests.chapter.artifacts.quest2255D3F05F8B895A.task.3516062960629316800.title}** | `society:token_of_unity` | `config\ftbquests\quests\chapters\artifacts.snbt` |
| **Chapter: {ftbquests.chapter.banners.quest1FFF66E7B3DE1E6D.task.6970538343027311856.title}** | `bakery:braided_bread` | `config\ftbquests\quests\chapters\banners.snbt` |
| **Chapter: {ftbquests.chapter.banners.quest1FFF66E7B3DE1E6D.task.6970538343027311856.title}** | `candlelight:fresh_garden_salad` | `config\ftbquests\quests\chapters\banners.snbt` |
| **Chapter: {ftbquests.chapter.banners.quest1FFF66E7B3DE1E6D.task.6970538343027311856.title}** | `minecraft:cake` | `config\ftbquests\quests\chapters\banners.snbt` |
| **Chapter: {ftbquests.chapter.beginner.quest201D4A576453FB99.task.5870353506331740988.title}** | `society:treasure_totem` | `config\ftbquests\quests\chapters\beginner.snbt` |
| **Chapter: {ftbquests.chapter.boiler_room.quest3428ADDC87A77916.subtitle}** | `minecraft:raw_iron_block` | `config\ftbquests\quests\chapters\boiler_room.snbt` |
| **Chapter: {ftbquests.chapter.boiler_room.quest3428ADDC87A77916.subtitle}** | `minecraft:raw_gold_block` | `config\ftbquests\quests\chapters\boiler_room.snbt` |
| **Chapter: {ftbquests.chapter.boiler_room.quest3428ADDC87A77916.subtitle}** | `society:earth_crystal` | `config\ftbquests\quests\chapters\boiler_room.snbt` |
| **Chapter: {ftbquests.chapter.boiler_room.quest3428ADDC87A77916.subtitle}** | `minecraft:raw_copper_block` | `config\ftbquests\quests\chapters\boiler_room.snbt` |
| **Chapter: {ftbquests.chapter.botania.quest5E5E6E09E6C6DF02.title}** | `botania:runic_altar` | `config\ftbquests\quests\chapters\botania.snbt` |
| **Chapter: {ftbquests.chapter.botania.quest5E5E6E09E6C6DF02.title}** | `botania:mana_pylon` | `config\ftbquests\quests\chapters\botania.snbt` |
| **Chapter: {ftbquests.chapter.botania.quest5E5E6E09E6C6DF02.title}** | `minecraft:stone` | `config\ftbquests\quests\chapters\botania.snbt` |
| **Chapter: {ftbquests.chapter.botania.quest5E5E6E09E6C6DF02.title}** | `botania:gaia_pylon` | `config\ftbquests\quests\chapters\botania.snbt` |
| **Chapter: {ftbquests.chapter.crafts_room.quest403045A4DA7A770.task.8796865779311042502.title}** | `society:crystalberry` | `config\ftbquests\quests\chapters\crafts_room.snbt` |
| **Chapter: {ftbquests.chapter.creatures.quest5045DE566B4AC009.task.3224597358468663487.title}** | `minecraft:coal` | `config\ftbquests\quests\chapters\creatures.snbt` |
| **Chapter: {ftbquests.chapter.creatures.quest5045DE566B4AC009.task.3224597358468663487.title}** | `minecraft:emerald` | `config\ftbquests\quests\chapters\creatures.snbt` |
| **Chapter: {ftbquests.chapter.creatures.quest5045DE566B4AC009.task.3224597358468663487.title}** | `minecraft:hay_block` | `config\ftbquests\quests\chapters\creatures.snbt` |
| **Chapter: {ftbquests.chapter.creatures.quest5045DE566B4AC009.task.3224597358468663487.title}** | `minecraft:heart_of_the_sea` | `config\ftbquests\quests\chapters\creatures.snbt` |
| **Chapter: {ftbquests.chapter.crops.quest262E7E71CF6AD26A.subtitle}** | `minecraft:pitcher_plant` | `config\ftbquests\quests\chapters\crops.snbt` |
| **Chapter: {ftbquests.chapter.crops.quest262E7E71CF6AD26A.subtitle}** | `minecraft:torchflower` | `config\ftbquests\quests\chapters\crops.snbt` |
| **Chapter: {ftbquests.chapter.crops.quest262E7E71CF6AD26A.subtitle}** | `minecraft:melon_slice` | `config\ftbquests\quests\chapters\crops.snbt` |
| **Chapter: {ftbquests.chapter.crops.quest262E7E71CF6AD26A.subtitle}** | `minecraft:potato` | `config\ftbquests\quests\chapters\crops.snbt` |
| **Chapter: {ftbquests.chapter.crops.quest262E7E71CF6AD26A.subtitle}** | `minecraft:beetroot` | `config\ftbquests\quests\chapters\crops.snbt` |
| **Chapter: {ftbquests.chapter.crops.quest262E7E71CF6AD26A.subtitle}** | `minecraft:carrot` | `config\ftbquests\quests\chapters\crops.snbt` |
| **Chapter: {ftbquests.chapter.crops.quest262E7E71CF6AD26A.subtitle}** | `minecraft:pumpkin` | `config\ftbquests\quests\chapters\crops.snbt` |
| **Chapter: {ftbquests.chapter.crops.quest262E7E71CF6AD26A.subtitle}** | `society:crystalberry` | `config\ftbquests\quests\chapters\crops.snbt` |
| **Chapter: {ftbquests.chapter.crops.quest262E7E71CF6AD26A.subtitle}** | `minecraft:red_mushroom` | `config\ftbquests\quests\chapters\crops.snbt` |
| **Chapter: {ftbquests.chapter.crops.quest262E7E71CF6AD26A.subtitle}** | `minecraft:brown_mushroom` | `config\ftbquests\quests\chapters\crops.snbt` |
| **Chapter: {ftbquests.chapter.crops.quest262E7E71CF6AD26A.subtitle}** | `minecraft:nether_wart` | `config\ftbquests\quests\chapters\crops.snbt` |
| **Chapter: {ftbquests.chapter.crops.quest262E7E71CF6AD26A.subtitle}** | `moreminecarts:glass_cactus` | `config\ftbquests\quests\chapters\crops.snbt` |
| **Chapter: {ftbquests.chapter.crops.quest262E7E71CF6AD26A.subtitle}** | `minecraft:wheat` | `config\ftbquests\quests\chapters\crops.snbt` |
| **Chapter: {ftbquests.chapter.crops.quest262E7E71CF6AD26A.subtitle}** | `minecraft:cocoa_beans` | `config\ftbquests\quests\chapters\crops.snbt` |
| **Chapter: {ftbquests.chapter.crops.quest262E7E71CF6AD26A.subtitle}** | `minecraft:apple` | `config\ftbquests\quests\chapters\crops.snbt` |
| **Chapter: {ftbquests.chapter.crops.quest262E7E71CF6AD26A.subtitle}** | `minecraft:cactus` | `config\ftbquests\quests\chapters\crops.snbt` |
| **Chapter: {ftbquests.chapter.crops.quest262E7E71CF6AD26A.subtitle}** | `minecraft:chorus_fruit` | `config\ftbquests\quests\chapters\crops.snbt` |
| **Chapter: {ftbquests.chapter.crops.quest262E7E71CF6AD26A.subtitle}** | `betterarcheology:growth_totem` | `config\ftbquests\quests\chapters\crops.snbt` |
| **Chapter: {ftbquests.chapter.crops.quest262E7E71CF6AD26A.subtitle}** | `minecraft:sweet_berries` | `config\ftbquests\quests\chapters\crops.snbt` |
| **Chapter: {ftbquests.chapter.crops.quest262E7E71CF6AD26A.subtitle}** | `minecraft:sugar_cane` | `config\ftbquests\quests\chapters\crops.snbt` |
| **Chapter: {ftbquests.chapter.crops.quest262E7E71CF6AD26A.subtitle}** | `minecraft:glow_berries` | `config\ftbquests\quests\chapters\crops.snbt` |
| **Chapter: {ftbquests.chapter.fishing.questC17CF9D782787BE.task.1440697492781150857.title}** | `minecraft:salmon` | `config\ftbquests\quests\chapters\fishing.snbt` |
| **Chapter: {ftbquests.chapter.fishing.questC17CF9D782787BE.task.1440697492781150857.title}** | `minecraft:pufferfish` | `config\ftbquests\quests\chapters\fishing.snbt` |
| **Chapter: {ftbquests.chapter.fishing.questC17CF9D782787BE.task.1440697492781150857.title}** | `minecraft:cod` | `config\ftbquests\quests\chapters\fishing.snbt` |
| **Chapter: {ftbquests.chapter.fishing.questC17CF9D782787BE.task.1440697492781150857.title}** | `minecraft:tropical_fish` | `config\ftbquests\quests\chapters\fishing.snbt` |
| **Chapter: {ftbquests.chapter.gems.quest21B62899C63D3C4B.task.6717948577994736044.title}** | `minecraft:amethyst_shard` | `config\ftbquests\quests\chapters\gems.snbt` |
| **Chapter: {ftbquests.chapter.gems.quest21B62899C63D3C4B.task.6717948577994736044.title}** | `minecraft:prismarine_crystals` | `config\ftbquests\quests\chapters\gems.snbt` |
| **Chapter: {ftbquests.chapter.gems.quest21B62899C63D3C4B.task.6717948577994736044.title}** | `minecraft:diamond` | `config\ftbquests\quests\chapters\gems.snbt` |
| **Chapter: {ftbquests.chapter.gems.quest21B62899C63D3C4B.task.6717948577994736044.title}** | `minecraft:quartz` | `config\ftbquests\quests\chapters\gems.snbt` |
| **Chapter: {ftbquests.chapter.gems.quest21B62899C63D3C4B.task.6717948577994736044.title}** | `minecraft:emerald` | `config\ftbquests\quests\chapters\gems.snbt` |
| **Chapter: {ftbquests.chapter.getting_started.quest3862A7D1A471A215.title}** | `minecraft:smithing_table` | `config\ftbquests\quests\chapters\getting_started.snbt` |
| **Chapter: {ftbquests.chapter.getting_started.quest3862A7D1A471A215.title}** | `minecraft:dirt` | `config\ftbquests\quests\chapters\getting_started.snbt` |
| **Chapter: {ftbquests.chapter.getting_started.quest3862A7D1A471A215.title}** | `minecraft:cobblestone` | `config\ftbquests\quests\chapters\getting_started.snbt` |
| **Chapter: {ftbquests.chapter.getting_started.quest3862A7D1A471A215.title}** | `minecraft:crafting_table` | `config\ftbquests\quests\chapters\getting_started.snbt` |
| **Chapter: {ftbquests.chapter.hunting_legends.quest399D1B26D9C41182.title}** | `cobblemon_farmers:worker_permit` | `config\ftbquests\quests\chapters\hunting_legends.snbt` |
| **Chapter: {ftbquests.chapter.hunting_legends.quest399D1B26D9C41182.title}** | `sunlit_cobblemon:moongeist_crystal` | `config\ftbquests\quests\chapters\hunting_legends.snbt` |
| **Chapter: {ftbquests.chapter.hunting_legends.quest399D1B26D9C41182.title}** | `sunlit_cobblemon:gem_box` | `config\ftbquests\quests\chapters\hunting_legends.snbt` |
| **Chapter: {ftbquests.chapter.hunting_legends.quest399D1B26D9C41182.title}** | `sunlit_cobblemon:swampy_mystica_branch` | `config\ftbquests\quests\chapters\hunting_legends.snbt` |
| **Chapter: {ftbquests.chapter.hunting_legends.quest399D1B26D9C41182.title}** | `sunlit_cobblemon:biodome_altar` | `config\ftbquests\quests\chapters\hunting_legends.snbt` |
| **Chapter: {ftbquests.chapter.ic__cobblemon.quest68588C07B2EFCA55.task.7192841727701503607.title}** | `cobblemon_farmers:worker_permit` | `config\ftbquests\quests\chapters\ic__cobblemon.snbt` |
| **Chapter: {ftbquests.chapter.ic__cobblemon.quest68588C07B2EFCA55.task.7192841727701503607.title}** | `cobblemon_farmers:energy_pylon` | `config\ftbquests\quests\chapters\ic__cobblemon.snbt` |
| **Chapter: {ftbquests.chapter.ic__cobblemon.quest68588C07B2EFCA55.task.7192841727701503607.title}** | `cobblemon_farmers:crystal_ball` | `config\ftbquests\quests\chapters\ic__cobblemon.snbt` |
| **Chapter: {ftbquests.chapter.ic__cobblemon.quest68588C07B2EFCA55.task.7192841727701503607.title}** | `cobblemon_farmers:mystery_mine` | `config\ftbquests\quests\chapters\ic__cobblemon.snbt` |
| **Chapter: {ftbquests.chapter.ic__cobblemon.quest68588C07B2EFCA55.task.7192841727701503607.title}** | `sunlit_cobblemon:sun_raid_statue` | `config\ftbquests\quests\chapters\ic__cobblemon.snbt` |
| **Chapter: {ftbquests.chapter.ic__cobblemon.quest68588C07B2EFCA55.task.7192841727701503607.title}** | `cobblemon_farmers:gardening_station` | `config\ftbquests\quests\chapters\ic__cobblemon.snbt` |
| **Chapter: {ftbquests.chapter.ic__cobblemon.quest68588C07B2EFCA55.task.7192841727701503607.title}** | `sunlit_cobblemon:sunlit_league_medallion` | `config\ftbquests\quests\chapters\ic__cobblemon.snbt` |
| **Chapter: {ftbquests.chapter.ic__cobblemon.quest68588C07B2EFCA55.task.7192841727701503607.title}** | `sunlit_cobblemon:mystica_branch` | `config\ftbquests\quests\chapters\ic__cobblemon.snbt` |
| **Chapter: {ftbquests.chapter.ic__cobblemon.quest68588C07B2EFCA55.task.7192841727701503607.title}** | `cobblemon_farmers:ranching_station` | `config\ftbquests\quests\chapters\ic__cobblemon.snbt` |
| **Chapter: {ftbquests.chapter.iii__advanced_farming.quest66E1AC55824DF1D9.subtitle}** | `minecraft:blaze_rod` | `config\ftbquests\quests\chapters\iii__advanced_farming.snbt` |
| **Chapter: {ftbquests.chapter.iii__advanced_farming.quest66E1AC55824DF1D9.subtitle}** | `splendid_slimes:slime_incubator` | `config\ftbquests\quests\chapters\iii__advanced_farming.snbt` |
| **Chapter: {ftbquests.chapter.iii__advanced_farming.quest66E1AC55824DF1D9.subtitle}** | `moreminecarts:chiseled_organic_glass` | `config\ftbquests\quests\chapters\iii__advanced_farming.snbt` |
| **Chapter: {ftbquests.chapter.iii__advanced_farming.quest66E1AC55824DF1D9.subtitle}** | `minecraft:slime_block` | `config\ftbquests\quests\chapters\iii__advanced_farming.snbt` |
| **Chapter: {ftbquests.chapter.ii__building_up_the_farm.quest6ADD884F3FFE5D42.subtitle}** | `society:pristine_earth_crystal` | `config\ftbquests\quests\chapters\ii__building_up_the_farm.snbt` |
| **Chapter: {ftbquests.chapter.ii__building_up_the_farm.quest6ADD884F3FFE5D42.subtitle}** | `minecraft:bone_meal` | `config\ftbquests\quests\chapters\ii__building_up_the_farm.snbt` |
| **Chapter: {ftbquests.chapter.ii__building_up_the_farm.quest6ADD884F3FFE5D42.subtitle}** | `minecraft:name_tag` | `config\ftbquests\quests\chapters\ii__building_up_the_farm.snbt` |
| **Chapter: {ftbquests.chapter.ii__building_up_the_farm.quest6ADD884F3FFE5D42.subtitle}** | `minecraft:poisonous_potato` | `config\ftbquests\quests\chapters\ii__building_up_the_farm.snbt` |
| **Chapter: {ftbquests.chapter.ii__building_up_the_farm.quest6ADD884F3FFE5D42.subtitle}** | `society:earth_crystal` | `config\ftbquests\quests\chapters\ii__building_up_the_farm.snbt` |
| **Chapter: {ftbquests.chapter.ivi__mechanical_farming.quest345432E72BD82727.title}** | `minecraft:netherite_scrap` | `config\ftbquests\quests\chapters\ivi__mechanical_farming.snbt` |
| **Chapter: {ftbquests.chapter.ivi__mechanical_farming.quest345432E72BD82727.title}** | `minecraft:andesite` | `config\ftbquests\quests\chapters\ivi__mechanical_farming.snbt` |
| **Chapter: {ftbquests.chapter.ivi__mechanical_farming.quest345432E72BD82727.title}** | `minecraft:chain` | `config\ftbquests\quests\chapters\ivi__mechanical_farming.snbt` |
| **Chapter: {ftbquests.chapter.ivi__mechanical_farming.quest345432E72BD82727.title}** | `minecraft:hopper` | `config\ftbquests\quests\chapters\ivi__mechanical_farming.snbt` |
| **Chapter: {ftbquests.chapter.iv__prismatic_farming.quest146475549DD7BF4A.task.5940946691310424587.title}** | `society:crystalarium` | `config\ftbquests\quests\chapters\iv__prismatic_farming.snbt` |
| **Chapter: {ftbquests.chapter.iv__prismatic_farming.quest146475549DD7BF4A.task.5940946691310424587.title}** | `minecraft:enchanting_table` | `config\ftbquests\quests\chapters\iv__prismatic_farming.snbt` |
| **Chapter: {ftbquests.chapter.iv__prismatic_farming.quest146475549DD7BF4A.task.5940946691310424587.title}** | `society:treasure_totem` | `config\ftbquests\quests\chapters\iv__prismatic_farming.snbt` |
| **Chapter: {ftbquests.chapter.iv__prismatic_farming.quest146475549DD7BF4A.task.5940946691310424587.title}** | `society:sunlit_crystal` | `config\ftbquests\quests\chapters\iv__prismatic_farming.snbt` |
| **Chapter: {ftbquests.chapter.iv__prismatic_farming.quest146475549DD7BF4A.task.5940946691310424587.title}** | `moreminecarts:chiseled_organic_glass` | `config\ftbquests\quests\chapters\iv__prismatic_farming.snbt` |
| **Chapter: {ftbquests.chapter.iv__prismatic_farming.quest146475549DD7BF4A.task.5940946691310424587.title}** | `society:moon_statue` | `config\ftbquests\quests\chapters\iv__prismatic_farming.snbt` |
| **Chapter: {ftbquests.chapter.iv__prismatic_farming.quest146475549DD7BF4A.task.5940946691310424587.title}** | `minecraft:netherite_ingot` | `config\ftbquests\quests\chapters\iv__prismatic_farming.snbt` |
| **Chapter: {ftbquests.chapter.iv__prismatic_farming.quest146475549DD7BF4A.task.5940946691310424587.title}** | `minecraft:netherite_scrap` | `config\ftbquests\quests\chapters\iv__prismatic_farming.snbt` |
| **Chapter: {ftbquests.chapter.iv__prismatic_farming.quest146475549DD7BF4A.task.5940946691310424587.title}** | `splendid_slimes:slime_incubator` | `config\ftbquests\quests\chapters\iv__prismatic_farming.snbt` |
| **Chapter: {ftbquests.chapter.iv__prismatic_farming.quest146475549DD7BF4A.task.5940946691310424587.title}** | `minecraft:dragon_egg` | `config\ftbquests\quests\chapters\iv__prismatic_farming.snbt` |
| **Chapter: {ftbquests.chapter.iv__prismatic_farming.quest146475549DD7BF4A.task.5940946691310424587.title}** | `dew_drop_farmland_growth:garden_pot` | `config\ftbquests\quests\chapters\iv__prismatic_farming.snbt` |
| **Chapter: {ftbquests.chapter.minerals.quest1B75D6174593D5E5.task.2294170644355025534.title}** | `society:ghost_crystal` | `config\ftbquests\quests\chapters\minerals.snbt` |
| **Chapter: {ftbquests.chapter.minerals.quest1B75D6174593D5E5.task.2294170644355025534.title}** | `society:earth_crystal` | `config\ftbquests\quests\chapters\minerals.snbt` |
| **Chapter: {ftbquests.chapter.pantry.quest7D155FD0EFEEB5AC.title}** | `minecraft:sniffer_egg` | `config\ftbquests\quests\chapters\pantry.snbt` |
| **Chapter: {ftbquests.chapter.pantry.quest7D155FD0EFEEB5AC.title}** | `minecraft:pumpkin` | `config\ftbquests\quests\chapters\pantry.snbt` |
| **Chapter: {ftbquests.chapter.pantry.quest7D155FD0EFEEB5AC.title}** | `minecraft:melon` | `config\ftbquests\quests\chapters\pantry.snbt` |
| **Chapter: {ftbquests.chapter.pantry.quest7D155FD0EFEEB5AC.title}** | `minecraft:beetroot` | `config\ftbquests\quests\chapters\pantry.snbt` |
| **Chapter: {ftbquests.chapter.rare_pokmon.quest5258D723273DF790.subtitle}** | `sunlit_cobblemon:sunlit_league_medallion` | `config\ftbquests\quests\chapters\rare_pokmon.snbt` |
| **Chapter: {ftbquests.chapter.relics.quest19B466150B9315AE.subtitle}** | `minecraft:music_disc_relic` | `config\ftbquests\quests\chapters\relics.snbt` |
| **Chapter: {ftbquests.chapter.tools.quest31F6C5811A72396C.task.5746329288855922241.title}** | `minecraft:oak_log` | `config\ftbquests\quests\chapters\tools.snbt` |
| **Chapter: {ftbquests.chapter.transportation.quest4622E3EC44CED1B6.task.5869016450286606504.title}** | `moreminecarts:wooden_rail` | `config\ftbquests\quests\chapters\transportation.snbt` |
| **Chapter: {ftbquests.chapter.transportation.quest4622E3EC44CED1B6.task.5869016450286606504.title}** | `minecraft:lightning_rod` | `config\ftbquests\quests\chapters\transportation.snbt` |
| **Chapter: {ftbquests.chapter.transportation.quest4622E3EC44CED1B6.task.5869016450286606504.title}** | `moreminecarts:maglev_rail` | `config\ftbquests\quests\chapters\transportation.snbt` |
| **Chapter: {ftbquests.chapter.transportation.quest4622E3EC44CED1B6.task.5869016450286606504.title}** | `moreminecarts:wooden_rail_turn` | `config\ftbquests\quests\chapters\transportation.snbt` |
| **Chapter: {ftbquests.chapter.transportation.quest4622E3EC44CED1B6.task.5869016450286606504.title}** | `minecraft:rail` | `config\ftbquests\quests\chapters\transportation.snbt` |
| **Chapter: {ftbquests.chapter.transportation.quest4622E3EC44CED1B6.task.5869016450286606504.title}** | `moreminecarts:lightspeed_rail` | `config\ftbquests\quests\chapters\transportation.snbt` |
| **Chapter: {ftbquests.chapter.transportation.quest4622E3EC44CED1B6.task.5869016450286606504.title}** | `moreminecarts:wooden_cross_rail` | `config\ftbquests\quests\chapters\transportation.snbt` |
| **Chapter: {ftbquests.chapter.transportation.quest4622E3EC44CED1B6.task.5869016450286606504.title}** | `moreminecarts:lightspeed_powered_rail` | `config\ftbquests\quests\chapters\transportation.snbt` |
| **Chapter: {ftbquests.chapter.transportation.quest4622E3EC44CED1B6.task.5869016450286606504.title}** | `moreminecarts:maglev_powered_rail` | `config\ftbquests\quests\chapters\transportation.snbt` |
| **Chapter: {ftbquests.chapter.vault.quest7CE6C320CC9F9B87.title}** | `society:crystalarium` | `config\ftbquests\quests\chapters\vault.snbt` |
| **Chapter: {ftbquests.chapter.welcome.quest2B6877708A709B5C.subtitle}** | `minecraft:bundle` | `config\ftbquests\quests\chapters\welcome.snbt` |
| **Chapter: {ftbquests.chapter.welcome.quest2B6877708A709B5C.subtitle}** | `minecraft:oak_sapling` | `config\ftbquests\quests\chapters\welcome.snbt` |
| **Chapter: {ftbquests.chapter.welcome.quest2B6877708A709B5C.subtitle}** | `minecraft:dirt` | `config\ftbquests\quests\chapters\welcome.snbt` |

---

## 3. 🧩 Интерактивные блоки и сущности из JAR-модов

| Мод / Архив | Блок / Сущность (Класс) | Путь в JAR |
| :--- | :--- | :--- |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `craft_station.json` | `data/cobblemon_farmers/recipes/craft_station.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `raw_aluminum.json` | `data/cobblemon_farmers/recipes/craft_station/compat/create/steel/raw_aluminum.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `raw_copper.json` | `data/cobblemon_farmers/recipes/craft_station/compat/create/steel/raw_copper.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `raw_gold.json` | `data/cobblemon_farmers/recipes/craft_station/compat/create/steel/raw_gold.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `raw_iron.json` | `data/cobblemon_farmers/recipes/craft_station/compat/create/steel/raw_iron.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `raw_lead.json` | `data/cobblemon_farmers/recipes/craft_station/compat/create/steel/raw_lead.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `raw_nickel.json` | `data/cobblemon_farmers/recipes/craft_station/compat/create/steel/raw_nickel.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `raw_osmium.json` | `data/cobblemon_farmers/recipes/craft_station/compat/create/steel/raw_osmium.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `raw_platinum.json` | `data/cobblemon_farmers/recipes/craft_station/compat/create/steel/raw_platinum.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `raw_quicksilver.json` | `data/cobblemon_farmers/recipes/craft_station/compat/create/steel/raw_quicksilver.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `raw_silver.json` | `data/cobblemon_farmers/recipes/craft_station/compat/create/steel/raw_silver.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `raw_tin.json` | `data/cobblemon_farmers/recipes/craft_station/compat/create/steel/raw_tin.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `raw_uranium.json` | `data/cobblemon_farmers/recipes/craft_station/compat/create/steel/raw_uranium.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `raw_zinc.json` | `data/cobblemon_farmers/recipes/craft_station/compat/create/steel/raw_zinc.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `battery.json` | `data/cobblemon_farmers/recipes/craft_station/electric/battery.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `endless_battery.json` | `data/cobblemon_farmers/recipes/craft_station/electric/endless_battery.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `iron_ingot.json` | `data/cobblemon_farmers/recipes/craft_station/fire/iron_ingot.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `steak.json` | `data/cobblemon_farmers/recipes/craft_station/fire/steak.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `spectral_battery.json` | `data/cobblemon_farmers/recipes/craft_station/ghost/spectral_battery.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `energy_pylon.json` | `data/cobblemon_farmers/recipes/energy_pylon.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `cell_battery.json` | `data/cobblemon_farmers/recipes/energy_pylon/cell_battery.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `ranching_station.json` | `data/cobblemon_farmers/recipes/ranching_station.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `abra.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/abra.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `aerodactyl.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/aerodactyl.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `aggron.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/aggron.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `alakazam.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/alakazam.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `altaria.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/altaria.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `applin.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/applin.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `arbok.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/arbok.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `ariados.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/ariados.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `aron.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/aron.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `avalugg.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/avalugg.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `bayleef.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/bayleef.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `beedrill.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/beedrill.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `bergmite.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/bergmite.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `bibarel.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/bibarel.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `bidoof.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/bidoof.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `blastoise.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/blastoise.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `blaziken.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/blaziken.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `blissey.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/blissey.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `braixen.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/braixen.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `brionne.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/brionne.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `bulbasaur.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/bulbasaur.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `buneary.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/buneary.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `bunnelby.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/bunnelby.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `cacnea.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/cacnea.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `cacturne.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/cacturne.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `carbink.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/carbink.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `caterpie.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/caterpie.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `chansey.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/chansey.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `charizard.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/charizard.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `charmander.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/charmander.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `charmeleon.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/charmeleon.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `chesnaught.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/chesnaught.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `chespin.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/chespin.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `chikorita.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/chikorita.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `chimchar.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/chimchar.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `cinderace.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/cinderace.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `combee.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/combee.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `combusken.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/combusken.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `crocalor.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/crocalor.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `croconaw.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/croconaw.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `cryogonal.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/cryogonal.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `cyndaquil.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/cyndaquil.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `dartrix.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/dartrix.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `decidueye.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/decidueye.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `delphox.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/delphox.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `dewott.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/dewott.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `diglett.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/diglett.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `diglett_alolan.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/diglett_alolan.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `drapion.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/drapion.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `drizzile.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/drizzile.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `dubwool.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/dubwool.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `dugtrio.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/dugtrio.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `dugtrio_alolan.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/dugtrio_alolan.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `ekans.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/ekans.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `emboar.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/emboar.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `empoleon.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/empoleon.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `exeggcute.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/exeggcute.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `exeggutor.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/exeggutor.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `exeggutor_alolan.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/exeggutor_alolan.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `fennekin.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/fennekin.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `feraligatr.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/feraligatr.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `fletchinder.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/fletchinder.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `fletchling.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/fletchling.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `floragato.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/floragato.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `foongus.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/foongus.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `froakie.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/froakie.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `frogadier.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/frogadier.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `fuecoco.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/fuecoco.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `galvantula.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/galvantula.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `gholdengo.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/gholdengo.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `gimmighoul.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/gimmighoul.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `gourgeist.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/gourgeist.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `grafaiai.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/grafaiai.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `greninja.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/greninja.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `grimer.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/grimer.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `grookey.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/grookey.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `grotle.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/grotle.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `grovyle.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/grovyle.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `herdier.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/herdier.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `incineroar.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/incineroar.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `infernape.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/infernape.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `inteleon.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/inteleon.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `ivysaur.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/ivysaur.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `kadabra.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/kadabra.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `lairon.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/lairon.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `lapras.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/lapras.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `lillipup.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/lillipup.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `litten.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/litten.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `lopunny.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/lopunny.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `mareep.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/mareep.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `marshtomp.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/marshtomp.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `meganium.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/meganium.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `meowscarada.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/meowscarada.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `monferno.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/monferno.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `morelull.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/morelull.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `mudkip.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/mudkip.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `muk.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/muk.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `naganadel.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/naganadel.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `nidoking.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/nidoking.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `nidoranf.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/nidoranf.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `nidoranm.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/nidoranm.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `nidorina.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/nidorina.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `nidorino.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/nidorino.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `omanyte.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/omanyte.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `omastar.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/omastar.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `oshawott.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/oshawott.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `pachirisu.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/pachirisu.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `palossand.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/palossand.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `paras.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/paras.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `parasect.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/parasect.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `patrat.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/patrat.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `pelipper.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/pelipper.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `pignite.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/pignite.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `piplup.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/piplup.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `poipole.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/poipole.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `popplio.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/popplio.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `primarina.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/primarina.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `prinplup.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/prinplup.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `psyduck.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/psyduck.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `quaquaval.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/quaquaval.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `quaxly.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/quaxly.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `quaxwell.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/quaxwell.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `quilava.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/quilava.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `quilladin.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/quilladin.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `raboot.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/raboot.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `rillaboom.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/rillaboom.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `rowlet.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/rowlet.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `samurott.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/samurott.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `sandygast.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/sandygast.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `scatterbug.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/scatterbug.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `sceptile.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/sceptile.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `scorbunny.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/scorbunny.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `serperior.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/serperior.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `servine.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/servine.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `shellder.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/shellder.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `shroodle.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/shroodle.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `shroomish.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/shroomish.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `silicobra.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/silicobra.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `skeledirge.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/skeledirge.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `skorupi.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/skorupi.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `sliggoo.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/sliggoo.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `sliggoo_hisuian.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/sliggoo_hisuian.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `slurpuff.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/slurpuff.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `snivy.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/snivy.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `sobble.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/sobble.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `spidops.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/spidops.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `spinarak.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/spinarak.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `sprigatito.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/sprigatito.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `squirtle.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/squirtle.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `starmie.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/starmie.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `stoutland.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/stoutland.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `swablu.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/swablu.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `swampert.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/swampert.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `swirlix.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/swirlix.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `talonflame.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/talonflame.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `tarountula.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/tarountula.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `tatsugiri.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/tatsugiri.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `teddiursa.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/teddiursa.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `tentacool.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/tentacool.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `tepig.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/tepig.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `thwackey.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/thwackey.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `torchic.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/torchic.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `torracat.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/torracat.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `torterra.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/torterra.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `totodile.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/totodile.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `toxapex.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/toxapex.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `treecko.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/treecko.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `turtwig.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/turtwig.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `typhlosion.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/typhlosion.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `unfezant.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/unfezant.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `ursaluna.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/ursaluna.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `ursaring.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/ursaring.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `venonat.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/venonat.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `venusaur.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/venusaur.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `vespiquen.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/vespiquen.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `wartortle.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/wartortle.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `weedle.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/weedle.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `wingull.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/wingull.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `wooloo.json` | `data/cobblemon_farmers/recipes/ranching_station/forage/wooloo.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `miltank.json` | `data/cobblemon_farmers/recipes/ranching_station/milk/miltank.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `shuckle.json` | `data/cobblemon_farmers/recipes/ranching_station/milk/shuckle.json` |
| **Recipe in cobblemon_farmers-2.4-all.jar** | `slugma.json` | `data/cobblemon_farmers/recipes/ranching_station/milk/slugma.json` |
| **Mod: cobblemon_farmers-2.4-all.jar** | `CraftStationBlock` | `io/github/chakyl/cobblemonfarmers/block/CraftStationBlock.class` |
| **Mod: cobblemon_farmers-2.4-all.jar** | `CrystalBallBlock` | `io/github/chakyl/cobblemonfarmers/block/CrystalBallBlock.class` |
| **Mod: cobblemon_farmers-2.4-all.jar** | `EnergyPylonBlock` | `io/github/chakyl/cobblemonfarmers/block/EnergyPylonBlock.class` |
| **Mod: cobblemon_farmers-2.4-all.jar** | `GardeningStationBlock` | `io/github/chakyl/cobblemonfarmers/block/GardeningStationBlock.class` |
| **Mod: cobblemon_farmers-2.4-all.jar** | `MysteryMineBlock` | `io/github/chakyl/cobblemonfarmers/block/MysteryMineBlock.class` |
| **Mod: cobblemon_farmers-2.4-all.jar** | `RanchingStationBlock` | `io/github/chakyl/cobblemonfarmers/block/RanchingStationBlock.class` |
| **Mod: cobblemon_farmers-2.4-all.jar** | `CraftStationBlockEntity` | `io/github/chakyl/cobblemonfarmers/blockentity/CraftStationBlockEntity.class` |
| **Mod: cobblemon_farmers-2.4-all.jar** | `CrystalBallBlockEntity` | `io/github/chakyl/cobblemonfarmers/blockentity/CrystalBallBlockEntity.class` |
| **Mod: cobblemon_farmers-2.4-all.jar** | `EnergyPylonBlockEntity` | `io/github/chakyl/cobblemonfarmers/blockentity/EnergyPylonBlockEntity.class` |
| **Mod: cobblemon_farmers-2.4-all.jar** | `GardeningStationBlockEntity` | `io/github/chakyl/cobblemonfarmers/blockentity/GardeningStationBlockEntity.class` |
| **Mod: cobblemon_farmers-2.4-all.jar** | `MysteryMineBlockEntity` | `io/github/chakyl/cobblemonfarmers/blockentity/MysteryMineBlockEntity.class` |
| **Mod: cobblemon_farmers-2.4-all.jar** | `RanchingStationBlockEntity` | `io/github/chakyl/cobblemonfarmers/blockentity/RanchingStationBlockEntity.class` |
| **Mod: cobblemon_farmers-2.4-all.jar** | `StationBaseBlockEntity` | `io/github/chakyl/cobblemonfarmers/blockentity/StationBaseBlockEntity.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `AbstractStoveBlock` | `vectorwing/farmersdelight/common/block/AbstractStoveBlock.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `BasketBlock` | `vectorwing/farmersdelight/common/block/BasketBlock.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `BuddingBushBlock` | `vectorwing/farmersdelight/common/block/BuddingBushBlock.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `BuddingTomatoBlock` | `vectorwing/farmersdelight/common/block/BuddingTomatoBlock.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `CabbageBlock` | `vectorwing/farmersdelight/common/block/CabbageBlock.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `CabinetBlock` | `vectorwing/farmersdelight/common/block/CabinetBlock.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `CanvasRugBlock` | `vectorwing/farmersdelight/common/block/CanvasRugBlock.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `CeilingHangingCanvasSignBlock` | `vectorwing/farmersdelight/common/block/CeilingHangingCanvasSignBlock.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `CookingPotBlock` | `vectorwing/farmersdelight/common/block/CookingPotBlock.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `CuttingBoardBlock` | `vectorwing/farmersdelight/common/block/CuttingBoardBlock.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `AbstractStoveBlockEntity` | `vectorwing/farmersdelight/common/block/entity/AbstractStoveBlockEntity.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `BasketBlockEntity` | `vectorwing/farmersdelight/common/block/entity/BasketBlockEntity.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `CabinetBlockEntity` | `vectorwing/farmersdelight/common/block/entity/CabinetBlockEntity.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `CanvasSignBlockEntity` | `vectorwing/farmersdelight/common/block/entity/CanvasSignBlockEntity.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `CookingPotBlockEntity` | `vectorwing/farmersdelight/common/block/entity/CookingPotBlockEntity.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `CuttingBoardBlockEntity` | `vectorwing/farmersdelight/common/block/entity/CuttingBoardBlockEntity.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `HangingCanvasSignBlockEntity` | `vectorwing/farmersdelight/common/block/entity/HangingCanvasSignBlockEntity.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `HeatableBlockEntity` | `vectorwing/farmersdelight/common/block/entity/HeatableBlockEntity.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `SkilletBlockEntity` | `vectorwing/farmersdelight/common/block/entity/SkilletBlockEntity.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `StoveBlockEntity` | `vectorwing/farmersdelight/common/block/entity/StoveBlockEntity.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `SyncedBlockEntity` | `vectorwing/farmersdelight/common/block/entity/SyncedBlockEntity.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `FeastBlock` | `vectorwing/farmersdelight/common/block/FeastBlock.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `GleamingSaladBlock` | `vectorwing/farmersdelight/common/block/GleamingSaladBlock.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `HangingTomatoBlock` | `vectorwing/farmersdelight/common/block/HangingTomatoBlock.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `MushroomColonyBlock` | `vectorwing/farmersdelight/common/block/MushroomColonyBlock.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `OnionBlock` | `vectorwing/farmersdelight/common/block/OnionBlock.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `OrganicCompostBlock` | `vectorwing/farmersdelight/common/block/OrganicCompostBlock.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `PieBlock` | `vectorwing/farmersdelight/common/block/PieBlock.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `RiceBaleBlock` | `vectorwing/farmersdelight/common/block/RiceBaleBlock.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `RiceBlock` | `vectorwing/farmersdelight/common/block/RiceBlock.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `RicePaniclesBlock` | `vectorwing/farmersdelight/common/block/RicePaniclesBlock.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `RiceRollMedleyBlock` | `vectorwing/farmersdelight/common/block/RiceRollMedleyBlock.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `RichSoilBlock` | `vectorwing/farmersdelight/common/block/RichSoilBlock.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `RichSoilFarmlandBlock` | `vectorwing/farmersdelight/common/block/RichSoilFarmlandBlock.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `RopeBlock` | `vectorwing/farmersdelight/common/block/RopeBlock.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `RopeFenceBlock` | `vectorwing/farmersdelight/common/block/RopeFenceBlock.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `RopeFenceGateBlock` | `vectorwing/farmersdelight/common/block/RopeFenceGateBlock.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `RotatedFeastBlock` | `vectorwing/farmersdelight/common/block/RotatedFeastBlock.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `SafetyNetBlock` | `vectorwing/farmersdelight/common/block/SafetyNetBlock.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `SandyShrubBlock` | `vectorwing/farmersdelight/common/block/SandyShrubBlock.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `SkilletBlock` | `vectorwing/farmersdelight/common/block/SkilletBlock.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `StandingCanvasSignBlock` | `vectorwing/farmersdelight/common/block/StandingCanvasSignBlock.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `StoveBlock` | `vectorwing/farmersdelight/common/block/StoveBlock.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `StrawBaleBlock` | `vectorwing/farmersdelight/common/block/StrawBaleBlock.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `TatamiBlock` | `vectorwing/farmersdelight/common/block/TatamiBlock.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `TatamiHalfMatBlock` | `vectorwing/farmersdelight/common/block/TatamiHalfMatBlock.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `TatamiMatBlock` | `vectorwing/farmersdelight/common/block/TatamiMatBlock.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `TomatoBlock` | `vectorwing/farmersdelight/common/block/TomatoBlock.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `TomatoVineBlock` | `vectorwing/farmersdelight/common/block/TomatoVineBlock.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `WallCanvasSignBlock` | `vectorwing/farmersdelight/common/block/WallCanvasSignBlock.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `WallHangingCanvasSignBlock` | `vectorwing/farmersdelight/common/block/WallHangingCanvasSignBlock.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `WildCropBlock` | `vectorwing/farmersdelight/common/block/WildCropBlock.class` |
| **Mod: FarmersDelight-1.20.1-1.3.2.jar** | `WildRiceBlock` | `vectorwing/farmersdelight/common/block/WildRiceBlock.class` |
| **Mod: Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar** | `MultiblockBlock` | `com/cobblemon/mod/common/api/multiblock/MultiblockBlock.class` |
| **Mod: Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar** | `ApricornBlock` | `com/cobblemon/mod/common/block/ApricornBlock.class` |
| **Mod: Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar** | `ApricornSaplingBlock` | `com/cobblemon/mod/common/block/ApricornSaplingBlock.class` |
| **Mod: Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar** | `BerryBlock` | `com/cobblemon/mod/common/block/BerryBlock.class` |
| **Mod: Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar** | `BigRootBlock` | `com/cobblemon/mod/common/block/BigRootBlock.class` |
| **Mod: Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar** | `CoinPouchBlock` | `com/cobblemon/mod/common/block/CoinPouchBlock.class` |
| **Mod: Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar** | `DisplayCaseBlock` | `com/cobblemon/mod/common/block/DisplayCaseBlock.class` |
| **Mod: Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar** | `EnergyRootBlock` | `com/cobblemon/mod/common/block/EnergyRootBlock.class` |
| **Mod: Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar** | `FossilAnalyzerBlock` | `com/cobblemon/mod/common/block/FossilAnalyzerBlock.class` |
| **Mod: Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar** | `GrowableStoneBlock` | `com/cobblemon/mod/common/block/GrowableStoneBlock.class` |
| **Mod: Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar** | `HealingMachineBlock` | `com/cobblemon/mod/common/block/HealingMachineBlock.class` |
| **Mod: Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar** | `MedicinalLeekBlock` | `com/cobblemon/mod/common/block/MedicinalLeekBlock.class` |
| **Mod: Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar** | `MintBlock` | `com/cobblemon/mod/common/block/MintBlock.class` |
| **Mod: Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar** | `MonitorBlock` | `com/cobblemon/mod/common/block/MonitorBlock.class` |
| **Mod: Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar** | `PCBlock` | `com/cobblemon/mod/common/block/PCBlock.class` |
| **Mod: Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar** | `PastureBlock` | `com/cobblemon/mod/common/block/PastureBlock.class` |
| **Mod: Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar** | `RestorationTankBlock` | `com/cobblemon/mod/common/block/RestorationTankBlock.class` |
| **Mod: Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar** | `RevivalHerbBlock` | `com/cobblemon/mod/common/block/RevivalHerbBlock.class` |
| **Mod: Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar** | `RootBlock` | `com/cobblemon/mod/common/block/RootBlock.class` |
| **Mod: Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar** | `ShearableBlock` | `com/cobblemon/mod/common/block/ShearableBlock.class` |
| **Mod: Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar** | `TumblestoneBlock` | `com/cobblemon/mod/common/block/TumblestoneBlock.class` |
| **Mod: Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar** | `VivichokeBlock` | `com/cobblemon/mod/common/block/VivichokeBlock.class` |
| **Mod: Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar** | `GildedChestBlock` | `com/cobblemon/mod/common/block/chest/GildedChestBlock.class` |
| **Mod: Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar** | `BerryBlockEntity` | `com/cobblemon/mod/common/block/entity/BerryBlockEntity.class` |
| **Mod: Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar** | `CobblemonHangingSignBlockEntity` | `com/cobblemon/mod/common/block/entity/CobblemonHangingSignBlockEntity.class` |
| **Mod: Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar** | `CobblemonSignBlockEntity` | `com/cobblemon/mod/common/block/entity/CobblemonSignBlockEntity.class` |
| **Mod: Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar** | `DisplayCaseBlockEntity` | `com/cobblemon/mod/common/block/entity/DisplayCaseBlockEntity.class` |
| **Mod: Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar** | `FossilAnalyzerBlockEntity` | `com/cobblemon/mod/common/block/entity/FossilAnalyzerBlockEntity.class` |
| **Mod: Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar** | `GildedChestBlockEntity` | `com/cobblemon/mod/common/block/entity/GildedChestBlockEntity.class` |
| **Mod: Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar** | `HealingMachineBlockEntity` | `com/cobblemon/mod/common/block/entity/HealingMachineBlockEntity.class` |
| **Mod: Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar** | `PCBlockEntity` | `com/cobblemon/mod/common/block/entity/PCBlockEntity.class` |
| **Mod: Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar** | `PokemonPastureBlockEntity` | `com/cobblemon/mod/common/block/entity/PokemonPastureBlockEntity.class` |
| **Mod: Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar** | `RestorationTankBlockEntity` | `com/cobblemon/mod/common/block/entity/RestorationTankBlockEntity.class` |
| **Mod: Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar** | `CobblemonHangingSignBlock` | `com/cobblemon/mod/common/block/sign/CobblemonHangingSignBlock.class` |
| **Mod: Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar** | `CobblemonSignBlock` | `com/cobblemon/mod/common/block/sign/CobblemonSignBlock.class` |
| **Mod: Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar** | `CobblemonWallHangingSignBlock` | `com/cobblemon/mod/common/block/sign/CobblemonWallHangingSignBlock.class` |
| **Mod: Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar** | `CobblemonWallSignBlock` | `com/cobblemon/mod/common/block/sign/CobblemonWallSignBlock.class` |
| **Mod: Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar** | `ServerPlayerEvent$RightClickBlock` | `com/cobblemon/mod/common/platform/events/ServerPlayerEvent$RightClickBlock.class` |
| **Mod: Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar** | `UCharacter$UnicodeBlock` | `com/cobblemon/mod/relocations/ibm/icu/lang/UCharacter$UnicodeBlock.class` |
| **Mod: Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar** | `Block` | `com/oracle/js/parser/ir/Block.class` |
| **Mod: Sunlit_Cobblebackported-forge-1.5.2-1.3_1.20.1.jar** | `HostAdapterBytecodeGenerator$TryBlock` | `com/oracle/truffle/host/HostAdapterBytecodeGenerator$TryBlock.class` |
| **Mod: sunlit_cobblemon-1.9.jar** | `MonBoxBlock` | `io/github/chakyl/sunlitcobblemon/block/MonBoxBlock.class` |
| **Mod: sunlit_cobblemon-1.9.jar** | `MonBoxBlockEntity` | `io/github/chakyl/sunlitcobblemon/blockentity/MonBoxBlockEntity.class` |
