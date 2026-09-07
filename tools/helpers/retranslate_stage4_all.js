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
// VERONICA / LIBRARIAN (08_librarian.md)
// -------------------------------------------------------------
const librarianTrans = {
    "dialog.npc.librarian.name": "Вероника",
    "dialog.npc.librarian.chatter.description": "Разговор с Вероникой",
    "dialog.npc.librarian.intro.description": "Знакомство с Вероникой",
    "dialog.npc.librarian.intro.0.line_0": "Привет, @i! Меня зовут Вероника. Меня пригласили сюда, чтобы помочь тебе навести порядок в хранилищах и сундуках.",
    "dialog.npc.librarian.intro.0.line_1": "Кэролайн сказала мне, что твоя усадьба — это «отвратительная куча неорганизованного хлама»...",
    "dialog.npc.librarian.intro.0.line_2": "Мне кажется, она слегка сгустила краски, но, надеюсь, мои материалы для каталогизации тебе пригодятся.",
    "dialog.npc.librarian.intro.0.line_3": "У меня степень магистра библиотечных наук, так что я отлично разбираюсь в самых передовых системах хранения.",
    "dialog.npc.librarian.intro.0.line_4": "Заглядывай в библиотеку, как только появится свободная минутка.",

    "dialog.npc.librarian.chatter_friendship0.0.line_0": "Здравствуй, @i! Что я могу предложить тебе сегодня?",
    "dialog.npc.librarian.chatter_friendship0.1.line_0": "Тебе нужны принадлежности для сортировки или книги?",
    "dialog.npc.librarian.chatter_friendship0.2.line_0": "Обязательно загляни ко мне в конце сезона — у меня появятся редкие сезонные книги на продажу.",
    "dialog.npc.librarian.chatter_friendship0.3.line_0": "Добро пожаловать! Что тебе подобрать?",
    "dialog.npc.librarian.chatter_friendship0.4.line_0": "Как тебе сегодняшняя погода?",
    "dialog.npc.librarian.chatter_friendship0.4.line_1": "...Прости, я совсем не сильна в пустой светской болтовне...",

    "dialog.npc.librarian.chatter_friendship1.0.line_0": "Снова ты? Расширяешь складские помещения на ферме?",
    "dialog.npc.librarian.chatter_friendship1.1.line_0": "Ты на этот раз собираешься что-то купить или опять будешь «так смотреть» на меня, когда я озвучу цены?",
    "dialog.npc.librarian.chatter_friendship1.2.line_0": "К этому времени ты уже должен знать мой ассортимент, выбирай на здоровье.",
    "dialog.npc.librarian.chatter_friendship1.3.line_0": "Эвелин хвасталась мне какими-то магическими ящиками, которые телепортируют предметы...",
    "dialog.npc.librarian.chatter_friendship1.3.line_1": "Какая грубиянка. Я же не могу держать в лавке *вообще все* мыслимые виды сундуков.",
    "dialog.npc.librarian.chatter_friendship1.4.line_0": "Как проходит твой день? Вокруг так непривычно тихо.",

    "dialog.npc.librarian.chatter_friendship2.0.line_0": "Как Эйдену удаётся ломать столько моих ящиков для хранения? Он что, кладёт в них раскалённые слитки?!",
    "dialog.npc.librarian.chatter_friendship2.1.line_0": "Ты случайно не видел где-нибудь свежий номер «Vōg Italia»?",
    "dialog.npc.librarian.chatter_friendship2.1.line_1": "У меня ещё не было времени взглянуть на модную коллекцию этого сезона...",
    "dialog.npc.librarian.chatter_friendship2.2.line_0": "Чем могу помочь тебе сегодня, @i?",
    "dialog.npc.librarian.chatter_friendship2.3.line_0": "Мы скоро идём обедать с Кэролайн, так что давай побыстрее, у меня мало времени.",
    "dialog.npc.librarian.chatter_friendship2.4.line_0": "Ума не приложу, как вообще разговаривать с этим Эйсом.",
    "dialog.npc.librarian.chatter_friendship2.4.line_1": "Я ещё никогда не встречала людей, которые тараторят с такой скоростью. Это жутко утомляет.",

    "dialog.npc.librarian.chatter_friendship3.0.line_0": "Некоторые фермеры предпочитают прикладную школу цифровых хранилищ, хотя я нахожу её излишне громоздкой.",
    "dialog.npc.librarian.chatter_friendship3.0.line_1": "К сожалению, в моей лавке хватает места только для изысканного классического подхода.",
    "dialog.npc.librarian.chatter_friendship3.1.line_0": "Не забывай заглядывать на каждую Книжную Ярмарку! Количество книг ограничено, многие из них сезонные!",
    "dialog.npc.librarian.chatter_friendship3.2.line_0": "Можешь напомнить Леону? Мне нужно вернуть экземпляр «Записок из подполья», он держит его уже несколько недель...",
    "dialog.npc.librarian.chatter_friendship3.3.line_0": "Ох, это уже третий полевой справочник по природе, который Эйс испортил за этот месяц! Невыносимо!",
    "dialog.npc.librarian.chatter_friendship3.4.line_0": "Чем могу помочь тебе сегодня?",

    "dialog.npc.librarian.chatter_friendship4.0.line_0": "Эвелин — самый неорганизованный и хаотичный человек, которого я знаю. Это просто позор какой-то.",
    "dialog.npc.librarian.chatter_friendship4.1.line_0": "У меня сердце кровью обливается от того, насколько превратно все понимают Кэролайн...",
    "dialog.npc.librarian.chatter_friendship4.1.line_1": "Поддержка таких городков требует колоссального количества времени, сил и ресурсов.",
    "dialog.npc.librarian.chatter_friendship4.1.line_2": "Это крайне неблагодарный труд, большинство людей быстро выгорают. Но только не моя Кэролайн!",
    "dialog.npc.librarian.chatter_friendship4.2.line_0": "Кэролайн не любит непрофессионализм, так что пусть наши милые беседы в рабочее время останутся строго между нами.",
    "dialog.npc.librarian.chatter_friendship4.3.line_0": "Привет, @i! Что тебе предложить? Тебе ведь не может требоваться ЕЩЁ больше места, правда?",
    "dialog.npc.librarian.chatter_friendship4.4.line_0": "Заведи мини-овечек! У них потрясающе шелковистая шерсть. Из неё получаются восхитительные свитера... ♡",
    "dialog.npc.librarian.chatter_friendship4.4.line_1": "Ой! Не то чтобы я была экспертом в животноводстве! Спроси у Марии!",

    "dialog.npc.librarian.chatter_friendship5.0.line_0": "Секрет создания роскошных вязаных тканей — делать всё вручную. Ты как фермер должен понимать это интуитивно.",
    "dialog.npc.librarian.chatter_friendship5.1.line_0": "Ты видел последнюю коллекцию Ирис ван Херпен?!",
    "dialog.npc.librarian.chatter_friendship5.1.line_1": "Понятия не имею, как ей удаётся использовать столь необычные материалы для создания таких божественных силуэтов... ♡",
    "dialog.npc.librarian.chatter_friendship5.2.line_0": "Кого я вижу — это же @i! Я так рада тебя видеть: Кэролайн на этой неделе безумно занята, а мне так нужно с кем-нибудь поговорить!",
    "dialog.npc.librarian.chatter_friendship5.3.line_0": "Интересно, куда Карлос отправляет все те случайные вещи, что ты ему сгружаешь?",
    "dialog.npc.librarian.chatter_friendship5.3.line_1": "Он постоянно выпрашивает у меня упаковочные материалы для посылок.",
    "dialog.npc.librarian.chatter_friendship5.4.line_0": "О, привет, @i! Что я могу сделать для тебя сегодня?",
    "dialog.npc.librarian.chatter_friendship5.5.line_0": "Модные дома должны закрываться в тот момент, когда их покидают дизайнеры-основатели.",
    "dialog.npc.librarian.chatter_friendship5.5.line_1": "Да, бывают исключения, но взгляните на Готье после его ухода! Это стало настолько безвкусно!",

    "dialog.npc.librarian.dialog.book_fair.line_0": "В этом сезоне на книжной ярмарке представлен особый выбор книг, взгляните пожалуйста.",
    "dialog.npc.librarian.dialog.book_fair.option_0": "Купить материалы",
    "dialog.npc.librarian.dialog.book_fair.option_1": "Посетить книжную ярмарку",

    "dialog.npc.librarian.gift_loved.0.line_0": "Я обязана предупредить, что по правилам должна составить служебный отчёт на столь роскошные подарки... ♡",
    "dialog.npc.librarian.gift_loved.1.line_0": "Зачем ты показываешь мне столь прекрасный наряд? Я ведь никогда не смогу достать себе нечто подобное...",
    "dialog.npc.librarian.gift_loved.1.line_1": "...? Ты отдаёшь это мне?!",
    "dialog.npc.librarian.gift_loved.1.line_2": "Спасибо тебе, @i! Я буду беречь его как зеницу ока, у меня как раз есть чехол для одежды ♡",
    "dialog.npc.librarian.gift_loved.2.line_0": "Как тебе удалось раздобыть такую вещь?!",
    "dialog.npc.librarian.gift_loved.2.line_1": "Французские швы такого качества невероятно сложно выполнить на изделии подобного кроя.",
    "dialog.npc.librarian.gift_loved.2.line_2": "Это определённо создал мастер, всем сердцем влюблённый в своё ремесло ♡",
    "dialog.npc.librarian.gift_loved.3.line_0": "Текстура просто невероятная! Мария, должно быть, научила тебя ухаживать за овечками с огромной любовью ♡",
    "dialog.npc.librarian.gift_loved.4.line_0": "Какой восхитительный подарок! Не терпится внести его в каталог моей личной коллекции... ♡",

    "dialog.npc.librarian.gift_liked.0.line_0": "Спасибо, @i, я очень ценю твою доброту.",
    "dialog.npc.librarian.gift_liked.1.line_0": "Спасибо за подарок! Такие милые мелочи очень скрашивают дни.",
    "dialog.npc.librarian.gift_liked.2.line_0": "О! Мне не так уж часто дарят подарки, большое спасибо.",
    "dialog.npc.librarian.gift_liked.3.line_0": "Тебе нужен особый контейнер для этого? Выглядит симпатично.",
    "dialog.npc.librarian.gift_liked.3.line_1": "Оу, это мне? Спасибо тебе, @i.",
    "dialog.npc.librarian.gift_liked.4.line_0": "Благодарю за подарок, я знаю того, кто будет в восторге от этой вещи.",

    "dialog.npc.librarian.gift_neutral.0.line_0": "Хм-м-м? А, можешь положить это в секцию E6.",
    "dialog.npc.librarian.gift_neutral.1.line_0": "Я пока придержу это у себя, @i. Когда захочешь забрать обратно?",
    "dialog.npc.librarian.gift_neutral.2.line_0": "Подарок? С какой стати мне нужен подарок?",
    "dialog.npc.librarian.gift_neutral.3.line_0": "Я вообще-то не занимаюсь доставкой, это больше по части Эйса.",
    "dialog.npc.librarian.gift_neutral.3.line_1": "А, это подарок мне? Ну, спасибо.",
    "dialog.npc.librarian.gift_neutral.4.line_0": "Положи это в ту стопку на задней полке, пожалуйста.",

    "dialog.npc.librarian.gift_disliked.0.line_0": "Мне это совершенно ни к чему.",
    "dialog.npc.librarian.gift_disliked.1.line_0": "Я не поклонница подобных вещей.",
    "dialog.npc.librarian.gift_disliked.2.line_0": "Ты случайно не перепутал адресата? Я не совсем понимаю...",
    "dialog.npc.librarian.gift_disliked.3.line_0": "Можешь отдать это кому-нибудь другому? Мне это не нравится.",
    "dialog.npc.librarian.gift_disliked.4.line_0": "У меня нет никакой потребности в этой вещи.",

    "dialog.npc.librarian.gift_hated.0.line_0": "Не приходи ко мне за советами, как сортировать твой омерзительный мусор.",
    "dialog.npc.librarian.gift_hated.1.line_0": "Чем я заслужила такую неприкрытую неприязнь с твоей стороны?",
    "dialog.npc.librarian.gift_hated.2.line_0": "Должна предупредить: я обязана подать рапорт о подобных выходках.",
    "dialog.npc.librarian.gift_hated.2.line_1": "Пусть Кэролайн разберётся с тобой. Пожалуйста, уйди.",
    "dialog.npc.librarian.gift_hated.3.line_0": "Это отвратительно.",
    "dialog.npc.librarian.gift_hated.4.line_0": "Если бы Эйден узнал, что ты преподносишь людям ТАКОЕ, это разбило бы ему сердце.",

    "dialog.npc.librarian.unique_five_gift.line_0": "Привет, @i! У меня родилась отличная идея, как заслужить искреннее уважение Кэролайн!",
    "dialog.npc.librarian.unique_five_gift.line_1": "Как ты наверняка уже понял, её аппетиты в отношении развития нашего городка просто ненасытны.",
    "dialog.npc.librarian.unique_five_gift.line_2": "Неважно, сколько производит твоя ферма — ей всегда будет мало! Ведь всё здешнее благополучие держится на твоей экономической активности.",
    "dialog.npc.librarian.unique_five_gift.line_3": "Она заставила меня разобрать архивы старых долговых пещер... Прочти эту рукопись — там описаны древние механизмы расширения влияния!",
    "dialog.npc.librarian.unique_five_gift_read.line_0": "Ты уже изучил рукопись долговых пещер, @i? Потрясающе!",
    "dialog.npc.librarian.unique_five_gift_read.line_1": "Держи в награду амулет Дивы и кольцо маны Botania — они помогут тебе манипулировать энергией и предметами!",
    "dialog.npc.librarian.unique_five_gift_read.line_2": "Кэролайн будет в восторге от твоих новых возможностей!"
};

updateMd('08_librarian.md', librarianTrans);
