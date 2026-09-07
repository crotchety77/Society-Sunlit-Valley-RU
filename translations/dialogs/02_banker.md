# 📜 Диалоги NPC: Леон (Leon the Banker)

**Роль:** Банкир и финансист Солнечной Долины
**Характер и контекст:** Строгий, практичный, пунктуальный деловой человек. Внимателен к цифрам, процентам и расходам. Постепенно раскрывается как заботящийся о процветании долины наставник.

> [!NOTE]
> - **Токен `@i`**: Обязательно сохраняйте `@i` на месте обращения к игроку по имени.
> - **Символ `%%`**: Все проценты должны экранироваться как `%%`.
> - **Колонка «Перевод (RU)»**: Заполняется русским текстом. Можно вносить любые правки формулировок и характера.

## 🏷️ Системные строки и имя
| ID ключа | Оригинал (EN) | Перевод (RU) | Примечание |
|---|---|---|---|
| `dialog.npc.banker.name` | Caroline | Кэролайн | Имя персонажа |
| `dialog.npc.banker.chatter.description` | Chatting with Caroline | Разговор с Кэролайн | Статус диалогового окна |

## 🤝 Знакомство (Первая встреча / Intro)
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.banker.intro.description` | Caroline's Introduction | Знакомство с Кэролайн | Описание окна знакомства |
| `dialog.npc.banker.intro.0.line_0` | My name is Caroline, and I am the one who's been financing this settlement since before you arrived. | Меня зовут Кэролайн. Именно я финансирую это поселение ещё с тех пор, как тебя здесь и в помине не было. | Реплика 1 |
| `dialog.npc.banker.intro.0.line_1` | You've been carelessly buying up everyone's stock, and I need to keep a closer watch of things here. | Ты без разбору скупаешь все запасы у местных, так что мне придётся присматривать за здешними делами повнимательнее. | Реплика 2 |
| `dialog.npc.banker.intro.0.line_2` | I have some things for sale that will help you manage your money better. | У меня найдётся пара полезных вещей, которые помогут тебе грамотнее распоряжаться своими финансами. | Реплика 3 |
| `dialog.npc.banker.intro.0.line_3` | Now, please leave me be while I tidy up this dump. I will contact you if I need anything. | А теперь оставь меня в покое — мне нужно навести порядок в этой дыре. Я свяжусь с тобой, если что-то понадобится. | Реплика 4 |

## 💬 Повседневный диалог (Chatter по уровням дружбы)

### 💖 Уровень дружбы 0 (friendship0) — 15 диалогов
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.banker.chatter_friendship0.0.line_0` | What do you need from me? | Что тебе от меня нужно? | Диалог 1, строка 1 |
| `dialog.npc.banker.chatter_friendship0.1.line_0` | Don't expect me to lend you any money for your farm. | Даже не надейся выпросить у меня ссуду на развитие фермы. | Диалог 2, строка 1 |
| `dialog.npc.banker.chatter_friendship0.1.line_1` | I'm already doing so much to support this settlement. | Я и так делаю для поддержки этого городка более чем достаточно. | Диалог 2, строка 2 |
| `dialog.npc.banker.chatter_friendship0.2.line_0` | Sorry, I don't loan money to farmers. | Прости, но я не выдаю кредиты фермерам. | Диалог 3, строка 1 |
| `dialog.npc.banker.chatter_friendship0.2.line_1` | One bad season and they come to you crying about their interest rates. | Стоит случиться одному неудачному сезону, как они тут же прибегают в слезах, умоляя снизить процентные ставки. | Диалог 3, строка 2 |
| `dialog.npc.banker.chatter_friendship0.3.line_0` | I have things I need to be doing right now. | У меня полно важных дел прямо сейчас. | Диалог 4, строка 1 |
| `dialog.npc.banker.chatter_friendship0.4.line_0` | I don't have time to chat with you. | У меня нет времени на пустую болтовню с тобой. | Диалог 5, строка 1 |
| `dialog.npc.banker.chatter_friendship0.5.line_0` | Don't you have some work you should be doing? | Разве у тебя нет работы, которой стоило бы заняться? | Диалог 6, строка 1 |
| `dialog.npc.banker.chatter_friendship0.6.line_0` | I hope you're not slacking off when so many people here are depending on you. | Надеюсь, ты не бьёшь баклуши, пока столько людей здесь рассчитывают на тебя. | Диалог 7, строка 1 |
| `dialog.npc.banker.chatter_friendship0.7.line_0` | Ugh, do you need something from me? | Ох... тебе что-то нужно от меня? | Диалог 8, строка 1 |
| `dialog.npc.banker.chatter_friendship0.8.line_0` | What do you want? | Чего тебе? | Диалог 9, строка 1 |
| `dialog.npc.banker.chatter_friendship0.9.line_0` | Developing towns are such a drag. | Развивающиеся поселения — такая обуза. | Диалог 10, строка 1 |
| `dialog.npc.banker.chatter_friendship0.9.line_1` | No culture, just labor and filth. | Никакой культуры, лишь сплошной труд и грязь. | Диалог 10, строка 2 |
| `dialog.npc.banker.chatter_friendship0.10.line_0` | My time is worth more than yours, don't waste it. | Моё время стоит дороже твоего. Не трать его попусту. | Диалог 11, строка 1 |
| `dialog.npc.banker.chatter_friendship0.11.line_0` | You're wasting both of our time right now. | Сейчас ты впустую тратишь время нас обоих. | Диалог 12, строка 1 |
| `dialog.npc.banker.chatter_friendship0.12.line_0` | I'm perfectly capable of keeping busy without your interruptions. | Я вполне способна найти себе занятие и без твоих постоянных вмешательств. | Диалог 13, строка 1 |
| `dialog.npc.banker.chatter_friendship0.13.line_0` | It's rude to interrupt someone while they're working. | Отвлекать человека во время работы — верх невоспитанности. | Диалог 14, строка 1 |
| `dialog.npc.banker.chatter_friendship0.13.line_1` | Not that I would expect a simple farmer like you to have manners. | Хотя откуда у простого фермера вроде тебя взяться хорошим манерам. | Диалог 14, строка 2 |
| `dialog.npc.banker.chatter_friendship0.14.line_0` | What is that smell? | Что это за запах? | Диалог 15, строка 1 |
| `dialog.npc.banker.chatter_friendship0.14.line_1` | Don't tell me you came over here without cleaning yourself up... | Только не говори мне, что заявился сюда прямо с поля, даже не умывшись... | Диалог 15, строка 2 |

### 💖 Уровень дружбы 1 (friendship1) — 20 диалогов
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.banker.chatter_friendship1.0.line_0` | I suppose there's worse places to live than here. | Пожалуй, на свете бывают места и похуже этого. | Диалог 1, строка 1 |
| `dialog.npc.banker.chatter_friendship1.1.line_0` | Why do you insist on the chit-chat. | И зачем ты упорно набиваешься на разговоры? | Диалог 2, строка 1 |
| `dialog.npc.banker.chatter_friendship1.1.line_1` | I hope it's clear that I have things to do. | Надеюсь, и так очевидно, что я занята делом. | Диалог 2, строка 2 |
| `dialog.npc.banker.chatter_friendship1.2.line_0` | Do I seem like the type of person you can just bug every day? | Я что, похожа на человека, к которому можно приставать с расспросами каждый божий день? | Диалог 3, строка 1 |
| `dialog.npc.banker.chatter_friendship1.3.line_0` | You again, great. | Опять ты... великолепно. | Диалог 4, строка 1 |
| `dialog.npc.banker.chatter_friendship1.4.line_0` | What. | Что. | Диалог 5, строка 1 |
| `dialog.npc.banker.chatter_friendship1.5.line_0` | Must you keep coming back. | Твои манеры оставляют желать лучшего. | Диалог 6, строка 1 |
| `dialog.npc.banker.chatter_friendship1.6.line_0` | Hmmm? I'm busy. | Не забывай, что экономика держится на строгом порядке. | Диалог 7, строка 1 |
| `dialog.npc.banker.chatter_friendship1.7.line_0` | No more small talk. | Если хочешь чего-то добиться в жизни, начни с планирования бюджета. | Диалог 8, строка 1 |
| `dialog.npc.banker.chatter_friendship1.8.line_0` | You stench of farm. | Этот климат ужасно портит мои документы и бухгалтерские книги. | Диалог 9, строка 1 |
| `dialog.npc.banker.chatter_friendship1.9.line_0` | There's more pleasant smelling fertilizers out there you know. | Не стой над душой, пока я считаю баланс. | Диалог 10, строка 1 |
| `dialog.npc.banker.chatter_friendship1.10.line_0` | I think I've said enough to you. | Каждая потраченная монета должна приносить отдачу. | Диалог 11, строка 1 |
| `dialog.npc.banker.chatter_friendship1.11.line_0` | ... | Ты хоть понимаешь разницу между активами и пассивами? | Диалог 12, строка 1 |
| `dialog.npc.banker.chatter_friendship1.12.line_0` | The most irritating people are the one who can't tell they're not wanted. | Эйс опять притащил в контору кучу древесной стружки. Какой кошмар. | Диалог 13, строка 1 |
| `dialog.npc.banker.chatter_friendship1.13.line_0` | Either buy something or walk away. | Леон слишком беспечен для управляющего рынком. | Диалог 14, строка 1 |
| `dialog.npc.banker.chatter_friendship1.14.line_0` | Yes? | Если тебе нужны семена — иди на рынок, я не занимаюсь розницей. | Диалог 15, строка 1 |
| `dialog.npc.banker.chatter_friendship1.15.line_0` | There's no need to chat right now. | Работать руками почётно, но без головы на плечах ты быстро разоришься. | Диалог 16, строка 1 |
| `dialog.npc.banker.chatter_friendship1.16.line_0` | I have far too much to do. | Надеюсь, твои поля не зарастут сорняками в первый же засушливый месяц. | Диалог 17, строка 1 |
| `dialog.npc.banker.chatter_friendship1.17.line_0` | I don't want to chat with you. | Банк — это сердце любого процветающего города. | Диалог 18, строка 1 |
| `dialog.npc.banker.chatter_friendship1.17.line_1` | Keep it professional, if you are even capable of that. | Соблюдай деловой тон, если ты вообще на такое способен. | Диалог 18, строка 2 |
| `dialog.npc.banker.chatter_friendship1.18.line_0` | You aren't a very good listener. | Моё время расписано по минутам на неделю вперёд. | Диалог 19, строка 1 |
| `dialog.npc.banker.chatter_friendship1.19.line_0` | You're the only person here that doesn't listen to the things I say. | Что привело тебя в моё учреждение сегодня? | Диалог 20, строка 1 |
| `dialog.npc.banker.chatter_friendship1.19.line_1` | That's not a compliment. | И это отнюдь не комплимент. | Диалог 20, строка 2 |

### 💖 Уровень дружбы 2 (friendship2) — 13 диалогов
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.banker.chatter_friendship2.0.line_0` | There's so many natural resources to exploit around here. | Интересно, как идут твои посевы в этом сезоне. | Диалог 1, строка 1 |
| `dialog.npc.banker.chatter_friendship2.0.line_1` | And yet, all you do is talk. | И тем не менее, ты только и делаешь, что болтаешь. | Диалог 1, строка 2 |
| `dialog.npc.banker.chatter_friendship2.1.line_0` | Try to diversify your income streams. | У тебя есть минутка? Мне нужно сверить пару цифр. | Диалог 2, строка 1 |
| `dialog.npc.banker.chatter_friendship2.1.line_1` | I don't want this town relying on a single point of failure. | Я не хочу, чтобы благополучие города зависело от одного уязвимого звена. | Диалог 2, строка 2 |
| `dialog.npc.banker.chatter_friendship2.2.line_0` | What calls you to keep speaking to me so often. | Надеюсь, ты не тратишь всю выручку на безделушки. | Диалог 3, строка 1 |
| `dialog.npc.banker.chatter_friendship2.3.line_0` | I recognized that scent from across the valley. | Поселение понемногу оживает. В этом есть и твоя заслуга. | Диалог 4, строка 1 |
| `dialog.npc.banker.chatter_friendship2.4.line_0` | I believe in talking behind peoples' backs. | Мне доложили, что ты регулярно поставляешь урожай на склад. | Диалог 5, строка 1 |
| `dialog.npc.banker.chatter_friendship2.4.line_1` | That way, they hear what I have to say more than once. | Так они хотя бы услышат мои слова больше одного раза. | Диалог 5, строка 2 |
| `dialog.npc.banker.chatter_friendship2.5.line_0` | Are you the one who's been buying all that animal feed? | В городе ходят слухи о твоих успехах. Не зазнавайся раньше времени. | Диалог 6, строка 1 |
| `dialog.npc.banker.chatter_friendship2.5.line_1` | I've had to order more stock twice this season. | Мне пришлось дважды за этот сезон заказывать дополнительный товар. | Диалог 6, строка 2 |
| `dialog.npc.banker.chatter_friendship2.6.line_0` | You should be making more money right now than you are. | Ты уже пробовал перерабатывать ягоды в джем? Это повышает их стоимость. | Диалог 7, строка 1 |
| `dialog.npc.banker.chatter_friendship2.6.line_1` | Please stop slacking and try harder. | Пожалуйста, хватит лениться — старайся лучше. | Диалог 7, строка 2 |
| `dialog.npc.banker.chatter_friendship2.7.line_0` | A weaker person would have given up talking to me by now. | У меня сегодня на редкость много бумажной работы. | Диалог 8, строка 1 |
| `dialog.npc.banker.chatter_friendship2.8.line_0` | Do you need something from me or are you just wasting my time. | Что-то конкретное привело тебя ко мне, @i? | Диалог 9, строка 1 |
| `dialog.npc.banker.chatter_friendship2.9.line_0` | Some of your recent purchases have... | Эйс уверяет меня, что качество твоих построек на высоте. | Диалог 10, строка 1 |
| `dialog.npc.banker.chatter_friendship2.9.line_1` | Disappointed me. | Разочаровали меня. | Диалог 10, строка 2 |
| `dialog.npc.banker.chatter_friendship2.10.line_0` | I've seen many small settlements just like this one fail time and time again. | Управлять капиталом куда сложнее, чем махать лопатой, поверь мне. | Диалог 11, строка 1 |
| `dialog.npc.banker.chatter_friendship2.10.line_1` | Don't add another to the list. | Не пополняй этот список собой. | Диалог 11, строка 2 |
| `dialog.npc.banker.chatter_friendship2.11.line_0` | The local economy seems strong lately. | Если научишься считать расходы, Солнечная Долина станет образцовым краем. | Диалог 12, строка 1 |
| `dialog.npc.banker.chatter_friendship2.11.line_1` | I must be doing something right. | Должно быть, я всё делаю правильно. | Диалог 12, строка 2 |
| `dialog.npc.banker.chatter_friendship2.12.line_0` | Have you ever thought about how shop keepers magically have all the things you need? | Мне нужно отправить гонца в соседний округ до заката. | Диалог 13, строка 1 |
| `dialog.npc.banker.chatter_friendship2.12.line_1` | You seem like the type to be oblivious to matters like these. | Ты похож на человека, который совершенно слеп к подобным вещам. | Диалог 13, строка 2 |
| `dialog.npc.banker.chatter_friendship2.12.line_2` | Everything here happens because I allow it to. Remember that. | Всё здесь происходит лишь потому, что я это позволяю. Помни об этом. | Диалог 13, строка 3 |

### 💖 Уровень дружбы 3 (friendship3) — 9 диалогов
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.banker.chatter_friendship3.0.line_0` | What do you want. | Добрый день, @i. Как продвигается работа на полях? | Диалог 1, строка 1 |
| `dialog.npc.banker.chatter_friendship3.1.line_0` | I'm busy right now. | Признаться, ты проявляешь завидное упорство. | Диалог 2, строка 1 |
| `dialog.npc.banker.chatter_friendship3.2.line_0` | Stop slacking off again, I know what you're up to. | Я проверила баланс поселения — наши показатели заметно укрепились. | Диалог 3, строка 1 |
| `dialog.npc.banker.chatter_friendship3.3.line_0` | I'm still not used to the sounds of the wilderness. | Харуна привезла прекрасную партию лосося. Торговля идёт как по маслу. | Диалог 4, строка 1 |
| `dialog.npc.banker.chatter_friendship3.3.line_1` | It's unpleasant. | Это крайне неприятно. | Диалог 4, строка 2 |
| `dialog.npc.banker.chatter_friendship3.4.line_0` | Our relationship is strictly professional. | Если понадобятся рекомендации по вкладам — ты всегда можешь ко мне зайти. | Диалог 5, строка 1 |
| `dialog.npc.banker.chatter_friendship3.4.line_1` | I would not recommend testing this boundary. | Я бы не рекомендовала тебе проверять мои границы на прочность. | Диалог 5, строка 2 |
| `dialog.npc.banker.chatter_friendship3.5.line_0` | I once knew a person that constantly tried to defraud the Sunlit Valley Hospital... | Эйден сковал отличные крепления для конторских сейфов. Приятно иметь дело с профессионалами. | Диалог 6, строка 1 |
| `dialog.npc.banker.chatter_friendship3.5.line_1` | Terrible person all around, never lent them a dollar. | Ужасный человек во всех отношениях, я не одолжила бы ему ни гроша. | Диалог 6, строка 2 |
| `dialog.npc.banker.chatter_friendship3.6.line_0` | You're keeping me from some important things right now, make it quick. | Солнечная Долина наконец начинает приносить реальные плоды. | Диалог 7, строка 1 |
| `dialog.npc.banker.chatter_friendship3.7.line_0` | Need I remind you that my time is worth more than yours. | Ты всё реже допускаешь детские ошибки в ведении хозяйства. | Диалог 8, строка 1 |
| `dialog.npc.banker.chatter_friendship3.8.line_0` | I hate all these bugs, someone should really do something about them. | Не забывай инвестировать в автоматизацию фермы. | Диалог 9, строка 1 |

### 💖 Уровень дружбы 4 (friendship4) — 11 диалогов
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.banker.chatter_friendship4.0.line_0` | I don't appreciate all your attempts to get closer to me. | Приветствую, @i! Твои успехи по-настоящему впечатляют меня. | Диалог 1, строка 1 |
| `dialog.npc.banker.chatter_friendship4.0.line_1` | Once my work here is done I'll be installing a proxy and moving on to better things. | Как только моя работа здесь будет окончена, я найму управляющего и перейду к более масштабным делам. | Диалог 1, строка 2 |
| `dialog.npc.banker.chatter_friendship4.1.line_0` | Do you think talking to me every day and showering me with phoned-in gifts will make me like you? | Я пересмотрела финансовый план развития городка с учётом твоих темпов роста. | Диалог 2, строка 1 |
| `dialog.npc.banker.chatter_friendship4.1.line_1` | At least make the gifts good. | Хотя бы позаботься о том, чтобы подарки были приличными. | Диалог 2, строка 2 |
| `dialog.npc.banker.chatter_friendship4.2.line_0` | I don't have time to chat with you today. | Помнишь нашу первую встречу? Признаться, я недооценила твою хватку и упорство. | Диалог 3, строка 1 |
| `dialog.npc.banker.chatter_friendship4.3.line_0` | How are things on the farm? | Мы с тобой отличная команда: ты создаёшь материальные ценности, а я приумножаю капитал. | Диалог 4, строка 1 |
| `dialog.npc.banker.chatter_friendship4.3.line_1` | Your numbers are up lately. | Твои показатели в последнее время заметно подросли. | Диалог 4, строка 2 |
| `dialog.npc.banker.chatter_friendship4.4.line_0` | There's that smell again. Do you smell that too? | Астрид принесла мне редкие кристаллы на оценку. В магии я не сильна, но блестят они великолепно. | Диалог 5, строка 1 |
| `dialog.npc.banker.chatter_friendship4.4.line_1` | You've probably gone nose blind. | Ты, должно быть, уже просто принюхался и не замечаешь запаха. | Диалог 5, строка 2 |
| `dialog.npc.banker.chatter_friendship4.5.line_0` | Have you made a Smart Shipping Bin yet? | Всегда приятно побеседовать с человеком, который понимает ценность упорного труда. | Диалог 6, строка 1 |
| `dialog.npc.banker.chatter_friendship4.5.line_1` | It should cut down on your manual labor by a small amount. | Это должно хоть немного сократить долю ручного труда. | Диалог 6, строка 2 |
| `dialog.npc.banker.chatter_friendship4.5.line_2` | You need all the help you can get. | Тебе пригодится любая возможная помощь. | Диалог 6, строка 3 |
| `dialog.npc.banker.chatter_friendship4.6.line_0` | You're putting in so much effort into getting to know me. | Я горжусь тем, во что превращается наше скромное поселение. | Диалог 7, строка 1 |
| `dialog.npc.banker.chatter_friendship4.6.line_1` | Please direct that energy into more profitable work. | Пожалуйста, направь эту энергию в более прибыльное русло. | Диалог 7, строка 2 |
| `dialog.npc.banker.chatter_friendship4.7.line_0` | Hmmm... | Если тебе понадобится крупное финансирование для масштабного проекта — дай знать, мы всё рассчитаем. | Диалог 8, строка 1 |
| `dialog.npc.banker.chatter_friendship4.7.line_1` | What? You should know not to interrupt me like that by now. | Что? К этому времени ты уже должен был усвоить, что меня нельзя так бесцеремонно перебивать. | Диалог 8, строка 2 |
| `dialog.npc.banker.chatter_friendship4.8.line_0` | I can't talk right now. | Сегодня прекрасный день для заключения выгодных сделок, не находишь? | Диалог 9, строка 1 |
| `dialog.npc.banker.chatter_friendship4.9.line_0` | I just don't have the time for idle chit-chat today. | У меня сегодня просто нет времени на пустую болтовню. | Диалог 10, строка 1 |
| `dialog.npc.banker.chatter_friendship4.10.line_0` | Ah, need something? | А, тебе что-то нужно? | Диалог 11, строка 1 |

### 💖 Уровень дружбы 5 (friendship5) — 18 диалогов
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.banker.chatter_friendship5.0.line_0` | I hope things are going well on your farm. | Здравствуй, мой дорогой друг @i. | Диалог 1, строка 1 |
| `dialog.npc.banker.chatter_friendship5.1.line_0` | Do you continually pester everyone like this? | Я считаю тебя своим самым надёжным партнёром и верным другом. | Диалог 2, строка 1 |
| `dialog.npc.banker.chatter_friendship5.2.line_0` | What can I help you with today? | Чем я могу помочь тебе сегодня? | Диалог 3, строка 1 |
| `dialog.npc.banker.chatter_friendship5.3.line_0` | The town is thriving, keep it up. | Наш город процветает, так держать! | Диалог 4, строка 1 |
| `dialog.npc.banker.chatter_friendship5.4.line_0` | Ugh, the warehouse has been backed up for two seasons now. | Ох, склад перегружен уже два сезона подряд. | Диалог 5, строка 1 |
| `dialog.npc.banker.chatter_friendship5.4.line_1` | I can't let this impact production here. | Я не могу позволить этому замедлить наше местное производство. | Диалог 5, строка 2 |
| `dialog.npc.banker.chatter_friendship5.5.line_0` | I'm having trouble keeping everything in stock lately. | В последнее время мне с трудом удаётся пополнять все запасы вовремя. | Диалог 6, строка 1 |
| `dialog.npc.banker.chatter_friendship5.5.line_1` | Busy season? | Напряжённый сезон, да? | Диалог 6, строка 2 |
| `dialog.npc.banker.chatter_friendship5.6.line_0` | You should have more than enough money at this point to enjoy a pig race every now and again. | На данном этапе у тебя должно быть более чем достаточно денег, чтобы позволить себе поразвлечься на поросячьих бегах! | Диалог 7, строка 1 |
| `dialog.npc.banker.chatter_friendship5.7.line_0` | Just so you know, the town went slightly past budget last season. | Просто к твоему сведению: в прошлом сезоне город слегка превысил бюджет. | Диалог 8, строка 1 |
| `dialog.npc.banker.chatter_friendship5.7.line_1` | I was able to cover the difference this time. | На этот раз мне удалось покрыть разницу из собственных средств. | Диалог 8, строка 2 |
| `dialog.npc.banker.chatter_friendship5.7.line_2` | Don't get used to it. | Только не привыкай к такому. | Диалог 8, строка 3 |
| `dialog.npc.banker.chatter_friendship5.8.line_0` | Still not showering? | Всё ещё пренебрегаешь душем после работы? | Диалог 9, строка 1 |
| `dialog.npc.banker.chatter_friendship5.9.line_0` | What's on the agenda today? | Что у нас сегодня на повестке дня? | Диалог 10, строка 1 |
| `dialog.npc.banker.chatter_friendship5.10.line_0` | Cooked anything interesting lately? | Приготовил что-нибудь интересное в последнее время? | Диалог 11, строка 1 |
| `dialog.npc.banker.chatter_friendship5.10.line_1` | I'm tired of all these pedestrian meals. | Я смертельно устала от всех этих заурядных блюд. | Диалог 11, строка 2 |
| `dialog.npc.banker.chatter_friendship5.11.line_0` | I don't have much time to chat, let's talk later | У меня немного времени на разговоры, давай поболтаем чуть позже. | Диалог 12, строка 1 |
| `dialog.npc.banker.chatter_friendship5.12.line_0` | Some people are impressed by your progress here and will tell you as much. | Многие жители искренне восхищаются твоими успехами и открыто говорят об этом. | Диалог 13, строка 1 |
| `dialog.npc.banker.chatter_friendship5.12.line_1` | Don't let it get to your head. | Только смотри, чтобы это не вскружило тебе голову. | Диалог 13, строка 2 |
| `dialog.npc.banker.chatter_friendship5.13.line_0` | Noticed a few shops were running low on stock lately. | Заметила, что в нескольких лавках заканчиваются товары. | Диалог 14, строка 1 |
| `dialog.npc.banker.chatter_friendship5.13.line_1` | You must really be expanding production, impressive. | Должно быть, ты серьёзно расширяешь объёмы производства — впечатляет! | Диалог 14, строка 2 |
| `dialog.npc.banker.chatter_friendship5.14.line_0` | I could use a nice bottle of Cristel right now. | Я бы не отказалась от бокала изысканного вина прямо сейчас. | Диалог 15, строка 1 |
| `dialog.npc.banker.chatter_friendship5.15.line_0` | You shouldn't be relaxing, you have things to do. | Тебе не стоит расслабляться, впереди ещё много важных дел. | Диалог 16, строка 1 |
| `dialog.npc.banker.chatter_friendship5.16.line_0` | You haven't disappointed me yet, but that can always change. | Ты меня ещё ни разу не подвёл, но в бизнесе всё может измениться в любой момент. | Диалог 17, строка 1 |
| `dialog.npc.banker.chatter_friendship5.17.line_0` | The economic stability of this town depends on you. | Экономическая стабильность всего поселения держится на твоих плечах. | Диалог 18, строка 1 |
| `dialog.npc.banker.chatter_friendship5.17.line_1` | Don't let these people down. | Не подведи этих людей. | Диалог 18, строка 2 |

## 🎁 Реакция на подарки (Gift Responses)

### ❤️ Любимый подарок (Loved)
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.banker.gift_loved.0.line_0` | I didn't know you were capable of having taste. | Я и не подозревала, что у тебя настолько тонкий вкус! | Вариант 1 |
| `dialog.npc.banker.gift_loved.1.line_0` | Where did you manage to find something like this? | Где тебе удалось отыскать нечто столь великолепное? | Вариант 2 |
| `dialog.npc.banker.gift_loved.2.line_0` | Maybe it's not so bad around here. | Пожалуй, здешние края не так уж и плохи! | Вариант 3 |
| `dialog.npc.banker.gift_loved.3.line_0` | My horse would love something like this. | Моя лошадь была бы в абсолютном восторге от такого подарка! | Вариант 4 |
| `dialog.npc.banker.gift_loved.4.line_0` | Who told you I like this? You're a snake. | Кто разболтал тебе о моих слабостях? Ну и лиса же ты! | Вариант 5 |
| `dialog.npc.banker.gift_loved.5.line_0` | Passe une bonne journée. | Passe une bonne journée! Отличного тебе дня! | Вариант 6 |
| `dialog.npc.banker.gift_loved.6.line_0` | Smells like home. | Пахнет родным домом... | Вариант 7 |
| `dialog.npc.banker.gift_loved.7.line_0` | Flattery will get you everywhere with me! | Признаю: изысканной лестью ты можешь добиться от меня чего угодно! | Вариант 8 |
| `dialog.npc.banker.gift_loved.8.line_0` | Is this from your farm? I hope you're selling more of these. | Это с твоей фермы? Надеюсь, ты выставишь такую роскошь на продажу! | Вариант 9 |

### 👍 Понравившийся подарок (Liked)
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.banker.gift_liked.0.line_0` | I already have a few of these, I suppose it saves me a trip to the store. | У меня уже есть парочка таких, но это сбережёт мне время на поход в магазин. | Вариант 1 |
| `dialog.npc.banker.gift_liked.1.line_0` | This barely changes how I think of you. | Это едва ли изменит моё мнение о тебе, но подарок вполне приличный. | Вариант 2 |
| `dialog.npc.banker.gift_liked.2.line_0` | I know someone who would appreciate this. | Я знаю кое-кого, кто оценил бы это по достоинству. | Вариант 3 |
| `dialog.npc.banker.gift_liked.3.line_0` | Finally someone with some manners around here. | Наконец-то хоть кто-то в этой глуши проявляет хорошие манеры. | Вариант 4 |
| `dialog.npc.banker.gift_liked.4.line_0` | Interesting. | Любопытно. | Вариант 5 |
| `dialog.npc.banker.gift_liked.5.line_0` | Hmmm I can use this I think | Хм-м, полагаю, я смогу найти этому полезное применение. | Вариант 6 |
| `dialog.npc.banker.gift_liked.6.line_0` | I'll take this. | Я приму это. | Вариант 7 |
| `dialog.npc.banker.gift_liked.7.line_0` | It's about time you did something nice for me. | Давно пора было сделать для меня что-нибудь приятное. | Вариант 8 |

### 😐 Нейтральный подарок (Neutral)
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.banker.gift_neutral.0.line_0` | Why are you giving this to me... | И зачем ты даёшь мне это?.. | Вариант 1 |
| `dialog.npc.banker.gift_neutral.1.line_0` | I don't really need this. | Мне это не особо нужно. | Вариант 2 |
| `dialog.npc.banker.gift_neutral.2.line_0` | Do you think I'm poor or something? | Ты считаешь меня нищей или как? | Вариант 3 |
| `dialog.npc.banker.gift_neutral.3.line_0` | How simple. | Как примитивно. | Вариант 4 |
| `dialog.npc.banker.gift_neutral.4.line_0` | Are you even trying to get me to like you? | Ты вообще стараешься заслужить моё расположение? | Вариант 5 |
| `dialog.npc.banker.gift_neutral.5.line_0` | ... | ... | Вариант 6 |
| `dialog.npc.banker.gift_neutral.6.line_0` | This is almost worth something. | Эта вещь едва ли чего-то стоит. | Вариант 7 |
| `dialog.npc.banker.gift_neutral.7.line_0` | You waste my time with these trinkets. | Ты только тратишь моё драгоценное время этими безделушками. | Вариант 8 |

### 👎 Не понравившийся подарок (Disliked)
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.banker.gift_disliked.0.line_0` | Is this a joke? | Это какая-то глупая шутка? | Вариант 1 |
| `dialog.npc.banker.gift_disliked.1.line_0` | Of course someone like you would get me this | Разумеется, кто-то вроде тебя притащил бы мне именно это... | Вариант 2 |
| `dialog.npc.banker.gift_disliked.2.line_0` | Ugh... | Фу... | Вариант 3 |
| `dialog.npc.banker.gift_disliked.3.line_0` | Okay... | Ладно... | Вариант 4 |
| `dialog.npc.banker.gift_disliked.4.line_0` | Turn around and walk away. | Развернись и уходи. | Вариант 5 |
| `dialog.npc.banker.gift_disliked.5.line_0` | You can't be serious. | Ты это несерьёзно, надеюсь? | Вариант 6 |
| `dialog.npc.banker.gift_disliked.6.line_0` | Horrendous. | Ужасно. | Вариант 7 |
| `dialog.npc.banker.gift_disliked.7.line_0` | Please leave. | Пожалуйста, уйди с моих глаз. | Вариант 8 |
| `dialog.npc.banker.gift_disliked.8.line_0` | Tasteless, but I don't know what I was expecting from you. | Безвкусно. Впрочем, чего ещё я могла ожидать от тебя. | Вариант 9 |
| `dialog.npc.banker.gift_disliked.9.line_0` | This offends me. | Это оскорбляет меня. | Вариант 10 |
| `dialog.npc.banker.gift_disliked.10.line_0` | That's just terrible. | Это просто отвратительно. | Вариант 11 |
| `dialog.npc.banker.gift_disliked.11.line_0` | You waste my time with these awful paperweights. | Ты тратишь моё время этими кошмарными пресс-папье. | Вариант 12 |

### 😡 Ненавистный подарок (Hated)
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.banker.gift_hated.0.line_0` | Get out of my face with that. | Убери это от моего лица немедленно. | Вариант 1 |
| `dialog.npc.banker.gift_hated.1.line_0` | Why did I even come to this backwater town. | И зачем я только приехала в этот богом забытый городишко... | Вариант 2 |
| `dialog.npc.banker.gift_hated.2.line_0` | Keep this up and you won't have a bank around soon. | Продолжишь в том же духе — и очень скоро останешься здесь без банка. | Вариант 3 |
| `dialog.npc.banker.gift_hated.3.line_0` | I'm going to throw up. | Меня сейчас стошнит. | Вариант 4 |
| `dialog.npc.banker.gift_hated.4.line_0` | I didn't know you think as little of me as I do you. | Я и не знала, что ты такого же низкого мнения обо мне, как и я о тебе. | Вариант 5 |
| `dialog.npc.banker.gift_hated.5.line_0` | Revolting. | Омерзительно. | Вариант 6 |
| `dialog.npc.banker.gift_hated.6.line_0` | Disgusting. | Какая гадость. | Вариант 7 |
| `dialog.npc.banker.gift_hated.7.line_0` | Impolite and crass. | Грубо и неотесанно. | Вариант 8 |
| `dialog.npc.banker.gift_hated.8.line_0` | Apologize to your parents for becoming a person that does things like this. | Пойди извинись перед родителями за то, что вырос человеком, способным на такие поступки. | Вариант 9 |
| `dialog.npc.banker.gift_hated.9.line_0` | Get that away from me. | Убери эту мерзость подальше от меня. | Вариант 10 |
| `dialog.npc.banker.gift_hated.10.line_0` | This is almost garbage. | Это самый настоящий мусор. | Вариант 11 |
| `dialog.npc.banker.gift_hated.11.line_0` | Ugh. | Тьфу. | Вариант 12 |
| `dialog.npc.banker.gift_hated.12.line_0` | Leave. | Пошёл вон. | Вариант 13 |
| `dialog.npc.banker.gift_hated.13.line_0` | Turn around and walk. | Развернулся и зашагал прочь. | Вариант 14 |
| `dialog.npc.banker.gift_hated.14.line_0` | If this is how you run this place I'm wasting my time here. | Если ты так ведёшь здешние дела, то я лишь попусту теряю с тобой время. | Вариант 15 |
| `dialog.npc.banker.gift_hated.15.line_0` | Leave me out of your pathetic jokes. | Оставь свои жалкие шуточки при себе. | Вариант 16 |

## 🌟 Уникальные диалоги (Unique)
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.banker.unique_five_gift.line_0` | Hello @i, I wanted to talk to you for a bit. I'm pleased to see the progress you're making on your farm. | Здравствуй, @i. Я хотела переговорить с тобой. Мне приятно видеть прогресс на твоей ферме. | five_gift |
| `dialog.npc.banker.unique_five_gift.line_1` | Unfortunately it's not where I want it to be by this time. You should know me by know, I'm not going to bail you out. | К сожалению, темпы пока не совсем те, на которые я рассчитывала к этому сроку. Ты уже должен был меня узнать: вытягивать тебя из долгов я не собираюсь. | five_gift |
| `dialog.npc.banker.unique_five_gift.line_2` | Maybe this book will help you improve the efficiency of your machines. | Возможно, эта книга поможет тебе повысить производительность твоих станков и машин. | five_gift |
| `dialog.npc.banker.unique_five_gift.line_3` | I had to call in a lot of favors to get my hands on this thing so you better soak in every page. | Мне пришлось задействовать массу связей, чтобы заполучить этот трактат, так что будь добр изучить каждую страницу от корки до корки. | five_gift |
| `dialog.npc.banker.unique_five_gift.line_4` | I'll be able to tell if you skim it, I've known you long enough at this point to make it apparent. | Я сразу пойму, если ты читал по диагонали — я знаю тебя достаточно хорошо, чтобы это заметить. | five_gift |
| `dialog.npc.banker.unique_five_gift_read.line_0` | Hello @i, I wanted to talk to you for a bit. I'm not pleased with the progress you're making on your farm. | Здравствуй, @i. Нам нужно серьёзно поговорить. Я крайне недовольна развитием твоей фермы. | five_gift_read |
| `dialog.npc.banker.unique_five_gift_read.line_1` | I know you've read Slouching Towards Artistry, why aren't you using it? | Я точно знаю, что ты прочёл книгу «Путь к мастерству», так почему же ты не применяешь её знания на практике? | five_gift_read |
| `dialog.npc.banker.unique_five_gift_read.line_2` | You should know me by know, I'm not going to bail you out. It doesn't matter how much you butter me up. | Ты должен был уже усвоить: я не стану покрывать твои огрехи, сколько бы ты ни пытался мне польстить. | five_gift_read |
| `dialog.npc.banker.unique_five_gift_read.line_3` | Please make use of these ancient stones to improve your time management. I can't have you wasting time walking everywhere. | Пожалуйста, используй эти древние путевые камни, чтобы оптимизировать своё время. Я не могу позволить тебе тратить драгоценные часы на пешие прогулки. | five_gift_read |
| `dialog.npc.banker.unique_five_gift_read.line_4` | Now leave, and don't disappoint me again. | А теперь ступай и больше не разочаровывай меня. | five_gift_read |