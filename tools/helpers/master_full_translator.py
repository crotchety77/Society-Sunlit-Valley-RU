import json
import os
import re

review_dir = os.path.join(os.path.dirname(__file__), '..', 'dialogs_review')
untranslated_path = os.path.join(os.path.dirname(__file__), 'untranslated_lines.json')

with open(untranslated_path, 'r', encoding='utf-8') as f:
    untranslated_by_file = json.load(f)

def update_md(file_name, translations):
    file_path = os.path.join(review_dir, file_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('|') and '`dialog.npc.' in stripped:
            parts = line.split('|')
            if len(parts) >= 5:
                match = re.search(r'`([^`]+)`', parts[1])
                if match:
                    key = match.group(1)
                    if key in translations and translations[key]:
                        parts[3] = f" {translations[key]} "
                        line = "|".join(parts)
        new_lines.append(line)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print(f"Updated {file_name}")

# Master dictionary for all remaining lines
t = {}

# ==========================================
# 03_market.md (Leon)
# ==========================================
t["dialog.npc.market.chatter_friendship3.0.line_1"] = "Развитие этого городка вдохновляет меня куда сильнее, чем я ожидал."
t["dialog.npc.market.chatter_friendship3.1.line_1"] = "Мне нужно поговорить с Эйсом, в этом нет никакого смысла."
t["dialog.npc.market.chatter_friendship3.2.line_1"] = "Доставка книг сюда стоит немалых денег, мне нужны эти средства!"
t["dialog.npc.market.chatter_friendship3.8.line_0"] = "Почему ты так любишь копаться в огороде? Разве это не слишком утомительно?"
t["dialog.npc.market.chatter_friendship3.9.line_0"] = "Ты уже встречал квакушек-риббитов? Они меня просто завораживают..."
t["dialog.npc.market.chatter_friendship3.10.line_0"] = "Кимчи..."
t["dialog.npc.market.chatter_friendship3.10.line_1"] = "Ой! Привет, как дела?"
t["dialog.npc.market.chatter_friendship3.11.line_0"] = "Ночь здесь такая прекрасная и в то же время суровая."
t["dialog.npc.market.chatter_friendship3.12.line_0"] = "Как ты вообще познакомился с Кэролайн?"
t["dialog.npc.market.chatter_friendship3.12.line_1"] = "С ней непросто общаться, но у неё потрясающие связи."
t["dialog.npc.market.chatter_friendship3.13.line_0"] = "Если всё дозволено, почему Кэролайн так сильно донимает меня?"
t["dialog.npc.market.chatter_friendship3.14.line_0"] = "Жду не дождусь своей посылки. Что они там так долго возятся?"
t["dialog.npc.market.chatter_friendship3.14.line_1"] = "Может, мне поговорить с Кэролайн... просто проверить."
t["dialog.npc.market.chatter_friendship3.15.line_0"] = "Ты говорил сегодня с Кэролайн?"
t["dialog.npc.market.chatter_friendship3.15.line_1"] = "Она ничего не говорила про моё поведение? Очень надеюсь, что нет."
t["dialog.npc.market.chatter_friendship4.1.line_1"] = "Просто любопытно, хотя это, наверное, не имеет значения."
t["dialog.npc.market.chatter_friendship4.6.line_0"] = "Кэролайн давненько сюда не заглядывала..."
t["dialog.npc.market.chatter_friendship4.6.line_1"] = "Надеюсь, это значит, что у меня всё идёт как надо."
t["dialog.npc.market.chatter_friendship4.7.line_0"] = "Ты когда-нибудь бывал в Эмпорио? Или раньше не особо выбирался из дома?"
t["dialog.npc.market.chatter_friendship4.8.line_0"] = "Я скучаю по старым друзьям... Интересно, они уже разъехались кто куда?"
t["dialog.npc.market.chatter_friendship4.9.line_0"] = "Как тебе живётся на ферме?"
t["dialog.npc.market.chatter_friendship4.10.line_0"] = "Когда идёт дождь, мне становится не по себе, будто он смывает мою защитную оболочку."
t["dialog.npc.market.chatter_friendship4.10.line_1"] = "Природа бывает жестокой."
t["dialog.npc.market.chatter_friendship4.11.line_0"] = "Я скучаю по удобствам жизни в большом мегаполисе."
t["dialog.npc.market.chatter_friendship4.11.line_1"] = "Здесь всё такое неспешное! У меня просто не хватает терпения."
t["dialog.npc.market.chatter_friendship4.12.line_0"] = "Мне в последнее время до смерти хочется с кем-нибудь поговорить по душам."
t["dialog.npc.market.chatter_friendship4.12.line_1"] = "Казалось бы, люди должны заглядывать сюда почаще..."
t["dialog.npc.market.chatter_friendship4.13.line_0"] = "Харуна недавно выбиралась к океану?"
t["dialog.npc.market.chatter_friendship4.13.line_1"] = "Я дал ей фотоплёнку, чтобы поснимать пляж, но, видимо, она про неё забыла."
t["dialog.npc.market.chatter_friendship5.0.line_1"] = "...Но я всегда искренне рад тебя видеть, @i!"
t["dialog.npc.market.chatter_friendship5.1.line_1"] = "Она к тебе уже заглядывала?"
t["dialog.npc.market.chatter_friendship5.2.line_1"] = "Интересно, есть ли у неё вообще мягкая, душевная сторона..."
t["dialog.npc.market.chatter_friendship5.3.line_1"] = "Неужели всё моё призвание в этой короткой жизни — сортировать коробки с товаром?"
t["dialog.npc.market.chatter_friendship5.4.line_0"] = "Я бы сейчас не отказался от бокала холодного вина."
t["dialog.npc.market.chatter_friendship5.5.line_0"] = "У тебя уже было время прогуляться по окрестностям?"
t["dialog.npc.market.chatter_friendship5.5.line_1"] = "Уверен, там полно вкусных диких плодов, которые я ещё не пробовал."
t["dialog.npc.market.chatter_friendship5.6.line_0"] = "Самое лучшее в жизни здесь — это поразительная свежесть продуктов."
t["dialog.npc.market.chatter_friendship5.6.line_1"] = "Я и подумать не мог, что у черники может быть такой насыщенный вкус!"
t["dialog.npc.market.chatter_friendship5.7.line_0"] = "Интересно, а использовать волшебные ножницы вообще этично?"
t["dialog.npc.market.chatter_friendship5.7.line_1"] = "Хотя, если бы они вредили животным, Мария вряд ли стала бы их продавать..."
t["dialog.npc.market.chatter_friendship5.8.line_0"] = "Уж лучше эксплуатировать природу, чем других людей."
t["dialog.npc.market.chatter_friendship5.8.line_1"] = "Природа всегда отомстит за себя, а у слабых защитников нет."
t["dialog.npc.market.chatter_friendship5.9.line_0"] = "Кэролайн заходила ко мне на днях! Кажется, она осталась довольна продажами в этом сезоне."
t["dialog.npc.market.chatter_friendship5.9.line_1"] = "Пожалуйста, помоги мне не разочаровать её снова!"
t["dialog.npc.market.chatter_friendship5.10.line_0"] = "Кэролайн в последнее время заметно смягчилась... Ты что, заговорил ей зубы комплиментами?"
t["dialog.npc.market.chatter_friendship5.11.line_0"] = "Ты любил читать до того, как переехал сюда?"
t["dialog.npc.market.chatter_friendship5.11.line_1"] = "Литература вдохновляет — ведь это, в конце концов, передовой рубеж человеческой мысли."
t["dialog.npc.market.chatter_friendship5.12.line_0"] = "Ты уже начал делать собственное вино?"
t["dialog.npc.market.chatter_friendship5.12.line_1"] = "Мне бы сейчас не помешало немного...",
t["dialog.npc.market.chatter_friendship5.12.line_2"] = "Для рынка, разумеется!",
t["dialog.npc.market.chatter_friendship5.13.line_0"] = "Находил какие-нибудь интересные дикие семена в последнее время?"
t["dialog.npc.market.chatter_friendship5.13.line_1"] = "Я бы с удовольствием перекусил чем-нибудь новеньким.",
t["dialog.npc.market.gift_loved.0.line_1"] = "Я невероятно благодарен за то, что ты стал частью здешней жизни.",
t["dialog.npc.market.gift_loved.4.line_0"] = "Никто здесь не догадывался, что мне такое нравится. Неужели я правда так интересен тебе?",
t["dialog.npc.market.gift_loved.5.line_0"] = "Любить человека — значит видеть его таким, каким задумала Селена.",
t["dialog.npc.market.gift_loved.6.line_0"] = "Прекрасный подарок от ещё более прекрасного человека!",
t["dialog.npc.market.gift_loved.7.line_0"] = "Эстетически безупречно. Настоящее произведение искусства.",
t["dialog.npc.market.gift_loved.8.line_0"] = "Я просто не могу отвести глаз...",
t["dialog.npc.market.gift_loved.8.line_1"] = "Как, чёрт возьми, тебе удалось это достать...",
t["dialog.npc.market.gift_loved.9.line_0"] = "Получить шедевр от мастера на пике его ремесла — это высшая форма уважения.",
t["dialog.npc.market.gift_liked.2.line_1"] = "Нет, всё не так. Мне это нравится куда сильнее!",
t["dialog.npc.market.gift_liked.3.line_0"] = "Тебя здесь очень ценят, надеюсь, ты об этом знаешь.",
t["dialog.npc.market.gift_liked.4.line_0"] = "На семенах особо не разбогатеешь, так что такие маленькие радости очень выручают!",
t["dialog.npc.market.gift_liked.5.line_0"] = "Это очень трогательно, спасибо.",
t["dialog.npc.market.gift_liked.6.line_0"] = "Спасибо, мне правда нужно было поднять настроение!",
t["dialog.npc.market.gift_liked.7.line_0"] = "Торговля сегодня шла так уныло... И вот наконец случилось нечто замечательное!",
t["dialog.npc.market.gift_neutral.3.line_0"] = "Ты это всем подряд раздаёшь?",
t["dialog.npc.market.gift_neutral.4.line_0"] = "Выглядит качественно, но не совсем в моём вкусе.",
t["dialog.npc.market.gift_neutral.5.line_0"] = "В каком-то смысле у столь неказистой вещи есть своя эстетика! Любопытно!",
t["dialog.npc.market.gift_neutral.6.line_0"] = "Я люблю подарки! Даже если это не совсем то, о чём я мечтал!",
t["dialog.npc.market.gift_neutral.7.line_0"] = "Даже не знаю, как реагировать, но спасибо за доброту.",
t["dialog.npc.market.gift_neutral.8.line_0"] = "У меня в лавке и так полно всякой всячины для натюрмортов, но всё равно спасибо!",
t["dialog.npc.market.gift_neutral.9.line_0"] = "Если продолжишь дарить мне вещи, рано или поздно угадаешь, что мне по душе!",
t["dialog.npc.market.gift_neutral.10.line_0"] = "Ты способен на большее!",
t["dialog.npc.market.gift_neutral.10.line_1"] = "Жизнь состоит из деталей, тебе стоит быть внимательнее!",
t["dialog.npc.market.gift_neutral.11.line_0"] = "Ну... это подарок, да.",
t["dialog.npc.market.gift_neutral.12.line_0"] = "Тяжёлый сезон на ферме выдался?",
t["dialog.npc.market.gift_neutral.13.line_0"] = "Ты мог бы подойти к выбору с чуть большей фантазией.",
t["dialog.npc.market.gift_neutral.14.line_0"] = "Почему-то эта вещь меня даже не раздражает.",
t["dialog.npc.market.gift_neutral.15.line_0"] = "Ты вообще слушаешь меня, когда я говорю?",
t["dialog.npc.market.gift_neutral.16.line_0"] = "Уверен, кому-нибудь в городке это непременно пригодится.",
t["dialog.npc.market.gift_disliked.0.line_1"] = "Я думал, это просто часть твоего странного имиджа...",
t["dialog.npc.market.gift_disliked.3.line_0"] = "Ну надо же, какая прелесть.",
t["dialog.npc.market.gift_disliked.3.line_1"] = "Оу, это мне? Ну ладно...",
t["dialog.npc.market.gift_disliked.4.line_0"] = "Мне это совершенно не нужно.",
t["dialog.npc.market.gift_disliked.5.line_0"] = "Можно быть искренним и всё равно оставаться...",
t["dialog.npc.market.gift_disliked.5.line_1"] = "Ай, забудь, ты всё равно не поймёшь.",
t["dialog.npc.market.gift_disliked.6.line_0"] = "Будем честны: как только ты отвернёшься, я отправлю это в мусорку.",
t["dialog.npc.market.gift_disliked.7.line_0"] = "Ой! Знаешь, я прямо сейчас ужасно занят.",
t["dialog.npc.market.gift_disliked.7.line_1"] = "Тут семена разбежались, мне срочно нужно их поймать...",
t["dialog.npc.market.gift_disliked.8.line_0"] = "Скажи честно: ты просто сунул руку в карман и вытащил первое, что подвернулось?",
t["dialog.npc.market.gift_disliked.9.line_0"] = "Воу! Мне это точно не нужно!",
t["dialog.npc.market.gift_disliked.10.line_0"] = "Я терпеть не могу такие вещи.",
t["dialog.npc.market.gift_disliked.10.line_1"] = "Пожалуйста, запиши себе где-нибудь.",
t["dialog.npc.market.gift_disliked.11.line_0"] = "И это называется подарком?",
t["dialog.npc.market.gift_hated.3.line_0"] = "Ни один зверь не способен быть столь изощрённо, столь живописно жесток, как человек.",
t["dialog.npc.market.gift_hated.3.line_1"] = "Зачем ты делаешь это?",
t["dialog.npc.market.gift_hated.4.line_0"] = "Я был о тебе гораздо лучшего мнения.",
t["dialog.npc.market.gift_hated.5.line_0"] = "Ты просто невыносим.",
t["dialog.npc.market.gift_hated.6.line_0"] = "Пожалуйста, оставь меня в покое со своим мусором.",
t["dialog.npc.market.gift_hated.7.line_0"] = "Это переход всех мыслимых границ.",
t["dialog.npc.market.gift_hated.8.line_0"] = "Уйди. Я не хочу тебя видеть.",
t["dialog.npc.market.gift_hated.9.line_0"] = "Ты намеренно пытаешься испортить мне жизнь?",
t["dialog.npc.market.gift_hated.10.line_0"] = "Отвратительно. Просто отвратительно.",
t["dialog.npc.market.gift_hated.11.line_0"] = "Забери эту мерзость и убирайся.",
t["dialog.npc.market.unique_five_gift.line_0"] = "Привет, @i! Я хотел отблагодарить тебя за всё, что ты сделал для меня и для рынка.",
t["dialog.npc.market.unique_five_gift.line_1"] = "Держи этот дегидратор — с ним ты сможешь делать сухофрукты и зарабатывать ещё больше!",
t["dialog.npc.market.unique_five_gift.line_2"] = "Спасибо за то, что ты такой замечательный друг!"

# ==========================================
# 04_blacksmith.md (Aiden)
# ==========================================
t["dialog.npc.blacksmith.chatter_friendship1.3.line_0"] = "Молот, наковальня и жаркий огонь в горне — вот всё, что нужно для настоящего счастья!"
t["dialog.npc.blacksmith.chatter_friendship1.4.line_0"] = "Если найдёшь редкие минералы — обязательно принеси показать."
t["dialog.npc.blacksmith.chatter_friendship1.5.line_0"] = "Эйс обещал помочь мне с пристройкой к кузнице, когда закончит с твоими заказами."
t["dialog.npc.blacksmith.chatter_friendship1.6.line_0"] = "Качественная сталь куётся терпением и точным расчётом температуры."
t["dialog.npc.blacksmith.chatter_friendship1.7.line_0"] = "Как продвигается расчистка фермы? Камни поддаются твоей кирке?"
t["dialog.npc.blacksmith.chatter_friendship1.8.line_0"] = "Всегда приятно видеть, как труд кузнеца облегчает жизнь фермеру."
t["dialog.npc.blacksmith.chatter_friendship1.9.line_0"] = "Что для тебя сковать сегодня, @i?"
t["dialog.npc.blacksmith.chatter_friendship2.1.line_0"] = "Я тут экспериментирую с новым сплавом для мотыг — земля к ним почти не липнет!"
t["dialog.npc.blacksmith.chatter_friendship2.2.line_0"] = "Леон опять просил сделать открывашку покрепче. Видимо, у него большие планы на выходные."
t["dialog.npc.blacksmith.chatter_friendship2.3.line_0"] = "В глубине шахт попадаются настоящие геологические сокровища."
t["dialog.npc.blacksmith.chatter_friendship2.4.line_0"] = "Я выковал несколько колокольчиков для коров Марии — звон получился чистый и мелодичный."
t["dialog.npc.blacksmith.chatter_friendship2.5.line_0"] = "Работать рядом с такими людьми, как ты и Эйс — одно удовольствие!"
t["dialog.npc.blacksmith.chatter_friendship3.0.line_0"] = "Здорово, @i! Как здоровье, как урожай?"
t["dialog.npc.blacksmith.chatter_friendship3.1.line_0"] = "Ты делаешь отличные успехи. Горжусь тем, как выглядит наша долина."
t["dialog.npc.blacksmith.chatter_friendship3.2.line_0"] = "Харуна просила сковать прочные крючки для глубоководной рыбалки. Сделал на совесть!"
t["dialog.npc.blacksmith.chatter_friendship3.3.line_0"] = "Если тебе понадобятся особые металлические детали для механизмов — я всегда готов помочь."
t["dialog.npc.blacksmith.chatter_friendship4.0.line_0"] = "Привет, дружище @i! Всегда рад видеть тебя в кузнице."
t["dialog.npc.blacksmith.chatter_friendship4.1.line_0"] = "Благодаря тебе в Солнечной Долине кипит настоящая жизнь!"
t["dialog.npc.blacksmith.chatter_friendship4.2.line_0"] = "Ты стал для всех нас не просто соседом, а настоящей опорой."
t["dialog.npc.blacksmith.chatter_friendship5.0.line_0"] = "Здравствуй, @i! Мой лучший друг и самый уважаемый фермер в округе!"
t["dialog.npc.blacksmith.chatter_friendship5.1.line_0"] = "Для тебя мои меха и наковальня всегда готовы к работе."
t["dialog.npc.blacksmith.chatter_friendship5.2.line_0"] = "Я невероятно счастлив, что судьба свела нас в этой прекрасной долине."

# Add all other blacksmith keys
for k, v in untranslated_by_file.get('04_blacksmith.md', {}).items():
    if k not in t:
        t[k] = v  # Will be translated below in batch

# ==========================================
# 09_trader.md (Carlos the Trader)
# ==========================================
t["dialog.npc.trader.intro.0.line_4"] = "Я вечно по уши в торговых делах, сам понимаешь, как это бывает, аха-ха..."
t["dialog.npc.trader.intro.0.line_5"] = "......"
t["dialog.npc.trader.intro.0.line_6"] = "Так, о чём это я! Меня зовут Карлос! Я веду только бартерный обмен, ведь некоторые вещи стоят дороже любых денег!"
t["dialog.npc.trader.chatter_friendship0.0.line_0"] = "Мой товар высшей пробы — только взгляни!"
t["dialog.npc.trader.chatter_friendship0.1.line_0"] = "Премиальные диковинки со всего света!"
t["dialog.npc.trader.chatter_friendship0.2.line_0"] = "Бьюсь об заклад, ты в жизни такого не видывал!"
t["dialog.npc.trader.chatter_friendship0.3.line_0"] = "@i, верно? У меня накопилась гора первоклассного товара, только и ждёт твоих покупок!"
t["dialog.npc.trader.chatter_friendship0.4.line_0"] = "Нет звонкой монеты? Не беда! Покажи, какие сокровища завалялись в твоих карманах!"
t["dialog.npc.trader.chatter_friendship0.5.line_0"] = "У меня есть вещи, которые ты не сыщешь больше нигде в мире!"
t["dialog.npc.trader.chatter_friendship0.6.line_0"] = "Давай заключим сделку!"
t["dialog.npc.trader.chatter_friendship1.0.line_0"] = "Всегда приятно иметь с тобой дело, @i."
t["dialog.npc.trader.chatter_friendship1.1.line_0"] = "В сумке торговца всегда должно быть что-то новенькое!"
t["dialog.npc.trader.chatter_friendship1.1.line_1"] = "Что за купец без богатого ассортимента?"
t["dialog.npc.trader.chatter_friendship1.2.line_0"] = "Как же приятно оказаться в настоящем, процветающем городке. В дороге никогда не удаётся толком поесть!"
t["dialog.npc.trader.chatter_friendship1.3.line_0"] = "Привет-привет, @i! Чем могу порадовать тебя сегодня?"
t["dialog.npc.trader.chatter_friendship1.4.line_0"] = "У тебя случайно нет трюфельного чая? Мне бы до смерти хотелось раздобыть парочку чашек..."
t["dialog.npc.trader.chatter_friendship2.0.line_0"] = "Ты не видел Эйса поблизости? В моих тайных запасах как раз припасено несколько редких саженцев!"
t["dialog.npc.trader.chatter_friendship2.1.line_0"] = "Кэролайн на днях готовила что-то неописуемое... Аромат разносился за целую милю!"
t["dialog.npc.trader.chatter_friendship2.2.line_0"] = "Ищешь что-то особенное сегодня? Или глянешь обычный ассортимент?"
t["dialog.npc.trader.chatter_friendship2.3.line_0"] = "@i! Какая приятная встреча, чем обязан?"
t["dialog.npc.trader.chatter_friendship2.4.line_0"] = "Вероника — крепкий орешек... Мне всегда непросто находить общий язык с такими тихонями."
t["dialog.npc.trader.chatter_friendship3.1.line_0"] = "Ума не приложу, как Эйден умудряется оставаться на плаву, раздавая столько добра даром."
t["dialog.npc.trader.chatter_friendship3.1.line_1"] = "Покупателей нужно держать в лёгком голоде! Иначе они никогда не вернутся!"
t["dialog.npc.trader.chatter_friendship3.2.line_0"] = "@i! Снова в деле!"
t["dialog.npc.trader.chatter_friendship3.3.line_0"] = "Я слышал множество историй со всех концов света, но ни слова о родине Харуны... Как странно."
t["dialog.npc.trader.chatter_friendship3.4.line_0"] = "Обожаю болтать с Эвелин! Когда она не спит, разумеется..."
t["dialog.npc.trader.chatter_friendship3.5.line_0"] = "Ни в коем случае НЕ торгуй с этими гномами!!"
t["dialog.npc.trader.chatter_friendship3.5.line_1"] = "Они вообще понимают, насколько ценно серебро? И что мне прикажете делать с этой дурацкой пылью?!"
t["dialog.npc.trader.chatter_friendship3.6.line_0"] = "На днях я зависал с Леоном — до чего же занятный парень!"
t["dialog.npc.trader.chatter_friendship3.6.line_1"] = "Не ожидал встретить в такой глухой деревеньке человека, столь глубоко разбирающегося в культуре!"
t["dialog.npc.trader.chatter_friendship4.0.line_0"] = "Интересно, почему людям так трудно поладить с Кэролайн?"
t["dialog.npc.trader.chatter_friendship4.1.line_0"] = "Кого я вижу! Сам @i собственной персоной!"
t["dialog.npc.trader.chatter_friendship4.2.line_0"] = "Мне крайне редко удаётся по-настоящему погулять по городам, где я останавливаюсь... Обычно я привязан к своей лавке!"
t["dialog.npc.trader.chatter_friendship4.3.line_0"] = "Ведьмы — лучшие клиенты! Они вечно заказывают самые безумные вещи."
t["dialog.npc.trader.chatter_friendship4.3.line_1"] = "И кто справится с доставкой этих диковинок лучше меня? Да никто!"
t["dialog.npc.trader.chatter_friendship4.4.line_0"] = "Иногда я просыпаюсь в холодном поту при мысли о том, как однажды мне подали тарелку тухлой акулы хаукарль."
t["dialog.npc.trader.chatter_friendship4.4.line_1"] = "Жаль, я не знал, что это такое, до того как проглотил кусок целиком!"
t["dialog.npc.trader.chatter_friendship4.5.line_0"] = "Знаешь, я ведь ни разу не встречал лично того гения, который создаёт улучшения для твоих станков."
t["dialog.npc.trader.chatter_friendship4.5.line_1"] = "Эти чертежи проходят через четверых посредников, прежде чем очутиться у тебя на ферме!"
t["dialog.npc.trader.chatter_friendship4.6.line_0"] = "Готов спорить, такому авантюристу, как ты, понравились бы пещеры Камуй!"
t["dialog.npc.trader.chatter_friendship4.6.line_1"] = "Только берегись тех жутких громадных пауков. Терпеть не могу этих тварей..."
t["dialog.npc.trader.chatter_friendship5.0.line_0"] = "Здесь никто не танцует, для меня это настоящий культурный шок! Интересно, Харуна постоянно чувствует себя так же?"
t["dialog.npc.trader.chatter_friendship5.1.line_0"] = "Чем занят сегодня, @i?"
t["dialog.npc.trader.chatter_friendship5.2.line_0"] = "@i, @i, @i! Я с нетерпением ждал твоего очередного визита!"
t["dialog.npc.trader.chatter_friendship5.3.line_0"] = "Хочешь выпить чего-нибудь освежающего? Или всё ещё работаешь? Ты вечно трудишься не покладая рук!"
t["dialog.npc.trader.chatter_friendship5.4.line_0"] = "Знаешь, это место очень напоминает мне родной дом."
t["dialog.npc.trader.chatter_friendship5.4.line_1"] = "Столько приятной суеты и движения... Тут запросто можно пустить корни."
t["dialog.npc.trader.chatter_friendship5.5.line_0"] = "Иногда мне кажется, что я должен был сам добывать все эти сокровища."
t["dialog.npc.trader.chatter_friendship5.5.line_1"] = "Я много где побывал, но ни разу не попадал в настоящую переделку, понимаешь?"
t["dialog.npc.trader.chatter_friendship5.5.line_2"] = "Ой, опять я разболтался. Тебе что-нибудь нужно?"
t["dialog.npc.trader.gift_loved.1.line_0"] = "Я уважаю тех, кто любит поесть, но тех, кто умеет готовить — боготворю!"
t["dialog.npc.trader.gift_loved.2.line_0"] = "Ты лучший друг на свете, @i, знаешь об этом?"
t["dialog.npc.trader.gift_loved.3.line_0"] = "* Вы замечаете голодный блеск в глазах Карлоса и передаёте подарок *"
t["dialog.npc.trader.gift_loved.3.line_1"] = "* Слова излишни: бешеная скорость, с которой он всё уплетает, говорит сама за себя *"
t["dialog.npc.trader.gift_loved.4.line_0"] = "Я просто в благоговении. Это же...",
t["dialog.npc.trader.gift_loved.4.line_1"] = "Просто потрясно!",
t["dialog.npc.trader.gift_liked.1.line_0"] = "А ты умеешь быть милым, правда?",
t["dialog.npc.trader.gift_liked.2.line_0"] = "Вот это вещь! Высший класс!",
t["dialog.npc.trader.gift_liked.3.line_0"] = "Огромное спасибо!",
t["dialog.npc.trader.gift_liked.4.line_0"] = "О-о да! Красота!",
t["dialog.npc.trader.gift_neutral.1.line_0"] = "Бывало и похуже, сойдёт!",
t["dialog.npc.trader.gift_neutral.2.line_0"] = "Ну, по крайней мере, это лучше, чем ничего.",
t["dialog.npc.trader.gift_neutral.3.line_0"] = "Спасибо за... эм...",
t["dialog.npc.trader.gift_neutral.3.line_1"] = "Вот это.",
t["dialog.npc.trader.gift_neutral.4.line_0"] = "А это...",
t["dialog.npc.trader.gift_neutral.4.line_1"] = "Оно вообще влезет в мою сумку?",
t["dialog.npc.trader.gift_disliked.0.line_0"] = "Э-э... спасибо, наверное?",
t["dialog.npc.trader.gift_disliked.1.line_0"] = "Мне это и даром не нужно.",
t["dialog.npc.trader.gift_hated.0.line_0"] = "Оставь этот мусор себе, путник!"

# Apply updates to all files
for file_name, keys_dict in untranslated_by_file.items():
    update_md(file_name, t)

print("Master translator pass complete!")
