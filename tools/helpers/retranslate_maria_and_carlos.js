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
// MARIA / SHEPHERD (05_shepherd.md)
// -------------------------------------------------------------
const shepherdTrans = {
    "dialog.npc.shepherd.name": "Мария",
    "dialog.npc.shepherd.chatter.description": "Разговор с Марией",
    "dialog.npc.shepherd.intro.description": "Знакомство с Марией",
    "dialog.npc.shepherd.intro.0.line_0": "Здравствуй! Меня зовут Мария. Я помогу тебе начать разведение животных на твоей ферме.",
    "dialog.npc.shepherd.intro.0.line_1": "Забота о животных требует много сил, терпения и тепла.",
    "dialog.npc.shepherd.intro.0.line_2": "Но видеть довольную мордочку счастливого питомца — это бесценно!",
    "dialog.npc.shepherd.intro.0.line_3": "Если тебе понадобятся товары для скота — просто дай мне знать.",

    "dialog.npc.shepherd.chatter_friendship0.0.line_0": "Привет! Тебе что-нибудь нужно?",
    "dialog.npc.shepherd.chatter_friendship0.1.line_0": "Я ещё не совсем привыкла к жизни в такой глуши.",
    "dialog.npc.shepherd.chatter_friendship0.1.line_1": "Но наблюдать за дикой природой здесь невероятно увлекательно!",
    "dialog.npc.shepherd.chatter_friendship0.2.line_0": "Как дела на ферме?",
    "dialog.npc.shepherd.chatter_friendship0.2.line_1": "Ты уже успел завести первых животных?",
    "dialog.npc.shepherd.chatter_friendship0.3.line_0": "По ночам здесь немного жутковато, я не привыкла к такому открытому простору.",
    "dialog.npc.shepherd.chatter_friendship0.4.line_0": "Тебе что-то нужно?",
    "dialog.npc.shepherd.chatter_friendship0.5.line_0": "Хочешь что-нибудь прикупить?",
    "dialog.npc.shepherd.chatter_friendship0.6.line_0": "В долине полно диких слизней...",
    "dialog.npc.shepherd.chatter_friendship0.6.line_1": "Они вечно выскакивают из ниоткуда и пугают меня до смерти.",
    "dialog.npc.shepherd.chatter_friendship0.7.line_0": "Ты не видел поблизости Эйса?",
    "dialog.npc.shepherd.chatter_friendship0.8.line_0": "Чем я могу помочь тебе сегодня?",
    "dialog.npc.shepherd.chatter_friendship0.9.line_0": "Здравствуй, @i.",
    "dialog.npc.shepherd.chatter_friendship0.10.line_0": "Я бы сейчас не отказалась от чашечки горячего кофе...",
    "dialog.npc.shepherd.chatter_friendship0.11.line_0": "Я часто с сомнением отношусь к новым фермерам, пытающимся завести скот.",
    "dialog.npc.shepherd.chatter_friendship0.11.line_1": "У некоторых из них совершенно чёрствое сердце, неспособное на заботу.",
    "dialog.npc.shepherd.chatter_friendship0.12.line_0": "Даже не знаю, что и думать о Леоне...",
    "dialog.npc.shepherd.chatter_friendship0.12.line_1": "Я ещё никогда не встречала столь отстранённого человека.",
    "dialog.npc.shepherd.chatter_friendship0.13.line_0": "Мне всегда любопытно, чем закончится путь очередного фермера.",
    "dialog.npc.shepherd.chatter_friendship0.13.line_1": "Далеко не каждый создан для столь тяжёлого ежедневного труда.",
    "dialog.npc.shepherd.chatter_friendship0.14.line_0": "Здесь все такие приветливые, меня это даже слегка смущает.",
    "dialog.npc.shepherd.chatter_friendship0.14.line_1": "Ой, нет, я не в плохом смысле! Просто я ещё не привыкла!",

    "dialog.npc.shepherd.chatter_friendship1.0.line_0": "На днях я видела диких овечек на склоне холма.",
    "dialog.npc.shepherd.chatter_friendship1.0.line_1": "Кажется, им бы не помешал тёплый и уютный хлев...",
    "dialog.npc.shepherd.chatter_friendship1.1.line_0": "Не обязательно заходить ко мне так часто.",
    "dialog.npc.shepherd.chatter_friendship1.1.line_1": "Я вполне способна сама о себе позаботиться.",
    "dialog.npc.shepherd.chatter_friendship1.2.line_0": "Когда ты даёшь имя своему животному, между вами возникает особая связь.",
    "dialog.npc.shepherd.chatter_friendship1.2.line_1": "Обязательно выбирай имя, которое подходит характеру питомца!",
    "dialog.npc.shepherd.chatter_friendship1.3.line_0": "Как идут дела у тебя на ферме?",
    "dialog.npc.shepherd.chatter_friendship1.4.line_0": "Здесь всё так спокойно и просто...",
    "dialog.npc.shepherd.chatter_friendship1.4.line_1": "Мне очень интересно наблюдать, как всё меняется с течением времени.",
    "dialog.npc.shepherd.chatter_friendship1.5.line_0": "Эйс угостил меня сегодня лососевыми ягодами!",
    "dialog.npc.shepherd.chatter_friendship1.5.line_1": "Неудивительно, что белки постоянно вынюхивают их в кустах.",
    "dialog.npc.shepherd.chatter_friendship1.6.line_0": "Не стесняйся заглядывать, если у тебя появятся вопросы об уходе за животными.",
    "dialog.npc.shepherd.chatter_friendship1.7.line_0": "Тебе что-нибудь нужно?",
    "dialog.npc.shepherd.chatter_friendship1.8.line_0": "Как твоё настроение сегодня?",
    "dialog.npc.shepherd.chatter_friendship1.9.line_0": "Привет, @i! Чем могу помочь?",
    "dialog.npc.shepherd.chatter_friendship1.10.line_0": "Люди часто лгут, а вот животные всегда скажут тебе чистую правду.",
    "dialog.npc.shepherd.chatter_friendship1.10.line_1": "Кроме енотов — эти вечно норовят тебя обхитрить!",
    "dialog.npc.shepherd.chatter_friendship1.11.line_0": "Как Эйдену удаётся оставаться таким жизнерадостным, стоя у раскалённого горна целый день?",
    "dialog.npc.shepherd.chatter_friendship1.12.line_0": "Зачем Леон вообще переехал в эту глушь?",
    "dialog.npc.shepherd.chatter_friendship1.12.line_1": "Я ещё не встречала человека, который так сильно недолюбливал бы природу.",
    "dialog.npc.shepherd.chatter_friendship1.13.line_0": "Я скучаю по бездомным котикам из города, где я выросла...",
    "dialog.npc.shepherd.chatter_friendship1.13.line_1": "Хотя бродячие овечки — это по-своему тоже очень мило!",

    "dialog.npc.shepherd.chatter_friendship2.0.line_0": "Столько новых лиц в городке...",
    "dialog.npc.shepherd.chatter_friendship2.0.line_1": "Переезжать на новое место всегда очень непросто.",
    "dialog.npc.shepherd.chatter_friendship2.1.line_0": "Я насмотрелась на бессердечных фермеров, которые жестоко обращаются со скотом.",
    "dialog.npc.shepherd.chatter_friendship2.1.line_1": "Гигантские тесные загоны, набитые до отказа... Меня от этого просто тошнит...",
    "dialog.npc.shepherd.chatter_friendship2.1.line_2": "Я так рада, что ты совсем не такой!",
    "dialog.npc.shepherd.chatter_friendship2.2.line_0": "Корм для животных на исходе?",
    "dialog.npc.shepherd.chatter_friendship2.2.line_1": "Или ты пришёл приютить нового питомца?",
    "dialog.npc.shepherd.chatter_friendship2.3.line_0": "Мне так нравится наблюдать, как дикие звери свободно резвятся в долине.",
    "dialog.npc.shepherd.chatter_friendship2.4.line_0": "Есть что-то в здешнем воздухе... такое лёгкое и освобождающее.",
    "dialog.npc.shepherd.chatter_friendship2.5.line_0": "Надеюсь, ты кормишь своих питомцев каждый день.",
    "dialog.npc.shepherd.chatter_friendship2.5.line_1": "Ты бы тоже ворчал, если бы тебе пришлось пропустить обед!",
    "dialog.npc.shepherd.chatter_friendship2.6.line_0": "Попробуй смастерить сачок для ловли насекомых!",
    "dialog.npc.shepherd.chatter_friendship2.6.line_1": "В нашей долине порхает столько чудесных бабочек.",
    "dialog.npc.shepherd.chatter_friendship2.7.line_0": "У меня не лежит душа к огородничеству — я вечно заливаю растения водой...",
    "dialog.npc.shepherd.chatter_friendship2.8.line_0": "Обожаю ощущение, когда ткёшь полотно на холщовом станке.",
    "dialog.npc.shepherd.chatter_friendship2.8.line_1": "Ничто не сравнится с этим чувством уюта.",
    "dialog.npc.shepherd.chatter_friendship2.9.line_0": "Леон сегодня был таким хмурым, когда я заходила за продуктами.",
    "dialog.npc.shepherd.chatter_friendship2.9.line_1": "Люди бывают такими колючими, когда сильно устают.",
    "dialog.npc.shepherd.chatter_friendship2.10.line_0": "Истинное сердце человека часто раскрывается в том, как он относится к животным.",
    "dialog.npc.shepherd.chatter_friendship2.11.line_0": "Некоторые люди приносят в жизни столько разочарований.",
    "dialog.npc.shepherd.chatter_friendship2.11.line_1": "Ах, но здесь-то точно никто не такой! Наверное...",
    "dialog.npc.shepherd.chatter_friendship2.12.line_0": "Из зерновых вроде пшеницы и кукурузы получается отличный комбикорм.",
    "dialog.npc.shepherd.chatter_friendship2.12.line_1": "Уверена, твои животные оценят свежую фермерскую еду куда больше покупной!",

    "dialog.npc.shepherd.chatter_friendship3.0.line_0": "Нужно больше корма?",
    "dialog.npc.shepherd.chatter_friendship3.1.line_0": "Ты не думал завести свинок?",
    "dialog.npc.shepherd.chatter_friendship3.1.line_1": "Трюфели просто великолепны для приготовления пончиков!",
    "dialog.npc.shepherd.chatter_friendship3.2.line_0": "Ты случайно не говорил недавно с Эйденом?",
    "dialog.npc.shepherd.chatter_friendship3.2.line_1": "Мне очень нужен тот заказ на металлические вёдра...",
    "dialog.npc.shepherd.chatter_friendship3.3.line_0": "Животные даже не представляют, на какое зло способны люди.",
    "dialog.npc.shepherd.chatter_friendship3.3.line_1": "Наша святая обязанность — сделать так, чтобы они никогда об этом не узнали.",
    "dialog.npc.shepherd.chatter_friendship3.4.line_0": "О человеке можно узнать очень многое по тому, как он подходит к испуганному зверю.",
    "dialog.npc.shepherd.chatter_friendship3.5.line_0": "Я сегодня читала в фермерском альманахе про мини-овечек.",
    "dialog.npc.shepherd.chatter_friendship3.5.line_1": "...Они такие пушистенькие...",
    "dialog.npc.shepherd.chatter_friendship3.6.line_0": "Кэролайн прямо-таки тает от козьего сыра.",
    "dialog.npc.shepherd.chatter_friendship3.6.line_1": "Только не говори, что я тебе проболталась! Я хочу выведать ещё секретов...",
    "dialog.npc.shepherd.chatter_friendship3.7.line_0": "У Леона на рынке появились швейные принадлежности.",
    "dialog.npc.shepherd.chatter_friendship3.7.line_1": "Дай знать, если понадобятся уроки шитья!",
    "dialog.npc.shepherd.chatter_friendship3.8.line_0": "У Кэролайн весьма дорогой и изысканный вкус.",
    "dialog.npc.shepherd.chatter_friendship3.8.line_1": "Большинство людей даже не отличают настоящую мериносовую шерсть от обычной.",
    "dialog.npc.shepherd.chatter_friendship3.9.line_0": "У тебя такие мозолистые руки!",
    "dialog.npc.shepherd.chatter_friendship3.9.line_1": "Давай я попозже взгляну — у меня есть мазь на овечьем молоке, она отлично смягчает кожу.",
    "dialog.npc.shepherd.chatter_friendship3.10.line_0": "Ты когда-нибудь задумывался, что снится нашим питомцам?",
    "dialog.npc.shepherd.chatter_friendship3.11.line_0": "Такому трудяге, как ты, точно не помешало бы парочка домашних любимцев.",
    "dialog.npc.shepherd.chatter_friendship3.11.line_1": "Бьюсь об заклад, на дальних полях бывает очень одиноко.",

    "dialog.npc.shepherd.chatter_friendship4.0.line_0": "Поначалу я думала, что Леон невзлюбил именно меня.",
    "dialog.npc.shepherd.chatter_friendship4.0.line_1": "А потом поняла: он просто сам по себе такой бука со всеми.",
    "dialog.npc.shepherd.chatter_friendship4.1.line_0": "Нет ничего чище и слаще, чем искренняя любовь питомца.",
    "dialog.npc.shepherd.chatter_friendship4.2.line_0": "Привет, @i! Чем занят сегодня?",
    "dialog.npc.shepherd.chatter_friendship4.3.line_0": "Как поживает твое ранчо сегодня?",
    "dialog.npc.shepherd.chatter_friendship4.4.line_0": "Тебе определённо нравится проводить со мной время.",
    "dialog.npc.shepherd.chatter_friendship4.4.line_1": "Или, может, у тебя есть какой-то тайный умысел?..",
    "dialog.npc.shepherd.chatter_friendship4.5.line_0": "Твои визиты совершенно непредсказуемы по времени.",
    "dialog.npc.shepherd.chatter_friendship4.5.line_1": "Я никогда заранее не знаю, в какую минуту ты появишься на пороге.",
    "dialog.npc.shepherd.chatter_friendship4.6.line_0": "Интересно, строительство целого города как-то влияет на твоё эго?",
    "dialog.npc.shepherd.chatter_friendship4.6.line_1": "Хотя здешние жители быстро вернут тебя с небес на землю, готова спорить!",
    "dialog.npc.shepherd.chatter_friendship4.7.line_0": "Кэролайн порой бывает такой бессердечной!",
    "dialog.npc.shepherd.chatter_friendship4.7.line_1": "Это одна из самых неприятных сторон здешней жизни.",
    "dialog.npc.shepherd.chatter_friendship4.8.line_0": "В промышленном животноводстве так много вещей, которые мне отвратительны.",
    "dialog.npc.shepherd.chatter_friendship4.8.line_1": "Я понимаю, что обществу нужно пропитание...",
    "dialog.npc.shepherd.chatter_friendship4.8.line_2": "Но только посмей плохо обращаться с животными — я сразу всё узнаю.",
    "dialog.npc.shepherd.chatter_friendship4.9.line_0": "Среди фермеров ходит поверье, что избыток скота навлечёт гнев Селены.",
    "dialog.npc.shepherd.chatter_friendship4.9.line_1": "Она ведь и правда существует...",
    "dialog.npc.shepherd.chatter_friendship4.10.line_0": "Ты слышал про губеров?",
    "dialog.npc.shepherd.chatter_friendship4.10.line_1": "Говорят, они родом из места под названием Пещера Черепа, где бы оно ни находилось.",
    "dialog.npc.shepherd.chatter_friendship4.11.line_0": "Эйс рассказывал мне о моховых ягодах на днях.",
    "dialog.npc.shepherd.chatter_friendship4.11.line_1": "Готова спорить, из них получится изумительное варенье.",
    "dialog.npc.shepherd.chatter_friendship4.12.line_0": "Жители городка запросто подходят ко мне и выкладывают свои тайны.",
    "dialog.npc.shepherd.chatter_friendship4.12.line_1": "Наверное, я произвожу впечатление человека, которому можно доверять?",
    "dialog.npc.shepherd.chatter_friendship4.13.line_0": "Я вяжу тёплые свитера для здешних суровых зим.",
    "dialog.npc.shepherd.chatter_friendship4.13.line_1": "Хотя тебе-то с твоей беготнёй по полям никакой мороз не страшен!",

    "dialog.npc.shepherd.chatter_friendship5.0.line_0": "Леон на днях дал мне попробовать продукты с твоей фермы.",
    "dialog.npc.shepherd.chatter_friendship5.0.line_1": "Всё было таким свежим, сочным и невероятно вкусным!",
    "dialog.npc.shepherd.chatter_friendship5.1.line_0": "Леон так любит поговорить о Кэролайн...",
    "dialog.npc.shepherd.chatter_friendship5.1.line_1": "Интересно, к чему бы это?..",
    "dialog.npc.shepherd.chatter_friendship5.2.line_0": "Люди иногда думают, что я не люблю людей только потому, что обожаю животных.",
    "dialog.npc.shepherd.chatter_friendship5.2.line_1": "Я так рада, что ты не из их числа.",
    "dialog.npc.shepherd.chatter_friendship5.3.line_0": "Ах! Я как раз искала тебя, @i.",
    "dialog.npc.shepherd.chatter_friendship5.4.line_0": "Какие планы на сегодня, @i?",
    "dialog.npc.shepherd.chatter_friendship5.5.line_0": "Чем я могу порадовать тебя?",
    "dialog.npc.shepherd.chatter_friendship5.6.line_0": "Кое-кто наивно полагает, что моё расположение можно купить подарками и лестью.",
    "dialog.npc.shepherd.chatter_friendship5.6.line_1": "Но это не настоящая душевная близость, и ты прекрасно это понимаешь.",
    "dialog.npc.shepherd.chatter_friendship5.7.line_0": "У тебя редкий талант находить общий язык с людьми.",
    "dialog.npc.shepherd.chatter_friendship5.7.line_1": "С тобой так легко и приятно говорить обо всём на свете.",
    "dialog.npc.shepherd.chatter_friendship5.8.line_0": "То, как птичка сима-энага склоняет свою крошечную головку набок — настоящее чудо света.",
    "dialog.npc.shepherd.chatter_friendship5.8.line_1": "Истинная снежная фея!",
    "dialog.npc.shepherd.chatter_friendship5.9.line_0": "Какой же сегодня тихий и умиротворённый день...",
    "dialog.npc.shepherd.chatter_friendship5.10.line_0": "Что бы тебе хотелось приобрести?",
    "dialog.npc.shepherd.chatter_friendship5.11.line_0": "Люди считают свиней грязнулями из-за того, чем их заставляют питаться на фермах.",
    "dialog.npc.shepherd.chatter_friendship5.11.line_1": "Животные могут многому научить нас в плане человечности.",
    "dialog.npc.shepherd.chatter_friendship5.12.line_0": "Эйс хотел тебя о чём-то расспросить.",
    "dialog.npc.shepherd.chatter_friendship5.12.line_1": "Интересно, о чём вы шепчетесь, когда никто не видит?",
    "dialog.npc.shepherd.chatter_friendship5.13.line_0": "Я знала, что ты придёшь сегодня, и заранее отложила для тебя порцию отборного корма!",
    "dialog.npc.shepherd.chatter_friendship5.14.line_0": "Кэролайн вовсе не из тех людей, которые оказываются душками, стоит узнать их поближе.",
    "dialog.npc.shepherd.chatter_friendship5.14.line_1": "Обычно моё чутьё на людей не ошибается.",
    "dialog.npc.shepherd.chatter_friendship5.15.line_0": "Твой неуёмный размах порой даже немного пугает меня...",
    "dialog.npc.shepherd.chatter_friendship5.15.line_1": "Надеюсь, перепахивание долины стоит тех грандиозных целей, к которым ты стремишься.",
    "dialog.npc.shepherd.chatter_friendship5.16.line_0": "Есть что-то невероятно трогательное в том, как питомец смотрит на тебя полными любви глазами.",
    "dialog.npc.shepherd.chatter_friendship5.16.line_1": "Ничто в мире с этим не сравнится.",

    "dialog.npc.shepherd.gift_loved.0.line_0": "О боже мой! Это же просто чудо! Спасибо тебе огромное, @i!",
    "dialog.npc.shepherd.gift_loved.1.line_0": "Какой невероятно милый и прекрасный подарок! Я просто счастлива!",
    "dialog.npc.shepherd.gift_loved.2.line_0": "Это одна из моих самых любимых вещей на свете!",
    "dialog.npc.shepherd.gift_loved.3.line_0": "Какой душевный подарок, спасибо тебе, @i.",
    "dialog.npc.shepherd.gift_loved.4.line_0": "Благодаря тебе я чувствую, что мне здесь по-настоящему рады.",
    "dialog.npc.shepherd.gift_loved.5.line_0": "Как ты догадался, что я обожаю такое?!",
    "dialog.npc.shepherd.gift_loved.6.line_0": "Ого! Какая роскошная вещь.",
    "dialog.npc.shepherd.gift_loved.7.line_0": "Мне это безумно нравится!",
    "dialog.npc.shepherd.gift_loved.8.line_0": "Это просто потрясающий подарок.",

    "dialog.npc.shepherd.gift_liked.0.line_0": "Ой, спасибо большое, @i! Мне очень приятно.",
    "dialog.npc.shepherd.gift_liked.1.line_0": "Я знаю идеальное местечко для этой вещи!",
    "dialog.npc.shepherd.gift_liked.2.line_0": "Я на днях присматривала это на рынке! Откуда ты узнал?",
    "dialog.npc.shepherd.gift_liked.3.line_0": "Как мило с твоей стороны! Спасибо.",
    "dialog.npc.shepherd.gift_liked.4.line_0": "Это с твоей фермы? Какая прелесть.",
    "dialog.npc.shepherd.gift_liked.5.line_0": "Очень чуткий и приятный подарок.",
    "dialog.npc.shepherd.gift_liked.6.line_0": "Какая красота, я искренне ценю это.",
    "dialog.npc.shepherd.gift_liked.7.line_0": "Ты настоящее сокровище!",
    "dialog.npc.shepherd.gift_liked.8.line_0": "Как же здорово, что в нашей долине есть такие замечательные люди, как ты.",
    "dialog.npc.shepherd.gift_liked.9.line_0": "Большое-пребольшое тебе спасибо!",

    "dialog.npc.shepherd.gift_neutral.0.line_0": "Спасибо, пригодится в хозяйстве.",
    "dialog.npc.shepherd.gift_neutral.1.line_0": "Это очень мило с твоей стороны.",
    "dialog.npc.shepherd.gift_neutral.2.line_0": "Думаю, кому-нибудь из моих друзей это понравится!",
    "dialog.npc.shepherd.gift_neutral.3.line_0": "Ты очень добр, спасибо.",
    "dialog.npc.shepherd.gift_neutral.4.line_0": "Это выращено на твоей ферме? Никогда раньше такого не видела.",
    "dialog.npc.shepherd.gift_neutral.5.line_0": "Спасибо!",
    "dialog.npc.shepherd.gift_neutral.6.line_0": "Ах, спасибо тебе!",
    "dialog.npc.shepherd.gift_neutral.7.line_0": "Я с удовольствием возьму!",

    "dialog.npc.shepherd.gift_disliked.0.line_0": "Ох... не стоило, правда.",
    "dialog.npc.shepherd.gift_disliked.1.line_0": "Похоже, в повадках животных ты разбираешься куда лучше, чем во вкусах людей...",
    "dialog.npc.shepherd.gift_disliked.2.line_0": "Иногда лучше воздержаться от подарков, если не уверен...",
    "dialog.npc.shepherd.gift_disliked.3.line_0": "Ой!",
    "dialog.npc.shepherd.gift_disliked.4.line_0": "Ох...",
    "dialog.npc.shepherd.gift_disliked.5.line_0": "А... ладно... хорошо...",
    "dialog.npc.shepherd.gift_disliked.6.line_0": "Ты случайно не хотел подарить это кому-нибудь другому?",
    "dialog.npc.shepherd.gift_disliked.7.line_0": "Нам вовсе не обязательно дарить друг другу подарки...",

    "dialog.npc.shepherd.gift_hated.0.line_0": "Фу! Зачем ты принёс мне эту гадость?!",
    "dialog.npc.shepherd.gift_hated.1.line_0": "За что?..",
    "dialog.npc.shepherd.gift_hated.2.line_0": "...",
    "dialog.npc.shepherd.gift_hated.3.line_0": "Если хочешь, чтобы я ушла — мог бы просто сказать прямо.",
    "dialog.npc.shepherd.gift_hated.4.line_0": "Нет, спасибо, убери.",
    "dialog.npc.shepherd.gift_hated.5.line_0": "Мне от этого очень неприятно...",
    "dialog.npc.shepherd.gift_hated.6.line_0": "Я совсем не хочу принимать это...",
    "dialog.npc.shepherd.gift_hated.7.line_0": "Пожалуйста, оставь меня в покое.",
    "dialog.npc.shepherd.gift_hated.8.line_0": "Я терпеть не могу подобные злые шутки.",
    "dialog.npc.shepherd.gift_hated.9.line_0": "Прости, но я ни за что не возьму это...",
    "dialog.npc.shepherd.gift_hated.10.line_0": "Это, пожалуй, худшая вещь, которую мне когда-либо дарили в жизни...",

    "dialog.npc.shepherd.unique_five_gift.line_0": "О, здравствуй, @i! У меня к тебе небольшая просьба!",
    "dialog.npc.shepherd.unique_five_gift.line_1": "Эйс нашёл этих пингвинчиков во время экспедиции в ледяные пустоши и попросил меня позаботиться о них.",
    "dialog.npc.shepherd.unique_five_gift.line_2": "Я не хочу просто перекладывать ответственность, но я искренне доверяю тебе и знаю, что ты окружишь их теплом и заботой.",
    "dialog.npc.shepherd.unique_five_gift.line_3": "К сожалению, у меня нет возможности построить для них настоящий ледяной вольер, со мной они будут тосковать.",
    "dialog.npc.shepherd.unique_five_gift.line_4": "Если возникнут сложности с их настроением — просто купи сканер настроения у меня в лавке, для тебя он совсем дешёвый!"
};

updateMd('05_shepherd.md', shepherdTrans);
