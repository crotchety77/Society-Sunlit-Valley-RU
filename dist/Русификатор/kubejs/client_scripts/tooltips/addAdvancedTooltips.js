const getDynamicPlushieCondition = (typeIndex, quality) => {
    let q = (typeof quality === "number" && !isNaN(quality)) ? Math.max(0, Math.min(3, quality)) : 0;
    let mult = q + 1; // 1, 2, 3, 4

    switch (typeIndex) {
        case 0: // aquatic
            return `§6${5 * mult}% шанс добыть желе [Речное / Океаническое]`;
        case 1: // woodsy
            return [
                `§6Добывает древесину: ${8 * mult} шт. §7Требуются брёвна в радиусе 3 [Область: 7x7x7]`,
                `§7Брёвна не разрушаются`
            ];
        case 2: // eldritch
            return `§6Добывает ${1 * mult} шт. сырого серебра при сборе`;
        case 3: // wrathful
            return `§6Добывает ${3 * mult} шт. сырого свинца при сборе`;
        case 4: // sommelier
            return `§6${25 * mult}% шанс сделать продукт ремесленным`;
        case 5: // sunlit
            return `§6${5 * mult}% шанс добыть Солнечный кристалл`;
        case 6: // hungry
            return `§6${10 * mult}% шанс повторно собрать продукцию в тот же день`;
        case 7: // anxious
            return `§6+${25 * mult}% к базовому шансу редкого сбора`;
        case 8: // shy
            let radius = 3 - q;
            let side = radius * 2 + 1;
            return radius === 0
                ? `§6Двойная продукция: гарантировано`
                : `§6Двойная продукция: нет других игрушек в радиусе ${radius} [Область: ${side}x${side}x${side}]`;
        case 9: // cheerful
            let reqOtherToys = 28 - 4 * mult; // total count > (28 - 4*mult) -> other toys >= (28 - 4*mult)
            return `§6Двойная продукция: требуется от ${reqOtherToys} других игрушек рядом [Область: 5x5x5]`;
        case 10: // chill
            return `§6Добывает ${1 * mult} шт. безупречных алмазов при сборе`;
        case 11: // machiavellian
            return `§6Добывает ${1 * mult} шт. иридиевого лома при сборе`;
        case 12: // cutesy
            return `§6Добывает ${1 * mult} шт. коробок с мебелью при сборе`;
        case 13: // fashionista
            let reqFurniture = 28 - 4 * mult; // count >= T
            return `§6Двойная продукция: требуется от ${reqFurniture} мебели рядом [Область: 5x5x5]`;
        case 14: // neutral
        default:
            return `§6${10 * mult}% шанс получить в 2 раза больше продукции`;
    }
};

ItemEvents.tooltip((tooltip) => {
    global.plushies.forEach((plush) => {
        tooltip.addAdvanced(plush, (item, advanced, text) => {
            if (item.nbt) {
                let rawType = item.nbt.getInt("type");
                let typeIndex = (typeof rawType === "number" && rawType >= 0 && rawType < global.plushieTraits.length) ? rawType : 14;
                let type = global.plushieTraits[typeIndex] || global.plushieTraits[14];
                let quality = 0;
                if (item.nbt.getCompound("quality_food")) {
                    quality = item.nbt.getCompound("quality_food").getInt("quality");
                    if (isNaN(quality) || quality < 0) quality = 0;
                    if (quality > 3) quality = 3;
                }

                if (tooltip.shift) {
                    text.add(1, [
                        Text.translatable("tooltip.society.plushies.trait"),
                        global.getTranslatedTextWithColorCode(
                            type.color,
                            `society.item.plushie.${type.trait}`
                        ),
                    ]);
                    text.add(2, [
                        Text.translate(`society.item.plushie.trait.description`).darkGray(),
                    ]);
                    let conditionLines = getDynamicPlushieCondition(typeIndex, quality);
                    if (Array.isArray(conditionLines)) {
                        conditionLines.forEach((line, idx) => {
                            text.add(3 + idx, [Text.of(line)]);
                        });
                    } else {
                        text.add(3, [Text.of(conditionLines)]);
                    }
                } else {
                    if (item.nbt.getCompound("quality_food"))
                        text.add(1, [
                            Text.translatable("tooltip.society.plushies.rarity"),
                            Text.gold(
                                "★".repeat(
                                    item.nbt.getCompound("quality_food").getInt("quality") + 1
                                )
                            ),
                            Text.gray(
                                "☆".repeat(
                                    3 - item.nbt.getCompound("quality_food").getInt("quality")
                                )
                            ),
                        ]);
                    else text.add(1, [Text.gray("☆".repeat(4))]);
                    let affection = item.nbt.getInt("affection");
                    text.add(2, [
                        Text.translatable("tooltip.society.plushies.affection"),
                        `§c${affection > 0 ? `❤`.repeat(affection) : ""}§7${affection < 4 ? `❤`.repeat(4 - affection) : ""
                        }`,
                    ]);
                    text.add(3, [
                        Text.translatable("tooltip.society.plushies.trait"),
                        global.getTranslatedTextWithColorCode(
                            type.color,
                            `society.item.plushie.${type.trait}`
                        ),
                        Text.of(" "),
                        Text.translatable(
                            "tooltip.society.hold_key",
                            global.getTranslatedTextWithColorCode(
                                type.color,
                                "key.keyboard.shift"
                            )
                        ).gray(),
                    ]);
                    if (item.nbt.animal) {
                        let animal = item.nbt.getCompound("animal");
                        text.add(4, [
                            Text.translatable("tooltip.society.plushies.animal_type"),
                            global.getTranslatedEntityName(String(animal.type)).gold(),
                        ]);
                        if (animal.name) {
                            text.add(5, [
                                Text.translatable("tooltip.society.plushies.animal_name"),
                                `§6${String(animal.name)}`,
                            ]);
                        }
                    } else {
                        text.add(4, [Text.translatable("tooltip.society.plushies")]);
                    }
                }
            } else {
                text.add(1, [Text.translatable("tooltip.society.plushies")]);
            }
        });
    });
    tooltip.addAdvanced("society:villager_invitation", (item, advanced, text) => {
        if (item.nbt) {
            text.add(
                1,
                Text.translatable(
                    "block.society.fish_pond.fish.type",
                    `${item.nbt.get("type")}`
                ).aqua()
            );
            text.add(
                2,
                Text.translatable("block.society.fish_pond.description").gray()
            );
        } else {
            text.add(
                1,
                Text.translatable("block.society.fish_pond.description").gray()
            );
        }
    });
    tooltip.addAdvanced("society:villager_home", (item, advanced, text) => {
        if (item.nbt) {
            text.add(
                1,
                Text.translatable(
                    "block.society.villager_home.type",
                    `${item.nbt.getString("type")}`
                ).green()
            );
            text.add(
                2,
                Text.translatable("block.society.villager_home.description").gray()
            );
        } else {
            text.add(
                1,
                Text.translatable("block.society.villager_home.description").gray()
            );
        }
    });
    tooltip.addAdvanced("society:fish_pond", (item, advanced, text) => {
        if (item.nbt) {
            text.add(
                1,
                Text.translatable(
                    "block.society.fish_pond.fish.type",
                    `${Item.of(item.nbt.get("type")).id}`
                ).aqua()
            );
            text.add(
                2,
                Text.translatable(
                    "block.society.fish_pond.fish.population",
                    `${item.nbt.get("population")}`,
                    `${item.nbt.get("max_population")}`
                ).aqua()
            );
        } else {
            text.add(
                1,
                Text.translatable("block.society.fish_pond.description").gray()
            );
            text.add(
                2,
                Text.translatable(
                    "block.society.fish_pond.description.place"
                ).darkAqua()
            );
        }
    });
    tooltip.addAdvanced("society:caterpillar_eggs", (item, advanced, text) => {
        if (item.nbt) {
            text.add(
                1,
                Text.translatable("item.society.caterpillar_eggs.description").darkGray()
            );
            text.add(
                2,
                Text.translatable(
                    "item.society.caterpillar_eggs.longwing.type",
                    Text.translatable(`item.longwings.${item.nbt.getString("child")}`).gray()
                ).green()
            );
            text.add(
                3,
                Text.translatable(
                    "item.society.caterpillar_eggs.longwing.parents",
                    Text.translatable(`item.longwings.${item.nbt.getString("parent")}`).gray(),
                    Text.translatable(`item.longwings.${item.nbt.getString("coparent")}`).gray()
                ).lightPurple()
            );
            text.add(
                4,
                Text.translatable(
                    "item.society.caterpillar_eggs.longwing.size",
                    `${item.nbt.getDouble("size")}`
                ).darkGray()
            );
        } else {
            text.add(
                1,
                Text.translatable("item.society.caterpillar_eggs.description").gray()
            );
        }
    });
    // Sometimes season just breaks for the tooltip and I have no idea why
    tooltip.addAdvanced("farmersdelight:tomato_seeds", (item, advanced, text) => {
        if (tooltip.shift) {
            text.add(1, [
                Text.white("")
                    .append(Text.translatable("desc.sereneseasons.fertile_seasons"))
                    .append(":"),
                Text.of(" "),
                Text.translatable("desc.sereneseasons.spring").green().append(","),
                Text.of(" "),
                Text.translatable("desc.sereneseasons.summer").yellow().append(","),
                Text.of(" "),
                Text.translatable("desc.sereneseasons.autumn").gold(),
            ]);
        } else {
            text.add(1, [
                Text.translatable(
                    "tooltip.society.hold_key",
                    Text.translatable("key.keyboard.shift").gray()
                ).darkGray(),
            ]);
        }
    });
    tooltip.addAdvanced(
        "farm_and_charm:strawberry_seed",
        (item, advanced, text) => {
            if (tooltip.shift) {
                text.add(1, [
                    Text.white("")
                        .append(Text.translatable("desc.sereneseasons.fertile_seasons"))
                        .append(":"),
                    Text.of(" "),
                    Text.translatable("desc.sereneseasons.spring").green(),
                ]);
            } else {
                text.add(1, [
                    Text.translatable(
                        "tooltip.society.hold_key",
                        Text.translatable("key.keyboard.shift").gray()
                    ).darkGray(),
                ]);
            }
        }
    );

    const magnifyingBlocks = [
        Text.translatable("block.society.auto_grabber"),
        Text.translatable("block.society.artisan_hopper"),
        Text.translatable("block.farmingforblockheads.chicken_nest"),
        Text.translatable("block.society.feeding_trough"),
        Text.translatable("block.splendid_slimes.slime_feeder"),
        Text.translatable("block.society.snow_melter"),
        Text.translatable("block.society.fish_pond_basket"),
        Text.translatable("block.society.fish_pond_hatchery"),
        Text.translatable("block.society.golden_clock"),
        Text.translatable("block.society.mana_clock"),
        Text.translatable("block.society.mana_milker"),
        Text.translatable("item.society.magnifying_glass.description.view_block.sprinklers"),
        Text.translatable("block.society.growth_obelisk"),
        Text.translatable("block.society.ribbit_hut"),
        Text.translatable("block.society.fish_pond_manager"),
    ];
    tooltip.addAdvanced("society:magnifying_glass", (item, advanced, text) => {
        if (tooltip.shift) {
            magnifyingBlocks.forEach((block, index) => {
                text.add(index + 1, Text.gold(block));
            });
        } else {
            text.add(
                1,
                Text.translatable("item.society.magnifying_glass.description").green()
            );
            text.add(2, [
                Text.translatable(
                    "item.society.magnifying_glass.description.view_block",
                    Text.translatable("key.keyboard.shift").gray()
                ).darkGray(),
            ]);
        }
    });
    tooltip.addAdvanced("society:car_key", (item, advanced, text) => {
        text.add(1, [Text.translatable("item.society.car_key.description").gray()]);
        if (item.nbt) {
            text.add(2, [
                Text.translatable("item.society.car_key.description.parked").green(),
            ]);
        } else {
            text.add(2, [
                Text.translatable("item.society.car_key.description.empty").red(),
            ]);
        }
    });
    const getPigColoredName = (pig) => {
        switch (pig) {
            case "Red":
                return Text.translatable("society.pig_race.red_pig").red();
            case "Blue":
                return Text.translatable("society.pig_race.blue_pig").blue();
            case "Yellow":
                return Text.translatable("society.pig_race.yellow_pig").yellow();
            case "Green":
                return Text.translatable("society.pig_race.green_pig").green();
            default:
                console.log(`Invalid pig color`);
        }
        return Text.of(`${pig}`);
    };
    tooltip.addAdvanced(
        ["society:pig_race_ticket", "society:multiplayer_pig_race_ticket"],
        (item, advanced, text) => {
            text.add(1, [
                Text.translatable("item.society.pig_race_ticket.description").gray(),
            ]);
            if (item.nbt) {
                text.add(2, [
                    Text.translatable(
                        "item.society.pig_race_ticket.description.bet",
                        getPigColoredName(item.nbt.bet)
                    ).gray(),
                ]);
            } else {
                text.add(2, [
                    Text.translatable(
                        "item.society.pig_race_ticket.description.no_pig"
                    ).gray(),
                ]);
            }
        }
    );
    global.ageableProductInputs.forEach((product) => {
        const splitProduct = product.item.split(":");
        tooltip.addAdvanced(`society:aged_${splitProduct[1]}`, (item, advance, text) => {
            if (product.item === "brewery:whiskey_maggoallan" || product.item === "brewery:whiskey_smokey_reverie")
                text.set(0, text.get(0).copy().gold())
            else
                text.set(0, text.get(0).copy().aqua());
        });
        tooltip.addAdvanced(`society:double_aged_${splitProduct[1]}`, (item, advance, text) => {
            if (product.item === "brewery:whiskey_maggoallan" || product.item === "brewery:whiskey_smokey_reverie")
                text.set(0, text.get(0).copy().gold())
            else
                text.set(0, text.get(0).copy().darkAqua());
        });
    });
});
