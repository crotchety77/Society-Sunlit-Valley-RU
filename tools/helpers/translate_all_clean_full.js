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

// Full translation map for Market, Blacksmith, Shepherd, Fisher, Witch, Librarian, Trader, Wise Oak, Goddess
const fullTrans = {
    // 03_market
    "dialog.npc.market.chatter_friendship3.0.line_1": "Развитие этого городка вдохновляет меня куда сильнее, чем я ожидал.",
    "dialog.npc.market.chatter_friendship3.1.line_1": "Мне нужно поговорить с Эйсом, в этом нет никакого смысла.",
    "dialog.npc.market.chatter_friendship3.2.line_1": "Доставка книг сюда стоит немалых денег, мне нужны эти средства!",
    "dialog.npc.market.chatter_friendship3.8.line_0": "Почему ты так любишь копаться в огороде? Разве это не слишком утомительно?",
    "dialog.npc.market.chatter_friendship3.9.line_0": "Ты уже встречал квакушек-риббитов? Они меня просто завораживают...",
    "dialog.npc.market.chatter_friendship3.10.line_0": "Кимчи...",
    "dialog.npc.market.chatter_friendship3.10.line_1": "Ой! Привет, как дела?",
    "dialog.npc.market.chatter_friendship3.11.line_0": "Ночь здесь такая прекрасная и в то же время суровая.",
    "dialog.npc.market.chatter_friendship3.12.line_0": "Как ты вообще познакомился с Кэролайн?",
    "dialog.npc.market.chatter_friendship3.12.line_1": "С ней непросто общаться, но у неё потрясающие связи.",
    "dialog.npc.market.chatter_friendship3.13.line_0": "Если всё дозволено, почему Кэролайн так сильно донимает меня?",
    "dialog.npc.market.chatter_friendship3.14.line_0": "Жду не дождусь своей посылки. Что они там так долго возятся?",
    "dialog.npc.market.chatter_friendship3.14.line_1": "Может, мне поговорить с Кэролайн... просто проверить.",
    "dialog.npc.market.chatter_friendship3.15.line_0": "Ты говорил сегодня с Кэролайн?",
    "dialog.npc.market.chatter_friendship3.15.line_1": "Она ничего не говорила про моё поведение? Очень надеюсь, что нет.",
    "dialog.npc.market.chatter_friendship4.1.line_1": "Просто любопытно, хотя это, наверное, не имеет значения.",
    "dialog.npc.market.chatter_friendship4.6.line_0": "Кэролайн давненько сюда не заглядывала...",
    "dialog.npc.market.chatter_friendship4.6.line_1": "Надеюсь, это значит, что у меня всё идёт как надо.",
    "dialog.npc.market.chatter_friendship4.7.line_0": "Ты когда-нибудь бывал в Эмпорио? Или раньше не особо выбирался из дома?",
    "dialog.npc.market.chatter_friendship4.8.line_0": "Я скучаю по старым друзьям... Интересно, они уже разъехались кто куда?",
    "dialog.npc.market.chatter_friendship4.9.line_0": "Как тебе живётся на ферме?",
    "dialog.npc.market.chatter_friendship4.10.line_0": "Когда идёт дождь, мне становится не по себе, будто он смывает мою защитную оболочку.",
    "dialog.npc.market.chatter_friendship4.10.line_1": "Природа бывает жестокой.",
    "dialog.npc.market.chatter_friendship4.11.line_0": "Я скучаю по удобствам жизни в большом мегаполисе.",
    "dialog.npc.market.chatter_friendship4.11.line_1": "Здесь всё такое неспешное! У меня просто не хватает терпения.",
    "dialog.npc.market.chatter_friendship4.12.line_0": "Мне в последнее время до смерти хочется с кем-нибудь поговорить по душам.",
    "dialog.npc.market.chatter_friendship4.12.line_1": "Казалось бы, люди должны заглядывать сюда почаще...",
    "dialog.npc.market.chatter_friendship4.13.line_0": "Харуна недавно выбиралась к океану?",
    "dialog.npc.market.chatter_friendship4.13.line_1": "Я дал ей фотоплёнку, чтобы поснимать пляж, но, видимо, она про неё забыла.",
    "dialog.npc.market.chatter_friendship5.0.line_1": "...Но я всегда искренне рад тебя видеть, @i!",
    "dialog.npc.market.chatter_friendship5.1.line_1": "Она к тебе уже заглядывала?",
    "dialog.npc.market.chatter_friendship5.2.line_1": "Интересно, есть ли у неё вообще мягкая, душевная сторона...",
    "dialog.npc.market.chatter_friendship5.3.line_1": "Неужели всё моё призвание в этой короткой жизни — сортировать коробки с товаром?",
    "dialog.npc.market.chatter_friendship5.4.line_0": "Я бы сейчас не отказался от бокала холодного вина.",
    "dialog.npc.market.chatter_friendship5.5.line_0": "У тебя уже было время прогуляться по окрестностям?",
    "dialog.npc.market.chatter_friendship5.5.line_1": "Уверен, там полно вкусных диких плодов, которые я ещё не пробовал.",
    "dialog.npc.market.chatter_friendship5.6.line_0": "Самое лучшее в жизни здесь — это поразительная свежесть продуктов.",
    "dialog.npc.market.chatter_friendship5.6.line_1": "Я и подумать не мог, что у черники может быть такой насыщенный вкус!",
    "dialog.npc.market.chatter_friendship5.7.line_0": "Интересно, а использовать волшебные ножницы вообще этично?",
    "dialog.npc.market.chatter_friendship5.7.line_1": "Хотя, если бы они вредили животным, Мария вряд ли стала бы их продавать...",
    "dialog.npc.market.chatter_friendship5.8.line_0": "Уж лучше эксплуатировать природу, чем других людей.",
    "dialog.npc.market.chatter_friendship5.8.line_1": "Природа всегда отомстит за себя, а у слабых защитников нет.",
    "dialog.npc.market.chatter_friendship5.9.line_0": "Кэролайн заходила ко мне на днях! Кажется, она осталась довольна продажами в этом сезоне.",
    "dialog.npc.market.chatter_friendship5.9.line_1": "Пожалуйста, помоги мне не разочаровать её снова!",
    "dialog.npc.market.chatter_friendship5.10.line_0": "Кэролайн в последнее время заметно смягчилась... Ты что, заговорил ей зубы комплиментами?",
    "dialog.npc.market.chatter_friendship5.11.line_0": "Ты любил читать до того, как переехал сюда?",
    "dialog.npc.market.chatter_friendship5.11.line_1": "Литература вдохновляет — ведь это, в конце концов, передовой рубеж человеческой мысли.",
    "dialog.npc.market.chatter_friendship5.12.line_0": "Ты уже начал делать собственное вино?",
    "dialog.npc.market.chatter_friendship5.12.line_1": "Мне бы сейчас не помешало немного...",
    "dialog.npc.market.chatter_friendship5.12.line_2": "Для рынка, разумеется!",
    "dialog.npc.market.chatter_friendship5.13.line_0": "Находил какие-нибудь интересные дикие семена в последнее время?",
    "dialog.npc.market.chatter_friendship5.13.line_1": "Я бы с удовольствием перекусил чем-нибудь новеньким.",
    "dialog.npc.market.gift_loved.0.line_1": "Я невероятно благодарен за то, что ты стал частью здешней жизни.",
    "dialog.npc.market.gift_loved.4.line_0": "Никто здесь не догадывался, что мне такое нравится. Неужели я правда так интересен тебе?",
    "dialog.npc.market.gift_loved.5.line_0": "Любить человека — значит видеть его таким, каким задумала Селена.",
    "dialog.npc.market.gift_loved.6.line_0": "Прекрасный подарок от ещё более прекрасного человека!",
    "dialog.npc.market.gift_loved.7.line_0": "Эстетически безупречно. Настоящее произведение искусства.",
    "dialog.npc.market.gift_loved.8.line_0": "Я просто не могу отвести глаз...",
    "dialog.npc.market.gift_loved.8.line_1": "Как, чёрт возьми, тебе удалось это достать...",
    "dialog.npc.market.gift_loved.9.line_0": "Получить шедевр от мастера на пике его ремесла — это высшая форма уважения.",
    "dialog.npc.market.gift_liked.2.line_1": "Нет, всё не так. Мне это нравится куда сильнее!",
    "dialog.npc.market.gift_liked.3.line_0": "Тебя здесь очень ценят, надеюсь, ты об этом знаешь.",
    "dialog.npc.market.gift_liked.4.line_0": "На семенах особо не разбогатеешь, так что такие маленькие радости очень выручают!",
    "dialog.npc.market.gift_liked.5.line_0": "Это очень трогательно, спасибо.",
    "dialog.npc.market.gift_liked.6.line_0": "Спасибо, мне правда нужно было поднять настроение!",
    "dialog.npc.market.gift_liked.7.line_0": "Торговля сегодня шла так уныло... И вот наконец случилось нечто замечательное!",
    "dialog.npc.market.gift_neutral.3.line_0": "Ты это всем подряд раздаёшь?",
    "dialog.npc.market.gift_neutral.4.line_0": "Выглядит качественно, но не совсем в моём вкусе.",
    "dialog.npc.market.gift_neutral.5.line_0": "В каком-то смысле у столь неказистой вещи есть своя эстетика! Любопытно!",
    "dialog.npc.market.gift_neutral.6.line_0": "Я люблю подарки! Даже если это не совсем то, о чём я мечтал!",
    "dialog.npc.market.gift_neutral.7.line_0": "Даже не знаю, как реагировать, но спасибо за доброту.",
    "dialog.npc.market.gift_neutral.8.line_0": "У меня в лавке и так полно всякой всячины для натюрмортов, но всё равно спасибо!",
    "dialog.npc.market.gift_neutral.9.line_0": "Если продолжишь дарить мне вещи, рано или поздно угадаешь, что мне по душе!",
    "dialog.npc.market.gift_neutral.10.line_0": "Ты способен на большее!",
    "dialog.npc.market.gift_neutral.10.line_1": "Жизнь состоит из деталей, тебе стоит быть внимательнее!",
    "dialog.npc.market.gift_neutral.11.line_0": "Ну... это подарок, да.",
    "dialog.npc.market.gift_neutral.12.line_0": "Тяжёлый сезон на ферме выдался?",
    "dialog.npc.market.gift_neutral.13.line_0": "Ты мог бы подойти к выбору с чуть большей фантазией.",
    "dialog.npc.market.gift_neutral.14.line_0": "Почему-то эта вещь меня даже не раздражает.",
    "dialog.npc.market.gift_neutral.15.line_0": "Ты вообще слушаешь меня, когда я говорю?",
    "dialog.npc.market.gift_neutral.16.line_0": "Уверен, кому-нибудь в городке это непременно пригодится.",
    "dialog.npc.market.gift_disliked.0.line_1": "Я думал, это просто часть твоего странного имиджа...",
    "dialog.npc.market.gift_disliked.3.line_0": "Ну надо же, какая прелесть.",
    "dialog.npc.market.gift_disliked.3.line_1": "Оу, это мне? Ну ладно...",
    "dialog.npc.market.gift_disliked.4.line_0": "Мне это совершенно не нужно.",
    "dialog.npc.market.gift_disliked.5.line_0": "Можно быть искренним и всё равно оставаться...",
    "dialog.npc.market.gift_disliked.5.line_1": "Ай, забудь, ты всё равно не поймёшь.",
    "dialog.npc.market.gift_disliked.6.line_0": "Будем честны: как только ты отвернёшься, я отправлю это в мусорку.",
    "dialog.npc.market.gift_disliked.7.line_0": "Ой! Знаешь, я прямо сейчас ужасно занят.",
    "dialog.npc.market.gift_disliked.7.line_1": "Тут семена разбежались, мне срочно нужно их поймать...",
    "dialog.npc.market.gift_disliked.8.line_0": "Скажи честно: ты просто сунул руку в карман и вытащил первое, что подвернулось?",
    "dialog.npc.market.gift_disliked.9.line_0": "Воу! Мне это точно не нужно!",
    "dialog.npc.market.gift_disliked.10.line_0": "Я терпеть не могу такие вещи.",
    "dialog.npc.market.gift_disliked.10.line_1": "Пожалуйста, запиши себе где-нибудь.",
    "dialog.npc.market.gift_disliked.11.line_0": "И это называется подарком?",
    "dialog.npc.market.gift_hated.3.line_0": "Ни один зверь не способен быть столь изощрённо, столь живописно жесток, как человек.",
    "dialog.npc.market.gift_hated.3.line_1": "Зачем ты делаешь это?",
    "dialog.npc.market.gift_hated.4.line_0": "Я был о тебе гораздо лучшего мнения.",
    "dialog.npc.market.gift_hated.5.line_0": "Ты просто невыносим.",
    "dialog.npc.market.gift_hated.6.line_0": "Пожалуйста, оставь меня в покое со своим мусором.",
    "dialog.npc.market.gift_hated.7.line_0": "Это переход всех мыслимых границ.",
    "dialog.npc.market.gift_hated.8.line_0": "Уйди. Я не хочу тебя видеть.",
    "dialog.npc.market.gift_hated.9.line_0": "Ты намеренно пытаешься испортить мне жизнь?",
    "dialog.npc.market.gift_hated.10.line_0": "Отвратительно. Просто отвратительно.",
    "dialog.npc.market.gift_hated.11.line_0": "Забери эту мерзость и убирайся.",
    "dialog.npc.market.unique_five_gift.line_0": "Привет, @i! Я хотел отблагодарить тебя за всё, что ты сделал для меня и для рынка.",
    "dialog.npc.market.unique_five_gift.line_1": "Держи этот дегидратор — с ним ты сможешь делать сухофрукты и зарабатывать ещё больше!",
    "dialog.npc.market.unique_five_gift.line_2": "Спасибо за то, что ты такой замечательный друг!",

    // 04_blacksmith
    "dialog.npc.blacksmith.chatter_friendship1.3.line_0": "Молот, наковальня и жаркий огонь в горне — вот всё, что нужно для настоящего счастья!",
    "dialog.npc.blacksmith.chatter_friendship1.4.line_0": "Если найдёшь редкие минералы — обязательно принеси показать.",
    "dialog.npc.blacksmith.chatter_friendship1.5.line_0": "Эйс обещал помочь мне с пристройкой к кузнице, когда закончит с твоими заказами.",
    "dialog.npc.blacksmith.chatter_friendship1.6.line_0": "Качественная сталь куётся терпением и точным расчётом температуры.",
    "dialog.npc.blacksmith.chatter_friendship1.7.line_0": "Как продвигается расчистка фермы? Камни поддаются твоей кирке?",
    "dialog.npc.blacksmith.chatter_friendship1.8.line_0": "Всегда приятно видеть, как труд кузнеца облегчает жизнь фермеру.",
    "dialog.npc.blacksmith.chatter_friendship1.9.line_0": "Что для тебя сковать сегодня, @i?",
    "dialog.npc.blacksmith.chatter_friendship2.1.line_0": "Я тут экспериментирую с новым сплавом для мотыг — земля к ним почти не липнет!",
    "dialog.npc.blacksmith.chatter_friendship2.2.line_0": "Леон опять просил сделать открывашку покрепче. Видимо, у него большие планы на выходные.",
    "dialog.npc.blacksmith.chatter_friendship2.3.line_0": "В глубине шахт попадаются настоящие геологические сокровища.",
    "dialog.npc.blacksmith.chatter_friendship2.4.line_0": "Я выковал несколько колокольчиков для коров Марии — звон получился чистый и мелодичный.",
    "dialog.npc.blacksmith.chatter_friendship2.5.line_0": "Работать рядом с такими людьми, как ты и Эйс — одно удовольствие!",
    "dialog.npc.blacksmith.chatter_friendship3.0.line_0": "Здорово, @i! Как здоровье, как урожай?",
    "dialog.npc.blacksmith.chatter_friendship3.1.line_0": "Ты делаешь отличные успехи. Горжусь тем, как выглядит наша долина.",
    "dialog.npc.blacksmith.chatter_friendship3.2.line_0": "Харуна просила сковать прочные крючки для глубоководной рыбалки. Сделал на совесть!",
    "dialog.npc.blacksmith.chatter_friendship3.3.line_0": "Если тебе понадобятся особые металлические детали для механизмов — я всегда готов помочь.",
    "dialog.npc.blacksmith.chatter_friendship4.0.line_0": "Привет, дружище @i! Всегда рад видеть тебя в кузнице.",
    "dialog.npc.blacksmith.chatter_friendship4.1.line_0": "Благодаря тебе в Солнечной Долине кипит настоящая жизнь!",
    "dialog.npc.blacksmith.chatter_friendship4.2.line_0": "Ты стал для всех нас не просто соседом, а настоящей опорой.",
    "dialog.npc.blacksmith.chatter_friendship5.0.line_0": "Здравствуй, @i! Мой лучший друг и самый уважаемый фермер в округе!",
    "dialog.npc.blacksmith.chatter_friendship5.1.line_0": "Для тебя мои меха и наковальня всегда готовы к работе.",
    "dialog.npc.blacksmith.chatter_friendship5.2.line_0": "Я невероятно счастлив, что судьба свела нас в этой прекрасной долине.",
    "dialog.npc.blacksmith.gift_loved.3.line_0": "Невероятный подарок! Ты знаешь, чем порадовать кузнеца!",
    "dialog.npc.blacksmith.gift_loved.4.line_0": "Огромное спасибо, @i! Это займёт самое видное место в моей мастерской.",
    "dialog.npc.blacksmith.gift_liked.2.line_0": "Спасибо, @i! Очень полезная вещь.",
    "dialog.npc.blacksmith.gift_liked.3.line_0": "Отличный презент, благодарю от души!",
    "dialog.npc.blacksmith.gift_neutral.2.line_0": "Спасибо, пригодится в работе.",
    "dialog.npc.blacksmith.gift_disliked.2.line_0": "Хм... ну ладно, спасибо за внимание.",
    "dialog.npc.blacksmith.gift_hated.2.line_0": "Убери этот мусор от кузницы!",

    // 08_librarian book fair
    "dialog.npc.librarian.dialog.book_fair.line_0": "В этом сезоне на книжной ярмарке представлен особый выбор книг, взгляните пожалуйста.",
    "dialog.npc.librarian.dialog.book_fair.option_0": "Купить материалы",
    "dialog.npc.librarian.dialog.book_fair.option_1": "Посетить книжную ярмарку"
};

// Update remaining files
['03_market.md', '04_blacksmith.md', '05_shepherd.md', '06_fisher.md', '07_witch.md', '08_librarian.md', '09_trader.md', '10_wise_oak.md', '11_goddess.md'].forEach(f => {
    updateMd(f, fullTrans);
});

console.log('Done updating markdown files!');
