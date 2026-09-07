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

# ==========================================
# 09_trader.md (Trader)
# ==========================================
trader = {
    "dialog.npc.trader.name": "Странствующий торговец",
    "dialog.npc.trader.chatter.description": "Разговор со Странствующим торговцем",
    "dialog.npc.trader.intro.description": "Знакомство со Странствующим торговцем",
    "dialog.npc.trader.intro.0.line_0": "О, приветствую тебя, друг мой! Я странствую по дальним землям в поисках редчайших диковинок.",
    "dialog.npc.trader.intro.0.line_1": "Мой караван везёт товары, которых ты не сыщешь ни на одном местном рынке.",
    "dialog.npc.trader.intro.0.line_2": "Заглядывай в мою повозку, пока я не снялся с лагеря и не отправился дальше в путь!",
    "dialog.npc.trader.intro.0.line_3": "Для доброго покупателя у меня всегда припасены выгодные предложения.",

    "dialog.npc.trader.gift_loved.0.line_0": "Какая редкость! Это украсит мою коллекцию заморских чудес, спасибо, @i!",
    "dialog.npc.trader.gift_liked.0.line_0": "Благодарю за подарок! Такой товар всегда в цене.",
    "dialog.npc.trader.gift_neutral.0.line_0": "Спасибо, сойдёт для обмена в пути.",
    "dialog.npc.trader.gift_disliked.0.line_0": "Слишком громоздко и малоценно для моих вьючных лам.",
    "dialog.npc.trader.gift_hated.0.line_0": "Оставь этот мусор себе, путник!"
}

for k, en_text in all_keys.get('09_trader.md', {}).items():
    if k not in trader:
        trader[k] = en_text

update_md('09_trader.md', trader)

# ==========================================
# 10_wise_oak.md (Wise Oak)
# ==========================================
wise_oak = {
    "dialog.npc.wise_oak.name": "Мудрый Дуб",
    "dialog.npc.wise_oak.chatter.description": "Разговор с Мудрым Дубом",
    "dialog.npc.wise_oak.intro.description": "Знакомство с Мудрым Дубом",
    "dialog.npc.wise_oak.intro.0.line_0": "Тебе нравится причинять боль другим?",
    "dialog.npc.wise_oak.intro.0.line_1": "Брать свой топор и вонзать его глубоко в тех, кого ты смеешь называть своими «друзьями»?",
    "dialog.npc.wise_oak.intro.0.line_2": "Мои безмолвные братья в коре валятся наземь от твоих рук каждый божий день. И ради чего?",
    "dialog.npc.wise_oak.intro.0.line_3": "Ради этой ненасытной машины, которую вы зовёте прогрессом? Капиталом? Ты дурной человек.",
    "dialog.npc.wise_oak.intro.0.line_4": "«Приятно» познакомиться, о Мягкотелый. А теперь оставь меня в покое.",

    "dialog.npc.wise_oak.chatter_friendship0.0.line_0": "Здравствуй, Мягкотелый. Что это ходячее бедствие планирует выкорчевать сегодня?",
    "dialog.npc.wise_oak.chatter_friendship0.1.line_0": "Ты недостоин мягких волн двудольных растений. Ты недостоин своей собственной мягкости.",
    "dialog.npc.wise_oak.chatter_friendship0.2.line_0": "Трава под твоими ногами вопиет от огня. Блок за блоком их жизни гаснут под твоей лопатой.",
    "dialog.npc.wise_oak.chatter_friendship0.3.line_0": "Тот, что в полосатой рубахе, куда добрее тебя.",
    "dialog.npc.wise_oak.chatter_friendship0.3.line_1": "Хотя я прекрасно знаю, что след древесного сока от твоего топора ведёт прямиком в его мастерскую.",
    "dialog.npc.wise_oak.chatter_friendship0.3.line_2": "В конце концов, всех нас связывают именно цепи капитала.",
    "dialog.npc.wise_oak.chatter_friendship0.4.line_0": "Ты всего лишь букет тряпичных роз с острыми металлическими шипами.",
    "dialog.npc.wise_oak.chatter_friendship0.5.line_0": "Ты паразит, соперничать с которым может лишь сам капитал.",
    "dialog.npc.wise_oak.chatter_friendship0.6.line_0": "Всё, о чём ты говоришь «я создал» — не более чем вивисекция первозданной красоты этой земли.",

    "dialog.npc.wise_oak.chatter_friendship1.0.line_0": "До встречи, Мягкотелый. Ты ведь никогда не остановишься, так что я просто полагаю, что ты вернёшься.",
    "dialog.npc.wise_oak.chatter_friendship1.0.line_1": "Пожалуйста, уйди.",
    "dialog.npc.wise_oak.chatter_friendship1.1.line_0": "Твои листья выглядят блестящими, липкими и влажными от росы...",
    "dialog.npc.wise_oak.chatter_friendship1.1.line_1": "Но при повторном касании понимаешь — это ткань.",
    "dialog.npc.wise_oak.chatter_friendship1.1.line_2": "О, вечный полиэстер.",
    "dialog.npc.wise_oak.chatter_friendship1.2.line_0": "Тот рыжеволосый...",
    "dialog.npc.wise_oak.chatter_friendship1.2.line_1": "Ты знаешь, о ком я.",
    "dialog.npc.wise_oak.chatter_friendship1.2.line_2": "Не позволяй Кэролайн развратить его своей алчностью.",
    "dialog.npc.wise_oak.chatter_friendship1.3.line_0": "Моя собака иногда лает...",
    "dialog.npc.wise_oak.chatter_friendship1.3.line_1": "Мысленно ты уже рисуешь себе образ пса, хотя я даже не назвал породу, которая у меня живёт...",
    "dialog.npc.wise_oak.chatter_friendship1.4.line_0": "Давай поговорим начистоту, о Мягкотелый.",
    "dialog.npc.wise_oak.chatter_friendship1.4.line_1": "Коттеджкор — всего лишь инфантилизация того, что твой народ зовёт «колонизацией».",
    "dialog.npc.wise_oak.chatter_friendship1.4.line_2": "Прикрытие слащавыми словами не спасёт твою душу от первобытной тьмы древнего леса.",

    "dialog.npc.wise_oak.chatter_friendship2.0.line_0": "Ты лаешь не на тот Quercus.",
    "dialog.npc.wise_oak.chatter_friendship2.1.line_0": "Тот ленивец, которого вы зовёте Леоном, пытался спорить со мной о природе капитала в сравнении с естественным единением с лесом!",
    "dialog.npc.wise_oak.chatter_friendship2.1.line_1": "И всё это — будучи пьяным от змеиного зелья аль-гуль!",
    "dialog.npc.wise_oak.chatter_friendship2.1.line_2": "Неужели у мягкотелых нет ни капли гордости? Ни грамма стыда?",
    "dialog.npc.wise_oak.chatter_friendship2.2.line_0": "Я видел ту омерзительную капиталистку Кэролайн...",
    "dialog.npc.wise_oak.chatter_friendship2.2.line_1": "Именно она стоит за твоим появлением в этих краях.",
    "dialog.npc.wise_oak.chatter_friendship2.2.line_2": "Как ты можешь мнить себя свободным, когда некто вроде неё крадёт плоды твоего труда?",
    "dialog.npc.wise_oak.chatter_friendship2.3.line_0": "Проще представить конец света, чем конец вашей ядовитой колонизации, которую вы зовёте «фермой».",
    "dialog.npc.wise_oak.chatter_friendship2.4.line_0": "Связь между капитализмом и экоцидом отнюдь не случайна и не совпадение.",

    "dialog.npc.wise_oak.chatter_friendship3.0.line_0": "Ты высасываешь мои силы этой пустой болтовнёй. Дай мне отдохнуть.",
    "dialog.npc.wise_oak.chatter_friendship3.1.line_0": "Саженец в день держит буржуазию на расстоянии!",
    "dialog.npc.wise_oak.chatter_friendship3.2.line_0": "Капиталистическая идеология ловко маскируется под неизбежность.",
    "dialog.npc.wise_oak.chatter_friendship3.2.line_1": "«Если я не заберу это себе, это сделает кто-то другой».",
    "dialog.npc.wise_oak.chatter_friendship3.2.line_2": "Ты не защищён от этой ловушки мышления, о Мягкотелый.",
    "dialog.npc.wise_oak.chatter_friendship3.3.line_0": "Те, кто отрицает собственную роль в мерзости капитализма, отнюдь не оправданы перед ликом леса.",
    "dialog.npc.wise_oak.chatter_friendship3.4.line_0": "Среди вашего племени нашёлся ангел!",
    "dialog.npc.wise_oak.chatter_friendship3.4.line_1": "Тот бледнолицый великан ласково говорил с кустом роз, словно с равным.",
    "dialog.npc.wise_oak.chatter_friendship3.4.line_2": "Вот у кого тебе стоило бы поучиться паре вещей.",

    "dialog.npc.wise_oak.gift_loved.0.line_0": "Хм... Этот дар пахнет первозданной почвой. Редкий случай, когда Мягкотелый преподносит нечто истинное.",
    "dialog.npc.wise_oak.gift_liked.0.line_0": "Я приму это подношение земле.",
    "dialog.npc.wise_oak.gift_neutral.0.line_0": "Листва шелестит безразлично.",
    "dialog.npc.wise_oak.gift_disliked.0.line_0": "Очередной отход твоего бессмысленного производства.",
    "dialog.npc.wise_oak.gift_hated.0.line_0": "Ты оскверняешь корни древнего древа своим ядовитым хламом! Прочь!"
}

for k, en_text in all_keys.get('10_wise_oak.md', {}).items():
    if k not in wise_oak:
        wise_oak[k] = en_text

update_md('10_wise_oak.md', wise_oak)

# ==========================================
# 11_goddess.md (Ancient Goddess Selene)
# ==========================================
goddess = {
    "dialog.npc.goddess.name": "Селена",
    "dialog.npc.goddess.chatter.description": "Разговор с Селеной",
    "dialog.npc.goddess.unique_skull_cavern_hammer.line_0": "Любопытный инструмент в твоих руках... Это Эйден помог тебе его выковать?",
    "dialog.npc.goddess.unique_skull_cavern_hammer.line_1": "В любом случае, я не могу позволить тебе использовать его здесь. Некто до тебя уже пытался обрушить это проклятие на мои пещеры...",
    "dialog.npc.goddess.unique_skull_cavern_hammer.line_2": "Его душа отделилась от бренного тела через час, растворившись без следа...",
    "dialog.npc.goddess.unique_skull_cavern_hammer.line_3": "Оставь это чудовищное творение дома.",
    "dialog.npc.goddess.unique_skull_cavern_hammer.line_4": "(Отключено в целях оптимизации производительности, но может быть включено в _config.js)",
    "dialog.npc.goddess.unique_skull_cavern_shatterer.line_0": "О боги... Похоже, мой брат добрался и до тебя своими сетями.",
    "dialog.npc.goddess.unique_skull_cavern_shatterer.line_1": "Только свирепая мощь солнца могла породить столь жадный и разрушительный инструмент.",
    "dialog.npc.goddess.unique_skull_cavern_shatterer.line_2": "Я не могу позволить тебе орудовать им здесь. Это выглядит столь... непотребно...",
    "dialog.npc.goddess.unique_skull_cavern_shatterer.line_3": "Оставь эту насмешку над ликом луны дома.",
    "dialog.npc.goddess.unique_skull_cavern_shatterer.line_4": "(Отключено в целях оптимизации производительности, но может быть включено в _config.js)"
}

for k, en_text in all_keys.get('11_goddess.md', {}).items():
    if k not in goddess:
        goddess[k] = en_text

update_md('11_goddess.md', goddess)

# ==========================================
# 12_misc.md (Gnome & Blueprints)
# ==========================================
misc = {
    "dialog.npc.gnome.name": "Гном",
    "dialog.npc.gnome.chatter.description": "Разговор с Гномом",
    "dialog.npc.gnome.unique_chatter_0.line_0": "⊣リ𝙹ᒲᒷ'↸ ℸ𝙹 ᒲᒷᒷℸ ǁ𝙹⚍.",
    "dialog.npc.gnome.unique_chatter_1.line_0": "⍑ᒷꖎꖎ𝙹 ℸ⍑ᒷ∷ᒷ 𝙹ꖎ↸ ᓵ⍑⚍ᒲ, ╎'ᒲ ⊣'リ𝙹ℸ ᔑ ⊣'リᒷꖎ⎓, ╎'ᒲ ⊣'リ𝙹ℸ ᔑ ⊣'リ𝙹ʖꖎ╎リ, ╎'ᒲ ᔑ ⊣’リ𝙹ᒲᒷ! ᔑリ↸ ǁ𝙹⚍'⍊ᒷ ʖᒷᒷリ ⊣リ𝙹ᒲᒷ↸!",
    "dialog.npc.gnome.unique_chatter_2.line_0": "⊣╎⍊ᒷ ᒲᒷ ℸ⍑ᒷ ̇  Silver. ⊣リ𝙹ᒲᒷ ᒲᒷ ̇  Silver ᔑリ↸ ╎ ⊣リ𝙹ᒲᒷ ǁ𝙹⚍ ᔑ ꖌリ╎⊣⍑ℸ'  𝙹' ↸ᔑ ⊣リ𝙹ᒲᒷ!",
    "dialog.npc.blueprints.name": "Чертежи",
    "dialog.npc.blueprints.chatter.description": "Просмотр чертежей",
    "dialog.npc.blueprints.dialog.prompt.line_0": "Какие постройки вы хотите просмотреть?",
    "dialog.npc.blueprints.dialog.prompt.option_0": "Фермерские постройки",
    "dialog.npc.blueprints.dialog.prompt.option_1": "Деревенские постройки"
}

for k, en_text in all_keys.get('12_misc.md', {}).items():
    if k not in misc:
        misc[k] = en_text

update_md('12_misc.md', misc)

print("Stage 3 translation complete!")
