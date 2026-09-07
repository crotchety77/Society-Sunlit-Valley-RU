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

// -------------------------------------------------------------
// AIDEN / BLACKSMITH (04_blacksmith.md)
// -------------------------------------------------------------
const blacksmithTrans = {
    "dialog.npc.blacksmith.name": "Эйден",
    "dialog.npc.blacksmith.chatter.description": "Разговор с Эйденом",
    "dialog.npc.blacksmith.intro.description": "Знакомство с Эйденом",
    "dialog.npc.blacksmith.intro.0.line_0": "Привет, @i! Эйс во всех красках расписал мне твои грандиозные планы в долине.",
    "dialog.npc.blacksmith.intro.0.line_1": "Меня зовут Эйден. Я буду держать твои сельскохозяйственные инструменты в идеальной боеготовности!",
    "dialog.npc.blacksmith.intro.0.line_2": "Если понадобятся кузнечные шаблоны или дробилки жеод — просто заглядывай ко мне в кузницу.",
    "dialog.npc.blacksmith.intro.0.line_3": "Строить такой городок с нуля — дело не из лёгких, и я всегда готов подставить плечо!",

    "dialog.npc.blacksmith.chatter_friendship0.0.line_0": "Привет! Тебе что-нибудь нужно?",
    "dialog.npc.blacksmith.chatter_friendship0.1.line_0": "Наконец-то решил улучшить свои инструменты?",
    "dialog.npc.blacksmith.chatter_friendship0.2.line_0": "Чем могу помочь тебе сегодня, @i?",
    "dialog.npc.blacksmith.chatter_friendship0.3.line_0": "Приветствую, @i! Тебе что-то сковать?",
    "dialog.npc.blacksmith.chatter_friendship0.4.line_0": "Завалялись необработанные жеоды? Обожаю раскалывать их этими дробилками!",
    "dialog.npc.blacksmith.chatter_friendship0.5.line_0": "Трудовой денёк выдался, @i?",
    "dialog.npc.blacksmith.chatter_friendship0.6.line_0": "Если кто-то скажет тебе, что видел блюдечко-улитку, из вежливости стоит спросить, какого именно вида.",
    "dialog.npc.blacksmith.chatter_friendship0.7.line_0": "Как продвигаются дела на ферме, @i?",
    "dialog.npc.blacksmith.chatter_friendship0.8.line_0": "Эйс столько рассказывал мне об этой долине до того, как я сюда переехал.",
    "dialog.npc.blacksmith.chatter_friendship0.8.line_1": "Его искренняя любовь к природе видна невооружённым глазом!",
    "dialog.npc.blacksmith.chatter_friendship0.9.line_0": "Хм... руды под землёй предостаточно, но пещеры прямо-таки кишат монстрами.",
    "dialog.npc.blacksmith.chatter_friendship0.9.line_1": "Береги себя там внизу, @i!",
    "dialog.npc.blacksmith.chatter_friendship0.10.line_0": "На днях я гулял и клянусь — видел кусочек угля на ножках...",
    "dialog.npc.blacksmith.chatter_friendship0.10.line_1": "В этих пещерах творится какая-то странная магия, я абсолютно уверен!",
    "dialog.npc.blacksmith.chatter_friendship0.11.line_0": "Привет, @i! Как сегодня твои грядки?",
    "dialog.npc.blacksmith.chatter_friendship0.12.line_0": "Уже успел спуститься в шахты?",
    "dialog.npc.blacksmith.chatter_friendship0.12.line_1": "Скоро тебе понадобятся глубинные материалы, которых у меня в лавке нет.",
    "dialog.npc.blacksmith.chatter_friendship0.13.line_0": "Если нет времени копать руду для спринклеров — у меня есть готовый запас!",
    "dialog.npc.blacksmith.chatter_friendship0.13.line_1": "Ой, я вовсе не пытался навязать товар! Просто хотел, чтобы ты знал!",
    "dialog.npc.blacksmith.chatter_friendship0.14.line_0": "У кристаллов земли такое мягкое свечение, их сразу видно в темноте пещер!",
    "dialog.npc.blacksmith.chatter_friendship0.14.line_1": "На мой взгляд, они куда красивее любых алмазов!",
    "dialog.npc.blacksmith.chatter_friendship0.15.line_0": "Эйс подарил мне на днях прекрасный цветок. Поразительно, какие чудеса можно найти в дикой природе!",

    "dialog.npc.blacksmith.chatter_friendship1.0.line_0": "Улучшать инструменты важно, но и про хорошую броню не забывай!",
    "dialog.npc.blacksmith.chatter_friendship1.0.line_1": "Вылазки в пещеры без брони могут закончиться очень плачевно.",
    "dialog.npc.blacksmith.chatter_friendship1.1.line_0": "Завалялись жеоды? Обожаю смотреть, как ты раскалываешь их!",
    "dialog.npc.blacksmith.chatter_friendship1.2.line_0": "Ты уже познакомился с Марией? Я ещё не встречал человека, который бы так ладил с животными.",
    "dialog.npc.blacksmith.chatter_friendship1.3.line_0": "Леон — тот ещё оригинал...",
    "dialog.npc.blacksmith.chatter_friendship1.4.line_0": "Ох, не могу сегодня поболтать, @i, слишком много работы в кузнице!",
    "dialog.npc.blacksmith.chatter_friendship1.5.line_0": "Что для тебя сковать сегодня, @i?",
    "dialog.npc.blacksmith.chatter_friendship1.6.line_0": "Привет, @i! Что тебе нужно?",
    "dialog.npc.blacksmith.chatter_friendship1.7.line_0": "Я сегодня видел невероятную бабочку!",
    "dialog.npc.blacksmith.chatter_friendship1.7.line_1": "Они такие изящные и грациозные...",
    "dialog.npc.blacksmith.chatter_friendship1.8.line_0": "Мария заказывает у меня кучу нестандартного инвентаря...",
    "dialog.npc.blacksmith.chatter_friendship1.8.line_1": "Интересно, Кэролайн не могла бы найти для неё другого поставщика?",
    "dialog.npc.blacksmith.chatter_friendship1.9.line_0": "Даже не знаю, можно ли доверять Леону...",
    "dialog.npc.blacksmith.chatter_friendship1.9.line_1": "Некоторые люди запросто могут воспользоваться твоей добротой, если потеряешь бдительность.",

    "dialog.npc.blacksmith.chatter_friendship2.0.line_0": "Много дел сегодня, @i?",
    "dialog.npc.blacksmith.chatter_friendship2.1.line_0": "Как поживаешь, @i?",
    "dialog.npc.blacksmith.chatter_friendship2.1.line_1": "Прекрасный сегодня денёк!",
    "dialog.npc.blacksmith.chatter_friendship2.2.line_0": "Привет, @i! Я как раз надеялся, что ты сегодня заглянешь!",
    "dialog.npc.blacksmith.chatter_friendship2.3.line_0": "Чем занят, @i? Ещё не надумал обновиться до золотых инструментов?",
    "dialog.npc.blacksmith.chatter_friendship2.4.line_0": "Слишком занят, чтобы болтать, @i — Мария только что прислала огромный заказ на вёдра!",
    "dialog.npc.blacksmith.chatter_friendship2.5.line_0": "Запястье ноет не на шутку! Надо бы сегодня поработать полегче...",
    "dialog.npc.blacksmith.chatter_friendship2.6.line_0": "Хм-м-м, вилы у Леона на рынке почему-то никто не берёт.",
    "dialog.npc.blacksmith.chatter_friendship2.6.line_1": "Или, может, кое-кто опять просто забыл оформить заказ...",
    "dialog.npc.blacksmith.chatter_friendship2.7.line_0": "Как твои дела сегодня? На улице просто потрясающая погода!",
    "dialog.npc.blacksmith.chatter_friendship2.8.line_0": "Уму непостижимо, сколько топоров и пил Эйс умудряется стачивать за неделю!",
    "dialog.npc.blacksmith.chatter_friendship2.8.line_1": "Все здесь трудятся не покладая рук!",
    "dialog.npc.blacksmith.chatter_friendship2.8.line_2": "...Кроме, пожалуй, Леона...",
    "dialog.npc.blacksmith.chatter_friendship2.9.line_0": "Эйс вчера вечером рассказал мне подробнее о Пещере Черепа...",
    "dialog.npc.blacksmith.chatter_friendship2.9.line_1": "Оказывается, пещеры в пустыне буквально забиты золотом и иридием!",
    "dialog.npc.blacksmith.chatter_friendship2.9.line_2": "А ещё там полно смертельно опасных ловушек.",
    "dialog.npc.blacksmith.chatter_friendship2.10.line_0": "Гулял на днях и заметил, как из расщелины скалы на меня глазеет улитка-блюдечко!",
    "dialog.npc.blacksmith.chatter_friendship2.10.line_1": "Какая милая крохотная ракушка!",
    "dialog.npc.blacksmith.chatter_friendship2.11.line_0": "Кэролайн наотрез отказывается работать с другими кузнецами по моим изделиям.",
    "dialog.npc.blacksmith.chatter_friendship2.11.line_1": "Наверное, стоит счесть это за комплимент, но для меня это просто гора лишней работы...",
    "dialog.npc.blacksmith.chatter_friendship2.12.line_0": "Слышал, что Леон наговорил про Кэролайн?",
    "dialog.npc.blacksmith.chatter_friendship2.12.line_1": "Впрочем, не моё дело распускать слухи — лучше сам спроси у Леона.",

    "dialog.npc.blacksmith.chatter_friendship3.0.line_0": "Здравствуй, мой друг! Что тебе нужно?",
    "dialog.npc.blacksmith.chatter_friendship3.1.line_0": "Привет, дружище! Что для тебя сковать сегодня?",
    "dialog.npc.blacksmith.chatter_friendship3.2.line_0": "Привет, @i! Я как раз надеялся тебя встретить!",
    "dialog.npc.blacksmith.chatter_friendship3.3.line_0": "Чем могу помочь тебе, @i?",
    "dialog.npc.blacksmith.chatter_friendship3.4.line_0": "Что ты думаешь о Харуне? Никак не пойму: она просто нелюдимая или скрытная...",
    "dialog.npc.blacksmith.chatter_friendship3.5.line_0": "Интересно, зачем Кэролайн понадобилось столько золота в последнем заказе?",
    "dialog.npc.blacksmith.chatter_friendship3.6.line_0": "Привет, @i! Что сковать?",
    "dialog.npc.blacksmith.chatter_friendship3.7.line_0": "С возвращением! Я уже успел соскучиться!",
    "dialog.npc.blacksmith.chatter_friendship3.8.line_0": "Когда я тоскую по родному дому, я вспоминаю, какие замечательные люди меня здесь окружают.",
    "dialog.npc.blacksmith.chatter_friendship3.8.line_1": "И ты, конечно же, на первом месте в этом списке!",
    "dialog.npc.blacksmith.chatter_friendship3.9.line_0": "Хм, Леон всё ещё должен мне за починку стеллажа... Интересно, перепадёт ли мне сегодня что-нибудь сладкое на рынке?",
    "dialog.npc.blacksmith.chatter_friendship3.10.line_0": "Ох, я сегодня как-то неловко отлежал шею во сне...",
    "dialog.npc.blacksmith.chatter_friendship3.10.line_1": "Но встреча с тобой мгновенно подняла мне настроение!",
    "dialog.npc.blacksmith.chatter_friendship3.11.line_0": "Леон сегодня бесплатно добавил букетик цветов к моим покупкам!",
    "dialog.npc.blacksmith.chatter_friendship3.11.line_1": "Мне даже стало немного стыдно, что я принимал его невозмутимость за грубость.",

    "dialog.npc.blacksmith.chatter_friendship4.0.line_0": "Ну надо же, @i снова заглянул в мою кузницу!",
    "dialog.npc.blacksmith.chatter_friendship4.1.line_0": "Привет, друг! Что тебе предложить?",
    "dialog.npc.blacksmith.chatter_friendship4.2.line_0": "Прекрасный денёк, @i! Что тебе нужно?",
    "dialog.npc.blacksmith.chatter_friendship4.3.line_0": "От тебя пахнет розами! Ты недавно бродил по цветочным лесам?",
    "dialog.npc.blacksmith.chatter_friendship4.3.line_1": "Я слышал, там можно найти радужные деревья, но мне это кажется какой-то сказкой.",
    "dialog.npc.blacksmith.chatter_friendship4.4.line_0": "Иногда за работой я слышу, как тихонько напевает Харуна... Здесь так умиротворяюще...",
    "dialog.npc.blacksmith.chatter_friendship4.5.line_0": "Я невероятно рад, что перебрался сюда — жизнь в последнее время стала такой насыщенной.",
    "dialog.npc.blacksmith.chatter_friendship4.6.line_0": "♫ Привет-привет, @i! ♫",
    "dialog.npc.blacksmith.chatter_friendship4.7.line_0": "Я всегда немного нервничаю, когда Кэролайн проводит ревизию моих запасов.",
    "dialog.npc.blacksmith.chatter_friendship4.7.line_1": "Она бывает резковата, но в глубине души всегда желает поселению добра.",
    "dialog.npc.blacksmith.chatter_friendship4.8.line_0": "Тебе стоит закончить обустройство котельной, если ты ещё этого не сделал.",
    "dialog.npc.blacksmith.chatter_friendship4.8.line_1": "В хороших паровых механизмах нет ничего плохого, они здорово облегчают фермерский труд!",
    "dialog.npc.blacksmith.chatter_friendship4.9.line_0": "Кажется, я начинаю лучше понимать Леона.",
    "dialog.npc.blacksmith.chatter_friendship4.9.line_1": "Некоторые люди кажутся колючими просто из-за тяжёлых обстоятельств в прошлом.",
    "dialog.npc.blacksmith.chatter_friendship4.9.line_2": "Хотя я не до конца уверен, относится ли это к Леону...",
    "dialog.npc.blacksmith.chatter_friendship4.10.line_0": "Многие думают, что кузнечное дело — это исключительно грубая сила, но это далеко не так.",
    "dialog.npc.blacksmith.chatter_friendship4.10.line_1": "Редкие металлы вроде нептуния или электрума требуют очень деликатной и точной ковки.",
    "dialog.npc.blacksmith.chatter_friendship4.10.line_2": "У каждого вида металла свой уникальный характер!",

    "dialog.npc.blacksmith.chatter_friendship5.0.line_0": "Привет, @i! Что тебе нужно сковать?",
    "dialog.npc.blacksmith.chatter_friendship5.1.line_0": "С возвращением! Я скучал по нашим беседам!",
    "dialog.npc.blacksmith.chatter_friendship5.2.line_0": "Привет, дружище! Хочешь прикупить слитков?",
    "dialog.npc.blacksmith.chatter_friendship5.3.line_0": "Добро пожаловать! Для лучшего друга у меня всегда найдётся время.",
    "dialog.npc.blacksmith.chatter_friendship5.4.line_0": "♫ Новый день! Свежий старт! Сияющее утро! ♫",
    "dialog.npc.blacksmith.chatter_friendship5.5.line_0": "Искристый камень — удивительная вещь. Это чистейшая эссенция луны, благословение Селены.",
    "dialog.npc.blacksmith.chatter_friendship5.6.line_0": "Тебе уже удалось раздобыть немного серебра?",
    "dialog.npc.blacksmith.chatter_friendship5.6.line_1": "Оно крайне редкое, но инструменты из электрума сделают твои походы в шахту в разы плодотворнее!",
    "dialog.npc.blacksmith.chatter_friendship5.7.line_0": "Эйс угостил меня моховыми ягодами из вчерашнего похода! Они такие приятно-терпкие!",
    "dialog.npc.blacksmith.chatter_friendship5.8.line_0": "Обожаю свежий запах долины — он напоминает мне весенние магнолии из моего родного городка.",
    "dialog.npc.blacksmith.chatter_friendship5.9.line_0": "Леон начал регулярно махать мне рукой при встрече! Это значит то, о чём я думаю?",
    "dialog.npc.blacksmith.chatter_friendship5.10.line_0": "Ты уже прокачал свои инструменты до иридия?",
    "dialog.npc.blacksmith.chatter_friendship5.10.line_1": "Эйс рассказывал мне, что на нижних уровнях Пещеры Черепа его полным-полно!",
    "dialog.npc.blacksmith.chatter_friendship5.11.line_0": "Мне бы до смерти хотелось подержать в руках призматический осколок...",
    "dialog.npc.blacksmith.chatter_friendship5.11.line_1": "Но Пещера Черепа слишком опасна для такого простого кузнеца, как я!",
    "dialog.npc.blacksmith.chatter_friendship5.12.line_0": "Мария связала мне идеальный свитер для суровых зим!",
    "dialog.npc.blacksmith.chatter_friendship5.12.line_1": "Жаль, он мне чуточку маловат в плечах, но зато как приятно на него смотреть!",
    "dialog.npc.blacksmith.chatter_friendship5.13.line_0": "Леон сказал мне сегодня что-то приятное!",
    "dialog.npc.blacksmith.chatter_friendship5.13.line_1": "Ну, наверное, приятное, я не совсем уверен.",
    "dialog.npc.blacksmith.chatter_friendship5.13.line_2": "Но слышать это было чертовски приятно!",

    "dialog.npc.blacksmith.gift_loved.0.line_0": "Ого! Это же просто великолепно! Огромное спасибо, @i!",
    "dialog.npc.blacksmith.gift_loved.0.line_1": "Я буду беречь этот подарок вечно, @i!",
    "dialog.npc.blacksmith.gift_loved.1.line_0": "Потрясающий подарок! Ты прямо в душу мне заглянул!",
    "dialog.npc.blacksmith.gift_loved.2.line_0": "Какая красота! Я в полном восторге, спасибо тебе от всего сердца!",
    "dialog.npc.blacksmith.gift_loved.2.line_1": "Было бы верхом грубости не принять такой шедевр!",
    "dialog.npc.blacksmith.gift_loved.2.line_2": "Спасибо тебе, @i!",
    "dialog.npc.blacksmith.gift_loved.3.line_0": "Я сейчас расплачусь от радости! Нельзя же вот так ошарашивать человека столь прекрасными вещами!",
    "dialog.npc.blacksmith.gift_loved.4.line_0": "Откуда ты узнал, что я мечтал об этом?! Ты слишком добр ко мне!",
    "dialog.npc.blacksmith.gift_loved.5.line_0": "Ого! @i, я и не думал, что так дорог тебе... Спасибо огромное!",
    "dialog.npc.blacksmith.gift_loved.6.line_0": "Чем я заслужил такого невероятного друга?! Огромнейшее спасибо!",
    "dialog.npc.blacksmith.gift_loved.7.line_0": "Нельзя просто так подойти к человеку и вручить такой роскошный подарок!",
    "dialog.npc.blacksmith.gift_loved.7.line_1": "Спасибо тебе, верный друг!",

    "dialog.npc.blacksmith.gift_liked.0.line_0": "О, отличная штука! Спасибо большое, @i.",
    "dialog.npc.blacksmith.gift_liked.1.line_0": "Мне очень приятно! Обязательно найду этому применение в кузнице.",
    "dialog.npc.blacksmith.gift_liked.2.line_0": "Что-о-о?! Такой классный подарок! Спасибо!",
    "dialog.npc.blacksmith.gift_liked.3.line_0": "Это так мило с твоей стороны... Спасибо от всего сердца!",
    "dialog.npc.blacksmith.gift_liked.4.line_0": "Ого! Огромное тебе спасибо!",
    "dialog.npc.blacksmith.gift_liked.5.line_0": "Ты потрясающий друг, @i, спасибо!",
    "dialog.npc.blacksmith.gift_liked.6.line_0": "Как же приятно чувствовать, что твой труд ценят!",
    "dialog.npc.blacksmith.gift_liked.7.line_0": "Моё сердце поёт от радости, @i~",
    "dialog.npc.blacksmith.gift_liked.8.line_0": "Ты такой чуткий и добрый человек... Спасибо, @i.",

    "dialog.npc.blacksmith.gift_neutral.0.line_0": "Спасибо, пригодится.",
    "dialog.npc.blacksmith.gift_neutral.1.line_0": "Благодарю за подарок.",
    "dialog.npc.blacksmith.gift_neutral.2.line_0": "Что ж, спасибо!",
    "dialog.npc.blacksmith.gift_neutral.3.line_0": "Спасибо, @i!",
    "dialog.npc.blacksmith.gift_neutral.4.line_0": "Очень признателен, друг!",
    "dialog.npc.blacksmith.gift_neutral.5.line_0": "Думаю, я смогу приспособить это к какому-нибудь делу!",
    "dialog.npc.blacksmith.gift_neutral.6.line_0": "О! Спасибо за презент.",
    "dialog.npc.blacksmith.gift_neutral.7.line_0": "Приятно, когда о тебе помнят.",

    "dialog.npc.blacksmith.gift_disliked.0.line_0": "Э-э... спасибо, наверное?",
    "dialog.npc.blacksmith.gift_disliked.1.line_0": "Я не особо люблю такое, но всё равно спасибо.",
    "dialog.npc.blacksmith.gift_disliked.2.line_0": "Я ценю внимание, но тебе следовало бы узнать мои вкусы чуточку лучше!",
    "dialog.npc.blacksmith.gift_disliked.2.line_1": "Это ведь важный признак настоящей дружбы.",
    "dialog.npc.blacksmith.gift_disliked.3.line_0": "Оу...",
    "dialog.npc.blacksmith.gift_disliked.4.line_0": "Это не совсем в моём вкусе, но ничего страшного!",
    "dialog.npc.blacksmith.gift_disliked.5.line_0": "О! Подарок! Это ведь подарок, да?",
    "dialog.npc.blacksmith.gift_disliked.6.line_0": "Не думаю, что смогу переплавить это во что-то дельное, если ты об этом...",
    "dialog.npc.blacksmith.gift_disliked.6.line_1": "А, это подарок мне? Оу!",
    "dialog.npc.blacksmith.gift_disliked.7.line_0": "Я никогда не стану злиться на того, кто просто искренне пытался сделать приятное.",

    "dialog.npc.blacksmith.gift_hated.0.line_0": "Фу, убери это от наковальни немедленно!",
    "dialog.npc.blacksmith.gift_hated.1.line_0": "Ты серьёзно принёс мне этот мусор? Не ожидал от тебя такого.",
    "dialog.npc.blacksmith.gift_hated.2.line_0": "С настоящими друзьями так не поступают.",
    "dialog.npc.blacksmith.gift_hated.3.line_0": "Я чем-то обидел тебя? Что происходит...",
    "dialog.npc.blacksmith.gift_hated.4.line_0": "...",
    "dialog.npc.blacksmith.gift_hated.4.line_1": "...",
    "dialog.npc.blacksmith.gift_hated.4.line_2": "Пожалуйста, уйди.",
    "dialog.npc.blacksmith.gift_hated.5.line_0": "Как же это бессердечно.",
    "dialog.npc.blacksmith.gift_hated.6.line_0": "Жаль, что я был о тебе гораздо более высокого мнения.",
    "dialog.npc.blacksmith.gift_hated.7.line_0": "Поговори со мной, когда будешь в более адекватном настроении.",
    "dialog.npc.blacksmith.gift_hated.7.line_1": "Если ты продолжишь срывать свою злость на жителях городка, я тебе этого не прощу.",
    "dialog.npc.blacksmith.gift_hated.8.line_0": "Зачем ты преподносишь мне подобную гадость...",
    "dialog.npc.blacksmith.gift_hated.9.line_0": "Я стараюсь не злиться на людей...",
    "dialog.npc.blacksmith.gift_hated.9.line_1": "Но это выглядит как откровенное издевательство.",

    "dialog.npc.blacksmith.unique_five_gift.line_0": "О, кого я вижу — мой лучший друг @i!! У меня есть кое-что, что сделает твой день ярче!",
    "dialog.npc.blacksmith.unique_five_gift.line_1": "Особое издание моего фирменного шахтёрского молота — за счёт заведения!",
    "dialog.npc.blacksmith.unique_five_gift.line_2": "Уверен, ты ворочаешь тонны камня при строительстве фермы, так что он здорово ускорит твою работу.",
    "dialog.npc.blacksmith.unique_five_gift.line_3": "Да, кстати: я не совсем согласовал этот подарок с Кэролайн, так что не хвастайся им перед ней. Ты же знаешь, как она трясётся за наш бюджет...",
    "dialog.npc.blacksmith.unique_five_gift.line_4": "...Пусть это останется нашей маленькой тайной!"
};

updateMd('04_blacksmith.md', blacksmithTrans);
