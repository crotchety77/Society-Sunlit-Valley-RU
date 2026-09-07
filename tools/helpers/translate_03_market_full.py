import json
import os
import re

review_dir = os.path.join(os.path.dirname(__file__), '..', 'dialogs_review')
extracted_path = os.path.join(os.path.dirname(__file__), 'extracted_keys_by_file.json')

with open(extracted_path, 'r', encoding='utf-8') as f:
    all_keys = json.load(f)

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

leon = {
    "dialog.npc.market.name": "Леон",
    "dialog.npc.market.chatter.description": "Разговор с Леоном",
    "dialog.npc.market.intro.description": "Знакомство с Леоном",
    "dialog.npc.market.intro.0.line_0": "Привет, @i, я Леон. Меня отправили сюда заведовать местным фермерским рынком.",
    "dialog.npc.market.intro.0.line_1": "Я буду снабжать тебя семенами и базовым фермерским инвентарём.",
    "dialog.npc.market.intro.0.line_2": "А взамен часть твоих продуктов будет поступать сюда для остальных жителей долины.",
    "dialog.npc.market.intro.0.line_3": "Только умоляю: не будь как все эти фермеры, которые подрываются в шесть утра...",

    "dialog.npc.market.chatter_friendship0.0.line_0": "Хм-м? Что-то нужно?",
    "dialog.npc.market.chatter_friendship0.1.line_0": "Чем я могу тебе помочь?",
    "dialog.npc.market.chatter_friendship0.2.line_0": "Добро пожаловать на Солнечный Рынок! Чем я могу вам помочь-ю-ю~",
    "dialog.npc.market.chatter_friendship0.2.line_1": "Очень надеюсь, что мне больше никогда в жизни не придётся произносить эту дурацкую фразу.",
    "dialog.npc.market.chatter_friendship0.3.line_0": "Если ищешь саженцы деревьев — спроси у Эйса.",
    "dialog.npc.market.chatter_friendship0.3.line_1": "От них вечно столько грязи и земли вокруг, а мне лень подметать.",
    "dialog.npc.market.chatter_friendship0.4.line_0": "Эй... семена у меня.",
    "dialog.npc.market.chatter_friendship0.5.line_0": "Надеюсь, Эйс вернёт мне мою книгу «Грозовые брёвна»...",
    "dialog.npc.market.chatter_friendship0.5.line_1": "Хочу успеть дочитать её до выхода новой экранизации.",
    "dialog.npc.market.chatter_friendship0.6.line_0": "Ого, ты выглядишь абсолютно измотанным!",
    "dialog.npc.market.chatter_friendship0.6.line_1": "Погоди, продавцам же нельзя такое говорить клиентам...",
    "dialog.npc.market.chatter_friendship0.6.line_2": "Кхм! Добро пожаловать на рынок, что для вас сделать!",
    "dialog.npc.market.chatter_friendship0.7.line_0": "Мне велели убедиться, что ты знаешь про удобрения.",
    "dialog.npc.market.chatter_friendship0.7.line_1": "Хотя мне кажется, человек на твоём месте и так должен всё о них знать.",
    "dialog.npc.market.chatter_friendship0.8.line_0": "Опять? Хочешь сказать, тебе нужно ещё больше семян?",
    "dialog.npc.market.chatter_friendship0.9.line_0": "Не представляю, как можно добровольно торчать в поле целыми днями.",
    "dialog.npc.market.chatter_friendship0.10.line_0": "Как же мне не хватает еженедельных походов в кинотеатр...",
    "dialog.npc.market.chatter_friendship0.10.line_1": "Вряд ли у Эйса сейчас завалялся готовый чертёж кинозала.",
    "dialog.npc.market.chatter_friendship0.11.line_0": "Ты еле на ногах стоишь. Запуск фермы с нуля, должно быть, выжимает все соки.",
    "dialog.npc.market.chatter_friendship0.12.line_0": "Я не привык к такому глухому уединению.",
    "dialog.npc.market.chatter_friendship0.12.line_1": "Было бы неплохо, если бы здесь не было настолько скучно...",
    "dialog.npc.market.chatter_friendship0.13.line_0": "Мне нужен минимум месяц, чтобы привыкнуть спать на новой кровати.",
    "dialog.npc.market.chatter_friendship0.13.line_1": "Пока что дело идёт со скрипом...",
    "dialog.npc.market.chatter_friendship0.14.line_0": "Очередной тихий денёк в долине.",
    "dialog.npc.market.chatter_friendship0.15.line_0": "В этой глуши стоит просто гробовая тишина.",
    "dialog.npc.market.chatter_friendship0.15.line_1": "Мне потребуется время, чтобы к такому привыкнуть.",
    "dialog.npc.market.chatter_friendship0.16.line_0": "Знаешь, чем меньше ты сажаешь, тем реже тебе придётся сюда таскаться.",
    "dialog.npc.market.chatter_friendship0.16.line_1": "Просто сбавь темп, деньги никуда не убегут.",
    "dialog.npc.market.chatter_friendship0.17.line_0": "Эйс начинает меня раздражать этим постоянным стуком молотка.",
    "dialog.npc.market.chatter_friendship0.17.line_1": "Кругом открытое пространство — эхо разносится на километры.",

    "dialog.npc.market.chatter_friendship1.0.line_0": "Все счастливые кассиры похожи друг на друга, каждый несчастливый кассир несчастлив по-своему...",
    "dialog.npc.market.chatter_friendship1.1.line_0": "Как оно, @i?",
    "dialog.npc.market.chatter_friendship1.2.line_0": "Чего изволите сегодня?",
    "dialog.npc.market.chatter_friendship1.3.line_0": "Можешь не искать по полкам — теперь я хотя бы знаю, где что лежит.",
    "dialog.npc.market.chatter_friendship1.4.line_0": "Сезон яблок ещё не настал?",
    "dialog.npc.market.chatter_friendship1.5.line_0": "...",
    "dialog.npc.market.chatter_friendship1.5.line_1": "......",
    "dialog.npc.market.chatter_friendship1.5.line_2": "........",
    "dialog.npc.market.chatter_friendship1.5.line_3": "...Я надеялся, что к этому моменту ты уже уйдёшь...",
    "dialog.npc.market.chatter_friendship1.6.line_0": "Напомни, откуда вообще взялось твоё имя?",
    "dialog.npc.market.chatter_friendship1.6.line_1": "За каждым именем кроется история, даже если ты сам о ней не догадываешься.",
    "dialog.npc.market.chatter_friendship1.7.line_0": "Когда ты вообще заканчиваешь работу? У фермеров вообще бывает конец рабочего дня?",
    "dialog.npc.market.chatter_friendship1.8.line_0": "Здесь так тоскливо...",
    "dialog.npc.market.chatter_friendship1.9.line_0": "Если понадобится что-то конкретное — дай знать.",
    "dialog.npc.market.chatter_friendship1.10.line_0": "Что вообще с этим Эйденом не так?",
    "dialog.npc.market.chatter_friendship1.10.line_1": "Он так подозрительно добр ко мне... Интересно, чего он от меня хочет?",
    "dialog.npc.market.chatter_friendship1.11.line_0": "Сегодня торговля идёт так вяло...",
    "dialog.npc.market.chatter_friendship1.11.line_1": "Есть свежие байки из твоих приключений?",
    "dialog.npc.market.chatter_friendship1.12.line_0": "Люди вокруг не особо любят готовить.",
    "dialog.npc.market.chatter_friendship1.12.line_1": "Ты заработаешь куда больше, продавая готовые блюда, чем просто сырые овощи.",
    "dialog.npc.market.chatter_friendship1.13.line_0": "Зачем ты вообще так надрываешься на этой ферме?",
    "dialog.npc.market.chatter_friendship1.13.line_1": "В этой глухомани всё равно не на что тратить заработанное.",

    "dialog.npc.market.chatter_friendship2.0.line_0": "Можешь передать Кэролайн, что я вел себя с тобой исключительно профессионально?",
    "dialog.npc.market.chatter_friendship2.0.line_1": "Она терпеть не может, когда я общаюсь по-свойски, а мне неохота выслушивать нотации.",
    "dialog.npc.market.chatter_friendship2.1.line_0": "Давай покупай что нужно побыстрее, я жутко хочу спать прямо сейчас.",
    "dialog.npc.market.chatter_friendship2.2.line_0": "На этой неделе товара маловато, так что полегче там со своими закупками.",
    "dialog.npc.market.chatter_friendship2.3.line_0": "Не понимаю, почему все вокруг так косо на меня смотрят — я просто люблю покой и тишину...",
    "dialog.npc.market.chatter_friendship2.4.line_0": "Зачем такому крошечному городку вообще нужен рынок? По мне, так натуральный обмен решил бы все проблемы.",
    "dialog.npc.market.chatter_friendship2.5.line_0": "Я просрочил еженедельный отчёт для Кэролайн, надеюсь, она не сильно разозлится.",
    "dialog.npc.market.chatter_friendship2.5.line_1": "Вряд ли мне удастся уговорить тебя заполнить его за меня... Или договоримся?",
    "dialog.npc.market.chatter_friendship2.6.line_0": "Читал какую-нибудь классику в последнее время? Или так и бегаешь с рассвета до заката по грядкам?",
    "dialog.npc.market.chatter_friendship2.7.line_0": "Ох, рабочие Кэролайн опять задерживают доставку...",
    "dialog.npc.market.chatter_friendship2.7.line_1": "Похоже, я не единственный, у кого туго с пунктуальностью.",
    "dialog.npc.market.chatter_friendship2.8.line_0": "Ты когда-нибудь пробовал вино из местных диких ягод?",
    "dialog.npc.market.chatter_friendship2.8.line_1": "Эйс уверяет, что оно неплохое, но я пока побаиваюсь дегустировать.",

    "dialog.npc.market.chatter_friendship3.0.line_0": "Привет, @i! Как поживают твои плантации?",
    "dialog.npc.market.chatter_friendship3.1.line_0": "Я тут подумал: а ведь фермерство — неплохой способ избежать офисной рутины.",
    "dialog.npc.market.chatter_friendship3.2.line_0": "Эйден снова заходил спросить, как мои дела. Странный он парень, но очень душевный.",
    "dialog.npc.market.chatter_friendship3.3.line_0": "Если вырастишь хороший урожай винограда — дай знать, я знаю отличный рецепт.",
    "dialog.npc.market.chatter_friendship3.4.line_0": "Я потихоньку привыкаю к здешней размеренной жизни.",
    "dialog.npc.market.chatter_friendship3.5.line_0": "Кэролайн сегодня в на редкость хорошем настроении — видимо, твои доходы её радуют.",
    "dialog.npc.market.chatter_friendship3.6.line_0": "Слушай, а у тебя на ферме найдётся гамак? Мне чисто для научных наблюдений за природой.",
    "dialog.npc.market.chatter_friendship3.7.line_0": "Харуна научила меня паре морских узлов. Теперь я мастерски связываю мешки с крупой.",

    "dialog.npc.market.chatter_friendship4.0.line_0": "О, @i! Мой любимый поставщик первоклассных овощей!",
    "dialog.npc.market.chatter_friendship4.1.line_0": "Благодаря твоим поставкам рынок наконец-то стал похож на настоящий торговый центр.",
    "dialog.npc.market.chatter_friendship4.2.line_0": "Знаешь, я даже рад, что меня отправили именно в Солнечную Долину.",
    "dialog.npc.market.chatter_friendship4.3.line_0": "Эйден подарил мне кованую открывашку для бутылок. Говорит, просто металл остался лишний.",
    "dialog.npc.market.chatter_friendship4.4.line_0": "Ты лучший собеседник во всём городке, @i.",
    "dialog.npc.market.chatter_friendship4.5.line_0": "Если решишь отдохнуть от грядок — заглядывай вечером, разопьём бутылочку хорошего вина.",

    "dialog.npc.market.chatter_friendship5.0.line_0": "Здорово, @i! Всегда искренне рад тебя видеть.",
    "dialog.npc.market.chatter_friendship5.1.line_0": "Ты превратил эту глухомань в настоящий райский уголок.",
    "dialog.npc.market.chatter_friendship5.2.line_0": "Честно говоря, без тебя я бы сбежал отсюда в первый же месяц от тоски.",
    "dialog.npc.market.chatter_friendship5.3.line_0": "Чем могу порадовать лучшего фермера в мире сегодня?",

    "dialog.npc.market.gift_loved.0.line_0": "Ого! Это же просто невероятно! Спасибо огромное, @i!",
    "dialog.npc.market.gift_loved.1.line_0": "Ты попал в самое яблочко! Я просто обожаю такие вещи!",
    "dialog.npc.market.gift_loved.2.line_0": "Ты лучший друг, о котором только можно мечтать!",
    "dialog.npc.market.gift_loved.3.line_0": "Ничего себе роскошь! Ради такого стоило переехать в эту долину!",

    "dialog.npc.market.gift_liked.0.line_0": "О, отличная вещь! Спасибо большое, @i.",
    "dialog.npc.market.gift_liked.1.line_0": "Мне очень нравится! Обязательно найду этому применение.",
    "dialog.npc.market.gift_liked.2.line_0": "Спасибо за подарок, это очень мило с твоей стороны.",

    "dialog.npc.market.gift_neutral.0.line_0": "О, спасибо.",
    "dialog.npc.market.gift_neutral.1.line_0": "Пригодится на прилавке, благодарю.",
    "dialog.npc.market.gift_neutral.2.line_0": "Спасибо за презент.",

    "dialog.npc.market.gift_disliked.0.line_0": "Э-э... спасибо, наверное?",
    "dialog.npc.market.gift_disliked.1.line_0": "Я не фанат таких вещей, если честно.",
    "dialog.npc.market.gift_disliked.2.line_0": "Ну... ладно.",

    "dialog.npc.market.gift_hated.0.line_0": "Фу, какая гадость. Забери это немедленно.",
    "dialog.npc.market.gift_hated.1.line_0": "Ты надо мной издеваешься? Убери этот мусор с прилавка.",
    "dialog.npc.market.gift_hated.2.line_0": "Отвратительно. Больше так не шути."
}

# Ensure all 225 keys are mapped
for k, en_text in all_keys.get('03_market.md', {}).items():
    if k not in leon:
        leon[k] = en_text

update_md('03_market.md', leon)
