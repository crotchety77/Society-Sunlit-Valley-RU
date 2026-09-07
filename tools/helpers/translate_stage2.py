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
# 05_shepherd.md (Maria)
# ==========================================
maria = {
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
    "dialog.npc.shepherd.chatter_friendship0.11.line_1": "У некоторых из них совершенно черствое сердце, неспособное на заботу.",
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

    "dialog.npc.shepherd.gift_loved.0.line_0": "О боже мой! Это же просто чудо! Спасибо тебе огромное, @i!",
    "dialog.npc.shepherd.gift_loved.1.line_0": "Какой невероятно милый и прекрасный подарок! Я просто счастлива!",
    "dialog.npc.shepherd.gift_liked.0.line_0": "Ой, спасибо большое, @i! Мне очень приятно.",
    "dialog.npc.shepherd.gift_neutral.0.line_0": "Спасибо, пригодится в хозяйстве.",
    "dialog.npc.shepherd.gift_disliked.0.line_0": "Ох... не стоило, правда.",
    "dialog.npc.shepherd.gift_hated.0.line_0": "Фу! Зачем ты принёс мне эту гадость?!"
}

for k, en_text in all_keys.get('05_shepherd.md', {}).items():
    if k not in maria:
        maria[k] = en_text

update_md('05_shepherd.md', maria)

# ==========================================
# 06_fisher.md (Haruna)
# ==========================================
haruna = {
    "dialog.npc.fisher.name": "Харуна",
    "dialog.npc.fisher.chatter.description": "Разговор с Харуной",
    "dialog.npc.fisher.intro.description": "Знакомство с Харуной",
    "dialog.npc.fisher.intro.0.line_0": "Здравствуй, чужеземец. Меня зовут Харуна. Я прибыла из далёких восточных морей.",
    "dialog.npc.fisher.intro.0.line_1": "Воды этой долины таят в себе богатейшие уловы, если знать, на что и где ловить.",
    "dialog.npc.fisher.intro.0.line_2": "У меня найдётся первоклассная наживка, снасти и секреты рыбацкого ремесла.",
    "dialog.npc.fisher.intro.0.line_3": "Пусть ветер всегда будет попутным для твоих парусов.",

    "dialog.npc.fisher.chatter_friendship0.0.line_0": "Солёный бриз напоминает мне о родных берегах.",
    "dialog.npc.fisher.chatter_friendship0.1.line_0": "Хорошая удочка — вернейший друг в долгих странствиях.",
    "dialog.npc.fisher.chatter_friendship0.2.line_0": "Рыба клюёт лучше всего на рассвете и в тихие дождливые дни.",

    "dialog.npc.fisher.gift_loved.0.line_0": "Какое сокровище! Моё сердце трепещет от благодарности, @i!",
    "dialog.npc.fisher.gift_liked.0.line_0": "Прекрасный дар, спасибо тебе, друг мой.",
    "dialog.npc.fisher.gift_neutral.0.line_0": "Благодарю за улов.",
    "dialog.npc.fisher.gift_disliked.0.line_0": "Это не имеет для меня никакой ценности.",
    "dialog.npc.fisher.gift_hated.0.line_0": "Убери это прочь. Ты оскверняешь память моих предков."
}

for k, en_text in all_keys.get('06_fisher.md', {}).items():
    if k not in haruna:
        haruna[k] = en_text

update_md('06_fisher.md', haruna)

# ==========================================
# 07_witch.md (Astrid)
# ==========================================
astrid = {
    "dialog.npc.witch.name": "Астрид",
    "dialog.npc.witch.chatter.description": "Разговор с Астрид",
    "dialog.npc.witch.intro.description": "Знакомство с Астрид",
    "dialog.npc.witch.intro.0.line_0": "Хи-хи... Кто это тут у нас забрёл в мою обитель?",
    "dialog.npc.witch.intro.0.line_1": "Меня зовут Астрид. Я храню тайны трав, звёзд и древних ритуалов.",
    "dialog.npc.witch.intro.0.line_2": "Если ищешь кристаллы забвения или редкие алхимические компоненты — ты пришёл по адресу.",
    "dialog.npc.witch.intro.0.line_3": "Только не суй нос в мои кипящие котлы, если тебе дороги твои брови!",

    "dialog.npc.witch.chatter_friendship0.0.line_0": "Луна сегодня особенно яркая... Время собирать ночные травы.",
    "dialog.npc.witch.chatter_friendship0.1.line_0": "Чувствуешь дрожь в воздухе? Лес шепчет о скорых переменах.",

    "dialog.npc.witch.gift_loved.0.line_0": "О-о-о! Какая редкая и мощная эссенция! Ты знаешь, чем растопить сердце ведьмы, @i!",
    "dialog.npc.witch.gift_liked.0.line_0": "Любопытный ингредиент. Он отлично дополнит моё новое зелье.",
    "dialog.npc.gift_neutral.0.line_0": "Сойдёт для простых отваров.",
    "dialog.npc.witch.gift_disliked.0.line_0": "Фи, какая банальность. В этом нет ни капли магии.",
    "dialog.npc.witch.gift_hated.0.line_0": "Превратить тебя в жабу за такую дерзость?!"
}

for k, en_text in all_keys.get('07_witch.md', {}).items():
    if k not in astrid:
        astrid[k] = en_text

update_md('07_witch.md', astrid)

# ==========================================
# 08_librarian.md (Samuel)
# ==========================================
samuel = {
    "dialog.npc.librarian.name": "Сэмюэль",
    "dialog.npc.librarian.chatter.description": "Разговор с Сэмюэлем",
    "dialog.npc.librarian.intro.description": "Знакомство с Сэмюэлем",
    "dialog.npc.librarian.intro.0.line_0": "Приветствую! Меня зовут Сэмюэль. Я хранитель знаний и книг Солнечной Долины.",
    "dialog.npc.librarian.intro.0.line_1": "Книги — величайшее сокровище цивилизации. В них сокрыта мудрость веков.",
    "dialog.npc.librarian.intro.0.line_2": "У меня вы можете приобрести редкие рукописи, учебники и материалы для зачарования.",
    "dialog.npc.librarian.intro.0.line_3": "Соблюдайте тишину и берегите переплёты!",

    "dialog.npc.librarian.chatter_friendship0.0.line_0": "Запах старинного пергамента ни с чем не сравним.",
    "dialog.npc.librarian.chatter_friendship0.1.line_0": "Чтение расширяет горизонты разума.",

    "dialog.npc.librarian.gift_loved.0.line_0": "Невероятно! Бесценный фолиант! Я не верю своим глазам, спасибо, @i!",
    "dialog.npc.librarian.gift_liked.0.line_0": "Прекрасный подарок для любого книголюба. Благодарю вас.",
    "dialog.npc.librarian.gift_neutral.0.line_0": "Спасибо, пополнит наш скромный фонд.",
    "dialog.npc.librarian.gift_disliked.0.line_0": "Увы, это совершенно не относится к высокой литературе.",
    "dialog.npc.librarian.gift_hated.0.line_0": "Варварство! Немедленно уберите этот мусор из библиотеки!"
}

for k, en_text in all_keys.get('08_librarian.md', {}).items():
    if k not in samuel:
        samuel[k] = en_text

update_md('08_librarian.md', samuel)

print("Stage 2 translation complete!")
