import json
import os
import re

with open(os.path.join(os.path.dirname(__file__), 'all_remaining_en.json'), 'r', encoding='utf-8') as f:
    all_en = json.load(f)

# Comprehensive phrase translation engine
manual_map = {
    # Trader (Carlos)
    "dialog.npc.trader.intro.0.line_4": "Я вечно по уши в торговых делах, сам понимаешь, как это бывает, аха-ха...",
    "dialog.npc.trader.intro.0.line_5": "......",
    "dialog.npc.trader.intro.0.line_6": "Так, о чём это я! Меня зовут Карлос! Я веду только бартерный обмен, ведь некоторые вещи стоят дороже любых денег!",
    "dialog.npc.trader.chatter_friendship0.0.line_0": "Мой товар высшей пробы — только взгляни!",
    "dialog.npc.trader.chatter_friendship0.1.line_0": "Премиальные диковинки со всего света!",
    "dialog.npc.trader.chatter_friendship0.2.line_0": "Бьюсь об заклад, ты в жизни такого не видывал!",
    "dialog.npc.trader.chatter_friendship0.3.line_0": "@i, верно? У меня накопилась гора первоклассного товара, только и ждёт твоих покупок!",
    "dialog.npc.trader.chatter_friendship0.4.line_0": "Нет звонкой монеты? Не беда! Покажи, какие сокровища завалялись в твоих карманах!",
    "dialog.npc.trader.chatter_friendship0.5.line_0": "У меня есть вещи, которые ты не сыщешь больше нигде в мире!",
    "dialog.npc.trader.chatter_friendship0.6.line_0": "Давай заключим сделку!",
    "dialog.npc.trader.chatter_friendship1.0.line_0": "Всегда приятно иметь с тобой дело, @i.",
    "dialog.npc.trader.chatter_friendship1.1.line_0": "В сумке торговца всегда должно быть что-то новенькое!",
    "dialog.npc.trader.chatter_friendship1.1.line_1": "Что за купец без богатого ассортимента?",
    "dialog.npc.trader.chatter_friendship1.2.line_0": "Как же приятно оказаться в настоящем, процветающем городке. В дороге никогда не удаётся толком поесть!",
    "dialog.npc.trader.chatter_friendship1.3.line_0": "Привет-привет, @i! Чем могу порадовать тебя сегодня?",
    "dialog.npc.trader.chatter_friendship1.4.line_0": "У тебя случайно нет трюфельного чая? Мне бы до смерти хотелось раздобыть парочку чашек...",
    "dialog.npc.trader.chatter_friendship2.0.line_0": "Ты не видел Эйса поблизости? В моих тайных запасах как раз припасено несколько редких саженцев!",
    "dialog.npc.trader.chatter_friendship2.1.line_0": "Кэролайн на днях готовила что-то неописуемое... Аромат разносился за целую милю!",
    "dialog.npc.trader.chatter_friendship2.2.line_0": "Ищешь что-то особенное сегодня? Или глянешь обычный ассортимент?",
    "dialog.npc.trader.chatter_friendship2.3.line_0": "@i! Какая приятная встреча, чем обязан?",
    "dialog.npc.trader.chatter_friendship2.4.line_0": "Вероника — крепкий орешек... Мне всегда непросто находить общий язык с такими тихонями.",
    "dialog.npc.trader.chatter_friendship3.1.line_0": "Ума не приложу, как Эйден умудряется оставаться на плаву, раздавая столько добра даром.",
    "dialog.npc.trader.chatter_friendship3.1.line_1": "Покупателей нужно держать в лёгком голоде! Иначе они никогда не вернутся!",
    "dialog.npc.trader.chatter_friendship3.2.line_0": "@i! Снова в деле!",
    "dialog.npc.trader.chatter_friendship3.3.line_0": "Я слышал множество историй со всех концов света, но ни слова о родине Харуны... Как странно.",
    "dialog.npc.trader.chatter_friendship3.4.line_0": "Обожаю болтать с Эвелин! Когда она не спит, разумеется...",
    "dialog.npc.trader.chatter_friendship3.5.line_0": "Ни в коем случае НЕ торгуй с этими гномами!!",
    "dialog.npc.trader.chatter_friendship3.5.line_1": "Они вообще понимают, насколько ценно серебро? И что мне прикажете делать с этой дурацкой пылью?!",
    "dialog.npc.trader.chatter_friendship3.6.line_0": "На днях я зависал с Леоном — до чего же занятный парень!",
    "dialog.npc.trader.chatter_friendship3.6.line_1": "Не ожидал встретить в такой глухой деревеньке человека, столь глубоко разбирающегося в культуре!",
    "dialog.npc.trader.chatter_friendship4.0.line_0": "Интересно, почему людям так трудно поладить с Кэролайн?",
    "dialog.npc.trader.chatter_friendship4.1.line_0": "Кого я вижу! Сам @i собственной персоной!",
    "dialog.npc.trader.chatter_friendship4.2.line_0": "Мне крайне редко удаётся по-настоящему погулять по городам, где я останавливаюсь... Обычно я привязан к своей лавке!",
    "dialog.npc.trader.chatter_friendship4.3.line_0": "Ведьмы — лучшие клиенты! Они вечно заказывают самые безумные вещи.",
    "dialog.npc.trader.chatter_friendship4.3.line_1": "И кто справится с доставкой этих диковинок лучше меня? Да никто!",
    "dialog.npc.trader.chatter_friendship4.4.line_0": "Иногда я просыпаюсь в холодном поту при мысли о том, как однажды мне подали тарелку тухлой акулы хаукарль.",
    "dialog.npc.trader.chatter_friendship4.4.line_1": "Жаль, я не знал, что это такое, до того как проглотил кусок целиком!",
    "dialog.npc.trader.chatter_friendship4.5.line_0": "Знаешь, я ведь ни разу не встречал лично того гения, который создаёт улучшения для твоих станков.",
    "dialog.npc.trader.chatter_friendship4.5.line_1": "Эти чертежи проходят через четверых посредников, прежде чем очутиться у тебя на ферме!",
    "dialog.npc.trader.chatter_friendship4.6.line_0": "Готов спорить, такому авантюристу, как ты, понравились бы пещеры Камуй!",
    "dialog.npc.trader.chatter_friendship4.6.line_1": "Только берегись тех жутких громадных пауков. Терпеть не могу этих тварей...",
    "dialog.npc.trader.chatter_friendship5.0.line_0": "Здесь никто не танцует, для меня это настоящий культурный шок! Интересно, Харуна постоянно чувствует себя так же?",
    "dialog.npc.trader.chatter_friendship5.1.line_0": "Чем занят сегодня, @i?",
    "dialog.npc.trader.chatter_friendship5.2.line_0": "@i, @i, @i! Я с нетерпением ждал твоего очередного визита!",
    "dialog.npc.trader.chatter_friendship5.3.line_0": "Хочешь выпить чего-нибудь освежающего? Или всё ещё работаешь? Ты вечно трудишься не покладая рук!",
    "dialog.npc.trader.chatter_friendship5.4.line_0": "Знаешь, это место очень напоминает мне родной дом.",
    "dialog.npc.trader.chatter_friendship5.4.line_1": "Столько приятной суеты и движения... Тут запросто можно пустить корни.",
    "dialog.npc.trader.chatter_friendship5.5.line_0": "Иногда мне кажется, что я должен был сам добывать все эти сокровища.",
    "dialog.npc.trader.chatter_friendship5.5.line_1": "Я много где побывал, но ни разу не попадал в настоящую переделку, понимаешь?",
    "dialog.npc.trader.chatter_friendship5.5.line_2": "Ой, опять я разболтался. Тебе что-нибудь нужно?",
    "dialog.npc.trader.gift_loved.1.line_0": "Я уважаю тех, кто любит поесть, но тех, кто умеет готовить — боготворю!",
    "dialog.npc.trader.gift_loved.2.line_0": "Ты лучший друг на свете, @i, знаешь об этом?",
    "dialog.npc.trader.gift_loved.3.line_0": "* Вы замечаете голодный блеск в глазах Карлоса и передаёте подарок *",
    "dialog.npc.trader.gift_loved.3.line_1": "* Слова излишни: бешеная скорость, с которой он всё уплетает, говорит сама за себя *",
    "dialog.npc.trader.gift_loved.4.line_0": "Я просто в благоговении. Это же...",
    "dialog.npc.trader.gift_loved.4.line_1": "Просто потрясно!",
    "dialog.npc.trader.gift_liked.1.line_0": "А ты умеешь быть милым, правда?",
    "dialog.npc.trader.gift_liked.2.line_0": "Вот это вещь! Высший класс!",
    "dialog.npc.trader.gift_liked.3.line_0": "Огромное спасибо!",
    "dialog.npc.trader.gift_liked.4.line_0": "О-о да! Красота!",
    "dialog.npc.trader.gift_neutral.1.line_0": "Бывало и похуже, сойдёт!",
    "dialog.npc.trader.gift_neutral.2.line_0": "Ну, по крайней мере, это лучше, чем ничего.",
    "dialog.npc.trader.gift_neutral.3.line_0": "Спасибо за... эм...",
    "dialog.npc.trader.gift_neutral.3.line_1": "Вот это.",
    "dialog.npc.trader.gift_neutral.4.line_0": "А это...",
    "dialog.npc.trader.gift_neutral.4.line_1": "Оно вообще влезет в мою сумку?",
    "dialog.npc.trader.gift_disliked.0.line_0": "Э-э... спасибо, наверное?",
    "dialog.npc.trader.gift_disliked.1.line_0": "Мне это и даром не нужно.",
    "dialog.npc.trader.gift_hated.0.line_0": "Оставь этот мусор себе, путник!"
}

# Write out manual map
with open(os.path.join(os.path.dirname(__file__), 'manual_map.json'), 'w', encoding='utf-8') as f:
    json.dump(manual_map, f, ensure_ascii=False, indent=2)

print("Manual map saved!")
