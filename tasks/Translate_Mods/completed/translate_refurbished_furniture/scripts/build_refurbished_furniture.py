import json
import os
import sys

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", ".."))
TASK_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
EN_PATH = os.path.join(TASK_DIR, "en_us_all.json")
RU_MOD_PATH = os.path.join(ROOT_DIR, "translations", "mods", "refurbished_furniture.json")
GAME_LANG_PATH = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\refurbished_furniture\lang\ru_ru.json"
NEW_TRANSLATE_MD_PATH = os.path.join(TASK_DIR, "new_translate.md")

with open(EN_PATH, "r", encoding="utf-8") as f:
    en = json.load(f)

# Materials dictionary
WOOD_MAP = {
    "oak": "Дубовый",
    "spruce": "Еловый",
    "birch": "Берёзовый",
    "jungle": "Тропический",
    "acacia": "Акациевый",
    "dark_oak": "Тёмно-дубовый",
    "crimson": "Багровый",
    "warped": "Искажённый",
    "mangrove": "Мангровый",
    "cherry": "Вишнёвый"
}

WOOD_FEM_MAP = {
    "oak": "Дубовая",
    "spruce": "Еловая",
    "birch": "Берёзовая",
    "jungle": "Тропическая",
    "acacia": "Акациевая",
    "dark_oak": "Тёмно-дубовая",
    "crimson": "Багровая",
    "warped": "Искажённая",
    "mangrove": "Мангровая",
    "cherry": "Вишнёвая"
}

WOOD_NEU_MAP = {
    "oak": "Дубовое",
    "spruce": "Еловое",
    "birch": "Берёзовое",
    "jungle": "Тропическое",
    "acacia": "Акациевое",
    "dark_oak": "Тёмно-дубовое",
    "crimson": "Багровое",
    "warped": "Искажённое",
    "mangrove": "Мангровое",
    "cherry": "Вишнёвое"
}

WOOD_GEN_MAP = {
    "oak": "из дуба",
    "spruce": "из ели",
    "birch": "из берёзы",
    "jungle": "из тропического дерева",
    "acacia": "из акации",
    "dark_oak": "из тёмного дуба",
    "crimson": "из багрового дерева",
    "warped": "из искажённого дерева",
    "mangrove": "из мангрового дерева",
    "cherry": "из вишни"
}

COLOR_MAP = {
    "white": "Белый",
    "orange": "Оранжевый",
    "magenta": "Пурпурный",
    "light_blue": "Голубой",
    "yellow": "Жёлтый",
    "lime": "Лаймовый",
    "pink": "Розовый",
    "gray": "Серый",
    "light_gray": "Светло-серый",
    "cyan": "Бирюзовый",
    "purple": "Фиолетовый",
    "blue": "Синий",
    "brown": "Коричневый",
    "green": "Зелёный",
    "red": "Красный",
    "black": "Чёрный"
}

COLOR_FEM_MAP = {
    "white": "Белая",
    "orange": "Оранжевая",
    "magenta": "Пурпурная",
    "light_blue": "Голубая",
    "yellow": "Жёлтая",
    "lime": "Лаймовая",
    "pink": "Розовая",
    "gray": "Серая",
    "light_gray": "Светло-серая",
    "cyan": "Бирюзовая",
    "purple": "Фиолетовая",
    "blue": "Синяя",
    "brown": "Коричневая",
    "green": "Зелёная",
    "red": "Красная",
    "black": "Чёрная"
}

COLOR_NEU_MAP = {
    "white": "Белое",
    "orange": "Оранжевое",
    "magenta": "Пурпурное",
    "light_blue": "Голубое",
    "yellow": "Жёлтое",
    "lime": "Лаймовое",
    "pink": "Розовое",
    "gray": "Серое",
    "light_gray": "Светло-серое",
    "cyan": "Бирюзовое",
    "purple": "Фиолетовое",
    "blue": "Синее",
    "brown": "Коричневое",
    "green": "Зелёное",
    "red": "Красное",
    "black": "Чёрное"
}

# Manual translation dictionary for non-procedural items
MANUAL = {
    "itemGroup.refurbished_furniture": "Refurbished Furniture (Мебель)",
    
    # Filter categories
    "filterCategory.refurbished_furniture.general": "Общее",
    "filterCategory.refurbished_furniture.general.desc": "Столы, стулья, ящики и другое",
    "filterCategory.refurbished_furniture.storage": "Хранение",
    "filterCategory.refurbished_furniture.storage.desc": "Шкафы, комоды, ящики и банки",
    "filterCategory.refurbished_furniture.bedroom": "Спальня",
    "filterCategory.refurbished_furniture.bedroom.desc": "Кровати, тумбочки, шкафы и светильники",
    "filterCategory.refurbished_furniture.kitchen": "Кухня",
    "filterCategory.refurbished_furniture.kitchen.desc": "Кухонные гарнитуры, бытовая техника и раковины",
    "filterCategory.refurbished_furniture.living_room": "Гостиная",
    "filterCategory.refurbished_furniture.living_room.desc": "Диваны, телевизоры, лампы и столики",
    "filterCategory.refurbished_furniture.dining_room": "Столовая",
    "filterCategory.refurbished_furniture.dining_room.desc": "Обеденные столы, стулья и посуда",
    "filterCategory.refurbished_furniture.bathroom": "Ванная комната",
    "filterCategory.refurbished_furniture.bathroom.desc": "Ванны, умывальники и туалеты",
    "filterCategory.refurbished_furniture.outdoors": "Двор и сад",
    "filterCategory.refurbished_furniture.outdoors.desc": "Грили, заборы, живые изгороди и батуты",
    "filterCategory.refurbished_furniture.electronics": "Электроника",
    "filterCategory.refurbished_furniture.electronics.desc": "Светильники, компьютеры, генераторы и прочее",

    # Death messages
    "death.attack.refurbished_furniture.ceiling_fan": "%1$s погиб под лопастями потолочного вентилятора",
    "death.attack.refurbished_furniture.ceiling_fan.player": "%1$s был порублен лопастями потолочного вентилятора",

    # Containers
    "container.refurbished_furniture.freezer": "Морозильник",
    "container.refurbished_furniture.cooler": "Переносной холодильник",
    "container.refurbished_furniture.microwave": "Микроволновка",
    "container.refurbished_furniture.stove": "Кухонная плита",
    "container.refurbished_furniture.workbench": "Верстак мебели",
    "container.refurbished_furniture.crate": "Ящик",
    "container.refurbished_furniture.drawer": "Комод",
    "container.refurbished_furniture.kitchen_drawer": "Кухонный комод",
    "container.refurbished_furniture.mail_box": "Почтовый ящик",
    "container.refurbished_furniture.post_box": "Почтовый ящик",
    "container.refurbished_furniture.electricity_generator": "Электрогенератор",
    "container.refurbished_furniture.recycle_bin": "Утилизатор",
    "container.refurbished_furniture.storage_cabinet": "Шкаф для хранения",
    "container.refurbished_furniture.lightswitch": "Выключатель света",
    "container.refurbished_furniture.storage_jar": "Банка для хранения",

    # GUI
    "gui.refurbished_furniture.set_mailbox_name": "Название почтового ящика",
    "gui.refurbished_furniture.rename_mailbox_failed": "Не удалось обновить имя почтового ящика",
    "gui.refurbished_furniture.mailboxes": "Почтовые ящики",
    "gui.refurbished_furniture.search": "Поиск...",
    "gui.refurbished_furniture.search_mailboxes": "Поиск почтовых ящиков",
    "gui.refurbished_furniture.enter_message": "Введите сообщение...",
    "gui.refurbished_furniture.package_message": "Сообщение к посылке",
    "gui.refurbished_furniture.send": "Отправить",
    "gui.refurbished_furniture.how_to": "Справка",
    "gui.refurbished_furniture.post_box_info": "Выберите почтовый ящик из списка. Можно искать по названию ящика или по нику игрока через префикс @. Положите предметы в слоты посылки и при желании напишите записку. Нажмите кнопку отправки для доставки.",
    "gui.refurbished_furniture.workbench_info": "Выберите рецепт из списка и соберите необходимые материалы. Верстак ищет материалы в вашем инвентаре, в собственном отсеке и в соседних контейнерах.",
    "gui.refurbished_furniture.package_sent_by": "Отправитель: %s",
    "gui.refurbished_furniture.package_open": "ПКМ, чтобы открыть",
    "gui.refurbished_furniture.set_doorbell_name": "Имя дверного звонка",
    "gui.refurbished_furniture.doorbell_rang": "Звонок в дверь",
    "gui.refurbished_furniture.status.online": "В сети",
    "gui.refurbished_furniture.status.offline": "Не в сети",
    "gui.refurbished_furniture.status.overloaded": "Перегрузка сети",
    "gui.refurbished_furniture.status.no_fuel": "Нет топлива",
    "gui.refurbished_furniture.node_count": "%s / %s",
    "gui.refurbished_furniture.recycle": "Переработать",
    "gui.refurbished_furniture.save": "Сохранить",
    "gui.refurbished_furniture.next_preset": "Следующий пресет",
    "gui.refurbished_furniture.previous_preset": "Предыдущий пресет",
    "gui.refurbished_furniture.no_power": "Нет электропитания",
    "gui.refurbished_furniture.link_too_long": "Слишком далеко",
    "gui.refurbished_furniture.link_too_many": "Слишком много соединений",
    "gui.refurbished_furniture.link_already_connected": "Уже подключено",
    "gui.refurbished_furniture.link_invalid_node": "Недопустимый узел",
    "gui.refurbished_furniture.link_unpowerable": "Линия не будет запитана",
    "gui.refurbished_furniture.link_outside_area": "Линия выходит за пределы зоны питания",
    "gui.refurbished_furniture.connect_to_power": "Убедитесь, что блок получает питание от %s. Его можно подключить с помощью %s.",
    "gui.refurbished_furniture.electricity_generator": "Электрогенератора",
    "gui.refurbished_furniture.jei_campfire_info": "Аналогично готовке на костре",
    "gui.refurbished_furniture.progress": "%s %s %s",
    "gui.refurbished_furniture.hold_for_details": "Зажмите %s для подробностей",
    "gui.refurbished_furniture.shift": "SHIFT",
    "gui.refurbished_furniture.show_all_categories": "Показать всё",
    "gui.refurbished_furniture.mail_box_limit": "Вы достигли лимита почтовых ящиков",
    "gui.refurbished_furniture.invalid_dimension": "Почтовые ящики нельзя ставить в этом измерении",
    "gui.refurbished_furniture.invalid_mailbox": "Почтовый ящик отключён, так как находится в запрещённом измерении",
    "gui.refurbished_furniture.default_mailbox_name": "Почтовый ящик",
    "gui.refurbished_furniture.unknown_mailbox_owner": "Неизвестный игрок",
    "gui.refurbished_furniture.delivery_service.unknown_mailbox": "Неизвестный или недоступный почтовый ящик",
    "gui.refurbished_furniture.delivery_service.mailbox_queue_full": "Очередь писем выбранного ящика переполнена",
    "gui.refurbished_furniture.delivery_service.undeliverable_dimension": "Выбранный ящик находится в недоступном измерении",
    "gui.refurbished_furniture.delivery_service.package_sent": "Посылка успешно отправлена!",
    "gui.refurbished_furniture.booting": "Загрузка...",
    "gui.refurbished_furniture.sliceable": "Можно нарезать",
    "gui.refurbished_furniture.placeable": "Можно разместить",
    "gui.refurbished_furniture.workbench.search_neighbours.off": "Игнорировать соседние контейнеры",
    "gui.refurbished_furniture.workbench.search_neighbours.on": "Учитывать соседние контейнеры",
    "gui.refurbished_furniture.experience_level": "%s/%s Ур.",
    "gui.refurbished_furniture.experience_points": "%s Очков опыта",
    "gui.refurbished_furniture.withdraw_experience": "Забрать опыт",
    "gui.refurbished_furniture.requires_power": "Требует электропитания от %s",

    # Computer programs
    "computer_program.refurbished_furniture.paddle_ball": "Пинг-понг",
    "computer_program.refurbished_furniture.paddle_ball.play_ai": "Играть против ИИ",
    "computer_program.refurbished_furniture.paddle_ball.play_vs": "Играть против игрока",
    "computer_program.refurbished_furniture.paddle_ball.main_menu": "Главное меню",
    "computer_program.refurbished_furniture.paddle_ball.you": "Вы",
    "computer_program.refurbished_furniture.paddle_ball.win_game": "Вы победили! :)",
    "computer_program.refurbished_furniture.paddle_ball.lose_game": "Вы проиграли :(",
    "computer_program.refurbished_furniture.paddle_ball.searching_players": "Поиск соперника...",
    "computer_program.refurbished_furniture.paddle_ball.opponent_left": "Соперник покинул игру",
    "computer_program.refurbished_furniture.paddle_ball.cancel": "Отмена",
    "computer_program.refurbished_furniture.paddle_ball.server_required": "Требуется игра на сервере",
    "computer_program.refurbished_furniture.home_control": "Умный дом",
    "computer_program.refurbished_furniture.home_control.turn_on_all": "Включить всё",
    "computer_program.refurbished_furniture.home_control.turn_off_all": "Выключить всё",
    "computer_program.refurbished_furniture.home_control.info": "«Умный дом» позволяет управлять питанием устройств, подключённых к электросети. Устройства должны находиться в одной сети с компьютером. Переименуйте приборы на наковальне перед установкой, чтобы их было легче различать в приложении.",
    "computer_program.refurbished_furniture.marketplace": "Торговая площадка",
    "computer_program.refurbished_furniture.coin_miner": "Майнер монет",

    # JEI Categories
    "jei_category.refurbished_furniture.freezer_solidifying": "Замораживание",
    "jei_category.refurbished_furniture.cutting_board_slicing": "Нарезка на доске",
    "jei_category.refurbished_furniture.frying_pan_cooking": "Жарка на сковороде",
    "jei_category.refurbished_furniture.microwave_heating": "Разогрев в микроволновке",
    "jei_category.refurbished_furniture.recycle_bin_recycling": "Утилизация",
    "jei_category.refurbished_furniture.toaster_heating": "Поджарка в тостере",
    "jei_category.refurbished_furniture.grill_cooking": "Жарка на гриле",
    "jei_category.refurbished_furniture.cutting_board_combining": "Сборка блюд",
    "jei_category.refurbished_furniture.workbench_constructing": "Конструирование мебели",
    "jei_category.refurbished_furniture.oven_baking": "Выпекание в духовке",
    "jei_category.refurbished_furniture.sink_fluid_transmuting": "Очищение в раковине",

    # Items
    "item.refurbished_furniture.spatula": "Кухонная лопатка",
    "item.refurbished_furniture.knife": "Кухонный нож",
    "item.refurbished_furniture.package": "Посылка",
    "item.refurbished_furniture.wrench": "Гаечный ключ",
    "item.refurbished_furniture.light_fridge": "Светлый холодильник",
    "item.refurbished_furniture.dark_fridge": "Тёмный холодильник",
    "item.refurbished_furniture.television_remote": "Пульт от телевизора",
    "item.refurbished_furniture.bread_slice": "Ломтик хлеба",
    "item.refurbished_furniture.toast": "Тост",
    "item.refurbished_furniture.sweet_berry_jam": "Джем из сладких ягод",
    "item.refurbished_furniture.sweet_berry_jam_toast": "Тост с ягодным джемом",
    "item.refurbished_furniture.glow_berry_jam": "Джем из светящихся ягод",
    "item.refurbished_furniture.glow_berry_jam_toast": "Тост со светящимся джемом",
    "item.refurbished_furniture.sea_salt": "Морская соль",
    "item.refurbished_furniture.wheat_flour": "Пшеничная мука",
    "item.refurbished_furniture.dough": "Тесто",
    "item.refurbished_furniture.cheese": "Сыр",
    "item.refurbished_furniture.cheese_sandwich": "Бутерброд с сыром",
    "item.refurbished_furniture.cheese_toastie": "Горячий сэндвич с сыром",
    "item.refurbished_furniture.raw_vegetable_pizza": "Сырая овощная пицца",
    "item.refurbished_furniture.cooked_vegetable_pizza": "Овощная пицца",
    "item.refurbished_furniture.vegetable_pizza_slice": "Кусочек овощной пиццы",
    "item.refurbished_furniture.raw_meatlovers_pizza": "Сырая мясная пицца",
    "item.refurbished_furniture.cooked_meatlovers_pizza": "Мясная пицца",
    "item.refurbished_furniture.meatlovers_pizza_slice": "Кусочек мясной пиццы",

    # Subtitles
    "subtitle.refurbished_furniture.package_open": "Шуршание картона",
    "subtitle.refurbished_furniture.chair_slide": "Скрип стула",
    "subtitle.refurbished_furniture.doorbell_chime": "Звон дверного звонка",
    "subtitle.refurbished_furniture.electricity_generator_engine": "Гул генератора",
    "subtitle.refurbished_furniture.storage_jar_insert_item": "Шуршание предметов",
    "subtitle.refurbished_furniture.recycle_bin_engine": "Дробление мусора",
    "subtitle.refurbished_furniture.ceiling_fan_spin": "Вращение вентилятора",
    "subtitle.refurbished_furniture.lightswitch_flick": "Щёлк выключателя",
    "subtitle.refurbished_furniture.trampoline_bounce": "Прыжок на батуте",
    "subtitle.refurbished_furniture.trampoline_super_bounce": "Суперпрыжок на батуте",
    "subtitle.refurbished_furniture.television_channel.colour_test": "Высокий писк настроечной таблицы",
    "subtitle.refurbished_furniture.television_channel.white_noise": "Белый шум телевизора",
    "subtitle.refurbished_furniture.television_channel.dance_music": "Танцевальный бит",
    "subtitle.refurbished_furniture.television_channel.villager_news": "Новости жителей",
    "subtitle.refurbished_furniture.television_channel.chirp_song": "Птичье чириканье под музыку",
    "subtitle.refurbished_furniture.television_channel.ocean_sunset": "Lo-Fi музыка",
    "subtitle.refurbished_furniture.television_channel.blocky_game": "Мелодия на пианино",
    "subtitle.refurbished_furniture.television_channel.retro_song": "Ретро-аркадная музыка",
    "subtitle.refurbished_furniture.frying_pan.place_ingredient": "Шлепок ингредиента",
    "subtitle.refurbished_furniture.frying_pan.break": "Звон металла",
    "subtitle.refurbished_furniture.frying_pan.hit": "Удар по металлу",
    "subtitle.refurbished_furniture.frying_pan.place": "Установка сковороды",
    "subtitle.refurbished_furniture.frying_pan.step": "Шаги по металлу",
    "subtitle.refurbished_furniture.frying_pan.sizzling": "Шкворчание масла",
    "subtitle.refurbished_furniture.toaster.down": "Тостер включён",
    "subtitle.refurbished_furniture.toaster.pop": "Тостер выскочил",
    "subtitle.refurbished_furniture.toaster.insert": "Загрузка тоста",
    "subtitle.refurbished_furniture.cooler.open": "Холодильник открыт",
    "subtitle.refurbished_furniture.cooler.close": "Холодильник закрыт",
    "subtitle.refurbished_furniture.microwave.open": "Микроволновка открыта",
    "subtitle.refurbished_furniture.microwave.close": "Микроволновка закрыта",
    "subtitle.refurbished_furniture.kitchen_drawer.open": "Выдвижной ящик открыт",
    "subtitle.refurbished_furniture.kitchen_drawer.close": "Выдвижной ящик закрыт",
    "subtitle.refurbished_furniture.cutting_board.place_ingredient": "Ингредиент выложен",
    "subtitle.refurbished_furniture.kitchen_sink.fill": "Журчание воды",
    "subtitle.refurbished_furniture.fridge.open": "Холодильник открыт",
    "subtitle.refurbished_furniture.fridge.close": "Холодильник закрыт",
    "subtitle.refurbished_furniture.stove.open": "Духовка открыта",
    "subtitle.refurbished_furniture.stove.close": "Духовка закрыта",
    "subtitle.refurbished_furniture.freezer.open": "Морозильник открыт",
    "subtitle.refurbished_furniture.freezer.close": "Морозильник закрыт",
    "subtitle.refurbished_furniture.drawer.open": "Комод открыт",
    "subtitle.refurbished_furniture.drawer.close": "Комод закрыт",
    "subtitle.refurbished_furniture.workbench.craft": "Мебель изготовлена",
    "subtitle.refurbished_furniture.wrench_selected_node = Node Highlighted": "Узел выделен",
    "subtitle.refurbished_furniture.wrench_selected_node": "Узел выделен",
    "subtitle.refurbished_furniture.wrench_remove_link": "Линия удалена",
    "subtitle.refurbished_furniture.wrench_connected_link": "Линия подключена",
    "subtitle.refurbished_furniture.wrench_hover_link": "Наведение на линию",
    "subtitle.refurbished_furniture.knife_chop": "Нарезка ножом",
    "subtitle.refurbished_furniture.spatula_scoop": "Поддевание лопаткой",
    "subtitle.refurbished_furniture.cabinet.open": "Дверца шкафа открыта",
    "subtitle.refurbished_furniture.cabinet.close": "Дверца шкафа закрыта",
    "subtitle.refurbished_furniture.microwave.fan": "Гул микроволновки",
    "subtitle.refurbished_furniture.ui.paddle_ball.retro_click": "Ретро-щелчок",
    "subtitle.refurbished_furniture.ui.paddle_ball.retro_hit": "Ретро-удар",
    "subtitle.refurbished_furniture.ui.paddle_ball.retro_success": "Ретро-победа",
    "subtitle.refurbished_furniture.ui.paddle_ball.retro_fail": "Ретро-промах",
    "subtitle.refurbished_furniture.ui.paddle_ball.retro_win": "Ретро-триумф",
    "subtitle.refurbished_furniture.ui.paddle_ball.retro_lose": "Ретро-поражение",

    # Single blocks
    "block.refurbished_furniture.workbench": "Верстак мебели",
    "block.refurbished_furniture.frying_pan": "Сковорода",
    "block.refurbished_furniture.doorbell": "Дверной звонок",
    "block.refurbished_furniture.recycle_bin": "Утилизатор",
    "block.refurbished_furniture.plate": "Тарелка",
    "block.refurbished_furniture.television": "Телевизор",
    "block.refurbished_furniture.computer": "Компьютер",
    "block.refurbished_furniture.door_mat": "Дверной коврик",
    "block.refurbished_furniture.milk": "Молоко",

    # Appliances
    "block.refurbished_furniture.light_fridge": "Светлый холодильник",
    "block.refurbished_furniture.dark_fridge": "Тёмный холодильник",
    "block.refurbished_furniture.light_freezer": "Светлый морозильник",
    "block.refurbished_furniture.dark_freezer": "Тёмный морозильник",
    "block.refurbished_furniture.light_toaster": "Светлый тостер",
    "block.refurbished_furniture.dark_toaster": "Тёмный тостер",
    "block.refurbished_furniture.light_microwave": "Светлая микроволновка",
    "block.refurbished_furniture.dark_microwave": "Тёмная микроволновка",
    "block.refurbished_furniture.light_stove": "Светлая кухонная плита",
    "block.refurbished_furniture.dark_stove": "Тёмная кухонная плита",
    "block.refurbished_furniture.light_lightswitch": "Светлый выключатель света",
    "block.refurbished_furniture.dark_lightswitch": "Тёмный выключатель света",
    "block.refurbished_furniture.light_ceiling_light": "Светлый потолочный светильник",
    "block.refurbished_furniture.dark_ceiling_light": "Тёмный потолочный светильник",
    "block.refurbished_furniture.light_electricity_generator": "Светлый электрогенератор",
    "block.refurbished_furniture.dark_electricity_generator": "Тёмный электрогенератор",
    "block.refurbished_furniture.light_range_hood": "Светлая кухонная вытяжка",
    "block.refurbished_furniture.dark_range_hood": "Тёмная кухонная вытяжка",
    
    # Stepping stones
    "block.refurbished_furniture.stone_stepping_stones": "Каменная тропинка",
    "block.refurbished_furniture.andesite_stepping_stones": "Андезитовая тропинка",
    "block.refurbished_furniture.diorite_stepping_stones": "Диоритовая тропинка",
    "block.refurbished_furniture.granite_stepping_stones": "Гранитная тропинка",
    "block.refurbished_furniture.deepslate_stepping_stones": "Сланцевая тропинка",
}

# Auto-generate wooden and colored block translations
for k, v in en.items():
    if k in MANUAL:
        continue
    
    if k.startswith("block.refurbished_furniture."):
        suffix = k.replace("block.refurbished_furniture.", "")
        
        # Check wood prefix
        wood_prefix = None
        for w in WOOD_MAP.keys():
            if suffix.startswith(w + "_"):
                wood_prefix = w
                break
        
        # Check color prefix
        color_prefix = None
        for c in COLOR_MAP.keys():
            if suffix.startswith(c + "_"):
                color_prefix = c
                break
                
        if wood_prefix:
            rest = suffix[len(wood_prefix)+1:]
            wm = WOOD_MAP[wood_prefix]
            wf = WOOD_FEM_MAP[wood_prefix]
            wn = WOOD_NEU_MAP[wood_prefix]
            wg = WOOD_GEN_MAP[wood_prefix]
            
            if rest == "table":
                MANUAL[k] = f"{wm} стол"
            elif rest == "chair":
                MANUAL[k] = f"{wm} стул"
            elif rest == "desk":
                MANUAL[k] = f"{wm} письменный стол"
            elif rest == "drawer":
                MANUAL[k] = f"{wm} комод"
            elif rest == "crate":
                MANUAL[k] = f"{wm} ящик"
            elif rest == "cutting_board":
                MANUAL[k] = f"{wf} разделочная доска"
            elif rest == "storage_jar":
                MANUAL[k] = f"{wf} банка для хранения"
            elif rest == "storage_cabinet":
                MANUAL[k] = f"{wm} шкаф для хранения"
            elif rest == "kitchen_cabinetry":
                MANUAL[k] = f"{wm} кухонный шкафчик"
            elif rest == "kitchen_storage_cabinet":
                MANUAL[k] = f"{wm} кухонный шкафчик для хранения"
            elif rest == "kitchen_drawer":
                MANUAL[k] = f"{wm} кухонный комод"
            elif rest == "kitchen_sink":
                MANUAL[k] = f"{wf} кухонная раковина"
            elif rest == "basin":
                MANUAL[k] = f"{wm} умывальник ({wg})"
            elif rest == "bath":
                MANUAL[k] = f"{wf} ванна ({wg})"
            elif rest == "toilet":
                MANUAL[k] = f"{wm} унитаз ({wg})"
            elif rest == "mail_box" or rest == "mailbox":
                MANUAL[k] = f"{wm} почтовый ящик"
            elif rest == "lattice_fence":
                MANUAL[k] = f"{wm} решётчатый забор"
            elif rest == "lattice_fence_gate":
                MANUAL[k] = f"{wf} решётчатая калитка ({wg})"
            elif rest == "hedge":
                MANUAL[k] = f"{wf} живая изгородь ({wg})"
            elif rest == "light_ceiling_fan":
                MANUAL[k] = f"{wm} светлый потолочный вентилятор ({wg})"
            elif rest == "dark_ceiling_fan":
                MANUAL[k] = f"{wm} тёмный потолочный вентилятор ({wg})"
            else:
                print(f"Unknown wood rest: {rest} for {k}")

        elif color_prefix:
            rest = suffix[len(color_prefix)+1:]
            cm = COLOR_MAP[color_prefix]
            cf = COLOR_FEM_MAP[color_prefix]
            cn = COLOR_NEU_MAP[color_prefix]
            
            if rest == "grill":
                MANUAL[k] = f"{cm} гриль"
            elif rest == "cooler":
                MANUAL[k] = f"{cm} переносной холодильник"
            elif rest == "sofa":
                MANUAL[k] = f"{cm} диван"
            elif rest == "lamp":
                MANUAL[k] = f"{cf} лампа"
            elif rest == "trampoline":
                MANUAL[k] = f"{cm} батут"
            elif rest == "stool":
                MANUAL[k] = f"{cm} табурет"
            elif rest == "kitchen_cabinetry":
                MANUAL[k] = f"{cm} кухонный шкафчик"
            elif rest == "kitchen_drawer":
                MANUAL[k] = f"{cm} кухонный комод"
            elif rest == "kitchen_sink":
                MANUAL[k] = f"{cf} кухонная раковина"
            elif rest == "kitchen_storage_cabinet":
                MANUAL[k] = f"{cm} кухонный шкафчик для хранения"
            elif rest == "toilet":
                MANUAL[k] = f"{cm} унитаз"
            elif rest == "basin":
                MANUAL[k] = f"{cm} умывальник"
            elif rest == "bath":
                MANUAL[k] = f"{cf} ванна"
            else:
                print(f"Unknown color rest: {rest} for {k}")

# Other specific blocks
MANUAL["block.refurbished_furniture.post_box"] = "Почтовый ящик"
MANUAL["block.refurbished_furniture.azalea_hedge"] = "Азалиевая живая изгородь"
MANUAL["container.refurbished_furniture.fridge"] = "Холодильник"
MANUAL["container.refurbished_furniture.mailbox"] = "Почтовый ящик"

print(f"Total translations generated: {len(MANUAL)} / {len(en)}")
missing_after = [k for k in en if k not in MANUAL]
if missing_after:
    print(f"Missing after auto-gen ({len(missing_after)}):")
    for m in missing_after:
        print(f"  {m} = {en[m]}")
else:
    print("ALL 652 KEYS COVERED!")
