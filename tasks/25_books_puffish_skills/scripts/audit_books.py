import os, json, sys

sys.stdout.reconfigure(encoding='utf-8')

workspace = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
kubejs_dir = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs'
if not os.path.exists(kubejs_dir):
    kubejs_dir = os.path.join(workspace, 'game_data')

books = [
  ('alias_moss', 'Мох-имитатор'),
  ('animal_fancy', 'Журнал «Мир животных»'),
  ('banana_karenina', 'Бананина Каренина'),
  ('brine_and_punishment', 'Рассол и наказание'),
  ('bluegill_meridian', 'Синежаберный меридиан'),
  ('bullfish_jobs', 'Бычьи дела (Работа Бычка)'),
  ('canadian_and_famous', 'Канадский и знаменитый'),
  ('first_aid_guide', 'Руководство по первой помощи'),
  ('hitting_hard_and_soft', 'Бить сильно и мягко'),
  ('no_name_for_the_sheep', 'Безымянная овца'),
  ('intro_to_algorithms', 'Введение в алгоритмы'),
  ('paradise_crop', 'Райский урожай'),
  ('slouching_towards_artistry', 'Ползком к искусству'),
  ('debt_caverns', 'Пещеры долгов'),
  ('frogs_bounty_bazaar', 'Базар лягушачьей щедрости'),
  ('phenomenology_of_treasure', 'Феноменология сокровищ'),
  ('slime_contain_protect', 'Слизь. Содержание. Защита.'),
  ('the_spark_also_rises', 'И восходит искра'),
  ('universal_methods_of_farming', 'Универсальные методы фермерства'),
  ('wuthering_logs', 'Грозовые бревна'),
  ('pond_house_five', 'Бойня номер пруд'),
  ('the_quality_of_the_earth', 'Качество земли'),
  ('the_red_and_the_black', 'Красное и чёрное'),
  ('women_who_run_with_the_plushies', 'Бегущая с плюшевыми игрушками'),
  ('the_metamorphosize', 'Метаморфоза')
]

print("=" * 60)
print("📚 АУДИТ 25 КНИГ НАВЫКОВ (PUFFISH SKILLS -> SOCIETY:BOOKS)")
print("=" * 60)

# 1. Prize Machine
pm_file = os.path.join(kubejs_dir, 'startup_scripts/customMachines/prizeMachine.js')
pm_content = open(pm_file, 'r', encoding='utf-8', errors='ignore').read() if os.path.exists(pm_file) else ""

# 2. Book Fair
bf_file = os.path.join(kubejs_dir, 'data/society_trading/shops/book_fair.json')
bf_trades = {}
if os.path.exists(bf_file):
    bf_data = json.load(open(bf_file, 'r', encoding='utf-8'))
    for t in bf_data.get('trades', []):
        item = t.get('offer', {}).get('item', '')
        req = t.get('request', {})
        stage = t.get('stage_required', '')
        cost = f"{req.get('count', 1)}x {req.get('item', '').split(':')[-1]}"
        if stage:
            cost += f" (Требует: {stage})"
        bf_trades[item] = cost

for b, ru_name in books:
    full_id = f"society:{b}"
    print(f"\n[{ru_name}] (`{full_id}`)")
    
    # Book fair
    if full_id in bf_trades:
        print(f"  • Книжная ярмарка: {bf_trades[full_id]}")
    else:
        print(f"  • Книжная ярмарка: Не продаётся")
        
    # Prize machine
    pm_c = pm_content.count(full_id)
    if pm_c > 0:
        print(f"  • Призовой автомат: Да ({pm_c} в пуле)")
    else:
        print(f"  • Призовой автомат: Нет")
