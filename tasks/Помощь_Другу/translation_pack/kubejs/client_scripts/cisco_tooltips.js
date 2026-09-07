// =========================================================================
// Полная локализация подсказок и уникальных способностей Cisco's Mod (KubeJS)
// Путь в сборке: kubejs/client_scripts/cisco_tooltips.js
// Перезагрузка в игре: F3 + T (или /kubejs reload client_scripts)
// =========================================================================

ItemEvents.tooltip(tooltip => {

    /**
     * Вспомогательная функция: полностью удаляет зашитый английский текст из Java-классов
     * и вставляет чистый русский перевод под названием предмета.
     */
    function setCiscoTooltip(items, lines) {
        let itemArray = Array.isArray(items) ? items : [items];
        itemArray.forEach(id => {
            tooltip.addAdvanced(id, (item, advanced, text) => {
                // Оставляем только заголовок (индекс 0), всё старое английское удаляем
                while (text.size() > 1) {
                    text.remove(1);
                }
                // Добавляем наши переведённые строки
                lines.forEach(line => {
                    text.add(line);
                });
            });
        });
    }

    // ==========================================
    // 1. ЛЕГЕНДАРНОЕ ОРУЖИЕ И ИНСТРУМЕНТЫ
    // ==========================================

    // Глациес (Glacies)
    setCiscoTooltip('cisco_mod:glacies', [
        Text.lightPurple('Легендарный топор, передаваемый вождями ледяного племени из поколения в поколение.'),
        Text.gold('[Уникальный эффект]: Укус Глациеса:'),
        Text.white('Замедляет противников при попадании.'),
        Text.green('[Способность на ПКМ]: Погребение:'),
        Text.white('Заковывает броню в ледяной панцирь, даруя мощный прирост к защите, но накладывая замедление.')
    ]);

    // Дремлющее Равновесие (Slumbering Equillibrium)
    setCiscoTooltip('cisco_mod:slumbering_equillibrium', [
        Text.darkPurple('Этот легендарный клинок спит без Божественного рубина в качестве источника силы.')
    ]);

    // Пробуждённое Равновесие (Awakened Equillibrium)
    setCiscoTooltip(['cisco_mod:equillibrium', 'cisco:equillibrium'], [
        Text.darkPurple('Легендарный клинок равновесия. Некогда принадлежал великому герою.'),
        Text.gold('[Уникальный эффект] Равновесие:'),
        Text.white('Наносит 4% от макс. здоровья цели в виде чистого урона.'),
        Text.green('[Способность на ПКМ]:'),
        Text.white('Высвобождает волну энергии равновесия.')
    ]);

    // Очищенное Равновесие (Refined Equillibrium)
    setCiscoTooltip('cisco_mod:refined_equillibrium', [
        Text.gold('[Уникальный эффект] Стремительное Равновесие:'),
        Text.white('Наносит 2% от макс. здоровья цели в виде чистого урона.'),
        Text.green('[Способность на ПКМ]:'),
        Text.white('Совершает быстрый рывок и серию ударов.')
    ]);

    // Абсолютное Равновесие (Absolute Equillibrium)
    setCiscoTooltip('cisco_mod:absolute_equillibrium', [
        Text.darkPurple('Легендарный клинок равновесия, наполненный священным светом.'),
        Text.gold('[Уникальный эффект] Абсолютное Равновесие:'),
        Text.white('Наносит 4% от макс. здоровья цели чистым уроном и снижает получаемый урон на 15%.'),
        Text.green('[Способность на ПКМ]:'),
        Text.white('Призывает священные мечи правосудия.')
    ]);

    // Найтфолл (Nightfall)
    setCiscoTooltip('cisco_mod:nightfall', [
        Text.gold('[Уникальный эффект]:'),
        Text.white('Наносит 2% от макс. здоровья цели чистым уроном и сокрушительный урон целям с менее 25% HP.'),
        Text.green('[Способность на ПКМ]:'),
        Text.white('Повышает урон и скорость атаки, но накладывает иссушение на владельца.')
    ]);

    // Высший Найтфолл (Supreme Nightfall)
    setCiscoTooltip('cisco_mod:supreme_nightfall', [
        Text.darkPurple('Легендарный меч равновесия, осквернённый абсолютной тьмой.'),
        Text.gold('[Уникальный эффект] Высшее Равновесие:'),
        Text.white('Наносит 6% от макс. здоровья цели чистым уроном. Если находится в инвентаре (не в руке) — переходит в режим эгиды.'),
        Text.green('[Способность на ПКМ]:'),
        Text.white('Устанавливает здоровье на 50%, даруя колоссальный бонус к урону, скорости передвижения и атаки.')
    ]);

    // Падший Рагнарёк (Fell Ragnarok)
    setCiscoTooltip('cisco_mod:fell_ragnarok', [
        Text.gold('[Уникальный эффект]: Рагнарёк:'),
        Text.white('Наносит дополнительный урон, полностью игнорирующий броню.'),
        Text.gold('[Уникальный эффект]: Фенсалир:'),
        Text.white('Накладывает слабость на врагов при попадании.')
    ]);

    // Адское клеймо (Hellbrand)
    setCiscoTooltip('cisco_mod:hellbrand', [
        Text.darkPurple('Легендарное оружие 2-го Падшего короля Бьёрна.'),
        Text.gold('[Уникальный эффект] Адское клеймо:'),
        Text.white('Накладывает на цели адское клеймо, утраивая наносимый этим оружием урон.'),
        Text.green('[Способность на ПКМ]:'),
        Text.white('Если HP > 50%: дарует временный бонус к атаке от 60% брони. Если HP < 50%: дарует 5 сек. неуязвимости.')
    ]);

    // Ледяной клык (Frostfang)
    setCiscoTooltip('cisco_mod:frostfang', [
        Text.darkPurple('Легендарное оружие 3-го Падшего короля Сильви.'),
        Text.gold('[Уникальный эффект] Величие Серебряного Волка:'),
        Text.white('Вражеские атаки не могут отнять более 40% от вашего максимального здоровья за удар.'),
        Text.green('[Способность на ПКМ]:'),
        Text.white('Призывает ледяные клыки из-под земли.')
    ]);

    // Раскалыватель небес (Skysplitter)
    setCiscoTooltip('cisco_mod:skysplitter', [
        Text.gold('[Уникальный эффект] Благословение ветра:'),
        Text.white('Полностью нейтрализует урон от падения и дарует усиленный прыжок в основной руке.'),
        Text.green('[Способность на ПКМ]:'),
        Text.white('Совершает сокрушительный выпад с вращением копья.')
    ]);

    // Кастор и Поллукс (Castor & Pollux)
    setCiscoTooltip('cisco_mod:castor', [
        Text.gold('[Уникальный эффект] Близнецовая порча:'),
        Text.white('Поражённые враги получают эффект порчи, наносящий периодический урон сквозь броню.')
    ]);
    setCiscoTooltip('cisco_mod:pollux', [
        Text.gold('[Уникальный эффект] Неразлучные:'),
        Text.white('Если Кастор во второй руке: дарует +30% к урону и скорости атаки. Иначе — накладывает замедление.')
    ]);

    // Судия (Adjudicator)
    setCiscoTooltip('cisco_mod:adjudicator', [
        Text.gold('[Уникальный эффект]: Божественное правосудие:'),
        Text.white('Наносит огромный дополнительный урон целям с уровнем здоровья ниже 20%.'),
        Text.green('[Способность на ПКМ]:'),
        Text.white('Обрушивает небесный луч правосудия.')
    ]);

    // Лазурный гром (Azure Thunder)
    setCiscoTooltip('cisco_mod:azure_thunder', [
        Text.gold('[Уникальный эффект]: Лазурный суд:'),
        Text.white('Поражает врагов электрическими разрядами при ударе.'),
        Text.green('[Способность на ПКМ]:'),
        Text.white('Призывает шторм молний вокруг владельца.')
    ]);

    // Кирки
    setCiscoTooltip('cisco_mod:bright_pickaxe', [
        Text.lightPurple('Безупречная кирка из сплава сияющей стали. Увеличивает скорость копания при использовании.')
    ]);
    setCiscoTooltip('cisco_mod:dark_pickaxe', [
        Text.darkPurple('Кирка из древнейших материалов. Значительно увеличивает скорость копания при использовании.')
    ]);

    // ==========================================
    // 2. РЕЛИКВИИ, АМУЛЕТЫ И АРТЕФАКТЫ
    // ==========================================

    setCiscoTooltip('cisco_mod:band_of_brilliance', [
        Text.lightPurple('Легендарное кольцо, вручаемое при достижении ранга мудреца в Ордене Совы.'),
        Text.white('Дарует +20% к здоровью и броне при ношении.')
    ]);
    setCiscoTooltip('cisco_mod:amuletof_luck', [
        Text.white('Дарует +5 к удаче при ношении.')
    ]);
    setCiscoTooltip('cisco_mod:amuletof_vitality', [
        Text.white('Дарует +10 к максимальному здоровью при ношении.')
    ]);
    setCiscoTooltip('cisco_mod:amuletof_swim_speed', [
        Text.white('Дарует +20% к скорости плавания при ношении.')
    ]);
    setCiscoTooltip('cisco_mod:beltof_bracing', [
        Text.white('Дарует +50% к сопротивлению отбрасыванию при ношении.')
    ]);
    setCiscoTooltip('cisco_mod:crownofthe_emperor', [
        Text.white('Дарует +6 к броне при ношении.')
    ]);
    setCiscoTooltip('cisco_mod:crown_of_debilitating_desire', [
        Text.red('Снижает наносимый урон, броню, скорость и макс. HP на 80%.')
    ]);
    setCiscoTooltip('cisco_mod:dark_charm', [
        Text.white('При HP > 80%: постоянно наносит урон владельцу.'),
        Text.gold('При HP < 80%: дарует бонус к атаке, скорости, броне и стойкости брони.')
    ]);
    setCiscoTooltip('cisco_mod:unattuned_core', [
        Text.gray('Особое ядро, восприимчивое к силе стихий. Может принимать любую форму по воле владельца, являясь идеальной основой для могущественного снаряжения.')
    ]);

    // ==========================================
    // 3. КОМПЛЕКТЫ ДОСПЕХОВ
    // ==========================================

    // Доспехи верховного вознесённого (Sovereign Ascendant)
    setCiscoTooltip([
        'cisco_mod:sovereign_ascendant_helmet',
        'cisco_mod:sovereign_ascendant_chestplate',
        'cisco_mod:sovereign_ascendant_leggings',
        'cisco_mod:sovereign_ascendant_boots'
    ], [
        Text.gold('★ Бонус комплекта Верховного вознесённого:'),
        Text.white('• Дарует +40% HP; при HP > 50%: увеличивает атаку на 60% от макс. HP, а скорость бега и атаки на +20%.'),
        Text.white('• При HP > 50%: снижает весь входящий урон на 70%.'),
        Text.green('• [Клавиша X]: Увеличивает гравитацию врагов в 10 раз и снижает свою. Отматывает время к моменту полного здоровья.')
    ]);

    // Доспехи нисшедшего героя (Descended Hero)
    setCiscoTooltip([
        'cisco_mod:descended_hero_helmet',
        'cisco_mod:descended_hero_chestplate',
        'cisco_mod:descended_hero_leggings',
        'cisco_mod:descended_hero_boots'
    ], [
        Text.gold('★ Бонус комплекта Нисшедшего героя:'),
        Text.white('• Защита возрастает при падении HP (до 70% снижения урона при 50% HP).'),
        Text.white('• Увеличивает броню на +70% и повышает урон на 100% от значения брони.'),
        Text.green('• [Клавиша X]: Устанавливает HP на 50% и дарует 6 секунд полной неуязвимости.')
    ]);

    // Доспехи павшего героя (Fallen Hero)
    setCiscoTooltip([
        'cisco_mod:fallen_hero_armor_helmet',
        'cisco_mod:fallen_hero_armor_chestplate',
        'cisco_mod:fallen_hero_armor_leggings',
        'cisco_mod:fallen_hero_armor_boots'
    ], [
        Text.gold('★ Бонус комплекта Павшего героя:'),
        Text.white('• При HP < 80%: активирует ауру павшего героя.'),
        Text.green('• [Клавиша X]: Снимает эффекты иссушения и отравления, восстанавливая здоровье.')
    ]);

    // Доспехи Падшего короля (Fell King)
    setCiscoTooltip([
        'cisco_mod:fell_king_armor_helmet',
        'cisco_mod:fell_king_armor_chestplate',
        'cisco_mod:fell_king_armor_leggings',
        'cisco_mod:fell_king_armor_boots'
    ], [
        Text.gold('[Уникальный эффект]: Броккр:'),
        Text.white('Снижает весь получаемый урон на 25%.'),
        Text.gold('[Уникальный эффект]: Сёкквабеккр:'),
        Text.white('Отражает 30% полученного урона обратно в атакующего.')
    ]);

    // Доспехи орла (Gilded Eagle)
    setCiscoTooltip([
        'cisco_mod:gilded_eagle_helmet',
        'cisco_mod:gilded_eagle_chestplate',
        'cisco_mod:gilded_eagle_leggings',
        'cisco_mod:gilded_eagle_boots'
    ], [
        Text.green('[Способность]: Сверхъестественные рефлексы [Клавиша X]:'),
        Text.white('Позволяет уклоняться от всех входящих атак в течение 3 секунд.')
    ]);

    // Доспехи тёмной стали (Darksteel Armor)
    setCiscoTooltip([
        'cisco_mod:darksteel_armor_helmet',
        'cisco_mod:darksteel_armor_chestplate',
        'cisco_mod:darksteel_armor_leggings',
        'cisco_mod:darksteel_armor_boots'
    ], [
        Text.gold('★ Защита от гибели (1 раз в 5 мин):'),
        Text.white('Если полученный урон смертелен, оставляет 10 HP и дарует 3 секунды неуязвимости.')
    ]);

    // Доспехи сияющей стали (Brightsteel Armor)
    setCiscoTooltip([
        'cisco_mod:brightsteel_helmet',
        'cisco_mod:brightsteel_chestplate',
        'cisco_mod:brightsteel_leggings',
        'cisco_mod:brightsteel_boots'
    ], [
        Text.white('При уровне здоровья выше 80% дарует постоянный эффект сопротивления урону.')
    ]);

    // Доспехи Бьёрна и Сильви (Bjorn & Sylvi)
    setCiscoTooltip([
        'cisco_mod:bjorn_helmet',
        'cisco_mod:bjorn_chestplate',
        'cisco_mod:bjorn_leggings',
        'cisco_mod:bjorn_boots'
    ], [
        Text.white('Снижает входящий урон на 20% и увеличивает броню на +10%.')
    ]);
    setCiscoTooltip([
        'cisco_mod:sylvi_helmet',
        'cisco_mod:sylvi_chestplate',
        'cisco_mod:sylvi_leggings',
        'cisco_mod:sylvi_boots'
    ], [
        Text.white('Снижает входящий урон на 20% и увеличивает максимальное здоровье на +10%.')
    ]);

    // Доспехи ветрохода (Windwalker)
    setCiscoTooltip([
        'cisco_mod:test_helmet',
        'cisco_mod:test_chestplate',
        'cisco_mod:test_leggings',
        'cisco_mod:test_boots'
    ], [
        Text.aqua('★ Сила ветра:'),
        Text.white('Позволяет совершать прыжок в воздухе по нажатию [Пробел], накладывая плавное падение.')
    ]);

    // Алые и Фиолетовые вознесённые доспехи (Ascended Rouge / Violet)
    setCiscoTooltip([
        'cisco_mod:ascended_hero_rouge_helmet',
        'cisco_mod:ascended_hero_rouge_chestplate',
        'cisco_mod:ascended_hero_rouge_leggings',
        'cisco_mod:ascended_hero_rouge_boots'
    ], [
        Text.gold('★ Бонус комплекта Алого вознесённого:'),
        Text.white('• При HP > 50%: дарует +80% к боевым и защитным характеристикам.'),
        Text.white('• Спасает от смертельного урона (раз в 10 мин) и снижает входящий урон вдвое.'),
        Text.green('• [Клавиша X]: Дарует мощное сопротивление урону союзникам поблизости.')
    ]);
    setCiscoTooltip([
        'cisco_mod:ascended_hero_violet_helmet',
        'cisco_mod:ascended_hero_violet_chestplate',
        'cisco_mod:ascended_hero_violet_leggings',
        'cisco_mod:ascended_hero_violet_boots'
    ], [
        Text.gold('★ Бонус комплекта Фиолетового вознесённого:'),
        Text.white('• При HP > 50%: дарует +80% к боевым и защитным характеристикам.'),
        Text.white('• Спасает от смертельного урона (раз в 10 мин) и снижает входящий урон вдвое.'),
        Text.green('• [Клавиша X]: Дарует ночное зрение, подводное дыхание и прыгучесть союзникам.')
    ]);

    // Доспехи Циско (Cisco's Armor)
    setCiscoTooltip([
        'cisco_mod:ciscos_armor_helmet',
        'cisco_mod:ciscos_armor_chestplate',
        'cisco_mod:ciscos_armor_leggings',
        'cisco_mod:ciscos_armor_boots',
        'cisco:ciscos_armor_helmet',
        'cisco:ciscos_armor_chestplate',
        'cisco:ciscos_armor_leggings',
        'cisco:ciscos_armor_boots'
    ], [
        Text.gold('★ Доспехи героя:'),
        Text.white('Даруют постоянный эффект «Мощь Циско».'),
        Text.green('• [Клавиша X]: Активирует предельную боевую способность Циско.')
    ]);
});
