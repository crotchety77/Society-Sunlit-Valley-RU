import os, json, sys

sys.stdout.reconfigure(encoding='utf-8')

workspace = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
society_json_path = os.path.join(workspace, 'translations', 'society', 'ru_ru.json')
skills_json_path = os.path.join(workspace, 'translations', 'skills', 'ru_ru.json')

# 25 Books with base description and dark gray acquisition note (\n\n§8...§r)
book_data = {
  "alias_moss": {
    "desc": "Моховые ягоды можно найти в любой сезон.",
    "source": "§8Добыча: Рубка деревьев осенью (0.5%%), обмен у Мудрого Дуба или Книжная ярмарка.§r"
  },
  "animal_fancy": {
    "desc": "Увеличивает привязанность, получаемую при поглаживании сельхозживотных.",
    "source": "§8Добыча: Жёлтые воздушные шары, Призовой автомат или Книжная ярмарка.§r"
  },
  "banana_karenina": {
    "desc": "Удваивает выход плодов бананового дерева.",
    "source": "§8Добыча: Сбор спелых бананов с деревьев (1%%), Призовой автомат или Книжная ярмарка.§r"
  },
  "brine_and_punishment": {
    "desc": "Соленья стоят на 100%% дороже.",
    "source": "§8Добыча: Сбор огурцов с грядок (1%%), Призовой автомат или Книжная ярмарка.§r"
  },
  "bluegill_meridian": {
    "desc": "Синежаберник теперь стоит 666 §f●§r.",
    "source": "§8Добыча: Рыбалка в водных кругах (10%%), Призовой автомат или Книжная ярмарка.§r"
  },
  "bullfish_jobs": {
    "desc": "Качество рыбы из садков зависит от популяции.",
    "source": "§8Добыча: Книжная ярмарка Библиотекаря в конце сезона (2 Нептуниевые монеты).§r"
  },
  "canadian_and_famous": {
    "desc": "Сборщики смолы дают двойной результат. Не влияет на автоматические сборщики.",
    "source": "§8Добыча: Призовой автомат или Книжная ярмарка (1 Sun).§r"
  },
  "first_aid_guide": {
    "desc": "Вдвое снижает максимальную комиссию и долг после смерти.",
    "source": "§8Добыча: Оплата счёта в больнице при гибели (1%%), Жёлтые шары или Призовой автомат.§r"
  },
  "hitting_hard_and_soft": {
    "desc": "Атаки ближнего боя наносят на 4 единицы урона больше.",
    "source": "§8Добыча: Зловещие спавнеры Испытаний (~5%%), Призовой автомат или Книжная ярмарка.§r"
  },
  "no_name_for_the_sheep": {
    "desc": "Именование животных даёт дополнительное сердечко привязанности.",
    "source": "§8Добыча: Призовой автомат или Книжная ярмарка.§r"
  },
  "intro_to_algorithms": {
    "desc": "Добыча свинцовой руды больше не вызывает облака ядовитого газа.",
    "source": "§8Добыча: Добыча свинца (0.5%%), Тайники реликвий/артефактов (5%%) или Призовой автомат.§r"
  },
  "paradise_crop": {
    "desc": "+1 к выходу урожая при сборе.",
    "source": "§8Добыча: Раскопки земляных кучек лопатой (2%%), Жёлтые шары или Призовой автомат.§r"
  },
  "slouching_towards_artistry": {
    "desc": "Ремесленные воронки имеют +5%% шанс не потреблять Искрокамень за каждый день производства.",
    "source": "§8Добыча: 5 сердец дружбы с Банкиром Леоном, Призовой автомат или Книжная ярмарка.§r"
  },
  "debt_caverns": {
    "desc": "Обморок в Пещере Черепа больше не влечёт за собой штрафы или рост долга.",
    "source": "§8Добыча: 5 сердец дружбы с Библиотекарем, Чернитовые валуны (0.1%%) или Обморок в 6:00 (2%%).§r"
  },
  "frogs_bounty_bazaar": {
    "desc": "Призовые билеты дают двойные призы.",
    "source": "§8Добыча: Доска объявлений (Bountiful), Призовой автомат или Книжная ярмарка.§r"
  },
  "phenomenology_of_treasure": {
    "desc": "Артефакты и реликвии стоят на 200%% дороже.",
    "source": "§8Добыча: Тайники реликвий и артефактов в Раскалывателе (5%%), Призовой автомат или Ярмарка.§r"
  },
  "slime_contain_protect": {
    "desc": "Инкубация Сердца слизня даёт шанс получить Слизневый билет.",
    "source": "§8Добыча: Инкубатор слизи при закладке Сердца слизня (15%%) или Книжная ярмарка.§r"
  },
  "the_spark_also_rises": {
    "desc": "Добыча любой руды даёт Искрокамень.\n§6Требуется разблокированное Мастерство шахтёрства§r",
    "source": "§8Добыча: Руда искрокамня с Мастерством шахтёрства (0.1%%) или Книжная ярмарка.§r"
  },
  "universal_methods_of_farming": {
    "desc": "Рынок продаёт все базовые семена в любом сезоне.",
    "source": "§8Добыча: 5 сердец дружбы с Кэролайн с рынка или Книжная ярмарка.§r"
  },
  "wuthering_logs": {
    "desc": "У деревьев есть 15%% шанс при рубке дать Поленья.",
    "source": "§8Добыча: Рубка любых деревьев топором (0.5%%) или Книжная ярмарка.§r"
  },
  "pond_house_five": {
    "desc": "Рыбные садки требуют в два раза меньше предметов.\n§6Требуется разблокированное Мастерство рыболовства§r",
    "source": "§8Добыча: Книжная ярмарка (1 Prismatic Coin, требует Мастерство рыбалки).§r"
  },
  "the_quality_of_the_earth": {
    "desc": "Влияние качества на цену нерыбной фермерской продукции удваивается.\n§6Требуется разблокированное Мастерство фермерства§r",
    "source": "§8Добыча: Книжная ярмарка (1 Neptunium Coin, требует Мастерство фермерства).§r"
  },
  "the_red_and_the_black": {
    "desc": "Жеоды, ящики с добычей и игровые автоматы дают на один предмет больше.\n§6Требуется разблокированное Мастерство искателя приключений§r",
    "source": "§8Добыча: Джекпот в Игровом автомате с Мастерством приключений (5%%) или Ярмарка.§r"
  },
  "women_who_run_with_the_plushies": {
    "desc": "Плюшевые игрушки начинают с 2 сердечек привязанности.\n§6Требуется разблокированное Мастерство животноводства§r",
    "source": "§8Добыча: Книжная ярмарка (2 Neptunium Coin, требует Мастерство животноводства).§r"
  },
  "the_metamorphosize": {
    "desc": "Влияние размера на цену бабочек и мотыльков утраивается.",
    "source": "§8Добыча: Книжная ярмарка Библиотекаря в конце сезона (12 Sun).§r"
  }
}

# 1. Update translations/skills/ru_ru.json (Puffish Skills GUI tree)
with open(skills_json_path, 'r', encoding='utf-8') as f:
    skills_data = json.load(f)

for book_id, info in book_data.items():
    key = f"society_skills.books.{book_id}.description"
    skills_data[key] = f"{info['desc']}\n\n{info['source']}"

with open(skills_json_path, 'w', encoding='utf-8') as f:
    json.dump(skills_data, f, ensure_ascii=False, indent=2)

print(f"✅ Обновлены ячейки Puffish Skills ({len(book_data)} шт.) в {skills_json_path}")

# 2. Update translations/society/ru_ru.json (Item tooltips)
with open(society_json_path, 'r', encoding='utf-8') as f:
    society_data = json.load(f)

for book_id, info in book_data.items():
    key = f"item.society.{book_id}.description"
    society_data[key] = f"{info['desc']}\n\n{info['source']}"

with open(society_json_path, 'w', encoding='utf-8') as f:
    json.dump(society_data, f, ensure_ascii=False, indent=2)

print(f"✅ Обновлены описания предметов ({len(book_data)} шт.) в {society_json_path}")
