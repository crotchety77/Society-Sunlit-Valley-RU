# 📘 Анализ обновления Society 4.1.4 и Справочник новых ключей (`translate414.md`)

## 🌟 Введение: Что изменилось в обновлении 4.1.4?

Обновление **Society: Sunlit Valley 4.1.4** существенно переработало экономику, систему заселения города (NPC), механику строительства фермы и взаимодействие с больницей при потере сознания (смерти). 

Ниже разобран детальный анализ всех нововведений, лежащих за 62 добавленными языковыми ключами.

---

## 🏥 1. Механика Долгов и Больницы (`Debt System`)

### Как это работает:
1. **Потеря сознания (Смерть игрока):**
   * Когда здоровье игрока падает до 0, игрок очухивается в **Больнице Солнечной Долины (Sunlit Valley Hospital)**.
   * За лечение выставляется счёт. Если на банковском счёте игрока есть деньги, плата списывается автоматически, и игрок получает квитанцию (`society.hospital_receipt.fee_taked`).
   * Если на банковском счёте **недостаточно средств**, игроку открывается **медицинский долг** (`society.hospital_receipt.debt`).
2. **Погашение долга через ящик отправки (`shipping_bin`):**
   * Каждое утро в 6:00 при продаже товаров из Ящика отправки игра проверяет наличие активного долга.
   * Выручка с продажи в первую очередь направляется на погашение долга, а остаток выдаётся монетами.
   * Игрок получает квитанцию об оплате долга (`society.shipping_bin.debt_paid_note`) и системное уведомление на экране (`society.shipping_bin.debt_paid`).
3. **Команды управления долгом (`command.society.debt.*`):**
   * `/society debt get <игрок>` — проверить сумму долга игрока.
   * `/society debt add <игрок> <сумма>` — добавить долг.
   * `/society debt remove <игрок> <сумма>` — списать часть долга.
   * `/society debt set <игрок> <сумма>` — установить точную сумму долга.
   * `/society debt reset <игрок>` — полностью сбросить долг на 0.

### 📋 Таблица ключей долгов:
| Ключ | Оригинал (EN) | Перевод (RU) | Описание механики |
|---|---|---|---|
| `command.society.debt.has_debt` | `%s has a debt of %s §f●§r` | `Долг %s составляет %s §f●§r` | Ответ команды проверки долга |
| `command.society.debt.no_debt` | `%s has no debt.` | `У %s нет долгов.` | Если долг равен 0 |
| `command.society.debt.reset` | `Debt for %s has been reset to 0.` | `Долг игрока %s сброшен до 0.` | Сброс долга администратором |
| `command.society.debt.set` | `Debt for %s set to %s §f●§r` | `Долг игрока %s установлен на %s §f●§r` | Установка точного значения |
| `command.society.debt.add` | `Added %s §f●§r to %s's debt. Total: %s §f●§r` | `Добавлено %s §f●§r к долгу игрока %s. Итого: %s §f●§r` | Начисление долга |
| `command.society.debt.remove` | `Removed %s §f●§r from %s's debt. Remaining: %s §f●§r` | `Списано %s §f●§r из долга игрока %s. Остаток: %s §f●§r` | Частичное списание |
| `command.society.debt.invalid_amount_positive` | `Amount must be > 0.` | `Сумма должна быть больше 0.` | Валидация аргументов команды |
| `command.society.debt.invalid_amount_non_negative` | `Amount must be >= 0.` | `Сумма должна быть не меньше 0.` | Валидация аргументов команды |

---

## 🏗️ 2. Переработка Магазина построек (Ace the Carpenter & Blueprints)

### Что изменилось:
* Раньше фермерские постройки и дома жителей покупались напрямую через вкладку заданий в FTB Quests.
* **В 4.1.4 система переработана:** Теперь все чертежи зданий продаются у **Плотника Эйса (Ace the Carpenter)**.
* Появился специальный предмет **«Чертежи» (`society:blueprints`)**, который позволяет открывать меню покупки фермерских построек удалённо из любой точки карты без необходимости бежать к плотнику.

### 📋 Таблица ключей:
| Ключ | Оригинал (EN) | Перевод (RU) |
|---|---|---|
| `society.login_update.title` | `===[ Welcome to Society: Sunlit Valley 4.1! ]===` | `===[ Добро пожаловать в Society: Sunlit Valley 4.1! ]===` |
| `society.login_update.desc_0` | `Thank you for playing! The Building Shop has been removed from the quest book. You can now purchase blueprints from Ace the Carpenter.` | `Спасибо за игру! Магазин построек был убран из книги квестов. Теперь вы можете покупать чертежи у Плотника Эйса.` |
| `society.login_update.desc_1` | `There is also a dedicated item that can be used to access the bulding shop called 'Blueprints' that can be purchased from Ace as well.` | `Также появился специальный предмет «Чертежи» для удалённого доступа к магазину построек — его тоже можно приобрести у Эйса.` |
| `tooltip.society.blueprints` | `Allows you to purchase farm and villager buildings from Ace anywhere` | `Позволяет заказывать постройки и дома жителей у Эйса из любого места` |
| `society.new_villager.message` | `Someone new wants to move into your town! Check the Carpenter's invitation shop to invite them.` | `Кто-то хочет переехать в ваш городок! Проверьте магазин приглашений у Плотника, чтобы пригласить жителя.` |
| `jei.society.category.block_purchasing` | `Block Purchasing` | `Покупка блоков` |

---

## 🏘️ 3. Дерево приглашения жителей (Invitations System)

Жители больше не спавнятся сами по себе. Игрок должен приглашать их в город постепенно, выполняя условия прогрессии:

```
[Старт] → Крафт Приглашения Плотника
                ↓
[Приглашён Плотник (Ace)] → Открывает приглашения: Пастух, Рынок, Кузнец
                ↓
[Приглашён Торговец с Рынка] → Открывает приглашения: Рыбак, Банкир, Библиотекарь
                ↓
[Экспедиция в Пещеру Черепа] → Открывает Экзотического торговца
[Экспедиция в Незер] → Открывает Ведьму
[Встреча в дикой природе] → Мудрый Дуб
```

### 📋 Таблица условий разблокировки (`info.society.villager_unlock_condition.*`):
| Ключ | Оригинал (EN) | Перевод (RU) |
|---|---|---|
| `info.society.villager_unlock_condition.carpenter` | `Craft the capenter invitation using simple resources` | `Создайте приглашение плотника из простых ресурсов` |
| `info.society.villager_unlock_condition.shepherd` | `Invite the carpenter villager to unlock invitation` | `Пригласите плотника, чтобы открыть приглашение` |
| `info.society.villager_unlock_condition.market` | `Invite the carpenter villager to unlock invitation` | `Пригласите плотника, чтобы открыть приглашение` |
| `info.society.villager_unlock_condition.blacksmith` | `Invite the carpenter villager to unlock invitation` | `Пригласите плотника, чтобы открыть приглашение` |
| `info.society.villager_unlock_condition.fisher` | `Invite the market villager to unlock invitation` | `Пригласите торговца с рынка, чтобы открыть приглашение` |
| `info.society.villager_unlock_condition.banker` | `Invite the market villager to unlock invitation` | `Пригласите торговца с рынка, чтобы открыть приглашение` |
| `info.society.villager_unlock_condition.librarian` | `Invite the market villager to unlock invitation` | `Пригласите торговца с рынка, чтобы открыть приглашение` |
| `info.society.villager_unlock_condition.trader` | `Enter the Skull Cavern to unlock invitation` | `Войдите в Пещеру Черепа, чтобы открыть приглашение` |
| `info.society.villager_unlock_condition.witch` | `Enter the Nether to unlock invitation` | `Войдите в Незер, чтобы открыть приглашение` |
| `info.society.villager_unlock_condition.wise_oak` | `Find and talk to the Wise Oak in the wild...` | `Найдите Мудрый Дуб в дикой природе и поговорите с ним...` |

---

## 🌾 4. Интеграция с Jade (Отображение роста культур)

В 4.1.4 добавлено детальное отображение стадии созревания культур в днях и требований к почве прямо во всплывающей подсказке Jade:

| Ключ | Оригинал (EN) | Перевод (RU) | Смысл в игре |
|---|---|---|---|
| `jade.society.crop_growth` | `Growth: %s/%s Days` | `Рост: %s/%s дн.` | Текущий прогресс созревания |
| `jade.society.crop_growth.mature` | `Mature` | `Созрело` | Урожай готов к сбору |
| `jade.society.crop_growth.stop` | `Cannot grow` | `Рост невозможен` | Неподходящий сезон или условия |
| `jade.society.crop_growth.need_stem` | `Requires Grapevine Stem` | `Требуется виноградный стебель` | Лоза винограда Vinery |
| `jade.society.crop_growth.need_lattice` | `Requires Grapevine Lattice` | `Требуется виноградная шпалера` | Шпалера для вьющихся культур |
| `jade.society.crop_growth.need_farmland` | `Requires Farmland` | `Требуется вспаханная земля` | Обычная грядка |
| `jade.society.crop_growth.need_watered_farmland` | `Requires Farmland underwater` | `Требуется подводная пашня` | Подводные культуры (рис и т.д.) |

---

## 🪑 5. Каталоги мебели и награды Клуба (Community Center)

| Ключ | Оригинал (EN) | Перевод (RU) | Назначение |
|---|---|---|---|
| `tooltip.society.tanuki_catalog` | `Allows you to purchase furniture from the ♤ §aTanuki collection` | `Позволяет заказывать мебель из коллекции ♤ §aTanuki` | Каталог японской/природной мебели |
| `tooltip.society.modern_catalog` | `Allows you to purchase furniture from the ♧ §fModern collection` | `Позволяет заказывать мебель из коллекции ♧ §fМодерн` | Каталог современной мебели |
| `tooltip.society.fantasy_catalog` | `Allows you to purchase furniture from the ♡ §eFantasy collection` | `Позволяет заказывать мебель из коллекции ♡ §eФэнтези` | Каталог сказочной мебели |
| `tooltip.society.petal_apothecary.description` | `The Abandoned Farm is located in the Community Center section of the Quest Book after completing 3 other chapters.` | `«Заброшенная ферма» находится в разделе Клуба в Книге квестов после завершения 3 других глав.` | Подсказка к разблокировке Аптекаря |
| `tooltip.society.kinetic_blueprint.description` | `The Boiler Room is located in the Community Center section of the Quest Book.` | `«Котельная» находится в разделе Клуба в Книге квестов.` | Механические чертежи Create |
| `tooltip.society.skull_cavern_teleporter.description` | `The Vault is located in the Community Center section of the Quest Book.` | `«Хранилище» находится в разделе Клуба в Книге квестов.` | Телепорт в Пещеру Черепа |
| `tooltip.society.magic_mirror.description` | `The Crafts Room is located in the Community Center section of the Quest Book.` | `«Комната ремёсел» находится в разделе Клуба в Книге квестов.` | Зеркало телепортации домой |
| `tooltip.society.nether_star_hook.obtain` | `🏹 §6Fish Tank Reward` | `🏹 §6Награда Аквариума` | Крючок Звезды Незера |
| `tooltip.society.nether_star_hook.description` | `The Fish Tank is located in the Community Center section of the Quest Book.` | `«Аквариум» находится в разделе Клуба в Книге квестов.` | Награда за закрытие рыбного набора |
| `tooltip.society.general_mastery.required` | `🏹 §bSkill Mastery Item` | `🏹 §bПредмет Мастерства навыков` | Поздняя игра (Endgame) |
| `tooltip.society.general_mastery.description` | `The Skill Mastery tree is unlocked after reaching level 12 in every skill.` | `Древо Мастерства навыков открывается после достижения 12 уровня во всех навыках.` | Условие открытия Мастерства |
| `tooltip.society.charting_map` | `Allows you to link two signs together via a path for teleportation` | `Позволяет связать две таблички дорожкой для быстрой телепортации` | Быстрое перемещение по ферме |

---

## ⚙️ 6. Новые механизмы и автоматизация

* **Рог изобилия (`society:drum_cornucopia`):** блок автоматизации садов. Каждое утро ровно в 7:00 автоматически трясет окружающие плодовые деревья и собирает спелые фрукты.
* **Менеджер рыбных садков (`society:fish_pond_manager`):** каждое утро в 7:00 сканирует все садки в радиусе 10 блоков и автоматически сдаёт квесты, если в инвентаре или сундуках есть нужные ресурсы.
* **Инкубатор гусениц (`society:caterpillar_box`):** инкубирует яйца редких бабочек и мотыльков (мод Longwings). Каждые 5 минут выводит взрослую особь, которая вылетает через верх.

| Ключ | Оригинал (EN) | Перевод (RU) |
|---|---|---|
| `block.society.artisan_hopper.filter` | `This Artisan Hopper cannot work with a filter upgrade!` | `Эта Ремесленная воронка не может работать с улучшением-фильтром!` |
| `block.society.drum_cornucopia.description` | `Harvest fruits from nearby trees at 7am` | `Собирает плоды с соседних деревьев каждое утро в 7:00` |
| `block.society.fish_pond_manager.description` | `Submits quests for fish ponds at 7am every morning` | `Автоматически сдает квесты для рыбных садков каждое утро в 7:00` |
| `block.society.caterpillar_box.description` | `Hatches Caterpillar Eggs placed inside every 5 minutes. Butterflies and Moths fly out of the box's top.` | `Высиживает помещённые внутрь яйца гусениц каждые 5 минут. Вылупившиеся бабочки и мотыльки вылетают через верх инкубатора.` |

---

## 🪄 7. Тотемы погоды, Разведение бабочек и Артефакты

* **Тотемы погоды:** одноразовые или многоразовые идолы, позволяющие мгновенно вызывать дождь (`rain_totem`), грозу для зарядки батарей (`thunder_totem`) или разгонять тучи для чистого солнечного дня (`dry_totem`).
* **Пыльца фей (`fairy_dust`):** расходуемый порошок, ускоряющий созревание вин, сыров, бочек и ремесленных машин на 1 полный игровой день.
* **Генетика бабочек (`Longwings`):** яйца гусениц хранят информацию о родителях (`parents`), виде (`type`) и максимальном размере особи (`size`), который напрямую увеличивает цену продажи при наличии книги *«Метаморфоза»*.

| Ключ | Оригинал (EN) | Перевод (RU) |
|---|---|---|
| `item.society.ancient_builders_tool.description` | `Relic of the World-Shapers` | `Реликвия Создателей Мира` |
| `item.society.red_wrench.description` | `I swear I won't use it...` | `Клянусь, я не буду её использовать...` |
| `item.society.the_metamorphosize.description` | `Impact of size on Butterfly/Moth prices are tripled.` | `Влияние размера на цену бабочек и мотыльков утроено (x3).` |
| `item.society.the_metamorphosize.price_modifier` | `The Metamorphosize +%s from size` | `Метаморфоза +%s от размера` |
| `item.society.fairy_dust.description` | `Use on an Artisan Machine to progress it by 1 day` | `Используйте на Ремесленной машине, чтобы ускорить её работу на 1 день` |
| `item.society.suspicious_milk_tea.description` | `...Why is there a leaf sticking out of it?` | `...И почему из него торчит лист?` |
| `item.society.dry_totem.description` | `Summons clear skies by sucking up all the rain` | `Очищает небо от туч, поглощая весь дождь` |
| `item.society.thunder_totem.description` | `Summons a thunderstorm from its anger` | `Призывает яростную грозу` |
| `item.society.rain_totem.description` | `Summons drops of water that fall from the sky (rain)` | `Призывает капли воды, падающие с небес (дождь)` |
| `item.society.caterpillar_eggs.description` | `Place in Caterpillar Box to hatch into a Butterfly or Moth!` | `Поместите в Инкубатор гусениц, чтобы вырастить бабочку или мотылька!` |
| `item.society.caterpillar_eggs.longwing.type` | `Type: %s` | `Вид: %s` |
| `item.society.caterpillar_eggs.longwing.parents` | `Parents: %s & %s` | `Родители: %s и %s` |
| `item.society.caterpillar_eggs.longwing.size` | `Max size: %s` | `Макс. размер: %s` |
| `society.item_frame.rod` | `I need to remove my bobber before placing this here...` | `Мне нужно снять поплавок перед тем, как повесить её сюда...` |
