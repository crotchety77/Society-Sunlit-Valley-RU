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
    console.log(`Updated: ${fileName}`);
}

const wiseOakPerfect = {
    "dialog.npc.wise_oak.name": "Мудрый Дуб",
    "dialog.npc.wise_oak.chatter.description": "Разговор с Мудрым Дубом",
    "dialog.npc.wise_oak.intro.description": "Знакомство с Мудрым Дубом",
    "dialog.npc.wise_oak.intro.0.line_0": "Тебе нравится причинять боль другим?",
    "dialog.npc.wise_oak.intro.0.line_1": "Брать свой топор и вонзать его глубоко в тех, кого ты смеешь называть своими «друзьями»?",
    "dialog.npc.wise_oak.intro.0.line_2": "Мои безмолвные братья в коре валятся наземь от твоих рук каждый божий день. И ради чего?",
    "dialog.npc.wise_oak.intro.0.line_3": "Ради этой ненасытной машины, которую вы зовёте прогрессом? Капиталом? Ты дурной человек.",
    "dialog.npc.wise_oak.intro.0.line_4": "«Приятно» познакомиться, о Мягкотелый. А теперь оставь меня в покое.",

    "dialog.npc.wise_oak.chatter_friendship0.0.line_0": "Здравствуй, Мягкотелый. Что это ходячее бедствие планирует выкорчевать сегодня?",
    "dialog.npc.wise_oak.chatter_friendship0.1.line_0": "Ты недостоин мягких волн двудольных растений. Ты недостоин своей собственной мягкости.",
    "dialog.npc.wise_oak.chatter_friendship0.2.line_0": "Трава под твоими ногами вопиет от огня. Блок за блоком их жизни гаснут под твоей лопатой.",
    "dialog.npc.wise_oak.chatter_friendship0.3.line_0": "Тот, что в полосатой рубахе, куда добрее тебя.",
    "dialog.npc.wise_oak.chatter_friendship0.3.line_1": "Хотя я прекрасно знаю, что след древесного сока от твоего топора ведёт прямиком в его мастерскую.",
    "dialog.npc.wise_oak.chatter_friendship0.3.line_2": "В конце концов, всех нас связывают именно цепи капитала.",
    "dialog.npc.wise_oak.chatter_friendship0.4.line_0": "Ты всего лишь букет тряпичных роз с острыми металлическими шипами.",
    "dialog.npc.wise_oak.chatter_friendship0.5.line_0": "Ты паразит, соперничать с которым может лишь сам капитал.",
    "dialog.npc.wise_oak.chatter_friendship0.6.line_0": "Всё, о чём ты говоришь «я создал» — не более чем вивисекция первозданной красоты этой земли.",

    "dialog.npc.wise_oak.chatter_friendship1.0.line_0": "До встречи, Мягкотелый. Ты ведь никогда не остановишься, так что я просто полагаю, что ты вернёшься.",
    "dialog.npc.wise_oak.chatter_friendship1.0.line_1": "Пожалуйста, уйди.",
    "dialog.npc.wise_oak.chatter_friendship1.1.line_0": "Твои листья выглядят блестящими, липкими и влажными от росы...",
    "dialog.npc.wise_oak.chatter_friendship1.1.line_1": "Но при повторном касании понимаешь — это ткань.",
    "dialog.npc.wise_oak.chatter_friendship1.1.line_2": "О, вечный полиэстер.",
    "dialog.npc.wise_oak.chatter_friendship1.2.line_0": "Тот рыжеволосый...",
    "dialog.npc.wise_oak.chatter_friendship1.2.line_1": "Ты знаешь, о ком я.",
    "dialog.npc.wise_oak.chatter_friendship1.2.line_2": "Не позволяй Кэролайн развратить его своей алчностью.",
    "dialog.npc.wise_oak.chatter_friendship1.3.line_0": "Моя собака иногда лает...",
    "dialog.npc.wise_oak.chatter_friendship1.3.line_1": "Мысленно ты уже рисуешь себе образ пса, хотя я даже не назвал породу, которая у меня живёт...",
    "dialog.npc.wise_oak.chatter_friendship1.4.line_0": "Давай поговорим начистоту, о Мягкотелый.",
    "dialog.npc.wise_oak.chatter_friendship1.4.line_1": "Коттеджкор — всего лишь инфантилизация того, что твой народ зовёт «колонизацией».",
    "dialog.npc.wise_oak.chatter_friendship1.4.line_2": "Прикрытие слащавыми словами не спасёт твою душу от первобытной тьмы древнего леса.",

    "dialog.npc.wise_oak.chatter_friendship2.0.line_0": "Ты лаешь не на тот Quercus.",
    "dialog.npc.wise_oak.chatter_friendship2.1.line_0": "Тот ленивец, которого вы зовёте Леоном, пытался спорить со мной о природе капитала в сравнении с естественным единением с лесом!",
    "dialog.npc.wise_oak.chatter_friendship2.1.line_1": "И всё это — будучи пьяным от змеиного зелья аль-гуль!",
    "dialog.npc.wise_oak.chatter_friendship2.1.line_2": "Неужели у мягкотелых нет ни капли гордости? Ни грамма стыда?",
    "dialog.npc.wise_oak.chatter_friendship2.2.line_0": "Я видел ту омерзительную капиталистку Кэролайн...",
    "dialog.npc.wise_oak.chatter_friendship2.2.line_1": "Именно она стоит за твоим появлением в этих краях.",
    "dialog.npc.wise_oak.chatter_friendship2.2.line_2": "Как ты можешь мнить себя свободным, когда некто вроде неё крадёт плоды твоего труда?",
    "dialog.npc.wise_oak.chatter_friendship2.3.line_0": "Проще представить конец света, чем конец вашей ядовитой колонизации, которую вы зовёте «фермой».",
    "dialog.npc.wise_oak.chatter_friendship2.4.line_0": "Связь между капитализмом и экоцидом отнюдь не случайна и не совпадение.",

    "dialog.npc.wise_oak.chatter_friendship3.0.line_0": "Ты высасываешь мои силы этой пустой болтовнёй. Дай мне отдохнуть.",
    "dialog.npc.wise_oak.chatter_friendship3.1.line_0": "Саженец в день держит буржуазию на расстоянии!",
    "dialog.npc.wise_oak.chatter_friendship3.2.line_0": "Капиталистическая идеология ловко маскируется под неизбежность.",
    "dialog.npc.wise_oak.chatter_friendship3.2.line_1": "«Если я не заберу это себе, это сделает кто-то другой».",
    "dialog.npc.wise_oak.chatter_friendship3.2.line_2": "Ты не защищён от этой ловушки мышления, о Мягкотелый.",
    "dialog.npc.wise_oak.chatter_friendship3.3.line_0": "Те, кто отрицает собственную роль в мерзости капитализма, отнюдь не оправданы перед ликом леса.",
    "dialog.npc.wise_oak.chatter_friendship3.4.line_0": "Среди вашего племени нашёлся ангел!",
    "dialog.npc.wise_oak.chatter_friendship3.4.line_1": "Тот бледнолицый великан ласково говорил с кустом роз, словно с равным.",
    "dialog.npc.wise_oak.chatter_friendship3.4.line_2": "Вот у кого тебе стоило бы поучиться паре вещей.",

    "dialog.npc.wise_oak.chatter_friendship4.0.line_0": "Цветы увядают, но ты — нет.",
    "dialog.npc.wise_oak.chatter_friendship4.1.line_0": "В воздухе вокруг тебя разлито странное, тревожное затишье.",
    "dialog.npc.wise_oak.chatter_friendship4.2.line_0": "Слышат ли растения в глиняных горшках?",
    "dialog.npc.wise_oak.chatter_friendship4.3.line_0": "Капитал обладает свойством поглощать любую критику в свой адрес.",
    "dialog.npc.wise_oak.chatter_friendship4.3.line_1": "Даже критику от таких древних созданий, как я.",
    "dialog.npc.wise_oak.chatter_friendship4.3.line_2": "Значит ли это, что нужно прекратить критику? Не дай бог.",
    "dialog.npc.wise_oak.chatter_friendship4.4.line_0": "Сегодня приятный ветер. Подлинный, живой ветер — это то, что твоя индустриальная натура никогда не сможет воссоздать.",
    "dialog.npc.wise_oak.chatter_friendship4.4.line_1": "Лопасти тех металлических чудовищ, которых вы зовёте вентиляторами, никогда с ним не сравнятся.",

    "dialog.npc.wise_oak.chatter_friendship5.0.line_0": "Тайна Селены никогда не будет разгадана смертными. Загадки луны поистине бесконечны.",
    "dialog.npc.wise_oak.chatter_friendship5.1.line_0": "Меня интригует тот ваш мудрец — вечно сонный и растрёпанный.",
    "dialog.npc.wise_oak.chatter_friendship5.1.line_1": "В ясные ночи я замечаю мерцающий взгляд, пристально следящий за мной...",
    "dialog.npc.wise_oak.chatter_friendship5.1.line_2": "Словно весенний кардинал, высматривающий спелую ягоду...",
    "dialog.npc.wise_oak.chatter_friendship5.2.line_0": "Здравствуй, мой Мягкотелый.",
    "dialog.npc.wise_oak.chatter_friendship5.3.line_0": "Обществом других нужно наслаждаться, а не клеймить его. Будь добр к остальным, как был добр ко мне.",
    "dialog.npc.wise_oak.chatter_friendship5.4.line_0": "Когда деревья падают, древесный полог расцветает, а грибы борются за жизнь. Естественный круговорот бытия в этих чащах.",
    "dialog.npc.wise_oak.chatter_friendship5.5.line_0": "Лист скорби по всей моей павшей общине.",
    "dialog.npc.wise_oak.chatter_friendship5.5.line_1": "Безмолвное благословение вечнозелёным хвойным, что придут им на смену.",
    "dialog.npc.wise_oak.chatter_friendship5.5.line_2": "Пронесённое сквозь эпохи пламя.",
    "dialog.npc.wise_oak.chatter_friendship5.6.line_0": "Почему плачет ива?",
    "dialog.npc.wise_oak.chatter_friendship5.6.line_1": "Почему дуб так дорожит этим объёмным мешком из плоти и хрящей?",
    "dialog.npc.wise_oak.chatter_friendship5.7.line_0": "Капитал подчиняет себе всё вокруг.",
    "dialog.npc.wise_oak.chatter_friendship5.7.line_1": "Точно так же, как вы вырубаете землю, мой род осыпает тех, кто под нами, густой тенью.",
    "dialog.npc.wise_oak.chatter_friendship5.7.line_2": "Несущая тень гибель для этих отчаянных цветочных бутонов в залитой солнцем долине.",

    "dialog.npc.wise_oak.unique_five_gift.line_0": "И снова здравствуй, мягкотелый. Я долго наблюдал за тобой и этой вашей маленькой общиной, которую вы зовёте городком.",
    "dialog.npc.wise_oak.unique_five_gift.line_1": "В этом вашем маленьком обществе что-то есть... Подобно самому лесу, ты и твои сородичи просто пытаетесь выжить в гармонии.",
    "dialog.npc.wise_oak.unique_five_gift.line_2": "Труд — это ваш общий плод, из которого каждый извлекает взаимную пользу. Здесь нет единой доминирующей силы, присваивающей чужой капитал.",
    "dialog.npc.wise_oak.unique_five_gift.line_3": "Даже тот фиолетовый демон оставляет плоды твоего труда тебе самому... Но я отвлёкся.",
    "dialog.npc.wise_oak.unique_five_gift.line_4": "Я желаю стать частью этого общества, но, как и для любого другого, это должно быть на моих условиях, ибо я представляю естественный порядок вещей.",

    "dialog.npc.wise_oak.unique_no_gifting.line_0": "О, мягкотелый, твои жалкие мелкие подачки со мной не сработают.",
    "dialog.npc.wise_oak.unique_no_gifting.line_1": "Моё уважение нельзя купить за вещи, как бы этого ни хотелось вам, капиталистам.",
    "dialog.npc.wise_oak.unique_no_gifting.line_2": "Заслужи моё уважение исключительно беседами, и ничем иным."
};

updateMd('10_wise_oak.md', wiseOakPerfect);
