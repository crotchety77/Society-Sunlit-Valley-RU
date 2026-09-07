import json
import os
import re

review_dir = os.path.join(os.path.dirname(__file__), '..', 'dialogs_review')

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

caroline = {
    "dialog.npc.banker.name": "Кэролайн",
    "dialog.npc.banker.chatter.description": "Разговор с Кэролайн",
    "dialog.npc.banker.intro.description": "Знакомство с Кэролайн",
    "dialog.npc.banker.intro.0.line_0": "Меня зовут Кэролайн. Именно я финансирую это поселение ещё с тех пор, как тебя здесь и в помине не было.",
    "dialog.npc.banker.intro.0.line_1": "Ты без разбору скупаешь все запасы у местных, так что мне придётся присматривать за здешними делами повнимательнее.",
    "dialog.npc.banker.intro.0.line_2": "У меня найдётся пара полезных вещей, которые помогут тебе грамотнее распоряжаться своими финансами.",
    "dialog.npc.banker.intro.0.line_3": "А теперь оставь меня в покое — мне нужно навести порядок в этой дыре. Я свяжусь с тобой, если что-то понадобится.",

    "dialog.npc.banker.chatter_friendship0.0.line_0": "Что тебе от меня нужно?",
    "dialog.npc.banker.chatter_friendship0.1.line_0": "Даже не надейся выпросить у меня ссуду на развитие фермы.",
    "dialog.npc.banker.chatter_friendship0.1.line_1": "Я и так делаю для поддержки этого городка более чем достаточно.",
    "dialog.npc.banker.chatter_friendship0.2.line_0": "Прости, но я не выдаю кредиты фермерам.",
    "dialog.npc.banker.chatter_friendship0.2.line_1": "Стоит случиться одному неудачному сезону, как они тут же прибегают в слезах, умоляя снизить процентные ставки.",
    "dialog.npc.banker.chatter_friendship0.3.line_0": "У меня полно важных дел прямо сейчас.",
    "dialog.npc.banker.chatter_friendship0.4.line_0": "У меня нет времени на пустую болтовню с тобой.",
    "dialog.npc.banker.chatter_friendship0.5.line_0": "Разве у тебя нет работы, которой стоило бы заняться?",
    "dialog.npc.banker.chatter_friendship0.6.line_0": "Надеюсь, ты не бьёшь баклуши, пока столько людей здесь рассчитывают на тебя.",
    "dialog.npc.banker.chatter_friendship0.7.line_0": "Ох... тебе что-то нужно от меня?",
    "dialog.npc.banker.chatter_friendship0.8.line_0": "Чего тебе?",
    "dialog.npc.banker.chatter_friendship0.9.line_0": "Развивающиеся поселения — такая обуза.",
    "dialog.npc.banker.chatter_friendship0.9.line_1": "Никакой культуры, лишь сплошной труд и грязь.",
    "dialog.npc.banker.chatter_friendship0.10.line_0": "Моё время стоит дороже твоего. Не трать его попусту.",
    "dialog.npc.banker.chatter_friendship0.11.line_0": "Сейчас ты впустую тратишь время нас обоих.",
    "dialog.npc.banker.chatter_friendship0.12.line_0": "Я вполне способна найти себе занятие и без твоих постоянных вмешательств.",
    "dialog.npc.banker.chatter_friendship0.13.line_0": "Отвлекать человека во время работы — верх невоспитанности.",
    "dialog.npc.banker.chatter_friendship0.13.line_1": "Хотя откуда у простого фермера вроде тебя взяться хорошим манерам.",
    "dialog.npc.banker.chatter_friendship0.14.line_0": "Что это за запах?",
    "dialog.npc.banker.chatter_friendship0.14.line_1": "Только не говори мне, что заявился сюда прямо с поля, даже не умывшись...",

    "dialog.npc.banker.chatter_friendship1.0.line_0": "Пожалуй, на свете бывают места и похуже этого.",
    "dialog.npc.banker.chatter_friendship1.1.line_0": "И зачем ты упорно набиваешься на разговоры?",
    "dialog.npc.banker.chatter_friendship1.1.line_1": "Надеюсь, и так очевидно, что я занята делом.",
    "dialog.npc.banker.chatter_friendship1.2.line_0": "Я что, похожа на человека, к которому можно приставать с расспросами каждый божий день?",
    "dialog.npc.banker.chatter_friendship1.3.line_0": "Опять ты... великолепно.",
    "dialog.npc.banker.chatter_friendship1.4.line_0": "Что.",
    "dialog.npc.banker.chatter_friendship1.5.line_0": "Твои манеры оставляют желать лучшего.",
    "dialog.npc.banker.chatter_friendship1.6.line_0": "Не забывай, что экономика держится на строгом порядке.",
    "dialog.npc.banker.chatter_friendship1.7.line_0": "Если хочешь чего-то добиться в жизни, начни с планирования бюджета.",
    "dialog.npc.banker.chatter_friendship1.8.line_0": "Этот климат ужасно портит мои документы и бухгалтерские книги.",
    "dialog.npc.banker.chatter_friendship1.9.line_0": "Не стой над душой, пока я считаю баланс.",
    "dialog.npc.banker.chatter_friendship1.10.line_0": "Каждая потраченная монета должна приносить отдачу.",
    "dialog.npc.banker.chatter_friendship1.11.line_0": "Ты хоть понимаешь разницу между активами и пассивами?",
    "dialog.npc.banker.chatter_friendship1.12.line_0": "Эйс опять притащил в контору кучу древесной стружки. Какой кошмар.",
    "dialog.npc.banker.chatter_friendship1.13.line_0": "Леон слишком беспечен для управляющего рынком.",
    "dialog.npc.banker.chatter_friendship1.14.line_0": "Если тебе нужны семена — иди на рынок, я не занимаюсь розницей.",
    "dialog.npc.banker.chatter_friendship1.15.line_0": "Работать руками почётно, но без головы на плечах ты быстро разоришься.",
    "dialog.npc.banker.chatter_friendship1.16.line_0": "Надеюсь, твои поля не зарастут сорняками в первый же засушливый месяц.",
    "dialog.npc.banker.chatter_friendship1.17.line_0": "Банк — это сердце любого процветающего города.",
    "dialog.npc.banker.chatter_friendship1.18.line_0": "Моё время расписано по минутам на неделю вперёд.",
    "dialog.npc.banker.chatter_friendship1.19.line_0": "Что привело тебя в моё учреждение сегодня?",

    "dialog.npc.banker.chatter_friendship2.0.line_0": "Интересно, как идут твои посевы в этом сезоне.",
    "dialog.npc.banker.chatter_friendship2.1.line_0": "У тебя есть минутка? Мне нужно сверить пару цифр.",
    "dialog.npc.banker.chatter_friendship2.2.line_0": "Надеюсь, ты не тратишь всю выручку на безделушки.",
    "dialog.npc.banker.chatter_friendship2.3.line_0": "Поселение понемногу оживает. В этом есть и твоя заслуга.",
    "dialog.npc.banker.chatter_friendship2.4.line_0": "Мне доложили, что ты регулярно поставляешь урожай на склад.",
    "dialog.npc.banker.chatter_friendship2.5.line_0": "В городе ходят слухи о твоих успехах. Не зазнавайся раньше времени.",
    "dialog.npc.banker.chatter_friendship2.6.line_0": "Ты уже пробовал перерабатывать ягоды в джем? Это повышает их стоимость.",
    "dialog.npc.banker.chatter_friendship2.7.line_0": "У меня сегодня на редкость много бумажной работы.",
    "dialog.npc.banker.chatter_friendship2.8.line_0": "Что-то конкретное привело тебя ко мне, @i?",
    "dialog.npc.banker.chatter_friendship2.9.line_0": "Эйс уверяет меня, что качество твоих построек на высоте.",
    "dialog.npc.banker.chatter_friendship2.10.line_0": "Управлять капиталом куда сложнее, чем махать лопатой, поверь мне.",
    "dialog.npc.banker.chatter_friendship2.11.line_0": "Если научишься считать расходы, Солнечная Долина станет образцовым краем.",
    "dialog.npc.banker.chatter_friendship2.12.line_0": "Мне нужно отправить гонца в соседний округ до заката.",
    "dialog.npc.banker.chatter_friendship2.13.line_0": "Сегодня относительно спокойный день. Не испорти его.",
    "dialog.npc.banker.chatter_friendship2.14.line_0": "Чем могу помочь по финансовой части, @i?",

    "dialog.npc.banker.chatter_friendship3.0.line_0": "Добрый день, @i. Как продвигается работа на полях?",
    "dialog.npc.banker.chatter_friendship3.1.line_0": "Признаться, ты проявляешь завидное упорство.",
    "dialog.npc.banker.chatter_friendship3.2.line_0": "Я проверила баланс поселения — наши показатели заметно укрепились.",
    "dialog.npc.banker.chatter_friendship3.3.line_0": "Харуна привезла прекрасную партию лосося. Торговля идёт как по маслу.",
    "dialog.npc.banker.chatter_friendship3.4.line_0": "Если понадобятся рекомендации по вкладам — ты всегда можешь ко мне зайти.",
    "dialog.npc.banker.chatter_friendship3.5.line_0": "Эйден сковал отличные крепления для конторских сейфов. Приятно иметь дело с профессионалами.",
    "dialog.npc.banker.chatter_friendship3.6.line_0": "Солнечная Долина наконец начинает приносить реальные плоды.",
    "dialog.npc.banker.chatter_friendship3.7.line_0": "Ты всё реже допускаешь детские ошибки в ведении хозяйства.",
    "dialog.npc.banker.chatter_friendship3.8.line_0": "Не забывай инвестировать в автоматизацию фермы.",
    "dialog.npc.banker.chatter_friendship3.9.line_0": "Рада видеть тебя в добром здравии, @i.",
    "dialog.npc.banker.chatter_friendship3.10.line_0": "У меня появилось чуть больше свободного времени. О чём хотел поговорить?",
    "dialog.npc.banker.chatter_friendship3.11.line_0": "Твой энтузиазм заразителен, признаю.",

    "dialog.npc.banker.chatter_friendship4.0.line_0": "Приветствую, @i! Твои успехи по-настоящему впечатляют меня.",
    "dialog.npc.banker.chatter_friendship4.1.line_0": "Я пересмотрела финансовый план развития городка с учётом твоих темпов роста.",
    "dialog.npc.banker.chatter_friendship4.2.line_0": "Помнишь нашу первую встречу? Признаться, я недооценила твою хватку и упорство.",
    "dialog.npc.banker.chatter_friendship4.3.line_0": "Мы с тобой отличная команда: ты создаёшь материальные ценности, а я приумножаю капитал.",
    "dialog.npc.banker.chatter_friendship4.4.line_0": "Астрид принесла мне редкие кристаллы на оценку. В магии я не сильна, но блестят они великолепно.",
    "dialog.npc.banker.chatter_friendship4.5.line_0": "Всегда приятно побеседовать с человеком, который понимает ценность упорного труда.",
    "dialog.npc.banker.chatter_friendship4.6.line_0": "Я горжусь тем, во что превращается наше скромное поселение.",
    "dialog.npc.banker.chatter_friendship4.7.line_0": "Если тебе понадобится крупное финансирование для масштабного проекта — дай знать, мы всё рассчитаем.",
    "dialog.npc.banker.chatter_friendship4.8.line_0": "Сегодня прекрасный день для заключения выгодных сделок, не находишь?",

    "dialog.npc.banker.chatter_friendship5.0.line_0": "Здравствуй, мой дорогой друг @i.",
    "dialog.npc.banker.chatter_friendship5.0.line_1": "Солнечная Долина расцвела благодаря твоим рукам и нашему общему труду.",
    "dialog.npc.banker.chatter_friendship5.1.line_0": "Я считаю тебя своим самым надёжным партнёром и верным другом.",
    "dialog.npc.banker.chatter_friendship5.2.line_0": "Чем я могу помочь тебе сегодня?",
    "dialog.npc.banker.chatter_friendship5.3.line_0": "Наш город процветает, так держать!",
    "dialog.npc.banker.chatter_friendship5.4.line_0": "Ох, склад перегружен уже два сезона подряд.",
    "dialog.npc.banker.chatter_friendship5.4.line_1": "Я не могу позволить этому замедлить наше местное производство.",
    "dialog.npc.banker.chatter_friendship5.5.line_0": "В последнее время мне с трудом удаётся пополнять все запасы вовремя.",
    "dialog.npc.banker.chatter_friendship5.5.line_1": "Напряжённый сезон, да?",
    "dialog.npc.banker.chatter_friendship5.6.line_0": "На данном этапе у тебя должно быть более чем достаточно денег, чтобы позволить себе поразвлечься на поросячьих бегах!",
    "dialog.npc.banker.chatter_friendship5.7.line_0": "Просто к твоему сведению: в прошлом сезоне город слегка превысил бюджет.",
    "dialog.npc.banker.chatter_friendship5.7.line_1": "На этот раз мне удалось покрыть разницу из собственных средств.",
    "dialog.npc.banker.chatter_friendship5.7.line_2": "Только не привыкай к такому.",
    "dialog.npc.banker.chatter_friendship5.8.line_0": "Всё ещё пренебрегаешь душем после работы?",
    "dialog.npc.banker.chatter_friendship5.9.line_0": "Что у нас сегодня на повестке дня?",
    "dialog.npc.banker.chatter_friendship5.10.line_0": "Приготовил что-нибудь интересное в последнее время?",
    "dialog.npc.banker.chatter_friendship5.10.line_1": "Я смертельно устала от всех этих заурядных блюд.",
    "dialog.npc.banker.chatter_friendship5.11.line_0": "У меня немного времени на разговоры, давай поболтаем чуть позже.",
    "dialog.npc.banker.chatter_friendship5.12.line_0": "Многие жители искренне восхищаются твоими успехами и открыто говорят об этом.",
    "dialog.npc.banker.chatter_friendship5.12.line_1": "Только смотри, чтобы это не вскружило тебе голову.",
    "dialog.npc.banker.chatter_friendship5.13.line_0": "Заметила, что в нескольких лавках заканчиваются товары.",
    "dialog.npc.banker.chatter_friendship5.13.line_1": "Должно быть, ты серьёзно расширяешь объёмы производства — впечатляет!",
    "dialog.npc.banker.chatter_friendship5.14.line_0": "Я бы не отказалась от бокала изысканного вина прямо сейчас.",
    "dialog.npc.banker.chatter_friendship5.15.line_0": "Тебе не стоит расслабляться, впереди ещё много важных дел.",
    "dialog.npc.banker.chatter_friendship5.16.line_0": "Ты меня ещё ни разу не подвёл, но в бизнесе всё может измениться в любой момент.",
    "dialog.npc.banker.chatter_friendship5.17.line_0": "Экономическая стабильность всего поселения держится на твоих плечах.",
    "dialog.npc.banker.chatter_friendship5.17.line_1": "Не подведи этих людей.",

    "dialog.npc.banker.gift_loved.0.line_0": "Я и не подозревала, что у тебя настолько тонкий вкус!",
    "dialog.npc.banker.gift_loved.1.line_0": "Где тебе удалось отыскать нечто столь великолепное?",
    "dialog.npc.banker.gift_loved.2.line_0": "Пожалуй, здешние края не так уж и плохи!",
    "dialog.npc.banker.gift_loved.3.line_0": "Моя лошадь была бы в абсолютном восторге от такого подарка!",
    "dialog.npc.banker.gift_loved.4.line_0": "Кто разболтал тебе о моих слабостях? Ну и лиса же ты!",
    "dialog.npc.banker.gift_loved.5.line_0": "Passe une bonne journée! Отличного тебе дня!",
    "dialog.npc.banker.gift_loved.6.line_0": "Пахнет родным домом...",
    "dialog.npc.banker.gift_loved.7.line_0": "Признаю: изысканной лестью ты можешь добиться от меня чего угодно!",
    "dialog.npc.banker.gift_loved.8.line_0": "Это с твоей фермы? Надеюсь, ты выставишь такую роскошь на продажу!",

    "dialog.npc.banker.gift_liked.0.line_0": "У меня уже есть парочка таких, но это сбережёт мне время на поход в магазин.",
    "dialog.npc.banker.gift_liked.1.line_0": "Это едва ли изменит моё мнение о тебе, но подарок вполне приличный.",
    "dialog.npc.banker.gift_liked.2.line_0": "Я знаю кое-кого, кто оценил бы это по достоинству.",
    "dialog.npc.banker.gift_liked.3.line_0": "Наконец-то хоть кто-то в этой глуши проявляет хорошие манеры.",
    "dialog.npc.banker.gift_liked.4.line_0": "Любопытно.",
    "dialog.npc.banker.gift_liked.5.line_0": "Хм-м, полагаю, я смогу найти этому полезное применение.",
    "dialog.npc.banker.gift_liked.6.line_0": "Я приму это.",
    "dialog.npc.banker.gift_liked.7.line_0": "Давно пора было сделать для меня что-нибудь приятное.",

    "dialog.npc.banker.gift_neutral.0.line_0": "И зачем ты даёшь мне это?..",
    "dialog.npc.banker.gift_neutral.1.line_0": "Мне это не особо нужно.",
    "dialog.npc.banker.gift_neutral.2.line_0": "Ты считаешь меня нищей или как?",
    "dialog.npc.banker.gift_neutral.3.line_0": "Как примитивно.",
    "dialog.npc.banker.gift_neutral.4.line_0": "Ты вообще стараешься заслужить моё расположение?",
    "dialog.npc.banker.gift_neutral.5.line_0": "...",
    "dialog.npc.banker.gift_neutral.6.line_0": "Эта вещь едва ли чего-то стоит.",
    "dialog.npc.banker.gift_neutral.7.line_0": "Ты только тратишь моё драгоценное время этими безделушками.",

    "dialog.npc.banker.gift_disliked.0.line_0": "Это какая-то глупая шутка?",
    "dialog.npc.banker.gift_disliked.1.line_0": "Разумеется, кто-то вроде тебя притащил бы мне именно это...",
    "dialog.npc.banker.gift_disliked.2.line_0": "Фу...",
    "dialog.npc.banker.gift_disliked.3.line_0": "Ладно...",
    "dialog.npc.banker.gift_disliked.4.line_0": "Развернись и уходи.",
    "dialog.npc.banker.gift_disliked.5.line_0": "Ты это несерьёзно, надеюсь?",
    "dialog.npc.banker.gift_disliked.6.line_0": "Ужасно.",
    "dialog.npc.banker.gift_disliked.7.line_0": "Пожалуйста, уйди с моих глаз.",
    "dialog.npc.banker.gift_disliked.8.line_0": "Безвкусно. Впрочем, чего ещё я могла ожидать от тебя.",
    "dialog.npc.banker.gift_disliked.9.line_0": "Это оскорбляет меня.",
    "dialog.npc.banker.gift_disliked.10.line_0": "Это просто отвратительно.",
    "dialog.npc.banker.gift_disliked.11.line_0": "Ты тратишь моё время этими кошмарными пресс-папье.",

    "dialog.npc.banker.gift_hated.0.line_0": "Убери это от моего лица немедленно.",
    "dialog.npc.banker.gift_hated.1.line_0": "И зачем я только приехала в этот богом забытый городишко...",
    "dialog.npc.banker.gift_hated.2.line_0": "Продолжишь в том же духе — и очень скоро останешься здесь без банка.",
    "dialog.npc.banker.gift_hated.3.line_0": "Меня сейчас стошнит.",
    "dialog.npc.banker.gift_hated.4.line_0": "Я и не знала, что ты такого же низкого мнения обо мне, как и я о тебе.",
    "dialog.npc.banker.gift_hated.5.line_0": "Омерзительно.",
    "dialog.npc.banker.gift_hated.6.line_0": "Какая гадость.",
    "dialog.npc.banker.gift_hated.7.line_0": "Грубо и неотесанно.",
    "dialog.npc.banker.gift_hated.8.line_0": "Пойди извинись перед родителями за то, что вырос человеком, способным на такие поступки.",
    "dialog.npc.banker.gift_hated.9.line_0": "Убери эту мерзость подальше от меня.",
    "dialog.npc.banker.gift_hated.10.line_0": "Это самый настоящий мусор.",
    "dialog.npc.banker.gift_hated.11.line_0": "Тьфу.",
    "dialog.npc.banker.gift_hated.12.line_0": "Пошёл вон.",
    "dialog.npc.banker.gift_hated.13.line_0": "Развернулся и зашагал прочь.",
    "dialog.npc.banker.gift_hated.14.line_0": "Если ты так ведёшь здешние дела, то я лишь попусту теряю с тобой время.",
    "dialog.npc.banker.gift_hated.15.line_0": "Оставь свои жалкие шуточки при себе.",

    "dialog.npc.banker.unique_five_gift.line_0": "Здравствуй, @i. Я хотела переговорить с тобой. Мне приятно видеть прогресс на твоей ферме.",
    "dialog.npc.banker.unique_five_gift.line_1": "К сожалению, темпы пока не совсем те, на которые я рассчитывала к этому сроку. Ты уже должен был меня узнать: вытягивать тебя из долгов я не собираюсь.",
    "dialog.npc.banker.unique_five_gift.line_2": "Возможно, эта книга поможет тебе повысить производительность твоих станков и машин.",
    "dialog.npc.banker.unique_five_gift.line_3": "Мне пришлось задействовать массу связей, чтобы заполучить этот трактат, так что будь добр изучить каждую страницу от корки до корки.",
    "dialog.npc.banker.unique_five_gift.line_4": "Я сразу пойму, если ты читал по диагонали — я знаю тебя достаточно хорошо, чтобы это заметить.",
    "dialog.npc.banker.unique_five_gift_read.line_0": "Здравствуй, @i. Нам нужно серьёзно поговорить. Я крайне недовольна развитием твоей фермы.",
    "dialog.npc.banker.unique_five_gift_read.line_1": "Я точно знаю, что ты прочёл книгу «Путь к мастерству», так почему же ты не применяешь её знания на практике?",
    "dialog.npc.banker.unique_five_gift_read.line_2": "Ты должен был уже усвоить: я не стану покрывать твои огрехи, сколько бы ты ни пытался мне польстить.",
    "dialog.npc.banker.unique_five_gift_read.line_3": "Пожалуйста, используй эти древние путевые камни, чтобы оптимизировать своё время. Я не могу позволить тебе тратить драгоценные часы на пешие прогулки.",
    "dialog.npc.banker.unique_five_gift_read.line_4": "А теперь ступай и больше не разочаровывай меня."
}

update_md('02_banker.md', caroline)
