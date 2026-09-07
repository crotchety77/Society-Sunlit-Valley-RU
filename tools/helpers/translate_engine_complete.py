import json
import os
import re

review_dir = os.path.join(os.path.dirname(__file__), '..', 'dialogs_review')
untranslated_path = os.path.join(os.path.dirname(__file__), 'untranslated_lines.json')

with open(untranslated_path, 'r', encoding='utf-8') as f:
    untranslated_by_file = json.load(f)

# Translation dictionary covering ALL remaining keys across all files
with open(os.path.join(os.path.dirname(__file__), 'all_remaining_en.json'), 'r', encoding='utf-8') as f:
    all_en = json.load(f)

# Helper function to generate fluent Russian text
def get_russian_translation(key, en):
    # Strip any extra whitespace
    en = en.strip()

    # Manual specific overrides first
    # 03_market
    if "market.chatter_friendship3" in key or "market.chatter_friendship4" in key or "market.chatter_friendship5" in key:
        pass

    # Generic patterns
    if en == "My stuff is top notch - just take a look!":
        return "Мой товар высшей пробы — только взгляни!"
    if en == "Premium wares!":
        return "Премиальные диковинки со всего света!"
    if en == "I bet you've never seen this stuff before!":
        return "Бьюсь об заклад, ты в жизни такого не видывал!"
    if en.startswith("@i, was it?"):
        return "@i, верно? У меня накопилась гора первоклассного товара, только и ждёт твоих покупок!"
    if en.startswith("No money no problem!"):
        return "Нет звонкой монеты? Не беда! Покажи, какие сокровища завалялись в твоих карманах!"
    if en.startswith("I've got stuff you won't get anywhere else!"):
        return "У меня есть вещи, которые ты не сыщешь больше нигде в мире!"
    if en == "Let's make a deal!":
        return "Давай заключим сделку!"
    if en == "Always a pleasure doing business with you, @i.":
        return "Всегда приятно иметь с тобой дело, @i."
    if en == "Gotta keep something in the pack at all times!":
        return "В сумке торговца всегда должно быть что-то новенькое!"
    if en == "What's a merchant without wares?":
        return "Что за купец без богатого ассортимента?"
    if en.startswith("It feels good to be in a right proper town."):
        return "Как же приятно оказаться в настоящем, процветающем городке. В дороге никогда не удаётся толком поесть!"
    if en.startswith("Hello hello @i!"):
        return "Привет-привет, @i! Чем могу порадовать тебя сегодня?"
    if en.startswith("You got any Truffle Tea?"):
        return "У тебя случайно нет трюфельного чая? Мне бы до смерти хотелось раздобыть парочку чашек..."
    if en.startswith("Have you seen Ace around?"):
        return "Ты не видел Эйса поблизости? В моих тайных запасах как раз припасено несколько редких саженцев!"
    if en.startswith("Caroline was cooking up something wonderful"):
        return "Кэролайн на днях готовила что-то неописуемое... Аромат разносился за целую милю!"
    if en.startswith("Need anything special today?"):
        return "Ищешь что-то особенное сегодня? Или глянешь обычный ассортимент?"
    if en.startswith("@i! What do I have the pleasure for today?"):
        return "@i! Какая приятная встреча, чем обязан?"
    if en.startswith("Veronica is a tough one"):
        return "Вероника — крепкий орешек... Мне всегда непросто находить общий язык с такими тихонями."
    if en.startswith("I have no idea how Aiden stays in business"):
        return "Ума не приложу, как Эйден умудряется оставаться на плаву, раздавая столько добра даром."
    if en.startswith("Keep people wanting!"):
        return "Покупателей нужно держать в лёгком голоде! Иначе они никогда не вернутся!"
    if en == "@i! Back at it again!":
        return "@i! Снова в деле!"
    if en.startswith("I've heard a lot of stories, but nothing about Haruna"):
        return "Я слышал множество историй со всех концов света, но ни слова о родине Харуны... Как странно."
    if en.startswith("I always love chatting with Evelyne!"):
        return "Обожаю болтать с Эвелин! Когда она не спит, разумеется..."
    if en.startswith("Do NOT trade with those Gnomes!!"):
        return "Ни в коем случае НЕ торгуй с этими гномами!!"
    if en.startswith("Do they even understand how valuable silver is?"):
        return "Они вообще понимают, насколько ценно серебро? И что мне прикажете делать с этой дурацкой пылью?!"
    if en.startswith("I was hanging out with Leon the other day"):
        return "На днях я зависал с Леоном — до чего же занятный парень!"
    if en.startswith("I wasn't expecting someone familiar with culture"):
        return "Не ожидал встретить в такой глухой деревеньке человека, столь глубоко разбирающегося в культуре!"
    if en.startswith("I wonder why people find it so difficult to get along with Caroline."):
        return "Интересно, почему людям так трудно поладить с Кэролайн?"
    if en.startswith("What do you do what do you know, it's @i!"):
        return "Кого я вижу! Сам @i собственной персоной!"
    if en.startswith("Very rarely do I get to actually explore"):
        return "Мне крайне редко удаётся по-настоящему погулять по городам, где я останавливаюсь... Обычно я привязан к своей лавке!"
    if en.startswith("Witches are the best"):
        return "Ведьмы — лучшие клиенты! Они вечно заказывают самые безумные вещи."
    if en.startswith("And who better to aquire said things"):
        return "И кто справится с доставкой этих диковинок лучше меня? Да никто!"
    if en.startswith("Sometimes I wake up in a cold sweat"):
        return "Иногда я просыпаюсь в холодном поту при мысли о том, как однажды мне подали тарелку тухлой акулы хаукарль."
    if en.startswith("Wish I knew what that was before I hogged it down!"):
        return "Жаль, я не знал, что это такое, до того как проглотил кусок целиком!"
    if en.startswith("You know I've never actually met the person who makes all your machine upgrades."):
        return "Знаешь, я ведь ни разу не встречал лично того гения, который создаёт улучшения для твоих станков."
    if en.startswith("They've gone through like 4 different brokers"):
        return "Эти чертежи проходят через четверых посредников, прежде чем очутиться у тебя на ферме!"
    if en.startswith("I bet a person like you would love the Camuy Caves!"):
        return "Готов спорить, такому авантюристу, как ты, понравились бы пещеры Камуй!"
    if en.startswith("You just gotta watch out for those stupid horrifying spiders"):
        return "Только берегись тех жутких громадных пауков. Терпеть не могу этих тварей..."
    if en.startswith("Nobody around here dances"):
        return "Здесь никто не танцует, для меня это настоящий культурный шок! Интересно, Харуна постоянно чувствует себя так же?"
    if en.startswith("Watcha up to today @i?"):
        return "Чем занят сегодня, @i?"
    if en.startswith("@i @i @i! I've been looking forward"):
        return "@i, @i, @i! Я с нетерпением ждал твоего очередного визита!"
    if en.startswith("Do you want a drink? Or are you still working?"):
        return "Хочешь выпить чего-нибудь освежающего? Или всё ещё работаешь? Ты вечно трудишься не покладая рук!"
    if en.startswith("Y'know, this place is a lot like home."):
        return "Знаешь, это место очень напоминает мне родной дом."
    if en.startswith("So much hustle and bustle... a guy could get comfortable."):
        return "Столько приятной суеты и движения... Тут запросто можно пустить корни."
    if en.startswith("Sometimes I feel like I should've collected these things myself."):
        return "Иногда мне кажется, что я должен был сам добывать все эти сокровища."
    if en.startswith("I've been around, but I've never been in any real danger"):
        return "Я много где побывал, но ни разу не попадал в настоящую переделку, понимаешь?"
    if en.startswith("Oops, carried away again. Did you need anything?"):
        return "Ой, опять я разболтался. Тебе что-нибудь нужно?"
    if en.startswith("I love someone that can eat, but I love someone that can cook more!"):
        return "Я уважаю тех, кто любит поесть, но тех, кто умеет готовить — боготворю!"
    if en.startswith("You're the best, @i, you know that?"):
        return "Ты лучший друг на свете, @i, знаешь об этом?"
    if en.startswith("* You notice the ravenous look on Carlos' face"):
        return "* Вы замечаете голодный блеск в глазах Карлоса и передаёте подарок *"
    if en.startswith("* There are no words, but the sheer speed"):
        return "* Слова излишни: бешеная скорость, с которой он всё уплетает, говорит сама за себя *"
    if en.startswith("I'm in awe. This is like..."):
        return "Я просто в благоговении. Это же...",
    if en.startswith("So totally righteous."):
        return "Просто потрясно!"
    if en.startswith("You're a sweet one, aren't you?"):
        return "А ты умеешь быть милым, правда?"
    if en == "This rocks!":
        return "Вот это вещь! Высший класс!"
    if en == "Thanks so much!":
        return "Огромное спасибо!"
    if en == "Aww yeah! Awesome!":
        return "О-о да! Красота!"
    if en == "Not the worst I've gotten!":
        return "Бывало и похуже, сойдёт!"
    if en == "I guess this isn't nothing.":
        return "Ну, по крайней мере, это лучше, чем ничего."
    if en.startswith("Thanks for, uh..."):
        return "Спасибо за... эм..."
    if en == "This.":
        return "Вот это."
    if en.startswith("Does this, uh..."):
        return "А это..."
    if en.startswith("Will this fit in my pack?"):
        return "Оно вообще влезет в мою сумку?"
    
    # Fallback to smart translation
    return None

print("Loaded translation helper.")
