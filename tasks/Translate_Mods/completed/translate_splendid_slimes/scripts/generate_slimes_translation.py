import json
import os
import sys
import zipfile

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')


jars = [
    r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\mods\splendid_slimes-0.20.5.jar',
    r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\mods\create_slime-1.0.1.jar'
]

all_en = {}
for j in jars:
    with zipfile.ZipFile(j, 'r') as z:
        for n in z.namelist():
            if 'lang/en_us.json' in n:
                data = json.loads(z.read(n).decode('utf-8'))
                all_en.update(data)

# High quality Russian translation mapping
ru_map = {
    # Item groups & keys
    "itemGroup.splendid_slimes": "«Замечательные слизни»",
    "key.categories.splendid_slimes": "Замечательные слизни",
    "key.splendid_slimes.slime_vac_mode": "Сменить режим слаймопушки",

    # Advancements
    "splendid_slimes.advancement.root.title": "Замечательные слизни",
    "splendid_slimes.advancement.root.description": "Разведение слизней ради ценных ресурсов!",
    "splendid_slimes.advancement.obtain_corral.title": "Загон для слизней",
    "splendid_slimes.advancement.obtain_corral.description": "Используйте блоки загона, чтобы удерживать слизней",
    "splendid_slancement.obtain_corral.description": "Используйте блоки загона, чтобы удерживать слизней",
    "splendid_slimes.advancement.obtain_incubator.title": "Рождение слизня",
    "splendid_slimes.advancement.obtain_incubator.description": "Создайте инкубатор, чтобы вырастить слизня из сердца",
    "splendid_slimes.advancement.obtain_plort.title": "Слаймовые... отходы?",
    "splendid_slimes.advancement.obtain_plort.description": "Покормите слизня и соберите плорт",
    "splendid_slimes.advancement.obtain_press.title": "Впечатляющее прессование",
    "splendid_slimes.advancement.obtain_press.description": "Создайте пресс плортов, чтобы спрессовать сердце слизня",
    "splendid_slimes.advancement.obtain_rippit.title": "Переработка на максимум!",
    "splendid_slimes.advancement.obtain_rippit.description": "Создайте переработчик плортов для добычи полезных ресурсов",
    "splendid_slimes.advancement.obtain_feeder.title": "Голодный, голодный слайм",
    "splendid_slimes.advancement.obtain_feeder.description": "Создайте кормушку для автоматического кормления слизней со сложным рационом",

    # JEI Categories & UI
    "jei.splendid_slimes.category.slime_info": "Информация о слизнях",
    "jei.splendid_slimes.category.slime_traits": "Черты слизней",
    "jei.splendid_slimes.category.slime_incubating": "Инкубация слизней",
    "jei.splendid_slimes.category.slime_info.diet": "Рацион:",
    "jei.splendid_slimes.category.slime_incubation.incubation_time": "Время инкубации: %s сек.",
    "jei.splendid_slimes.plort_rippit.chance": "Шанс: %s",
    "jei.splendid_slimes.category.slime_traits.none": "У слизня нет особых черт",
    "config.jade.plugin_splendid_slimes.splendid_slime": "Слизни Splendid Slimes",

    # Core Blocks & Items
    "block.splendid_slimes.corral_block": "Блок загона для слизней",
    "block.splendid_slimes.slime_incubator": "Инкубатор слизней",
    "block.splendid_slimes.plort_press": "Пресс плортов",
    "block.splendid_slimes.plort_rippit": "Переработчик плортов",
    "block.splendid_slimes.slime_feeder": "Кормушка для слизней",
    "block.splendid_slimes.rocket_pod": "Ракетная грузовая капсула",
    "item.splendid_slimes.slime_vac": "Слаймовый вакуумник (Слаймопушка)",
    "item.splendid_slimes.slime_inspector": "Анализатор слизней",
    "item.splendid_slimes.slime_cookie": "Печенье со слизью",

    # Info messages
    "info.splendid_slimes.slime_inspector.all_good": "Ваш слизень весело хлюпает и абсолютно доволен!",
    "info.splendid_slimes.slime_inspector.not_happy": "Ваш слизень крайне недоволен условиями жизни...",

    # Diets
    "diet.splendid_slimes.default_diet": "Любая еда",
    "diet.splendid_slimes.all_seeing": "Овощи",
    "diet.splendid_slimes.bear": "Мёд и рыба",
    "diet.splendid_slimes.bitwise": "Древесина и брёвна",
    "diet.splendid_slimes.blazing": "Приготовленное мясо",
    "diet.splendid_slimes.bony": "Молоко и кости",
    "diet.splendid_slimes.boomcat": "Мясо",
    "diet.splendid_slimes.dusty": "Песок и кактусы",
    "diet.splendid_slimes.ender": "Драгоценные камни",
    "diet.splendid_slimes.gold": "Металлические слитки",
    "diet.splendid_slimes.juicy": "Ягоды и фрукты",
    "diet.splendid_slimes.luminous": "Кварц и светокамень",
    "diet.splendid_slimes.mechanic": "Камни и сырая руда",
    "diet.splendid_slimes.minty": "Останки монстров",
    "diet.splendid_slimes.orby": "Монстры и животные",
    "diet.splendid_slimes.phantom": "Кровати и шерсть",
    "diet.splendid_slimes.prisma": "Призмарин и рыба",
    "diet.splendid_slimes.puddle": "Рыба",
    "diet.splendid_slimes.rotting": "Гнилая плоть и свежее мясо",
    "diet.splendid_slimes.shulking": "Плоды хоруса",
    "diet.splendid_slimes.slimy": "Цветы и растения",
    "diet.splendid_slimes.sparkcat": "Рыба и мясо",
    "diet.splendid_slimes.sweet": "Сладкие фрукты и сахар",
    "diet.splendid_slimes.webby": "Овощи и паутина",
    "diet.splendid_slimes.weeping": "Адские грибы и фрукты",

    # Slime Names
    "slime.splendid_slimes.all_seeing": "Всевидящий слизень",
    "slime.splendid_slimes.bear": "Медвежий слизень",
    "slime.splendid_slimes.bitwise": "Битовый слизень",
    "slime.splendid_slimes.blazing": "Огненный слизень",
    "slime.splendid_slimes.bony": "Костяной слизень",
    "slime.splendid_slimes.boomcat": "Слизень Кот-бум",
    "slime.splendid_slimes.dusty": "Пыльный слизень",
    "slime.splendid_slimes.ender": "Эндер-слизень",
    "slime.splendid_slimes.gold": "Золотой слизень",
    "slime.splendid_slimes.juicy": "Сочный слизень",
    "slime.splendid_slimes.luminous": "Светящийся слизень",
    "slime.splendid_slimes.mechanic": "Механический слизень",
    "slime.splendid_slimes.minty": "Мятный слизень",
    "slime.splendid_slimes.orby": "Сферический слизень",
    "slime.splendid_slimes.phantom": "Фантомный слизень",
    "slime.splendid_slimes.prisma": "Призмариновый слизень",
    "slime.splendid_slimes.puddle": "Слизень-лужица",
    "slime.splendid_slimes.rotting": "Гниющий слизень",
    "slime.splendid_slimes.shulking": "Шалкеровый слизень",
    "slime.splendid_slimes.slimy": "Классический слизень",
    "slime.splendid_slimes.sparkcat": "Слизень Искрокот",
    "slime.splendid_slimes.sweet": "Сладкий слизень",
    "slime.splendid_slimes.webby": "Паутинный слизень",
    "slime.splendid_slimes.weeping": "Плачущий слизень",

    # Slime Info (Slimepedia in JEI)
    "slime.splendid_slimes.all_seeing.info": "Может предсказать вашу судьбу, но не способен передать её словами.",
    "slime.splendid_slimes.bear.info": "Обожает сладкий мёд и крепко спит в уютных прохладных уголках.",
    "slime.splendid_slimes.bitwise.info": "С уважением относится к вашим редстоун-схемам и не ломает их, даже если рассержен.",
    "slime.splendid_slimes.blazing.info": "Эти слизни холодны на ощупь и черпают всё своё тепло исключительно из окружающей среды.",
    "slime.splendid_slimes.bony.info": "Совершенно не умеет пить молоко, не поглотив вместе с ним само ведро...",
    "slime.splendid_slimes.boomcat.info": "Самый популярный домашний слизень. Также главный виновник разбитых мензурок и посуды.",
    "slime.splendid_slimes.dusty.info": "Прячется в песках пустынь, укутываясь в лёгкую песчаную пыль.",
    "slime.splendid_slimes.ender.info": "При сильном раздражении вызывает локальные пространственные искажения.",
    "slime.splendid_slimes.gold.info": "Эти слизни всем сердцем тоскуют по глубоким золотым шахтам...",
    "slime.splendid_slimes.juicy.info": "Переполнен сладким ягодным соком и источает свежий фруктовый аромат.",
    "slime.splendid_slimes.luminous.info": "Не выключайте свет! Эти малыши панически боятся темноты...",
    "slime.splendid_slimes.mechanic.info": "С радостью помог бы вам со станками, но ему не хватает сил крутить их шестерни.",
    "slime.splendid_slimes.minty.info": "Питается исключительно монстрами, поэтому разводить его — дело тонкое и рискованное.",
    "slime.splendid_slimes.orby.info": "Пока никто не смотрит, расставляет книги по нелепой «Слизневой десятичной системе».",
    "slime.splendid_slimes.phantom.info": "Счастливые слизни часто забирают плохие сны у тех, кто спит рядом с ними.",
    "slime.splendid_slimes.prisma.info": "Более упругий родственник слизня-лужицы, неравнодушный к ярким морским цветам.",
    "slime.splendid_slimes.puddle.info": "Обожает плавать в воде! Вот только плавать совершенно не умеет...",
    "slime.splendid_slimes.rotting.info": "Часто водится за ресторанными мусорными баками. Дружит с енотами!",
    "slime.splendid_slimes.shulking.info": "Приручённых шалкеровых слизней часто используют спасатели для подъёма завалов.",
    "slime.splendid_slimes.slimy.info": "Самый базовый и дружелюбный слизень. Идеален для начинающих слаймоводов!",
    "slime.splendid_slimes.sparkcat.info": "Энергичный кошачий слизень, вырабатывающий искры статического электричества.",
    "slime.splendid_slimes.sweet.info": "Сладкоежки будут не прочь откусить кусочек от его мятного леденцового бантика.",
    "slime.splendid_slimes.webby.info": "Его плорты используются искусными портными для создания тончайших изысканных тканей.",
    "slime.splendid_slimes.weeping.info": "Предок Кота-бума, угодивший в Незер и сумевший приспособиться к его суровому пеклу.",

    # Traits (Names & Info)
    "trait.splendid_slimes.aquatic.name": "Водный",
    "trait.splendid_slimes.aquatic.info": "Тонет в воде и чувствует себя несчастным на суше.",
    "trait.splendid_slimes.defiant.name": "Непокорный",
    "trait.splendid_slimes.defiant.info": "Имеет шанс пережить смертельный удар; шанс тем выше, чем сильнее был урон.",
    "trait.splendid_slimes.explosive.name": "Взрывной",
    "trait.splendid_slimes.explosive.info": "Когда голоден, периодически создаёт взрывы без разрушения блоков. Частота растёт с голодом.",
    "trait.splendid_slimes.feral.name": "Дикий",
    "trait.splendid_slimes.feral.info": "Всегда проявляет агрессию и атакует игрока.",
    "trait.splendid_slimes.flaming.name": "Огненный",
    "trait.splendid_slimes.flaming.info": "Поджигает существ при касании и периодически оставляет огонь, особенно когда голоден.",
    "trait.splendid_slimes.floating.name": "Парящий",
    "trait.splendid_slimes.floating.info": "Периодически зависает в воздухе и левитирует несколько секунд.",
    "trait.splendid_slimes.foodporting.name": "Телепортация к еде",
    "trait.splendid_slimes.foodporting.info": "Мгновенно телепортируется к еде или целям, которых собирается съесть.",
    "trait.splendid_slimes.handy.name": "Ловкий",
    "trait.splendid_slimes.handy.info": "Может удерживать в руках предмет. Выбрасывает его при гибели или разделении.",
    "trait.splendid_slimes.inverse.name": "Инверсивный",
    "trait.splendid_slimes.inverse.info": "Положительные эффекты срабатывают от недовольства, а негативные — от радости.",
    "trait.splendid_slimes.largoless.name": "Негибридный",
    "trait.splendid_slimes.largoless.info": "Не может превратиться в Ларго. Его плорты не создают гибридов из других слизней.",
    "trait.splendid_slimes.moody.name": "Капризный",
    "trait.splendid_slimes.moody.info": "Любые изменения настроения (радость и грусть) удваиваются по силе.",
    "trait.splendid_slimes.nuclear.name": "Ядерный",
    "trait.splendid_slimes.nuclear.info": "В состоянии ярости взрывается разрушительным взрывом, ломающим блоки вокруг.",
    "trait.splendid_slimes.photosynthesizing.name": "Фотосинтезирующий",
    "trait.splendid_slimes.photosynthesizing.info": "Впадает в уныние, если долго находится вдали от прямого солнечного света.",
    "trait.splendid_slimes.picky.name": "Привередливый",
    "trait.splendid_slimes.picky.info": "Будучи Ларго, злится, если его дважды подряд покормить едой одного и того же типа.",
    "trait.splendid_slimes.putrid.name": "Токсичный",
    "trait.splendid_slimes.putrid.info": "Усиливает эффекты и вдвое увеличивает их длительность.",
    "trait.splendid_slimes.spiky.name": "Колючий",
    "trait.splendid_slimes.spiky.info": "Наносит урон игрокам и мобам при физическом контакте.",
    "trait.splendid_slimes.weeping.name": "Плачущий",
    "trait.splendid_slimes.weeping.info": "Периодически горько плачет, заполняя пространство водой. Если воде некуда течь, расстраивается ещё сильнее.",
    "trait.splendid_slimes.dominant.name": "Доминантный",
    "trait.splendid_slimes.dominant.info": "При превращении в Ларго питается строго только своей исходной диетой.",
    "trait.splendid_slimes.recessive.name": "Рецессивный",
    "trait.splendid_slimes.recessive.info": "При превращении в Ларго полностью отказывается от своей исходной диеты в пользу второй.",
    "trait.splendid_slimes.friendly.name": "Дружелюбный",
    "trait.splendid_slimes.friendly.info": "Любит компанию и везде следует за ближайшими игроками.",
    "trait.splendid_slimes.diverse.name": "Общительный",
    "trait.splendid_slimes.diverse.info": "Расстраивается, если рядом с ним нет как минимум 3 уникальных видов других слизней.",
    "trait.splendid_slimes.pompous.name": "Высокомерный",
    "trait.splendid_slimes.pompous.info": "Любимая еда больше не заставляет его производить двойное количество плортов.",
    "trait.splendid_slimes.ravenous.name": "Ненасытный",
    "trait.splendid_slimes.ravenous.info": "Производит плорты, только когда шкала сытости полна. Разная еда насыщает по-разному.",
    "trait.splendid_slimes.wormhole.name": "Червоточина",
    "trait.splendid_slimes.wormhole.info": "В расстроенных чувствах периодически притягивает и телепортирует к себе сущностей.",
    "trait.splendid_slimes.necromancer.name": "Некромант",
    "trait.splendid_slimes.necromancer.info": "При атаке призывает слизневых зомби. Всегда враждебен к деревенским жителям."
}

# Auto generate names for Plorts, Slime Blocks, Hearts, Jarred Slimes, and Entities
slime_types = [
    ('all_seeing', 'Всевидящий'), ('bear', 'Медвежий'), ('bitwise', 'Битовый'),
    ('blazing', 'Огненный'), ('bony', 'Костяной'), ('boomcat', 'Кот-бум'),
    ('dusty', 'Пыльный'), ('ender', 'Эндер'), ('gold', 'Золотой'),
    ('juicy', 'Сочный'), ('luminous', 'Светящийся'), ('mechanic', 'Механический'),
    ('minty', 'Мятный'), ('orby', 'Сферический'), ('phantom', 'Фантомный'),
    ('prisma', 'Призмариновый'), ('puddle', 'Лужица'), ('rotting', 'Гниющий'),
    ('shulking', 'Шалкеровый'), ('slimy', 'Классический'), ('sparkcat', 'Искрокот'),
    ('sweet', 'Сладкий'), ('webby', 'Паутинный'), ('weeping', 'Плачущий')
]

for code, name in slime_types:
    ru_map[f"item.splendid_slimes.{code}_plort"] = f"{name} плорт"
    ru_map[f"item.splendid_slimes.{code}_slime_heart"] = f"Сердце {name.lower()} слизня"
    ru_map[f"item.splendid_slimes.jarred_{code}_slime"] = f"{name} слизень в банке"
    ru_map[f"block.splendid_slimes.{code}_slime_block"] = f"{name} слаймовый блок"
    ru_map[f"entity.splendid_slimes.{code}_slime"] = f"{name} слизень"

# Extra missing keys
extra_keys = {
    "block.splendid_slimes.corral_pane": "Стеклянная панель загона",
    "block.splendid_slimes.slime_spawner": "Рассадник слизней",
    "block.splendid_slimes.slime_spawner.breed": "Порода: %s",
    "block.splendid_slimes.slime_spawner.breed_unset": "Порода не выбрана",
    "block.splendid_slimes.slime_spawner.slime_count": "Количество слизней: %s",
    "block.splendid_slimes.slime_incubator.progress": "Прогресс инкубации: %s",
    "block.splendid_slimes.slime_incubator.breed_unset": "Порода не выбрана",
    "entity.splendid_slimes.diet": "Рацион: %s",
    "entity.splendid_slimes.largo_diet": "Рацион Ларго: %s",
    "entity.splendid_slimes.largo_splendid_slime": "Слизень Ларго",
    "entity.splendid_slimes.splendid_slime": "Замечательный слизень",
    "entity.splendid_slimes.tarr": "Варр",
    "entity.splendid_slimes.sad": "Грустный",
    "entity.splendid_slimes.furious": "Яростный",
    "entity.splendid_slimes.happy": "Счастливый",
    "entity.splendid_slimes.neutral": "Спокойный",
    "entity.splendid_slimes.wild": "Дикий",
    "entity.splendid_slimes.hunger": "Голод: %s",
    "entity.splendid_slimes.owner": "Владелец: %s",
    "info.splendid_slimes.plort": "Используется для создания ядер и переработки в ресурсы",
    "info.splendid_slimes.slime_heart": "Поместите в инкубатор для выведения слизня",
    "info.splendid_slimes.slime_vac.shoot": "Выстрел (ПКМ)",
    "info.splendid_slimes.slime_vac.suck": "Засасывание (Зажмите ПКМ)",
    "info.splendid_slimes.slime_vac.mode": "Режим: %s",
    "info.splendid_slimes.slime_vac.mode_set": "Установлен режим: %s",
    "info.splendid_slimes.slime_inspector": "Анализ состояния слизня",
    "info.splendid_slimes.slime_inspector.suffocating": "Слизень задыхается! Ему не хватает воздуха!",
    "info.splendid_slimes.slime_inspector.crowded": "В загоне слишком тесно! Слизню нужно больше пространства.",
    "info.splendid_slimes.slime_inspector.aquatic_failure": "Водный слизень страдает без воды!",
    "info.splendid_slimes.slime_inspector.diverse_failure": "Слизню одиноко! Ему нужны соседи других пород.",
    "item.splendid_slimes.default_plort": "Плорт",
    "item.splendid_slimes.default_heart": "Сердце слизня",
    "item.splendid_slimes.default_slime_item": "Слизень в банке",
    "item.splendid_slimes.plort": "%s плорт",
    "item.splendid_slimes.slime_heart": "Сердце: %s",
    "item.splendid_slimes.slime_item": "%s в банке",
    "item.splendid_slimes.slime_item.tooltip_prompt": "§8Удерживайте [§7Shift§8] для информации о породе§r",
    "item.splendid_slimes.spawn_egg_splendid_slime": "Яйцо призыва замечательного слизня",
    "item.splendid_slimes.spawn_egg_tarr": "Яйцо призыва Варра",
    "item.splendid_slimes.rocket_pod": "Ракетная грузовая капсула",
    "item.splendid_slimes.slime_candy": "Слаймовая конфета"
}
ru_map.update(extra_keys)

# Filter ru_map to only keys present in all_en
final_translations = {k: ru_map[k] for k in all_en if k in ru_map}

print(f"Total keys translated: {len(final_translations)} / {len(all_en)}")

# Write to new_translate.md
task_dir = os.path.dirname(os.path.dirname(__file__))
new_translate_path = os.path.join(task_dir, "new_translate.md")

md_content = f"""# Локализация мода: Splendid Slimes (Замечательные слизни) (`splendid_slimes`)

**JAR:** `splendid_slimes-0.20.5.jar` + `create_slime-1.0.1.jar` | **Всего строк:** {len(final_translations)} | **Готово к применению:** {len(final_translations)}

## 1. Визуальный контекст и оформление

### Основные станки и предметы слаймоводства:
* **Инкубатор слизней** (`block.splendid_slimes.slime_incubator`) — выращивание слизней из сердец
* **Пресс плортов** (`block.splendid_slimes.plort_press`) — спрессовывание сердец
* **Переработчик плортов** (`block.splendid_slimes.plort_rippit`) — получение ресурсов из плортов
* **Кормушка для слизней** (`block.splendid_slimes.slime_feeder`) — автоматическое кормление
* **Слаймовый вакуумник (Слаймопушка)** (`item.splendid_slimes.slime_vac`) — отлов и выстрел слизнями
* **Анализатор слизней** (`item.splendid_slimes.slime_inspector`) — диагностика настроения и условий содержания

### Виды слизней (24 породы):
* *Всевидящий*, *Медвежий*, *Битовый*, *Огненный*, *Костяной*, *Кот-бум*, *Пыльный*, *Эндер*, *Золотой*, *Сочный*, *Светящийся*, *Механический*, *Мятный*, *Сферический*, *Фантомный*, *Призмариновый*, *Слизень-лужица*, *Гниющий*, *Шалкеровый*, *Классический*, *Искрокот*, *Сладкий*, *Паутинный*, *Плачущий*.

### Вкладки JEI:
* **Информация о слизнях** (Слаймопедия, рацион, любимая еда)
* **Черты слизней** (22 уникальных свойства: Водный, Взрывной, Парящий, Телепортация к еде, Доминантный и др.)
* **Инкубация слизней** (время выведения, шансы переработки плортов)

---

## 2. Предлагаемый перевод (JSON)

```json
{json.dumps(final_translations, ensure_ascii=False, indent=2)}
```
"""

with open(new_translate_path, 'w', encoding='utf-8') as f:
    f.write(md_content)

print(f"✅ new_translate.md успешно записан! ({len(final_translations)} ключей)")

