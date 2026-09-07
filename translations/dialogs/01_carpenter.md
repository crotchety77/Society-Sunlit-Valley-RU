# 📜 Диалоги NPC: Эйс (Ace the Carpenter)

**Роль:** Плотник и строитель фермы / городка
**Характер и контекст:** Добродушный, активный, любит природу, собирательство ягод и трав в диких лесах, честный труженик. Дружит с кузнецом Эйденом и Кэролайн. Обращается к игроку на «ты» (@i).

> [!NOTE]
> - **Токен `@i`**: Обязательно сохраняйте `@i` на месте обращения к игроку по имени.
> - **Символ `%%`**: Все проценты должны экранироваться как `%%`.
> - **Колонка «Перевод (RU)»**: Заполняется русским текстом. Можно вносить любые правки формулировок и характера.

## 🏷️ Системные строки и имя
| ID ключа | Оригинал (EN) | Перевод (RU) | Примечание |
|---|---|---|---|
| `dialog.npc.carpenter.name` | Ace | Эйс | Имя персонажа |
| `dialog.npc.carpenter.chatter.description` | Chatting with Ace | Разговор с Эйсом | Статус диалогового окна |
| `dialog.npc.carpenter.purchase_supplies` | Purchase supplies | Купить материалы | Кнопка магазина |
| `dialog.npc.carpenter.invite_villagers` | Invite Villagers | Пригласить жителей | Кнопка магазина |
| `dialog.npc.carpenter.build_farm` | Build Farm buildings | Фермерские постройки | Кнопка магазина |
| `dialog.npc.carpenter.build_village` | Build Village buildings | Городские постройки | Кнопка магазина |

## 🤝 Знакомство (Первая встреча / Intro)
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.carpenter.intro.description` | Ace's Introduction | Знакомство с Эйсом | Описание окна знакомства |
| `dialog.npc.carpenter.intro.0.line_0` | Hey stranger, my name is Ace. I'm here to help you build the village you're starting in Sunlit Valley. | Привет, путник! Меня зовут Эйс. Я здесь, чтобы помочь тебе построить поселение в Солнечной Долине. | Реплика 1 |
| `dialog.npc.carpenter.intro.0.line_1` | If you're looking to invite more villagers, come talk to me and I can help you build homes for them. | Если захочешь пригласить новых жителей, заглядывай ко мне — я помогу построить для них уютные дома. | Реплика 2 |
| `dialog.npc.carpenter.intro.0.line_2` | If you'd prefer to do the building yourself, just let me know and I can sell any building supplies you'll need. | А если предпочитаешь строить сам, только скажи — у меня найдётся запас любых стройматериалов. | Реплика 3 |
| `dialog.npc.carpenter.intro.0.line_3` | You really have your work cut out for you here, come see me if you need anything! | Работы предстоит непочатый край! Приходи, если что-то понадобится! | Реплика 4 |

## 💬 Повседневный диалог (Chatter по уровням дружбы)

### 💖 Уровень дружбы 0 (friendship0) — 11 диалогов
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.carpenter.chatter_friendship0.0.line_0` | What can I help you with today @i? | Чем я могу помочь тебе сегодня, @i? | Диалог 1, строка 1 |
| `dialog.npc.carpenter.chatter_friendship0.1.line_0` | Need any building supplies @i? | Нужны стройматериалы, @i? | Диалог 2, строка 1 |
| `dialog.npc.carpenter.chatter_friendship0.2.line_0` | The blueprints I've made in my building shop come with all the building blocks you'll need pre-supplied! | В чертежи из моего магазина уже включены все необходимые блоки! | Диалог 3, строка 1 |
| `dialog.npc.carpenter.chatter_friendship0.2.line_1` | No need to run around crafting everything for a building, I gotcha covered! | Не придётся бегать и крафтить всё вручную для каждой постройки — я обо всём позаботился! | Диалог 3, строка 2 |
| `dialog.npc.carpenter.chatter_friendship0.3.line_0` | The wild berries scattered around are such a good field snack! | Дикие ягоды в лесу — отличный перекус во время работы на свежем воздухе! | Диалог 4, строка 1 |
| `dialog.npc.carpenter.chatter_friendship0.4.line_0` | Don't discount wild plants like nettle, you can use them to make some tasty tea! | Не сбрасывай со счетов дикие травы вроде крапивы — из них получается отличный ароматный чай! | Диалог 5, строка 1 |
| `dialog.npc.carpenter.chatter_friendship0.5.line_0` | Nature is full of valuable and useful plants if you know what you're looking for. | Природа полна полезных растений, если знать, где и что искать. | Диалог 6, строка 1 |
| `dialog.npc.carpenter.chatter_friendship0.6.line_0` | I'll always try to make sure I'm around when you need me! | Я всегда стараюсь быть рядом, когда тебе нужна помощь со стройкой! | Диалог 7, строка 1 |
| `dialog.npc.carpenter.chatter_friendship0.7.line_0` | If you can't find any tree you're looking for in the wild, I have some saplings in my supply shop! | Если не можешь найти нужное дерево в дикой природе, у меня в лавке есть саженцы! | Диалог 8, строка 1 |
| `dialog.npc.carpenter.chatter_friendship0.8.line_0` | Be sure to check in occasionally, I may have some more invitations for other villagers stocked. | Заглядывай ко мне время от времени — у меня могут появиться новые приглашения для жителей. | Диалог 9, строка 1 |
| `dialog.npc.carpenter.chatter_friendship0.9.line_0` | Hey @i, have you managed to find your footing yet? | Эй, @i, как успехи? Уже освоился на новом месте? | Диалог 10, строка 1 |
| `dialog.npc.carpenter.chatter_friendship0.10.line_0` | Have you gotten a good handle on farming yet? Inviting someone to manage the market will let you get some new seeds. | Уже разобрался с фермерством? Если пригласить кого-нибудь управлять рынком, сможешь покупать новые семена. | Диалог 11, строка 1 |

### 💖 Уровень дружбы 1 (friendship1) — 10 диалогов
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.carpenter.chatter_friendship1.0.line_0` | If you manage to find any earth crystals in the mines, be sure to make some tappers. | Если найдёшь кристаллы земли в шахтах, обязательно сделай подсочники для деревьев. | Диалог 1, строка 1 |
| `dialog.npc.carpenter.chatter_friendship1.0.line_1` | You can get some valuable liquids from tapping different logs. | С разных пород древесины с их помощью можно собирать ценные смолы и соки. | Диалог 1, строка 2 |
| `dialog.npc.carpenter.chatter_friendship1.1.line_0` | I came across a rotted and overgrown farmhouse while exploring the other day... | На днях во время прогулки я наткнулся на полуразрушенный и заросший фермерский дом... | Диалог 2, строка 1 |
| `dialog.npc.carpenter.chatter_friendship1.1.line_1` | I wonder why the farmer abandoned it. | Интересно, почему прежний фермер бросил его? | Диалог 2, строка 2 |
| `dialog.npc.carpenter.chatter_friendship1.2.line_0` | My building shop has plenty of blueprints for your farm to choose from. | В моём магазине чертежей полно вариантов построек для твоей фермы. | Диалог 3, строка 1 |
| `dialog.npc.carpenter.chatter_friendship1.2.line_1` | I just need a few basic supplies to be able to build them. | Мне потребуется лишь немного базовых материалов, чтобы возвести их. | Диалог 3, строка 2 |
| `dialog.npc.carpenter.chatter_friendship1.3.line_0` | What can I help you with today @i? | Чем могу помочь сегодня, @i? | Диалог 4, строка 1 |
| `dialog.npc.carpenter.chatter_friendship1.3.line_1` | What a beautiful day it is today. | Какой же сегодня чудесный денёк! | Диалог 4, строка 2 |
| `dialog.npc.carpenter.chatter_friendship1.4.line_0` | Potatoes are some of the only crops that can grow in the wild! I try to dig around for them when I can. | Картофель — одна из немногих культур, растущих в дикой природе! Я стараюсь выкапывать его при любой возможности. | Диалог 5, строка 1 |
| `dialog.npc.carpenter.chatter_friendship1.5.line_0` | It's worth spending some time to upgrade your farm's infrastructure. | Стоит потратить время на улучшение инфраструктуры фермы. | Диалог 6, строка 1 |
| `dialog.npc.carpenter.chatter_friendship1.5.line_1` | You can use a charting map to link together your paths to travel faster! | Ты можешь использовать картографическую карту, чтобы соединить дорожки и перемещаться быстрее! | Диалог 6, строка 2 |
| `dialog.npc.carpenter.chatter_friendship1.6.line_0` | I never leave my cabin without a potion of recall, being lost in the wild can be dangerous. | Я никогда не выхожу из дома без зелья возврата — заблудиться в глуши может быть опасно. | Диалог 7, строка 1 |
| `dialog.npc.carpenter.chatter_friendship1.7.line_0` | Make sure to prepare a bit before mining, I looked inside of a cave earlier and found some dangerous looking monsters. | Обязательно подготовься перед походом в шахту: недавно я заглянул в пещеру и встретил там опасных тварей. | Диалог 8, строка 1 |
| `dialog.npc.carpenter.chatter_friendship1.8.line_0` | What are you up to today? | Чем планируешь заняться сегодня? | Диалог 9, строка 1 |
| `dialog.npc.carpenter.chatter_friendship1.9.line_0` | Ahhh hey @i, I can't chat much right now. I'm preparing for a big hike soon! | А-а, привет, @i! Не могу долго болтать — собираюсь в большой поход в горы! | Диалог 10, строка 1 |

### 💖 Уровень дружбы 2 (friendship2) — 13 диалогов
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.carpenter.chatter_friendship2.0.line_0` | How's your farm going @i? | Как продвигаются дела на ферме, @i? | Диалог 1, строка 1 |
| `dialog.npc.carpenter.chatter_friendship2.1.line_0` | Ahhhh I finally feel settled into this new town, I can finally relax a bit. | Фух, наконец-то я обжился на новом месте. Можно немного и перевести дух. | Диалог 2, строка 1 |
| `dialog.npc.carpenter.chatter_friendship2.2.line_0` | Need anything built today? | Нужно что-нибудь построить сегодня? | Диалог 3, строка 1 |
| `dialog.npc.carpenter.chatter_friendship2.3.line_0` | Technically you don't have to buy one of my barns, but animals really dislike being out in the rain. | Строго говоря, ты не обязан покупать у меня хлев, но животные очень не любят мокнуть под дождём. | Диалог 4, строка 1 |
| `dialog.npc.carpenter.chatter_friendship2.4.line_0` | A good shed will keep all your artisan machines organized | Добротный сарай поможет держать все ремесленные станки в идеальном порядке. | Диалог 5, строка 1 |
| `dialog.npc.carpenter.chatter_friendship2.5.line_0` | All this open land to survey, I really end up exhausted by the end of every day. | Столько открытых земель нужно обойти и разметить... К концу дня я просто валюсь с ног от усталости. | Диалог 6, строка 1 |
| `dialog.npc.carpenter.chatter_friendship2.6.line_0` | Hey @i! What do you need today? | Привет, @i! Что тебе нужно сегодня? | Диалог 7, строка 1 |
| `dialog.npc.carpenter.chatter_friendship2.7.line_0` | Have you gotten to know Leon yet? You should really try to get to know everyone! | Ты уже познакомился с Леоном? Тебе стоит получше узнать всех в городке! | Диалог 8, строка 1 |
| `dialog.npc.carpenter.chatter_friendship2.7.line_1` | And I do mean everyone... | И я имею в виду абсолютно всех... | Диалог 8, строка 2 |
| `dialog.npc.carpenter.chatter_friendship2.8.line_0` | Make sure you're talking to everyone that you've invited to this town. | Не забывай общаться со всеми, кого приглашаешь в этот город. | Диалог 9, строка 1 |
| `dialog.npc.carpenter.chatter_friendship2.8.line_1` | It can be a little lonely to move all the way from your home to help with a settlement like this one. | Бросить родной дом и переехать в глухое поселение бывает довольно одиноко. | Диалог 9, строка 2 |
| `dialog.npc.carpenter.chatter_friendship2.9.line_0` | You should ask Maria about getting a pet squirrel! They can forage for nuts and wild berries. | Расспроси Марию о ручной белке! Они умеют собирать орехи и дикие ягоды. | Диалог 10, строка 1 |
| `dialog.npc.carpenter.chatter_friendship2.9.line_1` | I suppose they're kinda like me, in a way! | Пожалуй, мы с ними в чём-то похожи! | Диалог 10, строка 2 |
| `dialog.npc.carpenter.chatter_friendship2.10.line_0` | Don't get the wrong idea about me, I'm terrible at managing logistics! | Только не подумай лишнего — логист из меня просто никудышный! | Диалог 11, строка 1 |
| `dialog.npc.carpenter.chatter_friendship2.10.line_1` | Caroline really did all the heavy lifting when getting this town started. | Кэролайн взяла на себя всю самую сложную организационную работу при основании городка. | Диалог 11, строка 2 |
| `dialog.npc.carpenter.chatter_friendship2.11.line_0` | I love the calmness of being out in the wild and foraging for food. | Обожаю тишину дикой природы и сбор лесных даров. | Диалог 12, строка 1 |
| `dialog.npc.carpenter.chatter_friendship2.11.line_1` | If you stop and listen you can hear the little patters of wild animals. | Если замереть и прислушаться, можно услышать мягкие шаги лесных зверьков. | Диалог 12, строка 2 |
| `dialog.npc.carpenter.chatter_friendship2.12.line_0` | It's good to save at least one of every flower you find out in the wild. | Советую сохранять хотя бы по одному цветку каждого вида, найденного в природе. | Диалог 13, строка 1 |
| `dialog.npc.carpenter.chatter_friendship2.12.line_1` | They seem to grow wildly with a little bonemeal, unlike crops and saplings. | Они отлично размножаются от костной муки, в отличие от злаков и деревьев. | Диалог 13, строка 2 |
| `dialog.npc.carpenter.chatter_friendship2.12.line_2` | Plus Aiden really loves flowers, especially some of the rare ones I find! | К тому же Эйден просто обожает цветы, особенно редкие! | Диалог 13, строка 3 |

### 💖 Уровень дружбы 3 (friendship3) — 9 диалогов
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.carpenter.chatter_friendship3.0.line_0` | What can I get you @i? | Что для тебя сделать, @i? | Диалог 1, строка 1 |
| `dialog.npc.carpenter.chatter_friendship3.1.line_0` | Hey @i, how's it going? | Привет, @i! Как жизнь? | Диалог 2, строка 1 |
| `dialog.npc.carpenter.chatter_friendship3.2.line_0` | Grow any new crops this season @i? | Вырастил что-нибудь новенькое в этом сезоне, @i? | Диалог 3, строка 1 |
| `dialog.npc.carpenter.chatter_friendship3.3.line_0` | Caroline is the only other person that knows where Haruna is from. | Кэролайн — единственный человек, который знает, откуда родом Харуна. | Диалог 4, строка 1 |
| `dialog.npc.carpenter.chatter_friendship3.3.line_1` | I wonder why it's so secretive... But it's probably better to not pry about these things. | Интересно, почему вокруг этого столько тайн... Но, наверное, лучше не лезть не в своё дело. | Диалог 4, строка 2 |
| `dialog.npc.carpenter.chatter_friendship3.4.line_0` | Ahhhh @i, would you like to join me? I'm working on carving some wainscotting. | А-а, @i, не хочешь составить мне компанию? Я как раз вырезаю деревянные панели. | Диалог 5, строка 1 |
| `dialog.npc.carpenter.chatter_friendship3.5.line_0` | Haruna tried teaching me to fish the other day. The only thing I managed to hook was her hairband... | На днях Харуна пыталась научить меня рыбачить. Единственное, что я умудрился поймать на крючок — это её заколку для волос... | Диалог 6, строка 1 |
| `dialog.npc.carpenter.chatter_friendship3.6.line_0` | I always look forward to mossberry season. Nothing like chopping away at a try and seeing a juicy green fruit drop from a branch! | Всегда с нетерпением жду сезона моховых ягод. Нет ничего лучше, чем рубить дерево и увидеть, как с ветки падает сочный зелёный плод! | Диалог 7, строка 1 |
| `dialog.npc.carpenter.chatter_friendship3.7.line_0` | Trees are pretty hearty and can grow in most seasons. Though spruce in particular seems to really dislike summer I've found. | Деревья очень выносливы и растут почти в любой сезон. Хотя ели, как я заметил, терпеть не могут летнюю жару. | Диалог 8, строка 1 |
| `dialog.npc.carpenter.chatter_friendship3.8.line_0` | You should see if you can make a catching net! | Тебе стоит смастерить сачок для насекомых! | Диалог 9, строка 1 |
| `dialog.npc.carpenter.chatter_friendship3.8.line_1` | I've found tons of butterflies and moths just exploring. | Во время походов я встречал кучу редких бабочек и мотыльков. | Диалог 9, строка 2 |

### 💖 Уровень дружбы 4 (friendship4) — 9 диалогов
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.carpenter.chatter_friendship4.0.line_0` | Hey @i, how's your farm developing? | Эй, @i, как развивается твоя ферма? | Диалог 1, строка 1 |
| `dialog.npc.carpenter.chatter_friendship4.1.line_0` | How's it going? | Как дела? | Диалог 2, строка 1 |
| `dialog.npc.carpenter.chatter_friendship4.2.line_0` | Sorry I can't chat, I'm a bit behind on my resource collection this week. | Прости, не могу поболтать — я немного отстаю от плана по заготовке древесины на этой неделе. | Диалог 3, строка 1 |
| `dialog.npc.carpenter.chatter_friendship4.3.line_0` | Caroline has me working on furniture this week! It's a shame these are all designated as exports to other colonies. | Кэролайн поручила мне изготовление мебели! Жаль только, что всё это пойдёт на экспорт в другие колонии. | Диалог 4, строка 1 |
| `dialog.npc.carpenter.chatter_friendship4.4.line_0` | Haruna's smoked salmon is something else, it's perfect for long days in the wild! | Копчёный лосось от Харуны — это нечто невероятное! Идеальный перекус для долгих походов по лесу. | Диалог 5, строка 1 |
| `dialog.npc.carpenter.chatter_friendship4.5.line_0` | I still haven't figured out what's up with those birts... I should ask Maria. | Я до сих пор не понял, что это за странные птицы... Надо будет расспросить Марию. | Диалог 6, строка 1 |
| `dialog.npc.carpenter.chatter_friendship4.6.line_0` | Dehydrated fruits make great travel food. The market has a dehydrator for sale if you're interested. | Сушёные фрукты — отличная еда для путешествий. На рынке как раз продаётся дегидратор, если тебе интересно. | Диалог 7, строка 1 |
| `dialog.npc.carpenter.chatter_friendship4.7.line_0` | Leon gave me some samples of this season's produce! You can really taste the freshness from your farm. | Леон угостил меня образцами урожая этого сезона! Твои фермерские продукты просто пышут свежестью. | Диалог 8, строка 1 |
| `dialog.npc.carpenter.chatter_friendship4.8.line_0` | Seems like Aiden sharpened my axe when I wasn't looking, what a kind soul. | Похоже, Эйден наточил мой топор, пока я не видел. Какая же добрая душа! | Диалог 9, строка 1 |

### 💖 Уровень дружбы 5 (friendship5) — 15 диалогов
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.carpenter.chatter_friendship5.0.line_0` | I really appreciate what Caroline's done for the town. | Я искренне ценю всё, что Кэролайн сделала для этого городка. | Диалог 1, строка 1 |
| `dialog.npc.carpenter.chatter_friendship5.0.line_1` | Most people aren't aware of it from the outside, but she's done so much for everyone | Со стороны это не всегда заметно, но она вложила душу и колоссальный труд ради каждого из нас. | Диалог 1, строка 2 |
| `dialog.npc.carpenter.chatter_friendship5.1.line_0` | I wonder if there's a way we can get Haruna home... | Интересно, сможем ли мы когда-нибудь помочь Харуне вернуться на родину... | Диалог 2, строка 1 |
| `dialog.npc.carpenter.chatter_friendship5.1.line_1` | At least for a visit. I'd hate to see Haruna gone forever. | Хотя бы ненадолго повидаться. Не хотелось бы, чтобы она навсегда потеряла связь с домом. | Диалог 2, строка 2 |
| `dialog.npc.carpenter.chatter_friendship5.2.line_0` | On my last expedition I found some wild penguins! I should get some for Maria. | В прошлой экспедиции я встретил диких пингвинов! Надо обязательно поймать парочку для Марии. | Диалог 3, строка 1 |
| `dialog.npc.carpenter.chatter_friendship5.3.line_0` | How's your farm coming along? | Как успехи на ферме? | Диалог 4, строка 1 |
| `dialog.npc.carpenter.chatter_friendship5.4.line_0` | Make sure you have the right equipment before diving into the Skull Cavern. | Обязательно снарядись как следует перед спуском в Пещеру Черепа. | Диалог 5, строка 1 |
| `dialog.npc.carpenter.chatter_friendship5.4.line_1` | Wouldn't want anything to happen to you. | Не хочу, чтобы с тобой что-нибудь случилось. | Диалог 5, строка 2 |
| `dialog.npc.carpenter.chatter_friendship5.5.line_0` | Hope your day's going smoothly @i! | Надеюсь, твой день проходит удачно, @i! | Диалог 6, строка 1 |
| `dialog.npc.carpenter.chatter_friendship5.6.line_0` | I'm really happy with what we've managed to build here, @i. | Я по-настоящему счастлив тому, что нам удалось здесь построить, @i. | Диалог 7, строка 1 |
| `dialog.npc.carpenter.chatter_friendship5.7.line_0` | Mushroom logs are a great way to make money from planting trees, you should have some on your farm! | Грибные брёвна — отличный способ заработать на посадке деревьев, тебе обязательно стоит разместить их у себя на ферме! | Диалог 8, строка 1 |
| `dialog.npc.carpenter.chatter_friendship5.8.line_0` | Mystic willows are so pretty, I wonder if Caroline knows where to find the saplings. | Мистические ивы такие красивые... Интересно, знает ли Кэролайн, где достать их саженцы? | Диалог 9, строка 1 |
| `dialog.npc.carpenter.chatter_friendship5.9.line_0` | Grow any new crops this season @i? | Вырастил что-нибудь новенькое в этом сезоне, @i? | Диалог 10, строка 1 |
| `dialog.npc.carpenter.chatter_friendship5.10.line_0` | How have you been @i? | Как поживаешь, @i? | Диалог 11, строка 1 |
| `dialog.npc.carpenter.chatter_friendship5.11.line_0` | I'm sure dealing with seasons has been a burden on your farm. I can build you a greenhouse or two if you need! | Смена времён года наверняка доставляет хлопот твоей ферме. Я могу построить для тебя теплицу-другую, если нужно! | Диалог 12, строка 1 |
| `dialog.npc.carpenter.chatter_friendship5.11.line_1` | Just need some of that greenhouse glass first. | Только сначала достань немного тепличного стекла. | Диалог 12, строка 2 |
| `dialog.npc.carpenter.chatter_friendship5.12.line_0` | Leon is a sucker for red wine, so glad I kept some wild berries around to make some. | Леон просто без ума от красного вина, как же здорово, что я запас диких ягод для его приготовления. | Диалог 13, строка 1 |
| `dialog.npc.carpenter.chatter_friendship5.13.line_0` | I don't know how Aiden manages to make all this industrial iron for some of my buildings. | Ума не приложу, как Эйдену удаётся ковать столько промышленного железа для моих построек. | Диалог 14, строка 1 |
| `dialog.npc.carpenter.chatter_friendship5.14.line_0` | What can I get you @i? | Что для тебя смастерить, @i? | Диалог 15, строка 1 |

## 🎁 Реакция на подарки (Gift Responses)

### ❤️ Любимый подарок (Loved)
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.carpenter.gift_loved.0.line_0` | Who told you I like these? What a fantastic gift @i! | Кто тебе подсказал, что я люблю такое? Потрясающий подарок, @i! | Вариант 1 |
| `dialog.npc.carpenter.gift_loved.1.line_0` | Thank you so much, this is an incredible gift. | Огромное спасибо, это просто невероятный подарок! | Вариант 2 |
| `dialog.npc.carpenter.gift_loved.2.line_0` | You're a really good friend you know that @i? | Ты замечательный друг, знаешь об этом, @i? | Вариант 3 |
| `dialog.npc.carpenter.gift_loved.3.line_0` | Thank you, this is very special to me. | Спасибо, для меня это очень ценно. | Вариант 4 |
| `dialog.npc.carpenter.gift_loved.4.line_0` | This will really help me out in the field! Thank you so much @i! | Это невероятно пригодится мне в походах! Огромное спасибо, @i! | Вариант 5 |
| `dialog.npc.carpenter.gift_loved.5.line_0` | Wow, thank you @i! Grand gestures like these mean so much to me! | Ого, спасибо, @i! Такие широкие жесты значат для меня очень много! | Вариант 6 |

### 👍 Понравившийся подарок (Liked)
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.carpenter.gift_liked.0.line_0` | Things like these help me out while I'm exploring the field | Такие вещи очень выручают меня во время исследований диких земель. | Вариант 1 |
| `dialog.npc.carpenter.gift_liked.1.line_0` | That's so kind of you, I was thinking about picking this up soon. | Как мило с твоей стороны! Я как раз собирался раздобыть нечто подобное. | Вариант 2 |
| `dialog.npc.carpenter.gift_liked.2.line_0` | You read my mind @i, I was running out of these! | Ты прямо читаешь мои мысли, @i! У меня они как раз заканчивались! | Вариант 3 |
| `dialog.npc.carpenter.gift_liked.3.line_0` | Thank you, I can't wait to get done working today so I can use this. | Спасибо! Жду не дождусь окончания работы, чтобы опробовать это. | Вариант 4 |
| `dialog.npc.carpenter.gift_liked.4.line_0` | That's very nice of you, going out of your way to get me this with that busy schedule you have means a lot. | Очень приятно! Найти время в твоём плотном графике ради такого подарка — это дорогого стоит. | Вариант 5 |
| `dialog.npc.carpenter.gift_liked.5.line_0` | I'm a little awkward when receiving gifts but trust me I do like this! | Я немного смущаюсь, когда мне дарят подарки, но поверь — мне правда очень нравится! | Вариант 6 |
| `dialog.npc.carpenter.gift_liked.6.line_0` | Thank you @i, large gestures like these mean a lot. | Спасибо, @i, такой знак внимания очень много для меня значит. | Вариант 7 |

### 😐 Нейтральный подарок (Neutral)
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.carpenter.gift_neutral.0.line_0` | Thank you @i, small gestures like these mean a lot. | Спасибо, @i! Приятно получить такой знак внимания. | Вариант 1 |
| `dialog.npc.carpenter.gift_neutral.1.line_0` | Why thank you. | О, благодарю. | Вариант 2 |
| `dialog.npc.carpenter.gift_neutral.2.line_0` | That's very nice of you. | Очень мило с твоей стороны. | Вариант 3 |
| `dialog.npc.carpenter.gift_neutral.3.line_0` | Thanks! | Спасибо! | Вариант 4 |
| `dialog.npc.carpenter.gift_neutral.4.line_0` | Thank you kindly, that's very considerate. | Сердечно благодарю, очень внимательно с твоей стороны. | Вариант 5 |
| `dialog.npc.carpenter.gift_neutral.5.line_0` | This kind of thing will help make the long days feel shorter, thank you! | Такая вещь скрасит долгий рабочий день, спасибо! | Вариант 6 |
| `dialog.npc.carpenter.gift_neutral.6.line_0` | Thank you for the gift. | Спасибо за подарок. | Вариант 7 |
| `dialog.npc.carpenter.gift_neutral.7.line_0` | You were thinking of me @i? That's very kind. | Ты вспомнил обо мне, @i? Это очень приятно. | Вариант 8 |

### 👎 Не понравившийся подарок (Disliked)
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.carpenter.gift_disliked.0.line_0` | Oh... | Ох... | Вариант 1 |
| `dialog.npc.carpenter.gift_disliked.1.line_0` | I don't really want this... | Мне это не особо нужно... | Вариант 2 |
| `dialog.npc.carpenter.gift_disliked.2.line_0` | Thanks? | Э-э... спасибо? | Вариант 3 |
| `dialog.npc.carpenter.gift_disliked.3.line_0` | Oh okay... Please don't give me any more of these. | Ясно... Пожалуйста, не дари мне такое больше. | Вариант 4 |
| `dialog.npc.carpenter.gift_disliked.4.line_0` | Gift giving isn't your strong suit I'm guessing? | Похоже, выбор подарков — не самая сильная твоя сторона? | Вариант 5 |
| `dialog.npc.carpenter.gift_disliked.5.line_0` | I wonder if I can make tree fertilizer out of this... | Интересно, получится ли пустить это на древесное удобрение... | Вариант 6 |
| `dialog.npc.carpenter.gift_disliked.6.line_0` | Did Leon tell you I like this? That's not a very funny prank... | Это Леон сказал тебе, что мне такое нравится? Не очень-то смешная шутка... | Вариант 7 |
| `dialog.npc.carpenter.gift_disliked.7.line_0` | I'm glad you're not littering but surely there's a better place with it! | Здорово, конечно, что ты не мусоришь где попало, но этому добру точно можно найти место получше! | Вариант 8 |
| `dialog.npc.carpenter.gift_disliked.8.line_0` | What do you mean you're giving this to me? Why? | В смысле ты отдаёшь это мне? Зачем? | Вариант 9 |
| `dialog.npc.carpenter.gift_disliked.9.line_0` | Why did you think I would like this? | С чего ты взял, что мне это понравится? | Вариант 10 |

### 😡 Ненавистный подарок (Hated)
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.carpenter.gift_hated.0.line_0` | This is extremely disrespectful. Get away from me. | Это вопиющее неуважение. Отойди от меня. | Вариант 1 |
| `dialog.npc.carpenter.gift_hated.1.line_0` | Get out of my face with that you hateful piece of dirt. | Убери это от моего лица, бессовестный ты человек. | Вариант 2 |
| `dialog.npc.carpenter.gift_hated.2.line_0` | When you wake up in the morning I hope you reflect on what kind of person you're trying to be | Надеюсь, проснувшись завтра утром, ты задумаешься о том, каким человеком становишься. | Вариант 3 |
| `dialog.npc.carpenter.gift_hated.3.line_0` | Treating people horribly won't get you anywhere around here. | С таким хамским отношением к людям ты здесь далеко не уедешь. | Вариант 4 |
| `dialog.npc.carpenter.gift_hated.4.line_0` | All you do is take take take from everyone around you. | Всё, что ты делаешь — это берёшь, берёшь и берёшь от окружающих. | Вариант 5 |
| `dialog.npc.carpenter.gift_hated.4.line_1` | This is what you give back? | И вот этим ты решил отплатить? | Вариант 5 |
| `dialog.npc.carpenter.gift_hated.5.line_0` | I wasn't aware you were that kind of person. | Я и не подозревал, что ты настолько неприятный человек. | Вариант 6 |
| `dialog.npc.carpenter.gift_hated.5.line_1` | Maybe coming here was a mistake. | Похоже, приезжать сюда было большой ошибкой. | Вариант 6 |
| `dialog.npc.carpenter.gift_hated.6.line_0` | ... | ... | Вариант 7 |
| `dialog.npc.carpenter.gift_hated.6.line_1` | Get away from me with that. | Уйди от меня с этой дрянью. | Вариант 7 |
| `dialog.npc.carpenter.gift_hated.7.line_0` | It's a cold world out here. Give me more garbage like this and you'll end up alone. | Этот мир и так суров. Будешь совать мне такой мусор — останешься в полном одиночестве. | Вариант 8 |
| `dialog.npc.carpenter.gift_hated.8.line_0` | What did I do to deserve this treatment. | Чем я заслужил такое отношение? | Вариант 9 |
| `dialog.npc.carpenter.gift_hated.9.line_0` | I don't have to be here you know. | Знаешь ли, я вовсе не обязан здесь оставаться. | Вариант 10 |

## 🌟 Уникальные диалоги (Unique)
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.carpenter.unique_five_gift.line_0` | Hey @i, do you have time to chat? I wanted to show you what I've been working on all this time! | Эй, @i, есть минутка поболтать? Хочу показать тебе, над чем я всё это время работал! | five_gift |
| `dialog.npc.carpenter.unique_five_gift.line_1` | It's the Blockapedia! A complete set of all the building blocks I could manage to get my hands on. | Это Блокопедия! Полный справочник всех строительных блоков, которые мне удалось раздобыть. | five_gift |
| `dialog.npc.carpenter.unique_five_gift.line_2` | Knowing how much you care about this town, I feel confident entrusting my little hobby project to you. | Зная, как сильно ты заботишься о нашем городке, я со спокойной душой доверяю плод своего скромного хобби тебе. | five_gift |
| `dialog.npc.carpenter.unique_five_gift.line_3` | I couldn't manage to find mystic willow logs though, I had to call in a favor to Caroline to get some blocks made with them... | Правда, брёвна мистической ивы мне найти так и не удалось — пришлось просить об одолжении Кэролайн, чтобы изготовить пару блоков из них... | five_gift |
| `dialog.npc.carpenter.unique_five_gift.line_4` | I appreciate everything you've done for this town, and I hope you'll find this useful when building it out more! | Я очень ценю всё, что ты сделал для городка, и надеюсь, это пригодится тебе при дальнейшем строительстве! | five_gift |

## 🔀 Диалоги с выбором (Choice Dialogs)
| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |
|---|---|---|---|
| `dialog.npc.carpenter.dialog.need_to_buy.line_0` | Need to pick up something from the shop? | Нужно что-то приобрести в лавке? | need_to_buy |
| `dialog.npc.carpenter.dialog.need_to_buy.option_0` | Purchase supplies | Купить материалы | Кнопка выбора: need_to_buy |
| `dialog.npc.carpenter.dialog.need_to_buy.option_1` | Invite Villagers | Пригласить жителей | Кнопка выбора: need_to_buy |
| `dialog.npc.carpenter.dialog.need_to_buy.option_2` | Build Farm buildings | Фермерские постройки | Кнопка выбора: need_to_buy |
| `dialog.npc.carpenter.dialog.need_to_buy.option_3` | Build Village buildings | Городские постройки | Кнопка выбора: need_to_buy |