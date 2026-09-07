const fs = require('fs');
const path = require('path');

const reviewDir = path.join(__dirname, '../dialogs_review');

function updateMd(fileName, dict) {
    const filePath = path.join(reviewDir, fileName);
    let content = fs.readFileSync(filePath, 'utf8');
    const lines = content.split('\n');

    let updatedLines = lines.map((line) => {
        let trimmed = line.trim();
        if (trimmed.startsWith('|') && trimmed.includes('`dialog.npc.')) {
            const parts = line.split('|');
            if (parts.length >= 5) {
                const keyMatch = parts[1].match(/`([^`]+)`/);
                if (keyMatch) {
                    const key = keyMatch[1];
                    if (dict[key] !== undefined && dict[key].length > 0) {
                        parts[3] = ` ${dict[key]} `;
                        return parts.join('|');
                    }
                }
            }
        }
        return line;
    });

    fs.writeFileSync(filePath, updatedLines.join('\n'), 'utf8');
    console.log(`Successfully updated with 100% unique translations: ${fileName}`);
}

// -------------------------------------------------------------
// HARUNA (06_fisher.md)
// -------------------------------------------------------------
const fisherTranslations = {
    "dialog.npc.fisher.name": "Харуна",
    "dialog.npc.fisher.chatter.description": "Разговор с Харуной",
    "dialog.npc.fisher.intro.description": "Знакомство с Харуной",
    "dialog.npc.fisher.intro.0.line_0": "Здравствуй, меня зовут Харуна. Я хочу обустроить себе уютный дом в твоём городке.",
    "dialog.npc.fisher.intro.0.line_1": "Я могу научить тебя азам рыбной ловли. Это неспешное ремесло, требующее безграничного терпения.",
    "dialog.npc.fisher.intro.0.line_2": "Здешние воды не столь чисты и свежи, как на моей далёкой родине, но пока я вполне могу ими довольствоваться...",

    "dialog.npc.fisher.chatter_friendship0.0.line_0": "Сегодня воды неспокойны.",
    "dialog.npc.fisher.chatter_friendship0.1.line_0": "Как же далеко я от родного дома...",
    "dialog.npc.fisher.chatter_friendship0.2.line_0": "В одиночестве всегда кроется тихая печаль.",
    "dialog.npc.fisher.chatter_friendship0.3.line_0": "Сегодня здесь так тихо.",
    "dialog.npc.fisher.chatter_friendship0.4.line_0": "Обыденные волны, тоскливый океан.",
    "dialog.npc.fisher.chatter_friendship0.5.line_0": "Звёзды падают беспрестанно... прямо как я, оказавшись на этой чужой земле.",
    "dialog.npc.fisher.chatter_friendship0.6.line_0": "Хм-м-м? Прости, я немного погрузилась в свои мысли.",
    "dialog.npc.fisher.chatter_friendship0.7.line_0": "Здешние края удивительно безмятежны.",
    "dialog.npc.fisher.chatter_friendship0.8.line_0": "А, мне передали, что я должна продать тебе удочку.",
    "dialog.npc.fisher.chatter_friendship0.8.line_1": "У меня также найдётся отличная наживка, если ты прикупишь коробку для снастей.",
    "dialog.npc.fisher.chatter_friendship0.9.line_0": "Рыбалка — это безмятежная радость, которую приятнее всего вкушать в одиночестве.",
    "dialog.npc.fisher.chatter_friendship0.10.line_0": "Я сейчас занята рыбалкой, прошу меня простить.",

    "dialog.npc.fisher.chatter_friendship1.0.line_0": "Интересно, кто пишет все эти послания в бутылках?",
    "dialog.npc.fisher.chatter_friendship1.0.line_1": "Надеюсь, автор не против моего скромного любопытства.",
    "dialog.npc.fisher.chatter_friendship1.1.line_0": "Эйден, пожалуй, самый огромный человек, которого я когда-либо видела. Такой высокий...",
    "dialog.npc.fisher.chatter_friendship1.2.line_0": "Эйс для меня — настоящая загадка. Я совершенно не умею читать таких людей.",
    "dialog.npc.fisher.chatter_friendship1.3.line_0": "Там, откуда я родом, мы используем куда больше нептуния.",
    "dialog.npc.fisher.chatter_friendship1.4.line_0": "Светлячки у речного берега.",
    "dialog.npc.fisher.chatter_friendship1.4.line_1": "Их мерцание напоминает мне звёзды над родным домом.",
    "dialog.npc.fisher.chatter_friendship1.5.line_0": "Здравствуй, @i.",
    "dialog.npc.fisher.chatter_friendship1.6.line_0": "В этих водах водится много необычной рыбы. Мне бы хотелось получше с ней познакомиться.",
    "dialog.npc.fisher.chatter_friendship1.7.line_0": "Если рыбалка даётся тебе с трудом, рекомендую попробовать пробковый поплавок.",
    "dialog.npc.fisher.chatter_friendship1.8.line_0": "Чем я могу помочь тебе сегодня, @i?",

    "dialog.npc.fisher.chatter_friendship2.0.line_0": "♫ Моя жизнь, моя любовь и моя дама сердца... ♫",
    "dialog.npc.fisher.chatter_friendship2.0.line_1": "*Кхм-кхм*...",
    "dialog.npc.fisher.chatter_friendship2.0.line_2": "Да?",
    "dialog.npc.fisher.chatter_friendship2.1.line_0": "♫ Возьми меня за руку, отведи в те края... ♫",
    "dialog.npc.fisher.chatter_friendship2.1.line_1": "Ой. Прошу прощения.",
    "dialog.npc.fisher.chatter_friendship2.2.line_0": "И снова здравствуй, @i.",
    "dialog.npc.fisher.chatter_friendship2.3.line_0": "Доброго тебе дня, @i.",
    "dialog.npc.fisher.chatter_friendship2.4.line_0": "Я вижу Морану в тихом блеске застывшего океана.",
    "dialog.npc.fisher.chatter_friendship2.5.line_0": "У рек есть свои прекрасные и щедрые дары.",
    "dialog.npc.fisher.chatter_friendship2.6.line_0": "Эйс рассказывал мне о морских блинчиках! Мне бы очень хотелось увидеть скатов...",
    "dialog.npc.fisher.chatter_friendship2.7.line_0": "Леон очень прямолинеен и честен. Мне нравится эта черта в людях.",
    "dialog.npc.fisher.chatter_friendship2.8.line_0": "На моей родине каждый прекрасно разбирается в повадках рыб.",
    "dialog.npc.fisher.chatter_friendship2.8.line_1": "Но я ещё никогда не встречала никого, кто рыбачил бы так же неумело, как Эйс...",
    "dialog.npc.fisher.chatter_friendship2.9.line_0": "Хочешь опробовать новые поплавки? У меня богатейший выбор снастей.",

    "dialog.npc.fisher.chatter_friendship3.0.line_0": "♫ Пусть дни уходят прочь, пусть вода укроет меня... ♫",
    "dialog.npc.fisher.chatter_friendship3.0.line_1": "О. Приветствую.",
    "dialog.npc.fisher.chatter_friendship3.1.line_0": "Есть что-то особенное в здешних водах...",
    "dialog.npc.fisher.chatter_friendship3.1.line_1": "Словно само солнце противится магии морских волн.",
    "dialog.npc.fisher.chatter_friendship3.1.line_2": "Любопытно.",
    "dialog.npc.fisher.chatter_friendship3.2.line_0": "Рассвет сегодня невероятно красив.",
    "dialog.npc.fisher.chatter_friendship3.2.line_1": "...",
    "dialog.npc.fisher.chatter_friendship3.2.line_2": "Впрочем, нельзя позволять красоте отвлекать тебя от поклёвки.",
    "dialog.npc.fisher.chatter_friendship3.3.line_0": "Кэролайн уважает моё ремесло, хотя и заглядывает сюда нечасто...",
    "dialog.npc.fisher.chatter_friendship3.4.line_0": "Забавно: свежая рыба водится как в солёной, так и в пресной воде...",
    "dialog.npc.fisher.chatter_friendship3.4.line_1": "А чтобы сохранить её свежей надолго — её посыпают солью.",
    "dialog.npc.fisher.chatter_friendship3.5.line_0": "Поймал что-нибудь новенькое в последнее время?",
    "dialog.npc.fisher.chatter_friendship3.6.line_0": "Ты уже проверил свои рыбные пруды сегодня?",
    "dialog.npc.fisher.chatter_friendship3.7.line_0": "Как думаешь, Эйс сможет смастерить что-нибудь из этого плавника, что я нашла на берегу?",
    "dialog.npc.fisher.chatter_friendship3.8.line_0": "Здешняя рыба бывает... весьма необычной.",
    "dialog.npc.fisher.chatter_friendship3.9.line_0": "Создатели наживки удобны, но верная рука рыбака всегда поймает лучшую рыбу.",

    "dialog.npc.fisher.chatter_friendship4.0.line_0": "Склоняюсь с удочкой в руке,",
    "dialog.npc.fisher.chatter_friendship4.0.line_1": "Волна разбилась о причал,",
    "dialog.npc.fisher.chatter_friendship4.0.line_2": "Мистический простор глубин.",
    "dialog.npc.fisher.chatter_friendship4.1.line_0": "Мария слишком мягкосердечна, чтобы до конца принять естественный круговорот жизни и смерти.",
    "dialog.npc.fisher.chatter_friendship4.2.line_0": "Чистейший купол небес,",
    "dialog.npc.fisher.chatter_friendship4.2.line_1": "Трудятся люди, собирая урожай,",
    "dialog.npc.fisher.chatter_friendship4.2.line_2": "Солнечная Долина.",
    "dialog.npc.fisher.chatter_friendship4.3.line_0": "Рыбалка способна завести тебя в самые невероятные уголки мира.",
    "dialog.npc.fisher.chatter_friendship4.3.line_1": "Пляжи, бурные реки, ледники, острова... и даже жерла вулканов.",
    "dialog.npc.fisher.chatter_friendship4.4.line_0": "Морские рынки весьма непредсказуемы, знаешь ли.",
    "dialog.npc.fisher.chatter_friendship4.4.line_1": "Раньше я зарабатывала большую часть монет выполнением контрактов на редкие уловы.",
    "dialog.npc.fisher.chatter_friendship4.5.line_0": "Эти воды меня озадачивают.",
    "dialog.npc.fisher.chatter_friendship4.5.line_1": "Откуда здесь берётся столько желе?",
    "dialog.npc.fisher.chatter_friendship4.6.line_0": "♫ Стук и плеск воды, из резервуара в резервуар! ♫",
    "dialog.npc.fisher.chatter_friendship4.7.line_0": "Да, @i?",
    "dialog.npc.fisher.chatter_friendship4.8.line_0": "Всегда приятно перекинуться с тобой словом.",
    "dialog.npc.fisher.chatter_friendship4.9.line_0": "Чудесный денёк для рыбной ловли.",

    "dialog.npc.fisher.chatter_friendship5.0.line_0": "Ты слышишь это? Прислушайся!",
    "dialog.npc.fisher.chatter_friendship5.0.line_1": "...",
    "dialog.npc.fisher.chatter_friendship5.0.line_2": "Вода издаёт такие чарующие звуки.",
    "dialog.npc.fisher.chatter_friendship5.1.line_0": "Я уже давненько не выходила в открытое море.",
    "dialog.npc.fisher.chatter_friendship5.1.line_1": "Полагаю, это место обладает необъяснимым притяжением.",
    "dialog.npc.fisher.chatter_friendship5.2.line_0": "Такая огромная долина, и столько рыбы ждёт своих сетей...",
    "dialog.npc.fisher.chatter_friendship5.2.line_1": "О! Отличный ритм для стиха.",
    "dialog.npc.fisher.chatter_friendship5.3.line_0": "И снова здравствуй, мой друг.",
    "dialog.npc.fisher.chatter_friendship5.4.line_0": "Горестен удел рыбака с пустой удочкой...",
    "dialog.npc.fisher.chatter_friendship5.5.line_0": "Сонет глубоководных рыб — орган пещерных вод.",
    "dialog.npc.fisher.chatter_friendship5.6.line_0": "Снип-снорп... Снип-снорп... Какая забавная ритмика у названия этой рыбки.",
    "dialog.npc.fisher.chatter_friendship5.7.line_0": "Я обожаю такие дни.",
    "dialog.npc.fisher.chatter_friendship5.8.line_0": "♫ Хм-м-м, хм-м-м... ♫",
    "dialog.npc.fisher.chatter_friendship5.9.line_0": "Я искренне привязалась к безграничной любви Марии к животным. Это невероятно трогательно!",
    "dialog.npc.fisher.chatter_friendship5.10.line_0": "Я всегда с удовольствием разделяю бокал вина с Леоном в прохладные вечера.",

    "dialog.npc.fisher.gift_loved.0.line_0": "Ты, должно быть, вложил много души и мыслей в этот подарок.",
    "dialog.npc.fisher.gift_loved.1.line_0": "Такие маленькие радости дают мне повод петь, @i.",
    "dialog.npc.fisher.gift_loved.2.line_0": "Ты знаешь меня слишком хорошо, ты настоящая жемчужина этой земли.",
    "dialog.npc.fisher.gift_loved.3.line_0": "Поистине чудесный дар. Он живо напоминает мне о родных краях.",
    "dialog.npc.fisher.gift_loved.4.line_0": "Спасибо тебе, @i. Благодаря тебе я чувствую себя здесь как дома.",
    "dialog.npc.fisher.gift_loved.5.line_0": "♫ Спасибо тебе, мой самый милый друг ♫",
    "dialog.npc.fisher.gift_loved.6.line_0": "Я не смогу отплатить за такую доброту, но было бы невежливо отказаться от столь прекрасного дара.",

    "dialog.npc.fisher.gift_liked.0.line_0": "Прямо как у меня на родине.",
    "dialog.npc.fisher.gift_liked.1.line_0": "Спасибо, @i, ты слишком добр ко мне.",
    "dialog.npc.fisher.gift_liked.2.line_0": "Почти столь же приятно, как шум вечернего прибоя.",
    "dialog.npc.fisher.gift_liked.3.line_0": "Я ценю это сильнее, чем ты можешь представить.",
    "dialog.npc.fisher.gift_liked.4.line_0": "У тебя настоящий талант к выбору подарков, @i.",
    "dialog.npc.fisher.gift_liked.5.line_0": "Это словно свежий бриз в знойный день — желанный и отрадный.",

    "dialog.npc.fisher.gift_neutral.0.line_0": "Благодарю за подарок.",
    "dialog.npc.fisher.gift_neutral.1.line_0": "Спасибо, @i.",
    "dialog.npc.fisher.gift_neutral.2.line_0": "Благодарю за внимание, @i.",
    "dialog.npc.fisher.gift_neutral.3.line_0": "Хм, думаешь, кому-нибудь ещё из горожан это тоже понравится?",
    "dialog.npc.fisher.gift_neutral.4.line_0": "Я смогу использовать это как подношение звёздам, спасибо.",
    "dialog.npc.fisher.gift_neutral.5.line_0": "Я как раз хотела поэкспериментировать с новыми видами поплавков, спасибо.",
    "dialog.npc.fisher.gift_neutral.6.line_0": "Спасибо за подарок, @i.",
    "dialog.npc.fisher.gift_neutral.7.line_0": "Странно: люди здесь часто дарят мне самые случайные вещи. Я всё ещё не привыкла.",
    "dialog.npc.fisher.gift_neutral.8.line_0": "Не уверена, как именно применю это, но жест ценю.",

    "dialog.npc.fisher.gift_disliked.0.line_0": "Пожалуй, лучше я сохраню это у себя, чем позволю засорять среду обитания рыб.",
    "dialog.npc.fisher.gift_disliked.1.line_0": "Некоторые вещи лучше оставлять при себе, чем дарить другим.",
    "dialog.npc.fisher.gift_disliked.2.line_0": "Не уверена, что мне это по душе...",
    "dialog.npc.fisher.gift_disliked.3.line_0": "В моей культуре подобное считается дурным тоном («faux pas»).",
    "dialog.npc.fisher.gift_disliked.4.line_0": "Как бы мне сейчас хотелось прижать к уху раковину и слушать море, а не это...",
    "dialog.npc.fisher.gift_disliked.5.line_0": "Не думаю, что это сгодится даже в качестве наживки...",
    "dialog.npc.fisher.gift_disliked.6.line_0": "Это у вас здесь считается шуткой?",

    "dialog.npc.fisher.gift_hated.0.line_0": "Это выбросило на берег вместе с тем мусором, что я видела утром?",
    "dialog.npc.fisher.gift_hated.1.line_0": "Интересно, безопасно ли прямо сейчас отплыть обратно на родину...",
    "dialog.npc.fisher.gift_hated.2.line_0": "Какое оскорбление...",
    "dialog.npc.fisher.gift_hated.3.line_0": "Я надеюсь, ты принёс это по ошибке.",
    "dialog.npc.fisher.gift_hated.4.line_0": "Прошу, не подходи ко мне больше с такими вещами.",
    "dialog.npc.fisher.gift_hated.5.line_0": "Море не терпит столь пренебрежительного отношения.",
    "dialog.npc.fisher.gift_hated.6.line_0": "Убери это прочь. Немедленно.",

    "dialog.npc.fisher.unique_five_gift.line_0": "Приветствую, @i. Я приготовила для тебя нечто особенное в знак нашей дружбы.",
    "dialog.npc.fisher.unique_five_gift.line_1": "Это Сердце Нептуния — древняя реликвия морских глубин с моей родины.",
    "dialog.npc.fisher.unique_five_gift.line_2": "Оно поможет тебе дышать под водой и свободно исследовать глубочайшие океанские впадины.",
    "dialog.npc.fisher.unique_five_gift.line_3": "Пусть духи глубин всегда хранят твой путь, мой дорогой друг."
};

updateMd('06_fisher.md', fisherTranslations);

// -------------------------------------------------------------
// WITCH (07_witch.md)
// -------------------------------------------------------------
const witchTranslations = {
    "dialog.npc.witch.name": "Эвелин",
    "dialog.npc.witch.chatter.description": "Разговор с Эвелин",
    "dialog.npc.witch.intro.description": "Знакомство с Эвелин",
    "dialog.npc.witch.intro.0.line_0": "...Я знаю, кто ТЫ такой!",
    "dialog.npc.witch.intro.0.line_1": "Но дело не в этом! Дело во мне! И в том, что ты видел!",
    "dialog.npc.witch.intro.0.line_2": "Кэролайн рассказала мне о твоей вылазке в Незер. Мне понадобятся твои находки для исследований!",
    "dialog.npc.witch.intro.0.line_3": "О, ещё я вроде как должна продавать тебе магические штуковины, над которыми работаю. Не то чтобы мне хотелось, но эта Кэролайн выглядит пугающе убедительно...",

    "dialog.npc.witch.chatter_friendship0.0.line_0": "Уходи! Я работаю!",
    "dialog.npc.witch.chatter_friendship0.1.line_0": "Я задрала цены на всё подряд, так что, пожалуйста, ничего не покупай.",
    "dialog.npc.witch.chatter_friendship0.1.line_1": "Хотя ладно, это ложь: Кэролайн регулярно проверяет мои гроссбухи...",
    "dialog.npc.witch.chatter_friendship0.2.line_0": "Чего тебе надо?!",
    "dialog.npc.witch.chatter_friendship0.3.line_0": "Клянусь, это не я сделала! Готова спорить, это Леон натворил!",
    "dialog.npc.witch.chatter_friendship0.3.line_1": "А? Тебя послала не Кэролайн? Тогда проехали.",
    "dialog.npc.witch.chatter_friendship0.4.line_0": "Извини, я не гадаю на таро. Я ведьма совсем другого толка.",
    "dialog.npc.witch.chatter_friendship0.5.line_0": "* Похоже, Эвелин ходит во сне... *",
    "dialog.npc.witch.chatter_friendship0.5.line_1": "* Лучше просто оставить оплату где-нибудь поблизости... *",
    "dialog.npc.witch.chatter_friendship0.6.line_0": "...Хм-м-м-м? Чего тебе, @i?",

    "dialog.npc.witch.chatter_friendship1.0.line_0": "Что интересного удалось откопать сегодня? Ты ведь не прячешь от меня редкие образцы, верно?",
    "dialog.npc.witch.chatter_friendship1.1.line_0": "Мне не нравится эта Харуна...",
    "dialog.npc.witch.chatter_friendship1.1.line_1": "С какой стати люди вечно хранят от меня секреты?! От МЕНЯ, подумать только!",
    "dialog.npc.witch.chatter_friendship1.2.line_0": "Вы записаны на приём?",
    "dialog.npc.witch.chatter_friendship1.2.line_1": "Прости, я сегодня всех об этом спрашиваю — просто не могу найти свой календарь...",
    "dialog.npc.witch.chatter_friendship1.3.line_0": "Мария уже замучила меня своими просьбами пополнить запас чудо-зелий!",
    "dialog.npc.witch.chatter_friendship1.3.line_1": "Кому вообще нужно СТОЛЬКО животных?!",
    "dialog.npc.witch.chatter_friendship1.4.line_0": "Не встречал странных жуков в последнее время? Я знаю одного типа, который прямо тащится от странных жуков.",
    "dialog.npc.witch.chatter_friendship1.4.line_1": "Мне очень нужна от него одна услуга, но я не хочу лишних расспросов.",

    "dialog.npc.witch.chatter_friendship2.0.line_0": "Ты ничегошеньки не смыслишь, @i. В мире действуют силы, которые ты даже представить не в состоянии.",
    "dialog.npc.witch.chatter_friendship2.1.line_0": "Кэролайн вечно ко мне придирается! Все вокруг засыпают на деловых планёрках, они же жутко скучные!",
    "dialog.npc.witch.chatter_friendship2.2.line_0": "* Приближаясь, вы слышите храп. Эвелин снова сладко спит прямо стоя. *",
    "dialog.npc.witch.chatter_friendship2.3.line_0": "Я фонтан крови в форме девушки...",
    "dialog.npc.witch.chatter_friendship2.3.line_1": "Полагаю, это делает тебя птицей? По крайней мере, так говорят.",
    "dialog.npc.witch.chatter_friendship2.4.line_0": "Я изучаю здешнюю магию уже несколько сезонов. Тут явно сокрыто нечто большее...",
    "dialog.npc.witch.chatter_friendship2.4.line_1": "...Только пусть это останется строго между нами.",
    "dialog.npc.witch.chatter_friendship2.5.line_0": "В этой долине таится глубинная магия. Я чувствую её, и ты, уверена, тоже.",

    "dialog.npc.witch.chatter_friendship3.0.line_0": "Я НИЧЕГО не понимаю!! Вокруг действуют силы, которые я даже вообразить не могу!!",
    "dialog.npc.witch.chatter_friendship3.1.line_0": "* Невозможно понять: Эвелин наполовину спит или собирается выкрикнуть заклинание *",
    "dialog.npc.witch.chatter_friendship3.1.line_1": "Хм-м-м? Чего ты так на меня уставился? Купи уже что-нибудь.",
    "dialog.npc.witch.chatter_friendship3.2.line_0": "Мои планы рассчитаны на столетия вперёд...",
    "dialog.npc.witch.chatter_friendship3.2.line_1": "...Но я хоть убей не помню, куда положила свиток с записями...",
    "dialog.npc.witch.chatter_friendship3.3.line_0": "Я решила навести идеальный порядок на рабочем столе... До чего по-скандинавски с моей стороны!",
    "dialog.npc.witch.chatter_friendship3.4.line_0": "Эйс — просто сокровище, он всегда приносит мне редкие травы.",
    "dialog.npc.witch.chatter_friendship3.4.line_1": "Я на самом деле терпеееть не могу бродить по дикой природе, так что очень ценю тех, кто делает это за меня.",
    "dialog.npc.witch.chatter_friendship3.5.line_0": "То, что наш разум способен выдумать всё что угодно, вовсе не означает, что это никогда не сбудется...",
    "dialog.npc.witch.chatter_friendship3.5.line_1": "Так гласят заветы верховной покровительницы!",
    "dialog.npc.witch.chatter_friendship3.6.line_0": "Вчера ночью я совершила грандиозный прорыв! Обычно я бы поделилась с тобой, мы ведь друзья, но это знание явно выше твоего допуска...",
    "dialog.npc.witch.chatter_friendship3.7.line_0": "Пожалуйста, купи что-нибудь! Мне срочно нужно подкупить Эйдена, чтобы он выдал мне дорогое шахтёрское снаряжение!",

    "dialog.npc.witch.chatter_friendship4.0.line_0": "Эта дурацкая лунная дева постоянно отчитывает меня во сне!",
    "dialog.npc.witch.chatter_friendship4.0.line_1": "И что плохого в накопительстве? Вдруг мне весь этот хлам ещё когда-нибудь пригодится!",
    "dialog.npc.witch.chatter_friendship4.1.line_0": "Ты в последнее время сдаёшь маловато минералов. Только не говори, что зажимаешь всё для себя...",
    "dialog.npc.witch.chatter_friendship4.2.line_0": "Не позволяй поэтам вешать тебе лапшу на уши!! И под поэтами я имею в виду этого Леона!!!",
    "dialog.npc.witch.chatter_friendship4.3.line_0": "Я видела это в видении!",
    "dialog.npc.witch.chatter_friendship4.3.line_1": "Кора Незера опускается на дно бездны, взмывая прямо в небеса!",
    "dialog.npc.witch.chatter_friendship4.3.line_2": "Очищаясь в кристальные поля мучительно яркого света!",
    "dialog.npc.witch.chatter_friendship4.3.line_3": "Я абсолютно уверена, что всё так и случится!",
    "dialog.npc.witch.chatter_friendship4.4.line_0": "С возвращением, @i! Твой спецзаказ где-то тут валялся, сейчас достану...",
    "dialog.npc.witch.chatter_friendship4.4.line_1": "А, ты ничего не заказывал? И что мне теперь делать с 20 килограммами плортов?!",
    "dialog.npc.witch.chatter_friendship4.5.line_0": "Карлос постоянно пытается навязать мне грабительские сделки! У кого вообще есть время варить столько трюфельного чая?",
    "dialog.npc.witch.chatter_friendship4.5.line_1": "Зачем ему вообще СТОЛЬКО чая?!",

    "dialog.npc.witch.chatter_friendship5.0.line_0": "Мы с лунной девой сейчас в лучших отношениях, но я всё равно считаю, что она чересчур агрессивная...",
    "dialog.npc.witch.chatter_friendship5.1.line_0": "Раз уж мы такие закадычные друзья... Не поможешь прибраться в моей хижине? Мы ведь друзья, да?",
    "dialog.npc.witch.chatter_friendship5.2.line_0": "А ты знал, что в некоторых мирах люди тренируют жуков и драконов для боёв друг с другом?",
    "dialog.npc.witch.chatter_friendship5.2.line_1": "Они позволяют заниматься этим детям, и даже за деньги!",
    "dialog.npc.witch.chatter_friendship5.3.line_0": "Передай Веронике, что в 12-м издании «Словаря геологии и минералогии» Гнейса опять опечатка.",
    "dialog.npc.witch.chatter_friendship5.3.line_1": "Честно говоря, современное книгоиздание в полном упадке, просто позорище.",
    "dialog.npc.witch.chatter_friendship5.4.line_0": "Эйден каждое утро приносит мне кофе, и я до сих пор не поняла, зачем...",
    "dialog.npc.witch.chatter_friendship5.4.line_1": "Может, в наших рядах появился ещё один тайный исследователь оккультизма?!",

    "dialog.npc.witch.gift_loved.0.line_0": "Где ты это откопал, @i?! Я искала такую вещь целую вечность!",
    "dialog.npc.witch.gift_loved.1.line_0": "МНЕ НУЖНО ЕЩЁ.",
    "dialog.npc.witch.gift_loved.1.line_1": "ПРИНЕСИ МНЕ ЕЩЁ ТАКОГО.",
    "dialog.npc.witch.gift_loved.2.line_0": "Это поддержит мои силы ещё на пару дней, спасибо, @i.",
    "dialog.npc.witch.gift_loved.3.line_0": "Какой диковинный образец... Пожалуй, оставлю его для своей постоянной коллекции.",
    "dialog.npc.witch.gift_loved.4.line_0": "Я знала, что от тебя есть толк! Кэролайн ошибалась! Спасибо, @i!",

    "dialog.npc.witch.gift_liked.0.line_0": "Я как раз собиралась раздобыть побольше таких штук, спасибо.",
    "dialog.npc.witch.gift_liked.1.line_0": "Кто тебя подослал? Они в курсе?",
    "dialog.npc.witch.gift_liked.1.line_1": "Выглядишь растерянно... ладно, проехали.",
    "dialog.npc.witch.gift_liked.1.line_2": "Ой, дай сюда, пока не ушёл, мне это нужно.",
    "dialog.npc.witch.gift_liked.2.line_0": "Давай сюда, пригодится в опытах. Наверное.",
    "dialog.npc.witch.gift_liked.3.line_0": "Прости, у меня сейчас нет при себе монет.",
    "dialog.npc.witch.gift_liked.3.line_1": "Ой, ты просто так мне это отдаёшь? Задаром? Ну ты и чудик.",
    "dialog.npc.witch.gift_liked.4.line_0": "Я понимаю, почему ты решил, что мне это будет интересно.",

    "dialog.npc.witch.gift_neutral.0.line_0": "О, мне как раз не хватало таких штук.",
    "dialog.npc.witch.gift_neutral.1.line_0": "Просто брось в ту кучу в углу.",
    "dialog.npc.witch.gift_neutral.2.line_0": "Э-э-э, я вообще-то не изучаю подобные вещи, но, думаю, смогу найти применение!",
    "dialog.npc.witch.gift_neutral.3.line_0": "Скучновато. Это для моих исследований или подарок лично мне?",
    "dialog.npc.witch.gift_neutral.3.line_1": "Не отвечай, так даже загадочнее.",
    "dialog.npc.witch.gift_neutral.4.line_0": "Хм-м-м-м-м......",
    "dialog.npc.witch.gift_neutral.4.line_1": "...",
    "dialog.npc.witch.gift_neutral.4.line_2": "* Непонятно: Эвелин пристально изучает подарок или тихо уснула стоя... *",

    "dialog.npc.witch.gift_disliked.0.line_0": "Ого, я даже не знала, что на свете существует настолько мерзкая дрянь.",
    "dialog.npc.witch.gift_disliked.1.line_0": "Мне точно не нужны дополнительные чистящие средства.",
    "dialog.npc.witch.gift_disliked.2.line_0": "Пожалуй, я могла бы бросить это в свой вечный котёл, убивающий людей...",
    "dialog.npc.witch.gift_disliked.2.line_1": "...Ты ведь не на полном серьёзе веришь, что у меня есть такой котёл? Уходи.",
    "dialog.npc.witch.gift_disliked.3.line_0": "Это мне? Зачем?",
    "dialog.npc.witch.gift_disliked.4.line_0": "По-моему, такое больше по вкусу Марии, если ты понимаешь, о чём я.",

    "dialog.npc.witch.gift_hated.0.line_0": "Хм-м-м-м...? Мне не нужен лишний мусор для сжигания, у меня своего навалом.",
    "dialog.npc.witch.gift_hated.1.line_0": "У меня нет места, чтобы хранить этот хлам.",
    "dialog.npc.witch.gift_hated.2.line_0": "Я для тебя какая-то шутка? Имей хоть каплю уважения.",
    "dialog.npc.witch.gift_hated.3.line_0": "* Раздаётся вызывающе громкий наигранный храп. *",
    "dialog.npc.witch.gift_hated.3.line_1": "* Похоже, Эвелин категорически не желает это принимать. *",
    "dialog.npc.witch.gift_hated.4.line_0": "У меня нет ни малейшего желания выносить за тобой мусор.",
    "dialog.npc.witch.gift_hated.5.line_0": "Зачем ты суёшь мне это? Мне оно даром не нужно.",
    "dialog.npc.witch.gift_hated.5.line_1": "Никому такое не нужно.",

    "dialog.npc.witch.unique_five_gift.line_0": "Эй, @i! Я закончила работу над новым магическим устройством.",
    "dialog.npc.witch.unique_five_gift.line_1": "Держи этот автопоглаживатель для скота — он сам заботится о животных в хлеву, пока ты занят делом!",
    "dialog.npc.witch.unique_five_gift.line_2": "Теперь Мария точно перестанет донимать меня своими просьбами, хи-хи!"
};

updateMd('07_witch.md', witchTranslations);
