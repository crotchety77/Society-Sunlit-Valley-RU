# 📜 Диалоги NPC: Ведьма (Witch)

**Роль:** Обитательница Незера и мастер мистических ритуалов
**Характер и контекст:** Эксцентричная, острая на язык, независимая ведьма. Понимает язык духов и животных, создает магические механизмы вроде Авто-ласки (Auto-Petter).

> [!NOTE]
> - **Токен `@i`**: Обязательно сохраняйте `@i` на месте обращения к игроку по имени.
> - **Символ `%%`**: Все проценты должны экранироваться как `%%`.
> - **Колонка «Перевод (RU)»**: Заполняется русским текстом. Можно вносить любые правки формулировок и характера.

## 🏷️ Системные строки и имя
| ID ключа | Оригинал (EN) | Перевод (RU) | Примечание |
|---|---|---|---|
| `dialog.npc.witch.name` | Evelyne | Эвелин | Имя персонажа |
| `dialog.npc.witch.chatter.description` | Chatting with Evelyne | Разговор с Эвелин | Статус диалогового окна |

## 🤝 Знакомство (Первая встреча / Intro)
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.witch.intro.description` | Evelyne's Introduction | Знакомство с Эвелин | Описание окна знакомства |
| `dialog.npc.witch.intro.0.line_0` | ...I know who YOU are! | ...Я знаю, кто ТЫ такой! | Реплика 1 |
| `dialog.npc.witch.intro.0.line_1` | But it's not about that! It's about me! And what you've seen! | Но дело не в этом! Дело во мне! И в том, что ты видел! | Реплика 2 |
| `dialog.npc.witch.intro.0.line_2` | Caroline told me all about your little trip to the Nether. I'll be needing to see your findings for my research! | Кэролайн рассказала мне о твоей вылазке в Незер. Мне понадобятся твои находки для исследований! | Реплика 3 |
| `dialog.npc.witch.intro.0.line_3` | Oh I'm also supposed to sell you some magical stuff I've been working on. I don't really want to, but that Caroline seems very threatening... | О, ещё я вроде как должна продавать тебе магические штуковины, над которыми работаю. Не то чтобы мне хотелось, но эта Кэролайн выглядит пугающе убедительно... | Реплика 4 |

## 💬 Повседневный диалог (Chatter по уровням дружбы)

### 💖 Уровень дружбы 0 (friendship0) — 7 диалогов
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.witch.chatter_friendship0.0.line_0` | Begone! I'm working! | Уходи! Я работаю! | Диалог 1, строка 1 |
| `dialog.npc.witch.chatter_friendship0.1.line_0` | I made everything more expensive, please don't buy it. | Я задрала цены на всё подряд, так что, пожалуйста, ничего не покупай. | Диалог 2, строка 1 |
| `dialog.npc.witch.chatter_friendship0.1.line_1` | That's a lie actually, Caroline audits my books regularly... | Хотя ладно, это ложь: Кэролайн регулярно проверяет мои гроссбухи... | Диалог 2, строка 2 |
| `dialog.npc.witch.chatter_friendship0.2.line_0` | What do you want!? | Чего тебе надо?! | Диалог 3, строка 1 |
| `dialog.npc.witch.chatter_friendship0.3.line_0` | I didn't do it I swear, I bet Leon did it! | Клянусь, это не я сделала! Готова спорить, это Леон натворил! | Диалог 4, строка 1 |
| `dialog.npc.witch.chatter_friendship0.3.line_1` | Oh? Caroline didn't send you? Nevermind then. | А? Тебя послала не Кэролайн? Тогда проехали. | Диалог 4, строка 2 |
| `dialog.npc.witch.chatter_friendship0.4.line_0` | Sorry, I don't do tarot readings. Not that kind of witch. | Извини, я не гадаю на таро. Я ведьма совсем другого толка. | Диалог 5, строка 1 |
| `dialog.npc.witch.chatter_friendship0.5.line_0` | * It appears that Evelyne is sleepwalking * | * Похоже, Эвелин ходит во сне... * | Диалог 6, строка 1 |
| `dialog.npc.witch.chatter_friendship0.5.line_1` | * Would be best to leave your payment somewhere nearby... * | * Лучше просто оставить оплату где-нибудь поблизости... * | Диалог 6, строка 2 |
| `dialog.npc.witch.chatter_friendship0.6.line_0` | ...Hmmmmm? What do you want @i. | ...Хм-м-м-м? Чего тебе, @i? | Диалог 7, строка 1 |

### 💖 Уровень дружбы 1 (friendship1) — 5 диалогов
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.witch.chatter_friendship1.0.line_0` | What have you found today? You aren't holding out on me right? | Что интересного удалось откопать сегодня? Ты ведь не прячешь от меня редкие образцы, верно? | Диалог 1, строка 1 |
| `dialog.npc.witch.chatter_friendship1.1.line_0` | I don't like that Haruna... | Мне не нравится эта Харуна... | Диалог 2, строка 1 |
| `dialog.npc.witch.chatter_friendship1.1.line_1` | Why do people keep secrets from me! Of all people! | С какой стати люди вечно хранят от меня секреты?! От МЕНЯ, подумать только! | Диалог 2, строка 2 |
| `dialog.npc.witch.chatter_friendship1.2.line_0` | Do you have an appointment? | Вы записаны на приём? | Диалог 3, строка 1 |
| `dialog.npc.witch.chatter_friendship1.2.line_1` | Sorry, I've been asking everyone that, I can't find my calendar... | Прости, я сегодня всех об этом спрашиваю — просто не могу найти свой календарь... | Диалог 3, строка 2 |
| `dialog.npc.witch.chatter_friendship1.3.line_0` | Maria is so annoying about getting those Miracle Potions restocked! | Мария уже замучила меня своими просьбами пополнить запас чудо-зелий! | Диалог 4, строка 1 |
| `dialog.npc.witch.chatter_friendship1.3.line_1` | Who even needs that many animals! | Кому вообще нужно СТОЛЬКО животных?! | Диалог 4, строка 2 |
| `dialog.npc.witch.chatter_friendship1.4.line_0` | Found any weird bugs lately? I know a person that really likes weird bugs. | Не встречал странных жуков в последнее время? Я знаю одного типа, который прямо тащится от странных жуков. | Диалог 5, строка 1 |
| `dialog.npc.witch.chatter_friendship1.4.line_1` | I really need a favor from them, but I don't want anyone asking questions. | Мне очень нужна от него одна услуга, но я не хочу лишних расспросов. | Диалог 5, строка 2 |

### 💖 Уровень дружбы 2 (friendship2) — 6 диалогов
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.witch.chatter_friendship2.0.line_0` | You don't know a thing @i. There are forces at work you cannot imagine. | Ты ничегошеньки не смыслишь, @i. В мире действуют силы, которые ты даже представить не в состоянии. | Диалог 1, строка 1 |
| `dialog.npc.witch.chatter_friendship2.1.line_0` | Caroline is so mean to me! Everybody dozes off during business meetings, they're boring! | Кэролайн вечно ко мне придирается! Все вокруг засыпают на деловых планёрках, они же жутко скучные! | Диалог 2, строка 1 |
| `dialog.npc.witch.chatter_friendship2.2.line_0` | * You hear snoring as you approach. Evelyne is once again fast sleep while standing. * | * Приближаясь, вы слышите храп. Эвелин снова сладко спит прямо стоя. * | Диалог 3, строка 1 |
| `dialog.npc.witch.chatter_friendship2.3.line_0` | I'm a fountain of blood. In the shape of a girl... | Я фонтан крови в форме девушки... | Диалог 4, строка 1 |
| `dialog.npc.witch.chatter_friendship2.3.line_1` | I guess that makes you a bird? So they say of course. | Полагаю, это делает тебя птицей? По крайней мере, так говорят. | Диалог 4, строка 2 |
| `dialog.npc.witch.chatter_friendship2.4.line_0` | I've been studying the magic around here for a few seasons, there's definitely more to be found... | Я изучаю здешнюю магию уже несколько сезонов. Тут явно сокрыто нечто большее... | Диалог 5, строка 1 |
| `dialog.npc.witch.chatter_friendship2.4.line_1` | ...Keep that between us. | ...Только пусть это останется строго между нами. | Диалог 5, строка 2 |
| `dialog.npc.witch.chatter_friendship2.5.line_0` | There is a deeper magic in this valley, I can sense it and you can too. | В этой долине таится глубинная магия. Я чувствую её, и ты, уверена, тоже. | Диалог 6, строка 1 |

### 💖 Уровень дружбы 3 (friendship3) — 8 диалогов
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.witch.chatter_friendship3.0.line_0` | I don't know a thing!! There are forces at work I cannot imagine!! | Я НИЧЕГО не понимаю!! Вокруг действуют силы, которые я даже вообразить не могу!! | Диалог 1, строка 1 |
| `dialog.npc.witch.chatter_friendship3.1.line_0` | * You cannot tell if Evelyne is half asleep or about to yell strange things at you * | * Невозможно понять: Эвелин наполовину спит или собирается выкрикнуть заклинание * | Диалог 2, строка 1 |
| `dialog.npc.witch.chatter_friendship3.1.line_1` | Hmmm? Why are you staring at me like that? Buy something. | Хм-м-м? Чего ты так на меня уставился? Купи уже что-нибудь. | Диалог 2, строка 2 |
| `dialog.npc.witch.chatter_friendship3.2.line_0` | My plans are measured in centuries... | Мои планы рассчитаны на столетия вперёд... | Диалог 3, строка 1 |
| `dialog.npc.witch.chatter_friendship3.2.line_1` | ...But I cannot for the life of me remember where I put them... | ...Но я хоть убей не помню, куда положила свиток с записями... | Диалог 3, строка 2 |
| `dialog.npc.witch.chatter_friendship3.3.line_0` | I thought I could organize my worktable.... How Scandinavian of me! | Я решила навести идеальный порядок на рабочем столе... До чего по-скандинавски с моей стороны! | Диалог 4, строка 1 |
| `dialog.npc.witch.chatter_friendship3.4.line_0` | Ace has been such a treasure for finding me herbs. | Эйс — просто сокровище, он всегда приносит мне редкие травы. | Диалог 5, строка 1 |
| `dialog.npc.witch.chatter_friendship3.4.line_1` | I actually realllly hate being out in nature so I can appreciate a person that does. | Я на самом деле терпеееть не могу бродить по дикой природе, так что очень ценю тех, кто делает это за меня. | Диалог 5, строка 2 |
| `dialog.npc.witch.chatter_friendship3.5.line_0` | Just because the mind can make up whatever it wants, doesn't mean that it'll never come true... | То, что наш разум способен выдумать всё что угодно, вовсе не означает, что это никогда не сбудется... | Диалог 6, строка 1 |
| `dialog.npc.witch.chatter_friendship3.5.line_1` | So sayeth the matron saint! | Так гласят заветы верховной покровительницы! | Диалог 6, строка 2 |
| `dialog.npc.witch.chatter_friendship3.6.line_0` | I've made a break through last night! Normally I would tell you because we're friends and all but I think this one is a bit above your paygrade... | Вчера ночью я совершила грандиозный прорыв! Обычно я бы поделилась с тобой, мы ведь друзья, но это знание явно выше твоего допуска... | Диалог 7, строка 1 |
| `dialog.npc.witch.chatter_friendship3.7.line_0` | Please buy something, I need to bribe Aiden into giving me some expensive mining equipment! | Пожалуйста, купи что-нибудь! Мне срочно нужно подкупить Эйдена, чтобы он выдал мне дорогое шахтёрское снаряжение! | Диалог 8, строка 1 |

### 💖 Уровень дружбы 4 (friendship4) — 6 диалогов
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.witch.chatter_friendship4.0.line_0` | That stupid moon lady keeps yelling at me in my sleep! | Эта дурацкая лунная дева постоянно отчитывает меня во сне! | Диалог 1, строка 1 |
| `dialog.npc.witch.chatter_friendship4.0.line_1` | What's so wrong with hoarding? I might need this stuff again at some point! | И что плохого в накопительстве? Вдруг мне весь этот хлам ещё когда-нибудь пригодится! | Диалог 1, строка 2 |
| `dialog.npc.witch.chatter_friendship4.1.line_0` | You haven't been shipping enough minerals lately, please don't tell me you're keeping them all for yourself... | Ты в последнее время сдаёшь маловато минералов. Только не говори, что зажимаешь всё для себя... | Диалог 2, строка 1 |
| `dialog.npc.witch.chatter_friendship4.2.line_0` | You shouldn't let poets lie to you!! And by poets I mean that Leon!!! | Не позволяй поэтам вешать тебе лапшу на уши!! И под поэтами я имею в виду этого Леона!!! | Диалог 3, строка 1 |
| `dialog.npc.witch.chatter_friendship4.3.line_0` | I've seen it in a vision! | Я видела это в видении! | Диалог 4, строка 1 |
| `dialog.npc.witch.chatter_friendship4.3.line_1` | The crust of the Nether sinking to the bottom of the abyss, descending into the heavens! | Кора Незера опускается на дно бездны, взмывая прямо в небеса! | Диалог 4, строка 2 |
| `dialog.npc.witch.chatter_friendship4.3.line_2` | Purified into crystline fields of agonizing brightness! | Очищаясь в кристальные поля мучительно яркого света! | Диалог 4, строка 3 |
| `dialog.npc.witch.chatter_friendship4.3.line_3` | I'm certain it shall come to pass! | Я абсолютно уверена, что всё так и случится! | Диалог 4, строка 4 |
| `dialog.npc.witch.chatter_friendship4.4.line_0` | Welcome back @i! I have your special order somewhere around here, let me fetch it... | С возвращением, @i! Твой спецзаказ где-то тут валялся, сейчас достану... | Диалог 5, строка 1 |
| `dialog.npc.witch.chatter_friendship4.4.line_1` | Oh you didn't order anything? What am I supposed to do with 48 pounds of plorts? | А, ты ничего не заказывал? И что мне теперь делать с 20 килограммами плортов?! | Диалог 5, строка 2 |
| `dialog.npc.witch.chatter_friendship4.5.line_0` | Carlos keeps trying to give me these raw deals! Who has the time to make that much Truffle Tea? | Карлос постоянно пытается навязать мне грабительские сделки! У кого вообще есть время варить столько трюфельного чая? | Диалог 6, строка 1 |
| `dialog.npc.witch.chatter_friendship4.5.line_1` | Why would anyone want that much? | Зачем ему вообще СТОЛЬКО чая?! | Диалог 6, строка 2 |

### 💖 Уровень дружбы 5 (friendship5) — 5 диалогов
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.witch.chatter_friendship5.0.line_0` | Moon lady and I are on better terms these days but I still think she's way more aggressive than she should be... | Мы с лунной девой сейчас в лучших отношениях, но я всё равно считаю, что она чересчур агрессивная... | Диалог 1, строка 1 |
| `dialog.npc.witch.chatter_friendship5.1.line_0` | Now that we're such good friends... Do you mind cleaning up around here for me? We're friends right? | Раз уж мы такие закадычные друзья... Не поможешь прибраться в моей хижине? Мы ведь друзья, да? | Диалог 2, строка 1 |
| `dialog.npc.witch.chatter_friendship5.2.line_0` | Did you know that in some worlds, people train bugs and dragons to fight against each other? | А ты знал, что в некоторых мирах люди тренируют жуков и драконов для боёв друг с другом? | Диалог 3, строка 1 |
| `dialog.npc.witch.chatter_friendship5.2.line_1` | They let children do this, for money even! | Они позволяют заниматься этим детям, и даже за деньги! | Диалог 3, строка 2 |
| `dialog.npc.witch.chatter_friendship5.3.line_0` | Can you tell Vernoica there's another typo in the 12 edition of 'Gneiss' Dictionary of Geology & Mineralogy'? | Передай Веронике, что в 12-м издании «Словаря геологии и минералогии» Гнейса опять опечатка. | Диалог 4, строка 1 |
| `dialog.npc.witch.chatter_friendship5.3.line_1` | Honestly literature these days is in shambles, its embarrassing. | Честно говоря, современное книгоиздание в полном упадке, просто позорище. | Диалог 4, строка 2 |
| `dialog.npc.witch.chatter_friendship5.4.line_0` | Aiden keeps bringing me coffee every morning and I haven't figured out why... | Эйден каждое утро приносит мне кофе, и я до сих пор не поняла, зачем... | Диалог 5, строка 1 |
| `dialog.npc.witch.chatter_friendship5.4.line_1` | Maybe we have another occult researcher on our hands! | Может, в наших рядах появился ещё один тайный исследователь оккультизма?! | Диалог 5, строка 2 |

## 🎁 Реакция на подарки (Gift Responses)

### ❤️ Любимый подарок (Loved)
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.witch.gift_loved.0.line_0` | Where did you find this @i!? I've been looking for one of these for ages! | Где ты это откопал, @i?! Я искала такую вещь целую вечность! | Вариант 1 |
| `dialog.npc.witch.gift_loved.1.line_0` | I NEED ANOTHER. | МНЕ НУЖНО ЕЩЁ. | Вариант 2 |
| `dialog.npc.witch.gift_loved.1.line_1` | BRING ME ANOTHER. | ПРИНЕСИ МНЕ ЕЩЁ ТАКОГО. | Вариант 2 |
| `dialog.npc.witch.gift_loved.2.line_0` | This will keep me going for another few days, thank you @i. | Это поддержит мои силы ещё на пару дней, спасибо, @i. | Вариант 3 |
| `dialog.npc.witch.gift_loved.3.line_0` | Such a peculiar specimen... I think I'll keep it for my permanent collection. | Какой диковинный образец... Пожалуй, оставлю его для своей постоянной коллекции. | Вариант 4 |
| `dialog.npc.witch.gift_loved.4.line_0` | I knew you weren't useless! Caroline was wrong! Thank you @i! | Я знала, что от тебя есть толк! Кэролайн ошибалась! Спасибо, @i! | Вариант 5 |

### 👍 Понравившийся подарок (Liked)
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.witch.gift_liked.0.line_0` | I've been meaning to get more of these, thank you. | Я как раз собиралась раздобыть побольше таких штук, спасибо. | Вариант 1 |
| `dialog.npc.witch.gift_liked.1.line_0` | Who sent you? Do they know? | Кто тебя подослал? Они в курсе? | Вариант 2 |
| `dialog.npc.witch.gift_liked.1.line_1` | You seem confused, nevermind then. | Выглядишь растерянно... ладно, проехали. | Вариант 2 |
| `dialog.npc.witch.gift_liked.1.line_2` | Oh give me that before you go, I kinda want it. | Ой, дай сюда, пока не ушёл, мне это нужно. | Вариант 2 |
| `dialog.npc.witch.gift_liked.2.line_0` | Hand it over, I can use that. I think. | Давай сюда, пригодится в опытах. Наверное. | Вариант 3 |
| `dialog.npc.witch.gift_liked.3.line_0` | Sorry I don't have any money right now. | Прости, у меня сейчас нет при себе монет. | Вариант 4 |
| `dialog.npc.witch.gift_liked.3.line_1` | Oh, you're just giving it to me? Just like that? Okay weirdo. | Ой, ты просто так мне это отдаёшь? Задаром? Ну ты и чудик. | Вариант 4 |
| `dialog.npc.witch.gift_liked.4.line_0` | I can see why you would think this would be interesting to me. | Я понимаю, почему ты решил, что мне это будет интересно. | Вариант 5 |

### 😐 Нейтральный подарок (Neutral)
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.witch.gift_neutral.0.line_0` | Oh I needed more of these. | О, мне как раз не хватало таких штук. | Вариант 1 |
| `dialog.npc.witch.gift_neutral.1.line_0` | Just put that in the pile over there. | Просто брось в ту кучу в углу. | Вариант 2 |
| `dialog.npc.witch.gift_neutral.2.line_0` | Uhhhh I don't really research these types of things but I'm sure I could find a use for it! | Э-э-э, я вообще-то не изучаю подобные вещи, но, думаю, смогу найти применение! | Вариант 3 |
| `dialog.npc.witch.gift_neutral.3.line_0` | This is kinda boring, is this supposed to be for my research or a gift? | Скучновато. Это для моих исследований или подарок лично мне? | Вариант 4 |
| `dialog.npc.witch.gift_neutral.3.line_1` | Don't answer that, it's better that way. | Не отвечай, так даже загадочнее. | Вариант 4 |
| `dialog.npc.witch.gift_neutral.4.line_0` | Hmmmmmm...... | Хм-м-м-м-м...... | Вариант 5 |
| `dialog.npc.witch.gift_neutral.4.line_1` | ... | ... | Вариант 5 |
| `dialog.npc.witch.gift_neutral.4.line_2` | ... | * Непонятно: Эвелин пристально изучает подарок или тихо уснула стоя... * | Вариант 5 |
| `dialog.npc.witch.gift_neutral.4.line_3` | * You can't tell if Evelyne is studying the gift or has silently fallen asleep... * | Спасибо за подарок, пригодится в хозяйстве. | Вариант 5 |

### 👎 Не понравившийся подарок (Disliked)
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.witch.gift_disliked.0.line_0` | Woah, I didn't even know something this gross existed. | Ого, я даже не знала, что на свете существует настолько мерзкая дрянь. | Вариант 1 |
| `dialog.npc.witch.gift_disliked.1.line_0` | Oh I don't really need more cleaning supplies. | Мне точно не нужны дополнительные чистящие средства. | Вариант 2 |
| `dialog.npc.witch.gift_disliked.2.line_0` | I guess I could put this in my perpetual soup that kills people... | Пожалуй, я могла бы бросить это в свой вечный котёл, убивающий людей... | Вариант 3 |
| `dialog.npc.witch.gift_disliked.2.line_1` | ...You don't seriously believe I have one of those right? Go away. | ...Ты ведь не на полном серьёзе веришь, что у меня есть такой котёл? Уходи. | Вариант 3 |
| `dialog.npc.witch.gift_disliked.3.line_0` | Is that for me? Why? | Это мне? Зачем? | Вариант 4 |
| `dialog.npc.witch.gift_disliked.4.line_0` | I think this is more Maria's speed if you know what I mean. | По-моему, такое больше по вкусу Марии, если ты понимаешь, о чём я. | Вариант 5 |

### 😡 Ненавистный подарок (Hated)
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.witch.gift_hated.0.line_0` | Hmmmmm...? I don't really need more garbage to burn I have plenty. | Хм-м-м-м...? Мне не нужен лишний мусор для сжигания, у меня своего навалом. | Вариант 1 |
| `dialog.npc.witch.gift_hated.1.line_0` | I don't have space to keep this. | У меня нет места, чтобы хранить этот хлам. | Вариант 2 |
| `dialog.npc.witch.gift_hated.2.line_0` | Am I joke to you or something? Have some respect. | Я для тебя какая-то шутка? Имей хоть каплю уважения. | Вариант 3 |
| `dialog.npc.witch.gift_hated.3.line_0` | * You hear aggressively loud fake snoring. * | * Раздаётся вызывающе громкий наигранный храп. * | Вариант 4 |
| `dialog.npc.witch.gift_hated.3.line_1` | * It appears Evelyne does not want this. * | * Похоже, Эвелин категорически не желает это принимать. * | Вариант 4 |
| `dialog.npc.witch.gift_hated.4.line_0` | I really don't feel like throwing your garbage away for you. | У меня нет ни малейшего желания выносить за тобой мусор. | Вариант 5 |
| `dialog.npc.witch.gift_hated.5.line_0` | Oh, why are you giving this to me? I don't want this. | Зачем ты суёшь мне это? Мне оно даром не нужно. | Вариант 6 |
| `dialog.npc.witch.gift_hated.5.line_1` | Nobody wants this. | Никому такое не нужно. | Вариант 6 |

## 🌟 Уникальные диалоги (Unique)
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.witch.unique_five_gift.line_0` | Want to make Maria mad for me? Not for me actually, WITH ME. | Эй, @i! Я закончила работу над новым магическим устройством. | five_gift |
| `dialog.npc.witch.unique_five_gift.line_1` | Take this peculiar device and put it near your animals! | Держи этот автопоглаживатель для скота — он сам заботится о животных в хлеву, пока ты занят делом! | five_gift |
| `dialog.npc.witch.unique_five_gift.line_2` | It's imbued with the power of the sun and makes your animals feel as though they've been pet! | Теперь Мария точно перестанет донимать меня своими просьбами, хи-хи! | five_gift |
| `dialog.npc.witch.unique_five_gift.line_3` | Normally it's nearly impossible to get one of these things, but I reallly want to prove to Maria that cattle is cattle! | Магия леса открывается лишь тем, кто умеет слушать шёпот ветра. | five_gift |
| `dialog.npc.witch.unique_five_gift.line_4` | None of that 'love and affection' stuff! She's conning everyone and you will prove it! | Магия леса открывается лишь тем, кто умеет слушать шёпот ветра. | five_gift |