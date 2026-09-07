# 📜 Диалоги NPC: Библиотекарь (Librarian)

**Роль:** Хранитель знаний, книг и свитков
**Характер и контекст:** Эрудированный, вдумчивый интеллектуал. Изучает историю долины, подземелий и древних артефактов.

> [!NOTE]
> - **Токен `@i`**: Обязательно сохраняйте `@i` на месте обращения к игроку по имени.
> - **Символ `%%`**: Все проценты должны экранироваться как `%%`.
> - **Колонка «Перевод (RU)»**: Заполняется русским текстом. Можно вносить любые правки формулировок и характера.

## 🏷️ Системные строки и имя
| ID ключа | Оригинал (EN) | Перевод (RU) | Примечание |
|---|---|---|---|
| `dialog.npc.librarian.name` | Veronica | Вероника | Имя персонажа |
| `dialog.npc.librarian.chatter.description` | Chatting with Veronica | Разговор с Вероникой | Статус диалогового окна |

## 🤝 Знакомство (Первая встреча / Intro)
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.librarian.intro.description` | Veronica's Introduction | Знакомство с Вероникой | Описание окна знакомства |
| `dialog.npc.librarian.intro.0.line_0` | Hello @i, my name is Veronica. I've been brought on here to help you get your storage in order. | Привет, @i! Меня зовут Вероника. Меня пригласили сюда, чтобы помочь тебе навести порядок в хранилищах и сундуках. | Реплика 1 |
| `dialog.npc.librarian.intro.0.line_1` | Caroline tells me that your homestead is a 'disgusting pile of unorganized rubbish'... | Кэролайн сказала мне, что твоя усадьба — это «отвратительная куча неорганизованного хлама»... | Реплика 2 |
| `dialog.npc.librarian.intro.0.line_2` | I feel like that was a slight exaggeration, but hopefully some of my cataloging supplies can help you out. | Мне кажется, она слегка сгустила краски, но, надеюсь, мои материалы для каталогизации тебе пригодятся. | Реплика 3 |
| `dialog.npc.librarian.intro.0.line_3` | I have a masters in library sciences, so I'm well versed in the various storage solutions. | У меня степень магистра библиотечных наук, так что я отлично разбираюсь в самых передовых системах хранения. | Реплика 4 |
| `dialog.npc.librarian.intro.0.line_4` | Please stop by the next time you get the chance. | Заглядывай в библиотеку, как только появится свободная минутка. | Реплика 5 |

## 💬 Повседневный диалог (Chatter по уровням дружбы)

### 💖 Уровень дружбы 0 (friendship0) — 5 диалогов
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.librarian.chatter_friendship0.0.line_0` | Hello @i, what can I get for you today? | Здравствуй, @i! Что я могу предложить тебе сегодня? | Диалог 1, строка 1 |
| `dialog.npc.librarian.chatter_friendship0.1.line_0` | Do you need some organizational supplies or books? | Тебе нужны принадлежности для сортировки или книги? | Диалог 2, строка 1 |
| `dialog.npc.librarian.chatter_friendship0.2.line_0` | Make sure to check in during the end of the season, I have some rare books for sale then. | Обязательно загляни ко мне в конце сезона — у меня появятся редкие сезонные книги на продажу. | Диалог 3, строка 1 |
| `dialog.npc.librarian.chatter_friendship0.3.line_0` | Welcome, what can I get you? | Добро пожаловать! Что тебе подобрать? | Диалог 4, строка 1 |
| `dialog.npc.librarian.chatter_friendship0.4.line_0` | How about that weather? | Как тебе сегодняшняя погода? | Диалог 5, строка 1 |
| `dialog.npc.librarian.chatter_friendship0.4.line_1` | ...Sorry I'm not good with small talk... | ...Прости, я совсем не сильна в пустой светской болтовне... | Диалог 5, строка 2 |

### 💖 Уровень дружбы 1 (friendship1) — 5 диалогов
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.librarian.chatter_friendship1.0.line_0` | Back again? Have you been doing some more farm expansion? | Снова ты? Расширяешь складские помещения на ферме? | Диалог 1, строка 1 |
| `dialog.npc.librarian.chatter_friendship1.1.line_0` | Are you going to buy something this time or just give me 'that look' when I show you the prices again? | Ты на этот раз собираешься что-то купить или опять будешь «так смотреть» на меня, когда я озвучу цены? | Диалог 2, строка 1 |
| `dialog.npc.librarian.chatter_friendship1.2.line_0` | You should know what I'm here for by now, please have a look. | К этому времени ты уже должен знать мой ассортимент, выбирай на здоровье. | Диалог 3, строка 1 |
| `dialog.npc.librarian.chatter_friendship1.3.line_0` | Evelyne was bragging to me about these magical drawers that teleport items between them... | Эвелин хвасталась мне какими-то магическими ящиками, которые телепортируют предметы... | Диалог 4, строка 1 |
| `dialog.npc.librarian.chatter_friendship1.3.line_1` | What a rude person. It's not like I can sell *every* type of box out there. | Какая грубиянка. Я же не могу держать в лавке *вообще все* мыслимые виды сундуков. | Диалог 4, строка 2 |
| `dialog.npc.librarian.chatter_friendship1.4.line_0` | Is your day going alright? It's been quiet out there. | Как проходит твой день? Вокруг так непривычно тихо. | Диалог 5, строка 1 |

### 💖 Уровень дружбы 2 (friendship2) — 5 диалогов
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.librarian.chatter_friendship2.0.line_0` | How has Aiden managed to break so many of my storage crates? Are ingots being placed in them hot or something? | Как Эйдену удаётся ломать столько моих ящиков для хранения? Он что, кладёт в них раскалённые слитки?! | Диалог 1, строка 1 |
| `dialog.npc.librarian.chatter_friendship2.1.line_0` | Have you seen a copy of Vōg Italia lying around anywhere? | Ты случайно не видел где-нибудь свежий номер «Vōg Italia»? | Диалог 2, строка 1 |
| `dialog.npc.librarian.chatter_friendship2.1.line_1` | I haven't had a chance to look at this season's collection yet... | У меня ещё не было времени взглянуть на модную коллекцию этого сезона... | Диалог 2, строка 2 |
| `dialog.npc.librarian.chatter_friendship2.2.line_0` | What can I do for you today @i? | Чем могу помочь тебе сегодня, @i? | Диалог 3, строка 1 |
| `dialog.npc.librarian.chatter_friendship2.3.line_0` | I'm getting food with Caroline soon so make it quick, I don't have much time. | Мы скоро идём обедать с Кэролайн, так что давай побыстрее, у меня мало времени. | Диалог 4, строка 1 |
| `dialog.npc.librarian.chatter_friendship2.4.line_0` | I have no idea how to talk to that Ace. | Ума не приложу, как вообще разговаривать с этим Эйсом. | Диалог 5, строка 1 |
| `dialog.npc.librarian.chatter_friendship2.4.line_1` | I've never met someone that talks so fast, it's frustrating. | Я ещё никогда не встречала людей, которые тараторят с такой скоростью. Это жутко утомляет. | Диалог 5, строка 2 |

### 💖 Уровень дружбы 3 (friendship3) — 5 диалогов
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.librarian.chatter_friendship3.0.line_0` | Some farmers prefer the more applied school of digital storage, though I find it overly complex. | Некоторые фермеры предпочитают прикладную школу цифровых хранилищ, хотя я нахожу её излишне громоздкой. | Диалог 1, строка 1 |
| `dialog.npc.librarian.chatter_friendship3.0.line_1` | Unfortunately, I only have enough room in my shop for the refined approach. | К сожалению, в моей лавке хватает места только для изысканного классического подхода. | Диалог 1, строка 2 |
| `dialog.npc.librarian.chatter_friendship3.1.line_0` | Don't forget to stop by every time I do the Book Fair! I can only stock so many books so some are seasonal! | Не забывай заглядывать на каждую Книжную Ярмарку! Количество книг ограничено, многие из них сезонные! | Диалог 2, строка 1 |
| `dialog.npc.librarian.chatter_friendship3.2.line_0` | Can you check in with Leon? I need that copy of 'Notebooks from Underneath' back, it's been weeks... | Можешь напомнить Леону? Мне нужно вернуть экземпляр «Записок из подполья», он держит его уже несколько недель... | Диалог 3, строка 1 |
| `dialog.npc.librarian.chatter_friendship3.3.line_0` | Ugh, this is the third nature field guide Ace has ruined this month! Annoying! | Ох, это уже третий полевой справочник по природе, который Эйс испортил за этот месяц! Невыносимо! | Диалог 4, строка 1 |
| `dialog.npc.librarian.chatter_friendship3.4.line_0` | How can I help you today? | Чем могу помочь тебе сегодня? | Диалог 5, строка 1 |

### 💖 Уровень дружбы 4 (friendship4) — 5 диалогов
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.librarian.chatter_friendship4.0.line_0` | Evelyne has to be the most unorganized person I have ever met. It's embarrassing. | Эвелин — самый неорганизованный и хаотичный человек, которого я знаю. Это просто позор какой-то. | Диалог 1, строка 1 |
| `dialog.npc.librarian.chatter_friendship4.1.line_0` | It breaks my heart that Caroline is so misunderstood... | У меня сердце кровью обливается от того, насколько превратно все понимают Кэролайн... | Диалог 2, строка 1 |
| `dialog.npc.librarian.chatter_friendship4.1.line_1` | Supporting towns like these require so much time, energy and resources to support. | Поддержка таких городков требует колоссального количества времени, сил и ресурсов. | Диалог 2, строка 2 |
| `dialog.npc.librarian.chatter_friendship4.1.line_2` | It's very thankless work, most people flame out of it. But not my Caroline! | Это крайне неблагодарный труд, большинство людей быстро выгорают. Но только не моя Кэролайн! | Диалог 2, строка 3 |
| `dialog.npc.librarian.chatter_friendship4.2.line_0` | Caroline doesn't like when people are unprofessional, so keep our little chats when I'm on the clock between you and I. | Кэролайн не любит непрофессионализм, так что пусть наши милые беседы в рабочее время останутся строго между нами. | Диалог 3, строка 1 |
| `dialog.npc.librarian.chatter_friendship4.3.line_0` | Hey @i, what can I get you? You can't possibly need more space, right? | Привет, @i! Что тебе предложить? Тебе ведь не может требоваться ЕЩЁ больше места, правда? | Диалог 4, строка 1 |
| `dialog.npc.librarian.chatter_friendship4.4.line_0` | Get some minisheep! They have the most beautifully shininig coats. Their wool makes some gorgeous sweaters... ♡ | Заведи мини-овечек! У них потрясающе шелковистая шерсть. Из неё получаются восхитительные свитера... ♡ | Диалог 5, строка 1 |
| `dialog.npc.librarian.chatter_friendship4.4.line_1` | Ah! Not that I'm an expert or anything! Ask Maria! | Ой! Не то чтобы я была экспертом в животноводстве! Спроси у Марии! | Диалог 5, строка 2 |

### 💖 Уровень дружбы 5 (friendship5) — 6 диалогов
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.librarian.chatter_friendship5.0.line_0` | The key to making beautiful nit fabrics to do it by hand, this is something you should understand intuitively being a farmer and all. | Секрет создания роскошных вязаных тканей — делать всё вручную. Ты как фермер должен понимать это интуитивно. | Диалог 1, строка 1 |
| `dialog.npc.librarian.chatter_friendship5.1.line_0` | Did you seen Iris von Harpten's latest collection?? | Ты видел последнюю коллекцию Ирис ван Херпен?! | Диалог 2, строка 1 |
| `dialog.npc.librarian.chatter_friendship5.1.line_1` | I have no idea how she manages to use those strange materials to create such beautiful shapes... ♡ | Понятия не имею, как ей удаётся использовать столь необычные материалы для создания таких божественных силуэтов... ♡ | Диалог 2, строка 2 |
| `dialog.npc.librarian.chatter_friendship5.2.line_0` | It's @i! I'm so happy to see you right now, Carolines been so busy this week and I need someone to talk to! | Кого я вижу — это же @i! Я так рада тебя видеть: Кэролайн на этой неделе безумно занята, а мне так нужно с кем-нибудь поговорить! | Диалог 3, строка 1 |
| `dialog.npc.librarian.chatter_friendship5.3.line_0` | I wonder where Carlos sends all those random items you give him... | Интересно, куда Карлос отправляет все те случайные вещи, что ты ему сгружаешь? | Диалог 4, строка 1 |
| `dialog.npc.librarian.chatter_friendship5.3.line_1` | He's always asking for more shipping materials. | Он постоянно выпрашивает у меня упаковочные материалы для посылок. | Диалог 4, строка 2 |
| `dialog.npc.librarian.chatter_friendship5.4.line_0` | Oh hey @i! What can I get you today? | О, привет, @i! Что я могу сделать для тебя сегодня? | Диалог 5, строка 1 |
| `dialog.npc.librarian.chatter_friendship5.5.line_0` | Fashion houses should never continue once their founding designers leave. | Модные дома должны закрываться в тот момент, когда их покидают дизайнеры-основатели. | Диалог 6, строка 1 |
| `dialog.npc.librarian.chatter_friendship5.5.line_1` | Yes I get that there are exceptions, but just look at Gaultiyay! It's become so gauche! | Да, бывают исключения, но взгляните на Готье после его ухода! Это стало настолько безвкусно! | Диалог 6, строка 2 |

## 🎁 Реакция на подарки (Gift Responses)

### ❤️ Любимый подарок (Loved)
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.librarian.gift_loved.0.line_0` | I should let you know that I'm supposed to file a report for gifts this sweet... ♡ | Я обязана предупредить, что по правилам должна составить служебный отчёт на столь роскошные подарки... ♡ | Вариант 1 |
| `dialog.npc.librarian.gift_loved.1.line_0` | Why would you show me a garment this beautiful, I could never get my hands on something like this... | Зачем ты показываешь мне столь прекрасный наряд? Я ведь никогда не смогу достать себе нечто подобное... | Вариант 2 |
| `dialog.npc.librarian.gift_loved.1.line_1` | ...? You're giving it to me? | ...? Ты отдаёшь это мне?! | Вариант 2 |
| `dialog.npc.librarian.gift_loved.1.line_2` | Thank you @i, I'll take perfect care of it, I have a spare garment bag and everything ♡ | Спасибо тебе, @i! Я буду беречь его как зеницу ока, у меня как раз есть чехол для одежды ♡ | Вариант 2 |
| `dialog.npc.librarian.gift_loved.2.line_0` | How did you get your hands on something like this!? | Как тебе удалось раздобыть такую вещь?! | Вариант 3 |
| `dialog.npc.librarian.gift_loved.2.line_1` | French seams like this are difficult to pull off on a garment of this size. | Французские швы такого качества невероятно сложно выполнить на изделии подобного кроя. | Вариант 3 |
| `dialog.npc.librarian.gift_loved.2.line_2` | It must have been made by someone who truly loves the craft ♡ | Это определённо создал мастер, всем сердцем влюблённый в своё ремесло ♡ | Вариант 3 |
| `dialog.npc.librarian.gift_loved.3.line_0` | The texture of this is incredible, Maria must have taught you how to raise sheep with such kindness ♡ | Текстура просто невероятная! Мария, должно быть, научила тебя ухаживать за овечками с огромной любовью ♡ | Вариант 4 |
| `dialog.npc.librarian.gift_loved.4.line_0` | What a wonderful gift, I can't wait to catalog this for my collection... ♡ | Какой восхитительный подарок! Не терпится внести его в каталог моей личной коллекции... ♡ | Вариант 5 |

### 👍 Понравившийся подарок (Liked)
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.librarian.gift_liked.0.line_0` | Thank you @i, I appreciate the kindness. | Спасибо, @i, я очень ценю твою доброту. | Вариант 1 |
| `dialog.npc.librarian.gift_liked.1.line_0` | Thanks for the gift, small things like this go a long way. | Спасибо за подарок! Такие милые мелочи очень скрашивают дни. | Вариант 2 |
| `dialog.npc.librarian.gift_liked.2.line_0` | Oh! It's not so often I receive gifts, thank you. | О! Мне не так уж часто дарят подарки, большое спасибо. | Вариант 3 |
| `dialog.npc.librarian.gift_liked.3.line_0` | Do you need a special container for this? It seems nice. | Тебе нужен особый контейнер для этого? Выглядит симпатично. | Вариант 4 |
| `dialog.npc.librarian.gift_liked.3.line_1` | Oh this is for me? Thank you @i. | Оу, это мне? Спасибо тебе, @i. | Вариант 4 |
| `dialog.npc.librarian.gift_liked.4.line_0` | Thank you for the gift, I know someone who'd love something like this. | Благодарю за подарок, я знаю того, кто будет в восторге от этой вещи. | Вариант 5 |

### 😐 Нейтральный подарок (Neutral)
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.librarian.gift_neutral.0.line_0` | Hmmm? Oh you can put that over in section E6. | Хм-м-м? А, можешь положить это в секцию E6. | Вариант 1 |
| `dialog.npc.librarian.gift_neutral.1.line_0` | I'll take care of this for you @i, when do you want it back? | Я пока придержу это у себя, @i. Когда захочешь забрать обратно? | Вариант 2 |
| `dialog.npc.librarian.gift_neutral.2.line_0` | Gift? Why do I need a gift? | Подарок? С какой стати мне нужен подарок? | Вариант 3 |
| `dialog.npc.librarian.gift_neutral.3.line_0` | I don't really do deliveries, that seems like Ace's type of thing. | Я вообще-то не занимаюсь доставкой, это больше по части Эйса. | Вариант 4 |
| `dialog.npc.librarian.gift_neutral.3.line_1` | Oh, it's a gift. Thanks. | А, это подарок мне? Ну, спасибо. | Вариант 4 |
| `dialog.npc.librarian.gift_neutral.4.line_0` | Put that one on the pile back there please. | Положи это в ту стопку на задней полке, пожалуйста. | Вариант 5 |

### 👎 Не понравившийся подарок (Disliked)
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.librarian.gift_disliked.0.line_0` | I don't really want this. | Мне это совершенно ни к чему. | Вариант 1 |
| `dialog.npc.librarian.gift_disliked.1.line_0` | I'm not a fan of things like this. | Я не поклонница подобных вещей. | Вариант 2 |
| `dialog.npc.librarian.gift_disliked.2.line_0` | Did you mean to give this to someone else? I don't understand... | Ты случайно не перепутал адресата? Я не совсем понимаю... | Вариант 3 |
| `dialog.npc.librarian.gift_disliked.3.line_0` | Can you give that to someone else? I don't really like it. | Можешь отдать это кому-нибудь другому? Мне это не нравится. | Вариант 4 |
| `dialog.npc.librarian.gift_disliked.4.line_0` | I don't really have a need for this. | У меня нет никакой потребности в этой вещи. | Вариант 5 |

### 😡 Ненавистный подарок (Hated)
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.librarian.gift_hated.0.line_0` | Don't come to me for advice on how to store your disgusting garbage. | Не приходи ко мне за советами, как сортировать твой омерзительный мусор. | Вариант 1 |
| `dialog.npc.librarian.gift_hated.1.line_0` | What have I done to deserve your ire? | Чем я заслужила такую неприкрытую неприязнь с твоей стороны? | Вариант 2 |
| `dialog.npc.librarian.gift_hated.2.line_0` | I should let you know that I have to file a report for things like this. | Должна предупредить: я обязана подать рапорт о подобных выходках. | Вариант 3 |
| `dialog.npc.librarian.gift_hated.2.line_1` | I'll let Caroline deal with you, please leave. | Пусть Кэролайн разберётся с тобой. Пожалуйста, уйди. | Вариант 3 |
| `dialog.npc.librarian.gift_hated.3.line_0` | This is disgusting. | Это отвратительно. | Вариант 4 |
| `dialog.npc.librarian.gift_hated.4.line_0` | If Aiden knew you gave people things like this, it would break his heart. | Если бы Эйден узнал, что ты преподносишь людям ТАКОЕ, это разбило бы ему сердце. | Вариант 5 |

## 🌟 Уникальные диалоги (Unique)
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.librarian.unique_five_gift.line_0` | Hey @i! I've got an idea on how to earn Caroline's respect! | Привет, @i! У меня родилась отличная идея, как заслужить искреннее уважение Кэролайн! | five_gift |
| `dialog.npc.librarian.unique_five_gift.line_1` | As you've probably figured out right now, she's insatiable when it comes to your role in this little town. | Как ты наверняка уже понял, её аппетиты в отношении развития нашего городка просто ненасытны. | five_gift |
| `dialog.npc.librarian.unique_five_gift.line_2` | It doesn't matter how much your farm makes, it will never be enough! Everyone around here relies on the economic activity of your farm after all. | Неважно, сколько производит твоя ферма — ей всегда будет мало! Ведь всё здешнее благополучие держится на твоей экономической активности. | five_gift |
| `dialog.npc.librarian.unique_five_gift.line_3` | That said, being knowledgeable about your financial history will give her at least a little more peace of mind. | Она заставила меня разобрать архивы старых долговых пещер... Прочти эту рукопись — там описаны древние механизмы расширения влияния! | five_gift |
| `dialog.npc.librarian.unique_five_gift.line_4` | It would be a shame if my two best friends didn't get along, so please read it when you get the chance ♡ | Чтение вдохновляет разум и открывает новые горизонты познания. | five_gift |
| `dialog.npc.librarian.unique_five_gift_read.line_0` | Hey @i! I've got another idea on how to earn Caroline's respect! | Ты уже изучил рукопись долговых пещер, @i? Потрясающе! | five_gift_read |
| `dialog.npc.librarian.unique_five_gift_read.line_1` | As you've probably figured out right now, she's insatiable when it comes to your role in this little town. | Держи в награду амулет Дивы и кольцо маны Botania — они помогут тебе манипулировать энергией и предметами! | five_gift_read |
| `dialog.npc.librarian.unique_five_gift_read.line_2` | It doesn't matter how much your farm makes, it will never be enough! Everyone around here relies on the economic activity of your farm after all. | Кэролайн будет в восторге от твоих новых возможностей! | five_gift_read |
| `dialog.npc.librarian.unique_five_gift_read.line_3` | That said, not having to worry about you passing out in the Skull Cavern should give her a little more peace of mind. | В тишине библиотеки сокрыта мудрость веков. Берегите переплёты! | five_gift_read |
| `dialog.npc.librarian.unique_five_gift_read.line_4` | It would be a shame if my two best friends didn't get along, so please make sure to wear these while you're down there ♡ | В тишине библиотеки сокрыта мудрость веков. Берегите переплёты! | five_gift_read |
| `dialog.npc.librarian.unique_book_fair.line_0` | I have a selection of special books available for the book fair this season, please take a look. | Книги — это мосты между эпохами. На книжной ярмарке собраны редчайшие труды. | book_fair |

## 🔀 Диалоги с выбором (Choice Dialogs)
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.librarian.dialog.book_fair.line_0` | I have a selection of special books available for the book fair this season, please take a look. | В этом сезоне на книжной ярмарке представлен особый выбор книг, взгляните пожалуйста. | book_fair |
| `dialog.npc.librarian.dialog.book_fair.option_0` | Purchase supplies | Купить материалы | Кнопка выбора: book_fair |
| `dialog.npc.librarian.dialog.book_fair.option_1` | Shop at the Book Fair | Посетить книжную ярмарку | Кнопка выбора: book_fair |