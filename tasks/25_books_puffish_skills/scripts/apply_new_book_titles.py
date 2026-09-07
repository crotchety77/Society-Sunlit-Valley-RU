import os, json, sys

sys.stdout.reconfigure(encoding='utf-8')

workspace = r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода'

books_mapping = [
  ("alias_moss", "Прорастание"),
  ("animal_fancy", "Журнал «В мире животных»"),
  ("banana_karenina", "Шимпанзини Бананини"),
  ("brine_and_punishment", "Дикий огурец"),
  ("bluegill_meridian", "Синежаберный меридиан"),
  ("bullfish_jobs", "Потомки скажут спасибо"),
  ("canadian_and_famous", "Канадский и знаменитый"),
  ("first_aid_guide", "Руководство по первой помощи"),
  ("hitting_hard_and_soft", "Бить сильно и нежно"),
  ("no_name_for_the_sheep", "Овца, назови себя"),
  ("intro_to_algorithms", "Добыча свинца без последствий"),
  ("paradise_crop", "Райский урожай"),
  ("slouching_towards_artistry", "Искусство экономить"),
  ("debt_caverns", "Долговая бездна"),
  ("frogs_bounty_bazaar", "Лягушачья ярмарка щедрости"),
  ("phenomenology_of_treasure", "Феноменальные сокровища"),
  ("slime_contain_protect", "Слаймик. Спрятать. Сберечь."),
  ("the_spark_also_rises", "И рождается искра"),
  ("universal_methods_of_farming", "Круглый год фермерства"),
  ("wuthering_logs", "Бурелом"),
  ("pond_house_five", "Бойня номер пруд"),
  ("the_quality_of_the_earth", "Благодатная почва"),
  ("the_red_and_the_black", "Красное или чёрное"),
  ("women_who_run_with_the_plushies", "Плюшевый бум лабубум"),
  ("the_metamorphosize", "Метаморфозы")
]

# 1. Update translations/society/ru_ru.json
society_path = os.path.join(workspace, 'translations', 'society', 'ru_ru.json')
with open(society_path, 'r', encoding='utf-8') as f:
    soc_data = json.load(f)

for book_id, new_name in books_mapping:
    soc_data[f"item.society.{book_id}"] = new_name

with open(society_path, 'w', encoding='utf-8') as f:
    json.dump(soc_data, f, ensure_ascii=False, indent=2)

# 2. Update translations/skills/ru_ru.json
skills_path = os.path.join(workspace, 'translations', 'skills', 'ru_ru.json')
with open(skills_path, 'r', encoding='utf-8') as f:
    skills_data = json.load(f)

for book_id, new_name in books_mapping:
    skills_data[f"society_skills.books.{book_id}.title"] = new_name

with open(skills_path, 'w', encoding='utf-8') as f:
    json.dump(skills_data, f, ensure_ascii=False, indent=2)

print("✅ Обновлено название: no_name_for_the_sheep -> Овца, назови себя")
