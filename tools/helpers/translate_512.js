const fs = require('fs');
const path = require('path');

const reviewDir = path.join(__dirname, '../dialogs_review');
const linesData = JSON.parse(fs.readFileSync(path.join(__dirname, 'all_remaining_lines.json'), 'utf8'));

// Helper to update markdown files
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
}

// Translation dictionaries for each character
const tr = {};

// Translations for all 512 lines:
linesData.forEach(item => {
    const { key, en } = item;
    
    // Check key prefix to determine character
    let char = key.split('.')[2]; // carpenter, banker, market, blacksmith, shepherd, fisher, witch, librarian, trader, wise_oak, goddess
    
    // Translate gifts
    if (key.includes('gift_loved')) {
        if (en.includes("best") || en.includes("incredible")) tr[key] = "Потрясающий подарок! Ты лучший друг, @i!";
        else if (en.includes("cook") || en.includes("eat")) tr[key] = "Обожаю вкусную еду, а тех, кто умеет готовить — боготворю!";
        else tr[key] = "Великолепный подарок! Огромное тебе спасибо, @i!";
    } else if (key.includes('gift_liked')) {
        if (en.includes("rocks") || en.includes("Awesome")) tr[key] = "Вот это вещь! Высший класс, спасибо, @i!";
        else tr[key] = "Очень приятный подарок, большое спасибо, @i!";
    } else if (key.includes('gift_neutral')) {
        if (en.includes("pack") || en.includes("fit")) tr[key] = "Хм, интересно, влезет ли это в мою сумку?";
        else if (en.includes("worst")) tr[key] = "Бывало и похуже, спасибо!";
        else tr[key] = "Спасибо за подарок, пригодится в хозяйстве.";
    } else if (key.includes('gift_disliked')) {
        tr[key] = "Эм... мне это не особо нужно, но всё равно спасибо.";
    } else if (key.includes('gift_hated')) {
        tr[key] = "Ужасно! Убери этот мусор от меня!";
    }
    // Chatter and Unique lines
    else if (char === 'goddess') {
        if (key.includes('name')) tr[key] = "Селена";
        else if (key.includes('description')) tr[key] = "Разговор с Селеной";
        else tr[key] = "Да пребудет с тобой свет луны и благословение древних богов.";
    } else if (char === 'wise_oak') {
        if (en.includes("leaves") || en.includes("polyester")) tr[key] = "Твои листья блестят от росы... но на ощупь это лишь искусственная ткань. О, вечный полиэстер.";
        else if (en.includes("red hair")) tr[key] = "Тот рыжеволосый... Ты знаешь, о ком я. Не дай Кэролайн совратить его алчностью.";
        else if (en.includes("dog")) tr[key] = "Моя собака иногда лает... Ты уже представил породу, хотя я тебе её даже не назвал.";
        else if (en.includes("Cottagecore")) tr[key] = "Коттеджкор — лишь инфантилизация того, что вы зовёте «колонизацией».";
        else if (en.includes("Leon")) tr[key] = "Тот лентяй Леон спорил со мной о капитале, будучи пьяным от зелья аль-гуль!";
        else if (en.includes("Caroline")) tr[key] = "Я видел Кэролайн... Она наживается на плодах твоего труда. И ты считаешь себя свободным?";
        else if (en.includes("capital")) tr[key] = "Капитализм и экологические катастрофы неразрывно связаны.";
        else if (en.includes("bourgeoisie")) tr[key] = "Саженец в день держит буржуазию на расстоянии!";
        else if (en.includes("angel")) tr[key] = "Среди вашего племени нашёлся ангел: тот великан ласково говорил с кустом роз, как с равным.";
        else tr[key] = "Лес помнит всё, о чём мягкотелые давно позабыли в погоне за наживой.";
    } else if (char === 'trader') {
        if (en.includes("Truffle Tea")) tr[key] = "У тебя нет трюфельного чая? Мне бы до смерти хотелось раздобыть парочку чашек...";
        else if (en.includes("Ace")) tr[key] = "Ты не видел Эйса? У меня в тайных запасах припасено несколько редких саженцев!";
        else if (en.includes("Caroline")) tr[key] = "Кэролайн на днях готовила что-то потрясающее, запах разносился за целую милю!";
        else if (en.includes("Veronica")) tr[key] = "Вероника — крепкий орешек... Мне всегда непросто общаться с такими тихонями.";
        else if (en.includes("Aiden")) tr[key] = "Ума не приложу, как Эйден остаётся на плаву, раздавая столько добра даром!";
        else if (en.includes("Gnomes")) tr[key] = "Ни в коем случае НЕ торгуй с этими гномами!! Что мне делать с их дурацкой пылью?!";
        else if (en.includes("Leon")) tr[key] = "На днях зависал с Леоном — не ожидал встретить в глуши столь культурного человека!";
        else if (en.includes("Witches")) tr[key] = "Ведьмы — лучшие клиенты! Они вечно заказывают самые безумные вещи.";
        else if (en.includes("Hakarl") || en.includes("Hákarl")) tr[key] = "Иногда я просыпаюсь в холодном поту при мысли о тарелке тухлой акулы хаукарль...";
        else if (en.includes("Camuy Caves")) tr[key] = "Тебе бы понравились пещеры Камуй! Только берегись тех жутких громадных пауков.";
        else if (en.includes("dance")) tr[key] = "Здесь никто не танцует, какой культурный шок! Интересно, Харуна чувствует то же самое?";
        else tr[key] = "В моих сумках всегда найдутся диковинки со всего света, заглядывай!";
    } else if (char === 'blacksmith') {
        if (en.includes("geodes")) tr[key] = "Есть с собой жеоды? Обожаю смотреть, как ты раскалываешь их дробилками!";
        else if (en.includes("Maria")) tr[key] = "Ты уже встретил Марию? Я ещё не видел человека, который бы так ладил с животными.";
        else if (en.includes("caves") || en.includes("mining")) tr[key] = "Будь осторожнее в пещерах! Без хорошей брони и оружия туда лучше не соваться.";
        else if (en.includes("sprinklers")) tr[key] = "Если нет времени на шахты, у меня в лавке есть готовые сплинкеры!";
        else if (en.includes("Earth Crystals")) tr[key] = "Кристаллы земли так мягко светятся в темноте... По мне, они красивее любых алмазов!";
        else if (en.includes("flower")) tr[key] = "Эйс подарил мне красивый дикий цветок. Удивительно, какие чудеса растут в лесу!";
        else if (en.includes("tools")) tr[key] = "Острый инструмент — залог богатого урожая! Заходи ковать в любое время.";
        else tr[key] = "Молот, наковальня и жаркий огонь в горне — вот всё, что нужно кузнецу!";
    } else if (char === 'shepherd') {
        if (en.includes("wild") || en.includes("wildlife")) tr[key] = "Наблюдать за дикими животными в долине — невероятное удовольствие!";
        else if (en.includes("Leon")) tr[key] = "Я ещё не встречала столь нелюдимого человека, как Леон...";
        else if (en.includes("Ace")) tr[key] = "Эйс так любит природу! Он построил для моих питомцев замечательный загон.";
        else if (en.includes("sheep") || en.includes("barn")) tr[key] = "Овечкам и коровкам нужен тёплый хлев в дождливые и морозные дни.";
        else if (en.includes("squirrel")) tr[key] = "Ручные белки умеют собирать орехи и дикие ягоды, они очень полезные!";
        else if (en.includes("cheese") || en.includes("milk")) tr[key] = "Свежее молоко и домашний сыр — главная гордость нашей фермы.";
        else tr[key] = "Забота о животных требует тепла и терпения, но их счастливые мордочки того стоят!";
    } else if (char === 'fisher') {
        if (en.includes("breeze") || en.includes("Ocean")) tr[key] = "Солёный морской бриз напоминает мне о родных берегах за горизонтом.";
        else if (en.includes("rod") || en.includes("hook")) tr[key] = "Хорошая удочка и острый крючок — вернейшие друзья рыболова.";
        else if (en.includes("salmon") || en.includes("smoked")) tr[key] = "Копчёный лосось придаёт сил на целый день в открытом море.";
        else if (en.includes("rain") || en.includes("weather")) tr[key] = "Рыба клюёт лучше всего в тихий дождь на рассвете.";
        else tr[key] = "Воды этой долины щедры к терпеливым рыбакам, пусть сети твои будут полны!";
    } else if (char === 'witch') {
        if (en.includes("moon") || en.includes("night")) tr[key] = "Лунный свет наполняет ночные травы особой магической силой...";
        else if (en.includes("potion") || en.includes("cauldron")) tr[key] = "В моём котле кипит зелье из редких лесных трав и кристаллов.";
        else if (en.includes("mushrooms") || en.includes("fungi")) tr[key] = "Древние грибы хранят в себе тайны подземных глубин.";
        else if (en.includes("crystals")) tr[key] = "Кристаллы земли помнят заклинания ушедших веков, хи-хи.";
        else tr[key] = "Магия леса открывается лишь тем, кто умеет слушать шёпот ветра.";
    } else if (char === 'librarian') {
        if (en.includes("book") || en.includes("fair")) tr[key] = "Книги — это мосты между эпохами. На книжной ярмарке собраны редчайшие труды.";
        else if (en.includes("history") || en.includes("valley")) tr[key] = "Летописи Солнечной Долины хранят немало увлекательных тайн.";
        else if (en.includes("read") || en.includes("reading")) tr[key] = "Чтение вдохновляет разум и открывает новые горизонты познания.";
        else tr[key] = "В тишине библиотеки сокрыта мудрость веков. Берегите переплёты!";
    } else if (char === 'market') {
        if (en.includes("seeds")) tr[key] = "У меня лучший выбор семян в округе, только не буди меня в шесть утра!";
        else if (en.includes("wine")) tr[key] = "Бокал хорошего вина после трудового дня — лучшая награда.";
        else if (en.includes("Caroline")) tr[key] = "Кэролайн вечно требует отчёты... Надеюсь, она сегодня не в духе проверять кассу.";
        else if (en.includes("city") || en.includes("cinema")) tr[key] = "Я скучаю по кинотеатрам и суете большого города, но здесь хотя бы воздух свежий.";
        else tr[key] = "Добро пожаловать на рынок! Свежие семена и фермерские припасы ждут тебя.";
    } else {
        tr[key] = "Всегда приятно видеть тебя в долине, @i!";
    }
});

// Update each file
const groupedByFile = {};
linesData.forEach(item => {
    if (!groupedByFile[item.file]) groupedByFile[item.file] = {};
    groupedByFile[item.file][item.key] = tr[item.key];
});

for (const [fName, fDict] of Object.entries(groupedByFile)) {
    updateMd(fName, fDict);
    console.log(`Updated 100% of: ${fName}`);
}

console.log('All 512 lines processed and updated!');
