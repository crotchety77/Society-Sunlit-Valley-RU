# 📜 Диалоги NPC: Экзотический торговец (Exotic Trader)

**Роль:** Торговец из Пещеры Черепа
**Характер и контекст:** Авантюрист и искатель редких сокровищ в глубинах пещер. Готов обменивать подземные реликвии на ценные предметы.

> [!NOTE]
> - **Токен `@i`**: Обязательно сохраняйте `@i` на месте обращения к игроку по имени.
> - **Символ `%%`**: Все проценты должны экранироваться как `%%`.
> - **Колонка «Перевод (RU)»**: Заполняется русским текстом. Можно вносить любые правки формулировок и характера.

## 🏷️ Системные строки и имя
| ID ключа | Оригинал (EN) | Перевод (RU) | Примечание |
|---|---|---|---|
| `dialog.npc.trader.name` | Carlos | Карлос | Имя персонажа |
| `dialog.npc.trader.chatter.description` | Chatting with Carlos | Разговор с Карлосом | Статус диалогового окна |

## 🤝 Знакомство (Первая встреча / Intro)
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.trader.intro.description` | Carlos's Introduction | Знакомство с Карлосом | Описание окна знакомства |
| `dialog.npc.trader.intro.0.line_0` | Hey hey it's @i! The one and only! | О, приветствую тебя, друг мой! Я странствую по дальним землям в поисках редчайших диковинок. | Реплика 1 |
| `dialog.npc.trader.intro.0.line_1` | I've been searching for someone that's been down in the Skull Cavern for ages! | Мой караван везёт товары, которых ты не сыщешь ни на одном местном рынке. | Реплика 2 |
| `dialog.npc.trader.intro.0.line_2` | It's a real treasure trove since so few people are willing to brave it! | Заглядывай в мою повозку, пока я не снялся с лагеря и не отправился дальше в путь! | Реплика 3 |
| `dialog.npc.trader.intro.0.line_3` | Oh well, I'm not one of those people! I'm very brave actually! | Для доброго покупателя у меня всегда припасены выгодные предложения. | Реплика 4 |
| `dialog.npc.trader.intro.0.line_4` | I just am always tied up in the biz, you know how it is aha... | Я вечно по уши в торговых делах, сам понимаешь, как это бывает, аха-ха... | Реплика 5 |
| `dialog.npc.trader.intro.0.line_5` | ...... | ...... | Реплика 6 |
| `dialog.npc.trader.intro.0.line_6` | Right right anyways, my name's Carlos! I only barter because some things are worth more than money can buy! | Так, о чём это я! Меня зовут Карлос! Я веду только бартерный обмен, ведь некоторые вещи стоят дороже любых денег! | Реплика 7 |

## 💬 Повседневный диалог (Chatter по уровням дружбы)

### 💖 Уровень дружбы 0 (friendship0) — 7 диалогов
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.trader.chatter_friendship0.0.line_0` | My stuff is top notch - just take a look! | Мой товар высшей пробы — только взгляни! | Диалог 1, строка 1 |
| `dialog.npc.trader.chatter_friendship0.1.line_0` | Premium wares! | Премиальные диковинки со всего света! | Диалог 2, строка 1 |
| `dialog.npc.trader.chatter_friendship0.2.line_0` | I bet you've never seen this stuff before! | Бьюсь об заклад, ты в жизни такого не видывал! | Диалог 3, строка 1 |
| `dialog.npc.trader.chatter_friendship0.3.line_0` | @i, was it? I've got lots of stock piled up just waiting for your purchase! | @i, верно? У меня накопилась гора первоклассного товара, только и ждёт твоих покупок! | Диалог 4, строка 1 |
| `dialog.npc.trader.chatter_friendship0.4.line_0` | No money no problem! Just show me what those grubby hands have gotten ahold of! | Нет звонкой монеты? Не беда! Покажи, какие сокровища завалялись в твоих карманах! | Диалог 5, строка 1 |
| `dialog.npc.trader.chatter_friendship0.5.line_0` | I've got stuff you won't get anywhere else! | У меня есть вещи, которые ты не сыщешь больше нигде в мире! | Диалог 6, строка 1 |
| `dialog.npc.trader.chatter_friendship0.6.line_0` | Let's make a deal! | Давай заключим сделку! | Диалог 7, строка 1 |

### 💖 Уровень дружбы 1 (friendship1) — 5 диалогов
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.trader.chatter_friendship1.0.line_0` | Always a pleasure doing business with you, @i. | Всегда приятно иметь с тобой дело, @i. | Диалог 1, строка 1 |
| `dialog.npc.trader.chatter_friendship1.1.line_0` | Gotta keep something in the pack at all times! | В сумке торговца всегда должно быть что-то новенькое! | Диалог 2, строка 1 |
| `dialog.npc.trader.chatter_friendship1.1.line_1` | What's a merchant without wares? | Что за купец без богатого ассортимента? | Диалог 2, строка 2 |
| `dialog.npc.trader.chatter_friendship1.2.line_0` | It feels good to be in a right proper town. You can never get a good meal on the road! | Как же приятно оказаться в настоящем, процветающем городке. В дороге никогда не удаётся толком поесть! | Диалог 3, строка 1 |
| `dialog.npc.trader.chatter_friendship1.3.line_0` | Hello hello @i! What can I help you with today? | Привет-привет, @i! Чем могу порадовать тебя сегодня? | Диалог 4, строка 1 |
| `dialog.npc.trader.chatter_friendship1.4.line_0` | You got any Truffle Tea? I'd really like to get my hands on some... | У тебя случайно нет трюфельного чая? Мне бы до смерти хотелось раздобыть парочку чашек... | Диалог 5, строка 1 |

### 💖 Уровень дружбы 2 (friendship2) — 5 диалогов
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.trader.chatter_friendship2.0.line_0` | Have you seen Ace around? I've got plenty o' rare saplings in my private stock! | Ты не видел Эйса поблизости? В моих тайных запасах как раз припасено несколько редких саженцев! | Диалог 1, строка 1 |
| `dialog.npc.trader.chatter_friendship2.1.line_0` | Caroline was cooking up something wonderful the other day, I could smell it from a mile away... | Кэролайн на днях готовила что-то неописуемое... Аромат разносился за целую милю! | Диалог 2, строка 1 |
| `dialog.npc.trader.chatter_friendship2.2.line_0` | Need anything special today? Or just the usual stock? | Ищешь что-то особенное сегодня? Или глянешь обычный ассортимент? | Диалог 3, строка 1 |
| `dialog.npc.trader.chatter_friendship2.3.line_0` | @i! What do I have the pleasure for today? | @i! Какая приятная встреча, чем обязан? | Диалог 4, строка 1 |
| `dialog.npc.trader.chatter_friendship2.4.line_0` | Veronica is a tough one, I really struggle with talking to the quieter ones... | Вероника — крепкий орешек... Мне всегда непросто находить общий язык с такими тихонями. | Диалог 5, строка 1 |

### 💖 Уровень дружбы 3 (friendship3) — 7 диалогов
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.trader.chatter_friendship3.1.line_0` | I have no idea how Aiden stays in business with all these handouts. | Ума не приложу, как Эйден умудряется оставаться на плаву, раздавая столько добра даром. | Диалог 2, строка 1 |
| `dialog.npc.trader.chatter_friendship3.1.line_1` | Keep people wanting! Or they'll never come back! | Покупателей нужно держать в лёгком голоде! Иначе они никогда не вернутся! | Диалог 2, строка 2 |
| `dialog.npc.trader.chatter_friendship3.2.line_0` | @i! Back at it again! | @i! Снова в деле! | Диалог 3, строка 1 |
| `dialog.npc.trader.chatter_friendship3.3.line_0` | I've heard a lot of stories, but nothing about Haruna's homeland, how strange. | Я слышал множество историй со всех концов света, но ни слова о родине Харуны... Как странно. | Диалог 4, строка 1 |
| `dialog.npc.trader.chatter_friendship3.4.line_0` | I always love chatting with Evelyne! When she's awake of course... | Обожаю болтать с Эвелин! Когда она не спит, разумеется... | Диалог 5, строка 1 |
| `dialog.npc.trader.chatter_friendship3.5.line_0` | Do NOT trade with those Gnomes!! | Ни в коем случае НЕ торгуй с этими гномами!! | Диалог 6, строка 1 |
| `dialog.npc.trader.chatter_friendship3.5.line_1` | Do they even understand how valuable silver is? What am I supposed to do with that stupid dust?? | Они вообще понимают, насколько ценно серебро? И что мне прикажете делать с этой дурацкой пылью?! | Диалог 6, строка 2 |
| `dialog.npc.trader.chatter_friendship3.6.line_0` | I was hanging out with Leon the other day, what an interesting person! | На днях я зависал с Леоном — до чего же занятный парень! | Диалог 7, строка 1 |
| `dialog.npc.trader.chatter_friendship3.6.line_1` | I wasn't expecting someone familiar with culture to this extent out in a village like this! | Не ожидал встретить в такой глухой деревеньке человека, столь глубоко разбирающегося в культуре! | Диалог 7, строка 2 |

### 💖 Уровень дружбы 4 (friendship4) — 7 диалогов
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.trader.chatter_friendship4.0.line_0` | I wonder why people find it so difficult to get along with Caroline. | Интересно, почему людям так трудно поладить с Кэролайн? | Диалог 1, строка 1 |
| `dialog.npc.trader.chatter_friendship4.1.line_0` | What do you do what do you know, it's @i! | Кого я вижу! Сам @i собственной персоной! | Диалог 2, строка 1 |
| `dialog.npc.trader.chatter_friendship4.2.line_0` | Very rarely do I get to actually explore the towns and cities I've stayed in... Usually I'm tied up in my shop! | Мне крайне редко удаётся по-настоящему погулять по городам, где я останавливаюсь... Обычно я привязан к своей лавке! | Диалог 3, строка 1 |
| `dialog.npc.trader.chatter_friendship4.3.line_0` | Witches are the best, they always ask for the most random things | Ведьмы — лучшие клиенты! Они вечно заказывают самые безумные вещи. | Диалог 4, строка 1 |
| `dialog.npc.trader.chatter_friendship4.3.line_1` | And who better to aquire said things than yours truely! | И кто справится с доставкой этих диковинок лучше меня? Да никто! | Диалог 4, строка 2 |
| `dialog.npc.trader.chatter_friendship4.4.line_0` | Sometimes I wake up in a cold sweat thinking about the time someone served me a plate of Hákarl. | Иногда я просыпаюсь в холодном поту при мысли о том, как однажды мне подали тарелку тухлой акулы хаукарль. | Диалог 5, строка 1 |
| `dialog.npc.trader.chatter_friendship4.4.line_1` | Wish I knew what that was before I hogged it down! | Жаль, я не знал, что это такое, до того как проглотил кусок целиком! | Диалог 5, строка 2 |
| `dialog.npc.trader.chatter_friendship4.5.line_0` | You know I've never actually met the person who makes all your machine upgrades. | Знаешь, я ведь ни разу не встречал лично того гения, который создаёт улучшения для твоих станков. | Диалог 6, строка 1 |
| `dialog.npc.trader.chatter_friendship4.5.line_1` | They've gone through like 4 different brokers by the time they end up on your farm! | Эти чертежи проходят через четверых посредников, прежде чем очутиться у тебя на ферме! | Диалог 6, строка 2 |
| `dialog.npc.trader.chatter_friendship4.6.line_0` | I bet a person like you would love the Camuy Caves! | Готов спорить, такому авантюристу, как ты, понравились бы пещеры Камуй! | Диалог 7, строка 1 |
| `dialog.npc.trader.chatter_friendship4.6.line_1` | You just gotta watch out for those stupid horrifying spiders around there. Really don't like those things... | Только берегись тех жутких громадных пауков. Терпеть не могу этих тварей... | Диалог 7, строка 2 |

### 💖 Уровень дружбы 5 (friendship5) — 6 диалогов
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.trader.chatter_friendship5.0.line_0` | Nobody around here dances which is a bit of a culture shock! I wonder if this is how Haruna constantly feels! | Здесь никто не танцует, для меня это настоящий культурный шок! Интересно, Харуна постоянно чувствует себя так же? | Диалог 1, строка 1 |
| `dialog.npc.trader.chatter_friendship5.1.line_0` | Watcha up to today @i? | Чем занят сегодня, @i? | Диалог 2, строка 1 |
| `dialog.npc.trader.chatter_friendship5.2.line_0` | @i @i @i! I've been looking forward to your next visit. | @i, @i, @i! Я с нетерпением ждал твоего очередного визита! | Диалог 3, строка 1 |
| `dialog.npc.trader.chatter_friendship5.3.line_0` | Do you want a drink? Or are you still working? You always work too hard! | Хочешь выпить чего-нибудь освежающего? Или всё ещё работаешь? Ты вечно трудишься не покладая рук! | Диалог 4, строка 1 |
| `dialog.npc.trader.chatter_friendship5.4.line_0` | Y'know, this place is a lot like home. | Знаешь, это место очень напоминает мне родной дом. | Диалог 5, строка 1 |
| `dialog.npc.trader.chatter_friendship5.4.line_1` | So much hustle and bustle... a guy could get comfortable. | Столько приятной суеты и движения... Тут запросто можно пустить корни. | Диалог 5, строка 2 |
| `dialog.npc.trader.chatter_friendship5.5.line_0` | Sometimes I feel like I should've collected these things myself. | Иногда мне кажется, что я должен был сам добывать все эти сокровища. | Диалог 6, строка 1 |
| `dialog.npc.trader.chatter_friendship5.5.line_1` | I've been around, but I've never been in any real danger, y'know? | Я много где побывал, но ни разу не попадал в настоящую переделку, понимаешь? | Диалог 6, строка 2 |
| `dialog.npc.trader.chatter_friendship5.5.line_2` | Oops, carried away again. Did you need anything? | Ой, опять я разболтался. Тебе что-нибудь нужно? | Диалог 6, строка 3 |

## 🎁 Реакция на подарки (Gift Responses)

### ❤️ Любимый подарок (Loved)
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.trader.gift_loved.0.line_0` | Now this is beautiful, I can already tell you used the freshest ingredients! | Какая редкость! Это украсит мою коллекцию заморских чудес, спасибо, @i! | Вариант 1 |
| `dialog.npc.trader.gift_loved.1.line_0` | I love someone that can eat, but I love someone that can cook more! | Я уважаю тех, кто любит поесть, но тех, кто умеет готовить — боготворю! | Вариант 2 |
| `dialog.npc.trader.gift_loved.2.line_0` | You're the best, @i, you know that? | Ты лучший друг на свете, @i, знаешь об этом? | Вариант 3 |
| `dialog.npc.trader.gift_loved.3.line_0` | * You notice the ravenous look on Carlos' face and hand the gift over * | * Вы замечаете голодный блеск в глазах Карлоса и передаёте подарок * | Вариант 4 |
| `dialog.npc.trader.gift_loved.3.line_1` | * There are no words, but the sheer speed of consuption says everything you need to know * | * Слова излишни: бешеная скорость, с которой он всё уплетает, говорит сама за себя * | Вариант 4 |
| `dialog.npc.trader.gift_loved.4.line_0` | I'm in awe. This is like... | Я просто в благоговении. Это же... | Вариант 5 |
| `dialog.npc.trader.gift_loved.4.line_1` | So totally righteous. | Просто потрясно! | Вариант 5 |

### 👍 Понравившийся подарок (Liked)
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.trader.gift_liked.0.line_0` | Oh, now THIS is something! | Благодарю за подарок! Такой товар всегда в цене. | Вариант 1 |
| `dialog.npc.trader.gift_liked.1.line_0` | You're a sweet one, aren't you? | А ты умеешь быть милым, правда? | Вариант 2 |
| `dialog.npc.trader.gift_liked.2.line_0` | This rocks! | Вот это вещь! Высший класс! | Вариант 3 |
| `dialog.npc.trader.gift_liked.3.line_0` | Thanks so much! | Огромное спасибо! | Вариант 4 |
| `dialog.npc.trader.gift_liked.4.line_0` | Aww yeah! Awesome! | О-о да! Красота! | Вариант 5 |

### 😐 Нейтральный подарок (Neutral)
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.trader.gift_neutral.0.line_0` | This is fresh, right? | Спасибо, сойдёт для обмена в пути. | Вариант 1 |
| `dialog.npc.trader.gift_neutral.1.line_0` | Not the worst I've gotten! | Бывало и похуже, сойдёт! | Вариант 2 |
| `dialog.npc.trader.gift_neutral.2.line_0` | I guess this isn't nothing. | Ну, по крайней мере, это лучше, чем ничего. | Вариант 3 |
| `dialog.npc.trader.gift_neutral.3.line_0` | Thanks for, uh... | Спасибо за... эм... | Вариант 4 |
| `dialog.npc.trader.gift_neutral.3.line_1` | This. | Вот это. | Вариант 4 |
| `dialog.npc.trader.gift_neutral.4.line_0` | Does this, uh... | А это... | Вариант 5 |
| `dialog.npc.trader.gift_neutral.4.line_1` | Will this fit in my pack? | Оно вообще влезет в мою сумку? | Вариант 5 |

### 👎 Не понравившийся подарок (Disliked)
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.trader.gift_disliked.0.line_0` | I mean... | Э-э... спасибо, наверное? | Вариант 1 |
| `dialog.npc.trader.gift_disliked.1.line_0` | This kinda stinks, bud. | Мне это и даром не нужно. | Вариант 2 |
| `dialog.npc.trader.gift_disliked.2.line_0` | This is pretty lame. Sorry. | Ну... спасибо за попытку. | Вариант 3 |
| `dialog.npc.trader.gift_disliked.3.line_0` | Oh. | Эм, я не смогу это никому продать. | Вариант 4 |
| `dialog.npc.trader.gift_disliked.3.line_1` | I kinda thought you knew me a bit better. | Эм... мне это не особо нужно, но всё равно спасибо. | Вариант 4 |
| `dialog.npc.trader.gift_disliked.4.line_0` | What am I supposed to do with this? | Не лучший твой выбор, друг мой. | Вариант 5 |

### 😡 Ненавистный подарок (Hated)
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.trader.gift_hated.0.line_0` | Am I that hard to please? | Оставь этот мусор себе, путник! | Вариант 1 |
| `dialog.npc.trader.gift_hated.1.line_0` | I mean, if you want me to go, I can go. | Убери этот мусор с моих глаз! | Вариант 2 |
| `dialog.npc.trader.gift_hated.2.line_0` | You're joshing me, right? Yanking my chain? | Ты пытаешься меня оскорбить этим хламом? | Вариант 3 |
| `dialog.npc.trader.gift_hated.3.line_0` | This is, uh... | Отвратительно. Больше не подходи ко мне с таким. | Вариант 4 |
| `dialog.npc.trader.gift_hated.3.line_1` | Well, I really hate this, actually. | Ужасно! Убери этот мусор от меня! | Вариант 4 |
| `dialog.npc.trader.gift_hated.4.line_0` | ... I don't have to be here. Nobody here does. Remember that. | Забери эту мерзость немедленно! | Вариант 5 |

## 🌟 Уникальные диалоги (Unique)
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.trader.unique_five_gift.line_0` | @i! @i @i! | О-о-о, мой дорогой @i! Взгляни, что у меня есть! | five_gift |
| `dialog.npc.trader.unique_five_gift.line_1` | I've done something amazing! Amazingly funny! Nobody's gonna believe it! | В знак нашей крепкой дружбы я открываю для тебя секретную линейку заморских нарядов и экипировки! | five_gift |
| `dialog.npc.trader.unique_five_gift.line_2` | I tracked down the supplier for some of the town's accessories, with my amazing talent for acquiring things of course! | Таких стильных одеяний ты не сыщешь даже в столичных бутиках! | five_gift |
| `dialog.npc.trader.unique_five_gift.line_3` | Of course I have to be true to my worth, even with someone I adore like you! | Носи с гордостью, мой лучший торговый партнёр! | five_gift |
| `dialog.npc.trader.unique_five_gift.line_4` | I have these up for barter if you want to 'steal everyone's look'! | И помни: для тебя у меня всегда самые эксклюзивные предложения! | five_gift |