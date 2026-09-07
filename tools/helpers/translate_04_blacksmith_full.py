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

aiden = {
    "dialog.npc.blacksmith.name": "Эйден",
    "dialog.npc.blacksmith.chatter.description": "Разговор с Эйденом",
    "dialog.npc.blacksmith.intro.description": "Знакомство с Эйденом",
    "dialog.npc.blacksmith.intro.0.line_0": "Привет-привет, @i! Эйс рассказал мне всё о твоих грандиозных планах в долине.",
    "dialog.npc.blacksmith.intro.0.line_1": "Меня зовут Эйден. Я буду следить, чтобы твои инструменты всегда были острыми и готовыми к работе!",
    "dialog.npc.blacksmith.intro.0.line_2": "Если понадобятся кузнечные шаблоны или дробилки для жеод — просто загляни в мою кузницу.",
    "dialog.npc.blacksmith.intro.0.line_3": "Поднять такой город с нуля — задачка не из лёгких, и я с радостью тебе помогу!",

    "dialog.npc.blacksmith.chatter_friendship0.0.line_0": "Привет! Что-то нужно сковать?",
    "dialog.npc.blacksmith.chatter_friendship0.1.line_0": "Наконец-то решился улучшить инструменты?",
    "dialog.npc.blacksmith.chatter_friendship0.2.line_0": "Чем я могу тебе помочь, @i?",
    "dialog.npc.blacksmith.chatter_friendship0.3.line_0": "Здравствуй, @i! Что привело тебя в кузницу?",
    "dialog.npc.blacksmith.chatter_friendship0.4.line_0": "Есть с собой жеоды? Обожаю раскалывать их этими дробилками!",
    "dialog.npc.blacksmith.chatter_friendship0.5.line_0": "Много работы сегодня, @i?",
    "dialog.npc.blacksmith.chatter_friendship0.6.line_0": "Если кто-то говорит, что видел морское блюдечко — вежливо спросить, какого оно было вида.",
    "dialog.npc.blacksmith.chatter_friendship0.7.line_0": "Как продвигаются дела на ферме, @i?",
    "dialog.npc.blacksmith.chatter_friendship0.8.line_0": "Эйс столько рассказывал мне о долине перед моим переездом сюда.",
    "dialog.npc.blacksmith.chatter_friendship0.8.line_1": "Их искренняя любовь к природе видна невооружённым глазом!",
    "dialog.npc.blacksmith.chatter_friendship0.9.line_0": "Хм-м... руды под землёй предостаточно, но пещеры буквально кишат монстрами.",
    "dialog.npc.blacksmith.chatter_friendship0.9.line_1": "Будь осторожнее там внизу, @i!",
    "dialog.npc.blacksmith.chatter_friendship0.10.line_0": "На днях я прогуливался и готов поклясться, что видел уголёк на ножках...",
    "dialog.npc.blacksmith.chatter_friendship0.10.line_1": "В этих пещерах точно творится какая-то странная магия, я уверен!",
    "dialog.npc.blacksmith.chatter_friendship0.11.line_0": "Эй, @i, как успехи на ферме сегодня?",
    "dialog.npc.blacksmith.chatter_friendship0.12.line_0": "Ты уже успел спуститься в пещеры?",
    "dialog.npc.blacksmith.chatter_friendship0.12.line_1": "Скоро тебе понадобятся материалы из глубин, которых у меня нет на продажу.",
    "dialog.npc.blacksmith.chatter_friendship0.13.line_0": "Если нет времени бегать по шахтам ради сплинкеров — у меня в лавке есть готовые!",
    "dialog.npc.blacksmith.chatter_friendship0.13.line_1": "Ой, я вовсе не пытался навязать товар!! Просто хотел, чтобы ты знал!!",
    "dialog.npc.blacksmith.chatter_friendship0.14.line_0": "Кристаллы земли так мягко светятся в темноте, что их видно издалека!",
    "dialog.npc.blacksmith.chatter_friendship0.14.line_1": "Как по мне, они куда красивее любых алмазов!",
    "dialog.npc.blacksmith.chatter_friendship0.15.line_0": "Эйс подарил мне на днях потрясающий цветок. Удивительно, какие чудеса можно найти в диком лесу!",

    "dialog.npc.blacksmith.chatter_friendship1.0.line_0": "Улучшать инструменты важно, но и про броню не забывай!",
    "dialog.npc.blacksmith.chatter_friendship1.0.line_1": "Спускаться в пещеры без хороших доспехов может быть смертельно опасно.",
    "dialog.npc.blacksmith.chatter_friendship1.1.line_0": "Завалялись жеоды? Обожаю смотреть, как ты раскалываешь их!",
    "dialog.npc.blacksmith.chatter_friendship1.2.line_0": "Ты уже познакомился с Марией? Я ещё не встречал человека, который бы так ладил с животными.",
    "dialog.npc.blacksmith.chatter_friendship1.3.line_0": "Молот, наковальня и жаркий огонь в горне — вот всё, что нужно для настоящего счастья!",
    "dialog.npc.blacksmith.chatter_friendship1.4.line_0": "Если найдешь редкие минералы — обязательно принеси показать.",
    "dialog.npc.blacksmith.chatter_friendship1.5.line_0": "Эйс обещал помочь мне с пристройкой к кузнице, когда закончит с твоими заказами.",
    "dialog.npc.blacksmith.chatter_friendship1.6.line_0": "Качественная сталь куётся терпением и точным расчётом температуры.",
    "dialog.npc.blacksmith.chatter_friendship1.7.line_0": "Как продвигается расчистка фермы? Камни поддаются твоей кирке?",
    "dialog.npc.blacksmith.chatter_friendship1.8.line_0": "Всегда приятно видеть, как труд кузнеца облегчает жизнь фермеру.",
    "dialog.npc.blacksmith.chatter_friendship1.9.line_0": "Что для тебя сковать сегодня, @i?",

    "dialog.npc.blacksmith.chatter_friendship2.0.line_0": "Привет, @i! Твои инструменты всё ещё в строю?",
    "dialog.npc.blacksmith.chatter_friendship2.1.line_0": "Я тут экспериментирую с новым сплавом для мотыг — земля к ним почти не липнет!",
    "dialog.npc.blacksmith.chatter_friendship2.2.line_0": "Леон опять просил сделать открывашку покрепче. Видимо, у него большие планы на выходные.",
    "dialog.npc.blacksmith.chatter_friendship2.3.line_0": "В глубине шахт попадаются настоящие геологические сокровища.",
    "dialog.npc.blacksmith.chatter_friendship2.4.line_0": "Я выковал несколько колокольчиков для коров Марии — звон получился чистый и мелодичный.",
    "dialog.npc.blacksmith.chatter_friendship2.5.line_0": "Работать рядом с такими людьми, как ты и Эйс — одно удовольствие!",

    "dialog.npc.blacksmith.chatter_friendship3.0.line_0": "Здорово, @i! Как здоровье, как урожай?",
    "dialog.npc.blacksmith.chatter_friendship3.1.line_0": "Ты делаешь отличные успехи. Горжусь тем, как выглядит наша долина.",
    "dialog.npc.blacksmith.chatter_friendship3.2.line_0": "Харуна просила сковать прочные крючки для глубоководной рыбалки. Сделал на совесть!",
    "dialog.npc.blacksmith.chatter_friendship3.3.line_0": "Если тебе понадобятся особые металлические детали для механизмов — я всегда готов помочь.",

    "dialog.npc.blacksmith.chatter_friendship4.0.line_0": "Привет, дружище @i! Всегда рад видеть тебя в кузнице.",
    "dialog.npc.blacksmith.chatter_friendship4.1.line_0": "Благодаря тебе в Солнечной Долине кипит настоящая жизнь!",
    "dialog.npc.blacksmith.chatter_friendship4.2.line_0": "Ты стал для всех нас не просто соседом, а настоящей опорой.",

    "dialog.npc.blacksmith.chatter_friendship5.0.line_0": "Здравствуй, @i! Мой лучший друг и самый уважаемый фермер в округе!",
    "dialog.npc.blacksmith.chatter_friendship5.1.line_0": "Для тебя мои меха и наковальня всегда готовы к работе.",
    "dialog.npc.blacksmith.chatter_friendship5.2.line_0": "Я невероятно счастлив, что судьба свела нас в этой прекрасной долине.",

    "dialog.npc.blacksmith.gift_loved.0.line_0": "Ого! Это же просто великолепно! Огромное спасибо, @i!",
    "dialog.npc.blacksmith.gift_loved.1.line_0": "Потрясающий подарок! Ты прямо в душу мне заглянул!",
    "dialog.npc.blacksmith.gift_loved.2.line_0": "Какая красота! Я в полном восторге, спасибо тебе от всего сердца!",

    "dialog.npc.blacksmith.gift_liked.0.line_0": "О, отличная штука! Спасибо большое, @i.",
    "dialog.npc.blacksmith.gift_liked.1.line_0": "Мне очень приятно! Обязательно найду этому применение в кузнице.",

    "dialog.npc.blacksmith.gift_neutral.0.line_0": "Спасибо, пригодится.",
    "dialog.npc.blacksmith.gift_neutral.1.line_0": "Благодарю за подарок.",

    "dialog.npc.blacksmith.gift_disliked.0.line_0": "Э-э... спасибо, наверное?",
    "dialog.npc.blacksmith.gift_disliked.1.line_0": "Я не особо люблю такое, но всё равно спасибо.",

    "dialog.npc.blacksmith.gift_hated.0.line_0": "Фу, убери это от наковальни немедленно!",
    "dialog.npc.blacksmith.gift_hated.1.line_0": "Ты серьёзно принёс мне этот мусор? Не ожидал от тебя такого."
}

# Fill all remaining keys
for k, en_text in all_keys.get('04_blacksmith.md', {}).items():
    if k not in aiden:
        aiden[k] = en_text

update_md('04_blacksmith.md', aiden)
