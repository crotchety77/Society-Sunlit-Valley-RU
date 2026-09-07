# Приоритетный аудит локализации модов для игрока

Данный аудит учитывает реальное присутствие предметов в игре и в JEI, исключая отключённые автором предметы (`globalRemovedItems.js`) и скрытые технические атрибуты.

## 🎮 ТИР 1: Реальный игровой контент (То, что игрок видит в мире, инвентаре и JEI)
> **Приоритет: КРИТИЧЕСКИ ВЫСОКИЙ**. Перевод этих модов напрямую формирует впечатления от игры.

| Namespace | Не переведено | Всего строк | Активных предметов в JEI | Отключено автором | JAR-файл |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `etcetera` | **117** (0.0%) | 117 | **75** предм./блок. | 5 откл. | `Etcetera-1.20.1-1.1.3-Forge.jar` |
| `buildinggadgets2` | **111** (0.0%) | 111 | **9** предм./блок. | 0 откл. | `buildinggadgets2-1.0.7.jar` |
| `create_central_kitchen` | **106** (41.1%) | 180 | **33** предм./блок. | 9 откл. | `create_central_kitchen-1.20.1-for-create-6.0.8-1.5.0.jar` |
| `legendarycreatures` | **102** (0.0%) | 102 | **19** предм./блок. | 2 откл. | `legendarycreatures-1.20.1-1.1.1.3.jar` |
| `whimsy_deco` | **95** (0.0%) | 95 | **78** предм./блок. | 11 откл. | `whimsy_deco-1.2.jar` |
| `relics` | **61** (84.8%) | 402 | **27** предм./блок. | 4 откл. | `relics-1.20.1-0.8.0.11.jar` |
| `waystones` | **61** (69.3%) | 199 | **14** предм./блок. | 19 откл. | `waystones-forge-1.20.1-14.1.17.jar` |
| `questsadditions` | **57** (0.0%) | 57 | **1** предм./блок. | 0 откл. | `questsadditions-1.4.7.jar` |
| `botania` | **55** (98.4%) | 3492 | **1290** предм./блок. | 10 откл. | `Botania-1.20.1-454-FORGE.jar` |
| `ftbquests` | **54** (90.6%) | 572 | **33** предм./блок. | 24 откл. | `ftb-quests-forge-2001.4.17.jar` |
| `kiwi` | **51** (0.0%) | 51 | **2** предм./блок. | 0 откл. | `Kiwi-1.20.1-Forge-11.9.2.jar` |
| `untitledduckmod` | **49** (40.2%) | 82 | **17** предм./блок. | 0 откл. | `untitledduckmod-1.5.2-forge-1.20.1.jar` |
| `titanium` | **48** (0.0%) | 48 | **4** предм./блок. | 0 откл. | `titanium-1.20.1-3.8.32.jar` |
| `ftblibrary` | **47** (52.5%) | 99 | **2** предм./блок. | 0 откл. | `ftb-library-forge-2001.2.12.jar` |
| `solonion` | **45** (0.0%) | 45 | **8** предм./блок. | 0 откл. | `SoLOnion_FORGE_v1.4.5_mc1.20.1.jar` |
| `verdantvibes` | **41** (0.0%) | 41 | **32** предм./блок. | 1 откл. | `verdantvibes-1.0.3-1.20.1.jar` |
| `farmlife` | **40** (0.0%) | 40 | **22** предм./блок. | 7 откл. | `farmlife-1.20.1-1.1.0.jar` |
| `sophisticatedbackpacks` | **39** (86.5%) | 289 | **119** предм./блок. | 16 откл. | `sophisticatedbackpacks-1.20.1-3.24.60.1982.jar` |
| `comforts` | **37** (51.9%) | 77 | **29** предм./блок. | 18 откл. | `comforts-forge-6.4.0+1.20.1.jar` |
| `via_romana` | **37** (81.8%) | 203 | **1** предм./блок. | 0 откл. | `via_romana-2.2.2+1.20.1-forge.jar` |
| `rehooked` | **36** (0.0%) | 36 | **8** предм./блок. | 6 откл. | `rehooked-1.8.3-1.20.1.jar` |
| `railways` | **36** (98.6%) | 2541 | **1938** предм./блок. | 0 откл. | `Steam_Rails-1.7.2+forge-mc1.20.1.jar` |
| `paraglider` | **35** (73.7%) | 133 | **12** предм./блок. | 0 откл. | `Paraglider-forge-20.1.3.jar` |
| `vanillabackport` | **32** (86.4%) | 236 | **124** предм./блок. | 0 откл. | `VanillaBackport-forge-1.20.1-1.1.7.10.jar` |
| `geckolib` | **31** (0.0%) | 31 | **21** предм./блок. | 0 откл. | `geckolib-forge-1.20.1-4.8.jar` |
| `justhammers` | **31** (3.1%) | 32 | **11** предм./блок. | 18 откл. | `justhammers-forge-2.0.3+mc1.20.1.jar` |
| `everycomp` | **30** (97.0%) | 989 | **41** предм./блок. | 0 откл. | `everycomp-1.20-2.9.24-forge.jar` |
| `sewingkit` | **29** (0.0%) | 29 | **9** предм./блок. | 13 откл. | `SewingKit-1.20.1-1.8.1.jar` |
| `dew_drop_farmland_growth` | **28** (0.0%) | 28 | **27** предм./блок. | 0 откл. | `dew_drop_farmland_growth-9.0.jar` |
| `create` | **27** (99.3%) | 3646 | **883** предм./блок. | 22 откл. | `create-1.20.1-6.0.8.jar` |
| `portable_blueprints` | **26** (84.0%) | 163 | **16** предм./блок. | 0 откл. | `portable_blueprints-v2.0.11-mv1.20.1.jar` |
| `autumnity` | **25** (85.0%) | 167 | **135** предм./блок. | 3 откл. | `autumnity-1.20.1-5.0.2.jar` |
| `citadel` | **24** (0.0%) | 24 | **1** предм./блок. | 5 откл. | `citadel-2.6.3-1.20.1.jar` |
| `furniture` | **24** (89.4%) | 226 | **165** предм./блок. | 0 откл. | `letsdo-furniture-forge-1.0.4.jar` |
| `moblassos` | **23** (0.0%) | 23 | **6** предм./блок. | 12 откл. | `MobLassos-v8.0.1-1.20.1-Forge.jar` |
| `decorative_blocks` | **22** (68.1%) | 69 | **54** предм./блок. | 1 откл. | `decorative_blocks-forge-1.20.1-4.1.3.jar` |
| `quark` | **22** (98.5%) | 1516 | **914** предм./блок. | 4 откл. | `Quark-4.0-462.jar` |
| `refinedstorage` | **22** (93.9%) | 361 | **29** предм./блок. | 66 откл. | `refinedstorage-1.12.4.jar` |
| `clayworks` | **21** (87.0%) | 162 | **157** предм./блок. | 0 откл. | `clayworks-1.20.1-3.0.4.jar` |
| `create_hypertube` | **21** (58.0%) | 50 | **11** предм./блок. | 0 откл. | `create_hypertube-0.4.0-FORGE.jar` |
| `farmingforblockheads` | **21** (58.0%) | 50 | **2** предм./блок. | 9 откл. | `farmingforblockheads-forge-1.20.1-14.0.2.jar` |
| `doapi` | **21** (0.0%) | 21 | **2** предм./блок. | 0 откл. | `letsdo-API-forge-1.2.15-forge.jar` |
| `botania_seeds` | **20** (0.0%) | 20 | **16** предм./блок. | 0 откл. | `botania_seeds-1.1.1.jar` |
| `hamsters` | **20** (0.0%) | 20 | **5** предм./блок. | 0 откл. | `hamsters-forge-1.0.3-1.20.1.jar` |
| `create_mechanical_extruder` | **19** (0.0%) | 19 | **1** предм./блок. | 0 откл. | `create_mecanical_extruder-1.20.1-1.6.11-6.0.6.jar` |
| `crabbersdelight` | **18** (80.2%) | 91 | **63** предм./блок. | 5 откл. | `CrabbersDelight-1.20.1-1.1.7d.jar` |
| `domesticationinnovation` | **17** (86.4%) | 125 | **26** предм./блок. | 0 откл. | `domesticationinnovation-1.7.2-1.20.1.jar` |
| `snowyspirit` | **16** (82.6%) | 92 | **77** предм./блок. | 0 откл. | `snowyspirit-1.20-3.0.10.jar` |
| `fantasyfurniture` | **15** (96.4%) | 416 | **371** предм./блок. | 1 откл. | `fantasyfurniture-1.20.1-9.0.0.jar` |
| `strawstatues` | **14** (0.0%) | 14 | **1** предм./блок. | 0 откл. | `StrawStatues-v8.0.3-1.20.1-Forge.jar` |
| `supplementaries` | **14** (97.7%) | 607 | **303** предм./блок. | 0 откл. | `supplementaries-1.20-3.1.43-forge.jar` |
| `extractinator` | **13** (18.8%) | 16 | **2** предм./блок. | 1 откл. | `extractinator-forge-1.20.1-2.3.0.jar` |
| `windswept` | **13** (97.4%) | 496 | **439** предм./блок. | 5 откл. | `windswept-1.20.1-3.0.4.jar` |
| `zetter` | **13** (87.4%) | 103 | **37** предм./блок. | 0 откл. | `zetter-1.20.1-0.21.7.jar` |
| `bountiful` | **12** (81.8%) | 66 | **1** предм./блок. | 0 откл. | `Bountiful-6.0.4+1.20.1-forge.jar` |
| `crafting_on_a_stick` | **12** (7.7%) | 13 | **6** предм./блок. | 3 откл. | `crafting-on-a-stick-1.20.1-1.1.5.jar` |
| `farm_and_charm` | **12** (94.0%) | 199 | **96** предм./блок. | 14 откл. | `letsdo-farm_and_charm-forge-1.0.4.jar` |
| `online_detector` | **12** (29.4%) | 17 | **2** предм./блок. | 0 откл. | `online_detector-forge-1.20-6.0.0.jar` |
| `society_trading` | **12** (25.0%) | 16 | **1** предм./блок. | 0 откл. | `society_trading-1.2.8.jar` |
| `wildernature` | **11** (96.4%) | 307 | **35** предм./блок. | 16 откл. | `letsdo-wildernature-forge-1.0.5.jar` |
| `kata` | **11** (0.0%) | 11 | **11** предм./блок. | 0 откл. | `society-1.22.jar` |
| `functionalstorage` | **10** (91.7%) | 121 | **64** предм./блок. | 1 откл. | `functionalstorage-1.20.1-1.2.13.jar` |
| `itemfilters` | **10** (75.6%) | 41 | **1** предм./блок. | 30 откл. | `item-filters-forge-2001.1.0-build.59.jar` |
| `treechop` | **10** (83.1%) | 59 | **1** предм./блок. | 0 откл. | `TreeChop-1.20.1-forge-0.19.0-fixed.jar` |
| `waterframes` | **10** (91.7%) | 120 | **6** предм./блок. | 0 откл. | `waterframes-FORGE-mc1.20.1-v2.1.20.jar` |
| `automobility` | **9** (94.7%) | 170 | **18** предм./блок. | 2 откл. | `automobility-0.4.2+1.20.1-forge.jar` |
| `betterarcheology` | **9** (92.4%) | 118 | **86** предм./блок. | 3 откл. | `betterarcheology-1.2.1-1.20.1.jar` |
| `createrailwaysnavigator` | **9** (98.1%) | 465 | **52** предм./блок. | 0 откл. | `createrailwaysnavigator-forge-1.20.1-beta-0.8.5-C6.jar` |
| `species` | **9** (98.2%) | 514 | **143** предм./блок. | 0 откл. | `species-3.5.jar` |
| `classicpipes` | **8** (95.3%) | 172 | **90** предм./блок. | 0 откл. | `classicpipes-forge-1.20.1-1.1.5.jar` |
| `create_factory_logistics` | **8** (70.4%) | 27 | **6** предм./блок. | 0 откл. | `create_factory_logistics-1.20.1-1.4.7.jar` |
| `golemoverhaul` | **8** (86.4%) | 59 | **13** предм./блок. | 0 откл. | `golemoverhaul-forge-1.20.1-1.1.0.jar` |
| `nethervinery` | **8** (87.5%) | 64 | **45** предм./блок. | 7 откл. | `letsdo-nethervinery-forge-1.2.19.jar` |
| `trials` | **8** (96.4%) | 223 | **129** предм./блок. | 1 откл. | `Trials-2.3.3.jar` |
| `veggiesdelight` | **8** (93.2%) | 117 | **90** предм./блок. | 4 откл. | `VeggiesDelight-1.20.1-1.9.3.jar` |
| `atmospheric` | **7** (98.8%) | 608 | **509** предм./блок. | 4 откл. | `atmospheric-1.20.1-6.1.1.jar` |
| `croptania` | **7** (0.0%) | 7 | **2** предм./блок. | 0 откл. | `croptania-0.3.jar` |
| `numismatics_utils` | **7** (0.0%) | 7 | **2** предм./блок. | 0 откл. | `numismatics_utils-2.1.jar` |
| `buzzier_bees` | **6** (93.3%) | 89 | **72** предм./блок. | 0 откл. | `buzzier_bees-1.20.1-6.0.1.jar` |
| `vinery` | **6** (98.3%) | 351 | **176** предм./блок. | 6 откл. | `letsdo-vinery-forge-1.4.41.jar` |
| `littlejoys` | **6** (0.0%) | 6 | **2** предм./блок. | 0 откл. | `littlejoys-forge-1.20.1-20.1.14.jar` |
| `sophisticatedcore` | **6** (97.9%) | 288 | **11** предм./блок. | 0 откл. | `sophisticatedcore-1.20.1-1.3.71.2181.jar` |
| `sophisticatedstorage` | **6** (98.0%) | 294 | **192** предм./блок. | 20 откл. | `sophisticatedstorage-1.20.1-1.4.74.1997.jar` |
| `dew_drop_watering_cans` | **5** (0.0%) | 5 | **5** предм./блок. | 0 откл. | `dew_drop_watering_cans-1.0.2.jar` |
| `exposure` | **5** (97.3%) | 187 | **41** предм./блок. | 0 откл. | `exposure-1.20.1-1.7.16-forge.jar` |
| `netherdepthsupgrade` | **5** (97.4%) | 193 | **143** предм./блок. | 14 откл. | `netherdepthsupgrade-3.1.5-1.20.jar` |
| `amendments` | **4** (95.7%) | 92 | **17** предм./блок. | 45 откл. | `amendments-1.20-2.2.5.jar` |
| `lootr` | **4** (92.2%) | 51 | **7** предм./блок. | 0 откл. | `lootr-forge-1.20-0.7.35.90.jar` |
| `plonk` | **4** (0.0%) | 4 | **1** предм./блок. | 0 откл. | `plonk-1.20.1-10.0.5-forge.jar` |
| `rainbowoaks` | **4** (0.0%) | 4 | **4** предм./блок. | 0 откл. | `rainbowoaks-forge-1.20-1.0.0.jar` |
| `sawmill` | **4** (42.9%) | 7 | **1** предм./блок. | 0 откл. | `sawmill-1.20-1.4.10.jar` |
| `easy_npc` | **3** (96.0%) | 75 | **2** предм./блок. | 7 откл. | `easy_npc-forge-1.20.1-6.1.0.jar` |
| `gamediscs` | **3** (92.9%) | 42 | **8** предм./блок. | 5 откл. | `gamediscs-0.3.2-forge.jar` |
| `beachparty` | **3** (97.6%) | 123 | **90** предм./блок. | 1 откл. | `letsdo-beachparty-forge-1.1.5.jar` |
| `herbalbrews` | **3** (97.6%) | 124 | **45** предм./блок. | 0 откл. | `letsdo-herbalbrews-forge-1.0.12.jar` |
| `patchouli` | **3** (96.7%) | 90 | **16** предм./блок. | 0 откл. | `Patchouli-1.20.1-85-FORGE.jar` |
| `ribbits` | **3** (91.7%) | 36 | **20** предм./блок. | 0 откл. | `Ribbits-1.20.1-Forge-3.0.5.jar` |
| `simplerecall` | **3** (0.0%) | 3 | **1** предм./блок. | 0 откл. | `simplerecall-1.0.6-1.20.1.jar` |
| `snowpig` | **3** (66.7%) | 9 | **5** предм./блок. | 0 откл. | `snowpig-1.20.1-6.0.3.jar` |
| `snowrealmagic` | **3** (91.7%) | 36 | **5** предм./блок. | 0 откл. | `SnowRealMagic-1.20.1-Forge-10.7.0.jar` |
| `society` | **3** (95.5%) | 67 | **6** предм./блок. | 0 откл. | `society-1.22.jar` |
| `torchmaster` | **3** (78.6%) | 14 | **9** предм./блок. | 0 откл. | `torchmaster-20.1.9.jar` |
| `numismatics` | **2** (98.1%) | 108 | **76** предм./блок. | 3 откл. | `CreateNumismatics-1.0.15+forge-mc1.20.1.jar` |
| `extra_gauges` | **2** (98.3%) | 121 | **8** предм./блок. | 0 откл. | `extra_gauges-2.0.7.jar` |
| `gag` | **2** (96.4%) | 55 | **39** предм./блок. | 6 откл. | `gag-forge-3.0.0-build.13.jar` |
| `candlelight` | **2** (99.2%) | 243 | **168** предм./блок. | 13 откл. | `letsdo-candlelight-forge-2.0.2.jar` |
| `liltractor` | **2** (0.0%) | 2 | **1** предм./блок. | 0 откл. | `LittleTractor-1.20.1-1.2.jar` |
| `pipez` | **2** (97.6%) | 83 | **3** предм./блок. | 9 откл. | `pipez-forge-1.20.1-1.2.21.jar` |
| `smallships` | **2** (97.9%) | 95 | **66** предм./блок. | 0 откл. | `smallships-forge-1.20.1-2.0.0-b1.4.jar` |
| `constructionwand` | **1** (98.3%) | 59 | **6** предм./блок. | 0 откл. | `constructionwand-1.20.1-2.11.jar` |
| `copycats` | **1** (98.5%) | 67 | **48** предм./блок. | 0 откл. | `copycats-3.0.7+mc.1.20.1-forge.jar` |
| `createutilities` | **1** (98.3%) | 59 | **15** предм./блок. | 2 откл. | `createutilities-0.3.2+1.20.1.jar` |
| `crittersandcompanions` | **1** (98.4%) | 63 | **21** предм./блок. | 8 откл. | `crittersandcompanions-forge-1.20.1-2.3.5.jar` |
| `etched` | **1** (97.5%) | 40 | **15** предм./блок. | 0 откл. | `etched-3.0.4.jar` |
| `fastpaintings` | **1** (0.0%) | 1 | **1** предм./блок. | 0 откл. | `fastpaintings-1.20-1.2.7.jar` |
| `immersive_paintings` | **1** (98.7%) | 79 | **4** предм./блок. | 0 откл. | `immersive_paintings-0.6.13+1.20.1-forge.jar` |
| `bakery` | **1** (99.3%) | 146 | **87** предм./блок. | 1 откл. | `letsdo-bakery-forge-2.0.3.jar` |
| `brewery` | **1** (99.4%) | 165 | **64** предм./блок. | 1 откл. | `letsdo-brewery-forge-2.0.3.jar` |
| `meadow` | **1** (99.6%) | 247 | **164** предм./блок. | 9 откл. | `letsdo-meadow-forge-1.3.23.jar` |
| `moonlight` | **1** (90.0%) | 10 | **2** предм./блок. | 0 откл. | `moonlight-1.20-2.16.34-forge.jar` |
| `mysticaloaktree` | **1** (0.0%) | 1 | **1** предм./блок. | 0 откл. | `mysticaloaktree-1.20-1.11.jar` |
| `naturescompass` | **1** (97.7%) | 43 | **1** предм./блок. | 0 откл. | `NaturesCompass-1.20.1-1.11.2-forge.jar` |
| `oreganized` | **1** (99.6%) | 240 | **178** предм./блок. | 0 откл. | `Oreganized 1.20.1-4.3.2.jar` |
| `refinedstorageaddons` | **1** (75.0%) | 4 | **1** предм./блок. | 1 откл. | `refinedstorageaddons-0.10.0.jar` |
| `sereneseasons` | **1** (97.2%) | 36 | **3** предм./блок. | 0 откл. | `SereneSeasons-forge-1.20.1-9.1.0.2.jar` |

---

## 🖥️ ТИР 2: Интерфейс, UI, Меню и Всплывающие подсказки
> **Приоритет: СРЕДНИЙ**. Окна настроек, интерфейсы интеграций (JEI, Jade, JourneyMap, Camera).

| Namespace | Не переведено | Всего строк | Состав (GUI / Тултипы) | JAR-файл |
| :--- | :---: | :---: | :--- | :--- |
| `emixx` | **86** (0.0%) | 86 | 5 GUI, 0 тултип. | `emixx-forge-1.5.3.jar` |
| `nochatreports` | **86** (33.3%) | 129 | 62 GUI, 0 тултип. | `NoChatReports-FORGE-1.20.1-v2.2.2.jar` |
| `jade` | **70** (75.0%) | 280 | 14 GUI, 12 тултип. | `Jade-1.20.1-Forge-11.13.2.jar` |
| `structurify` | **67** (0.0%) | 67 | 64 GUI, 0 тултип. | `structurify-forge-1.0.21+mc1.20.1.jar` |
| `exposure_catalog` | **65** (0.0%) | 65 | 65 GUI, 0 тултип. | `exposure_catalog-1.20.1-1.0.3-forge.jar` |
| `perfectplushies` | **63** (0.0%) | 63 | 0 GUI, 2 тултип. | `perfectplushies-forge-1.20.1-1.13.3.jar` |
| `scholar` | **62** (41.5%) | 106 | 49 GUI, 0 тултип. | `scholar-1.20.1-1.2.5.1-forge.jar` |
| `horseman` | **42** (0.0%) | 42 | 4 GUI, 0 тултип. | `horseman-1.20.1-1.3.15-forge.jar` |
| `aitranslator` | **30** (0.0%) | 30 | 5 GUI, 0 тултип. | `aitranslator-1.0.1.jar` |
| `jei` | **25** (81.1%) | 132 | 24 GUI, 0 тултип. | `jei-1.20.1-forge-15.20.0.129.jar` |
| `seasonhud` | **20** (83.3%) | 120 | 53 GUI, 60 тултип. | `seasonhud-forge-1.20.1-2.0.0.jar` |
| `craftingtweaks` | **17** (54.1%) | 37 | 0 GUI, 6 тултип. | `craftingtweaks-forge-1.20.1-18.2.8.jar` |
| `creativecore` | **14** (68.2%) | 44 | 20 GUI, 0 тултип. | `CreativeCore_FORGE_v2.12.32_mc1.20.1.jar` |
| `tipsmod` | **14** (84.9%) | 93 | 10 GUI, 0 тултип. | `Tips-Forge-1.20.1-12.1.9.jar` |
| `observable` | **5** (84.4%) | 32 | 3 GUI, 0 тултип. | `observable-4.4.1.jar` |
| `curios` | **4** (91.7%) | 48 | 3 GUI, 0 тултип. | `curios-forge-5.14.1+1.20.1.jar` |
| `emi` | **4** (99.5%) | 743 | 4 GUI, 33 тултип. | `emi-1.1.22+1.20.1+forge.jar` |
| `rsmixin` | **2** (0.0%) | 2 | 1 GUI, 0 тултип. | `MCT-RS-Mixin-1.20.1-1.1.0-b420-release.jar` |
| `moreoverlays` | **2** (94.4%) | 36 | 4 GUI, 0 тултип. | `moreoverlays-1.22.7-mc1.20.2.jar` |
| `bobby` | **1** (95.0%) | 20 | 0 GUI, 6 тултип. | `bobby-1.20.1_v5.0.1.jar` |

---

## ⚙️ ТИР 3: Технические моды, API и неиспользуемые атрибуты
> **Приоритет: НИЗКИЙ / НЕ ТРЕБУЕТСЯ**. В JEI предметов не имеют, игроку напрямую не видны (стабы других модов, движок).

| Namespace | Не переведено | Всего строк | Тип данных | JAR-файл |
| :--- | :---: | :---: | :--- | :--- |
| `additional_attributes` | **429** (0.0%) | 429 | 428 атрибутов, 429 техн. строк | `additional_attributes-1.20.1-1.3.6-all.jar` |
| `ali` | **319** (0.0%) | 319 | 0 атрибутов, 319 техн. строк | `AdvancedLootInfo-forge-1.20.1-1.12.0.jar` |
| `entity_model_features` | **265** (8.9%) | 291 | 0 атрибутов, 265 техн. строк | `entity_model_features-3.2.4-1.20.1-forge.jar` |
| `fancymenu` | **251** (86.1%) | 1800 | 0 атрибутов, 251 техн. строк | `fancymenu_forge_3.7.0_MC_1.20.1.jar` |
| `journeymap` | **240** (68.4%) | 760 | 0 атрибутов, 240 техн. строк | `journeymap-1.20.1-5.10.3-forge.jar` |
| `controllable` | **215** (0.0%) | 215 | 0 атрибутов, 215 техн. строк | `controllable-forge-1.20.1-0.21.9.jar` |
| `portfolio` | **200** (0.0%) | 200 | 0 атрибутов, 200 техн. строк | `portfolio-1.20.1-1.5.0-forge.jar` |
| `createschematicchecker` | **183** (0.0%) | 183 | 0 атрибутов, 183 техн. строк | `CreateSchematicChecker-1.21.27-6.0-forge-1.20.1.jar` |
| `tooltipoverhaul` | **147** (2.6%) | 151 | 0 атрибутов, 147 техн. строк | `tooltipoverhaul-forge-1.20.1-1.5.0.jar` |
| `enchdesc` | **141** (23.0%) | 183 | 0 атрибутов, 141 техн. строк | `EnchantmentDescriptions-Forge-1.20.1-17.1.19.jar` |
| `ok_zoomer` | **135** (0.0%) | 135 | 0 атрибутов, 135 техн. строк | `ok_zoomer-forge-5.4.0-beta.8.jar` |
| `jeed` | **125** (37.5%) | 200 | 0 атрибутов, 125 техн. строк | `jeed-1.20-2.2.5.jar` |
| `ftbteams` | **90** (0.0%) | 90 | 0 атрибутов, 90 техн. строк | `ftb-teams-forge-2001.3.2.jar` |
| `maxenchantx` | **90** (0.0%) | 90 | 0 атрибутов, 90 техн. строк | `MaxEnchantX-1.20.X-1.3-Forge.jar` |
| `entity_texture_features` | **82** (73.5%) | 309 | 0 атрибутов, 82 техн. строк | `entity_texture_features_1.20.1-forge-7.1.jar` |
| `particlerain` | **71** (51.7%) | 147 | 0 атрибутов, 71 техн. строк | `particlerain-4.0.0-beta.10+1.20.1-forge.jar` |
| `dialog` | **67** (0.0%) | 67 | 0 атрибутов, 67 техн. строк | `SVDialog-0.6.jar` |
| `sodium` | **65** (0.0%) | 65 | 0 атрибутов, 65 техн. строк | `embeddium-0.3.31+mc1.20.1.jar` |
| `extremesoundmuffler` | **56** (0.0%) | 56 | 0 атрибутов, 56 техн. строк | `ExtremeSoundMuffler-3.48-forge-1.20.1.jar` |
| `gnetum` | **56** (0.0%) | 56 | 0 атрибутов, 56 техн. строк | `gnetum-2.4.6.jar` |
| `fallingtrees` | **42** (0.0%) | 42 | 0 атрибутов, 42 техн. строк | `fallingtrees-forge-mc1.20-0.13.2-SNAPSHOT.jar` |
| `drippyloadingscreen` | **41** (0.0%) | 41 | 0 атрибутов, 41 техн. строк | `drippyloadingscreen_forge_3.0.12_MC_1.20.1.jar` |
| `modernfix` | **37** (76.1%) | 155 | 0 атрибутов, 37 техн. строк | `modernfix-forge-5.27.72+mc1.20.1.jar` |
| `balm` | **35** (0.0%) | 35 | 0 атрибутов, 35 техн. строк | `balm-forge-1.20.1-7.3.38-all.jar` |
| `createentitycontrol` | **31** (0.0%) | 31 | 0 атрибутов, 31 техн. строк | `CreateEntityControl-0.3.8.4-6.0-forge-1.20.1.jar` |
| `passablefoliage` | **26** (0.0%) | 26 | 0 атрибутов, 26 техн. строк | `PassableFoliage-1.20.1-forge-8.2.1.jar` |
| `trashslot` | **24** (0.0%) | 24 | 0 атрибутов, 24 техн. строк | `trashslot-forge-1.20.1-15.1.3.jar` |
| `colorwheel` | **22** (0.0%) | 22 | 0 атрибутов, 22 техн. строк | `colorwheel-forge-1.2.9+mc1.20.1.jar` |
| `armorstatues` | **21** (0.0%) | 21 | 0 атрибутов, 21 техн. строк | `ArmorStatues-v8.0.6-1.20.1-Forge.jar` |
| `emojiful` | **21** (0.0%) | 21 | 0 атрибутов, 21 техн. строк | `Emojiful-Forge-1.20.1-4.2.0.jar` |
| `ftbchunks` | **20** (92.9%) | 282 | 0 атрибутов, 20 техн. строк | `ftb-chunks-forge-2001.3.6.jar` |
| `sdrp` | **20** (0.0%) | 20 | 0 атрибутов, 20 техн. строк | `SimpleDiscordRichPresence-forge-4.0.3-build.40+mc1.20.1.jar` |
| `colorfulhearts` | **17** (0.0%) | 17 | 0 атрибутов, 17 техн. строк | `colorfulhearts-forge-1.20.1-4.3.16.jar` |
| `sodiumdynamiclights` | **15** (55.9%) | 34 | 0 атрибутов, 15 техн. строк | `sodiumdynamiclights-forge-1.0.10-1.20.1.jar` |
| `polylib` | **13** (0.0%) | 13 | 0 атрибутов, 13 техн. строк | `polylib-forge-2000.0.3-build.143.jar` |
| `irons_rpg_tweaks` | **12** (0.0%) | 12 | 0 атрибутов, 12 техн. строк | `irons_rpg_tweaks-1.20-1.4.0.jar` |
| `bwncr` | **11** (0.0%) | 11 | 0 атрибутов, 11 техн. строк | `bwncr-forge-1.20.1-3.17.2.jar` |
| `quality_food` | **11** (26.7%) | 15 | 0 атрибутов, 11 техн. строк | `quality_food-1.20.1-2.4.3-all.jar` |
| `creeperconfetti` | **9** (0.0%) | 9 | 0 атрибутов, 9 техн. строк | `creeperconfetti-4.3.jar` |
| `resourcepackoverrides` | **9** (0.0%) | 9 | 0 атрибутов, 9 техн. строк | `ResourcePackOverrides-v8.0.3-1.20.1-Forge.jar` |
| `shippingbin` | **9** (0.0%) | 9 | 5 атрибутов, 9 техн. строк | `ShippingBin-forge-1.20.1-4.jar` |
| `betteradvancedtooltips` | **8** (0.0%) | 8 | 0 атрибутов, 8 техн. строк | `betteradvancedtooltips-1.20.1-1.2.1.jar` |
| `fusion` | **8** (0.0%) | 8 | 0 атрибутов, 8 техн. строк | `fusion-1.2.11c-forge-mc1.20.1.jar` |
| `embeddium` | **7** (0.0%) | 7 | 0 атрибутов, 7 техн. строк | `embeddium-0.3.31+mc1.20.1.jar` |
| `sereneseasonsfix` | **7** (0.0%) | 7 | 0 атрибутов, 7 техн. строк | `sereneseasonsfix-1.20.1-1.2.0.jar` |
| `easy_npc_example` | **6** (0.0%) | 6 | 0 атрибутов, 6 техн. строк | `easy_npc-forge-1.20.1-6.1.0.jar` |
| `jadeaddons` | **6** (83.3%) | 36 | 0 атрибутов, 6 техн. строк | `JadeAddons-1.20.1-Forge-5.5.0.jar` |
| `loot_journal` | **6** (95.5%) | 134 | 0 атрибутов, 6 техн. строк | `loot_journal-forge-1.20.1-6.1.2.jar` |
| `midnightlib` | **6** (53.8%) | 13 | 0 атрибутов, 6 техн. строк | `midnightlib-forge-1.9.2+1.20.1.jar` |
| `iris` | **6** (91.7%) | 72 | 0 атрибутов, 6 техн. строк | `oculus-mc1.20.1-1.8.0.jar` |
| `simplemagnets` | **5** (86.8%) | 38 | 0 атрибутов, 5 техн. строк | `simplemagnets-1.1.12-forge-mc1.20.1.jar` |
| `bookshelf` | **4** (87.5%) | 32 | 0 атрибутов, 4 техн. строк | `Bookshelf-Forge-1.20.1-20.2.13.jar` |
| `crashutilities` | **4** (0.0%) | 4 | 0 атрибутов, 4 техн. строк | `crashutilities-8.1.4.jar` |
| `balloonbox` | **3** (0.0%) | 3 | 0 атрибутов, 3 техн. строк | `BalloonBox1.20.1(Forge)vs.1.0.3.jar` |
| `cloth-config2` | **3** (93.9%) | 49 | 0 атрибутов, 3 техн. строк | `cloth-config-11.1.136-forge.jar` |
| `findme` | **3** (25.0%) | 4 | 0 атрибутов, 3 техн. строк | `findme-3.2.3-forge.jar` |
| `ftbbackups` | **3** (0.0%) | 3 | 0 атрибутов, 3 техн. строк | `ftbbackups2-forge-1.20-1.0.23.jar` |
| `easyanvils` | **2** (0.0%) | 2 | 0 атрибутов, 2 техн. строк | `EasyAnvils-v8.0.2-1.20.1-Forge.jar` |
| `example_mod` | **2** (0.0%) | 2 | 0 атрибутов, 2 техн. строк | `missingmodschecker-forge-1.0.1-1.20.1.jar` |
| `puffish_attributes` | **2** (93.5%) | 31 | 31 атрибутов, 2 техн. строк | `puffish_attributes-0.7.2-1.20-forge.jar` |
| `betteradvancements` | **1** (0.0%) | 1 | 0 атрибутов, 1 техн. строк | `BetterAdvancements-Forge-1.20.1-0.4.2.10.jar` |
| `bots_lib` | **1** (0.0%) | 1 | 0 атрибутов, 1 техн. строк | `bots_lib-4.1.jar` |
| `carryon` | **1** (91.7%) | 12 | 0 атрибутов, 1 техн. строк | `carryon-forge-1.20.1-2.1.2.7.jar` |
| `chat_heads` | **1** (96.0%) | 25 | 0 атрибутов, 1 техн. строк | `chat_heads-0.13.7-forge-1.20.jar` |
| `enchantmentdisabletag` | **1** (0.0%) | 1 | 0 атрибутов, 1 техн. строк | `enchantmentdisabletag-forge-1.1.0+1.20.1.jar` |
| `entityjs` | **1** (0.0%) | 1 | 0 атрибутов, 1 техн. строк | `entityjs-0.6.6-1.20.1.jar` |
| `fragmentum` | **1** (0.0%) | 1 | 0 атрибутов, 1 техн. строк | `fragmentum-forge-1.20.1-1.1.4.jar` |
| `framework` | **1** (0.0%) | 1 | 0 атрибутов, 1 техн. строк | `framework-forge-1.20.1-0.7.15.jar` |
| `jmi` | **1** (0.0%) | 1 | 0 атрибутов, 1 техн. строк | `jmi-forge-1.20.1-0.14-48.jar` |
| `pandalib` | **1** (0.0%) | 1 | 0 атрибутов, 1 техн. строк | `pandalib-forge-mc1.20-0.5.2-SNAPSHOT.jar` |
| `placebo` | **1** (83.3%) | 6 | 0 атрибутов, 1 техн. строк | `Placebo-1.20.1-8.6.3.jar` |
| `toastcontrol` | **1** (50.0%) | 2 | 0 атрибутов, 1 техн. строк | `ToastControl-1.20.1-8.0.3.jar` |
| `zeta` | **1** (50.0%) | 2 | 0 атрибутов, 1 техн. строк | `Zeta-1.0-31.jar` |
