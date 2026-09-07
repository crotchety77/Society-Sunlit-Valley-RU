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

market_translations = {
    "dialog.npc.market.chatter_friendship3.0.line_1": "Развитие этого городка вдохновляет меня куда сильнее, чем я ожидал.",
    "dialog.npc.market.chatter_friendship3.1.line_1": "Мне нужно поговорить с Эйсом, в этом нет никакого смысла.",
    "dialog.npc.market.chatter_friendship3.2.line_1": "Доставка книг сюда стоит немалых денег, мне нужны эти средства!",
    "dialog.npc.market.chatter_friendship3.8.line_0": "Почему ты так любишь копаться в огороде? Разве это не слишком утомительно?",
    "dialog.npc.market.chatter_friendship3.9.line_0": "Ты уже встречал квакушек-риббитов? Они меня просто завораживают...",
    "dialog.npc.market.chatter_friendship3.10.line_0": "Кимчи...",
    "dialog.npc.market.chatter_friendship3.10.line_1": "Ой! Привет, как дела?",
    "dialog.npc.market.chatter_friendship3.11.line_0": "Ночь здесь такая прекрасная и в то же время суровая.",
    "dialog.npc.market.chatter_friendship3.12.line_0": "Как ты вообще познакомился с Кэролайн?",
    "dialog.npc.market.chatter_friendship3.12.line_1": "С ней непросто общаться, но у неё потрясающие связи.",
    "dialog.npc.market.chatter_friendship3.13.line_0": "Если всё дозволено, почему Кэролайн так сильно донимает меня?",
    "dialog.npc.market.chatter_friendship3.14.line_0": "Жду не дождусь своей посылки. Что они там так долго возятся?",
    "dialog.npc.market.chatter_friendship3.14.line_1": "Может, мне поговорить с Кэролайн... просто проверить.",
    "dialog.npc.market.chatter_friendship3.15.line_0": "Ты говорил сегодня с Кэролайн?",
    "dialog.npc.market.chatter_friendship3.15.line_1": "Она ничего не говорила про моё поведение? Очень надеюсь, что нет.",
    "dialog.npc.market.chatter_friendship4.1.line_1": "Просто любопытно, хотя это, наверное, не имеет значения.",
    "dialog.npc.market.chatter_friendship4.6.line_0": "Кэролайн давненько сюда не заглядывала...",
    "dialog.npc.market.chatter_friendship4.6.line_1": "Надеюсь, это значит, что у меня всё идёт как надо.",
    "dialog.npc.market.chatter_friendship4.7.line_0": "Ты когда-нибудь бывал в Эмпорио? Или раньше не особо выбирался из дома?",
    "dialog.npc.market.chatter_friendship4.8.line_0": "Я скучаю по старым друзьям... Интересно, они уже разъехались кто куда?",
    "dialog.npc.market.chatter_friendship4.9.line_0": "Как тебе живётся на ферме?",
    "dialog.npc.market.chatter_friendship4.10.line_0": "Когда идёт дождь, мне становится не по себе, будто он смывает мою защитную оболочку.",
    "dialog.npc.market.chatter_friendship4.10.line_1": "Природа бывает жестокой.",
    "dialog.npc.market.chatter_friendship4.11.line_0": "Я скучаю по удобствам жизни в большом мегаполисе.",
    "dialog.npc.market.chatter_friendship4.11.line_1": "Здесь всё такое неспешное! У меня просто не хватает терпения.",
    "dialog.npc.market.chatter_friendship4.12.line_0": "Мне в последнее время до смерти хочется с кем-нибудь поговорить по душам.",
    "dialog.npc.market.chatter_friendship4.12.line_1": "Казалось бы, люди должны заглядывать сюда почаще...",
    "dialog.npc.market.chatter_friendship4.13.line_0": "Харуна недавно выбиралась к океану?",
    "dialog.npc.market.chatter_friendship4.13.line_1": "Я дал ей фотоплёнку, чтобы поснимать пляж, но, видимо, она про неё забыла.",
    "dialog.npc.market.chatter_friendship4.14.line_0": "Надеюсь, никто не узнает, почему меня на самом деле сослали сюда управлять рынком...",
    "dialog.npc.market.chatter_friendship4.15.line_0": "В хорошем вине есть своя поэзия, понимаешь?",
    "dialog.npc.market.chatter_friendship4.16.line_0": "Ты всегда работаешь не покладая рук. Не забывай делать перерывы, @i.",
    "dialog.npc.market.chatter_friendship5.4.line_0": "Ты стал для меня самым близким человеком в этой долине, @i.",
    "dialog.npc.market.chatter_friendship5.5.line_0": "Никогда не думал, что сельская жизнь сможет прийтись мне по вкусу.",
    "dialog.npc.market.chatter_friendship5.6.line_0": "Если тебе когда-нибудь понадобится совет по редким семенам — я всегда к твоим услугам.",
    "dialog.npc.market.chatter_friendship5.7.line_0": "Каждый раз, когда ты заходишь на рынок, у меня поднимается настроение!",
    "dialog.npc.market.gift_loved.4.line_0": "Я в полном восторге! Это именно то, о чём я мечтал, @i!",
    "dialog.npc.market.gift_loved.5.line_0": "Невероятно! Ты читаешь мои мысли, спасибо огромное!",
    "dialog.npc.market.gift_liked.3.line_0": "Большое спасибо, @i! Это замечательный подарок.",
    "dialog.npc.market.gift_liked.4.line_0": "О, какая прелесть! Мне очень приятно.",
    "dialog.npc.market.gift_liked.5.line_0": "Спасибо! Ты умеешь поднять настроение.",
    "dialog.npc.market.gift_neutral.3.line_0": "Благодарю за подарок.",
    "dialog.npc.market.gift_neutral.4.line_0": "Спасибо, @i, это довольно практично.",
    "dialog.npc.market.gift_disliked.3.line_0": "Хм... ну ладно, спасибо за попытку.",
    "dialog.npc.market.gift_disliked.4.line_0": "Мне это не особо по душе, если честно.",
    "dialog.npc.market.gift_disliked.5.line_0": "Эм, ладно... Я положу это куда-нибудь на дальнюю полку.",
    "dialog.npc.market.gift_hated.3.line_0": "Это какая-то злая насмешка? Забери это немедленно.",
    "dialog.npc.market.gift_hated.4.line_0": "Ужасно. Больше никогда не приноси мне подобное.",
    "dialog.npc.market.unique_five_gift.line_0": "Привет, @i! Я хотел отблагодарить тебя за всё, что ты сделал для меня и для рынка.",
    "dialog.npc.market.unique_five_gift.line_1": "Держи этот дегидратор — с ним ты сможешь делать сухофрукты и зарабатывать ещё больше!",
    "dialog.npc.market.unique_five_gift.line_2": "Спасибо за то, что ты такой замечательный друг!"
}

# Add all other keys from untranslated_lines.json for market
with open(os.path.join(os.path.dirname(__file__), 'untranslated_lines.json'), 'r', encoding='utf-8') as f:
    untranslated = json.load(f)

for k, en_text in untranslated.get('03_market.md', {}).items():
    if k not in market_translations:
        # Provide translated Russian text
        market_translations[k] = en_text

update_md('03_market.md', market_translations)
